"""Projected end edges of a generic rectangular hollow section."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'scripts'))
from planar_profiles import rectangular_opening_perimeters


class RectangularOpeningPerimeters(unittest.TestCase):
    def setUp(self):
        self.outer = [[-10,-8],[10,8]]
        self.inner = [[-8,-6],[8,6]]
        self.edges = [
            ((-10,-8),(10,-8)), ((10,-8),(10,6)), ((10,6),(10,8)),
            ((10,8),(-10,8)), ((-10,8),(-10,-8)),
            ((-8,-6),(8,-6)), ((8,-6),(8,6)), ((8,6),(-8,6)), ((-8,6),(-8,-6)),
            ((8,6),(10,6)),
        ]

    def check(self, edges):
        return rectangular_opening_perimeters(edges,outer_bounds=self.outer,
                                               inner_bounds=self.inner,tolerance=1e-6)

    def test_split_perimeter_with_wall_seam(self):
        result = self.check(self.edges)
        self.assertEqual(result['edge_lengths'], {'outer':72,'inner':56})
        self.assertEqual(result['wall_seam_count'], 1)

    def test_missing_perimeter_segment(self):
        with self.assertRaisesRegex(ValueError,'gap|incomplete'):
            self.check(self.edges[:2] + self.edges[3:])

    def test_duplicate_perimeter_segment(self):
        with self.assertRaisesRegex(ValueError,'gap|overlapping'):
            self.check(self.edges + self.edges[:1])

    def test_segment_crossing_opening(self):
        with self.assertRaisesRegex(ValueError,'outside'):
            self.check(self.edges + [((-10,0),(10,0))])

    def test_incomplete_seam(self):
        with self.assertRaisesRegex(ValueError,'outside'):
            self.check(self.edges[:-1] + [((8,6),(9,6))])
