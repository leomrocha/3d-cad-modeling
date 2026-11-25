import unittest

from scripts.feature_checks import axis_aligned_edge_coverage, feature_vertices


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


class AxisAlignedEdgeCoverage(unittest.TestCase):
    def test_split_overlapping_and_reversed_edges_match_coverage(self):
        whole = [((0, 2, 3), (8, 2, 3)), ((8, 2, 3), (8, 6, 3))]
        split = [((8, 6, 3), (8, 2, 3)), ((8, 2, 3), (4, 2, 3)),
                 ((0, 2, 3), (4, 2, 3)), ((2, 2, 3), (6, 2, 3))]
        self.assertEqual(axis_aligned_edge_coverage(whole, decimal_places=5),
                         axis_aligned_edge_coverage(split, decimal_places=5))

    def test_gaps_and_additional_lines_are_detectable(self):
        whole = [((0, 2, 3), (8, 2, 3))]
        incomplete = [((0, 2, 3), (3.999, 2, 3)), ((4, 2, 3), (8, 2, 3))]
        additional = [*whole, ((2, 2, 3), (2, 3, 3))]
        for alternate in (incomplete, additional):
            self.assertNotEqual(axis_aligned_edge_coverage(whole, decimal_places=5),
                                axis_aligned_edge_coverage(alternate, decimal_places=5))

    def test_refuses_degenerate_diagonal_and_nonfinite_inputs(self):
        for invalid in ([], [((0,0,0),(0,0,0))], [((0,0,0),(1,1,0))],
                        [((0,0,0),(float("inf"),0,0))]):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                axis_aligned_edge_coverage(invalid, decimal_places=5)
