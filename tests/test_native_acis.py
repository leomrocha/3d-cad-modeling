"""Check generic native geometry readers and numeric expectations."""

import importlib.util
from pathlib import Path
import sys
import unittest

TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS.parent / "scripts"))

from feature_checks import comparison, cylinder_pattern
from native_acis import sab_features, sab_structure
from rounded_tube import crossmember_checks


class NativeGeometryExpectations(unittest.TestCase):
    def test_invalid_pattern_expectations_stop_before_comparison(self):
        with self.assertRaises(ValueError):
            cylinder_pattern("missing expected holes", {"cylinders": []}, 13, 2, [], 1e-7)
        with self.assertRaises(ValueError):
            cylinder_pattern("invalid diameter", {"cylinders": []}, float("nan"), 2, [[0, 0]], 1e-7)
        with self.assertRaises(ValueError):
            comparison("empty measurements", [], [], 1e-7)

    def test_parallel_rail_gap_and_midpoint(self):
        rail = {"points": [[0, 0, 0], [10, 0, 0]]}
        crossmember = {"points": [[0, 0, 0], [0, 0, 60]]}
        cases = (
            ("matching gap and datum", crossmember, 80, ["PASS", "PASS"]),
            ("wrong frame width", crossmember, 90, ["FAIL", "PASS"]),
            ("shifted local origin", {"points": [[0, 0, 5], [0, 0, 65]]}, 80, ["PASS", "FAIL"]),
        )
        for label, features, frame_width, expected in cases:
            with self.subTest(label=label):
                checks = crossmember_checks(rail, features, frame_width, 60)["checks"]
                self.assertEqual([check["result"] for check in checks], expected)


@unittest.skipUnless(importlib.util.find_spec("ezdxf"), "requires local ezdxf native reader")
class NativeBinaryTests(unittest.TestCase):
    def setUp(self):
        self.data = (TESTS / "fixtures/sat-sab-persistence/after-reopen.sab").read_bytes()

    def test_truncated_binary_is_rejected(self):
        with self.assertRaises((ValueError, IndexError)):
            sab_features(self.data[:40])

    def test_structure_and_analytic_vertices_agree(self):
        analytic = sab_features(self.data)
        structure = sab_structure(self.data)
        self.assertCountEqual(
            (tuple(point) for point in analytic["points"]),
            (tuple(point) for point in structure["points"]),
        )
        self.assertEqual(analytic["topology"], structure["topology"])


class SatAnalyticSurfaceTests(unittest.TestCase):
    @staticmethod
    def world(values, point=False):
        numbers = [float(x) for x in values]
        return [-numbers[1] + (10 if point else 0), numbers[0], numbers[2]]

    def test_sphere_transform_and_radius(self):
        from native_acis import _sat_curved_surface
        fields = [None, *'1 2 3 5 1 0 0 0 0 1 forward_v'.split()]
        self.assertEqual(_sat_curved_surface('sphere-surface', fields, self.world),
                         {'origin': [8, 1, 3], 'radius': 5})
        fields[4] = 'nan'
        with self.assertRaisesRegex(ValueError, 'radius'):
            _sat_curved_surface('sphere-surface', fields, self.world)

    def test_ring_torus_radii_and_directions(self):
        from native_acis import _sat_curved_surface
        fields = [None, *'2 3 4 1 0 0 8 2 0 0 1 forward_v'.split()]
        self.assertEqual(_sat_curved_surface('torus-surface', fields, self.world),
                         {'center': [7, 2, 4], 'axis': [0, 1, 0],
                          'major_radius': 8, 'minor_radius': 2})
        fields[7] = '1'
        with self.assertRaisesRegex(ValueError, 'ring-shaped'):
            _sat_curved_surface('torus-surface', fields, self.world)
        fields[7] = '8'
        fields[9:12] = ['1', '0', '0']
        with self.assertRaisesRegex(ValueError, 'orthonormal'):
            _sat_curved_surface('torus-surface', fields, self.world)


if __name__ == "__main__":
    unittest.main()
