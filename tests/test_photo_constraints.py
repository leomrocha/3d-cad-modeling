import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from photo_constraints import backproject_line, direction_intervals


class FixedCameraLines(unittest.TestCase):
    def test_opposite_rays_and_wraparound(self):
        intervals = direction_intervals((0, 0), [(10, 0), (-20, 0)], 1)
        self.assertEqual(intervals[0][0], 0)
        self.assertAlmostEqual(intervals[0][1], math.asin(.05))
        self.assertAlmostEqual(intervals[1][0], math.pi - math.asin(.05))
        self.assertEqual(intervals[1][1], math.pi)

    def test_disjoint_and_uninformative_disks(self):
        self.assertEqual(direction_intervals((0, 0), [(10, 0), (0, 10)], 1), [])
        self.assertEqual(direction_intervals((1, 1), [(1, 1)], 1), [(0, math.pi)])

    def test_backprojection_leaves_depth_free(self):
        camera = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)]
        plane = backproject_line(camera, (0, 2), 0)
        self.assertEqual(plane, (0, 1, -2, 0))
        for point in [(20, 2, 1, 1), (-8, 10, 5, 1)]:
            self.assertEqual(sum(a*b for a, b in zip(plane, point)), 0)

    def test_invalid_inputs(self):
        for picks, radius in [([], 1), ([(0, 0)], -1), ([(0, math.inf)], 1)]:
            with self.assertRaises(ValueError):
                direction_intervals((0, 0), picks, radius)
        with self.assertRaises(ValueError):
            backproject_line([[0]*4]*3, (0, 0), 0)
