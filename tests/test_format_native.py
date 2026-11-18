"""Actual optional CAD runtimes. Use CADQUERY_PYTHON and BUILD123D_PYTHON to run."""

import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "format_translation/convert.py"
FIXTURE = ROOT / "skills/cad-format-translator/fixtures/plate.scad"
CQ = os.environ.get("CADQUERY_PYTHON")
READER = os.environ.get("BUILD123D_PYTHON")


def run(python, mode, source, target, *options):
    result = subprocess.check_output(
        [python, "-B", TOOL, mode, source, target, *options], text=True
    )
    return json.loads(result)


@unittest.skipUnless(
    CQ and READER and shutil.which("openscad"),
    "Requires local CadQuery, build123d and OpenSCAD",
)
class NativeRoutes(unittest.TestCase):
    def test_editable_program_and_independent_solid_reader(self):
        with tempfile.TemporaryDirectory() as folder:
            job = Path(folder)
            generated = job / "editable.py"
            run(sys.executable, "scad-python", FIXTURE, generated)
            for diameter in (10, 12):
                with self.subTest(diameter=diameter):
                    source = job / f"p{diameter}.scad"
                    source.write_text(
                        FIXTURE.read_text().replace("bore = 10;", f"bore = {diameter};")
                    )
                    target = job / f"p{diameter}.py"
                    target.write_text(
                        generated.read_text().replace(
                            "bore = 10.0", f"bore = {diameter}.0"
                        )
                    )
                    mesh = source.with_suffix(".stl")
                    a = run(
                        sys.executable, "scad-stl", source, mesh, "--trusted-source"
                    )["checks"]
                    facet_check = subprocess.check_output(
                        [
                            sys.executable,
                            "-B",
                            ROOT / "translator/bore_check.py",
                            mesh,
                            "--diameter-mm",
                            str(diameter),
                        ],
                        text=True,
                    )
                    self.assertEqual(json.loads(facet_check)["result"], "PASS")
                    step = source.with_suffix(".step")
                    b = run(CQ, "python-step", target, step, "--trusted-source")[
                        "checks"
                    ]
                    self.assertAlmostEqual(
                        a["signed_volume_mm3"], b["volume_mm3"], delta=0.03
                    )
                    self.assertEqual(b["cylinder_radii_mm"], [])
                    self.assertEqual(a["bounds_mm"], b["bounds_mm"])
                    # Preserve the faceted bore position/diameter, not just the volume.
                    translated_mesh = job / f"cq-{diameter}.stl"
                    run(CQ, "step-stl", step, translated_mesh)
                    observed = subprocess.check_output(
                        [
                            sys.executable,
                            "-B",
                            ROOT / "translator/bore_check.py",
                            translated_mesh,
                            "--diameter-mm",
                            str(diameter),
                        ],
                        text=True,
                    )
                    self.assertEqual(json.loads(observed)["result"], "PASS")
            analytic = job / "analytic.py"
            run(
                sys.executable, "scad-python", FIXTURE, analytic, "--analytic-cylinders"
            )
            step = job / "analytic.step"
            run(CQ, "python-step", analytic, step, "--trusted-source")
            inspect = (
                "import build123d as b,json,sys; s=b.import_step(sys.argv[1]); "
                "print(json.dumps([len(s.solids()),s.volume,[f.radius for f in s.faces() "
                "if f.geom_type==b.GeomType.CYLINDER]]))"
            )
            count, volume, radii = json.loads(
                subprocess.check_output([READER, "-B", "-c", inspect, step], text=True)
            )
            self.assertEqual((count, radii), (1, [5.0]))
            self.assertAlmostEqual(volume, 24000 - math.pi * 250, places=6)

    def test_assembly(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "assembly.py"
            source.write_text(
                "import cadquery as cq\nmodel=cq.Assembly(name='fixture')\n"
                "group=cq.Assembly(name='group')\npart=cq.Workplane('XY').box(2,3,4)\n"
                "group.add(part,name='first')\n"
                "group.add(part,name='second',loc=cq.Location((10,20,30),(0,0,1),45))\n"
                "model.add(group,loc=cq.Location((2,0,0)))\n"
            )
            checks = run(
                CQ,
                "python-step",
                source,
                source.with_suffix(".step"),
                "--trusted-source",
            )["checks"]
            self.assertEqual(checks["placements"], "PASS")
            self.assertIn(["fixture", "group", "second"], checks["assembly_paths"])
