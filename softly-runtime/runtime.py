"""Softly Runtime Mini 0.1: ejecución de una operación de archivo autorizada."""

from __future__ import annotations

import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class RuntimeConfigurationError(Exception):
    """El manifiesto no cumple el contrato mínimo del runtime."""


class _PolicyDenied(Exception):
    """La solicitud no supera las reglas de autorización del runtime."""


class SoftlyRuntime:
    """Runtime mínimo con autorización explícita y workspace confinado.

    Esta implementación es un prototipo local. La resolución real de rutas
    bloquea traversal y symlinks que escapen del workspace, pero no reemplaza
    un sandbox del sistema operativo ni protege frente a carreras concurrentes
    o un proceso local comprometido.
    """

    def __init__(self, manifest_path: str | os.PathLike[str] | None = None) -> None:
        self.manifest_path = Path(manifest_path).resolve() if manifest_path else Path(__file__).resolve().parent / "manifest.json"
        self.runtime_dir = self.manifest_path.parent
        self.events_path = self.runtime_dir / "events.jsonl"
        self.repo_root = self.runtime_dir.parent.resolve()
        self.manifest = self._load_manifest()
        workspace_value = self.manifest["workspace"]
        self.workspace = (self.repo_root / workspace_value).resolve()
        try:
            self.workspace.relative_to(self.repo_root)
        except ValueError as exc:
            raise RuntimeConfigurationError("El workspace declarado sale de la raíz del proyecto.") from exc
        if self.workspace.exists() and not self.workspace.is_dir():
            raise RuntimeConfigurationError("La ruta del workspace existe y no es un directorio.")
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.workspace = self.workspace.resolve()
        try:
            self.workspace.relative_to(self.repo_root)
        except ValueError as exc:
            raise RuntimeConfigurationError("El workspace real sale de la raíz del proyecto.") from exc

    def _load_manifest(self) -> dict[str, Any]:
        try:
            data = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise RuntimeConfigurationError("No se pudo leer un manifiesto JSON válido.") from exc
        if not isinstance(data, dict):
            raise RuntimeConfigurationError("El manifiesto debe ser un objeto JSON.")
        task = data.get("task")
        allowed = data.get("allowed_operations")
        workspace = data.get("workspace")
        if (
            not isinstance(task, dict)
            or not isinstance(task.get("task_id"), str)
            or not task["task_id"].strip()
            or not isinstance(workspace, str)
            or not workspace.strip()
            or not isinstance(allowed, list)
            or any(not isinstance(item, str) or not item.strip() for item in allowed)
            or len(set(allowed)) != len(allowed)
        ):
            raise RuntimeConfigurationError("El manifiesto no cumple el esquema mínimo requerido.")
        if set(allowed) != {"create_text_file"}:
            raise RuntimeConfigurationError("El manifiesto contiene capacidades no implementadas o ambiguas.")
        return data

    def execute(self, task_id: Any, operation: Any, **parameters: Any) -> dict[str, Any]:
        """Autoriza, ejecuta y emite exactamente un evento por solicitud."""
        requested = operation if isinstance(operation, str) else None
        event: dict[str, Any] = {
            "event_id": str(uuid.uuid4()),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "task_id": task_id if isinstance(task_id, str) else None,
            "requested_operation": requested,
            "authorization_result": "denied",
            "execution_result": "rejected",
            "artifact_reference": None,
        }

        try:
            if not isinstance(task_id, str) or task_id != self.manifest["task"]["task_id"]:
                raise _PolicyDenied("La tarea solicitada no está declarada en el manifiesto.")
            if not isinstance(operation, str) or operation not in self.manifest["allowed_operations"]:
                raise _PolicyDenied("Operación no autorizada por el manifiesto.")
            if operation != "create_text_file":
                raise _PolicyDenied("Operación no implementada.")
            if set(parameters) != {"path", "content"}:
                raise _PolicyDenied("Parámetros ausentes o no reconocidos para create_text_file.")

            target = self._resolve_target(parameters.get("path"))
            content = parameters.get("content")
            if not isinstance(content, str):
                raise _PolicyDenied("El contenido debe ser texto UTF-8.")
        except _PolicyDenied as exc:
            result = {"ok": False, "error": str(exc)}
        except OSError as exc:
            # Un fallo al inspeccionar la ruta ocurre antes de conceder
            # autorización: también debe producir un evento, sin fingir que
            # la política rechazó explícitamente la solicitud.
            event["execution_result"] = "error"
            result = {"ok": False, "error": f"Error de sistema de archivos: {exc.__class__.__name__}"}
        else:
            # La autorización queda fijada antes de tocar el filesystem para
            # crear el artefacto. Los errores OS posteriores no la revocan.
            event["authorization_result"] = "authorized"
            try:
                self._create_new_text_file(target, content)
            except OSError as exc:
                event["execution_result"] = "error"
                result = {"ok": False, "error": f"Error de sistema de archivos: {exc.__class__.__name__}"}
            else:
                event["execution_result"] = "success"
                event["artifact_reference"] = target.relative_to(self.workspace).as_posix()
                result = {"ok": True, "artifact_reference": event["artifact_reference"]}

        # Un solo punto de emisión: nunca se registra un segundo evento desde
        # los bloques de excepción ni se reclasifica autorización por un OSError.
        self._append_event(event)
        return result

    def _resolve_target(self, requested_path: Any) -> Path:
        if not isinstance(requested_path, str) or not requested_path.strip() or "\x00" in requested_path:
            raise _PolicyDenied("Ruta ausente o inválida.")
        candidate = Path(requested_path)
        if not candidate.is_absolute():
            candidate = self.workspace / candidate
        # resolve(strict=False) resuelve '..' y symlinks existentes en padres.
        resolved = candidate.resolve(strict=False)
        try:
            resolved.relative_to(self.workspace)
        except ValueError as exc:
            raise _PolicyDenied("La ruta solicitada está fuera del workspace autorizado.") from exc
        if resolved == self.workspace:
            raise _PolicyDenied("La ruta debe identificar un archivo dentro del workspace.")
        if not resolved.parent.is_dir():
            raise _PolicyDenied("El directorio padre debe existir dentro del workspace.")
        if candidate.exists() or candidate.is_symlink() or resolved.exists():
            raise _PolicyDenied("El destino ya existe; no se sobrescribe.")
        return resolved

    @staticmethod
    def _create_new_text_file(target: Path, content: str) -> None:
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(target, flags, 0o600)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
                handle.write(content)
        except BaseException:
            # No dejar un artefacto parcial si falla la escritura después de
            # que el sistema operativo alcanzó a crear el archivo.
            try:
                target.unlink(missing_ok=True)
            except OSError:
                pass
            raise

    def _append_event(self, event: dict[str, Any]) -> None:
        self.events_path.parent.mkdir(parents=True, exist_ok=True)
        payload = (json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
        flags = os.O_WRONLY | os.O_CREAT | os.O_APPEND
        fd = os.open(self.events_path, flags, 0o600)
        try:
            written = os.write(fd, payload)
            if written != len(payload):
                raise OSError("Escritura incompleta del evento en events.jsonl.")
        finally:
            os.close(fd)
