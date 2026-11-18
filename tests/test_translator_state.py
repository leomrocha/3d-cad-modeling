"""Persistence, concurrency and simulated crash tests, without a CAD installation."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
from threading import Barrier
import unittest

from translator.state import mapping_digest, StateConflict, StateStore


ENDPOINT = "connection-a"
OPERATION = "bore-diameter"
INTENT = dict(session="session-one", document="fixture", feature="bore",
              input_revision="r1", expected_effect="create exactly one feature")


def receipt(mapping, endpoint=ENDPOINT):
    return dict(endpoint=endpoint, operation=OPERATION, level="live_verified",
                result="PASS", mapping_sha256=mapping_digest(mapping),
                evidence_sha256="2" * 64)


class TranslatorState(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.path = Path(self.workspace.name) / "state.sqlite"
        self.store = StateStore(self.path)

    def promote(self, mapping, previous=None, endpoint=ENDPOINT):
        return self.store.promote(endpoint, OPERATION, expected_revision=previous,
                                  mapping=mapping, verification=receipt(mapping, endpoint))

    def test_promotion_cas_and_immutable_prior_revision(self):
        first = self.promote({"schema": 1})
        next_mapping = {"schema": 2}
        second = self.promote(next_mapping, previous=first["revision_id"])
        self.assertEqual(second["previous_revision"], first["revision_id"])
        with self.assertRaises(StateConflict):
            self.promote({"schema": 3}, previous=first["revision_id"])
        self.assertEqual(StateStore(self.path).active(ENDPOINT, OPERATION), second)
        with sqlite3.connect(self.path) as db:
            rows = db.execute("SELECT revision_id FROM revisions ORDER BY revision_id").fetchall()
            self.assertEqual(rows, [(first["revision_id"],), (second["revision_id"],)])

    def test_failed_verifications_never_replace_mapping(self):
        mapping = {"name": "tool-a"}
        first = self.promote(mapping)
        for override in [
            {"level": "offline_verified"}, {"endpoint": "connection-b"}, {"result": "FAIL"},
            {"operation": "other"}, {"mapping_sha256": "0" * 64}, {"evidence_sha256": ""},
        ]:
            with self.subTest(override=override), self.assertRaises(ValueError):
                self.store.promote(ENDPOINT, OPERATION, expected_revision=first["revision_id"],
                                   mapping=mapping, verification=dict(receipt(mapping), **override))
            self.assertEqual(self.store.active(ENDPOINT, OPERATION), first)

    def test_concurrent_promotion_has_one_winner(self):
        barrier = Barrier(2)

        def compete(number):
            barrier.wait(timeout=5)
            try:
                self.promote({"candidate": number})
                return "promoted"
            except StateConflict:
                return "conflict"

        with ThreadPoolExecutor(max_workers=2) as executor:
            self.assertCountEqual(executor.map(compete, [1, 2]), ["promoted", "conflict"])

    def test_process_death_before_commit_rolls_back_promotion(self):
        from translator import state
        first = self.promote({"schema": 1})
        code = """
import os, sys, sqlite3
db=sqlite3.connect(sys.argv[1])
db.execute('BEGIN IMMEDIATE')
db.execute('INSERT INTO revisions(endpoint,operation,mapping,verification) VALUES(?,?,?,?)',
           ('connection-a','bore-diameter','{}','{}'))
os._exit(31)
"""
        process = subprocess.run([sys.executable, "-I", "-B", "-c", code, self.path], check=False)
        self.assertEqual(process.returncode, 31)
        self.assertEqual(state.StateStore(self.path).active(ENDPOINT, OPERATION), first)

    def test_endpoint_isolation_and_tokens(self):
        self.store.begin_intent(ENDPOINT, "op-1", **INTENT)
        self.assertEqual(self.store.pending_intents("connection-b"), [])
        other = self.promote({"tool": "edit-b"}, endpoint="connection-b")
        self.assertIsNone(self.store.active(ENDPOINT, OPERATION))
        self.assertEqual(self.store.active("connection-b", OPERATION), other)
        self.store.begin_intent("connection-b", "op-1", **INTENT)
        self.store.resolve_intent("connection-b", "op-1", outcome="APPLIED",
                                  evidence="checked second connection")
        self.assertEqual(len(self.store.pending_intents(ENDPOINT)), 1)
        with self.assertRaises(StateConflict):
            self.store.begin_intent("connection-b", "op-1", **INTENT)

    def test_unresolved_intent_across_both_crash_windows(self):
        root = Path(__file__).resolve().parents[1]
        program = """
import os, sys
from pathlib import Path
sys.path.insert(0,sys.argv[1])
from translator.state import StateStore
store = StateStore(sys.argv[2])
store.begin_intent(sys.argv[3], 'create', session='s', document='d', feature='f',
                   input_revision='1', expected_effect='create one feature')
if sys.argv[4] == 'after':
    with open(sys.argv[5], 'a') as fixture:
        fixture.write('new feature')
os._exit(23)
"""
        for timing in ("before", "after"):
            with self.subTest(timing=timing):
                effect = self.path.with_name(timing + ".txt")
                process = subprocess.run([sys.executable, "-I", "-B", "-c", program, root,
                                          self.path, timing, timing, effect], check=False)
                self.assertEqual(process.returncode, 23)
                reopened = StateStore(self.path)
                pending = reopened.pending_intents(timing)
                self.assertEqual([(i["token"], i["status"]) for i in pending], [("create", "PENDING")])
                reopened.resolve_intent(timing, "create", outcome="UNKNOWN",
                                        evidence="connection lost after intent")
                with self.assertRaises(StateConflict):
                    reopened.begin_intent(timing, "another", **INTENT)
                self.assertEqual(bool(effect.exists()), timing == "after")
                if effect.exists():
                    self.assertEqual(effect.read_text(), "new feature")
                reopened.resolve_intent(timing, "create",
                                        outcome="APPLIED" if effect.exists() else "NOT_APPLIED",
                                        evidence="independent synthetic document inspected")
                self.assertEqual(reopened.pending_intents(timing), [])
                reopened.begin_intent(timing, "next", **INTENT)

    def test_unrelated_database_is_rejected(self):
        other = self.path.with_name("foreign.sqlite")
        with sqlite3.connect(other) as db:
            db.execute("CREATE TABLE user_data (v TEXT)")
        with self.assertRaises(ValueError):
            StateStore(other)


if __name__ == "__main__":
    unittest.main()
