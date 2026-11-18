import unittest

from scripts.feature_checks import feature_vertices


class FeatureVertices(unittest.TestCase):
    def test_reopened_points_can_be_reordered_and_include_other_geometry(self):
        r = feature_vertices("seat", [(10, 2, 3), (0, 1, 0), (10, 2, 3)],
                             [(0, 1, 0.125), (10, 2, 3)], 0.125)
        self.assertEqual(r["result"], "PASS")
        self.assertEqual(r["corners"][0]["distance_mm"], 0.125)

    def test_missing_moved_or_collapsed_corners_fail(self):
        for reopened in [[], [(0, 0, 0)], [(0, 0, 0), (3, 0, 0)]]:
            with self.subTest(reopened=reopened):
                self.assertEqual(feature_vertices("seat", reopened, [(0, 0, 0), (1, 0, 0)], 1)["result"], "FAIL")

    def test_invalid_inputs(self):
        for target in [[], [(0, 0, 0)] * 2, [(0, 0)], [(0, 0, float("nan"))]]:
            with self.assertRaises(ValueError):
                feature_vertices("seat", [], target, 0.01)
