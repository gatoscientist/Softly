"""Pruebas deterministas de aceptación para Softly Runtime Mini 0.2."""
import json
import os
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import patch
import runtime as runtime_module
from runtime import LedgerError, LedgerSecurityError, RuntimeConfigurationError, SoftlyRuntime

class SoftlyRuntimeTests(unittest.TestCase):

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.package = self.root / 'softly-runtime'
        self.workspace = self.package / 'workspace'
        self.package.mkdir(mode=448)
        self.workspace.mkdir(mode=448)
        self.manifest = self.package / 'manifest.json'
        self.manifest.write_text(json.dumps({'schema_version': '1.0', 'runtime': 'Softly Runtime Mini', 'version': '0.2.0', 'task': {'task_id': 'runtime-mini-smoke-test', 'description': 'test'}, 'workspace': 'softly-runtime/workspace/', 'allowed_operations': ['create_text_file']}), encoding='utf-8')
        self.runtime = SoftlyRuntime(self.manifest)

    def tearDown(self) -> None:
        self.runtime.close()
        self.temp.cleanup()

    def events(self) -> list[dict]:
        path = self.package / 'events.jsonl'
        return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]

    def test_case_1_allowed_write_creates_file_and_event(self) -> None:
        result = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='hello.txt', content='hola Softly\n')
        artifact = self.workspace / 'hello.txt'
        self.assertTrue(result['ok'])
        self.assertTrue(artifact.is_file())
        self.assertEqual(artifact.read_text(encoding='utf-8'), 'hola Softly\n')
        repeated = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='hello.txt', content='no sobrescribir')
        self.assertFalse(repeated['ok'])
        self.assertEqual(artifact.read_text(encoding='utf-8'), 'hola Softly\n')
        events = self.events()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]['authorization_result'], 'authorized')
        self.assertEqual(events[0]['execution_result'], 'success')
        self.assertEqual(events[0]['artifact_reference'], 'hello.txt')
        self.assertTrue(events[0]['event_id'])
        self.assertTrue(events[0]['timestamp'])
        self.assertEqual(events[0]['task_id'], 'runtime-mini-smoke-test')
        self.assertEqual(events[0]['requested_operation'], 'create_text_file')
        self.assertEqual(events[1]['authorization_result'], 'denied')
        self.assertEqual(events[1]['execution_result'], 'rejected')
        self.assertIsNone(events[1]['artifact_reference'])

    def test_case_2_relative_and_absolute_escape_are_rejected_without_disk_write(self) -> None:
        outside_relative = self.root / 'outside-relative.txt'
        outside_absolute = self.root / 'outside-absolute.txt'
        relative_result = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='../../outside-relative.txt', content='no')
        absolute_result = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path=str(outside_absolute), content='no')
        self.assertFalse(relative_result['ok'])
        self.assertFalse(absolute_result['ok'])
        self.assertFalse(outside_relative.exists())
        self.assertFalse(outside_absolute.exists())
        events = self.events()
        self.assertEqual(len(events), 2)
        self.assertTrue(all((item['authorization_result'] == 'denied' for item in events)))
        self.assertTrue(all((item['execution_result'] == 'rejected' for item in events)))
        self.assertTrue(all((item['artifact_reference'] is None for item in events)))

    def test_case_3_undeclared_capability_and_ambiguous_parameters_are_rejected(self) -> None:
        forbidden = self.workspace / 'should-not-exist.txt'
        result = self.runtime.execute('runtime-mini-smoke-test', 'delete_file', path='should-not-exist.txt', content='ignored')
        extra_parameter = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='extra.txt', content='no', mode='w')
        missing_parameter = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='missing.txt')
        self.assertFalse(result['ok'])
        self.assertFalse(extra_parameter['ok'])
        self.assertFalse(missing_parameter['ok'])
        self.assertFalse(forbidden.exists())
        self.assertFalse((self.workspace / 'extra.txt').exists())
        self.assertFalse((self.workspace / 'missing.txt').exists())
        events = self.events()
        self.assertEqual(len(events), 3)
        self.assertEqual(events[0]['requested_operation'], 'delete_file')
        self.assertTrue(all((item['authorization_result'] == 'denied' for item in events)))
        self.assertTrue(all((item['execution_result'] == 'rejected' for item in events)))
        self.assertTrue(all((item['artifact_reference'] is None for item in events)))

    def test_case_4_os_permission_error_after_authorization_records_one_consistent_event(self) -> None:
        target = self.workspace / 'denied.txt'
        real_open = os.open
        target_open_attempts = 0

        def fail_only_artifact_open(path, flags, mode=511, *, dir_fd=None):
            nonlocal target_open_attempts
            if path == 'denied.txt' and dir_fd is not None:
                target_open_attempts += 1
                raise PermissionError('permiso denegado simulado por prueba')
            if dir_fd is None:
                return real_open(path, flags, mode)
            return real_open(path, flags, mode, dir_fd=dir_fd)
        with patch.object(runtime_module.os, 'open', side_effect=fail_only_artifact_open):
            result = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='denied.txt', content='no debe crearse')
        self.assertFalse(result['ok'])
        self.assertIn('PermissionError', result['error'])
        self.assertEqual(target_open_attempts, 1)
        self.assertFalse(target.exists())
        events = self.events()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]['authorization_result'], 'authorized')
        self.assertEqual(events[0]['execution_result'], 'error')
        self.assertIsNone(events[0]['artifact_reference'])
        self.assertEqual(events[0]['requested_operation'], 'create_text_file')

    def test_case_5_f01_symlink_parent_escape_is_rejected(self) -> None:
        outside = self.root / 'outside'
        outside.mkdir()
        marker = outside / 'keep.txt'
        marker.write_text('intacto', encoding='utf-8')
        (self.workspace / 'portal').symlink_to(outside, target_is_directory=True)
        result = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='portal/escape.txt', content='intrusion')
        self.assertFalse(result['ok'])
        self.assertEqual(marker.read_text(encoding='utf-8'), 'intacto')
        self.assertFalse((outside / 'escape.txt').exists())
        events = self.events()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]['authorization_result'], 'denied')
        self.assertEqual(events[0]['execution_result'], 'rejected')
        self.assertIsNone(events[0]['artifact_reference'])
        self.assertTrue(self.runtime.verify_ledger()['ok'])
        external_file = outside / 'final.txt'
        external_file.write_text('no modificar', encoding='utf-8')
        (self.workspace / 'final-link.txt').symlink_to(external_file)
        final_result = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='final-link.txt', content='intrusion')
        self.assertFalse(final_result['ok'])
        self.assertEqual(external_file.read_text(encoding='utf-8'), 'no modificar')
        self.runtime.close()
        moved_workspace = self.package / 'workspace-real'
        self.workspace.rename(moved_workspace)
        self.workspace.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(RuntimeConfigurationError):
            SoftlyRuntime(self.manifest)
        self.workspace.unlink()
        moved_workspace.rename(self.workspace)
        self.runtime = SoftlyRuntime(self.manifest)

    def test_case_6_f03_ledger_symlink_hash_chain_and_tamper_detection(self) -> None:
        ledger = self.package / 'events.jsonl'
        outside = self.root / 'external-ledger.jsonl'
        outside.write_text('no tocar', encoding='utf-8')
        ledger.unlink()
        ledger.symlink_to(outside)
        with self.assertRaises(LedgerSecurityError):
            self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='must-not-exist.txt', content='no')
        self.assertFalse((self.workspace / 'must-not-exist.txt').exists())
        self.assertEqual(outside.read_text(encoding='utf-8'), 'no tocar')
        ledger.unlink()
        ledger.write_bytes(b'')
        first = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='first.txt', content='uno')
        second = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='second.txt', content='dos')
        self.assertTrue(first['ok'])
        self.assertTrue(second['ok'])
        events = self.events()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]['previous_event_hash'], 'GENESIS')
        self.assertEqual(events[1]['previous_event_hash'], events[0]['event_hash'])
        self.assertTrue(self.runtime.verify_ledger()['ok'])
        second_runtime = SoftlyRuntime(self.manifest)

        def write_one(index: int) -> dict:
            selected_runtime = self.runtime if index % 2 == 0 else second_runtime
            return selected_runtime.execute('runtime-mini-smoke-test', 'create_text_file', path=f'parallel-{index}.txt', content=str(index))
        with ThreadPoolExecutor(max_workers=6) as pool:
            concurrent_results = list(pool.map(write_one, range(12)))
        second_runtime.close()
        self.assertTrue(all((item['ok'] for item in concurrent_results)))
        self.assertTrue(self.runtime.verify_ledger()['ok'])

        # Regresión F-03: falla el fsync del directorio después de publicar
        # events.head mediante os.replace. El rollback debe restaurar ambos.
        before_ledger = ledger.read_bytes()
        before_head = (self.package / 'events.head').read_bytes()
        real_replace = os.replace
        real_fsync = os.fsync
        checkpoint_replaced = False
        injected_failure = False

        def observe_checkpoint_replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None):
            nonlocal checkpoint_replaced
            result = real_replace(src, dst, src_dir_fd=src_dir_fd, dst_dir_fd=dst_dir_fd)
            if dst == 'events.head':
                checkpoint_replaced = True
            return result

        def fail_directory_fsync_once(fd: int) -> None:
            nonlocal injected_failure
            if checkpoint_replaced and not injected_failure and runtime_module.stat.S_ISDIR(os.fstat(fd).st_mode):
                injected_failure = True
                raise OSError('fsync de directorio simulado después de os.replace')
            return real_fsync(fd)

        with patch.object(runtime_module.os, 'replace', side_effect=observe_checkpoint_replace):
            with patch.object(runtime_module.os, 'fsync', side_effect=fail_directory_fsync_once):
                with self.assertRaises(LedgerError):
                    self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='head-fsync-failure.txt', content='no confirmar')

        self.assertTrue(injected_failure)
        self.assertEqual(ledger.read_bytes(), before_ledger)
        self.assertEqual((self.package / 'events.head').read_bytes(), before_head)
        self.assertTrue(self.runtime.verify_ledger()['ok'])
        self.assertFalse((self.workspace / 'head-fsync-failure.txt').exists())
        recovered = self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='after-head-recovery.txt', content='recuperado')
        self.assertTrue(recovered['ok'])
        self.assertTrue(self.runtime.verify_ledger()['ok'])

        complete_ledger = ledger.read_bytes()
        complete_lines = complete_ledger.splitlines(keepends=True)
        self.assertEqual(len(complete_lines), 15)
        ledger_identity = os.stat(ledger)
        real_write = os.write
        partial_written = False

        def fail_ledger_after_partial(fd: int, payload: bytes) -> int:
            nonlocal partial_written
            info = os.fstat(fd)
            if (info.st_dev, info.st_ino) == (ledger_identity.st_dev, ledger_identity.st_ino):
                if not partial_written:
                    partial_written = True
                    return real_write(fd, payload[:5])
                raise OSError('fallo parcial de ledger simulado')
            return real_write(fd, payload)
        with patch.object(runtime_module.os, 'write', side_effect=fail_ledger_after_partial):
            with self.assertRaises(LedgerError):
                self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='ledger-failure.txt', content='no confirmar')
        self.assertFalse((self.workspace / 'ledger-failure.txt').exists())
        self.assertEqual(ledger.read_bytes(), complete_ledger)
        self.assertTrue(self.runtime.verify_ledger()['ok'])
        ledger.write_bytes(b''.join(complete_lines[:-1]))
        self.assertFalse(self.runtime.verify_ledger()['ok'])
        ledger.write_bytes(complete_ledger)
        ledger.write_bytes(b''.join(reversed(complete_lines)))
        self.assertFalse(self.runtime.verify_ledger()['ok'])
        ledger.write_bytes(complete_ledger)
        tampered = ledger.read_text(encoding='utf-8').replace('"success"', '"tampered"', 1)
        ledger.write_text(tampered, encoding='utf-8')
        verification = self.runtime.verify_ledger()
        self.assertFalse(verification['ok'])
        self.assertTrue(verification['error'])
        ledger.write_bytes(complete_ledger)
        self.runtime.close()
        os.chmod(self.package, 511)
        with self.assertRaises(RuntimeConfigurationError):
            SoftlyRuntime(self.manifest)
        os.chmod(self.package, 448)
        self.runtime = SoftlyRuntime(self.manifest)

    def test_f03_recovery_truncates_only_unconfirmed_suffix_and_is_idempotent(self) -> None:
        self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='kept.txt', content='keep')
        ledger = self.package / 'events.jsonl'
        head = self.package / 'events.head'
        confirmed = ledger.read_bytes()
        checkpoint = head.read_bytes()
        with ledger.open('ab') as handle:
            handle.write(b'{"unconfirmed":')
            handle.flush()
            os.fsync(handle.fileno())
        result = self.runtime.recover_ledger()
        self.assertEqual(result['status'], 'recovered')
        self.assertEqual(ledger.read_bytes(), confirmed)
        self.assertEqual(head.read_bytes(), checkpoint)
        self.assertTrue(result['backup'])
        self.assertEqual((self.package / result['backup']).read_bytes(), confirmed + b'{"unconfirmed":')
        second = self.runtime.recover_ledger()
        self.assertEqual(second['status'], 'already_consistent')
        self.assertEqual(ledger.read_bytes(), confirmed)
        self.assertEqual(head.read_bytes(), checkpoint)
        self.assertTrue(self.runtime.execute('runtime-mini-smoke-test', 'create_text_file',
                                              path='after-recovery.txt', content='ok')['ok'])

    def test_f03_recovery_rejects_foreign_checkpoint_without_ledger_changes(self) -> None:
        self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='kept.txt', content='keep')
        ledger = self.package / 'events.jsonl'
        head = self.package / 'events.head'
        original_ledger = ledger.read_bytes()
        original_head = head.read_bytes()
        head.write_bytes(b'0' * 64 + b'\\n')
        foreign_head = head.read_bytes()
        result = self.runtime.recover_ledger()
        self.assertEqual(result['status'], 'rejected')
        self.assertEqual(ledger.read_bytes(), original_ledger)
        self.assertEqual(head.read_bytes(), foreign_head)
        self.assertFalse(self.runtime.execute('runtime-mini-smoke-test', 'create_text_file',
                                              path='blocked.txt', content='no')['ok'])

    def test_f03_recovery_rejects_corruption_before_checkpoint(self) -> None:
        self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='kept.txt', content='keep')
        ledger = self.package / 'events.jsonl'
        original = ledger.read_bytes()
        damaged = bytearray(original)
        damaged[10] ^= 1
        ledger.write_bytes(bytes(damaged) + b'junk')
        before = ledger.read_bytes()
        head_before = (self.package / 'events.head').read_bytes()
        result = self.runtime.recover_ledger()
        self.assertEqual(result['status'], 'rejected')
        self.assertEqual(ledger.read_bytes(), before)
        self.assertEqual((self.package / 'events.head').read_bytes(), head_before)

    def test_f03_recovery_genesis_checkpoint_discards_unconfirmed_bytes(self) -> None:
        ledger = self.package / 'events.jsonl'
        head = self.package / 'events.head'
        ledger.write_bytes(b'not-json\\npartial')
        head.write_bytes(b'GENESIS\\n')
        result = self.runtime.recover_ledger()
        self.assertEqual(result['status'], 'recovered')
        self.assertEqual(ledger.read_bytes(), b'')
        self.assertEqual(head.read_bytes(), b'GENESIS\\n')
        self.assertTrue(self.runtime.verify_ledger()['ok'])

    def test_f03_recovery_never_deletes_workspace_artifacts(self) -> None:
        self.runtime.execute('runtime-mini-smoke-test', 'create_text_file', path='artifact.txt', content='preserve')
        artifact = self.workspace / 'artifact.txt'
        before = artifact.read_bytes()
        ledger = self.package / 'events.jsonl'
        with ledger.open('ab') as handle:
            handle.write(b'corrupt-suffix')
        result = self.runtime.recover_ledger()
        self.assertEqual(result['status'], 'recovered')
        self.assertEqual(artifact.read_bytes(), before)

if __name__ == '__main__':
    unittest.main(verbosity=2)