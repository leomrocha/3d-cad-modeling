"""Same-document recovery requires the original request and the live idle epoch."""
from pathlib import Path
from types import SimpleNamespace
import sys
import unittest
from unittest.mock import Mock

sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'scripts'))
from cadtools.checkpoints import recover_idle_mutation
from cadtools.runtime import CadError


class IdleMutationRecovery(unittest.TestCase):
    def setUp(self):
        self.key='job:move-part'
        self.fields={'handles':['AB'],'action':'move','vector':[1,2,3]}
        self.context={'session_id':'fixture','document_id':4}
        request=dict(self.fields,op='entities_transform',request_id=self.key,document_id=4,revision=2)
        self.state=dict(ok=True,document_id=4,revision=3,geometry_revision=11,
                        command=None,operation=None,modal=None)
        self.client=SimpleNamespace(namespace='job',descriptor=self.context,document_id=4,
            journal=SimpleNamespace(requests={self.key:{'context':self.context,'request':request}}),
            read=Mock(return_value=self.state.copy()),
            recover=Mock(return_value=dict(ok=True,status='completed',request_id=self.key,state=self.state.copy())))

    def run_check(self, fields=None):
        return recover_idle_mutation(self.client,'move-part','entities_transform',
                                     fields=self.fields if fields is None else fields)

    def test_valid_recovery_reads_same_request_once(self):
        self.assertEqual(self.run_check()['request_id'],self.key)
        self.client.recover.assert_called_once_with(self.key)
        self.client.read.assert_called_once_with('state')

    def test_different_operands_fail_before_recovery(self):
        with self.assertRaisesRegex(CadError,'contract'):
            self.run_check(dict(self.fields,vector=[1,2,4]))
        self.client.recover.assert_not_called()

    def test_new_geometry_revision_fails(self):
        self.client.read.return_value['geometry_revision']+=1
        with self.assertRaisesRegex(CadError,'idle owned document'):
            self.run_check()

    def test_active_prompt_fails_at_matching_revision(self):
        self.client.read.return_value['command']={'name':'INSERT'}
        with self.assertRaisesRegex(CadError,'idle owned document'):
            self.run_check()

    def test_waiting_operation_fails(self):
        self.client.recover.return_value['status']='waiting_input'
        with self.assertRaisesRegex(CadError,'completed receipt'):
            self.run_check()
        self.client.read.assert_not_called()
