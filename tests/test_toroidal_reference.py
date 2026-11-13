import copy
import hashlib
import importlib
import math
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from toroidal_reference import (build_torus, inspect, parameters, verify,
                                verify_metadata)


class ToroidalReferenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        source = Path(self.tmp.name) / 'synthetic-seal-source.txt'
        source.write_text('synthetic isolated torus dimensions\n', encoding='utf-8')
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        self.job = {
            'job_id': 'synthetic-torus-job',
            'part_id': 'TEST-ONLY',
            'part_name': 'Synthetic seal',
            'representation': 'nominal circular-section torus reference',
            'geometry_role': 'reference_torus',
            'geometry_name': 'Synthetic seal geometry',
            'metadata_application': 'CADTOOLS_SOURCE',
            'metadata_request_label': 'synthetic torus metadata write',
            'units': 'mm',
            'frame': 'synthetic frame',
            'local_frame': 'centre [2,-3,4] mm; local axis +Z',
            'center': [2.0, -3.0, 4.0],
            'axis': [0, 0, 1],
            'dimension_features': {
                'inside_diameter': 'inside diameter',
                'section_diameter': 'section diameter',
            },
            'features': [
                {'name': name, 'value': value, 'unit': 'mm', 'required': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic isolated fixture',
                 'evidence_status': 'synthetic test input'}
                for name, value in [('inside diameter', 20.0), ('section diameter', 4.0)]
            ],
            'readback_tolerance': 1e-7,
            'metadata': ['synthetic source binding'],
        }

    def _features(self):
        return {
            'tori': [
                {'center': [2.0, -3.0, 4.0], 'axis': [0, 0, 1],
                 'major_radius': 12.0, 'minor_radius': 2.0},
            ],
            'planes': [], 'cylinders': [], 'cones': [], 'spheres': [], 'ellipses': [],
            'topology': {'bodies': 1, 'lumps': 1, 'shells': 1,
                         'reciprocal_closed_partners': True},
        }

    def test_parameters_derive_radii_and_exact_four_arc_profile(self):
        p = parameters(self.job)
        self.assertEqual(12.0, p['major_radius'])
        self.assertEqual(2.0, p['minor_radius'])
        self.assertEqual(24.0, p['centerline_diameter'])
        self.assertEqual([[14.0, 0.0], [12.0, 2.0],
                          [10.0, 0.0], [12.0, -2.0]], p['profile_points'])
        self.assertAlmostEqual(math.tan(math.pi / 8), p['quarter_arc_bulge'])

    def test_build_uses_existing_revolve_and_moves_only_for_explicit_center(self):
        g = Mock()
        g.revolve_z.return_value = 'torus-handle'
        with patch('toroidal_reference.geometry', return_value=g):
            result = build_torus(object(), self.job)
        self.assertEqual('torus-handle', result)
        args, kwargs = g.revolve_z.call_args
        self.assertEqual('Synthetic seal geometry circular section', args[0])
        self.assertEqual(parameters(self.job)['profile_points'], args[1])
        self.assertEqual({0: math.tan(math.pi / 8), 1: math.tan(math.pi / 8),
                          2: math.tan(math.pi / 8), 3: math.tan(math.pi / 8)},
                         kwargs['bulges'])
        g.move.assert_called_once_with('Synthetic seal geometry local centre',
                                       ['torus-handle'], [2.0, -3.0, 4.0])
        g.metadata.assert_called_once()

    def test_invalid_inputs_fail_before_geometry_factory(self):
        cases = [
            ('zero inside diameter', lambda j: j['features'][0].update(value=0)),
            ('zero section diameter', lambda j: j['features'][1].update(value=0)),
            ('wrong units', lambda j: j.update(units='inch')),
            ('wrong geometry role', lambda j: j.update(geometry_role='detailed_part')),
            ('wrong local axis', lambda j: j.update(axis=[0, 1, 0])),
            ('wrong dimension keys', lambda j: j['dimension_features'].update(
                inside_diameter='section diameter')),
            ('nonfinite centre', lambda j: j['center'].__setitem__(1, float('nan'))),
            ('overflowing centre bound', lambda j: j['center'].__setitem__(0, 1e308)),
            ('nonfinite tolerance', lambda j: j.update(readback_tolerance=float('inf'))),
            ('invalid metadata', lambda j: j.update(metadata=[''])),
        ]
        for name, mutate in cases:
            with self.subTest(name=name):
                job = copy.deepcopy(self.job)
                mutate(job)
                factory = Mock()
                with patch('toroidal_reference.geometry', factory):
                    with self.assertRaises(ValueError):
                        build_torus(object(), job)
                factory.assert_not_called()

    def test_invalid_job_source_binding_fails_before_geometry_factory(self):
        job = copy.deepcopy(self.job)
        job['features'][0]['source_sha256'] = '0' * 64
        factory = Mock()
        with patch('toroidal_reference.geometry', factory):
            with self.assertRaises(ValueError):
                build_torus(object(), job)
        factory.assert_not_called()

    def test_analytic_torus_and_closed_body_observations_pass(self):
        result = verify(self._features(), self.job)
        self.assertEqual('PASS', result['result'])
        wrong = self._features()
        wrong['tori'][0]['major_radius'] = 12.1
        self.assertEqual('FAIL', verify(wrong, self.job)['result'])
        wrong = self._features()
        wrong['tori'][0]['center'][2] = 4.2
        self.assertEqual('FAIL', verify(wrong, self.job)['result'])
        wrong = self._features()
        wrong['tori'][0]['axis'] = [0, 1, 0]
        self.assertEqual('FAIL', verify(wrong, self.job)['result'])
        wrong = self._features()
        wrong['cylinders'] = [{'center': [2, -3, 4]}]
        self.assertEqual('FAIL', verify(wrong, self.job)['result'])
        wrong = self._features()
        wrong['topology']['reciprocal_closed_partners'] = False
        self.assertEqual('FAIL', verify(wrong, self.job)['result'])

    def test_duplicate_surface_patches_must_share_the_source_torus(self):
        features = self._features()
        features['tori'].append(copy.deepcopy(features['tori'][0]))
        self.assertEqual('PASS', verify(features, self.job)['result'])
        features['tori'][1]['minor_radius'] = 2.1
        self.assertEqual('FAIL', verify(features, self.job)['result'])

    def test_metadata_compares_stored_native_strings_and_handle(self):
        expected = parameters(self.job)['metadata']
        chunks = [line[i:i + 100] for line in expected for i in range(0, len(line), 100)]
        record = {'handle': 'A3', 'properties': {'common': {'extended_data': {
            'records': [{'application_name': 'CADTOOLS_SOURCE',
                         'values': [{'String': value} for value in chunks]}]}}}}
        self.assertEqual('PASS', verify_metadata(record, 'A3', self.job)['result'])
        with self.assertRaisesRegex(ValueError, 'handle'):
            verify_metadata(record, 'B4', self.job)
        record['properties']['common']['extended_data']['records'][0]['values'][0] = {
            'String': 'Changed synthetic identity'}
        self.assertEqual('FAIL', verify_metadata(record, 'A3', self.job)['result'])

    def test_installed_geometry_metadata_adapter_uses_fixed_application(self):
        try:
            Geometry = importlib.import_module('cadtools.geometry').Geometry
        except ImportError as error:
            self.skipTest('CADTOOLS adapter is not on this test runtime: ' + str(error))
        client = Mock()
        Geometry(client).metadata('synthetic request label', ['A3'], ['synthetic line'])
        client.mutate.assert_called_once_with(
            'synthetic request label', 'xdata_set', handles=['A3'],
            app='CADTOOLS_SOURCE', data=[{'code': 1000, 'value': 'synthetic line'}])

    def test_reopened_inspection_binds_reader_and_metadata_to_document_revision(self):
        expected = parameters(self.job)['metadata']
        chunks = [line[i:i + 100] for line in expected for i in range(0, len(line), 100)]
        record = {'handle': 'A3', 'type': 'Solid3D',
                  'properties': {'acis_data': {'sab_data': b'synthetic sab'},
                                 'common': {'extended_data': {'records': [
                                     {'application_name': 'CADTOOLS_SOURCE',
                                      'values': [{'String': value} for value in chunks]}]}}}}

        class Client:
            document_id = 91

            def __init__(self, response_geometry=12):
                self.states = [{'document_id': 91, 'geometry_revision': 12, 'revision': 8},
                               {'document_id': 91, 'geometry_revision': 12, 'revision': 8}]
                self.response_geometry = response_geometry

            def read(self, operation, **kwargs):
                if operation == 'state':
                    return self.states.pop(0)
                if operation == 'records':
                    return {'document_id': 91, 'geometry_revision': self.response_geometry,
                            'records': [record]}
                raise AssertionError('unexpected read')

        with patch('native_acis.sab_features', return_value=self._features()) as reader:
            _, result, found = inspect(Client(), 'A3', self.job)
        self.assertEqual('PASS', result['result'])
        self.assertEqual(12, result['geometry_revision'])
        self.assertIs(record, found)
        self.assertEqual('PASS', result['metadata']['result'])
        reader.assert_called_once_with(b'synthetic sab', include_loops=False,
                                       allow_tori=True)
        with patch('native_acis.sab_features', return_value=self._features()):
            with self.assertRaisesRegex(ValueError, 'geometry_revision differs'):
                inspect(Client(response_geometry=13), 'A3', self.job)


if __name__ == '__main__':
    unittest.main()
