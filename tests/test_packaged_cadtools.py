"""Generic runtime and persistence tests reused from the original cadtools suite.

Provenance and original hash: research/sources/skill-packaging-2026-11-13.json.
Component dictionaries, recipes and retained project data stay in their owner.
"""
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from cadtools.runtime import CadError, Client, Journal, Uncertain, redact
from cadtools.verification import save_reopen

class FakeHelper:
    READ_OPS = {"state","operation","query","audit","records","commands"}

    def __init__(self,responses=None,operations=None):
        self.responses = list(responses or [{"ok":True,"status":"completed","result":{}}])
        self.operations = list(operations or [])
        self.writes,self.reads = [],[]
        self.document_id = 7

    def request(self,descriptor,payload,timeout):
        self.reads.append(payload)
        if payload["op"]=="state":
            return {"ok":True,"document_id":self.document_id,"revision":4,"command":None,"modal":None}
        if payload["op"]=="operation":
            return self.operations.pop(0) if self.operations else {"ok":True,"status":"running"}
        return {"ok":True,"entities":[]}

    def execute_checked(self,descriptor,payload,allow_write,timeout):
        self.writes.append(payload)
        response = self.responses.pop(0)
        if isinstance(response,Exception):
            raise response
        return response

class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="cadtools-")
        self.path = Path(self.tmp.name)/"journal.jsonl"

    def tearDown(self):
        self.tmp.cleanup()

    def client(self,helper,allow_write=True,max_queries=2):
        return Client(helper,{"session_id":"fixture-session","token":"private-fixture"},7,"fixture",
                      Journal(self.path),allow_write=allow_write,max_queries=max_queries)

    def test_requires_authorisation(self):
        h = FakeHelper()
        with self.assertRaises(CadError):self.client(h,False).mutate("one","run",cmd="BOX")
        self.assertEqual(h.writes,[])

    def test_document_change_stops_before_send(self):
        h = FakeHelper();h.document_id=8
        with self.assertRaises(CadError):self.client(h).mutate("one","run",cmd="BOX")
        self.assertEqual(h.writes,[])

    def test_expected_revision_is_bound(self):
        h=FakeHelper();self.client(h).mutate('one','run',cmd='UNION')
        self.assertEqual(h.writes[0]['revision'],4)
        self.assertEqual(h.writes[0]['document_id'],7)

    def test_preflight_rejection_preserves_request(self):
        h=FakeHelper([RuntimeError('Current revision differs; write not sent')])
        with self.assertRaises(Uncertain):self.client(h).mutate('one','run',cmd='UNION')
        self.assertIn('fixture:one',Journal(self.path).requests)

    def test_same_id_timeout_recovery(self):
        h = FakeHelper([{"ok":False,"code":"response_timeout"}],
                       [{"ok":True,"status":"completed","result":{}}])
        self.client(h).mutate("one","run",cmd="EXTRUDE 10")
        self.assertEqual(len(h.writes),1)
        self.assertEqual([r['request_id'] for r in h.reads if r['op']=='operation'],['fixture:one'])

    def test_last_allowed_query_completion(self):
        h = FakeHelper([{"ok":True,"status":"running"}],
                       [{"ok":True,"status":"running"},{"ok":True,"status":"completed"}])
        self.assertEqual(self.client(h).mutate("one","run",cmd="UNION")["status"],"completed")

    def test_bounded_wait(self):
        h = FakeHelper([{"ok":True,"status":"running"}])
        with self.assertRaises(Uncertain):self.client(h).mutate("one","run",cmd="UNION")
        self.assertEqual(len(h.writes),1)
        self.assertEqual(len([r for r in h.reads if r['op']=='operation']),2)

    def test_lost_write_response_preserves_intent(self):
        h = FakeHelper([TimeoutError()]);c=self.client(h)
        with self.assertRaises(Uncertain):c.mutate("one","run",cmd="UNION")
        self.assertIn("fixture:one",Journal(self.path).requests)
        with self.assertRaises(CadError):c.mutate("one","run",cmd="UNION")
        self.assertEqual(len(h.writes),1)

    def test_explicit_recovery_never_writes(self):
        journal = Journal(self.path)
        journal.intent({"request_id":"fixture:one","op":"run"},
                       {"session_id":"fixture-session","document_id":7})
        h=FakeHelper(operations=[{"ok":True,"status":"completed"}])
        self.client(h,False).recover("fixture:one")
        self.assertEqual(h.writes,[])

    def test_recovery_rejects_different_context(self):
        Journal(self.path).intent({"request_id":"fixture:one"},
                                  {"session_id":"different-session","document_id":7})
        with self.assertRaises(CadError):self.client(FakeHelper()).recover("fixture:one")

    def test_creation_can_commit_during_waiting_input(self):
        response={"ok":True,"status":"waiting_input","result":{"created":1,"handles":["AA"]}}
        c=self.client(FakeHelper([response]))
        self.assertEqual(c.mutate("path","entities_create",allow_wait=True)["result"]["handles"],["AA"])

    def test_waiting_input_not_complete(self):
        c=self.client(FakeHelper([{"ok":True,"status":"waiting_input","result":{"created":1}}]))
        with self.assertRaises(CadError):c.mutate("path","entities_create")
        self.assertIn("fixture:path",Journal(self.path).requests)

    def test_partial_batch_cannot_replay(self):
        h=FakeHelper([{"ok":False,"status":"failed","changes":[{"kind":"Added","handle":"AA"}]}])
        c=self.client(h)
        with self.assertRaises(CadError):c.mutate("batch","batch",steps=[])
        with self.assertRaises(CadError):c.mutate("batch","batch",steps=[])
        self.assertIn('"handle": "AA"',self.path.read_text())

    def test_stale_second_journal_cannot_reserve_same_id(self):
        first,second=Journal(self.path),Journal(self.path)
        first.intent({"request_id":"same"},{})
        with self.assertRaises(CadError):second.intent({"request_id":"same"},{})

    def test_read_allowlist(self):
        with self.assertRaises(CadError):self.client(FakeHelper()).read("entities_delete")

    def test_unsupported_read_is_reported(self):
        h=FakeHelper();h.READ_OPS=h.READ_OPS|{"guide"}
        h.request=lambda *args:{"ok":False,"code":"unknown_operation","error":"Unknown operation"}
        with self.assertRaisesRegex(CadError,"Unknown operation"):self.client(h).read("guide")

    def test_journal_redacts_secrets(self):
        c=self.client(FakeHelper());c.mutate("tag","xdata_set",data={"token":"secret-fixture"})
        text=self.path.read_text()
        self.assertNotIn("secret-fixture",text)
        self.assertNotIn("private-fixture",text)
        self.assertEqual(redact({"Cookie":"abc"})['Cookie'],"[redacted]")

    def test_checkpoint_is_exclusive(self):
        c=self.client(FakeHelper());p=Path(self.tmp.name)/"state.json"
        c.checkpoint(p,{"body":"AA"})
        with self.assertRaises(FileExistsError):c.checkpoint(p,{})

