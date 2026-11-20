from importlib.util import find_spec
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from planar_positions import generate  # noqa: E402


FRAME = {"origin": [10, -2, 5], "x": [0, 1, 0], "y": [0, 0, 1]}
BASE = {"unit": "mm", "frame": FRAME, "reference": "test plane", "tolerance": 1e-7}


def rows(**spec):
    return generate(dict(BASE, **spec))["positions"]


requires_bezier = unittest.skipUnless(
    find_spec("numpy") and find_spec("scipy"), "Bezier requires NumPy and SciPy"
)
requires_interior = unittest.skipUnless(
    find_spec("shapely"), "Interior geometry requires Shapely"
)


class PlanarPositions(unittest.TestCase):
    def test_actual_dxf_line_cli(self):
        # This fixture is a unitless drawing. Declare its length unit for this job.
        fixture = ROOT / "tests/fixtures/catalogue-refresh/assembly-view.dxf"
        values = fixture.read_text().splitlines()
        pairs = list(zip(map(int, values[::2]), (s.strip() for s in values[1::2])))
        start = pairs.index((0, "LINE")) + 1
        end = next(i for i in range(start, len(pairs)) if pairs[i][0] == 0)
        line = dict(pairs[start:end])
        points = [[float(line[x]), float(line[y])] for x, y in ((10, 20), (11, 21))]
        spec = dict(
            BASE,
            kind="path",
            measure="path",
            pitch=2.5,
            orientation="tangent",
            reference="assembly-view.dxf modelspace LINE on layer 0",
            segments=[{"kind": "line", "points": points}],
        )
        with tempfile.TemporaryDirectory() as tmp:
            request = Path(tmp) / "request.json"
            request.write_text(json.dumps(spec))
            output = subprocess.check_output(
                [sys.executable, str(ROOT / "scripts/planar_positions.py"), request]
            )
        positions = json.loads(output)["positions"]
        self.assertEqual([p["station"] for p in positions], [0, 2.5, 5, 7.5, 10])
        self.assertEqual(positions[0]["xyz"], [10, -2, 5])
        self.assertEqual(positions[-1]["xyz"], [10, 8, 5])
        self.assertEqual(positions[-1]["direction_xyz"], FRAME["x"])

    def test_explicit_order_ids_and_direction(self):
        pts = [
            {"id": "B", "xy": [2, 4], "direction": [0, 2]},
            {"id": "A", "xy": [-1, 0]},
        ]
        positions = rows(kind="explicit", positions=pts)
        self.assertEqual([p["id"] for p in positions], ["B", "A"])
        self.assertEqual(positions[0]["direction_xyz"], FRAME["y"])
        with self.assertRaises(ValueError):
            rows(kind="explicit", positions=[pts[0], pts[0]])

    def test_arc_chord_against_arc_length(self):
        spec = dict(
            kind="path",
            pitch=5.0,
            segments=[
                dict(
                    kind="arc", centre=[0, 0], radius=5.0, start_deg=180, sweep_deg=-180
                )
            ],
        )
        along, direct = [rows(**spec, measure=m) for m in ("path", "chord")]
        self.assertEqual(len(along), 4)
        self.assertAlmostEqual(along[-1]["station"], 15)
        self.assertEqual(len(direct), 4)
        self.assertAlmostEqual(direct[-1]["xy"][0], 5)
        for a, b in zip(direct, direct[1:]):
            self.assertAlmostEqual(math.dist(a["xy"], b["xy"]), 5)
        for a, b in zip(along, along[1:]):
            self.assertAlmostEqual(
                2 * 5 * math.asin(math.dist(a["xy"], b["xy"]) / 10), 5
            )

    @requires_bezier
    def test_uneven_bezier_parameter_and_chords(self):
        # Quadratic Bezier (x,y)=(t,t²); integrate sqrt(1+4t²) independently.
        spec = dict(
            kind="path",
            segments=[dict(kind="bezier", points=[[0, 0], [0.5, 0], [1, 1]])],
            pitch=0.2,
        )
        for i, p in enumerate(rows(**spec, measure="path")):
            x, y = p["xy"]
            self.assertAlmostEqual(y, x * x)
            self.assertAlmostEqual(
                x * math.sqrt(1 + 4 * x * x) / 2 + math.asinh(2 * x) / 4, i * 0.2
            )
        direct = rows(**spec, measure="chord")
        for a, b in zip(direct, direct[1:]):
            self.assertAlmostEqual(math.dist(a["xy"], b["xy"]), 0.2)
        self.assertTrue(
            all(a["station"] < b["station"] for a, b in zip(direct, direct[1:]))
        )

    def test_polygon_corner_order_seam_and_restarts(self):
        spec = dict(
            kind="polygon",
            vertices=[[0, 0], [4, 0], [4, 2], [0, 2]],
            mode="sides",
            pitch=2,
            measure="path",
            orientation="tangent",
        )
        with self.assertRaisesRegex(ValueError, "corner_tangent"):
            rows(**spec, spacing="continuous")
        positions = rows(**spec, spacing="continuous", corner_tangent="incoming")
        self.assertEqual(len(positions), 6)
        self.assertEqual(positions[2]["direction_xyz"], FRAME["x"])
        self.assertEqual(positions[-1]["xy"], [0, 2])
        self.assertEqual(
            len(rows(**spec, spacing="restart", corner_tangent="outgoing")), 6
        )
        repeated = rows(
            **spec, spacing="restart", corner_tangent="outgoing", duplicates=True
        )
        self.assertEqual(len(repeated), 10)
        selected = dict(spec, sides=[3, 0], pitch=3)
        self.assertEqual(
            [
                r["xy"]
                for r in rows(
                    **selected, spacing="continuous", corner_tangent="outgoing"
                )
            ],
            [[0, 2], [1, 0], [4, 0]],
        )
        self.assertEqual(
            [
                r["xy"]
                for r in rows(**selected, spacing="restart", corner_tangent="outgoing")
            ],
            [[0, 2], [0, 0], [3, 0]],
        )
        triangle = rows(
            kind="polygon", vertices=[[0, 0], [2, 0], [1, 2]], mode="vertices"
        )
        self.assertEqual(len(triangle), 3)

    def test_circle_rotated_plane_and_seam(self):
        spec = dict(kind="circle", centre=[1, 2], radius=4, start_deg=90, order="cw")
        for distribution in (
            dict(count=4),
            dict(increment_deg=90),
            dict(angles_deg=[0, 90, 180, 270, 360]),
        ):
            pos = rows(**spec, **distribution)
            self.assertEqual(len(pos), 4)
            self.assertAlmostEqual(pos[0]["xyz"][2], 11)
            self.assertAlmostEqual(pos[1]["xy"][0], 5)
            self.assertAlmostEqual(pos[-1]["xy"][0], -3)

    @requires_interior
    def test_footprint_crossing_boundary_and_cutout(self):
        spec = dict(
            kind="interior",
            layout="rows",
            origin=[0, 0],
            pitch_xy=[1, 2],
            outer=dict(kind="polygon", vertices=[[0, 0], [12, 0], [12, 4], [0, 4]]),
            cutouts=[dict(kind="circle", centre=[6, 2], radius=1)],
            clearance=0.1,
        )

        def xy(**args):
            return [r["xy"] for r in rows(**spec, **args)]

        self.assertIn([4, 2], xy(containment="centre"))
        disk = dict(kind="circle", centre=[0, 0], radius=1)
        self.assertEqual(
            xy(containment="footprint", footprint=disk),
            [[2, 2], [3, 2], [9, 2], [10, 2]],
        )
        rect = dict(
            kind="polygon", vertices=[[-3, -0.5], [3, -0.5], [3, 0.5], [-3, 0.5]]
        )
        self.assertEqual(xy(containment="footprint", footprint=rect), [])
        # An opening wholly enclosed by a rectangle also excludes the rectangle.
        spec.update(
            outer=dict(kind="circle", centre=[0, 0], radius=10),
            cutouts=[
                dict(kind="polygon", vertices=[[-0.2, -0.2], [0.2, -0.2], [0, 0.2]])
            ],
        )
        self.assertNotIn([0, 0], xy(containment="footprint", footprint=rect))

    @requires_interior
    def test_concentric_rings_circle_containment(self):
        rings = [
            dict(centre=[1, 2], radius=r, count=4, start_deg=0, order="ccw")
            for r in (3, 5)
        ]
        spec = dict(
            kind="interior",
            outer=dict(kind="circle", centre=[1, 2], radius=5.5),
            layout="rings",
            rings=rings,
            clearance=0.5,
        )
        self.assertEqual(len(rows(**spec, containment="centre")), 8)
        pos = rows(
            **spec,
            containment="footprint",
            footprint=dict(kind="circle", centre=[0, 0], radius=0.25),
        )
        self.assertEqual(len(pos), 4)
        self.assertEqual({r["ring"] for r in pos}, {0})

    def test_full_arc_closes_once_and_bounds_requests(self):
        arc = dict(
            kind="arc", centre=[2.0, 3.0], radius=1.0, start_deg=10.0, sweep_deg=360.0
        )
        spec = dict(kind="path", segments=[arc], pitch=math.pi / 2, measure="path")
        self.assertEqual(len(rows(**spec)), 4)
        self.assertEqual(len(rows(**spec, duplicates=True)), 5)
        for pitch, measure in [(1e-6, "path"), (1e-6, "chord")]:
            if measure == "chord":
                # Exceed total count on a straight segment to keep the check independent of arc numerics.
                segments = [dict(kind="line", points=[[0, 0], [1, 0]])]
            else:
                segments = [arc]
            with self.assertRaisesRegex(ValueError, "limit"):
                rows(kind="path", segments=segments, pitch=pitch, measure=measure)
        for field in [dict(count=10**20), dict(increment_deg=1e-300)]:
            with self.assertRaisesRegex(ValueError, "limit"):
                rows(
                    kind="circle",
                    centre=[0, 0],
                    radius=1,
                    order="cw",
                    start_deg=0,
                    **field,
                )

    def test_selected_side_tangent_and_repeated_side(self):
        spec = dict(
            kind="polygon",
            vertices=[[0, 0], [2, 0], [2, 3], [0, 3]],
            mode="sides",
            measure="path",
            spacing="restart",
            pitch=1,
            orientation="tangent",
        )
        pos = rows(**spec, sides=[1])
        self.assertEqual([r["direction_xyz"] for r in pos], [FRAME["y"]] * 4)
        with self.assertRaisesRegex(ValueError, "Repeated"):
            rows(**spec, sides=[1, 1])

    @requires_bezier
    def test_endpoint_bezier_tangents(self):
        for points in (
            [[0, 0], [0, 0], [2, 0]],
            [[0, 0], [2, 0], [2, 0]],
            [[0, 0], [0, 0], [0, 0], [2, 0]],
        ):
            pos = rows(
                kind="path",
                segments=[dict(kind="bezier", points=points)],
                measure="path",
                pitch=1,
                orientation="tangent",
            )
            self.assertEqual([r["direction_xyz"] for r in pos], [FRAME["x"]] * 3)

    @requires_interior
    def test_interior_tangent_offset_footprint_and_grid_limit(self):
        spec = dict(
            kind="interior",
            outer=dict(kind="polygon", vertices=[[0, 0], [6, 0], [6, 2], [0, 2]]),
            clearance=0,
            containment="footprint",
            orientation="tangent",
        )
        bar = dict(
            kind="polygon",
            vertices=[[-0.8, -0.1], [0.8, -0.1], [0.8, 0.1], [-0.8, 0.1]],
        )
        ring = dict(centre=[3, 1], radius=0.7, count=4, start_deg=0, order="ccw")
        pos = rows(**spec, layout="rings", rings=[ring], footprint=bar)
        self.assertEqual(len(pos), 4)
        self.assertEqual(pos[0]["direction_xyz"], FRAME["y"])
        blocked = dict(kind="circle", centre=[3.7, 1.6], radius=0.15)
        accepted = rows(
            **spec, layout="rings", rings=[ring], footprint=bar, cutouts=[blocked]
        )
        self.assertNotIn(pos[0]["xy"], [p["xy"] for p in accepted])
        straight = rows(
            **spec,
            layout="rings",
            rings=[dict(ring, orientation=None)],
            footprint=bar,
            cutouts=[blocked],
        )
        self.assertIn(pos[0]["xy"], [p["xy"] for p in straight])
        offset = dict(kind="circle", centre=[3, 0], radius=0.4)
        pos = rows(
            **spec, layout="rows", origin=[0, 1], pitch_xy=[1, 2], footprint=offset
        )
        self.assertEqual([p["xy"] for p in pos], [[x, 1] for x in range(-2, 3)])
        self.assertTrue(all(p["direction_xyz"] == FRAME["x"] for p in pos))
        with self.assertRaisesRegex(ValueError, "limit"):
            rows(
                **spec,
                layout="rows",
                origin=[0, 1],
                pitch_xy=[1e-100, 1],
                footprint=offset,
            )

    def test_cli_with_standard_library_only(self):
        def run(spec):
            with tempfile.TemporaryDirectory() as tmp:
                request = Path(tmp) / "request.json"
                request.write_text(json.dumps(dict(BASE, **spec)))
                return subprocess.run(
                    [
                        sys.executable,
                        "-S",
                        str(ROOT / "scripts/planar_positions.py"),
                        request,
                    ],
                    capture_output=True,
                    text=True,
                )

        polygon = run(
            dict(kind="polygon", mode="vertices", vertices=[[0, 0], [1, 0], [1, 1]])
        )
        self.assertEqual(polygon.returncode, 0, polygon.stderr)
        self.assertEqual(len(json.loads(polygon.stdout)["positions"]), 3)
        for spec, message in [
            (dict(kind="interior"), "Shapely"),
            (
                dict(
                    kind="path",
                    segments=[dict(kind="bezier", points=[[0, 0], [1, 0], [1, 1]])],
                ),
                "SciPy",
            ),
        ]:
            failure = run(spec)
            self.assertEqual(failure.returncode, 2)
            self.assertEqual(failure.stdout, "")
            self.assertIn(message, failure.stderr)
