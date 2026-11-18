import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "format_translation"))
from routes import plan  # noqa: E402
from convert import convert  # noqa: E402
from scad_source import translate  # noqa: E402

PACKAGE = ROOT / "skills/cad-format-translator"


class FormatRoutes(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((PACKAGE / "fixtures/inventory.json").read_text())

    def search(self, required=("mm",), previous=None):
        return plan(
            self.data, "workshop-fixture", "step-solid", "stl-mesh", required, previous
        )

    def test_unfamiliar_import_export_handoff(self):
        result = self.search()
        self.assertEqual(result["status"], "CANDIDATE")
        steps = result["routes"][0]["steps"]
        self.assertEqual(
            [row["tool"] for row in steps], ["acquire_asset", "emit_asset"]
        )
        self.assertEqual(steps[1]["bindings"]["item"], "previous.result.id")
        self.assertEqual(self.search(["analytic-faces"])["status"], "GAP")
        self.data["tools"].pop()
        self.assertEqual(self.search()["status"], "GAP")

    def test_direct_route_and_reverse_direction(self):
        direct = copy.deepcopy(self.data["operations"][1])
        direct.update(
            tool="unfamiliar_direct",
            bindings={"file": "source"},
            **{"from": "step-solid"},
        )
        self.data["tools"].append(
            {"name": direct["tool"], "inputSchema": {"properties": {"file": {}}}}
        )
        self.data["operations"].append(direct)
        self.assertEqual(len(self.search()["routes"][0]["steps"]), 1)
        before = self.search()["binding"]
        self.data["bridge_version"] = "new"
        self.assertEqual(self.search(previous=before)["status"], "STALE")
        self.assertEqual(
            plan(self.data, "workshop-fixture", "stl-mesh", "step-solid", [])["status"],
            "GAP",
        )
        with self.assertRaises(ValueError):
            plan(self.data, "another-connection", "step-solid", "stl-mesh", [])

    def test_missing_runtime_unreachable_and_schema_mismatch(self):
        for change in [
            {"dependencies": ["absent"]},
            {"accessible": False},
            {"bindings": {"wrong": "output"}},
        ]:
            data = copy.deepcopy(self.data)
            data["operations"][1].update(change)
            self.assertEqual(
                plan(data, data["connection"], "step-solid", "stl-mesh", [])["status"],
                "GAP",
            )

    def test_editable_output_and_failure_before_publication(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / "result.py"
            source = PACKAGE / "fixtures/plate.scad"
            receipt = convert("scad-python", source, out)
            self.assertIn("bore = 10.0", out.read_text())
            self.assertIn("polygon(96, bore)", out.read_text())
            self.assertEqual(receipt["checks"]["cylinders"], "polygonal")
            with self.assertRaises(FileExistsError):
                convert("scad-python", source, out)
            bad = Path(temp) / "bad.scad"
            bad.write_text("d=10;\nrotate([0,0,90]) cube([1,2,3]);")
            output = out.with_name("bad.py")
            with self.assertRaisesRegex(ValueError, "bad.scad:2"):
                convert("scad-python", bad, output)
            self.assertFalse(output.exists())
            with self.assertRaisesRegex(ValueError, "trusted"):
                convert("scad-stl", source, out.with_suffix(".stl"))

    def test_extrusion_and_alternative_cylinder(self):
        source = "h=5; linear_extrude(height=h) square([4,3]);"
        self.assertIn("extrude(h)", translate(source, "input.scad"))
        with self.assertRaisesRegex(ValueError, "faceted cylinder"):
            translate("cylinder(h=5,d=3);", "a.scad")
        self.assertIn("circle", translate("cylinder(h=5,d=3);", "a.scad", True))
