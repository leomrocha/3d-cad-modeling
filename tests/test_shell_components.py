"""Synthetic shell winding, vertex links and disconnected shells."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from mesh_checks import shell_components


class Shells(unittest.TestCase):
    points = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    faces = [(0, 2, 1), (0, 1, 3), (0, 3, 2), (1, 2, 3)]

    def test_large_origin_and_reversed_component(self):
        p = [(x+1e12, y+1e12, z+1e12) for x, y, z in self.points]
        q = [(x+3, y, z) for x, y, z in p]
        rev = [tuple(i+4 for i in reversed(face)) for face in self.faces]
        result = shell_components(p+q+[(0, 0, 0)], self.faces+rev)
        a, b = result['components']
        self.assertEqual(result['unused_vertex_count'], 1)
        self.assertEqual([a['winding'], b['winding']], ['POSITIVE', 'NEGATIVE'])
        for component, sign in [(a, 1), (b, -1)]:
            self.assertEqual(component['euler_characteristic'], 2)
            self.assertTrue(component['closed_manifold'])
            self.assertAlmostEqual(component['signed_volume'], sign/6)

    def test_open_shell(self):
        part, = shell_components(self.points, self.faces[:-1])['components']
        self.assertFalse(part['closed_manifold'])
        self.assertIsNone(part['signed_volume'])

    def test_pinched_vertex_has_two_link_cycles(self):
        points = self.points + [(-1, 0, 0), (0, -1, 0), (0, 0, -1)]
        faces = self.faces + [tuple(0 if v == 0 else v+3 for v in f) for f in self.faces]
        part, = shell_components(points, faces)['components']
        self.assertEqual(part['noncycle_vertex_links'], [0])
        self.assertFalse(part['closed_manifold'])
