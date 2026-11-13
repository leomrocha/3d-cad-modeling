import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from calibrated_trace import calibrated_trace  # noqa: E402


class CalibratedTraceTests(unittest.TestCase):
    def test_signed_axes_and_worst_case_uncertainty(self):
        result = calibrated_trace(
            [(12, 8)], (10, 10), (-0.5, 0.25),
            point_uncertainty_px=(2, 2),
            origin_uncertainty_px=(1, 1),
            scale_uncertainty_per_px=(0.01, 0.02), units="mm",
        )[0]
        self.assertEqual(result["coordinates"], [-1.0, -0.5])
        self.assertAlmostEqual(result["uncertainty_worst_case"][0], 1.55)
        self.assertAlmostEqual(result["uncertainty_worst_case"][1], 0.85)
        # Enumerate the endpoints of point, origin and signed-scale intervals.
        nominal = result["coordinates"]
        scales = (-0.5, 0.25)
        point = (12, 8)
        origin = (10, 10)
        point_u = (2, 2)
        origin_u = (1, 1)
        scale_u = (0.01, 0.02)
        for axis in range(2):
            for dp in (-point_u[axis], point_u[axis]):
                for do in (-origin_u[axis], origin_u[axis]):
                    for ds in (-scale_u[axis], scale_u[axis]):
                        actual = (point[axis] + dp - origin[axis] - do) * (scales[axis] + ds)
                        error = abs(actual - nominal[axis])
                        self.assertLessEqual(error, result["uncertainty_worst_case"][axis] + 1e-12)
        self.assertEqual(result["units"], "mm")

    def test_axis_reversal_does_not_make_uncertainty_negative(self):
        result = calibrated_trace(
            [(5, 12)], (5, 10), (1.0, -0.5),
            point_uncertainty_px=1, origin_uncertainty_px=1,
        )[0]
        self.assertEqual(result["coordinates"], [0.0, -1.0])
        self.assertEqual(result["uncertainty_worst_case"], [2.0, 1.0])

    def test_zero_uncertainty_preserves_exact_calibrated_point(self):
        result = calibrated_trace([(5, 7)], (1, 2), (2, 3))[0]
        self.assertEqual(result["coordinates"], [8.0, 15.0])
        self.assertEqual(result["uncertainty_worst_case"], [0.0, 0.0])

    def test_degenerate_or_nonfinite_calibration_is_rejected(self):
        for scale in ((0, 1), (1, float("inf")), (math.nan, 1)):
            with self.subTest(scale=scale), self.assertRaises(ValueError):
                calibrated_trace([(0, 0)], (0, 0), scale)
        with self.assertRaisesRegex(ValueError, "nonfinite calibrated"):
            calibrated_trace([(1e308, 0)], (-1e308, 0), (1e308, 1))

    def test_nonfinite_points_and_negative_uncertainty_are_rejected(self):
        with self.assertRaises(ValueError):
            calibrated_trace([(float("nan"), 0)], (0, 0), (1, 1))
        with self.assertRaises(ValueError):
            calibrated_trace([(0, 0)], (0, 0), (1, 1), point_uncertainty_px=-1)
        with self.assertRaises(ValueError):
            calibrated_trace([(0, 0)], (0, 0), (1, 1), scale_uncertainty_per_px=(0, -0.1))

    def test_wrong_coordinate_dimensions_are_rejected(self):
        with self.assertRaises(ValueError):
            calibrated_trace([(1, 2, 3)], (0, 0), (1, 1))
        with self.assertRaises(ValueError):
            calibrated_trace([(1, 2)], (0, 0, 0), (1, 1))


if __name__ == "__main__":
    unittest.main()
