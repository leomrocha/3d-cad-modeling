import hashlib
import tempfile
import unittest
from pathlib import Path

from scripts.ocs_document_cleanup import cleanup_active_owned_document


class FakeUncertain(RuntimeError):
    pass


class FakeRejected(RuntimeError):
    pass


class FakeSession:
    def __init__(self, documents, active):
        self.documents = {row['id']: dict(row) for row in documents}
        self.active = active
        self.revisions = {row['id']: row.get('geometry_revision', 0)
                          for row in documents}
        self.responses = {}
        self.last_tab_replacement = False
        self.replacement_dirty = False
        self.extra_replacements = 0
        self.revision_change_before_mutation = None

    def state(self):
        return {'ok': True, 'document_id': self.active,
                'geometry_revision': self.revisions.get(self.active, 0),
                'command': None, 'modal': None,
                'documents': [dict(row) for row in self.documents.values()]}

    def close(self, identity, discard):
        self.documents.pop(identity)
        self.revisions.pop(identity, None)
        if self.documents:
            self.active = next(iter(self.documents))
        elif self.last_tab_replacement:
            self.active = 99
            self.documents[99] = {'id': 99, 'path': None,
                                   'dirty': self.replacement_dirty,
                                   'title': 'Drawing1'}
            self.revisions[99] = 0
            for index in range(self.extra_replacements):
                identity = 100 + index
                self.documents[identity] = {'id': identity, 'path': None,
                                             'dirty': False,
                                             'title': f'Drawing{identity}'}
                self.revisions[identity] = 0
        return {'result': {'closed': True}}


class FakeClient:
    def __init__(self, session, document_id, namespace, uncertain=False):
        self.session = session
        self.document_id = document_id
        self.namespace = namespace
        self.uncertain = uncertain
        self.mutations = []
        self.recoveries = []

    def mutate(self, label, operation, **fields):
        self.mutations.append((label, operation, fields))
        if self.session.revision_change_before_mutation is not None:
            self.session.revisions[self.document_id] = \
                self.session.revision_change_before_mutation
            self.session.documents[self.document_id]['geometry_revision'] = \
                self.session.revision_change_before_mutation
        if fields.get('geometry_revision') != self.session.revisions[self.document_id]:
            raise FakeRejected('geometry revision compare-and-swap rejected')
        response = self.session.close(self.document_id, fields.get('discard'))
        self.session.responses[self.namespace + ':' + label] = response
        if self.uncertain:
            raise FakeUncertain('response was lost after close')
        return response

    def recover(self, request_id):
        self.recoveries.append(request_id)
        return self.session.responses[request_id]


class DocumentCleanupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.saved_path = Path(self.temp.name) / 'component.dwg'
        self.saved_path.write_bytes(b'saved completed model')
        self.digest = hashlib.sha256(self.saved_path.read_bytes()).hexdigest()
        self.expected_path = str(self.saved_path)

    def tearDown(self):
        self.temp.cleanup()

    def evidence(self, *, dirty=False, revision=17, allowed=None,
                 construction_copy=None, digest=None, saved_path=None,
                 receipt_result='PASS', receipt_path=None, receipt_hash=None,
                 expected_path='USE_DEFAULT'):
        if allowed is None:
            allowed = dirty
        if construction_copy is None:
            construction_copy = dirty
        if digest is None:
            digest = self.digest
        if saved_path is None:
            saved_path = str(self.saved_path)
        if expected_path == 'USE_DEFAULT':
            expected_path = self.expected_path
        if receipt_path is None:
            receipt_path = expected_path if expected_path is not None else saved_path
        if receipt_hash is None:
            receipt_hash = digest
        return {
            'document_id': 10,
            'expected_path': expected_path,
            'expected_geometry_revision': revision,
            'construction_copy': construction_copy,
            'dirty_discard_allowed': allowed,
            'saved_model_path': saved_path,
            'saved_model_sha256': digest,
            'persistence_receipt': {'result': receipt_result,
                                    'saved_path': receipt_path,
                                    'sha256': receipt_hash},
        }

    def session(self, *, dirty=False, revision=17, active=10, path=None):
        return FakeSession([
            {'id': 10, 'path': self.expected_path if path is None else path, 'dirty': dirty,
             'geometry_revision': revision},
            {'id': 20, 'path': str(Path(self.temp.name) / 'unrelated.dwg'),
             'dirty': True, 'geometry_revision': 4},
        ], active)

    def run_cleanup(self, session, rows, *, uncertain=False):
        clients = []

        def factory(document_id, namespace):
            client = FakeClient(session, document_id, namespace, uncertain)
            clients.append(client)
            return client

        result = cleanup_active_owned_document(
            state_reader=session.state, client_factory=factory,
            owned_documents=rows, namespace='cleanup-test',
            uncertain_type=FakeUncertain)
        return result, clients

    def test_clean_owned_document_closes_and_preserves_unrelated_dirty_tab(self):
        session = self.session(dirty=False)
        result, clients = self.run_cleanup(session, [self.evidence()])
        self.assertEqual('CLOSED', result['cleanup_status'])
        self.assertEqual('PASS', result['result'])
        self.assertEqual([], result['remaining_owned_document_ids'])
        self.assertNotIn(10, session.documents)
        self.assertEqual({'path': str(Path(self.temp.name) / 'unrelated.dwg'),
                          'dirty': True},
                         {key: session.documents[20][key] for key in ('path', 'dirty')})
        self.assertEqual(('close-owned-document-10', 'close',
                          {'discard': False, 'geometry_revision': 17}),
                         clients[0].mutations[0])

    def test_owned_dirty_construction_copy_closes_at_matching_epoch(self):
        session = self.session(dirty=True, revision=17)
        result, clients = self.run_cleanup(session,
                                           [self.evidence(dirty=True, revision=17)])
        self.assertEqual('CLOSED', result['cleanup_status'])
        self.assertTrue(result['dirty_construction_copy_discarded'])
        self.assertTrue(clients[0].mutations[0][2]['discard'])

    def test_owned_unsaved_construction_copy_matches_null_expected_path(self):
        session = self.session(dirty=True, revision=17, path='')
        session.documents[10]['path'] = None
        result, clients = self.run_cleanup(
            session, [self.evidence(dirty=True, revision=17, expected_path=None)])
        self.assertEqual('CLOSED', result['cleanup_status'])
        self.assertTrue(clients[0].mutations[0][2]['discard'])

    def test_changed_geometry_epoch_blocks_dirty_discard(self):
        session = self.session(dirty=True, revision=18)
        result, clients = self.run_cleanup(session,
                                           [self.evidence(dirty=True, revision=17)])
        self.assertEqual('GEOMETRY_REVISION_MISMATCH', result['cleanup_status'])
        self.assertEqual([], clients)
        self.assertIn(10, session.documents)

    def test_missing_saved_model_blocks_close(self):
        session = self.session()
        result, clients = self.run_cleanup(
            session, [self.evidence(saved_path=str(Path(self.temp.name) / 'missing.dwg'))])
        self.assertEqual('SAVED_MODEL_UNAVAILABLE', result['cleanup_status'])
        self.assertEqual([], clients)
        self.assertIn(10, session.documents)

    def test_wrong_saved_model_hash_blocks_close(self):
        session = self.session()
        result, clients = self.run_cleanup(
            session, [self.evidence(digest='0' * 64, receipt_hash='0' * 64)])
        self.assertEqual('SAVED_MODEL_HASH_MISMATCH', result['cleanup_status'])
        self.assertEqual([], clients)
        self.assertIn(10, session.documents)

    def test_failed_or_mismatched_persistence_receipt_blocks_close(self):
        cases = [
            self.evidence(receipt_result='FAIL'),
            self.evidence(receipt_path='${PROJECT_ROOT}/cad/parts/other.dwg'),
            self.evidence(receipt_hash='0' * 64),
        ]
        for evidence in cases:
            with self.subTest(receipt=evidence['persistence_receipt']):
                session = self.session()
                result, clients = self.run_cleanup(session, [evidence])
                self.assertIn(result['cleanup_status'], {
                    'PERSISTENCE_RECEIPT_FAILED', 'PERSISTENCE_RECEIPT_MISMATCH'})
                self.assertEqual([], clients)
                self.assertIn(10, session.documents)

    def test_unrelated_dirty_document_is_preserved(self):
        session = self.session(dirty=False)
        before = {identity: (row['path'], row['dirty'])
                  for identity, row in session.documents.items() if identity != 10}
        result, _ = self.run_cleanup(session, [self.evidence()])
        after = {identity: (row['path'], row['dirty'])
                 for identity, row in session.documents.items()}
        self.assertEqual('CLOSED', result['cleanup_status'])
        self.assertEqual(before, after)

    def test_unknown_active_document_halts_and_returns_remaining_owned_ids(self):
        session = self.session(active=20)
        result, clients = self.run_cleanup(session, [self.evidence()])
        self.assertEqual('ACTIVE_DOCUMENT_OUTSIDE_OWNED_SET', result['cleanup_status'])
        self.assertEqual([10], result['remaining_owned_document_ids'])
        self.assertEqual([], clients)
        self.assertEqual({10, 20}, set(session.documents))

    def test_uncertain_close_recovers_same_request_without_replay(self):
        session = self.session()
        result, clients = self.run_cleanup(session, [self.evidence()], uncertain=True)
        self.assertEqual('CLOSED', result['cleanup_status'])
        self.assertEqual(1, len(clients[0].mutations))
        self.assertEqual(['cleanup-test:close-owned-document-10'],
                         clients[0].recoveries)
        self.assertNotIn(10, session.documents)

    def test_dirty_unowned_or_unapproved_document_is_never_discarded(self):
        session = self.session(dirty=True)
        result, clients = self.run_cleanup(
            session, [self.evidence(dirty=True, allowed=False, construction_copy=False)])
        self.assertEqual('DIRTY_DISCARD_NOT_AUTHORIZED', result['cleanup_status'])
        self.assertEqual([], clients)
        self.assertIn(10, session.documents)

    def test_revision_change_between_preflight_and_mutation_is_rejected_without_close(self):
        session = self.session(dirty=True, revision=17)
        session.revision_change_before_mutation = 18
        result, clients = self.run_cleanup(
            session, [self.evidence(dirty=True, revision=17)])
        self.assertEqual('GEOMETRY_REVISION_CHANGED_BEFORE_CLOSE',
                         result['cleanup_status'])
        self.assertIsNone(result['closed_document_id'])
        self.assertIn(10, session.documents)
        self.assertEqual(1, len(clients[0].mutations))
        self.assertEqual(17, clients[0].mutations[0][2]['geometry_revision'])

    def test_closing_last_owned_tab_accepts_new_clean_untitled_replacement(self):
        session = FakeSession([{'id': 10, 'path': self.expected_path,
                                'dirty': False, 'geometry_revision': 17}], 10)
        session.last_tab_replacement = True
        result, _ = self.run_cleanup(session, [self.evidence()])
        self.assertEqual('CLOSED', result['cleanup_status'])
        self.assertEqual(99, result['replacement_document_id'])
        self.assertEqual('NEW_CLEAN_UNTITLED_REPLACEMENT',
                         result['replacement_document_status'])
        self.assertEqual(99, result['active_document_after'])

    def test_dirty_last_tab_replacement_is_reported_as_postcheck_failure(self):
        session = FakeSession([{'id': 10, 'path': self.expected_path,
                                'dirty': False, 'geometry_revision': 17}], 10)
        session.last_tab_replacement = True
        session.replacement_dirty = True
        result, _ = self.run_cleanup(session, [self.evidence()])
        self.assertEqual('POSTCHECK_DOCUMENT_SET_CHANGED', result['cleanup_status'])
        self.assertEqual(10, result['closed_document_id'])

    def test_multiple_last_tab_replacements_are_reported_as_postcheck_failure(self):
        session = FakeSession([{'id': 10, 'path': self.expected_path,
                                'dirty': False, 'geometry_revision': 17}], 10)
        session.last_tab_replacement = True
        session.extra_replacements = 1
        result, _ = self.run_cleanup(session, [self.evidence()])
        self.assertEqual('POSTCHECK_DOCUMENT_SET_CHANGED', result['cleanup_status'])
        self.assertEqual(10, result['closed_document_id'])

    def test_postcheck_failure_preserves_confirmed_closed_identity(self):
        session = self.session()
        original_state = session.state
        reads = 0

        def altered_state():
            nonlocal reads
            reads += 1
            state = original_state()
            if reads == 2:
                state['documents'][0]['dirty'] = False
            return state

        clients = []

        def factory(document_id, namespace):
            client = FakeClient(session, document_id, namespace)
            clients.append(client)
            return client

        result = cleanup_active_owned_document(
            state_reader=altered_state, client_factory=factory,
            owned_documents=[self.evidence()], namespace='cleanup-test',
            uncertain_type=FakeUncertain)
        self.assertEqual('POSTCHECK_OTHER_DOCUMENT_CHANGED', result['cleanup_status'])
        self.assertEqual(10, result['closed_document_id'])
        self.assertTrue(result['close_confirmed'])
        self.assertEqual('cleanup-test:close-owned-document-10', result['request_id'])


if __name__ == '__main__':
    unittest.main()
