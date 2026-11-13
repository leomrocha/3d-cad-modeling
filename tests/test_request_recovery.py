"""Verify bounded same-request polling without mutation replay."""
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import envelope_job_runner as runner

class RecoveryBackoffTests(unittest.TestCase):
    def client(self):
        class Uncertain(Exception): pass
        self.Uncertain = Uncertain
        module=types.ModuleType('cadtools.runtime');module.Uncertain=Uncertain
        client=Mock();client.namespace='synthetic-request'
        client.mutate.side_effect=Uncertain('query bound')
        return client,module

    def test_running_queries_eventually_complete_same_request(self):
        client,module=self.client()
        client.recover.side_effect=[self.Uncertain('still running'),self.Uncertain('still running'),{'status':'completed'}]
        with patch.dict(sys.modules,{'cadtools.runtime':module}),patch.object(runner.time,'sleep') as sleep:
            result=runner.RecoveringClient(client).mutate('open','open',path='synthetic.dwg')
        self.assertEqual('completed',result['status'])
        client.mutate.assert_called_once_with('open','open',allow_wait=False,path='synthetic.dwg')
        self.assertEqual([(('synthetic-request:open',),{'allow_wait':False})]*3,client.recover.call_args_list)
        self.assertEqual([((0.25,),{}),((0.5,),{})],sleep.call_args_list)

    def test_persistent_uncertainty_stops_at_fixed_bound(self):
        client,module=self.client();client.recover.side_effect=self.Uncertain('still running')
        with patch.dict(sys.modules,{'cadtools.runtime':module}),patch.object(runner.time,'sleep') as sleep:
            with self.assertRaises(self.Uncertain):runner.RecoveringClient(client).mutate('open','open')
        self.assertEqual(1,client.mutate.call_count);self.assertEqual(4,client.recover.call_count)
        self.assertEqual(3,sleep.call_count)

    def test_definite_error_propagates_without_more_queries(self):
        client,module=self.client();client.recover.side_effect=ValueError('rejected')
        with patch.dict(sys.modules,{'cadtools.runtime':module}),patch.object(runner.time,'sleep') as sleep:
            with self.assertRaises(ValueError):runner.RecoveringClient(client).mutate('open','open')
        client.recover.assert_called_once();sleep.assert_not_called()

if __name__=='__main__':unittest.main()
