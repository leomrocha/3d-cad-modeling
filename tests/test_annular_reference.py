import hashlib
import importlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from annular_reference import build_annulus, inspect, parameters, verify, verify_metadata


class AnnularReferenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        source = Path(self.tmp.name) / 'synthetic-source.txt'
        source.write_text('synthetic dimension source for isolated tests\n', encoding='utf-8')
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        self.job = {
            'job_id': 'synthetic-annulus-job',
            'part_id': 'TEST-ONLY',
            'part_name': 'Synthetic ring',
            'representation': 'plain annular reference solid',
            'geometry_role': 'reference_annulus',
            'geometry_name': 'Synthetic ring geometry',
            'metadata_application': 'CADTOOLS_SOURCE',
            'metadata_request_label': 'synthetic geometry metadata write',
            'units': 'mm',
            'frame': 'test frame',
            'local_frame': 'local XY annulus with axis +Z; lower face at z_origin',
            'center': [2.0, -3.0],
            'z_origin': 4.0,
            'dimension_features': {
                'bore_diameter': 'bore',
                'outside_diameter': 'outside',
                'thickness': 'thickness',
            },
            'features': [
                {'name': name, 'value': value, 'unit': 'mm', 'required': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic isolated fixture',
                 'evidence_status': 'synthetic test input'}
                for name, value in [('bore', 8.0), ('outside', 18.0), ('thickness', 1.5)]
            ],
            'construction': {'cutter_overrun_mm': 0.25},
            'readback_tolerance': 1e-7,
        }

    def _features(self):
        return {
            'cylinders': [
                {'radius': 9.0, 'axis': [0, 0, 1], 'origin': [2, -3, 4]},
                {'radius': 4.0, 'axis': [0, 0, -1], 'origin': [2, -3, 4]},
            ],
            'planes': [
                {'origin': [2, -3, 4], 'normal': [0, 0, -1]},
                {'origin': [2, -3, 5.5], 'normal': [0, 0, 1]},
            ],
            'planar_face_loops': [
                {'origin': [2, -3, 4], 'normal': [0, 0, -1],
                 'loops': [{'edge_count': 1}, {'edge_count': 1}]},
                {'origin': [2, -3, 5.5], 'normal': [0, 0, 1],
                 'loops': [{'edge_count': 1}, {'edge_count': 1}]},
            ],
            'topology': {'bodies': 1, 'lumps': 1, 'shells': 1,
                         'reciprocal_closed_partners': True},
        }

    def test_parameters_are_external_and_dimension_bindings_are_explicit(self):
        p = parameters(self.job)
        self.assertEqual({'bore_diameter': 8.0, 'outside_diameter': 18.0,
                          'thickness': 1.5}, p['dimensions'])
        self.assertEqual([2.0, -3.0], p['center'])
        self.assertEqual((3.75, 5.75), (p['cut_start'], p['cut_end']))

    def test_build_uses_two_cylinders_and_boolean_subtraction(self):
        g = Mock()
        g.cylinder.side_effect = ['outer-handle', 'bore-handle']
        g.subtract.return_value = 'ring-handle'
        with patch('annular_reference.geometry', return_value=g):
            result = build_annulus(object(), self.job)
        self.assertEqual('ring-handle', result)
        self.assertEqual(2, g.cylinder.call_count)
        self.assertEqual(('Synthetic ring geometry annular solid', 'outer-handle',
                          ['bore-handle']), g.subtract.call_args.args)
        self.assertEqual('synthetic geometry metadata write', g.metadata.call_args.args[0])

    def test_invalid_inputs_fail_before_geometry_factory(self):
        cases = [
            ('nonpositive thickness', lambda j: j['features'][2].update(value=0)),
            ('bore not smaller than outside', lambda j: j['features'][0].update(value=18)),
            ('invalid cutter overrun', lambda j: j['construction'].update(cutter_overrun_mm=float('nan'))),
            ('overflowing cutter height', lambda j: j['construction'].update(cutter_overrun_mm=1e308)),
            ('underflowing bore radius', lambda j: j['features'][0].update(value=5e-324)),
            ('unsupported geometry role', lambda j: j.update(geometry_role='detailed_part')),
            ('invalid metadata', lambda j: j.update(metadata=[None])),
            ('far face lost to precision', lambda j: (j.update(z_origin=1e300),
                                                     j['features'][2].update(value=1.0))),
        ]
        for name, mutate in cases:
            with self.subTest(name=name):
                import copy
                job = copy.deepcopy(self.job)
                mutate(job)
                factory = Mock()
                with patch('annular_reference.geometry', factory):
                    with self.assertRaises(ValueError):
                        build_annulus(object(), job)
                factory.assert_not_called()

    def test_cylinder_plane_and_topology_observations_pass(self):
        result = verify(self._features(), self.job)
        self.assertEqual('PASS', result['result'])
        altered = self._features()
        altered['cylinders'][0]['radius'] = 8.9
        self.assertEqual('FAIL', verify(altered, self.job)['result'])
        altered = self._features()
        altered['planar_face_loops'][1]['loops'].pop()
        self.assertEqual('FAIL', verify(altered, self.job)['result'])
        altered = self._features()
        altered['cylinders'].append({'radius': 2.0, 'axis': [0, 0, 1],
                                     'origin': [4, -3, 4]})
        self.assertEqual('FAIL', verify(altered, self.job)['result'])
        altered = self._features()
        altered['planes'].append({'origin': [2, -3, 4.75], 'normal': [0, 1, 0]})
        self.assertEqual('FAIL', verify(altered, self.job)['result'])

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

    def test_installed_geometry_metadata_adapter_uses_reader_application(self):
        try:
            Geometry = importlib.import_module('cadtools.geometry').Geometry
        except ImportError as error:
            self.skipTest('CADTOOLS adapter is not on this test runtime: ' + str(error))
        client = Mock()
        Geometry(client).metadata('synthetic request label', ['A3'], ['synthetic line'])
        client.mutate.assert_called_once_with(
            'synthetic request label', 'xdata_set', handles=['A3'],
            app='CADTOOLS_SOURCE', data=[{'code': 1000, 'value': 'synthetic line'}])

    def test_unsupported_metadata_application_fails_before_geometry_factory(self):
        import copy
        job = copy.deepcopy(self.job)
        job['metadata_application'] = 'ANOTHER_APP'
        factory = Mock()
        with patch('annular_reference.geometry', factory):
            with self.assertRaisesRegex(ValueError, 'fixed CADTOOLS_SOURCE'):
                build_annulus(object(), job)
        factory.assert_not_called()

    def test_reopened_inspection_binds_sab_features_and_metadata_to_document_revision(self):
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
            response, result, found = inspect(Client(), 'A3', self.job)
        self.assertEqual('PASS', result['result'])
        self.assertEqual(12, result['geometry_revision'])
        self.assertIs(record, found)
        self.assertEqual('PASS', result['metadata']['result'])
        reader.assert_called_once_with(b'synthetic sab', include_loops=True)
        with patch('native_acis.sab_features', return_value=self._features()):
            with self.assertRaisesRegex(ValueError, 'geometry_revision differs'):
                inspect(Client(response_geometry=13), 'A3', self.job)


if __name__ == '__main__':
    unittest.main()
