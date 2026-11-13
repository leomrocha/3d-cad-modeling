"""Synthetic token guards and offline decoding of a retained native torus."""
import json
import os
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from native_acis import _torus_surface, sab_features
try:
    from ezdxf.acis.const import Tags
except ImportError:
    Tags = None

@unittest.skipUnless(Tags is not None, 'Requires caller-supplied native SAB reader')
class TorusTokenTests(unittest.TestCase):
    def tokens(self):
        return [SimpleNamespace(tag=tag, value=value) for tag,value in [
            (Tags.POINTER,None), (Tags.LOCATION_VEC,(1.,2.,3.)),
            (Tags.DIRECTION_VEC,(0.,0.,1.)), (Tags.DOUBLE,10.),
            (Tags.DOUBLE,2.), (Tags.DIRECTION_VEC,(1.,0.,0.))]]

    def test_typed_fields_and_rigid_world_mapping(self):
        def world(v,point=False):
            return [-v[1]+(20 if point else 0),v[0],v[2]]
        row=_torus_surface(self.tokens(),Tags,world)
        self.assertEqual([18.,1.,3.],row['center'])
        self.assertEqual([0.,0.,1.],row['axis'])
        self.assertEqual((10.,2.),(row['major_radius'],row['minor_radius']))

    def test_malformed_fields_and_invalid_geometry_fail(self):
        cases=[]
        t=self.tokens();cases.append(t[:5])
        t=self.tokens();t[1].tag=Tags.DOUBLE;cases.append(t)
        for slot,value in [(3,float('nan')),(4,0.),(4,11.),
                           (1,(1.,2.,float('inf'))),
                           (2,(0.,0.,2.)),(5,(0.,0.,1.))]:
            t=self.tokens();t[slot].value=value;cases.append(t)
        for tokens in cases:
            with self.subTest(tokens=tokens), self.assertRaises(ValueError):
                _torus_surface(tokens,Tags,lambda v,point=False:list(v))

@unittest.skipUnless(Tags is not None, 'Requires caller-supplied native SAB reader')
class RetainedTorusTests(unittest.TestCase):
    def data(self):
        path=os.environ.get('NATIVE_TORUS_SAB')
        if not path:self.skipTest('Supply external NATIVE_TORUS_SAB fixture')
        return Path(path).read_bytes()

    def test_torus_support_requires_explicit_option(self):
        with self.assertRaisesRegex(ValueError,'Unsupported surface: torus-surface'):
            sab_features(self.data())

    def test_saved_torus_surfaces_and_topology_decode(self):
        expectation_path=os.environ.get('NATIVE_TORUS_EXPECTATIONS')
        if not expectation_path:self.skipTest('Supply external torus geometry check record')
        geometry=json.loads(Path(expectation_path).read_text())['geometry']
        expected=geometry['checks'][0]['expected']
        tolerance=geometry['numeric_tolerance_mm']
        features=sab_features(self.data(),allow_tori=True)
        self.assertTrue(features['tori'])
        for row in features['tori']:
            self.assertAlmostEqual(expected['major_radius_mm'],row['major_radius'],delta=tolerance)
            self.assertAlmostEqual(expected['minor_radius_mm'],row['minor_radius'],delta=tolerance)
            for a,b in zip(row['center'],expected['center']):self.assertAlmostEqual(a,b,delta=tolerance)
            for a,b in zip(row['axis'],expected['axis']):self.assertAlmostEqual(a,b,delta=tolerance)
        self.assertEqual(1,features['topology']['bodies'])
        self.assertTrue(features['topology']['reciprocal_closed_partners'])
        self.assertTrue(features['points'])
        for family in ['planes','cylinders','spheres','cones']:
            self.assertFalse(features[family])

if __name__=='__main__':unittest.main()
