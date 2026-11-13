import copy
import hashlib
import math
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from hexagonal_reference import (build_hexagonal_reference, parameters,
                                 inspect, regular_hexagon_points, verify,
                                 verify_metadata)


class HexagonalReferenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / 'source.txt'
        self.source.write_text('synthetic dimension source\n', encoding='utf-8')
        self.digest = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.job = {
            'job_id': 'synthetic-hex-job', 'part_id': 'TEST-HEX',
            'part_name': 'Synthetic hex reference',
            'representation': 'source-bound external hexagonal prism reference',
            'geometry_role': 'reference_hexagonal_prism',
            'geometry_name': 'Synthetic hex',
            'metadata_application': 'CADTOOLS_SOURCE',
            'metadata_request_label': 'synthetic hex metadata',
            'units': 'mm', 'frame': 'test frame',
            'local_frame': 'origin at base face centre; +Z axial; +X radial',
            'dimension_features': {'across_flats': 'af', 'height': 'height'},
            'features': [
                {'name': name, 'value': value, 'unit': 'mm', 'required': True,
                 'source': str(self.source), 'source_sha256': self.digest,
                 'source_location': 'synthetic fixture', 'evidence_status': 'synthetic test'}
                for name, value in [('af', 19.0), ('height', 12.0)]
            ],
            'source_files': [{'path': str(self.source),
                              'locator': '${SOURCE_ROOT}/source.txt',
                              'sha256': self.digest}],
            'placement': {'origin': [4.0, -3.0, 2.0], 'axis': [0.0, 0.0, 1.0],
                          'radial_x': [1.0, 0.0, 0.0]},
            'metadata': ['Source limit values represented as reference geometry'],
            'readback_tolerance_mm': 1e-7,
        }

    def _features(self, job=None, bore=False):
        p = parameters(job or self.job)
        points = regular_hexagon_points(p['across_flats_mm'])
        middle = [p['origin'][i] + p['axis'][i] * p['height_mm'] / 2.0
                  for i in range(3)]
        planes = []
        for index, a in enumerate(points):
            b = points[(index + 1) % 6]
            dx, dy = b[0] - a[0], b[1] - a[1]
            length = math.hypot(dx, dy)
            normal = [(dy / length) * p['radial_x'][i]
                      + (-dx / length) * p['radial_y'][i]
                      for i in range(3)]
            distance = p['across_flats_mm'] / 2.0
            planes.append({'normal': normal,
                           'origin': [middle[i] + normal[i] * distance
                                      for i in range(3)]})
        planes += [
            {'normal': [-value for value in p['axis']], 'origin': p['origin']},
            {'normal': p['axis'], 'origin': p['end']},
        ]
        features = {'planes': planes, 'cylinders': [],
                    'topology': {'bodies': 1, 'lumps': 1, 'shells': 1,
                                 'reciprocal_closed_partners': True}}
        if bore:
            features['cylinders'] = [{'axis': p['axis'], 'origin': p['origin'],
                                      'radius': p['bore_diameter_mm'] / 2.0}]
            features['planar_face_loops'] = [
                {'origin': p['origin'], 'normal': [-v for v in p['axis']],
                 'loops': [{'edge_count': 6}, {'edge_count': 1}]},
                {'origin': p['end'], 'normal': p['axis'],
                 'loops': [{'edge_count': 6}, {'edge_count': 1}]},
            ]
        return features

    def test_regular_hexagon_has_sourced_across_flats(self):
        points = regular_hexagon_points(19.0)
        edge_normals = []
        for i, a in enumerate(points):
            b = points[(i + 1) % 6]
            dx, dy = b[0] - a[0], b[1] - a[1]
            length = math.hypot(dx, dy)
            normal = [dy / length, -dx / length]
            edge_normals.append(abs(normal[0] * a[0] + normal[1] * a[1]))
        self.assertEqual(6, len(points))
        for distance in edge_normals:
            self.assertAlmostEqual(9.5, distance)
        with self.assertRaises(ValueError):
            regular_hexagon_points(1e-300, center=[1e300, 1e300])
        with self.assertRaises(ValueError):
            regular_hexagon_points(10**1000)

    def test_frame_is_external_and_rotation_is_composed(self):
        job = copy.deepcopy(self.job)
        axis = [0.0, 1.0, 0.0]
        radial_x = [1.0, 0.0, 0.0]
        job['placement'].update(axis=axis, radial_x=radial_x)
        p = parameters(job)
        self.assertEqual(axis, p['axis'])
        self.assertEqual(radial_x, p['radial_x'])
        self.assertAlmostEqual(90.0, p['rotation_degrees']['Y_axis_tilt'])
        self.assertEqual('PASS', verify(self._features(job), job)['result'])
        diagonal = copy.deepcopy(self.job)
        diagonal['placement'].update(axis=[0.0, 0.6, 0.8],
                                     radial_x=[1.0, 0.0, 0.0])
        self.assertEqual('PASS', verify(self._features(diagonal), diagonal)['result'])

    def test_build_uses_existing_extrusion_and_metadata_api(self):
        geometry = Mock()
        geometry.extrude.return_value = 'body-handle'
        with patch('hexagonal_reference.geometry', return_value=geometry):
            result = build_hexagonal_reference(object(), self.job)
        self.assertEqual('body-handle', result)
        args = geometry.extrude.call_args.args
        self.assertEqual('Synthetic hex hexagonal prism', args[0])
        self.assertEqual(6, len(args[1]))
        self.assertEqual((0.0, 12.0), args[2:4])
        geometry.metadata.assert_called_once()

    def test_optional_bore_uses_source_feature_and_boolean_subtraction(self):
        job = copy.deepcopy(self.job)
        job['dimension_features']['bore_diameter'] = 'bore'
        job['features'].append({'name': 'bore', 'value': 12.0, 'unit': 'mm',
                                'required': True, 'source': str(self.source),
                                'source_sha256': self.digest,
                                'source_location': 'synthetic fixture',
                                'evidence_status': 'synthetic test'})
        job['construction'] = {'cutter_overrun_mm': 0.2}
        geometry = Mock()
        geometry.extrude.return_value = 'prism-handle'
        geometry.cylinder.return_value = 'bore-handle'
        geometry.subtract.return_value = 'bored-handle'
        with patch('hexagonal_reference.geometry', return_value=geometry):
            result = build_hexagonal_reference(object(), job)
        self.assertEqual('bored-handle', result)
        self.assertEqual(12.4, geometry.cylinder.call_args.args[3])
        geometry.subtract.assert_called_once_with(
            'Synthetic hex bored hexagonal solid', 'prism-handle', ['bore-handle'])

    def test_invalid_frame_or_unbound_bore_fails_before_geometry(self):
        cases = []
        bad_frame = copy.deepcopy(self.job)
        bad_frame['placement']['axis'] = [0.0, 0.0, 2.0]
        cases.append(bad_frame)
        nonorthogonal = copy.deepcopy(self.job)
        nonorthogonal['placement']['radial_x'] = [0.1, 0.0, 0.99]
        cases.append(nonorthogonal)
        malformed_bore = copy.deepcopy(self.job)
        malformed_bore['dimension_features']['bore_diameter'] = 'missing-bore'
        cases.append(malformed_bore)
        collapsed_bore = copy.deepcopy(self.job)
        collapsed_bore['dimension_features']['bore_diameter'] = 'tiny-bore'
        collapsed_bore['features'].append({'name': 'tiny-bore', 'value': 5e-324,
                                           'unit': 'mm', 'required': True,
                                           'source': str(self.source),
                                           'source_sha256': self.digest,
                                           'source_location': 'synthetic fixture',
                                           'evidence_status': 'synthetic test'})
        collapsed_bore['construction'] = {'cutter_overrun_mm': 0.2}
        cases.append(collapsed_bore)
        for job in cases:
            factory = Mock()
            with patch('hexagonal_reference.geometry', factory):
                with self.assertRaises(ValueError):
                    build_hexagonal_reference(object(), job)
            factory.assert_not_called()

    def test_native_plane_station_and_closed_body_checks(self):
        self.assertEqual('PASS', verify(self._features(), self.job)['result'])
        altered = self._features()
        altered['planes'][0]['origin'][1] += 0.1
        self.assertEqual('FAIL', verify(altered, self.job)['result'])
        altered = self._features()
        altered['topology']['reciprocal_closed_partners'] = False
        self.assertEqual('FAIL', verify(altered, self.job)['result'])

    def test_optional_bore_requires_one_analytic_coaxial_cylinder(self):
        job = copy.deepcopy(self.job)
        job['dimension_features']['bore_diameter'] = 'bore'
        job['features'].append({'name': 'bore', 'value': 12.0, 'unit': 'mm',
                                'required': True, 'source': str(self.source),
                                'source_sha256': self.digest,
                                'source_location': 'synthetic fixture',
                                'evidence_status': 'synthetic test'})
        job['construction'] = {'cutter_overrun_mm': 0.2}
        good = self._features(job, bore=True)
        self.assertEqual('PASS', verify(good, job)['result'])
        good['cylinders'][0]['origin'] = [5.0, -3.0, 2.0]
        self.assertEqual('FAIL', verify(good, job)['result'])

    def test_extra_hole_and_closed_bore_end_are_rejected(self):
        extra = self._features()
        extra['cylinders'] = [{'axis': [0.0, 0.0, 1.0], 'origin': [4.0, -3.0, 2.0],
                               'radius': 2.0}]
        self.assertEqual('FAIL', verify(extra, self.job)['result'])

        job = copy.deepcopy(self.job)
        job['dimension_features']['bore_diameter'] = 'bore'
        job['features'].append({'name': 'bore', 'value': 12.0, 'unit': 'mm',
                                'required': True, 'source': str(self.source),
                                'source_sha256': self.digest,
                                'source_location': 'synthetic fixture',
                                'evidence_status': 'synthetic test'})
        job['construction'] = {'cutter_overrun_mm': 0.2}
        closed_end = self._features(job, bore=True)
        closed_end['planar_face_loops'][1]['loops'] = [{'edge_count': 6}]
        self.assertEqual('FAIL', verify(closed_end, job)['result'])

    def test_duplicate_coplanar_surface_patches_are_deduplicated(self):
        features = self._features()
        features['planes'].append(copy.deepcopy(features['planes'][0]))
        self.assertEqual('PASS', verify(features, self.job)['result'])

    def test_metadata_is_checked_against_native_entity_strings(self):
        job = copy.deepcopy(self.job)
        lines = parameters(job)['metadata']
        chunks = [line[i:i + 100] for line in lines for i in range(0, len(line), 100)]
        record = {'handle': 'H1', 'properties': {'common': {'extended_data': {
            'records': [{'application_name': 'CADTOOLS_SOURCE',
                         'values': [{'String': value} for value in chunks]}]}}}}
        self.assertEqual('PASS', verify_metadata(record, 'H1', job)['result'])
        record['handle'] = 'H2'
        with self.assertRaisesRegex(ValueError, 'handle'):
            verify_metadata(record, 'H1', job)

    def test_metadata_uses_portable_source_locator_not_runtime_path(self):
        lines = parameters(self.job)['metadata']
        self.assertTrue(any('${SOURCE_ROOT}/source.txt' in line for line in lines))
        self.assertFalse(any(str(self.source) in line for line in lines))
        self.assertTrue(any(self.digest in line for line in lines))

    def test_inspection_binds_record_to_stable_document_geometry_epoch(self):
        state = {'document_id': 'DOC-1', 'revision': 12, 'geometry_revision': 8}
        record = {'handle': 'H1', 'type': 'Solid3D',
                  'properties': {'acis_data': {'sab_data': b'fixture'}}}
        response = {'document_id': 'DOC-1', 'revision': 12,
                    'geometry_revision': 8, 'records': [record]}
        client = Mock(document_id='DOC-1')
        client.read.side_effect = [state, response, state]
        with patch('native_acis.sab_features', return_value=self._features()), \
                patch('hexagonal_reference.compare_source_metadata',
                      return_value={'result': 'PASS'}):
            _, result = inspect(client, {'body': 'H1'}, self.job)
        self.assertEqual('PASS', result['result'])
        self.assertEqual(12, result['revision'])
        self.assertEqual(8, result['geometry_revision'])

        changed = dict(response, geometry_revision=9)
        client.read.side_effect = [state, changed]
        with self.assertRaisesRegex(ValueError, 'geometry epoch'):
            with patch('native_acis.sab_features') as reader:
                inspect(client, {'body': 'H1'}, self.job)
                reader.assert_not_called()


if __name__ == '__main__':
    unittest.main()
