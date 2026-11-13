import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import component_records as cr
from scripts import part_index as pi


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.index = self.root/'parts.json'
        self.index.write_text(json.dumps([{'id': 'P01', 'name': 'Rail équerre', 'file': 'rail.md'}]))

    def test_search_returns_original_namespace_and_digest(self):
        raw = self.index.read_bytes()
        row = pi.search([self.index], 'RAIL équerre')[0]
        self.assertEqual(row['id'], 'P01')
        self.assertEqual(row['index_sha256'], hashlib.sha256(raw).hexdigest())
        self.assertEqual(self.index.read_bytes(), raw)

    def test_dictionary_standard_is_searchable_with_edition(self):
        other = self.root/'dictionary.json'
        other.write_text(json.dumps({'entries': [{'id':'std', 'name':'Hitch interface', 'standard':'ISO 730', 'edition':'2009+A1:2014'}]}))
        self.assertEqual(pi.search([other], 'iso 730 2014')[0]['record_kind'], 'dictionary_entry')

    def test_same_id_in_two_indexes_keeps_both_sources(self):
        other = self.root/'dictionary.json'
        other.write_text(json.dumps({'entries':[{'id':'P01','name':'Different definition'}]}))
        self.assertEqual(len(pi.search([self.index, other], identifier='P01')), 2)

    def test_duplicate_id_rejected(self):
        self.index.write_text('[{"id":"x","name":"A"},{"id":"x","name":"B"}]')
        with self.assertRaises(pi.IndexError):pi.load_index(self.index)

    def test_duplicate_json_key_rejected(self):
        self.index.write_text('[{"id":"a","id":"b","name":"A"}]')
        with self.assertRaises(pi.IndexError):pi.load_index(self.index)

    def test_invalid_record_shape_rejected(self):
        self.index.write_text('[42]')
        with self.assertRaises(pi.IndexError):pi.load_index(self.index)

    def test_unknown_schema_rejected(self):
        self.index.write_text('{"parts":[]}')
        with self.assertRaises(pi.IndexError):pi.load_index(self.index)

    def test_cli_is_read_only_and_does_not_import_cad(self):
        before = self.index.read_bytes()
        r = subprocess.run([sys.executable,str(ROOT/'scripts/part_index.py'),'--index',str(self.index),'--id','P01'],capture_output=True,text=True)
        self.assertEqual(r.returncode,0)
        self.assertEqual(json.loads(r.stdout)['count'],1)
        self.assertEqual(self.index.read_bytes(),before)


class JobTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.source=self.root/'source.md';self.source.write_text('explicit fixture value\n')
        self.feature={'name':'fixture length','value':10,'unit':'mm','required':True,'evidence_status':'synthetic_fixture','source':str(self.source),'source_sha256':hashlib.sha256(self.source.read_bytes()).hexdigest(),'source_location':'line 1'}
        self.job={'job_id':'fixture','part_id':'fixture','part_name':'Fixture only','representation':'fixture','units':'mm','frame':'stated fixture frame','features':[self.feature]}

    def test_source_ready_requires_observed_matching_revision(self):
        result=cr.require_ready(self.job)
        self.assertEqual(result['state'],'SOURCE_READY')
        self.assertEqual(result['source_observations'][0]['sha256'],self.feature['source_sha256'])

    def test_missing_required_feature_blocks_without_filling_a_value(self):
        self.job['features'].append({'name':'corner profile','value':None,'required':True,'question':'Which sourced corner profile applies?'})
        before=copy.deepcopy(self.job)
        self.assertEqual(cr.readiness(self.job)['state'],'NEEDS_INPUT')
        with self.assertRaises(cr.RecordError):cr.require_ready(self.job)
        self.assertEqual(self.job,before)

    def test_source_revision_change_invalidates_readiness(self):
        self.source.write_text('corrected fixture value\n')
        with self.assertRaises(cr.RecordError):cr.readiness(self.job)

    def test_nonfinite_bool_and_unattributed_values_fail(self):
        for value in [float('nan'),float('inf'),True]:
            with self.subTest(value=value):
                self.feature['value']=value
                with self.assertRaises(cr.RecordError):cr.readiness(self.job)
        self.feature['value']=10;self.feature.pop('source_location')
        with self.assertRaises(cr.RecordError):cr.readiness(self.job)

    def test_required_flag_and_unique_feature_identity(self):
        self.job['features'].append(copy.deepcopy(self.feature))
        with self.assertRaises(cr.RecordError):cr.readiness(self.job)
        self.job['features']=[self.feature];self.feature['required']='yes'
        with self.assertRaises(cr.RecordError):cr.readiness(self.job)

    def test_file_changed_during_capture_is_detected(self):
        before=self.source.stat()
        fields={k:getattr(before,k) for k in ('st_dev','st_ino','st_size','st_mtime_ns','st_ctime_ns')}
        fields['st_size']+=1
        with mock.patch('scripts.component_records.Path.resolve',return_value=self.source), \
             mock.patch('scripts.component_records.Path.stat',side_effect=[before,type('Stat',(),fields)()]):
            with self.assertRaises(cr.RecordError):cr.observe_file(self.source)

    def test_optional_unknown_does_not_block_required_known_feature(self):
        self.job['features'].append({'name':'optional finish','value':None,'required':False})
        self.assertEqual(cr.readiness(self.job)['state'],'SOURCE_READY')

    def non_geometric_job(self):
        return {'job_id':'fixture-consumable','part_id':'fixture','part_name':'Fixture compound',
                'representation':'installation consumable record','units':'mm','frame':'mating pilot frame',
                'geometry_requirement':{'kind':'non_geometric_consumable','cad_required':False,
                    'source':{'path':'${PROJECT_ROOT}/source.md',
                              'sha256':hashlib.sha256(self.source.read_bytes()).hexdigest(),
                              'location':'Geometry and provenance, line 1'}}}

    def test_explicit_non_geometric_requirement_is_pinned_and_blocks_cad_builders(self):
        job=self.non_geometric_job()
        result=cr.readiness(job,{'PROJECT_ROOT':self.root})
        self.assertEqual(result['state'],'SOURCE_READY_NON_GEOMETRIC')
        self.assertEqual(result['geometry_requirement']['source']['sha256'],job['geometry_requirement']['source']['sha256'])
        with self.assertRaisesRegex(cr.RecordError,'CAD construction is prohibited'):
            cr.require_ready(job,{'PROJECT_ROOT':self.root})

    def test_non_geometric_requirement_rejects_changed_source(self):
        job=self.non_geometric_job();job['geometry_requirement']['source']['sha256']='0'*64
        with self.assertRaisesRegex(cr.RecordError,'source revision changed'):
            cr.readiness(job,{'PROJECT_ROOT':self.root})

    def test_non_geometric_requirement_rejects_malformed_declarations(self):
        mutations=[
            lambda r:r.update(cad_required=True),
            lambda r:r.update(cad_required='false'),
            lambda r:r.update(kind='skip'),
            lambda r:r.pop('source'),
        ]
        for mutate in mutations:
            job=self.non_geometric_job();mutate(job['geometry_requirement'])
            with self.subTest(requirement=job['geometry_requirement']), self.assertRaises(cr.RecordError):
                cr.readiness(job,{'PROJECT_ROOT':self.root})
        job=self.non_geometric_job();job['geometry_role']='reference_envelope'
        with self.assertRaisesRegex(cr.RecordError,'conflicts'):
            cr.readiness(job,{'PROJECT_ROOT':self.root})

    def test_non_geometric_cli_accepts_named_source_root(self):
        job=self.non_geometric_job();p=self.root/'non-geometric-job.json';p.write_text(json.dumps(job))
        r=subprocess.run([sys.executable,str(ROOT/'scripts/component_records.py'),str(p),
                          '--root','PROJECT_ROOT='+str(self.root)],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(json.loads(r.stdout)['state'],'SOURCE_READY_NON_GEOMETRIC')

    def test_cli_returns_named_question_and_preserves_input(self):
        self.feature['value']=None;self.feature['question']='What value applies?'
        p=self.root/'job.json';p.write_text(json.dumps(self.job));before=p.read_bytes()
        r=subprocess.run([sys.executable,str(ROOT/'scripts/component_records.py'),str(p)],capture_output=True,text=True)
        self.assertEqual(r.returncode,1);self.assertEqual(json.loads(r.stdout)['questions'][0]['question'],'What value applies?')
        self.assertEqual(p.read_bytes(),before)

    def occurrence(self):
        return {**{k:[] for k in cr.REQUIRED_ACTION_FIELDS},'occurrence_id':'event-1','job_id':'fixture','part_id':'fixture','part_name':'Fixture','action_id':'fixture','action_name':'Fixture operation','representation':'fixture record','units':'mm','frame':'explicit fixture frame','result':'PASS'}

    def test_append_preserves_previous_occurrence_and_rejects_duplicate(self):
        p=self.root/'actions.jsonl';e=self.occurrence();cr.append_occurrence(p,e);before=p.read_bytes()
        with self.assertRaises(cr.RecordError):cr.append_occurrence(p,e)
        self.assertEqual(p.read_bytes(),before)
        e['occurrence_id']='event-2';e['result']='FAIL';cr.append_occurrence(p,e)
        self.assertEqual([json.loads(x)['result'] for x in p.read_text().splitlines()],['PASS','FAIL'])

    def test_invalid_event_is_rejected_before_file_creation(self):
        p=self.root/'actions.jsonl';e=self.occurrence();e['result']='DONE'
        with self.assertRaises(cr.RecordError):cr.append_occurrence(p,e)
        self.assertFalse(p.exists())


if __name__=='__main__':unittest.main()
