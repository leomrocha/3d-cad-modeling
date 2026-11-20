"""Synthetic planar bearing checks using the shared rectangle helper."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from planar_profiles import rectangular_face_overlap


def face(x0, y0, x1, y1, z=0):
    return [[x0, y0, z], [x1, y0, z], [x1, y1, z], [x0, y1, z]]


class TestRectangularFaceOverlap(unittest.TestCase):
    def check(self, a, b, axis=2):
        return rectangular_face_overlap(a, b, normal_axis=axis, tolerance=1e-6)

    def test_partial_overlap_reverse_order_and_other_axis(self):
        a = face(0, 0, 8, 9)
        b = face(2, -2, 6, 4)
        result = self.check(a, list(reversed(b)))
        self.assertEqual(result['projected_overlap_lengths'], [4, 4])
        self.assertEqual(result['coplanar_overlap_area'], 16)
        rotate = lambda points: [[z, x, y] for x, y, z in points]
        self.assertEqual(self.check(rotate(a), rotate(b), 0)['coplanar_overlap_area'], 16)

    def test_plane_separation_is_distinct_from_projected_overlap(self):
        result = self.check(face(0, 0, 8, 9), face(2, -2, 6, 4, -.25))
        self.assertFalse(result['coplanar'])
        self.assertEqual(result['normal_offset'], -.25)
        self.assertEqual(result['projected_overlap_area'], 16)
        self.assertEqual(result['coplanar_overlap_area'], 0)

    def test_touching_edges_have_zero_area(self):
        result = self.check(face(0, 0, 8, 9), face(8, 0, 9, 9))
        self.assertTrue(result['coplanar'])
        self.assertEqual(result['coplanar_overlap_area'], 0)

    def test_rejects_crossed_or_nonparallel_boundary(self):
        a = face(0, 0, 8, 9)
        for b in ([a[0], a[2], a[1], a[3]], a[:3] + [[0, 9, 1]]):
            with self.subTest(b=b), self.assertRaises(ValueError):
                self.check(a, b)
