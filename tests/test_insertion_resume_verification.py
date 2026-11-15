"""Portable regression cases for inspected native recovery and assembly methods."""
import copy,hashlib,json,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import Mock
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from cadtools.runtime import CadError,Uncertain,Journal
from cadtools.checkpoints import verify_resume_checkpoint,save_checkpoint
from insert_recovery import insert_default_contract,accept_insert_default
from assembly_build import correct_insert_point
from assembly_verification import compare_occurrence_matrices,verify_nested_placements,match_world_vertices,check_world_envelope
from step_placements import eye


def command(stage):
    return dict(name='-INSERT',accepts=['token','enter'],prompt={
        'xscale':'Enter X scale factor, specify opposite corner, or [Corner/XYZ] <1>:',
        'yscale':'Enter Y scale factor <use X scale factor>:',
        'rotation':'Specify rotation angle <0>:'}[stage])


def state(stage=None):return dict(ok=True,document_id=7,revision=1,geometry_revision=20,command=command(stage) if stage else None,modal=None,operation=None,session_id='fixture')


def properties(point=(2,3,0)):
    return dict(normal=dict(x=0,y=0,z=1),rotation=0,insert_point=dict(zip('xyz',point)),x_scale=1,y_scale=1,z_scale=1,block_name='PART')


class FakeClient:
    def __init__(self,path,stage=None):
        self.journal=Journal(path);self.namespace='fixture';self.document_id=7;self.s=state(stage);self.calls=[];self.responses={};self.lose=False;self.conflict=False
        self.row=dict(handle='A',type='Insert',properties=properties())
    def read(self,op,**kw):
        if op=='state':return copy.deepcopy(self.s)
        if op=='records':return dict(records=[copy.deepcopy(self.row)])
        raise AssertionError(op)
    def mutate(self,label,op,**kw):
        key=self.namespace+':'+label;self.calls.append((op,copy.deepcopy(kw)))
        self.journal.intent(dict(op=op,request_id=key,document_id=7,**kw),dict(session_id='fixture',document_id=7))
        if op=='input':
            prompt=self.s['command']['prompt']
            self.s['command']=command('yscale') if 'Enter X' in prompt else command('rotation') if 'Enter Y' in prompt else None
        elif op=='set_properties':
            update=kw['updates'][0]
            if self.conflict:raise CadError('CAS expected property differs')
            if update['expected']!=self.row['properties']['insert_point']:raise CadError('CAS differs')
            self.row['properties']['insert_point']=copy.deepcopy(update['value'])
        else:raise AssertionError(op)
        self.s['revision']+=1
        if not self.s['command']:self.s['geometry_revision']+=1
        response=dict(ok=True,status='waiting_input' if self.s['command'] else 'completed',state=copy.deepcopy(self.s))
        self.responses[key]=response;self.journal.append(dict(event='response',request_id=key,response=response))
        if self.lose:self.lose=False;raise Uncertain('Synthetic lost response')
        return response
    def recover(self,key,**kw):return copy.deepcopy(self.responses[key])


