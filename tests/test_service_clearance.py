"""Continuous screening and exact same-definition witness regressions."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from service_clearance import shared_definition_coincidence, translation_box_window


def placement(x=0, y=0, z=0):
    return [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]


class ServiceClearance(unittest.TestCase):
    box = [[0, 0, 0], [1, 1, 1]]

    def test_between_pose_candidate_for_both_travel_signs(self):
        upper = [[0, 0, 2], [1, 1, 3]]
        for moving, fixed, travel in [(self.box, upper, 4), (upper, self.box, -4)]:
            self.assertEqual(
                translation_box_window(moving, fixed, [0, 0, travel])["candidate_fraction"],
                ["1/4", "3/4"],
            )

    def test_cross_axis_windows_must_intersect(self):
        fixed = [[2, 5, 0], [3, 6, 1]]
        self.assertEqual(translation_box_window(self.box, fixed, [6, 6, 0])["result"],
                         "DISJOINT_BOUNDS")

    def test_endpoint_touch_and_zero_thickness(self):
        fixed = [[1, 1, 3], [1, 1, 3]]
        self.assertEqual(translation_box_window(self.box, fixed, [0, 0, 2])["candidate_fraction"],
                         ["1", "1"])

    def test_static_separation_and_short_travel(self):
        for fixed, displacement in [([[2, 0, 0], [3, 1, 1]], [0, 0, 4]),
                                    ([[0, 0, 4], [1, 1, 5]], [0, 0, 2])]:
            self.assertEqual(translation_box_window(self.box, fixed, displacement)["result"],
                             "DISJOINT_BOUNDS")

    def test_static_overlap_covers_full_interval(self):
        self.assertEqual(translation_box_window(self.box, self.box, [0, 0, 0])["candidate_fraction"],
                         ["0", "1"])

    def test_witness_fraction_and_starting_coincidence(self):
        self.assertEqual(shared_definition_coincidence(placement(), placement(2, 0, 3),
                         [4, 0, 6])["travel_fraction"], "1/2")
        self.assertEqual(shared_definition_coincidence(placement(), placement(),
                         [0, 0, 0])["travel_fraction"], "0")

    def test_wrong_offset_linear_matrix_or_travel(self):
        changed = placement(z=3)
        changed[0][0] = 2
        for fixed in [placement(y=1, z=3), placement(z=7), changed]:
            self.assertEqual(shared_definition_coincidence(placement(), fixed, [0, 0, 6])["result"],
                             "NO_COINCIDENCE_WITNESS")
        self.assertEqual(shared_definition_coincidence(placement(), placement(2, 0, 3),
                         [4, 0, 5])["result"], "NO_COINCIDENCE_WITNESS")

    def test_rejects_invalid_data(self):
        with self.assertRaises(ValueError):
            translation_box_window(self.box[::-1], self.box, [0, 0, 1])
        with self.assertRaises(ValueError):
            translation_box_window(self.box, self.box, [True, 0, 1])
        singular = placement()
        singular[0][0] = 0
        with self.assertRaises(ValueError):
            shared_definition_coincidence(singular, singular, [0, 0, 1])
