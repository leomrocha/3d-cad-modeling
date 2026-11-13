import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from model_inventory import inventory_models,start_check,audit

class ExistingModelTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.cad=self.root/'cad';(self.cad/'parts').mkdir(parents=True)
        self.index=self.root/'parts.json';self.sheet=self.root/'part.md';self.sheet.write_text('Component input')
        self.part=dict(id='C001',name='Example ZX1234 component',file='part.md',existing_cad='')
    def check(self,job=None):return start_check(self.part,self.index,self.cad,inventory_models(self.root),job)
    def test_stale_not_started_record_skips_existing_file(self):
        p=self.cad/'parts/existing.dwg';p.write_bytes(b'AC1032 fixture')
        self.part['existing_cad']='parts/existing.dwg'
        result=self.check({'state':'NOT_STARTED'})
        self.assertEqual(result['action'],'SKIP_EXISTING_MODEL');self.assertEqual(result['models'][0]['path'],str(p))
    def test_completed_bmw_style_record_is_not_reopened(self):
        p=self.cad/'parts/module.dwg';p.write_bytes(b'AC1032 fixture')
        self.assertEqual(self.check({'state':'IN_PROGRESS','model':str(p)})['action'],'SKIP_EXISTING_MODEL')
    def test_file_link_in_sheet_is_found_without_manifest_model(self):
        p=self.cad/'parts/exterior.dwg';p.write_bytes(b'AC1032 fixture');self.sheet.write_text('[Existing model]('+str(p)+')')
        self.assertEqual(self.check()['action'],'SKIP_EXISTING_MODEL')
    def test_filesystem_candidate_blocks_new_construction(self):
        p=self.root/'manufacturer-ZX1234.step';p.write_text('retained model')
        result=self.check();self.assertEqual(result['action'],'REVIEW_EXISTING_CANDIDATES');self.assertEqual(result['candidates'][0]['path'],str(p))
    def test_2d_reference_is_separate_from_component_model(self):
        p=self.cad/'2d_schemas/drawings/ZX1234-interface.dwg';p.parent.mkdir(parents=True);p.write_bytes(b'AC1032 fixture')
        self.part['existing_cad']='2d_schemas/drawings/ZX1234-interface.dwg'
        result=self.check();self.assertEqual(result['action'],'NEW_MODEL_REQUIRED');self.assertEqual(len(result['references_2d']),1)
    def test_retained_copy_of_known_2d_drawing_stays_a_reference(self):
        original=self.cad/'2d_schemas/drawings/ZX1234-interface.dwg'
        original.parent.mkdir(parents=True);original.write_bytes(b'known 2D drawing')
        copied=self.cad/'checks/packet/source/ZX1234.dwg'
        copied.parent.mkdir(parents=True);copied.write_bytes(original.read_bytes())
        self.part['existing_cad']=str(copied)
        result=self.check()
        self.assertEqual(result['action'],'NEW_MODEL_REQUIRED')
        self.assertEqual(result['models'],[])
        self.assertEqual(result['candidates'],[])
        reference=next(row for row in result['references_2d'] if row['path']==str(copied))
        self.assertEqual(reference['role_source_paths'],[str(original)])
    def test_distinct_model_bytes_keep_model_role_beside_known_2d_reference(self):
        original=self.cad/'2d_schemas/drawings/ZX1234-interface.dwg'
        original.parent.mkdir(parents=True);original.write_bytes(b'known 2D drawing')
        model=self.cad/'parts/ZX1234.dwg';model.write_bytes(b'distinct completed 3D model')
        self.part['existing_cad']=str(model)
        result=self.check()
        self.assertEqual(result['action'],'SKIP_EXISTING_MODEL')
        self.assertEqual(result['models'][0]['path'],str(model))
    def test_completed_record_with_missing_path_requires_location(self):
        self.assertEqual(self.check({'state':'DONE'})['action'],'LOCATE_COMPLETED_MODEL')
    def test_recorded_native_model_path_skips_construction(self):
        p=self.cad/'parts/rail.dwg';p.write_bytes(b'AC1032 fixture')
        self.assertEqual(self.check({'state':'DONE','native_model':str(p)})['action'],'SKIP_EXISTING_MODEL')
    def test_dependency_motor_is_not_mistaken_for_its_mounting_plate(self):
        p=self.cad/'parts/ZX1234-motor.dwg';p.write_bytes(b'AC1032 fixture')
        motor=dict(id='M',name='ZX1234 motor',file='part.md',existing_cad='parts/ZX1234-motor.dwg')
        plate=dict(id='P',name='ZX1234 motor plate',file='part.md',existing_cad='')
        self.index.write_text(json.dumps([motor,plate]));work=self.root/'work.json'
        work.write_text(json.dumps({'jobs':[{'part_id':'M','state':'DONE'},{'part_id':'P','state':'NOT_STARTED','geometry_inputs':['M']}]}))
        result=audit(self.index,work,self.cad,self.root)['components'][1]
        self.assertEqual(result['action'],'NEW_MODEL_REQUIRED');self.assertEqual(len(result['dependency_models']),1)
    def test_completed_manifest_also_prevents_rebuilding(self):
        self.part['cad_state']='DONE'
        self.assertEqual(self.check({'state':'NOT_STARTED'})['action'],'LOCATE_COMPLETED_MODEL')
    def test_new_component_requires_actual_filesystem_scan(self):
        result=self.check();self.assertEqual(result['action'],'NEW_MODEL_REQUIRED');self.assertEqual(result['filesystem_model_files_checked'],0)
    def test_named_root_job_model_is_found(self):
        p=self.cad/'parts/existing.dwg';p.write_bytes(b'AC1032 fixture')
        result=start_check(self.part,self.index,self.cad,inventory_models(self.root),
            {'model':'${PROJECT_ROOT}/cad/parts/existing.dwg'}, {'PROJECT_ROOT':self.root})
        self.assertEqual(result['action'],'SKIP_EXISTING_MODEL')
    def test_relative_job_path_uses_cad_root(self):
        p=self.cad/'parts/existing.dwg';p.write_bytes(b'AC1032 fixture')
        self.assertEqual(self.check({'native_model':'parts/existing.dwg'})['action'],'SKIP_EXISTING_MODEL')
    def test_missing_root_blocks_false_new_model_result(self):
        with self.assertRaisesRegex(ValueError,'Missing configured path root'):
            self.check({'model':'${PROJECT_ROOT}/cad/parts/existing.dwg'})
    def test_sheet_named_root_link_is_resolved(self):
        p=self.cad/'parts/existing.dwg';p.write_bytes(b'AC1032 fixture')
        self.sheet.write_text('[Model](${PROJECT_ROOT}/cad/parts/existing.dwg)')
        result=start_check(self.part,self.index,self.cad,inventory_models(self.root),root_map={'PROJECT_ROOT':self.root})
        self.assertEqual(result['action'],'SKIP_EXISTING_MODEL')
    def test_relative_root_configuration_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'must be absolute'):
            start_check(self.part,self.index,self.cad,[],{'model':'${ROOT}/part.dwg'},{'ROOT':'relative'})
    def test_existing_iges_source_blocks_reconstruction(self):
        p=self.cad/'parts/ZX1234.igs';p.write_text('IGES source fixture')
        self.part['existing_cad']='parts/ZX1234.igs'
        self.assertEqual(self.check()['action'],'SKIP_EXISTING_MODEL')
    def test_unattributed_iges_candidate_requires_identity_review(self):
        p=self.cad/'parts/ZX1234.iges';p.write_text('IGES source fixture')
        self.assertEqual(self.check()['action'],'REVIEW_EXISTING_CANDIDATES')
    def test_component_id_filename_candidate_requires_review(self):
        p=self.cad/'parts/C001-existing.dwg';p.write_bytes(b'Possible component model')
        self.assertEqual(self.check()['action'],'REVIEW_EXISTING_CANDIDATES')

    def non_geometric_job(self):
        import hashlib
        return {'part_id':'C001','state':'NOT_STARTED',
                'geometry_requirement':{'kind':'non_geometric_consumable','cad_required':False,
                    'source':{'path':'${PROJECT_ROOT}/part.md',
                              'sha256':hashlib.sha256(self.sheet.read_bytes()).hexdigest(),
                              'location':'Explicit no-CAD instruction in fixture input'}}}

    def test_source_bound_non_geometric_job_skips_new_model_requirement(self):
        result=start_check(self.part,self.index,self.cad,inventory_models(self.root),
                           self.non_geometric_job(),{'PROJECT_ROOT':self.root})
        self.assertEqual(result['action'],'SKIP_NON_GEOMETRIC')
        self.assertEqual(result['geometry_requirement']['kind'],'non_geometric_consumable')

    def test_non_geometric_classification_preserves_matching_model_and_candidates(self):
        existing=self.cad/'parts/existing.dwg';existing.write_bytes(b'Existing model')
        self.part['existing_cad']='parts/existing.dwg'
        result=start_check(self.part,self.index,self.cad,inventory_models(self.root),
                           self.non_geometric_job(),{'PROJECT_ROOT':self.root})
        self.assertEqual(result['action'],'SKIP_EXISTING_MODEL')
        self.assertEqual(result['models'][0]['path'],str(existing))
        self.part['existing_cad']=''
        candidate=self.root/'C001-possible.dwg';candidate.write_bytes(b'Candidate model')
        result=start_check(self.part,self.index,self.cad,inventory_models(self.root),
                           self.non_geometric_job(),{'PROJECT_ROOT':self.root})
        self.assertEqual(result['action'],'REVIEW_EXISTING_CANDIDATES')
        self.assertEqual(result['candidates'][0]['path'],str(candidate))

    def test_non_geometric_done_state_skips_missing_model_after_candidate_scan(self):
        job=self.non_geometric_job();job['state']='DONE'
        result=start_check(self.part,self.index,self.cad,inventory_models(self.root),
                           job,{'PROJECT_ROOT':self.root})
        self.assertEqual(result['action'],'SKIP_NON_GEOMETRIC')
        candidate=self.root/'C001-possible.dwg';candidate.write_bytes(b'Candidate model')
        result=start_check(self.part,self.index,self.cad,inventory_models(self.root),
                           job,{'PROJECT_ROOT':self.root})
        self.assertEqual(result['action'],'REVIEW_EXISTING_CANDIDATES')

    def test_geometric_done_candidate_and_existing_model_precedence_is_unchanged(self):
        candidate=self.root/'C001-possible.dwg';candidate.write_bytes(b'Candidate model')
        self.assertEqual(self.check({'state':'DONE'})['action'],'LOCATE_COMPLETED_MODEL')
        self.assertEqual(self.check({'state':'DONE','features':[]})['action'],'LOCATE_COMPLETED_MODEL')
        existing=self.cad/'parts/existing.dwg';existing.write_bytes(b'Existing model')
        self.part['existing_cad']='parts/existing.dwg'
        result=self.check({'state':'DONE'})
        self.assertEqual(result['action'],'SKIP_EXISTING_MODEL')

    def test_non_geometric_classification_rejects_bad_source_or_part_binding(self):
        job=self.non_geometric_job();job['geometry_requirement']['source']['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'source revision changed'):
            start_check(self.part,self.index,self.cad,inventory_models(self.root),job,{'PROJECT_ROOT':self.root})
        job=self.non_geometric_job();job['part_id']='C099'
        with self.assertRaisesRegex(ValueError,'part_id must match'):
            start_check(self.part,self.index,self.cad,inventory_models(self.root),job,{'PROJECT_ROOT':self.root})

    def test_non_geometric_classification_rejects_configuration_mode(self):
        job=self.non_geometric_job();job['configurations']=[{'name':'Loctite'}]
        with self.assertRaisesRegex(ValueError,'cannot be combined'):
            start_check(self.part,self.index,self.cad,inventory_models(self.root),job,{'PROJECT_ROOT':self.root},'Loctite')

    def config_check(self,job,configuration):
        return start_check(self.part,self.index,self.cad,inventory_models(self.root),job,configuration=configuration)
    def test_selected_pending_configuration_proceeds_with_other_configuration_model(self):
        alpha=self.cad/'parts/ZX1234-alpha.dwg';alpha.write_bytes(b'Alpha model')
        job={'state':'DONE','configurations':[
            {'name':'State Alpha','state':'DONE','native_model':str(alpha)},
            {'name':'State Beta','state':'NOT_STARTED','native_model':'parts/ZX1234-beta.dwg'}]}
        result=self.config_check(job,'State Beta')
        self.assertEqual(result['action'],'NEW_MODEL_REQUIRED')
        self.assertEqual(result['models'],[])
        self.assertEqual(result['other_configuration_models'][0]['configuration'],'State Alpha')
    def test_selected_existing_configuration_skips(self):
        beta=self.cad/'parts/beta.dwg';beta.write_bytes(b'Beta model')
        job={'configurations':[{'name':'State Alpha'},{'name':'State Beta','native_model':str(beta)}]}
        result=self.config_check(job,'State Beta')
        self.assertEqual(result['action'],'SKIP_EXISTING_MODEL');self.assertEqual(result['models'][0]['path'],str(beta))
    def test_known_selected_model_is_reused_with_other_candidates_reported(self):
        beta=self.cad/'parts/beta.dwg';beta.write_bytes(b'Beta model')
        candidate=self.root/'candidate-ZX1234.dwg';candidate.write_bytes(b'Other candidate')
        job={'configurations':[{'name':'State Beta','native_model':str(beta)}]}
        result=self.config_check(job,'State Beta')
        self.assertEqual(result['action'],'SKIP_EXISTING_MODEL')
        self.assertEqual(result['candidates'][0]['path'],str(candidate))
    def test_unscoped_candidate_blocks_selected_configuration(self):
        beta=self.cad/'parts/beta.dwg';beta.write_bytes(b'Beta model')
        candidate=self.root/'candidate-ZX1234.dwg';candidate.write_bytes(b'Unscoped candidate')
        job={'configurations':[{'name':'State Alpha','native_model':str(beta)},{'name':'State Beta'}]}
        result=self.config_check(job,'State Beta')
        self.assertEqual(result['action'],'REVIEW_EXISTING_CANDIDATES')
        self.assertEqual(result['candidates'][0]['path'],str(candidate))
    def test_configuration_mode_preserves_2d_links_as_references(self):
        drawing=self.cad/'2d_schemas/drawings/ZX1234-interface.dwg';drawing.parent.mkdir(parents=True);drawing.write_bytes(b'2D fixture')
        selected=self.cad/'2d_schemas/drawings/ZX1234-selected-config.dwg';selected.write_bytes(b'Selected config 2D fixture')
        self.part['existing_cad']='2d_schemas/drawings/ZX1234-interface.dwg'
        job={'configurations':[{'name':'State Alpha'},{'name':'State Beta','native_model':str(selected)}]}
        result=self.config_check(job,'State Beta')
        self.assertEqual(result['action'],'NEW_MODEL_REQUIRED')
        self.assertEqual({r['path'] for r in result['references_2d']},{str(drawing),str(selected)})
    def test_configuration_audit_only_selects_requested_component(self):
        second_sheet=self.root/'second.md';second_sheet.write_text('Second input')
        model=self.cad/'parts/ZX5678-existing.dwg';model.write_bytes(b'Second component model')
        first=dict(id='C001',name='Example ZX1234 component',file='part.md',existing_cad='')
        second=dict(id='C002',name='Example ZX5678 component',file='second.md',existing_cad='parts/ZX5678-existing.dwg')
        self.index.write_text(json.dumps([first,second]));work=self.root/'work.json'
        work.write_text(json.dumps({'jobs':[
            {'part_id':'C001','state':'NOT_STARTED','configurations':[{'name':'State Alpha'},{'name':'State Beta'}]},
            {'part_id':'C002','state':'DONE'}]}))
        result=audit(self.index,work,self.cad,self.root,configuration='State Beta',part_id='C001')
        rows={row['part_id']:row for row in result['components']}
        self.assertEqual(rows['C001']['configuration'],'State Beta')
        self.assertEqual(rows['C001']['action'],'NEW_MODEL_REQUIRED')
        self.assertEqual(rows['C002']['action'],'SKIP_EXISTING_MODEL')
    def test_unknown_duplicate_and_missing_configurations_reject(self):
        with self.assertRaisesRegex(ValueError,'Unknown configuration'):
            self.config_check({'configurations':[{'name':'State Alpha'}]},'State Beta')
        with self.assertRaisesRegex(ValueError,'Duplicate declared configuration'):
            self.config_check({'configurations':[{'name':'State Beta'},{'name':'State Beta'}]},'State Beta')
        with self.assertRaisesRegex(ValueError,'nonempty configurations list'):
            self.config_check({'state':'DONE'},'State Beta')
    def test_selected_done_configuration_with_missing_model_requires_location(self):
        job={'state':'DONE','configurations':[{'name':'State Alpha'},{'name':'State Beta','state':'DONE','native_model':'parts/missing.dwg'}]}
        self.assertEqual(self.config_check(job,'State Beta')['action'],'LOCATE_COMPLETED_MODEL')
    def test_configured_audit_requires_id(self):
        self.index.write_text(json.dumps([self.part]));work=self.root/'work.json'
        work.write_text(json.dumps({'jobs':[{'part_id':'C001','configurations':[{'name':'State Alpha'}]}]}))
        with self.assertRaisesRegex(ValueError,'requires --id'):
            audit(self.index,work,self.cad,self.root,configuration='State Alpha')

if __name__=='__main__':unittest.main()