class Defaults(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.c=FakeClient(Path(self.t.name)/'journal.jsonl','xscale')
    def run_default(self,stage,value,receipt=None,checkpoint=None,label=None):
        plan=insert_default_contract(self.c.read('state'),stage=stage,planned_value=value,x_scale_receipt=receipt)
        return accept_insert_default(self.c,label or stage,plan,exclusive_interval=True,checkpoint=checkpoint)
    def test_verified_defaults_advance_and_checkpoint_completed_insert(self):
        x=self.run_default('xscale',1);y=self.run_default('yscale',1,x);saved=[]
        r=self.run_default('rotation',0,checkpoint=saved.append)
        self.assertEqual(r['result'],'PASS');self.assertEqual(saved,['insert-completed'])
        self.assertIsNone(self.c.s['command']);self.assertEqual(len(self.c.calls),3)
    def test_planned_value_different_from_default_rejected(self):
        with self.assertRaises(CadError):self.run_default('xscale',2)
        self.assertEqual(self.c.calls,[])
    def test_inherited_y_requires_same_epoch_verified_x(self):
        x=self.run_default('xscale',1);bad=dict(x,after_identity=[7,0,1])
        with self.assertRaises(CadError):self.run_default('yscale',1,bad)
        with self.assertRaises(CadError):self.run_default('yscale',1)
    def test_unrecognized_prompt_and_enter_rejection(self):
        self.c.s['command']['prompt']='Specify insertion point:'
        with self.assertRaises(CadError):self.run_default('xscale',1)
        self.c.s=state('xscale');self.c.s['command']['accepts']=['token']
        with self.assertRaises(CadError):self.run_default('xscale',1)
    def test_contract_revalidated_and_changed_document_refused(self):
        p=insert_default_contract(self.c.s,stage='xscale',planned_value=1)
        p['planned_value']=2
        with self.assertRaises(CadError):accept_insert_default(self.c,'x',p,exclusive_interval=True)
        p=insert_default_contract(self.c.s,stage='xscale',planned_value=1);self.c.s['document_id']=8
        with self.assertRaises(CadError):accept_insert_default(self.c,'x',p,exclusive_interval=True)
        self.assertEqual(self.c.calls,[])
    def test_lost_response_and_restart_do_not_replay_enter(self):
        p=insert_default_contract(self.c.s,stage='xscale',planned_value=1);self.c.lose=True
        accept_insert_default(self.c,'x',p,exclusive_interval=True)
        accept_insert_default(self.c,'x',p,exclusive_interval=True)
        self.assertEqual(len(self.c.calls),1)
    def test_original_failed_point_request_is_not_replayed(self):
        key='fixture:old-point'
        self.c.journal.intent(dict(op='input',kind='point',point=[0,0,0],request_id=key,document_id=7),dict(session_id='fixture',document_id=7))
        self.c.journal.append(dict(event='response',request_id=key,response=dict(ok=False,status='failed',error='An interactive command is already active')))
        self.run_default('xscale',1)
        self.assertEqual(len(self.c.calls),1);self.assertEqual(self.c.calls[0][1]['kind'],'enter')
    def test_rotation_requires_checkpoint_before_native_input(self):
        self.c.s=state('rotation')
        with self.assertRaises(CadError):self.run_default('rotation',0)
        self.assertEqual(self.c.calls,[])
    def test_changed_recovery_contract_refused(self):
        p=insert_default_contract(self.c.s,stage='xscale',planned_value=1)
        accept_insert_default(self.c,'x',p,exclusive_interval=True);p['value']='2'
        with self.assertRaises(CadError):accept_insert_default(self.c,'x',p,exclusive_interval=True)
    def test_completed_insert_checkpoint_failure_is_preserved(self):
        self.c.s=state('rotation')
        with self.assertRaisesRegex(RuntimeError,'save failed'):
            self.run_default('rotation',0,checkpoint=lambda label:(_ for _ in ()).throw(RuntimeError('save failed')))
        self.assertIsNone(self.c.s['command']);self.assertEqual(len(self.c.calls),1)
    def test_active_operation_and_missing_exclusive_interval_block(self):
        self.c.s['operation']={'status':'running'}
        with self.assertRaises(CadError):self.run_default('xscale',1)
        self.c.s=state('xscale');p=insert_default_contract(self.c.s,stage='xscale',planned_value=1)
        with self.assertRaises(CadError):accept_insert_default(self.c,'x',p)


class PointCorrection(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.c=FakeClient(Path(self.t.name)/'journal.jsonl');self.saved=[]
    def correct(self,**kw):
        opts=dict(expected_matrix=eye(),schema_paths=['/insert_point'],checkpoint=self.saved.append,exclusive_interval=True,translation_tolerance=1e-8,linear_tolerance=1e-10);opts.update(kw)
        return correct_insert_point(self.c,'point','A',[0,0,0],**opts)
    def test_corrects_only_point_with_exact_expected_old_value(self):
        r=self.correct();self.assertEqual(r['result'],'PASS');update=self.c.calls[0][1]['updates'][0]
        self.assertEqual(update['expected'],dict(x=2,y=3,z=0));self.assertEqual(self.saved,['before-point-correction','after-point-correction'])
    def test_other_placement_mismatch_rejected(self):
        self.c.row['properties']['rotation']=1
        with self.assertRaises(CadError):self.correct()
        self.assertEqual(self.c.calls,[])
    def test_schema_or_pre_checkpoint_failure_stops_mutation(self):
        with self.assertRaises(CadError):self.correct(schema_paths=[])
        with self.assertRaises(RuntimeError):self.correct(checkpoint=lambda label:(_ for _ in ()).throw(RuntimeError('checkpoint failed')))
        self.assertEqual(self.c.calls,[])
    def test_cas_failure_preserves_observed_document(self):
        self.c.conflict=True
        with self.assertRaises(CadError):self.correct()
        self.assertEqual(self.c.row['properties']['insert_point'],dict(x=2,y=3,z=0))
    def test_lost_response_and_recovery_no_second_property_write(self):
        self.c.lose=True;self.correct();self.correct()
        self.assertEqual(len(self.c.calls),1)


class Resume(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.root=Path(self.t.name)
        self.source=self.root/'source.json';self.source.write_text('{}\n');self.model=self.root/'progress.dwg';self.model.write_bytes(b'synthetic saved model')
        self.pins=[dict(path='${JOB_ROOT}/source.json',sha256=hashlib.sha256(self.source.read_bytes()).hexdigest())]
        self.checkpoint=dict(result='PASS',state='IN_PROGRESS',job_id='job',document_id=7,geometry_revision=20,saved_path='${JOB_ROOT}/progress.dwg',sha256=hashlib.sha256(self.model.read_bytes()).hexdigest(),source_pins=self.pins,session_id='fixture',handles={'part':'A'})
    def verify(self,**kw):
        opts=dict(job_id='job',source_pins=self.pins,state=state(),roots={'JOB_ROOT':self.root},expected_handles={'part':'A'},actual_handles={'part':'A'});opts.update(kw)
        return verify_resume_checkpoint(self.checkpoint,**opts)
    def test_pinned_idle_live_checkpoint_passes(self):self.assertEqual(self.verify()['result'],'PASS')
    def test_changed_source_or_saved_file_rejected(self):
        self.source.write_text('changed')
        with self.assertRaises(CadError):self.verify()
        self.source.write_text('{}\n');self.model.write_bytes(b'changed')
        with self.assertRaises(CadError):self.verify()
    def test_wrong_job_document_session_and_epoch_rejected(self):
        for field,value in [('document_id',8),('geometry_revision',21),('session_id','other')]:
            s=state();s[field]=value
            with self.subTest(field=field),self.assertRaises(CadError):self.verify(state=s)
        with self.assertRaises(CadError):self.verify(job_id='other')
    def test_pending_command_incomplete_handles_and_changed_contract_rejected(self):
        with self.assertRaises(CadError):self.verify(state=state('xscale'))
        with self.assertRaises(CadError):self.verify(actual_handles={})
        with self.assertRaises(CadError):self.verify(source_pins=[])
    def checkpoint_client(self,mutate_source=False):
        c=Mock();c.namespace='j';c.document_id=7;c.journal.requests={}
        c.read.side_effect=lambda op,**kw:state() if op=='state' else dict(document_id=7,summary={'errors':0,'warnings':0},manifest={'by_type':{'3D Solid':1}})
        def mutate(label,op,**kw):
            path=Path(kw['path']);path.write_bytes(b'verified checkpoint fixture')
            if mutate_source:self.source.write_text('new source revision')
            return dict(result=dict(saved=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),verified=True,dropped_on_save=0,manifest={'by_type':{'3D Solid':1}}))
        c.mutate.side_effect=mutate;return c
    def test_saved_checkpoint_records_resume_contract(self):
        c=self.checkpoint_client();r=save_checkpoint(c,self.root/'new.dwg',label='new',expected_counts={'3D Solid':1},job_id='job',source_pins=self.pins,roots={'JOB_ROOT':self.root},handles={'part':'A'})
        self.assertEqual(r['source_pins'],self.pins);self.assertEqual(r['handles'],{'part':'A'})
        self.assertEqual(verify_resume_checkpoint(r,job_id='job',source_pins=self.pins,state=state(),roots={'JOB_ROOT':self.root},expected_handles={'part':'A'},actual_handles={'part':'A'})['result'],'PASS')
    def test_source_change_during_save_stops_receipt_and_preserves_prior_file(self):
        c=self.checkpoint_client(mutate_source=True);previous=self.model.read_bytes()
        with self.assertRaises(CadError):save_checkpoint(c,self.root/'new.dwg',label='new',expected_counts={'3D Solid':1},job_id='job',source_pins=self.pins,roots={'JOB_ROOT':self.root})
        self.assertEqual(self.model.read_bytes(),previous);self.assertEqual(c.mutate.call_count,1)
    def test_source_locator_cannot_escape_declared_root(self):
        nested=self.root/'nested';nested.mkdir()
        pins=[dict(path='${JOB_ROOT}/../source.json',sha256=self.pins[0]['sha256'])]
        c=Mock();c.namespace='j';c.document_id=7;c.journal.requests={}
        with self.assertRaisesRegex(CadError,'escapes'):
            save_checkpoint(c,self.root/'new.dwg',label='new',expected_counts={},source_pins=pins,roots={'JOB_ROOT':nested})
        c.mutate.assert_not_called()

    def test_source_hash_failure_prevents_checkpoint_save(self):
        c=Mock();c.namespace='j';c.document_id=7;c.journal.requests={}
        self.source.write_text('changed')
        with self.assertRaises(CadError):save_checkpoint(c,self.root/'new.dwg',label='new',expected_counts={},source_pins=self.pins,roots={'JOB_ROOT':self.root})
        c.mutate.assert_not_called()


def occurrence(handle,path,x=0):
    m=eye();m[0][3]=x;return dict(handle=handle,path=[path,handle],matrix=m)


def observation(name,x):
    return dict(id=name,points=[[x,0,0],[x+1,0,0],[x,1,0],[x,0,1]],face_count=4,closed=True)


class Assemblies(unittest.TestCase):
    def matrices(self,a,b,bindings=None,**kw):return compare_occurrence_matrices(a,b,bindings or [dict(source_handle='S',target_handle='T')],translation_tolerance=kw.get('lt',1e-8),linear_tolerance=1e-10)
    def test_repeated_coincident_instances_are_counted(self):
        a=[occurrence('S','a'),occurrence('S','b')];b=[occurrence('T','x'),occurrence('T','y')]
        self.assertEqual(self.matrices(a,b)['result'],'PASS');self.assertEqual(self.matrices(a,b[:1])['result'],'FAIL')
    def test_global_matrix_multiset_cannot_hide_swapped_geometry(self):
        a=[occurrence('S1','a',0),occurrence('S2','b',3)];b=[occurrence('T1','c',3),occurrence('T2','d',0)]
        bindings=[dict(source_handle='S1',target_handle='T1'),dict(source_handle='S2',target_handle='T2')]
        self.assertEqual(self.matrices(a,b,bindings)['result'],'FAIL')
    def test_translation_tolerance_boundary_and_duplicate_path(self):
        self.assertEqual(self.matrices([occurrence('S','a')],[occurrence('T','b',1e-8)])['result'],'PASS')
        self.assertEqual(self.matrices([occurrence('S','a')],[occurrence('T','b',1.01e-8)])['result'],'FAIL')
        with self.assertRaises(ValueError):self.matrices([occurrence('S','a')]*2,[occurrence('T','b')]*2)
    def test_world_vertex_matching_uses_augmenting_paths(self):
        # A fits both targets; B fits only target 0. A greedy first hit fails.
        a=[observation('A',.04),observation('B',0)];b=[observation('X',0),observation('Y',.08)]
        r=match_world_vertices(a,b,length_tolerance=.05)
        self.assertEqual(r['result'],'PASS');self.assertEqual(r['matching'],{0:1,1:0})
    def test_world_missing_repeat_wrong_topology_or_facecount_fail(self):
        a=[observation('A',0),observation('B',0)];b=[observation('X',0)]
        self.assertEqual(match_world_vertices(a,b,length_tolerance=1e-8)['result'],'FAIL')
        for field,value in [('closed',False),('face_count',5)]:
            b=[observation('X',0)];b[0][field]=value
            self.assertEqual(match_world_vertices(a[:1],b,length_tolerance=1e-8)['result'],'FAIL')
    def test_detached_candidate_requires_source_review_without_changes(self):
        points=[[500,500,0],[501,501,1]];before=copy.deepcopy(points)
        r=check_world_envelope(points,[[0,10],[0,10],[-2,2]],length_tolerance=1e-8)
        self.assertEqual(r['result'],'SOURCE_REVIEW_REQUIRED');self.assertTrue(r['disjoint']);self.assertEqual(points,before)
        self.assertEqual(check_world_envelope([[0,0,0],[10,10,2]],[[0,10],[0,10],[-2,2]],length_tolerance=1e-8)['result'],'PASS')
    def test_nonfinite_and_unbounded_work_rejected(self):
        with self.assertRaises(CadError):check_world_envelope([[float('nan'),0,0]],[[0,1]]*3,length_tolerance=1e-8)
        with self.assertRaises(ValueError):match_world_vertices([observation('A',0)]*2,[observation('X',0)],length_tolerance=1e-8,max_instances=1)

if __name__=='__main__':unittest.main()
