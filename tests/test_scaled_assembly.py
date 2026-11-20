"""Check scale-aware native placement transforms."""
import math,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from step_placements import native_matrix,apply

class ScaledAssemblyTests(unittest.TestCase):
    def properties(self):
        return dict(normal=dict(x=0,y=0,z=1),rotation=math.pi/2,
                    insert_point=dict(x=5,y=2,z=0),x_scale=.001,y_scale=.001,z_scale=.001)
    def test_rotation_scale_and_translation_use_distinct_operations(self):
        p=self.properties()
        with self.assertRaisesRegex(ValueError,'Unit-scale'):native_matrix(p)
        actual=apply(native_matrix(p,allow_uniform_scale=True),[1000,0,0])
        for a,e in zip(actual,[5,3,0]):self.assertAlmostEqual(a,e)
    def test_reflections_zero_and_nonfinite_scales_rejected(self):
        for value in [-.001,0,float('nan'),float('inf')]:
            p=self.properties();p['x_scale']=value
            with self.assertRaises(ValueError):native_matrix(p,allow_uniform_scale=True)
    def test_nonuniform_scale_rejected(self):
        p=self.properties();p['z_scale']=.002
        with self.assertRaisesRegex(ValueError,'Uniform'):native_matrix(p,allow_uniform_scale=True)

if __name__=='__main__':unittest.main()
