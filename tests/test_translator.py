"""Exercise mapping scope and discovery without starting a CAD application."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'skills/cad-mcp-translator'
spec = importlib.util.spec_from_file_location('cad_mapping', ROOT / 'translator/translator.py')
mapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mapper)


class OfflineDiscovery(unittest.TestCase):
    def setUp(self):
        self.mapping = json.loads((PACKAGE / 'mappings/freecad.json').read_text())
        self.selection = ('freecad', self.mapping['bridge'], self.mapping['operation'])
        names = sorted({row['tool'] for row in self.mapping['steps']})
        self.snapshot = dict(application='freecad', bridge=self.selection[1], connection='fixture-A',
                             workspace='disposable', session='session-A', document='plate',
                             privileges='read', settings='mm', protocol='example', transport='http',
                             generation='epoch-1', changed=False, pages=[
                                 dict(cursor=None, generation='epoch-1', tools=[
                                     dict(name=n, inputSchema={'type': 'object'}) for n in names])])

    def observe(self, **kwargs):
        return mapper.plan(self.mapping, *self.selection, snapshot=self.snapshot,
                           connection='fixture-A', **kwargs)

    def test_offline_candidates(self):
        for path in (PACKAGE / 'mappings').glob('*.json'):
            mapping = json.loads(path.read_text())
            result = mapper.plan(mapping, mapping['application'], mapping['bridge'], mapping['operation'])
            self.assertIn(result['status'], ('DOCUMENTED', 'DISCOVERY_REQUIRED'))
            self.assertNotIn('binding_sha256', result)

    def test_scoped_selection(self):
        for selection in [('ocs', *self.selection[1:]), ('freecad', 'other', self.selection[2]),
                          ('freecad', self.selection[1], 'export')]:
            with self.assertRaises(ValueError):
                mapper.plan(self.mapping, *selection)
        self.snapshot['connection'] = 'fixture-B'
        with self.assertRaises(ValueError):
            self.observe()

    def test_missing_tools_and_version(self):
        self.assertTrue(self.observe()['session_only'])
        self.assertEqual(self.observe()['status'], 'SCHEMA_OBSERVED')
        self.snapshot['pages'][0]['tools'].pop()
        self.assertEqual(self.observe()['status'], 'DISCOVERY_REQUIRED')

    def test_stale_binding(self):
        first = self.observe()['binding_sha256']
        self.assertEqual(self.observe(previous=first)['status'], 'SCHEMA_OBSERVED')
        for key in ('privileges', 'workspace', 'settings', 'document', 'session', 'host_version'):
            with self.subTest(key=key):
                original = self.snapshot.copy()
                self.snapshot[key] = 'changed'
                self.assertEqual(self.observe(previous=first)['status'], 'STALE_BINDING')
                self.snapshot = original
        self.snapshot['pages'][0]['tools'][0]['inputSchema']['required'] = ['newField']
        self.assertEqual(self.observe(previous=first)['status'], 'STALE_BINDING')

    def test_interrupted_discovery(self):
        original = copy.deepcopy(self.snapshot)
        self.snapshot['changed'] = True
        with self.assertRaises(ValueError):
            self.observe()
        self.snapshot = original
        page = self.snapshot['pages'][0]
        page['nextCursor'] = 'page-2'
        with self.assertRaises(ValueError):
            self.observe()
        second = dict(cursor='page-2', generation='epoch-1', tools=[])
        self.snapshot['pages'].append(second)
        self.assertEqual(self.observe()['status'], 'SCHEMA_OBSERVED')
        second['nextCursor'] = 'page-2'
        with self.assertRaises(ValueError):
            self.observe()
        del second['nextCursor']
        second['generation'] = 'epoch-2'
        with self.assertRaises(ValueError):
            self.observe()


class ContributionChoices(unittest.TestCase):
    def test_opt_in_scope_change_and_partial_result(self):
        scope = dict(commit='fixture-commit', diff_sha256='fixture-digest', destination='fork',
                     source_branch='candidate', target_branch='base')
        calls = []
        for choice in (None, False):
            self.assertEqual(mapper.contribution_step(choice, None), 'KEEP_LOCAL')
        self.assertEqual(mapper.contribution_step(True, None), 'PREPARE_PREVIEW')
        self.assertEqual(mapper.contribution_step(True, scope), 'SHOW_FINAL_SCOPE')
        for field in scope:
            narrowed = dict(scope, **{field: 'changed'})
            self.assertEqual(mapper.contribution_step(True, narrowed, scope), 'SHOW_FINAL_SCOPE')
        if mapper.contribution_step(True, scope, scope.copy()) == 'SUBMIT_APPROVED_REVISION':
            calls.append(('push', 'ok'))
            calls.append(('open-pr', 'simulated failure'))
        self.assertEqual(calls, [('push', 'ok'), ('open-pr', 'simulated failure')])
