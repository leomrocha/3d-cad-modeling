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

if __name__=='__main__':unittest.main()
