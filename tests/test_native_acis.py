"""Recorded native-geometry integration tests; FERME owns the source records."""
import json,os,sys,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'scripts'))
from native_acis import sab_features
from rounded_tube import verify_features,dimensions,sat_features,crossmember_checks
F=Path(os.environ.get('FERME_ROOT',R.parent/'ferme'))
W=F/'engineering/module-development/cad/work/component-led-2026-11-12'
try:import ezdxf
except ImportError:ezdxf=None

@unittest.skipUnless(ezdxf is not None and (W/'p01-build-03/reopened-records.json').is_file(),'Requires native reader dependencies and retained FERME rail record')
class NativeBinaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record=json.loads((W/'p01-build-03/reopened-records.json').read_text())
        cls.data=bytes(cls.record['records'][0]['properties']['acis_data']['sab_data'])
        cls.job=json.loads((W/'p01-build-01/source-job-r02.json').read_text())
    def test_saved_native_rail_matches_source_dimensions(self):
        f=sab_features(self.data)
        self.assertEqual(verify_features(f,dimensions(self.job))['result'],'PASS')
        self.assertEqual(f['topology']['faces'],18)
        self.assertTrue(f['topology']['reciprocal_closed_partners'])
    def test_saved_and_presave_vertex_sets_agree(self):
        r=json.loads((W/'p01-build-03/pre-save-records.json').read_text())
        before=sat_features(r['records'][0]['properties']['acis_data']['sat_data'])
        after=sab_features(self.data)
        canon=lambda rows:sorted(tuple(round(v,9) for v in row) for row in rows)
        self.assertEqual(canon(before['points']),canon(after['points']))
        self.assertEqual(sorted(round(c['radius'],9) for c in before['cylinders']),sorted(round(c['radius'],9) for c in after['cylinders']))
    def test_wrong_length_still_fails_binary_check(self):
        p=dimensions(self.job);p['cut length']=260
        self.assertEqual(verify_features(sab_features(self.data),p)['result'],'FAIL')
    def test_truncated_binary_is_rejected(self):
        with self.assertRaises(Exception):sab_features(self.data[:40])

@unittest.skipUnless(ezdxf is not None and (W/'p02-build-01/reopened-records.json').is_file(),'Requires retained crossmember native record')
class CrossmemberNativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        def features(rel):
            r=json.loads((W/rel).read_text())
            return sab_features(bytes(r['records'][0]['properties']['acis_data']['sab_data']))
        cls.rail=features('p01-verify-04/native-records.json')
        cls.cross=features('p02-build-01/reopened-records.json')
    def test_source_frame_gap_and_midpoint(self):
        checks=crossmember_checks(self.rail,self.cross,340,260)
        self.assertTrue(all(c['result']=='PASS' for c in checks['checks']))
    def test_wrong_frame_width_fails_gap_check(self):
        checks=crossmember_checks(self.rail,self.cross,350,260)
        self.assertEqual(checks['checks'][0]['result'],'FAIL')
    def test_changed_local_origin_fails_midpoint_datum(self):
        import copy
        cross=copy.deepcopy(self.cross)
        for point in cross['points']:point[2]+=5
        checks=crossmember_checks(self.rail,cross,340,260)
        self.assertEqual(checks['checks'][1]['result'],'FAIL')

@unittest.skipUnless(ezdxf is not None and (W/'c009-reuse-01/reopened-records.json').is_file(),'Requires retained SKF native records')
class PillowBlockNativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.job=json.loads((W/'c009-reuse-01/source-job.json').read_text())
        cls.before=json.loads((W/'c009-reuse-01/native-records.json').read_text())
        cls.after=json.loads((W/'c009-reuse-01/reopened-records.json').read_text())
    def test_original_housing_crown_failure_is_detected(self):
        from pillow_block import check
        result=check(self.before,self.job)
        self.assertEqual([c['check'] for c in result['checks'] if c['result']=='FAIL'],['housing top width'])
    def test_saved_derivative_matches_bound_source_features(self):
        from pillow_block import check
        self.assertEqual(check(self.after,self.job)['result'],'PASS')
    def test_transformed_screw_requires_explicit_reader_option(self):
        row=next(r for r in self.before['records'] if r['handle']=='90')
        with self.assertRaisesRegex(ValueError,'rigid-frame'):
            sab_features(bytes(row['properties']['acis_data']['sab_data']))
    def test_fragmented_mount_plane_recovers_two_closed_slots(self):
        from pillow_block import read_parts
        housing=read_parts(self.before,self.job)['housing']
        plane=next(g for g in housing['planar_boundary_components'] if g['plane_normal']==[0,0,1] and abs(g['plane_offset'])<1e-7)
        slots=[c for c in plane['components'] if abs(c['bounds']['max'][1]-c['bounds']['min'][1]-11.5)<1e-7]
        self.assertEqual(len(slots),2)
        self.assertTrue(all(c['closed_degree_two'] for c in slots))
        self.assertTrue(all(abs(c['bounds']['max'][0]-c['bounds']['min'][0]-20.5)<1e-7 for c in slots))
    def test_wrong_bore_expectation_fails(self):
        import copy
        from pillow_block import check
        job=copy.deepcopy(self.job)
        next(f for f in job['features'] if f['name']=='shaft bore diameter')['value']=22
        self.assertEqual(check(self.after,job)['result'],'FAIL')

@unittest.skipUnless(ezdxf is not None and (W/'c021-reuse-01/native-records.json').is_file(),'Requires saved Leaf native record')
class BatteryModuleNativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.job=json.loads((W/'c021-reuse-01/source-job.json').read_text())
        cls.record=json.loads((W/'c021-reuse-01/native-records.json').read_text())
    def test_saved_shells_mounting_and_terminal_features(self):
        from battery_module import check
        self.assertEqual(check(self.record,self.job)['result'],'PASS')
    def test_wrong_terminal_pitch_is_rejected(self):
        import copy
        from battery_module import check
        job=copy.deepcopy(self.job)
        next(f for f in job['features'] if f['name']=='terminal pitch')['value']=40
        self.assertEqual(check(self.record,job)['result'],'FAIL')
    def test_missing_component_is_rejected(self):
        import copy
        from battery_module import check
        record=copy.deepcopy(self.record);record['records'].pop()
        with self.assertRaisesRegex(ValueError,'component set'):check(record,self.job)
    def test_observed_component_colon_spacing_variants(self):
        import copy
        from battery_module import check
        record=copy.deepcopy(self.record)
        for row in record['records']:
            for app in row['properties']['common']['extended_data']['records']:
                for v in app['values']:
                    if v.get('String','').startswith('Component:'):
                        v['String']=v['String'].replace('Component:','Component: ')
        self.assertEqual(check(record,self.job)['result'],'PASS')

if __name__=='__main__':unittest.main()
