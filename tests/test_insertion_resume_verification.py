"""Portable regression cases for inspected native recovery and assembly methods."""
import copy,hashlib,json,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import Mock, patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from cadtools.runtime import CadError,Uncertain,Journal
from cadtools.checkpoints import verify_resume_checkpoint,save_checkpoint,verify_finish_checkpoint
from cadtools.records import consumed_profile_transition, model_space_after_revolve, model_space_live_handles
from insert_recovery import insert_default_contract,accept_insert_default
from assembly_build import continue_insert_after_file, correct_insert_point, insert_component, recover_insert_component
from assembly_verification import check_axis_aligned_placement,compare_occurrence_matrices,verify_nested_placements,match_world_vertices,match_world_boundary_samples,check_world_envelope
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


class AxisAlignedPlacement(unittest.TestCase):
    def test_reverse_axis_still_binds_intended_face(self):
        local = [[0, 0, 0], [50, 20, 20]]
        target = [[190, 175, 720], [240, 195, 740]]
        matrix = [[-1, 0, 0, 240], [0, 1, 0, 195], [0, 0, 1, 720], [0, 0, 0, 1]]
        actual = check_axis_aligned_placement(local, target, matrix, length_tolerance=1e-6)
        self.assertEqual(actual['result'], 'FAIL')
        self.assertEqual(actual['coordinate_errors'], [[0, 20, 0], [0, 20, 0]])
        matrix[1][3] = 175
        self.assertEqual(check_axis_aligned_placement(local, target, matrix, length_tolerance=1e-6)['result'], 'PASS')
        matrix[0][0] = .5
        with self.assertRaisesRegex(ValueError, 'axis permutation'):
            check_axis_aligned_placement(local, target, matrix, length_tolerance=1e-6)


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
    def test_raw_live_handle_inventory_requires_exact_unrepeated_handles(self):
        options = dict(actual_handles=None)
        self.assertEqual(self.verify(observed_handles=['A'], **options)['result'], 'PASS')
        for actual in ([], ['B'], ['A', 'B'], ['A', 'A'], 'A'):
            with self.subTest(actual=actual), self.assertRaises(CadError):
                self.verify(observed_handles=actual, **options)
        with self.assertRaises(CadError):
            self.verify(observed_handles=['A'])
        with self.assertRaises(CadError):
            self.verify(observed_handles=['A'], expected_handles={'other': 'A'}, **options)

    def test_finish_requires_final_stage_and_all_planned_occurrences(self):
        self.checkpoint['request_id'] = 'job:save-after-labels'
        options = dict(job_id='job', source_pins=self.pins, state=state(),
                       roots={'JOB_ROOT':self.root}, final_stage_request_id='job:save-after-labels',
                       planned_roles=['part'], observed_handles=['A'])
        verified = verify_finish_checkpoint(self.checkpoint, **options)
        self.assertEqual(verified['state'], 'FINAL_VERIFICATION_PENDING')
        self.assertEqual(verified['occurrence_count'], 1)
        for changed in (
            {'final_stage_request_id':'job:save-after-insert'},
            {'planned_roles':['part','second part']},
            {'planned_roles':['part','part']},
            {'observed_handles':['B']},
        ):
            with self.subTest(changed=changed), self.assertRaises(CadError):
                verify_finish_checkpoint(self.checkpoint, **dict(options, **changed))

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
    def test_checkpoint_count_mismatch_reports_audit_labels_without_saving(self):
        c = self.checkpoint_client()
        c.read.side_effect = lambda op, **kw: state() if op == 'state' else dict(
            document_id=7, summary={'errors': 0, 'warnings': 0},
            manifest={'by_type': {'Polyline': 1}})
        path = self.root / 'new.dwg'
        with self.assertRaises(CadError) as error:
            save_checkpoint(c, path, label='new', expected_counts={'LwPolyline': 1})
        self.assertEqual(str(error.exception),
                         "Checkpoint entity counts differ: expected {'LwPolyline': 1}, observed {'Polyline': 1}")
        self.assertFalse(path.exists())
        c.mutate.assert_not_called()

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


