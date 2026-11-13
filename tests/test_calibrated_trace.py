import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from calibrated_trace import calibrated_scale_from_reference, calibrated_trace  # noqa: E402


class CalibratedTraceTests(unittest.TestCase):
    def test_reference_scale_bounds_all_uncertainty_endpoints(self):
        result = calibrated_scale_from_reference(
            100, 250, length_uncertainty_mm=2, span_uncertainty_px=3,
        )
        self.assertEqual(result["nominal_scale_mm_per_px"], 0.4)
        lower, upper = result["scale_interval_mm_per_px"]
        self.assertAlmostEqual(lower, 98 / 253)
        self.assertAlmostEqual(upper, 102 / 247)
        self.assertAlmostEqual(
            result["scale_uncertainty_mm_per_px"],
            max(0.4 - lower, upper - 0.4),
        )
        for length in (98, 102):
            for span in (247, 253):
                actual = length / span
                self.assertLessEqual(lower, actual)
                self.assertLessEqual(actual, upper)
                self.assertLessEqual(
                    abs(actual - result["nominal_scale_mm_per_px"]),
                    result["scale_uncertainty_mm_per_px"],
                )

    def test_reference_scale_zero_uncertainty(self):
        result = calibrated_scale_from_reference(25, 100)
        self.assertEqual(result["nominal_scale_mm_per_px"], 0.25)
        self.assertEqual(result["scale_interval_mm_per_px"], [0.25, 0.25])
        self.assertEqual(result["scale_uncertainty_mm_per_px"], 0.0)

    def test_reference_scale_rejects_invalid_endpoints_and_values(self):
        invalid = (
            (0, 10, 0, 0), (-1, 10, 0, 0), (10, 0, 0, 0),
            (10, 10, 10, 0), (10, 10, 0, 10),
            (10, 10, -1, 0), (10, 10, 0, -1),
            (True, 10, 0, 0), (10, False, 0, 0),
            (10, 10, True, 0), (10, 10, 0, False),
            (float("nan"), 10, 0, 0), (10, float("inf"), 0, 0),
            (1e308, 1e-308, 0, 0), (1e308, 10, 1e308, 0),
            (1e308, 1e308, 0, 9e307), (1e-300, 1e300, 0, 0),
        )
        for length, span, length_u, span_u in invalid:
            with self.subTest(length=length, span=span, lu=length_u, su=span_u):
                with self.assertRaises(ValueError):
                    calibrated_scale_from_reference(
                        length, span,
                        length_uncertainty_mm=length_u,
                        span_uncertainty_px=span_u,
                    )

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
