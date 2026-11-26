from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from cadtools.runtime import CadError, Client, Journal, bounded_request_namespace


class FakeNative:
    READ_OPS = {"state", "operation"}

    def __init__(self):
        self.writes = []
        self.queries = []

    def request(self, descriptor, payload, timeout):
        if payload["op"] == "operation":
            self.queries.append(payload["request_id"])
            return {"ok": True, "status": "completed"}
        return {"ok": True, "document_id": 7, "revision": 2}

    def execute_checked(self, descriptor, payload, allow_write, timeout):
        self.writes.append(payload["request_id"])
        return {"ok": True, "status": "completed"}


class RepeatedHelperNamespaces(unittest.TestCase):
    def test_repeated_fixed_label_uses_distinct_stage_keys_and_preserves_recovery(self):
        helper = FakeNative()
        descriptor = {"session_id": "test-session"}
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "operations.jsonl"
            journal = Journal(path)
            stages = [bounded_request_namespace("owned-model-" * 8 + suffix)
                      for suffix in ("surface-style", "finish-style")]
            clients = [Client(helper, descriptor, 7, stage, journal, allow_write=True)
                       for stage in stages]
            label = "create-supporting-entities"
            for client in clients:
                client.mutate(label, "entities_create")
            first, second = [f"{stage}:{label}" for stage in stages]
            self.assertNotEqual(first, second)
            with self.assertRaisesRegex(CadError, "recover"):
                clients[0].mutate(label, "entities_create")
            self.assertEqual(helper.writes, [first, second])
            loaded = Journal(path)
            recovered = Client(helper, descriptor, 7, stages[0], loaded)
            recovered.recover(first)
            self.assertEqual(helper.queries, [first])
            self.assertEqual(set(loaded.requests), {first, second})
