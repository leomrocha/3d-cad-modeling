"""Optional Open CASCADE synthetic checks; volumes use cubic fixture units."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from finite_solid_contact import finite_solid_contact

try:
    from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
    from OCP.BRepPrimAPI import BRepPrimAPI_MakeBox
    from OCP.gp import gp_Pnt
except ImportError:
    BRepPrimAPI_MakeBox = None


@unittest.skipUnless(BRepPrimAPI_MakeBox, 'optional Open CASCADE Python bindings unavailable')
class SolidContact(unittest.TestCase):
    def box(self, x):
        return BRepPrimAPI_MakeBox(gp_Pnt(x, 0, 0), 1, 1, 1).Solid()

    def check(self, first, second, points=()):
        return finite_solid_contact(first, second, relative_integration_target=1e-6,
                                    distance_deflection=1e-8, classifier_tolerance=1e-8,
                                    contact_tolerance=1e-6, witness_margin=1e-5, points=points)

    def test_positive_and_boundary_witness(self):
        source = self.box(0).Reversed()
        orientation = source.Orientation()
        result = self.check(source, self.box(0.5), [(0.75, 0.5, 0.5), (0.5, 0, 0)])
        self.assertEqual(result['state'], 'POSITIVE_OVERLAP', result)
        self.assertEqual(source.Orientation(), orientation)
        self.assertAlmostEqual(result['boolean_common_volume'], 0.5)
        self.assertTrue(result['witnesses'][0]['strict_interior'])
        self.assertFalse(result['witnesses'][1]['strict_interior'])

    def test_touching(self):
        result = self.check(self.box(0), self.box(1))
        self.assertEqual(result['state'], 'CONTACT_WITHIN_TOLERANCE', result)
        self.assertEqual(result['common_pieces'], [])

    def test_separated(self):
        result = self.check(self.box(0), self.box(3))
        self.assertEqual(result['state'], 'SEPARATED', result)
        self.assertAlmostEqual(result['solid_distance'], 2)

    def test_unbounded_half_space_is_unknown(self):
        from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeFace
        from OCP.BRepPrimAPI import BRepPrimAPI_MakeHalfSpace
        from OCP.gp import gp_Dir, gp_Pln

        plane = gp_Pln(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
        face = BRepBuilderAPI_MakeFace(plane).Face()
        half_space = BRepPrimAPI_MakeHalfSpace(face, gp_Pnt(0, 0, -1)).Solid()
        result = self.check(self.box(0), half_space)
        self.assertEqual(result['state'], 'UNKNOWN')
        self.assertIn('finite bounds', result['reason'])

    def test_non_solid_is_unknown(self):
        vertex = BRepBuilderAPI_MakeVertex(gp_Pnt(0, 0, 0)).Vertex()
        result = self.check(self.box(0), vertex)
        self.assertEqual(result['state'], 'UNKNOWN')
        self.assertIn('one finite solid', result['reason'])
