"""Synthetic repeat-integration regressions; no native session required."""
import copy,hashlib,json,math,sys,tempfile,unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock,patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from exact_profiles import straight_bezier_certificate,compare_with_linear_cubics,compare_loops
from profile_conditioning import conditioning_point,condition_profiles,conditioning_depth,conditioning_roundtrip
from solid_transfer import verify_solid_transfer
from cadtools.checkpoints import save_checkpoint
from cadtools.runtime import CadError


def source_loop():
    e=dict(kind='NURBS',degree=3,control_points=[[0,0],[1,0],[2,0],[3,0]],weights=[1]*4,knots=[4]*4+[9]*4,periodic=False,fit_points=[])
    pts=[[3,0],[3,2],[0,2],[0,0]]
    return [dict(role='outer',edges=[e]+[dict(kind='Line',start=a,end=b) for a,b in zip(pts,pts[1:])])]


class LineEquivalence(unittest.TestCase):
    def compare(self,a,b,allowed=((0,0),)):
        return compare_with_linear_cubics(a,b,allowed_source_edges=allowed,length_tolerance=1e-8,parameter_tolerance=1e-10)
    def test_exact_proof_and_strict_failure_remain_separate(self):
        a=source_loop();b=copy.deepcopy(a);b[0]['edges'][0]=dict(kind='Line',start=[0,0],end=[3,0])
        r=self.compare(a,b);self.assertEqual(r['result'],'PASS');self.assertEqual(r['strict_result']['result'],'FAIL')
        self.assertEqual(self.compare(a,b,())['result'],'FAIL')
    def test_nearly_straight_is_rejected_exactly(self):
        e=source_loop()[0]['edges'][0];e['control_points'][1][1]=1e-15
        self.assertEqual(straight_bezier_certificate(e)['result'],'FAIL')
    def test_backtracking_controls_rejected(self):
        e=source_loop()[0]['edges'][0];e['control_points'][1][0]=2.5;e['control_points'][2][0]=.5
        self.assertEqual(straight_bezier_certificate(e)['result'],'FAIL')
    def test_rational_and_multispan_cubics_rejected(self):
        e=source_loop()[0]['edges'][0];e['weights'][1]=2
        self.assertEqual(straight_bezier_certificate(e)['result'],'FAIL')
        e=source_loop()[0]['edges'][0];e['control_points'].insert(2,[1.5,0]);e['weights'].append(1);e['knots']=[0]*4+[.5]+[1]*4
        self.assertEqual(straight_bezier_certificate(e)['result'],'FAIL')
    def test_other_curves_stay_strict_and_indices_unique(self):
        a=source_loop();b=copy.deepcopy(a);b[0]['edges'][1]['end']=[3,3];b[0]['edges'][2]['start']=[3,3]
        self.assertEqual(self.compare(a,b)['result'],'FAIL')
        with self.assertRaises(ValueError):self.compare(a,a,[(0,0),(0,0)])
        with self.assertRaises(ValueError):self.compare(a,a,[(0,9)])
    def test_reversed_axis_and_diagonal_exact_proofs(self):
        for pts in ([[3,0],[2,0],[1,0],[0,0]],[[0,0],[1,2],[2,4],[3,6]]):
            e=source_loop()[0]['edges'][0];e['control_points']=pts
            self.assertEqual(straight_bezier_certificate(e)['result'],'PASS')


class Conditioning(unittest.TestCase):
    def test_full_profiles_roundtrip_and_inputs_preserved(self):
        loops=source_loop();before=copy.deepcopy(loops)
        r=conditioning_roundtrip(loops,anchor=[3,-2],scale=750,translation=[17,-20],length_tolerance=1e-8,parameter_tolerance=1e-10)
        self.assertEqual(r['result'],'PASS');self.assertEqual(loops,before)
        self.assertEqual(r['working_profiles'][0]['edges'][0]['knots'],loops[0]['edges'][0]['knots'])
    def test_seed_and_depth_same_uniform_contract(self):
        p=[.25,-.1];q=conditioning_point(p,anchor=[1,-2],scale=20,translation=[5,7]);back=conditioning_point(q,anchor=[1,-2],scale=20,translation=[5,7],inverse=True)
        for a,b in zip(p,back):self.assertAlmostEqual(a,b)
        self.assertEqual(conditioning_depth(.5,20),10);self.assertEqual(conditioning_depth(10,20,inverse=True),.5)
    def test_arc_controls_and_sweep_preserved(self):
        loops=[dict(role='outer',edges=[dict(kind='Arc',start=[1,0],end=[0,1],center=[0,0],sweep=math.pi/2),dict(kind='Line',start=[0,1],end=[1,0])])]
        r=conditioning_roundtrip(loops,anchor=[3,4],scale=10,length_tolerance=1e-8,parameter_tolerance=1e-10)
        self.assertEqual(r['result'],'PASS');self.assertEqual(r['working_profiles'][0]['edges'][0]['sweep'],math.pi/2)
    def test_bad_scale_nonfinite_and_collapsed_depth_rejected(self):
        for scale in (0,-1,math.nan):
            with self.assertRaises((ValueError,CadError)):conditioning_point([0,0],anchor=[0,0],scale=scale)
        with self.assertRaises(ValueError):conditioning_point([1e308,0],anchor=[0,0],scale=1e308)
        with self.assertRaises(ValueError):conditioning_depth(1e-300,1e-300)


