"""Softly Runtime Mini 0.2: workspace confinado y ledger encadenado.

El aislamiento fuerte sigue dependiendo de permisos/identidad y controles del SO.
En POSIX, las rutas del workspace se recorren mediante descriptores de directorio,
O_NOFOLLOW y dir_fd. Si esas primitivas no están disponibles, las operaciones
que requieran confinamiento fallan cerradas: no se degrada silenciosamente a
una validación pathname vulnerable a TOCTOU.
"""
from __future__ import annotations
import errno
import hashlib
import json
import os
import secrets
import stat
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator
try:
    import fcntl
except ImportError:
    fcntl = None
try:
    import msvcrt
except ImportError:
    msvcrt = None

class RuntimeConfigurationError(Exception):
    """El manifiesto o las primitivas de seguridad requeridas no son válidos."""

class _PolicyDenied(Exception):
    """La solicitud no supera las reglas de autorización del runtime."""

class LedgerError(RuntimeError):
    """El ledger no está disponible, no es seguro o no supera su verificación."""

class LedgerIntegrityError(LedgerError):
    """La cadena de eventos o su checkpoint no es íntegro."""

class LedgerSecurityError(LedgerError):
    """El ledger/checkpoint fue sustituido o no es un archivo regular seguro."""

class SoftlyRuntime:
    LEDGER_NAME = 'events.jsonl'
    HEAD_NAME = 'events.head'
    GENESIS = 'GENESIS'

    def __init__(self, manifest_path: str | os.PathLike[str] | None=None) -> None:
        raw_manifest = Path(manifest_path) if manifest_path else Path(__file__).parent / 'manifest.json'
        self.manifest_path = Path(os.path.abspath(raw_manifest))
        self.runtime_dir = self.manifest_path.parent
        self.repo_root = self.runtime_dir.parent
        self.manifest = self._load_manifest()
        self._require_secure_primitives()
        self._root_fd = self._open_directory(self.repo_root)
        self._runtime_fd = self._open_child_directory(self._root_fd, self.runtime_dir.name, create=False)
        self._check_private_directory(self._runtime_fd, 'directorio softly-runtime')
        workspace_parts = self._relative_parts(self.manifest['workspace'])
        current = os.dup(self._root_fd)
        try:
            for part in workspace_parts:
                next_fd = self._open_child_directory(current, part, create=True)
                os.close(current)
                current = next_fd
            self._workspace_fd = current
            current = -1
        finally:
            if current >= 0:
                os.close(current)
        os.fchmod(self._workspace_fd, 448)
        self._check_private_directory(self._workspace_fd, 'workspace')
        self.workspace = self.repo_root.joinpath(*workspace_parts)
        self.events_path = self.runtime_dir / self.LEDGER_NAME
        self.head_path = self.runtime_dir / self.HEAD_NAME
        with self._locked_ledger() as (ledger_fd, head_fd):
            status = self._verify_open_ledger(ledger_fd, head_fd)
            if not status['ok']:
                raise LedgerIntegrityError(status['error'])

    def close(self) -> None:
        for name in ('_workspace_fd', '_runtime_fd', '_root_fd'):
            fd = getattr(self, name, None)
            if fd is not None:
                try:
                    os.close(fd)
                except OSError:
                    pass
                setattr(self, name, None)

    def __del__(self) -> None:
        self.close()

    @staticmethod
    def _require_secure_primitives() -> None:
        required_flags = ('O_NOFOLLOW', 'O_DIRECTORY')
        if os.name != 'posix' or any((not hasattr(os, flag) for flag in required_flags)):
            raise RuntimeConfigurationError('Plataforma sin confinamiento dir_fd/O_NOFOLLOW verificable; Mini 0.2 falla cerradamente.')
        if os.open not in os.supports_dir_fd or os.stat not in os.supports_dir_fd:
            raise RuntimeConfigurationError('La plataforma no soporta open/stat relativos a dir_fd.')
        if fcntl is None and msvcrt is None:
            raise RuntimeConfigurationError('No hay primitiva de bloqueo de ledger disponible.')

    def _load_manifest(self) -> dict[str, Any]:
        try:
            data = json.loads(self.manifest_path.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError) as exc:
            raise RuntimeConfigurationError('No se pudo leer un manifiesto JSON válido.') from exc
        if not isinstance(data, dict):
            raise RuntimeConfigurationError('El manifiesto debe ser un objeto JSON.')
        task, allowed, workspace = (data.get('task'), data.get('allowed_operations'), data.get('workspace'))
        if not isinstance(task, dict) or not isinstance(task.get('task_id'), str) or (not task['task_id'].strip()) or (not isinstance(workspace, str)) or (not workspace.strip()) or (not isinstance(allowed, list)) or any((not isinstance(item, str) or not item.strip() for item in allowed)) or (len(set(allowed)) != len(allowed)):
            raise RuntimeConfigurationError('El manifiesto no cumple el esquema mínimo requerido.')
        if set(allowed) != {'create_text_file'}:
            raise RuntimeConfigurationError('El manifiesto contiene capacidades no implementadas o ambiguas.')
        self_version = str(data.get('version', '0.2.0'))
        if self_version not in {'0.2.0', '0.2'}:
            raise RuntimeConfigurationError('Versión de manifiesto incompatible con Runtime Mini 0.2.')
        return data

    @staticmethod
    def _relative_parts(value: str) -> tuple[str, ...]:
        if not isinstance(value, str) or not value or os.path.isabs(value):
            raise RuntimeConfigurationError('La ruta debe ser relativa a la raíz del proyecto.')
        normalized = value.replace('\\', '/')
        parts = tuple((part for part in normalized.split('/') if part not in ('', '.')))
        if not parts or any((part == '..' or '\x00' in part for part in parts)):
            raise RuntimeConfigurationError('La ruta contiene componentes no permitidos.')
        return parts

    @staticmethod
    def _directory_flags() -> int:
        return os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | getattr(os, 'O_CLOEXEC', 0)

    def _open_directory(self, path: Path) -> int:
        try:
            fd = os.open(path, self._directory_flags())
        except OSError as exc:
            raise RuntimeConfigurationError(f'No se pudo abrir directorio raíz seguro: {exc.__class__.__name__}') from exc
        if not stat.S_ISDIR(os.fstat(fd).st_mode):
            os.close(fd)
            raise RuntimeConfigurationError('La raíz indicada no es un directorio regular.')
        return fd

    def _open_child_directory(self, parent_fd: int, name: str, *, create: bool) -> int:
        if name in ('', '.', '..') or '/' in name or '\\' in name:
            raise RuntimeConfigurationError('Componente de directorio inválido.')
        try:
            before = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            if not create:
                raise RuntimeConfigurationError(f'No existe el directorio requerido: {name}')
            try:
                os.mkdir(name, mode=448, dir_fd=parent_fd)
            except FileExistsError:
                pass
            before = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        if not stat.S_ISDIR(before.st_mode):
            raise RuntimeConfigurationError(f'Componente no-directory o symlink rechazado: {name}')
        fd = os.open(name, self._directory_flags(), dir_fd=parent_fd)
        after = os.fstat(fd)
        if not stat.S_ISDIR(after.st_mode) or (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
            os.close(fd)
            raise RuntimeConfigurationError(f'Componente de directorio cambió durante apertura: {name}')
        return fd

    @staticmethod
    def _check_private_directory(fd: int, label: str) -> None:
        info = os.fstat(fd)
        if not stat.S_ISDIR(info.st_mode) or info.st_mode & (stat.S_IWGRP | stat.S_IWOTH):
            raise RuntimeConfigurationError(f'{label} debe ser directorio no modificable por grupo/otros.')
        if hasattr(os, 'getuid') and info.st_uid != os.getuid():
            raise RuntimeConfigurationError(f'{label} debe pertenecer al usuario efectivo del runtime.')

    @staticmethod
    def _lock(fd: int) -> None:
        if fcntl is not None:
            fcntl.flock(fd, fcntl.LOCK_EX)
        elif msvcrt is not None:
            os.lseek(fd, 0, os.SEEK_SET)
            msvcrt.locking(fd, msvcrt.LK_LOCK, 1)
        else:
            raise LedgerError('No existe bloqueo exclusivo compatible.')

    @staticmethod
    def _unlock(fd: int) -> None:
        if fcntl is not None:
            fcntl.flock(fd, fcntl.LOCK_UN)
        elif msvcrt is not None:
            os.lseek(fd, 0, os.SEEK_SET)
            msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)

    def _open_regular_ledger_file(self, name: str, *, create: bool) -> int:
        try:
            before = os.stat(name, dir_fd=self._runtime_fd, follow_symlinks=False)
        except FileNotFoundError:
            if not create:
                raise LedgerSecurityError(f'Falta {name}.')
            before = None
        if before is not None and (not stat.S_ISREG(before.st_mode)):
            raise LedgerSecurityError(f'{name} debe ser archivo regular, no symlink/FIFO/socket/dispositivo.')
        flags = os.O_RDWR | os.O_APPEND | os.O_NOFOLLOW | getattr(os, 'O_CLOEXEC', 0) | getattr(os, 'O_NONBLOCK', 0)
        if create:
            flags |= os.O_CREAT
        try:
            fd = os.open(name, flags, 384, dir_fd=self._runtime_fd)
        except OSError as exc:
            if exc.errno in (errno.ELOOP, errno.ENOTDIR):
                raise LedgerSecurityError(f'Apertura segura rechazada para {name}.') from exc
            raise LedgerError(f'No se pudo abrir {name}: {exc.__class__.__name__}') from exc
        after = os.fstat(fd)
        if not stat.S_ISREG(after.st_mode):
            os.close(fd)
            raise LedgerSecurityError(f'{name} no es un archivo regular.')
        if before is not None and (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
            os.close(fd)
            raise LedgerSecurityError(f'{name} fue sustituido durante su apertura.')
        if before is None:
            now = os.stat(name, dir_fd=self._runtime_fd, follow_symlinks=False)
            if (now.st_dev, now.st_ino) != (after.st_dev, after.st_ino):
                os.close(fd)
                raise LedgerSecurityError(f'{name} cambió durante su creación.')
        os.fchmod(fd, 384)
        return fd

    @contextmanager
    def _locked_ledger(self) -> Iterator[tuple[int, int]]:
        ledger_fd = self._open_regular_ledger_file(self.LEDGER_NAME, create=True)
        locked = False
        head_fd = -1
        try:
            self._lock(ledger_fd)
            locked = True
            head_fd = self._open_regular_ledger_file(self.HEAD_NAME, create=True)
            if os.fstat(head_fd).st_size == 0 and os.fstat(ledger_fd).st_size == 0:
                os.close(head_fd)
                head_fd = -1
                self._atomic_write_head(self.GENESIS)
                head_fd = self._open_regular_ledger_file(self.HEAD_NAME, create=False)
            yield (ledger_fd, head_fd)
        finally:
            if head_fd >= 0:
                os.close(head_fd)
            if locked:
                self._unlock(ledger_fd)
            os.close(ledger_fd)

    @staticmethod
    def _read_all(fd: int) -> bytes:
        os.lseek(fd, 0, os.SEEK_SET)
        chunks: list[bytes] = []
        while True:
            part = os.read(fd, 65536)
            if not part:
                break
            chunks.append(part)
        return b''.join(chunks)

    @staticmethod
    def _canonical_hash(event: dict[str, Any]) -> str:
        unhashed = {key: value for key, value in event.items() if key != 'event_hash'}
        canonical = json.dumps(unhashed, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
        return hashlib.sha256(canonical).hexdigest()

    def _verify_open_ledger(self, ledger_fd: int, head_fd: int) -> dict[str, Any]:
        try:
            raw = self._read_all(ledger_fd)
            head_raw = self._read_all(head_fd)
            expected_head = head_raw.decode('ascii').strip()
            if expected_head == self.GENESIS and raw:
                raise LedgerIntegrityError('Checkpoint GENESIS contradice un ledger no vacío.')
            previous = self.GENESIS
            count = 0
            if raw and (not raw.endswith(b'\n')):
                raise LedgerIntegrityError('Ledger truncado: última línea JSONL incompleta.')
            for line_number, line in enumerate(raw.splitlines(), 1):
                try:
                    event = json.loads(line.decode('utf-8'))
                except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                    raise LedgerIntegrityError(f'Línea {line_number} no es JSON válido.') from exc
                if not isinstance(event, dict) or event.get('previous_event_hash') != previous:
                    raise LedgerIntegrityError(f'Cadena rota/reordenada en línea {line_number}.')
                recorded = event.get('event_hash')
                calculated = self._canonical_hash(event)
                if not isinstance(recorded, str) or not secrets.compare_digest(recorded, calculated):
                    raise LedgerIntegrityError(f'Hash inválido en línea {line_number}.')
                previous = recorded
                count += 1
            if expected_head != previous:
                raise LedgerIntegrityError('Checkpoint no coincide: posible truncamiento, sustitución o ledger reordenado.')
            return {'ok': True, 'event_count': count, 'head_hash': previous, 'error': None}
        except (OSError, UnicodeDecodeError, LedgerError) as exc:
            return {'ok': False, 'event_count': 0, 'head_hash': None, 'error': str(exc)}

    def verify_ledger(self) -> dict[str, Any]:
        """Verifica JSONL, hashes encadenados y checkpoint externo de cabeza."""
        try:
            with self._locked_ledger() as (ledger_fd, head_fd):
                return self._verify_open_ledger(ledger_fd, head_fd)
        except (OSError, LedgerError) as exc:
            return {'ok': False, 'event_count': 0, 'head_hash': None, 'error': str(exc)}

    def _atomic_write_head(self, head_hash: str) -> None:
        temp_name = f'.events.head.{uuid.uuid4().hex}.tmp'
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | getattr(os, 'O_CLOEXEC', 0)
        fd = os.open(temp_name, flags, 384, dir_fd=self._runtime_fd)
        try:
            payload = (head_hash + '\n').encode('ascii')
            offset = 0
            while offset < len(payload):
                offset += os.write(fd, payload[offset:])
            os.fsync(fd)
        except BaseException:
            try:
                os.unlink(temp_name, dir_fd=self._runtime_fd)
            except OSError:
                pass
            raise
        finally:
            os.close(fd)
        try:
            os.replace(temp_name, self.HEAD_NAME, src_dir_fd=self._runtime_fd, dst_dir_fd=self._runtime_fd)
            os.fsync(self._runtime_fd)
        except BaseException:
            try:
                os.unlink(temp_name, dir_fd=self._runtime_fd)
            except OSError:
                pass
            raise

    def _append_event_locked(self, ledger_fd: int, event: dict[str, Any], previous: str) -> None:
        event['previous_event_hash'] = previous
        event['event_hash'] = self._canonical_hash(event)
        payload = (json.dumps(event, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n').encode('utf-8')
        old_size = os.fstat(ledger_fd).st_size
        try:
            offset = 0
            while offset < len(payload):
                offset += os.write(ledger_fd, payload[offset:])
            os.fsync(ledger_fd)
            self._atomic_write_head(event['event_hash'])
        except BaseException:
            try:
                os.ftruncate(ledger_fd, old_size)
                os.fsync(ledger_fd)
            except OSError:
                pass
            raise

    def execute(self, task_id: Any, operation: Any, **parameters: Any) -> dict[str, Any]:
        """Ejecuta con ledger verificado/bloqueado y emite un evento encadenado."""
        with self._locked_ledger() as (ledger_fd, head_fd):
            integrity = self._verify_open_ledger(ledger_fd, head_fd)
            if not integrity['ok']:
                raise LedgerIntegrityError(integrity['error'] or 'Ledger inválido.')
            previous = integrity['head_hash'] or self.GENESIS
            requested = operation if isinstance(operation, str) else None
            event: dict[str, Any] = {'event_id': str(uuid.uuid4()), 'timestamp': datetime.now(timezone.utc).isoformat(), 'task_id': task_id if isinstance(task_id, str) else None, 'requested_operation': requested, 'authorization_result': 'denied', 'execution_result': 'rejected', 'artifact_reference': None}
            created: tuple[int, str] | None = None
            try:
                if not isinstance(task_id, str) or task_id != self.manifest['task']['task_id']:
                    raise _PolicyDenied('La tarea solicitada no está declarada en el manifiesto.')
                if not isinstance(operation, str) or operation not in self.manifest['allowed_operations']:
                    raise _PolicyDenied('Operación no autorizada por el manifiesto.')
                if operation != 'create_text_file':
                    raise _PolicyDenied('Operación no implementada.')
                if set(parameters) != {'path', 'content'}:
                    raise _PolicyDenied('Parámetros ausentes o no reconocidos para create_text_file.')
                content = parameters.get('content')
                if not isinstance(content, str):
                    raise _PolicyDenied('El contenido debe ser texto UTF-8.')
                parent_fd, filename = self._open_target_parent(parameters.get('path'))
                try:
                    event['authorization_result'] = 'authorized'
                    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | getattr(os, 'O_CLOEXEC', 0)
                    artifact_fd = os.open(filename, flags, 384, dir_fd=parent_fd)
                    created = (os.dup(parent_fd), filename)
                    with os.fdopen(artifact_fd, 'w', encoding='utf-8', newline='') as handle:
                        handle.write(content)
                        handle.flush()
                        os.fsync(handle.fileno())
                    event['execution_result'] = 'success'
                    event['artifact_reference'] = str(parameters['path']).replace('\\', '/')
                finally:
                    os.close(parent_fd)
            except _PolicyDenied as exc:
                result = {'ok': False, 'error': str(exc)}
            except FileExistsError:
                event['authorization_result'] = 'denied'
                event['execution_result'] = 'rejected'
                result = {'ok': False, 'error': 'El destino ya existe; no se sobrescribe.'}
            except OSError as exc:
                event['execution_result'] = 'error'
                if created is not None:
                    cleanup_fd, cleanup_name = created
                    try:
                        os.unlink(cleanup_name, dir_fd=cleanup_fd)
                        os.fsync(cleanup_fd)
                    except OSError:
                        pass
                    finally:
                        os.close(cleanup_fd)
                    created = None
                result = {'ok': False, 'error': f'Error de sistema de archivos: {exc.__class__.__name__}'}
            else:
                result = {'ok': True, 'artifact_reference': event['artifact_reference']}
            try:
                self._append_event_locked(ledger_fd, event, previous)
            except OSError as exc:
                if created is not None:
                    parent_fd, filename = created
                    try:
                        os.unlink(filename, dir_fd=parent_fd)
                        os.fsync(parent_fd)
                    except OSError:
                        pass
                    finally:
                        os.close(parent_fd)
                raise LedgerError(f'No se pudo persistir el evento; operación no confirmada: {exc.__class__.__name__}') from exc
            if created is not None:
                os.close(created[0])
            return result

    def _open_target_parent(self, requested_path: Any) -> tuple[int, str]:
        if not isinstance(requested_path, str) or not requested_path.strip() or os.path.isabs(requested_path):
            raise _PolicyDenied('La ruta debe ser relativa al workspace.')
        try:
            parts = self._relative_parts(requested_path)
        except RuntimeConfigurationError as exc:
            raise _PolicyDenied(str(exc)) from exc
        current = os.dup(self._workspace_fd)
        try:
            for component in parts[:-1]:
                try:
                    next_fd = os.open(component, self._directory_flags(), dir_fd=current)
                except OSError as exc:
                    if exc.errno in (errno.ELOOP, errno.ENOTDIR):
                        raise _PolicyDenied('Symlink o componente no-directorio rechazado en el workspace.') from exc
                    if exc.errno == errno.ENOENT:
                        raise _PolicyDenied('El directorio padre debe existir dentro del workspace.') from exc
                    raise
                info = os.fstat(next_fd)
                if not stat.S_ISDIR(info.st_mode):
                    os.close(next_fd)
                    raise _PolicyDenied('Componente padre no es un directorio seguro.')
                os.close(current)
                current = next_fd
            try:
                info = os.stat(parts[-1], dir_fd=current, follow_symlinks=False)
            except FileNotFoundError:
                info = None
            if info is not None:
                raise _PolicyDenied('El destino ya existe o es un enlace simbólico.')
            return (current, parts[-1])
        except BaseException:
            os.close(current)
            raise
