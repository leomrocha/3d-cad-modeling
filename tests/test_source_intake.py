"""Source-intake contracts: fidelity, revisions, conflicts and protected output."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import source_intake as intake


class IntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.source=self.root/'drawing.txt';self.source.write_bytes(b'original drawing\n')
        self.spec={'job_name':'New source intake','revision_id':'r1','model':'test fixture',
                   'request':{'text':'Read drawing.\nPreserve café dimensions.','location':'test message'},
                   'scope':{'statement':'Record the supplied sources and correction.','requested_output':'source index',
                            'authorized_paths':[str(self.root)]},
                   'sources':[{'id':'drawing','title':'Original drawing','summary':'Fixture drawing source.',
                               'kind':'file','locator':str(self.source),'observed_at':'2026-11-12'}],
                   'corrections':[]}
    def execute(self,spec=None,name='result'):
        p=self.root/(name+'-input.json');p.write_text(json.dumps(spec or self.spec,ensure_ascii=False))
        result=intake.run(p,self.root/name)
        return Path(result['revision']),intake.verify_revision(Path(result['revision'])/'source-index.json')
    def test_file_hash_original_bytes_and_complete_output(self):
        before=self.source.read_bytes();folder,index=self.execute()
        self.assertEqual(index['sources'][0]['observation']['sha256'],hashlib.sha256(before).hexdigest())
        self.assertEqual(index['sources'][0]['observation']['bytes'],len(before))
        self.assertEqual(self.source.read_bytes(),before)
        self.assertTrue((folder/'scope.md').is_file())
        self.assertFalse((folder.parent/'incomplete').exists())
    def test_exact_text_correction_and_url_registration_without_network(self):
        s=copy.deepcopy(self.spec);s['sources'] += [
            dict(id='message',title='Correction message',summary='Exact supplied correction.',kind='text',locator='message:2',observed_at='2026-11-12',text='Ø22\n``` literal\n尾\n'),
            dict(id='url',title='Supplied reference',summary='URL locator only.',kind='url',locator='https://example.invalid/model?q=a%20b#source',observed_at='2026-11-12')]
        s['corrections']=[dict(id='correction1',source_id='drawing',statement='Use the revised drawing.',location='message:2')]
        with patch('socket.socket',side_effect=AssertionError('Network attempted')):
            folder,index=self.execute(s)
        self.assertEqual(index['request'],s['request']);self.assertEqual(index['sources'][1]['text'],s['sources'][1]['text'])
        self.assertEqual(index['corrections'],s['corrections'])
        self.assertEqual(index['sources'][2]['locator'],s['sources'][2]['locator'])
        self.assertEqual(index['sources'][2]['observation'],{'state':'registered_url_reference','network_requests':0})
    def test_new_revision_preserves_old_and_reports_changed_bytes(self):
        first,index=self.execute();old={p.name:p.read_bytes() for p in first.iterdir()}
        self.source.write_bytes(b'new drawing\n');spec=copy.deepcopy(self.spec);spec['revision_id']='r2';spec['prior_revision']=str(first/'source-index.json')
        second,current=self.execute(spec,'second')
        self.assertTrue(current['sources'][0]['content_changed'])
        self.assertEqual(current['sources'][0]['previous_observation'],index['sources'][0]['observation'])
        self.assertEqual(old,{p.name:p.read_bytes() for p in first.iterdir()})
    def test_equal_bytes_at_distinct_locators_keep_distinct_sources(self):
        second=self.root/'other.txt';second.write_bytes(self.source.read_bytes());s=copy.deepcopy(self.spec)
        row=copy.deepcopy(s['sources'][0]);row.update(id='other',locator=str(second));s['sources'].append(row)
        _,index=self.execute(s);a,b=index['sources'];self.assertNotEqual(a['locator'],b['locator'])
        self.assertEqual(a['observation']['sha256'],b['observation']['sha256'])
    def test_existing_completed_directory_is_protected(self):
        folder,_=self.execute();before={p.name:p.read_bytes() for p in folder.iterdir()}
        with self.assertRaises(FileExistsError):self.execute()
        self.assertEqual(before,{p.name:p.read_bytes() for p in folder.iterdir()})
    def test_duplicate_keys_and_nonfinite_input_rejected_before_output(self):
        for i,raw in enumerate(['{"job_name":"one","job_name":"two"}','{"n":NaN}','{"n":1e999}']):
            p=self.root/f'bad{i}.json';p.write_text(raw)
            with self.assertRaises(ValueError):intake.run(p,self.root/f'bad{i}')
            self.assertFalse((self.root/f'bad{i}').exists())
    def test_broken_references_duplicate_sources_and_cycles_rejected(self):
        bad=[]
        s=copy.deepcopy(self.spec);s['sources'].append(copy.deepcopy(s['sources'][0]));bad.append(s)
        s=copy.deepcopy(self.spec);s['sources'][0]['parent_id']='drawing';bad.append(s)
        s=copy.deepcopy(self.spec);s['corrections']=[dict(id='c',source_id='absent',statement='Change it.',location='m2')];bad.append(s)
        s=copy.deepcopy(self.spec);s['conflicts']=[dict(source_ids=['drawing','drawing'],summary='Duplicate source identity.',affected_scope='same source')];bad.append(s)
        for spec in bad:
            with self.assertRaises(ValueError):intake.validate(spec)
    def test_hash_conflict_retains_named_failed_attempt(self):
        s=copy.deepcopy(self.spec);s['sources'][0]['expected_sha256']='0'*64
        with self.assertRaises(intake.SourceConflict):self.execute(s)
        out=self.root/'result';self.assertTrue((out/'failure.json').is_file());self.assertTrue((out/'incomplete').is_dir())
        self.assertFalse((out/'revision').exists());self.assertEqual(json.loads((out/'failure.json').read_text())['state'],'FAILED')
    def test_missing_or_changing_file_retains_failure(self):
        for name,exception in [('missing',FileNotFoundError('source missing')),('changed',intake.RecordError('Source changed during capture'))]:
            original=intake.observe_file
            def observer(path):
                if Path(path)==self.source:raise exception
                return original(path)
            with patch.object(intake,'observe_file',side_effect=observer):
                with self.assertRaises(intake.SourceConflict):self.execute(name=name)
            self.assertTrue((self.root/name/'failure.json').is_file())
    def test_interrupted_publication_keeps_incomplete_attempt(self):
        with patch.object(intake.os,'rename',side_effect=OSError('publication interrupted')):
            with self.assertRaises(OSError):self.execute()
        out=self.root/'result';self.assertTrue((out/'incomplete/source-index.json').is_file())
        self.assertTrue((out/'failure.json').is_file());self.assertFalse((out/'revision').exists())
    def test_modified_prior_revision_is_detected(self):
        first,_=self.execute();(first/'scope.md').write_text('changed')
        s=copy.deepcopy(self.spec);s.update(revision_id='r2',prior_revision=str(first/'source-index.json'))
        with self.assertRaisesRegex(ValueError,'artifact changed'):self.execute(s,'second')
    def test_recorded_conflict_remains_attributed(self):
        s=copy.deepcopy(self.spec);row=copy.deepcopy(s['sources'][0]);row.update(id='other',parent_id='drawing');s['sources'].append(row)
        s['conflicts']=[dict(source_ids=['drawing','other'],summary='Two source claims differ.',affected_scope='terminal dimension')]
        _,index=self.execute(s);self.assertEqual(index['conflicts'],s['conflicts'])


if __name__=='__main__':unittest.main()
