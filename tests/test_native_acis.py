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


if __name__ == "__main__":
    unittest.main()
