import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from profile_reference import (  # noqa: E402
    build_profile_reference, inspect, parameters, validate_profile, verify,
)


class ProfileReferenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        source = Path(self.tmp.name) / 'source.txt'
        source.write_text('synthetic source profile and depth values\n')
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        self.source = str(source)
        self.digest = digest
        self.job = {
            'job_id': 'synthetic-profile-reference-job',
            'part_id': 'SYNTHETIC',
            'part_name': 'Synthetic traced profile',
            'representation': 'synthetic source-traced packaging reference',
            'geometry_role': 'source_traced_projected_profile_reference',
            'geometry_name': 'Synthetic profile extrusion',
            'units': 'mm',
            'frame': 'local profile and extrusion frame',
            'local_frame': 'XY profile at supplied origin, positive local Z extrusion',
            'geometry_scope': 'synthetic polygon trace extruded to source depth',
            'origin': [10, 20, 30],
            'profile_points_2d': [[0, 0], [2, 0], [2, 1], [0, 1]],
            'profile_extent_features': {'x': 'source width', 'y': 'source height'},
            'profile_extent_bounds_mm': {'x': [1.99, 2.01], 'y': [0.99, 1.01]},
            'profile_extent_basis': {'x': 'synthetic source width interval',
                                     'y': 'synthetic source height interval'},
            'depth_mm': 2,
            'depth_feature_name': 'depth',
            'readback_tolerance_mm': 1e-7,
            'source_files': [{'path': str(source), 'sha256': digest}],
            'features': [
                {'name': 'profile trace', 'value': 'four synthetic vertices',
                 'unit': 'point record', 'required': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic test fixture',
                 'evidence_status': 'synthetic test input'},
                {'name': 'source width', 'value': 2, 'unit': 'mm',
                 'required': True, 'source_dimension_expectation': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic test fixture width',
                 'evidence_status': 'synthetic test input'},
                {'name': 'source height', 'value': 1, 'unit': 'mm',
                 'required': True, 'source_dimension_expectation': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic test fixture height',
                 'evidence_status': 'synthetic test input'},
                {'name': 'depth', 'value': 2, 'unit': 'mm', 'required': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic test fixture depth',
                 'evidence_status': 'synthetic test input'},
            ],
        }

    def test_build_uses_existing_guarded_geometry_extrude_and_source_metadata(self):
        fake_geometry = Mock()
        fake_geometry.extrude.return_value = 'solid-handle'
        with patch('profile_reference.geometry', return_value=fake_geometry):
            result = build_profile_reference(object(), self.job)
        self.assertEqual('solid-handle', result)
        fake_geometry.extrude.assert_called_once_with(
            'Synthetic profile extrusion',
            [[10.0, 20.0], [12.0, 20.0], [12.0, 21.0], [10.0, 21.0]], 30.0, 2.0)
        metadata = fake_geometry.metadata.call_args.args[2]
        self.assertIn('Geometry role: source_traced_projected_profile_reference', metadata)
        self.assertIn('Geometry scope: synthetic polygon trace extruded to source depth', metadata)
        self.assertIn('Source file: ' + self.source + ' SHA-256 ' + self.digest, metadata)

    def test_parameters_preserve_source_dimensions_separately_from_profile_bounds(self):
        result = verify({'points': self._box_points()}, self.job)
        self.assertEqual('PASS', result['result'])
        self.assertEqual([[10, 12], [20, 21], [30, 32]],
                         result['output_bounds_expected_from_profile_and_depth'])
        self.assertEqual([{'name': 'source width', 'value': 2, 'unit': 'mm',
                           'evidence_status': 'synthetic test input',
                           'source_location': 'synthetic test fixture width'},
                          {'name': 'source height', 'value': 1, 'unit': 'mm',
                           'evidence_status': 'synthetic test input',
                           'source_location': 'synthetic test fixture height'}],
                         result['source_dimension_expectations'])
        self.assertEqual(['PASS', 'PASS'], [row['result'] for row in result['source_bound_profile_extent_checks']])

    def test_outline_point_set_passes_and_changed_vertices_fail(self):
        points = self._box_points()
        self.assertEqual('PASS', verify({'points': points}, self.job)['result'])
        changed = [point[:] for point in points]
        changed[-1][0] += 0.01
        result = verify({'points': changed}, self.job)
        self.assertEqual('FAIL', result['result'])
        self.assertEqual('FAIL', result['checks'][1]['result'])

    def test_duplicate_native_points_are_deduplicated(self):
        points = self._box_points()
        points.append(points[0][:])
        self.assertEqual('PASS', verify({'points': points}, self.job)['result'])

    def test_invalid_polygons_are_rejected(self):
        invalid = [
            ([[0, 0], [1, 0]], 'at least three'),
            ([[0, 0], [1, 0], [1, 0]], 'duplicate'),
            ([[0, 0], [1, 0], [1, 1], [0, 0]], 'duplicate'),
            ([[0, 0], [2, 0], [1, 1], [2, 0], [0, 2]], 'repeat or retrace'),
            ([[0, 0], [2, 2], [0, 2], [2, 0]], 'nonzero area|cross, touch or retrace'),
            ([[0, 0], [2, 0], [1, 0], [1, 1]], 'cross, touch or retrace'),
            ([[0, 0], [1, 1], [2, 2]], 'nonzero area'),
            ([[0, 0], [True, 0], [0, 1]], 'finite number'),
            ([[0, 0], [float('nan'), 1], [1, 0]], 'finite number'),
        ]
        for polygon, message in invalid:
            with self.subTest(polygon=polygon):
                with self.assertRaisesRegex(ValueError, message):
                    validate_profile(polygon)

    def test_all_invalid_input_is_rejected_before_geometry_factory(self):
        mutations = [
            ('units', 'inch'),
            ('geometry_role', ''),
            ('local_frame', ''),
            ('profile_points_2d', [[0, 0], [1, 0], [0, 1], [0, 0]]),
            ('origin', [True, 0, 0]),
            ('depth_mm', True),
            ('depth_mm', 0),
            ('depth_mm', -1),
            ('depth_mm', float('inf')),
            ('depth_mm', float('nan')),
            ('readback_tolerance_mm', 0),
            ('source_files', [{'path': self.source, 'sha256': 'wrong'}]),
            ('geometry_role', 'detailed_body'),
            ('profile_extent_bounds_mm', {'x': [5, 6], 'y': [5, 6]}),
            ('profile_extent_bounds_mm', {'x': [2.1, 2.2], 'y': [0.99, 1.01]}),
            ('profile_extent_features', {'x': 'source width', 'y': 'source width'}),
        ]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                job = dict(self.job)
                job[key] = value
                factory = Mock()
                with patch('profile_reference.geometry', factory):
                    with self.assertRaises(ValueError):
                        build_profile_reference(object(), job)
                factory.assert_not_called()

    def test_wrong_scale_profile_is_rejected_against_source_extent_before_geometry_factory(self):
        job = dict(self.job)
        job['profile_points_2d'] = [[0, 0], [91, 0], [91, 1], [0, 1]]
        factory = Mock()
        with patch('profile_reference.geometry', factory):
            with self.assertRaisesRegex(ValueError, 'outside the source-bound interval'):
                build_profile_reference(object(), job)
        factory.assert_not_called()

    def test_depth_and_source_files_must_be_required_pinned_inputs(self):
        job = dict(self.job)
        job['features'] = [dict(row) for row in self.job['features']]
        job['features'][-1]['required'] = False
        with self.assertRaisesRegex(ValueError, 'depth_feature_name must identify a required source feature'):
            parameters(job)
        job = dict(self.job)
        job['source_files'] = [{'path': '/not-pinned', 'sha256': 'bad'}]
        with self.assertRaisesRegex(ValueError, 'pinned by a required source feature'):
            parameters(job)

    def test_boolean_depth_source_is_not_accepted_as_numeric_depth(self):
        job = dict(self.job)
        job['depth_mm'] = 1
        job['features'] = [dict(row) for row in self.job['features']]
        job['features'][-1]['value'] = True
        factory = Mock()
        with patch('profile_reference.geometry', factory):
            with self.assertRaises(ValueError):
                build_profile_reference(object(), job)
        factory.assert_not_called()

    def test_nonpositive_source_extent_value_is_rejected_prewrite(self):
        job = dict(self.job)
        job['features'] = [dict(row) for row in self.job['features']]
        job['features'][1]['value'] = 0
        factory = Mock()
        with patch('profile_reference.geometry', factory):
            with self.assertRaisesRegex(ValueError, 'must be positive'):
                build_profile_reference(object(), job)
        factory.assert_not_called()

    def test_positive_depth_lost_to_large_z_origin_is_rejected_prewrite(self):
        job = dict(self.job)
        job['origin'] = [10, 20, 1e308]
        factory = Mock()
        with patch('profile_reference.geometry', factory):
            with self.assertRaisesRegex(ValueError, 'depth is lost'):
                build_profile_reference(object(), job)
        factory.assert_not_called()

    def test_translated_polygon_collapse_is_rejected_prewrite(self):
        job = dict(self.job)
        job['origin'] = [1e17, 20, 30]
        factory = Mock()
        with patch('profile_reference.geometry', factory):
            with self.assertRaisesRegex(ValueError, 'duplicate'):
                build_profile_reference(object(), job)
        factory.assert_not_called()

    def test_coordinate_and_depth_arithmetic_overflow_is_rejected_prewrite(self):
        for origin, profile, depth in (
                ([1e308, 0, 0], [[0, 0], [1e308, 0], [0, 1]], 2),
                ([0, 0, 1e308], [[0, 0], [1, 0], [0, 1]], 1e308)):
            job = dict(self.job)
            job['origin'], job['profile_points_2d'], job['depth_mm'] = origin, profile, depth
            job['features'] = [dict(feature) for feature in self.job['features']]
            job['features'][2]['value'] = depth
            factory = Mock()
            with patch('profile_reference.geometry', factory):
                with self.assertRaisesRegex(ValueError, 'overflows'):
                    build_profile_reference(object(), job)
            factory.assert_not_called()

    def test_huge_integer_is_reported_as_value_error(self):
        with self.assertRaisesRegex(ValueError, 'finite number'):
            validate_profile([[0, 0], [10**1000, 0], [0, 1]])

    def _box_points(self):
        return [[x, y, z] for x, y in ((10, 20), (12, 20), (12, 21), (10, 21))
                for z in (30, 32)]

    def _sat_record(self, handle='A1', entity_type='Solid3D'):
        sat = '\n'.join('point -1 -1 -1 ' + ' '.join(map(str, point))
                        for point in self._box_points())
        return {'handle': handle, 'type': entity_type,
                'properties': {'acis_data': {'sat_data': sat, 'sab_data': []}}}

    class InspectClient:
        document_id = 71

        def __init__(self, states, record):
            self.states = list(states)
            self.record = record

        def read(self, operation, **kwargs):
            if operation == 'state':
                return self.states.pop(0)
            if operation == 'records':
                return {'records': [self.record]}
            raise AssertionError('unexpected read operation: ' + operation)

    def _state(self, geometry_revision=17, revision=4):
        return {'document_id': 71, 'geometry_revision': geometry_revision,
                'revision': revision}

    def test_inspect_binds_native_document_handle_and_stable_revisions(self):
        client = self.InspectClient([self._state(), self._state()], self._sat_record())
        response, result = inspect(client, {'solid': 'A1'}, self.job)
        self.assertEqual('PASS', result['result'])
        self.assertEqual(71, result['document_id'])
        self.assertEqual(4, result['document_revision'])
        self.assertEqual(17, result['geometry_revision'])
        self.assertEqual('A1', result['handle'])

    def test_inspect_rejects_changed_geometry_revision_and_wrong_handle(self):
        client = self.InspectClient([self._state(17), self._state(18)], self._sat_record())
        with self.assertRaisesRegex(ValueError, 'Geometry revision changed'):
            inspect(client, {'solid': 'A1'}, self.job)
        client = self.InspectClient([self._state()], self._sat_record(handle='B2'))
        with self.assertRaisesRegex(ValueError, 'handle differs'):
            inspect(client, {'solid': 'A1'}, self.job)

    def test_inspect_rejects_non_solid_and_mismatched_record_revision(self):
        client = self.InspectClient([self._state()], self._sat_record(entity_type='Polyline'))
        with self.assertRaisesRegex(ValueError, 'type Solid3D'):
            inspect(client, {'solid': 'A1'}, self.job)
        record = self._sat_record()
        record['revision'] = 8
        client = self.InspectClient([self._state()], record)
        with self.assertRaisesRegex(ValueError, 'record revision'):
            inspect(client, {'solid': 'A1'}, self.job)


if __name__ == '__main__':
    unittest.main()