class PersistenceTests(unittest.TestCase):
    """Synthetic file responses; no DWG encoder or OCS process is involved."""

    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='cadtools-')
        self.path=Path(self.tmp.name)/'synthetic.dwg'

    def tearDown(self):self.tmp.cleanup()

    def fixture(self,mode='ok'):
        import hashlib
        outer=self
        class Stub:
            document_id=7
            descriptor={}
            timeout=1
            opened=False
            def __init__(self):self.helper=self
            def read(self,op,**fields):
                counts={'3D Solid':2}
                if mode=='count_before' or (self.opened and mode=='count_after'):counts={'3D Solid':3}
                return {'summary':{'errors':0,'warnings':0},'manifest':{'by_type':counts,'total':sum(counts.values())}}
            def mutate(self,label,op,**fields):
                if op=='open':self.opened=True;return {'ok':True,'status':'completed'}
                content=b'synthetic transport fixture, not a CAD file'
                outer.path.write_bytes(content)
                result={'dropped_on_save':1 if mode=='loss' else 0,'verified':True,
                        'manifest':self.read('audit')['manifest'],
                        'sha256':'0'*64 if mode=='hash' else hashlib.sha256(content).hexdigest()}
                return {'ok':True,'status':'completed','result':result}
            def request(self,*args):
                return {'ok':True,'document_id':8,'documents':[{'id':8,'path':str(outer.path)}]}
        return Stub()

    def test_manifest_and_hash_round_trip(self):
        client=self.fixture();result=save_reopen(client,self.path,{'3D Solid':2})
        self.assertEqual(result['result'],'PASS');self.assertEqual(client.document_id,8)

    def test_existing_output_refused(self):
        self.path.write_bytes(b'existing')
        with self.assertRaises(CadError):save_reopen(self.fixture(),self.path,{'3D Solid':2})
        self.assertEqual(self.path.read_bytes(),b'existing')

    def test_wrong_presave_count(self):
        with self.assertRaises(CadError):save_reopen(self.fixture('count_before'),self.path,{'3D Solid':2})
        self.assertFalse(self.path.exists())

    def test_dropped_data_refused(self):
        with self.assertRaises(CadError):save_reopen(self.fixture('loss'),self.path,{'3D Solid':2})

    def test_file_hash_mismatch(self):
        with self.assertRaises(CadError):save_reopen(self.fixture('hash'),self.path,{'3D Solid':2})

    def test_reopened_manifest_mismatch(self):
        with self.assertRaises(CadError):save_reopen(self.fixture('count_after'),self.path,{'3D Solid':2})
