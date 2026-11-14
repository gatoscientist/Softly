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
        # Mini 0.1 solo implementa esta operación concreta; no se aceptan
        # alias, nombres alternativos ni capacidades declarativas desconocidas.
        if set(allowed) != {"create_text_file"}:
            raise RuntimeConfigurationError("El manifiesto contiene capacidades no implementadas o ambiguas.")
        return data

    def execute(self, task_id: Any, operation: Any, **parameters: Any) -> dict[str, Any]:
        """Autoriza y ejecuta una solicitud; siempre intenta registrar el evento."""
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
        result: dict[str, Any]
        try:
            if not isinstance(task_id, str) or task_id != self.manifest["task"]["task_id"]:
                raise PermissionError("La tarea solicitada no está declarada en el manifiesto.")
            if not isinstance(operation, str) or operation not in self.manifest["allowed_operations"]:
                raise PermissionError("Operación no autorizada por el manifiesto.")
            if operation != "create_text_file":
                raise PermissionError("Operación no implementada.")
            if set(parameters) != {"path", "content"}:
                raise PermissionError("Parámetros ausentes o no reconocidos para create_text_file.")

            target = self._resolve_target(parameters.get("path"))
            content = parameters.get("content")
            if not isinstance(content, str):
                raise PermissionError("El contenido debe ser texto UTF-8.")

            event["authorization_result"] = "authorized"
            self._create_new_text_file(target, content)
            event["execution_result"] = "success"
            event["artifact_reference"] = target.relative_to(self.workspace).as_posix()
            result = {"ok": True, "artifact_reference": event["artifact_reference"]}
        except PermissionError as exc:
            result = {"ok": False, "error": str(exc)}
        except FileExistsError:
            event["authorization_result"] = "authorized"
            event["execution_result"] = "error"
            result = {"ok": False, "error": "El archivo ya existe; no se sobrescribe."}
        except OSError as exc:
            event["execution_result"] = "error"
            result = {"ok": False, "error": f"Error de sistema de archivos: {exc.__class__.__name__}"}
        finally:
            self._append_event(event)
        return result

    def _resolve_target(self, requested_path: Any) -> Path:
        if not isinstance(requested_path, str) or not requested_path.strip() or "\x00" in requested_path:
            raise PermissionError("Ruta ausente o inválida.")
        candidate = Path(requested_path)
        if not candidate.is_absolute():
            candidate = self.workspace / candidate
        # resolve(strict=False) resuelve '..' y symlinks existentes en padres.
        resolved = candidate.resolve(strict=False)
        try:
            resolved.relative_to(self.workspace)
        except ValueError as exc:
            raise PermissionError("La ruta solicitada está fuera del workspace autorizado.") from exc
        if resolved == self.workspace:
            raise PermissionError("La ruta debe identificar un archivo dentro del workspace.")
        if not resolved.parent.is_dir():
            raise PermissionError("El directorio padre debe existir dentro del workspace.")
        # No aceptar un destino que ya exista, incluidos symlinks.
        if candidate.exists() or candidate.is_symlink() or resolved.exists():
            raise PermissionError("El destino ya existe; no se sobrescribe.")
        return resolved

    @staticmethod
    def _create_new_text_file(target: Path, content: str) -> None:
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(target, flags, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)

    def _append_event(self, event: dict[str, Any]) -> None:
        self.events_path.parent.mkdir(parents=True, exist_ok=True)
        with self.events_path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
