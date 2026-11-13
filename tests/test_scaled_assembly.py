"""Scale-aware traversal exercised on the retained Lynx manufacturer import."""
import copy,json,math,os,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from step_placements import native_matrix,solid_instances,apply

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
    def test_recorded_lynx_preserves_all_instance_paths_and_unit_conversion(self):
        root=Path(os.environ.get('FERME_ROOT',Path(__file__).resolve().parents[2]/'ferme'))
        b=root/'engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01'
        rows=[r for p in b.glob('records-*.json') for r in json.loads(p.read_text())['records']]
        self.assertTrue(rows,'Retained Lynx records required')
        blocks=json.loads((b/'blocks.json').read_text())['records']
        roots=[format(h,'X') for h in next(r for r in blocks if r['name']=='*Model_Space')['properties']['entity_handles']]
        with self.assertRaisesRegex(ValueError,'Unit-scale'):solid_instances(rows,blocks,roots)
        actual=solid_instances(rows,blocks,roots,allow_uniform_scale=True)
        self.assertEqual(len(actual),130)
        unscaled=copy.deepcopy(rows)
        outer=next(r for r in unscaled if r['handle']=='276')
        for k in ['x_scale','y_scale','z_scale']:outer['properties'][k]=1
        reference=solid_instances(unscaled,blocks,roots)
        self.assertEqual([v['path'] for v in actual],[v['path'] for v in reference])
        for a,r in zip(actual,reference):
            for x,y in zip(apply(a['matrix'],[1,2,3]),apply(r['matrix'],[1,2,3])):
                self.assertAlmostEqual(x,y*.001)

if __name__=='__main__':unittest.main()
