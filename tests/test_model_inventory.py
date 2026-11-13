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

if __name__=='__main__':unittest.main()
