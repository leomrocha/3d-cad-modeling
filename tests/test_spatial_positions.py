import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from spatial_positions import generate

BASE = dict(
    unit="mm",
    reference="host revision 1",
    frame=dict(origin=[0, 0, 0], axis=[0, 0, 1], meridian=[1, 0, 0]),
)
CYLINDER = dict(
    kind="cylinder",
    radius=5,
    height=12,
    levels=[0, 12],
    angles_deg=[0, 90, 360],
    orientation=dict(mode="normal", x="azimuth"),
)
SPHERE = dict(
    kind="sphere",
    radius=10,
    rings=[dict(latitude_deg=v) for v in (0, 60, 90, -90)],
    angles_deg=[0, 90, 360],
    orientation=dict(mode="normal", x="azimuth"),
)
PRISM = dict(
    kind="prism",
    vertices=[[0, 0], [4, 0], [0, 3]],
    height=5,
    orientation=dict(mode="fixed", z=[0, 0, 1], x=[1, 0, 0]),
)


def run(spec, **changes):
    return generate({**BASE, **spec, **changes})


class SpatialPositions(unittest.TestCase):
    def test_concave_and_selected_prism_faces_and_edges(self):
        spec = dict(PRISM, vertices=[[0, 0], [4, 0], [4, 1], [1, 1], [1, 4], [0, 4]])
        rows = run(spec, mode="volume", columns=[0.5, 2], rows=[0.5, 2], levels=[1, 3])[
            "positions"
        ]
        self.assertEqual(len(rows), 6)
        for mode, extra, expected in [
            ("side", dict(side=1, stations=[0, 5], levels=[2]), [[4, 0, 2], [0, 3, 2]]),
            ("upright", dict(side=2, levels=[0, 5]), [[0, 3, 0], [0, 3, 5]]),
            ("rim", dict(side=0, stations=[1, 3], levels=[5]), [[1, 0, 5], [3, 0, 5]]),
            ("cap", dict(columns=[1], rows=[1], levels=[0, 5]), [[1, 1, 0], [1, 1, 5]]),
        ]:
            self.assertEqual(
                [p["xyz"] for p in run(PRISM, mode=mode, **extra)["positions"]],
                expected,
            )
        with self.assertRaisesRegex(ValueError, "limit"):
            run(
                PRISM,
                mode="volume",
                columns=list(range(200)),
                rows=list(range(200)),
                levels=[0],
            )

    def test_spherical_spacing_and_pole_frame(self):
        targets = [
            ("P0001", "P0002", "latitude_arc", 5 * math.pi),
            ("P0003", "P0004", "latitude_arc", 2.5 * math.pi),
            ("P0001", "P0003", "great_circle", 10 * math.pi / 3),
            ("P0001", "P0002", "chord", math.sqrt(200)),
        ]
        checks = [
            dict(pair=[a, b], metric=m, distance=d, tolerance=1e-10)
            for a, b, m, d in targets
        ]
        result = run(SPHERE, checks=checks)
        self.assertEqual(len(result["positions"]), 6)
        self.assertEqual(len(result["measurements"]), 4)
        self.assertEqual(result["positions"][4]["xyz"], [0, 0, 10])
        for ring in ([0, 360], [137, 20]):
            pole = run(SPHERE, rings=[dict(latitude_deg=90)], angles_deg=ring)[
                "positions"
            ][0]
            self.assertEqual(
                pole["world_transform"],
                [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 10], [0, 0, 0, 1]],
            )
        checks[0]["distance"] = 0
        with self.assertRaisesRegex(ValueError, "measured"):
            run(SPHERE, checks=checks)

    def test_cylinder_axial_rows_roll_seam_and_fallback(self):
        results = run(
            CYLINDER,
            checks=[
                dict(
                    pair=["P0001", "P0004"],
                    metric="cylinder_surface",
                    distance=math.hypot(12, 2.5 * math.pi),
                    tolerance=1e-9,
                )
            ],
        )
        self.assertEqual(len(results["positions"]), 4)

        def axes(angle):
            mat = run(
                CYLINDER,
                levels=[0],
                angles_deg=[angle],
                orientation=dict(mode="normal", x="azimuth", roll_deg=30),
            )["positions"][0]["world_transform"]
            return [r[:3] for r in mat[:3]]

        for a, b in zip(axes(-0.00001), axes(0.00001)):
            self.assertLess(math.dist(a, b), 1e-6)
        self.assertAlmostEqual(axes(0)[2][0], 0.5)
        pos = run(
            CYLINDER,
            orientation=dict(
                mode="tangent", path="axial", x=[0, 0, 1], fallback_x=[0, 1, 0]
            ),
        )["positions"][0]
        self.assertEqual(
            [r[:3] for r in pos["world_transform"][:3]],
            [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
        )

    def test_decimal_angles_and_reference_identity(self):
        for shape in (
            dict(CYLINDER, levels=[0]),
            dict(SPHERE, rings=[dict(latitude_deg=10)]),
        ):
            result = run(shape, angles_deg=[0.1, 360.1, -359.9, -1e-16, 0, 360])
            self.assertEqual(len(result["positions"]), 2)
        with self.assertRaisesRegex(ValueError, "reference"):
            run(CYLINDER, reference=True)

    def test_translated_winding_and_decimal_boundary(self):
        offset = 1e10
        vertices = [[offset, offset], [offset + 2, offset], [offset, offset + 2]]
        for polygon, side in [(vertices, 0), (vertices[::-1], 1)]:
            result = run(
                PRISM,
                vertices=polygon,
                mode="side",
                levels=[1],
                side=side,
                stations=[1],
                orientation=dict(mode="normal", x=[0, 0, 1]),
            )
            self.assertEqual(
                [r[2] for r in result["positions"][0]["world_transform"][:3]],
                [0, -1, 0],
            )
        result = run(
            PRISM,
            vertices=[[0, 0], [0.1, 0], [0, 0.1]],
            mode="cap",
            levels=[0],
            columns=[0.08],
            rows=[0.02, 0.020000001],
        )
        self.assertEqual([p["xyz"] for p in result["positions"]], [[0.08, 0.02, 0]])

    def test_world_chord_and_large_radii(self):
        check = dict(pair=["P0001", "P0002"], metric="chord", distance=1, tolerance=0)
        with self.assertRaisesRegex(ValueError, "measured 0"):
            run(
                PRISM,
                mode="rim",
                side=0,
                stations=[0, 1],
                levels=[0],
                frame=dict(BASE["frame"], origin=[1e16, 0, 0]),
                checks=[check],
            )
        for metric, shape in [
            ("great_circle", SPHERE),
            ("latitude_arc", SPHERE),
            ("cylinder_surface", CYLINDER),
        ]:
            check.update(metric=metric, distance=1e155 * math.pi / 12, tolerance=1e140)
            run(
                shape,
                rings=[dict(latitude_deg=0)],
                levels=[0],
                angles_deg=[45, 60],
                radius=1e155,
                checks=[check],
            )
            check.update(distance=0, tolerance=1e308)
            with self.assertRaisesRegex(ValueError, "measured inf"):
                run(
                    shape,
                    rings=[dict(latitude_deg=0)],
                    levels=[0],
                    angles_deg=[0, 180],
                    radius=1e308,
                    checks=[check],
                )

    @unittest.skipUnless(
        shutil.which("openscad"), "CAD readback requires local OpenSCAD"
    )
    def test_cli_with_reopened_rotated_mirrored_plate(self):
        # Measure the existing asymmetric plate. Write a temporary assembly using its actual mesh.
        plate = ROOT / "tests/fixtures/mesh-position/plate-10.stl"

        def vertices(path):
            return {
                tuple(map(float, line.split()[1:]))
                for line in path.read_text().splitlines()
                if line.strip().startswith("vertex ")
            }

        source = vertices(plate)
        width, depth, height = [max(v[i] for v in source) for i in range(3)]
        self.assertEqual([width, depth, height], [60, 40, 10])
        parent = [[0, -1, 0, 20], [-1, 0, 0, 30], [0, 0, 1, 5], [0, 0, 0, 1]]
        request = dict(BASE, **CYLINDER)
        request.update(
            reference=plate.name,
            radius=5,
            levels=[0],
            angles_deg=[0],
            frame=dict(origin=[0, 0, height], axis=[0, 1, 0], meridian=[0, 0, 1]),
            parent_to_world=parent,
        )
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            inp = directory / "job.json"
            inp.write_text(json.dumps(request))
            result = json.loads(
                subprocess.check_output(
                    [sys.executable, ROOT / "scripts/spatial_positions.py", inp]
                )
            )
            occurrence = result["positions"][0]
            self.assertEqual(occurrence["hand"], "MIRRORED")
            # Source X maps to -world Y, source Y maps to -world X, source Z maps to world Z.
            expected = [[0, -1, 0, 20], [-1, 0, 0, 30], [0, 0, 1, 20], [0, 0, 0, 1]]
            self.assertEqual(occurrence["world_transform"], expected)
            scad = directory / "assembly.scad"
            scad.write_text(
                f"multmatrix({parent}) multmatrix({occurrence['parent_transform']}) import({json.dumps(str(plate))});"
            )
            output = directory / "reopened.stl"
            subprocess.run(
                ["openscad", "--export-format", "asciistl", "-o", output, scad],
                check=True,
                capture_output=True,
            )
            observed = vertices(output)
            predicted = {(20 - y, 30 - x, 20 + z) for x, y, z in source}
            self.assertEqual(len(observed), len(predicted))
            for point in predicted:
                self.assertLess(min(math.dist(point, q) for q in observed), 0.0001)


if __name__ == "__main__":
    unittest.main()