class CompletedInsertRecovery(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.path=Path(temp.name)/'part.dwg'
        self.path.write_bytes(b'source drawing')
        self.digest=hashlib.sha256(self.path.read_bytes()).hexdigest()
        self.client=Mock()
        self.client.namespace='fixture'
        self.client.document_id=7
        self.client.descriptor={'session_id':'fixture'}
        self.client.journal.requests={}
        for suffix,op,fields in [
            ('start','start',dict(cmd='-INSERT')),('file','input',dict(kind='token',text=str(self.path))),
            ('point','input',dict(kind='point',point=[2,3,0],space='wcs')),
            ('xscale','input',dict(kind='token',text='1')),('yscale','input',dict(kind='token',text='1')),
            ('rotation','input',dict(kind='token',text='0')),
        ]:
            key=f'fixture:part-{suffix}'
            self.client.journal.requests[key]=dict(context=dict(session_id='fixture',document_id=7),
                request=dict(op=op,document_id=7,request_id=key,**fields))
        self.client.recover.return_value=dict(ok=True,status='completed',state=state(),
                                              changes=[dict(kind='Added',handle='A')])
        self.client.read.return_value=state()

    def recover(self):
        return recover_insert_component(self.client,'part',self.path,source_locator='catalogue:part',
                                        source_sha256=self.digest,point=(2,3,0))

    def continue_at_point(self, checkpoint):
        for suffix in ('point', 'xscale', 'yscale', 'rotation'):
            self.client.journal.requests.pop('fixture:part-' + suffix, None)
        return continue_insert_after_file(
            self.client, 'part', self.path, source_locator='catalogue:part',
            source_sha256=self.digest, point=(2, 3, 0), checkpoint=checkpoint)

    def run_fresh_insert(self, checkpoint, *, saved_state=None):
        prompts = ['block name', 'insertion point', 'X scale factor', 'Y scale factor', 'rotation angle']
        self.client.read.side_effect = [
            *(dict(state(), command=dict(name='-INSERT', prompt=prompt)) for prompt in prompts),
            state(), saved_state or dict(state(), revision=2),
        ]
        self.client.mutate.side_effect = [
            *({} for _ in prompts),
            dict(ok=True, status='completed', state=state(), changes=[dict(kind='Added', handle='A')]),
            {},
        ]
        with patch('assembly_build.read_stable_entity',
                   return_value=(dict(type='Insert', properties=properties()), {})), \
             patch('assembly_build.compare_source_metadata', return_value={'result': 'PASS'}):
            return insert_component(self.client, 'part', self.path, source_locator='catalogue:part',
                                    point=(2, 3, 0), checkpoint=checkpoint)

    def test_fresh_insert_saves_before_source_metadata(self):
        checkpoint = Mock(side_effect=lambda _: self.assertEqual(self.client.mutate.call_count, 6))
        self.assertEqual(self.run_fresh_insert(checkpoint)['handle'], 'A')
        checkpoint.assert_called_once_with('A')
        self.assertEqual(self.client.mutate.call_args.args[:2], ('part-provenance', 'xdata_set'))

    def test_fresh_insert_save_failure_stops_before_source_metadata(self):
        checkpoint = Mock(side_effect=OSError('Save uncertain'))
        with self.assertRaisesRegex(OSError, 'Save uncertain'):
            self.run_fresh_insert(checkpoint)
        checkpoint.assert_called_once_with('A')
        self.assertEqual(self.client.mutate.call_count, 6)

    def test_fresh_insert_changed_geometry_stops_before_source_metadata(self):
        with self.assertRaisesRegex(CadError, 'geometry changed during checkpoint'):
            self.run_fresh_insert(Mock(), saved_state=dict(state(), geometry_revision=21))
        self.assertEqual(self.client.mutate.call_count, 6)

    def test_continue_file_prompt_sends_only_remaining_requests(self):
        prompts = ['insertion point', 'X scale factor', 'Y scale factor', 'rotation angle']
        states = [dict(state(), command=dict(name='-INSERT', prompt=prompt,
                  accepts=['point' if i == 0 else 'token'])) for i, prompt in enumerate(prompts)]
        done = dict(ok=True, status='completed', state=state(), changes=[dict(kind='Added', handle='A')])
        self.client.recover.return_value = dict(ok=True, status='waiting_input', state=states[0])
        self.client.read.side_effect = [*states, state()]
        self.client.mutate.side_effect = [*(dict(ok=True, status='waiting_input', state=v) for v in states[1:]), done]
        checkpoint = Mock()
        with patch('assembly_build._complete_insert', return_value={'handle':'A'}) as complete:
            checkpoint.side_effect = lambda _: complete.assert_not_called()
            self.assertEqual(self.continue_at_point(checkpoint), {'handle':'A'})
        checkpoint.assert_called_once_with('A')
        self.client.recover.assert_called_once_with('fixture:part-file', allow_wait=True)
        self.assertEqual([call.args[0] for call in self.client.mutate.call_args_list],
                         ['part-point','part-xscale','part-yscale','part-rotation'])

    def test_continue_file_prompt_stops_on_changed_document_epoch(self):
        old = dict(state(), command=dict(name='-INSERT', prompt='insertion point', accepts=['point']))
        self.client.recover.return_value = dict(ok=True, status='waiting_input', state=old)
        self.client.read.return_value = dict(old, geometry_revision=900)
        checkpoint = Mock()
        with self.assertRaisesRegex(CadError,'prompt differs at point'):
            self.continue_at_point(checkpoint)
        self.client.mutate.assert_not_called()
        checkpoint.assert_not_called()

    def test_recover_committed_insert_with_original_id_before_provenance(self):
        with patch('assembly_build.read_stable_entity',return_value=(dict(type='Insert',properties=properties()),{})), \
                patch('assembly_build._complete_insert',return_value={'handle':'A'}) as complete:
            self.assertEqual(self.recover(),{'handle':'A'})
        self.client.recover.assert_called_once_with('fixture:part-rotation')
        self.client.mutate.assert_not_called()
        complete.assert_called_once()

    def test_recover_repeated_occurrence_checks_original_native_block(self):
        previous=dict(handle='B',source='catalogue:part',source_sha256=self.digest,metadata=['pinned'])
        request=self.client.journal.requests['fixture:part-file']['request']
        request['text']='PinnedBlock'
        source=dict(type='Insert',properties={'block_name':'PinnedBlock'})
        inserted=dict(type='Insert',properties=properties())
        with patch('assembly_build.read_stable_entity',side_effect=[(source,{}),(inserted,{})]), \
                patch('assembly_build.compare_source_metadata',return_value={'result':'PASS'}), \
                patch('assembly_build._complete_insert',return_value={'handle':'A'}) as complete:
            result=recover_insert_component(self.client,'part',self.path,source_locator='catalogue:part',
                source_sha256=self.digest,point=(2,3,0),previous=previous)
            self.assertEqual(result,{'handle':'A'})
            self.assertEqual(complete.call_args.kwargs['expected_block'],'PinnedBlock')
        self.client.recover.assert_called_once_with('fixture:part-rotation')

    def test_reject_changed_operand_or_already_submitted_provenance(self):
        request=self.client.journal.requests['fixture:part-file']['request']
        request['text']='other.dwg'
        with self.assertRaisesRegex(CadError,'intent differs at file'):
            self.recover()
        request['text']=str(self.path)
        self.client.journal.requests['fixture:part-provenance']={}
        with self.assertRaisesRegex(CadError,'Provenance already submitted'):
            self.recover()
        self.client.recover.assert_not_called()

    def test_rejects_recognized_response_after_geometry_changes(self):
        self.client.read.return_value=dict(state(),geometry_revision=21)
        with self.assertRaisesRegex(CadError,'current idle native revision'):
            self.recover()
        self.client.mutate.assert_not_called()


class ErasedModelSpaceReferences(unittest.TestCase):
    def setUp(self):
        self.block = dict(name='*Model_Space', properties={'entity_handles': [10, 11]})
        self.entities = [{'handle': 'A'}, {'handle': 'C'}]
        self.intent = dict(op='entities_delete', document_id=7, request_id='job:delete', handles=['B'])
        self.response = dict(ok=True, status='completed', request_id='job:delete', result={'erased': 1})

    def observe(self, expected=('A',)):
        return model_space_live_handles(self.block, self.entities, expected, document_id=7,
                                        erase_intent=self.intent, erase_response=self.response)

    def test_excludes_only_completed_absent_reference(self):
        self.assertEqual(self.observe(), dict(live_handles=['A'], erased_references=['B']))
        self.assertEqual(self.block['properties']['entity_handles'], [10, 11])

    def test_rejects_unknown_or_still_live_reference_and_missing_expected_root(self):
        self.block['properties']['entity_handles'].append('D')
        with self.assertRaises(CadError):
            self.observe()
        self.block['properties']['entity_handles'].pop()
        self.entities.append({'handle': 'B'})
        with self.assertRaises(CadError):
            self.observe()
        self.entities.pop()
        with self.assertRaises(CadError):
            self.observe(('A', 'C'))

    def test_rejects_wrong_request_and_partial_completion(self):
        self.response['request_id'] = 'other:delete'
        with self.assertRaises(CadError):
            self.observe()
        self.response['request_id'] = self.intent['request_id']
        self.response['result']['erased'] = 0
        with self.assertRaises(CadError):
            self.observe()


class ConsumedRevolveProfile(unittest.TestCase):
    def setUp(self):
        self.block = dict(name='*Model_Space', properties={'entity_handles': [10, 11]})
        self.rows = [dict(handle='B', type='Solid3D')]
        self.intent = dict(op='run', cmd='REVOLVE Y 360', document_id=7, request_id='job:revolve')
        self.response = dict(ok=True, status='completed', request_id='job:revolve',
            state={'document_id': 7}, changes=[dict(kind='Removed', handle='A'),
                                               dict(kind='Added', handle='B')])

    def checked(self):
        return model_space_after_revolve(self.block, self.rows, ['B'], document_id=7,
            profile_handle='A', solid_handle='B', revolve_intent=self.intent,
            revolve_response=self.response)

    def test_completed_extrude_binds_removed_profile_and_added_solid(self):
        intent = dict(self.intent, cmd='EXTRUDE 30')
        args = dict(document_id=7, command='EXTRUDE', profile_handle='A', solid_handle='B', intent=intent)
        expected = dict(request_id='job:revolve', profile_handle='A', solid_handle='B')
        self.assertEqual(consumed_profile_transition(**args, response=self.response), expected)
        with self.assertRaises(CadError):
            consumed_profile_transition(**args, response=dict(self.response,changes=[]))
        with self.assertRaises(CadError):
            consumed_profile_transition(**dict(args, command='REVOLVE'), response=self.response)

    def test_completed_revolve_consumes_the_expected_profile(self):
        self.assertEqual(self.checked(), dict(live_handles=['B'], erased_references=['A']))
        self.assertEqual(self.block['properties']['entity_handles'], [10, 11])

    def test_untracked_reference_and_live_profile_fail(self):
        self.block['properties']['entity_handles'].append(12)
        with self.assertRaises(CadError):
            self.checked()
        self.block['properties']['entity_handles'].pop()
        self.rows.append(dict(handle='A', type='LwPolyline'))
        with self.assertRaises(CadError):
            self.checked()

    def test_wrong_document_or_changes_fail(self):
        self.response['state']['document_id'] = 8
        with self.assertRaises(CadError):
            self.checked()
        self.response['state']['document_id'] = 7
        self.response['changes'][0]['handle'] = 'C'
        with self.assertRaises(CadError):
            self.checked()


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
    def test_sample_matching_uses_effective_display_when_geometry_is_coincident(self):
        first = dict(id="one", points=[[1, 2, 3], [4, 5, 6]], rgb=[49, 189, 178], layer="Supports")
        second = dict(first, id="two", layer="Wear")
        observed = [dict(second, id="B", points=list(reversed(first["points"]))), dict(first, id="A")]
        report = match_world_boundary_samples([first, second], observed, length_tolerance=1e-4,
                                              require_unique_source=True)
        self.assertEqual(report["result"], "PASS")
        self.assertEqual(report["matching"], {0: 1, 1: 0})
        observed[1]["rgb"] = [49, 189, 177]
        self.assertEqual(match_world_boundary_samples([first, second], observed,
                                                      length_tolerance=1e-4)["result"], "FAIL")

    def test_sample_matching_checks_both_directions_and_repeated_occurrences(self):
        source = dict(id="one", points=[[0, 0, 0], [4, 0, 0]], rgb=[0, 0, 0], layer="Frame")
        changed = dict(source, id="copy", points=[[0, 0, 0], [2, 0, 0], [4, 0, 0]])
        for a, b in ((source, changed), (changed, source)):
            report = match_world_boundary_samples([a], [b], length_tolerance=0.1)
            self.assertEqual(report["result"], "FAIL")
        repeat = dict(source, id="repeat")
        self.assertEqual(match_world_boundary_samples([source, repeat], [source],
                                                      length_tolerance=0.1)["result"], "FAIL")
        with self.assertRaises(ValueError):
            match_world_boundary_samples([source], [dict(source, rgb=[0, 0, 256])], length_tolerance=0.1)

    def test_detached_candidate_requires_source_review_without_changes(self):
        points=[[500,500,0],[501,501,1]];before=copy.deepcopy(points)
        r=check_world_envelope(points,[[0,10],[0,10],[-2,2]],length_tolerance=1e-8)
        self.assertEqual(r['result'],'SOURCE_REVIEW_REQUIRED');self.assertTrue(r['disjoint']);self.assertEqual(points,before)
        self.assertEqual(check_world_envelope([[0,0,0],[10,10,2]],[[0,10],[0,10],[-2,2]],length_tolerance=1e-8)['result'],'PASS')
    def test_nonfinite_and_unbounded_work_rejected(self):
        with self.assertRaises(CadError):check_world_envelope([[float('nan'),0,0]],[[0,1]]*3,length_tolerance=1e-8)
        with self.assertRaises(ValueError):match_world_vertices([observation('A',0)]*2,[observation('X',0)],length_tolerance=1e-8,max_instances=1)

if __name__=='__main__':unittest.main()
