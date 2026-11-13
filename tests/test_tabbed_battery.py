"""Actual saved BMW exterior and repeated-cover failure cases."""
import copy,json,os,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from battery_module import check_tabbed_case
from native_acis import sab_features
from feature_checks import planar_boundary_pattern

class TabbedBatteryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path(os.environ.get('FERME_ROOT',Path(__file__).resolve().parents[2]/'ferme'))
        b=root/'engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02'
        cls.record=json.loads((b/'native-records.json').read_text());cls.job=json.loads((b/'source-job.json').read_text())
        row=next(r for r in cls.record['records'] if r['properties']['common']['layer']=='removable_busbar_cover')
        cls.cover=sab_features(bytes(row['properties']['acis_data']['sab_data']),allow_rigid=True,include_loops=True)
        cls.v={f['name']:f['value'] for f in cls.job['features']}
    def pattern(self,features=None,level=None,centres=None):
        v=self.v
        return planar_boundary_pattern('Cover recesses',features or self.cover,2,v['cover floor level'] if level is None else level,[v['cover pocket width'],v['cover pocket height']],v['cover pocket centres'] if centres is None else centres,1e-6)
    def test_actual_saved_case_and_all_24_recesses_pass(self):
        result=check_tabbed_case(self.record,self.job)
        self.assertEqual(result['result'],'PASS');self.assertEqual(len(result['checks']),19)
        self.assertEqual(len(self.pattern()['observed']),24)
    def test_wrong_source_body_length_is_detected(self):
        job=copy.deepcopy(self.job)
        next(f for f in job['features'] if f['name']=='body length')['value']=386
        self.assertEqual(check_tabbed_case(self.record,job)['result'],'FAIL')
    def test_shifted_recess_pattern_is_detected(self):
        centres=[[x+1,y] for x,y in self.v['cover pocket centres']]
        self.assertEqual(self.pattern(centres=centres)['result'],'FAIL')
    def test_missing_native_recess_boundary_is_detected(self):
        f=copy.deepcopy(self.cover)
        plane=next(p for p in f['planar_boundary_components'] if abs(p['plane_normal'][2]-1)<1e-7 and abs(p['plane_offset']-148.6)<1e-7)
        plane['components'].pop()
        self.assertEqual(self.pattern(features=f)['result'],'FAIL')
    def test_wrong_floor_level_is_detected(self):
        self.assertEqual(self.pattern(level=149)['result'],'FAIL')
    def test_open_native_boundary_is_detected(self):
        f=copy.deepcopy(self.cover)
        plane=next(p for p in f['planar_boundary_components'] if abs(p['plane_normal'][2]-1)<1e-7 and abs(p['plane_offset']-148.6)<1e-7)
        plane['components'][0]['closed_degree_two']=False
        self.assertEqual(self.pattern(features=f)['result'],'FAIL')

if __name__=='__main__':unittest.main()
