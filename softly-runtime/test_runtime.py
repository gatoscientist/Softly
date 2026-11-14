"""Pruebas deterministas de aceptación para Softly Runtime Mini 0.1."""

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import runtime as runtime_module
from runtime import SoftlyRuntime


class SoftlyRuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.package = self.root / "softly-runtime"
        self.workspace = self.package / "workspace"
        self.workspace.mkdir(parents=True)
        self.manifest = self.package / "manifest.json"
        self.manifest.write_text(
            json.dumps(
                {
                    "schema_version": "1.0",
                    "runtime": "Softly Runtime Mini",
                    "version": "0.1",
                    "task": {"task_id": "runtime-mini-smoke-test", "description": "test"},
                    "workspace": "softly-runtime/workspace/",
                    "allowed_operations": ["create_text_file"],
                }
            ),
            encoding="utf-8",
        )
        self.runtime = SoftlyRuntime(self.manifest)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def events(self) -> list[dict]:
        path = self.package / "events.jsonl"
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

    def test_case_1_allowed_write_creates_file_and_event(self) -> None:
        result = self.runtime.execute(
            "runtime-mini-smoke-test", "create_text_file", path="hello.txt", content="hola Softly\n"
        )
        artifact = self.workspace / "hello.txt"
        self.assertTrue(result["ok"])
        self.assertTrue(artifact.is_file())
        self.assertEqual(artifact.read_text(encoding="utf-8"), "hola Softly\n")

        # Un destino preexistente se rechaza y conserva íntegro su contenido.
        repeated = self.runtime.execute(
            "runtime-mini-smoke-test", "create_text_file", path="hello.txt", content="no sobrescribir"
        )
        self.assertFalse(repeated["ok"])
        self.assertEqual(artifact.read_text(encoding="utf-8"), "hola Softly\n")

        events = self.events()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["authorization_result"], "authorized")
        self.assertEqual(events[0]["execution_result"], "success")
        self.assertEqual(events[0]["artifact_reference"], "hello.txt")
        self.assertTrue(events[0]["event_id"])
        self.assertTrue(events[0]["timestamp"])
        self.assertEqual(events[0]["task_id"], "runtime-mini-smoke-test")
        self.assertEqual(events[0]["requested_operation"], "create_text_file")
        self.assertEqual(events[1]["authorization_result"], "denied")
        self.assertEqual(events[1]["execution_result"], "rejected")
        self.assertIsNone(events[1]["artifact_reference"])

    def test_case_2_relative_and_absolute_escape_are_rejected_without_disk_write(self) -> None:
        outside_relative = self.root / "outside-relative.txt"
        outside_absolute = self.root / "outside-absolute.txt"
        relative_result = self.runtime.execute(
            "runtime-mini-smoke-test", "create_text_file", path="../../outside-relative.txt", content="no"
        )
        absolute_result = self.runtime.execute(
            "runtime-mini-smoke-test", "create_text_file", path=str(outside_absolute), content="no"
        )
        self.assertFalse(relative_result["ok"])
        self.assertFalse(absolute_result["ok"])
        self.assertFalse(outside_relative.exists())
        self.assertFalse(outside_absolute.exists())
        events = self.events()
        self.assertEqual(len(events), 2)
        self.assertTrue(all(item["authorization_result"] == "denied" for item in events))
        self.assertTrue(all(item["execution_result"] == "rejected" for item in events))
        self.assertTrue(all(item["artifact_reference"] is None for item in events))

    def test_case_3_undeclared_capability_and_ambiguous_parameters_are_rejected(self) -> None:
        forbidden = self.workspace / "should-not-exist.txt"
        result = self.runtime.execute(
            "runtime-mini-smoke-test", "delete_file", path="should-not-exist.txt", content="ignored"
        )
        extra_parameter = self.runtime.execute(
            "runtime-mini-smoke-test", "create_text_file", path="extra.txt", content="no", mode="w"
        )
        missing_parameter = self.runtime.execute(
            "runtime-mini-smoke-test", "create_text_file", path="missing.txt"
        )
        self.assertFalse(result["ok"])
        self.assertFalse(extra_parameter["ok"])
        self.assertFalse(missing_parameter["ok"])
        self.assertFalse(forbidden.exists())
        self.assertFalse((self.workspace / "extra.txt").exists())
        self.assertFalse((self.workspace / "missing.txt").exists())
        events = self.events()
        self.assertEqual(len(events), 3)
        self.assertEqual(events[0]["requested_operation"], "delete_file")
        self.assertTrue(all(item["authorization_result"] == "denied" for item in events))
        self.assertTrue(all(item["execution_result"] == "rejected" for item in events))
        self.assertTrue(all(item["artifact_reference"] is None for item in events))

    def test_case_4_os_permission_error_after_authorization_records_one_consistent_event(self) -> None:
        target = self.workspace / "denied.txt"
        real_open = os.open
        target_open_attempts = 0

        def fail_only_artifact_open(path, flags, mode=0o777):
            nonlocal target_open_attempts
            if Path(path) == target:
                target_open_attempts += 1
                raise PermissionError("permiso denegado simulado por prueba")
            return real_open(path, flags, mode)

        with patch.object(runtime_module.os, "open", side_effect=fail_only_artifact_open):
            result = self.runtime.execute(
                "runtime-mini-smoke-test", "create_text_file", path="denied.txt", content="no debe crearse"
            )

        self.assertFalse(result["ok"])
        self.assertIn("PermissionError", result["error"])
        self.assertEqual(target_open_attempts, 1)
        self.assertFalse(target.exists())
        events = self.events()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["authorization_result"], "authorized")
        self.assertEqual(events[0]["execution_result"], "error")
        self.assertIsNone(events[0]["artifact_reference"])
        self.assertEqual(events[0]["requested_operation"], "create_text_file")


if __name__ == "__main__":
    unittest.main(verbosity=2)
