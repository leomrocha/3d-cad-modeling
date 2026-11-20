"""Exercise first use, dependency checks, fallback selection and refresh through the CLI."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

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
        self.assertEqual([r["name"] for r in self.cli("routes", "contours")], ["trace"])
        self.assertEqual([r["name"] for r in self.cli("routes", "box")], ["locate"])
        self.assertEqual(self.cli("refresh")["became_available"], [])
        self.cli("failed", "drawing", "trace", "Source tracing tool closed")
        self.assertEqual(self.cli("routes", "contours"), [])
        self.assertEqual(
            self.cli("refresh")["became_available"], [["drawing", "trace"]]
        )
        self.resources.write_text("[]")
        self.assertEqual(
            self.cli("refresh", "--resources", self.resources)["resources"], []
        )

    def test_actual_intake_can_be_removed_and_rechecked(self):
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

    def test_opencv_probe_matches_interpreter_dependencies(self):
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
                row["usable"], json.loads(check.stdout)["status"] == "available"
            )