def solid(handle='A'):
    return dict(handle=handle,type='Solid3D',record_type='Solid3D',properties=dict(acis_data=dict(version=1,sat_data='synthetic native geometry',sab_data=[],metadata={'units':1}),common=dict(extended_data=dict(records=[dict(application_name='ORIGINAL',values=['pin'])])),history='retained'))


class SolidTransfer(unittest.TestCase):
    def check(self,a,b,**kw):return verify_solid_transfer(a,b,[dict(source_handle='A',target_handle='B')],**kw)
    def test_handles_may_change_with_full_payload_preserved(self):
        self.assertEqual(self.check([solid()],[solid('B')])['result'],'PASS')
    def test_full_acis_envelope_and_noncommon_properties_required(self):
        for change in ('version','geometry','history'):
            b=solid('B')
            if change=='version':b['properties']['acis_data'].pop('version')
            elif change=='geometry':b['properties']['acis_data']['sat_data']='altered'
            else:b['properties']['history']='changed'
            self.assertEqual(self.check([solid()],[b])['result'],'FAIL')
    def test_added_provenance_explicit_and_original_unchanged(self):
        b=solid('B');b['properties']['common']['extended_data']['records'].append(dict(application_name='PARENT',values=['parent']))
        self.assertEqual(self.check([solid()],[b])['result'],'FAIL')
        self.assertEqual(self.check([solid()],[b],added_metadata_apps=['PARENT'])['result'],'PASS')
        b['properties']['common']['extended_data']['records'][0]['values']=['changed']
        self.assertEqual(self.check([solid()],[b],added_metadata_apps=['PARENT'])['result'],'FAIL')
    def test_duplicate_metadata_and_ambiguous_mapping_rejected(self):
        b=solid('B');b['properties']['common']['extended_data']['records']*=2
        self.assertEqual(self.check([solid()],[b])['result'],'FAIL')
        with self.assertRaises(ValueError):self.check([solid(),solid()],[b])
        with self.assertRaises(ValueError):self.check([solid()],[b],added_metadata_apps=['ORIGINAL'])
    def test_unmapped_target_fails_coverage(self):
        self.assertEqual(self.check([solid()],[solid('B'),solid('C')])['result'],'FAIL')
        self.assertEqual(self.check([solid()],[solid('B'),solid('C')],require_all_targets=False)['result'],'PASS')


class CheckpointAudits(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.path=Path(self.temp.name)/'checkpoint.dwg'
        self.c=Mock();self.c.namespace='job';self.c.document_id=1;self.c.journal=SimpleNamespace(requests={})
        self.state=dict(ok=True,document_id=1,revision=0,geometry_revision=3,command=None,modal=None)
        self.audit=dict(document_id=1,summary={'errors':0,'warnings':0},manifest={'by_type':{'3D Solid':1}})
        self.c.read.side_effect=lambda op,**kw:self.state.copy() if op=='state' else self.audit
        def save(label,op,**kw):
            self.path.write_bytes(b'checkpoint fixture');return dict(result=dict(saved=str(self.path),sha256=hashlib.sha256(self.path.read_bytes()).hexdigest(),verified=True,dropped_on_save=0,manifest=self.audit['manifest']))
        self.c.mutate.side_effect=save
    def run_save(self):return save_checkpoint(self.c,self.path,label='stage',expected_counts={'3D Solid':1})
    def test_wrong_document_audit_stops_before_write(self):
        self.audit['document_id']=99
        with self.assertRaises(CadError):self.run_save()
        self.c.mutate.assert_not_called();self.assertFalse(self.path.exists())
    def test_pending_operation_stops_before_write(self):
        self.state['operation']={'status':'running'}
        with self.assertRaises(CadError):self.run_save()
        self.c.mutate.assert_not_called()
    def test_stale_epoch_recovery_stops_before_recover(self):
        self.c.journal.requests['job:stage']=dict(request=dict(op='save_verified',path=str(self.path),geometry_revision=2),context=dict(document_id=1))
        with self.assertRaises(CadError):self.run_save()
        self.c.recover.assert_not_called()
    def test_construction_label_collision_identifies_operation_without_write(self):
        self.c.journal.requests['job:stage'] = {'request': {'op': 'run'}}
        with self.assertRaisesRegex(CadError, "label 'stage' is already used by 'run'"):
            self.run_save()
        self.c.mutate.assert_not_called()
        self.c.recover.assert_not_called()
        self.assertFalse(self.path.exists())

    def test_existing_save_label_reports_path_conflict_without_recovery(self):
        self.c.journal.requests['job:stage'] = {'request': {
            'op': 'save_verified', 'path': str(self.path.with_name('other.dwg'))}}
        with self.assertRaisesRegex(CadError, "already has a different save path"):
            self.run_save()
        self.c.mutate.assert_not_called()
        self.c.recover.assert_not_called()

    def test_stable_owned_checkpoint_passes(self):
        self.assertEqual(self.run_save()['result'],'PASS')
    def test_external_epoch_change_during_audit_fails(self):
        def read(op,**kw):
            if op=='state':return self.state.copy()
            self.state['geometry_revision']+=1;return self.audit
        self.c.read.side_effect=read
        with self.assertRaises(CadError):self.run_save()
        self.c.mutate.assert_not_called()

if __name__=='__main__':unittest.main()
