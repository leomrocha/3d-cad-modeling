"""Synthetic screens, witnesses and finite pin clearance failures."""
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from mounting_pattern import finite_pin_witness, screen_assignments


class Mounting(unittest.TestCase):
    board = [((0, 0), 0.6), ((2, 0), 0.6)]
    bores = [((3, 4), 0.5), ((3, 6), 0.5)]

    def test_finite_rotated_translated_witness(self):
        checked = finite_pin_witness(self.board, self.bores, [0, 1], angle_degrees=90,
                                     translation=(3, 4), pin_axes=[(3, 4), (3, 6)], pin_radius=0.2)
        self.assertEqual(checked['state'], 'STRICT_PLANAR_CLEARANCE')
        self.assertAlmostEqual(checked['minimum_radial_gap'], 0.3)

    def test_screen_survivors_do_not_prove_probe_clearance(self):
        screen = screen_assignments(self.board, self.bores, tolerance=0)
        self.assertEqual(screen['survivors'], [(0, 1), (1, 0)])
        checked = finite_pin_witness(self.board, self.bores, [0, 1], angle_degrees=90,
                                     translation=(3, 4), pin_axes=[(3, 4), (3, 6)], pin_radius=0.5)
        self.assertEqual(checked['state'], 'POSE_FAILS_CLEARANCE')

    def test_span_exclusion_and_cardinality(self):
        far = [((0, 0), 0.2), ((10, 0), 0.2)]
        self.assertEqual(screen_assignments(self.board, far, tolerance=0)['state'], 'ALL_ASSIGNMENTS_EXCLUDED')
        self.assertEqual(screen_assignments(self.board, far[:1], tolerance=0)['tested'], 0)

    def test_invalid_reuse_and_search_limit(self):
        with self.assertRaises(ValueError):
            finite_pin_witness(self.board, self.bores, [0, 0], angle_degrees=0,
                               translation=(0, 0), pin_axes=[(0, 0)]*2, pin_radius=1)
        with self.assertRaises(ValueError):
            screen_assignments(self.board, self.bores, tolerance=0, max_assignments=1)
