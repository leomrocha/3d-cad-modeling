"""Optional native CLI readback using the installed skill's source fixture."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from translator.bore_check import verify_bytes


class OpenScadFixture(unittest.TestCase):
    @unittest.skipUnless(shutil.which("openscad"), "Requires OpenSCAD CLI for real mesh generation")
    def test_native_meshes_including_subslice_obstruction(self):
        saved = (Path(__file__).resolve().parents[1] / "skills/cad-mcp-translator/fixtures/plate.scad").read_text()
        through = "translate([17, 23, -1]) cylinder(h=12, d=bore);"
        self.assertEqual(saved.count(through), 1)
        obstructed = ("translate([17,23,-1]) cylinder(h=4.211,d=bore);"
                      "translate([17,23,3.221]) cylinder(h=8,d=bore);")
        cases = [
            ("valid", through, 12, True), ("stale diameter", through, 10, False),
            ("wrong position", through.replace("17, 23", "20, 23"), 12, False),
            ("blind hole", through.replace("h=12", "h=7"), 12, False),
            ("0.010 mm obstruction", obstructed, 12, False),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "plate.scad"
            mesh = source.with_suffix(".stl")
            for name, cutter, diameter, valid in cases:
                with self.subTest(case=name):
                    source.write_text(saved.replace("bore = 10;", f"bore = {diameter};").replace(through, cutter))
                    subprocess.run(["openscad", "--export-format", "asciistl", "-o", mesh, source],
                                   check=True, capture_output=True)
                    if valid:
                        self.assertEqual(verify_bytes(mesh.read_bytes(), 12)["result"], "PASS")
                    else:
                        with self.assertRaises(ValueError):
                            verify_bytes(mesh.read_bytes(), 12)
