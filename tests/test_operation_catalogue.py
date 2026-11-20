"""Exercise first use, operation fixtures, fallback selection and refresh through the CLI."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
import operation_catalogue as catalogue


class CatalogueCLI(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / "settings" / "operations.json"
        self.resources = self.root / "approved.json"

    def cli(self, *args, ok=True):
        result = subprocess.run(
            [
                sys.executable,
                SCRIPTS / "operation_catalogue.py",
                "--catalogue",
                self.path,
                *args,
            ],
            capture_output=True,
            text=True,
        )
        if not ok:
            self.assertNotEqual(result.returncode, 0)
            return result.stderr
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_initial_permission_and_typed_fallback(self):
        self.assertTrue(self.cli("show")["setup_required"])
        self.assertFalse(self.path.exists())
        self.assertIn("user-confirmed", self.cli("refresh", ok=False))
        self.resources.write_text(
            json.dumps(
                [
                    {
                        "id": "optional",
                        "kind": "opencv",
                        "python": str(self.root / "no-python"),
                    },
                    {
                        "id": "drawing",
                        "kind": "skill",
                        "location": str(ROOT / "skills/cad-drawing-inspection"),
                        "methods": [
                            {
                                "name": "trace",
                                "input": "image",
                                "output": "contours",
                                "probe": "guided",
                            },
                            {
                                "name": "locate",
                                "input": "image",
                                "output": "box",
                                "probe": "guided",
                            },
                        ],
                    },
                ]
            )
        )
        result = self.cli("refresh", "--resources", self.resources)
        missing = next(r for r in result["operations"] if r["resource"] == "optional")
        self.assertIn("no-python", missing["reason"])
        self.assertEqual(self.cli("routes", "contours"), [])
        artifact = self.root / "trace.json"
        artifact.write_text('{"contours":[[[0,0],[0,1],[1,1],[0,0]]]}')
        self.cli("observed", "drawing", "trace", artifact, "One closed triangle")
        routes = self.cli("routes", "contours")
        self.assertEqual([r["name"] for r in routes], ["trace"])
        self.assertTrue(routes[0]["evidence_sha256"])
        self.assertEqual(self.cli("routes", "box"), [])
        self.cli("failed", "drawing", "trace", "Source tracing tool closed")
        self.assertEqual(self.cli("routes", "contours"), [])
        self.assertEqual(self.cli("refresh")["became_available"], [])
        self.resources.write_text("[]")
        self.assertEqual(
            self.cli("refresh", "--resources", self.resources)["resources"], []
        )

    def test_actual_intake_can_be_removed_and_rechecked(self):
        sample = self.root / "input.json"
        sample.write_text(
            json.dumps(
                {
                    "job_name": "fixture",
                    "revision_id": "v1",
                    "model": "test",
                    "request": {"text": "Record fixture", "location": "test"},
                    "scope": {
                        "statement": "one sample",
                        "requested_output": "revision",
                        "authorized_paths": [str(self.root)],
                    },
                    "sources": [
                        {
                            "id": "s1",
                            "kind": "text",
                            "title": "sample",
                            "summary": "fixture",
                            "locator": "test",
                            "observed_at": "2026-01-01",
                            "text": "sample",
                        }
                    ],
                }
            )
        )
        resource = {
            "id": "intake",
            "kind": "skill",
            "scripts": str(SCRIPTS),
            "python": sys.executable,
            "methods": [
                {
                    "name": "register",
                    "input": "spec",
                    "output": "source revision",
                    "probe": "intake",
                    "sample": str(sample),
                }
            ],
        }
        self.resources.write_text(json.dumps([resource]))
        key = [["intake", "register"]]
        self.assertEqual(
            self.cli("refresh", "--resources", self.resources)["became_available"], key
        )
        self.assertEqual(self.cli("refresh")["became_available"], [])
        self.assertTrue(self.cli("routes", "source revision"))
        sample.rename(self.root / "moved.json")
        self.assertEqual(self.cli("refresh")["became_unavailable"], key)
        self.assertEqual(self.cli("routes", "source revision"), [])
        (self.root / "moved.json").rename(sample)
        self.assertEqual(self.cli("refresh")["became_available"], key)
        self.resources.write_text("[]")
        self.assertEqual(
            self.cli("refresh", "--resources", self.resources)["became_unavailable"],
            key,
        )

    def test_box_cannot_qualify_outline_or_other_output(self):
        with self.assertRaisesRegex(ValueError, "contours produces contours"):
            catalogue.qualify(
                {"python": sys.executable}, {"probe": "contours", "output": "CAD solid"}
            )
        config = self.root / "config.json"
        config.write_text(json.dumps({"url": "https://example.invalid/vision"}))
        method = dict(
            name="locate",
            input="image",
            output="polygon",
            probe="vision",
            sample="approved.png",
            config=str(config),
        )
        resource = dict(
            id="server",
            python=sys.executable,
            location="https://example.invalid/vision",
        )

        def fake_server(command, **kwargs):
            output = command[-1]
            output.mkdir()
            (output / "observations.json").write_text('{"instances":[{"kind":"box"}]}')

        with patch.object(catalogue, "run_checked", side_effect=fake_server):
            with self.assertRaisesRegex(ValueError, "no polygon"):
                catalogue.qualify(resource, method)
            catalogue.qualify(resource, dict(method, output="box"))

    def test_changed_server_sample_stops_before_new_request(self):
        config = self.root / "config.json"
        sample = self.root / "sample.png"
        config.write_text('{"url":"https://example.invalid"}')
        sample.write_bytes(b"approved")
        method = dict(
            name="locate",
            input="image",
            output="box",
            probe="vision",
            sample=str(sample),
            config=str(config),
        )
        resources = [
            dict(
                id="server",
                kind="server",
                python=sys.executable,
                methods=[method],
                location="https://example.invalid",
            )
        ]
        self.path.parent.mkdir()
        with patch.object(catalogue, "qualify") as probe:
            catalogue.refresh(self.path, resources)
            sample.write_bytes(b"changed")
            result = catalogue.refresh(self.path, resources, confirm_files=False)
            self.assertIn("confirm", result["operations"][0]["reason"])
            probe.assert_called_once()

    def test_server_error_body_is_never_saved(self):
        result = subprocess.CompletedProcess(
            ["fixture"], 1, "", "Error: token=sample_secret"
        )
        with patch.object(subprocess, "run", return_value=result):
            with self.assertRaisesRegex(
                ValueError, "^Inference fixture failed to return the requested output$"
            ):
                catalogue.run_checked(["vision"], server=True)

    def test_opencv_probe_matches_interpreter_fixture(self):
        self.resources.write_text(
            json.dumps([dict(id="img", kind="opencv", python=sys.executable)])
        )
        result = self.cli("refresh", "--resources", self.resources)
        for row in result["operations"]:
            check = subprocess.run(
                [sys.executable, "-I", SCRIPTS / "opencv_probe.py", row["name"]],
                capture_output=True,
                text=True,
            )
            self.assertEqual(
                row["usable"], json.loads(check.stdout)["status"] == "tested"
            )

    def test_installer_rejects_missing_or_combined_authorization_before_setup(self):
        installer = ROOT / "skills/cad-opencv-setup/scripts/opencv_env.py"
        for extra in (
            [],
            ["--authorization", "Install OpenCV"],
            ["--authorization", "EXECUTE install OpenCV and YOLO"],
        ):
            result = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    installer,
                    "setup",
                    "contours",
                    "--root",
                    self.root / "installer",
                    *extra,
                ],
                capture_output=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((self.root / "installer").exists())
