import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from row_spacing import resolve, run  # noqa: E402
from spatial_positions import generate  # noqa: E402

BASE = dict(
    unit="mm",
    tolerance=1e-8,
    reference="test plate, lower edge",
    frame=dict(origin=[1, 2, 3], x=[0, 1, 0], y=[0, 0, 1]),
    segment=dict(kind="line", points=[[0, 0], [60, 0]]),
    margins=[0, 0],
    margin_reference="face",
    include_endpoints=[True, True],
)


class RowSpacing(unittest.TestCase):
    def test_unequal_bars_on_existing_plate(self):
        source = ROOT / "tests/fixtures/mesh-position/plate-10.stl"
        xs = [
            float(row.split()[1])
            for row in source.read_text().splitlines()
            if row.strip().startswith("vertex ")
        ]
        request = dict(
            BASE,
            segment=dict(kind="line", points=[[min(xs), 0], [max(xs), 0]]),
            width=[4, 8, 12],
            count=3,
            gap={"value": 1, "unit": "cm"},
            remainder="split",
        )
        result = resolve(request)
        self.assertEqual(result["stations"], [10, 26, 46])
        self.assertEqual(result["positions"][-1]["xyz"], [1, 48, 3])
        self.assertEqual(result["margins"], [8, 8])
        self.assertEqual(result["gaps"], [10, 10])
        self.assertEqual(result, resolve(dict(request, gap=10)))
        with self.assertRaisesRegex(ValueError, "residual"):
            resolve(dict(request, remainder="fit"))

    def test_fit_repeat_single_and_closed(self):
        req = dict(BASE, width=4, remainder="end", pitch=15)
        self.assertEqual(resolve(req)["stations"], [2, 17, 32, 47])
        self.assertEqual(resolve(dict(req, remainder="split"))["margins"], [5.5, 5.5])
        fit = dict(
            BASE, width=0, count=2, include_endpoints=[False, False], remainder="fit"
        )
        self.assertEqual(resolve(fit)["stations"], [20, 40])
        self.assertEqual(resolve(dict(fit, count=1, anchor="centre"))["stations"], [30])
        with self.assertRaisesRegex(ValueError, "anchor"):
            resolve(dict(fit, count=1))
        with self.assertRaisesRegex(ValueError, "crosses"):
            resolve(
                dict(
                    BASE,
                    count=2,
                    width=10,
                    remainder="fit",
                    margin_reference="centre",
                    containment="complete",
                )
            )
        circle = dict(
            BASE,
            segment=dict(
                kind="arc", radius=10, centre=[0, 0], start_deg=0, sweep_deg=360
            ),
            count=4,
            include_endpoints=[True, False],
            margin_reference="centre",
            remainder="fit",
        )
        result = resolve(circle)
        self.assertEqual(result["intervals"], 4)
        for pitch in result["pitches"]:
            self.assertAlmostEqual(pitch, 5 * math.pi)

    def test_angled_faces_and_curved_profiles(self):
        polys = {
            "a": {"kind": "polygon", "vertices": [[0, 0], [1, -1], [6, 4], [5, 5]]},
            "b": {"kind": "polygon", "vertices": [[4, 0], [5, -1], [10, 4], [9, 5]]},
        }
        req = dict(
            kind="surface_check",
            unit="mm",
            reference="placed outlines",
            tolerance=1e-8,
            profiles=polys,
        )
        pair = ["a", "b"]
        checks = [
            dict(pair=pair, metric="shortest", expected=math.sqrt(2)),
            dict(pair=pair, metric="directed", direction=[1, 0], expected=2),
        ]
        self.assertEqual(len(run(dict(req, checks=checks))["checks"]), 2)
        circles = {
            k: dict(kind="circle", centre=c, radius=2)
            for k, c in zip(pair, [[0, 0], [6, 2]])
        }
        checks[1]["expected"] = 6 - math.sqrt(12)
        run(dict(req, profiles=circles, checks=checks[1:]))

    def test_spatial_spheres(self):
        points = generate(
            dict(
                reference="cylinder",
                unit="mm",
                frame=dict(origin=[0, 0, 0], axis=[0, 0, 1], meridian=[1, 0, 0]),
                kind="cylinder",
                radius=10,
                height=2,
                angles_deg=[0, 90],
                levels=[1],
                orientation=dict(mode="normal", x="azimuth"),
            )
        )["positions"]
        profiles = {
            p["id"]: dict(kind="sphere", centre=p["xyz"], radius=2) for p in points
        }
        checks = [
            dict(metric="shortest", pair=list(profiles), expected=math.sqrt(200) - 4)
        ]
        run(
            dict(
                kind="surface_check",
                profiles=profiles,
                checks=checks,
                reference="world",
                unit="mm",
                tolerance=1e-8,
            )
        )

    def test_closed_seams_and_numeric_readback(self):
        ring = dict(
            BASE,
            count=3,
            pitch=20,
            include_endpoints=[True, False],
            margin_reference="centre",
            segment=dict(
                kind="arc", radius=10, centre=[0, 0], start_deg=0, sweep_deg=360
            ),
            remainder="split",
        )
        result = resolve(ring)
        self.assertEqual(result["stations"][0], 0)
        self.assertAlmostEqual(result["pitches"][0], result["pitches"][-1])
        loop = dict(
            ring,
            segment=dict(kind="bezier", points=[[0, 0], [2, 4], [4, 1], [0, 0]]),
            remainder="fit",
        )
        del loop["pitch"]
        self.assertEqual(resolve(loop)["intervals"], 3)
        line = dict(BASE, width=0, count=2, pitch=60 + 1e-9, remainder="fit")
        self.assertEqual(resolve(line)["stations"][-1], 60)
        self.assertEqual(resolve(line)["margins"][-1], 0)
        with self.assertRaisesRegex(ValueError, "World coordinates"):
            resolve(
                dict(line, frame=dict(origin=[1e18, 0, 0], x=[1, 0, 0], y=[0, 1, 0]))
            )

    def test_round_distances_and_work_bounds(self):
        def sphere(x):
            return dict(kind="sphere", centre=[x, 0, 0], radius=1e155)

        check = dict(
            metric="directed", pair=["a", "b"], direction=[1, 0, 0], expected=2e155
        )
        req = dict(
            kind="surface_check",
            unit="mm",
            profiles={"a": sphere(0), "b": sphere(4e155)},
            reference="large spheres",
            tolerance=1e142,
            checks=[check],
        )
        row = run(req)["checks"][0]
        self.assertAlmostEqual(row["measured"] / row["expected"], 1)
        self.assertEqual(row["direction"], check["direction"])
        req["profiles"]["b"] = sphere(0)
        with self.assertRaisesRegex(ValueError, "nonzero"):
            run(dict(req, checks=[dict(check, direction=[0, 0, 0], expected=0)]))
        with self.assertRaisesRegex(ValueError, "4096"):
            run(dict(req, checks=[check] * 4097))
        polygon = dict(kind="polygon", vertices=[[0, 0]] * 1000)
        with self.assertRaisesRegex(ValueError, "aggregate"):
            run(dict(req, profiles={"a": polygon, "b": polygon}))
        with self.assertRaisesRegex(ValueError, "one width"):
            resolve(dict(BASE, width=[None] * 50000, count=2))
