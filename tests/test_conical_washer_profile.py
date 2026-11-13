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

from conical_washer_profile import (build_conical_washer, inspect, parameters,
                                     verify, verify_metadata)


class ConicalWasherProfileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        source = Path(self.tmp.name) / 'source-dimensions.txt'
        source.write_text('synthetic source fixture for isolated tests\n', encoding='utf-8')
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        bore, outside, thickness, height, _, _ = self._synthetic_dimensions(8.0, 3.0, 0.4, 12.0)
        self.job = {
            'job_id': 'synthetic-conical-washer-job',
            'part_id': 'TEST-WASHER',
            'part_name': 'Synthetic conical washer',
            'configuration': 'nominal option A',
            'representation': 'single nominal straight-strip conical washer',
            'geometry_role': 'reference_conical_washer',
            'geometry_name': 'Synthetic washer',
            'metadata_application': 'CADTOOLS_SOURCE',
            'metadata_request_label': 'synthetic washer metadata write',
            'units': 'mm',
            'frame': 'local washer axis at +Z',
            'local_frame': 'radial X, axis Z, free profile axial extent from z_origin',
            'center': [2.0, -3.0],
            'z_origin': 4.0,
            'angle_interval_degrees': [0.0, 45.0],
            'dimension_features': {
                'inside_diameter': 'bore',
                'outside_diameter': 'outside',
                'normal_thickness': 'thickness',
                'free_height': 'height',
            },
            'features': [
                {'name': name, 'value': value, 'unit': 'mm', 'required': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic source fixture table',
                 'evidence_status': 'synthetic test input'}
                for name, value in [('bore', bore), ('outside', outside),
                                    ('thickness', thickness), ('height', height)]
            ],
            'readback_tolerance': 1e-7,
            'readback_angle_tolerance_rad': 1e-7,
        }

    @staticmethod
    def _synthetic_dimensions(inside_diameter, strip_length, thickness, angle_degrees):
        alpha = math.radians(angle_degrees)
        radial_span = strip_length * math.cos(alpha) + thickness * math.sin(alpha)
        height = strip_length * math.sin(alpha) + thickness * math.cos(alpha)
        return (inside_diameter, inside_diameter + 2.0 * radial_span,
                thickness, height, strip_length, angle_degrees)

    def _features(self):
        p = parameters(self.job)
        points = []
        for radius, height in p['profile']:
            points.append([2.0 + radius, -3.0, 4.0 + height])
        alpha = p['inclination_radians']
        return {
            'points': points,
            'cones': [
                {'axis': [0, 0, 1], 'sin_angle': math.sin(a), 'cos_angle': math.cos(a),
                 'origin': [0, 0, 0], 'radius': 1.0}
                for a in [alpha, alpha, math.pi/2-alpha, math.pi/2-alpha]
            ],
            'planes': [], 'cylinders': [], 'spheres': [], 'tori': [], 'ellipses': [],
            'topology': {'bodies': 1, 'lumps': 1, 'shells': 1,
                         'reciprocal_closed_partners': True},
        }

    def test_profile_solves_source_projections_and_strip_invariants(self):
        p = parameters(self.job)
        self.assertAlmostEqual(3.0, p['strip_length'], places=10)
        self.assertAlmostEqual(12.0, p['inclination_degrees'], places=10)
        points = p['profile']
        self.assertAlmostEqual(8.0 / 2, min(row[0] for row in points), places=12)
        outside = self._synthetic_dimensions(8.0, 3.0, 0.4, 12.0)[1]
        self.assertAlmostEqual(outside / 2, max(row[0] for row in points), places=12)
        self.assertAlmostEqual(0.0, min(row[1] for row in points), places=12)
        expected_height = self._synthetic_dimensions(8.0, 3.0, 0.4, 12.0)[3]
        self.assertAlmostEqual(expected_height, max(row[1] for row in points), places=12)
        edges = [[b[0]-a[0], b[1]-a[1]]
                 for a, b in zip(points, points[1:] + points[:1])]
        self.assertAlmostEqual(0.4, math.hypot(*edges[1]), places=12)
        self.assertAlmostEqual(0.4, math.hypot(*edges[3]), places=12)
        self.assertAlmostEqual(0.0, edges[0][0]*edges[1][0] + edges[0][1]*edges[1][1], places=12)
        area2 = sum(a[0]*b[1] - b[0]*a[1]
                    for a, b in zip(points, points[1:] + points[:1]))
        self.assertAlmostEqual(p['strip_length']*0.4, abs(area2)/2, places=12)
        p0,p1,p2,p3=points
        self.assertAlmostEqual(p1[0]-p0[0], p2[0]-p3[0], places=12)
        self.assertAlmostEqual(p1[1]-p0[1], p2[1]-p3[1], places=12)

    def test_portable_source_paths_resolve_from_caller_roots_without_mutating_job(self):
        source = Path(self.tmp.name) / 'source-dimensions.txt'
        job = copy.deepcopy(self.job)
        for feature in job['features']:
            feature['source'] = '${PROJECT_ROOT}/source-dimensions.txt'
        original_locators = [feature['source'] for feature in job['features']]
        result = parameters(job, {'PROJECT_ROOT': self.tmp.name})
        self.assertAlmostEqual(3.0, result['strip_length'], places=10)
        self.assertEqual(original_locators, [feature['source'] for feature in job['features']])
        with self.assertRaisesRegex(ValueError, 'cannot be resolved'):
            parameters(job, {})

    def test_four_synthetic_dimension_sets_solve_on_shallow_branch(self):
        synthetic_sets = [
            (8.0, 3.0, 0.4, 12.0),
            (4.0, 1.8, 0.25, 8.0),
            (20.0, 6.0, 1.0, 18.0),
            (2.0, 0.6, 0.08, 25.0),
        ]
        for index, inputs in enumerate(synthetic_sets):
            with self.subTest(synthetic_case=index):
                values = self._synthetic_dimensions(*inputs)
                job = copy.deepcopy(self.job)
                job['configuration'] = f'synthetic case {index}'
                for feature, value in zip(job['features'], values[:4]):
                    feature['value'] = value
                result = parameters(job)
                self.assertAlmostEqual(inputs[1], result['strip_length'], places=9)
                self.assertAlmostEqual(inputs[3], result['inclination_degrees'], places=9)

    def test_build_uses_existing_revolve_and_places_metadata(self):
        geometry = Mock()
        geometry.revolve_z.return_value = 'washer-solid'
        with patch('conical_washer_profile.geometry', return_value=geometry):
            handle = build_conical_washer(object(), self.job)
        self.assertEqual('washer-solid', handle)
        call = geometry.revolve_z.call_args
        self.assertEqual('Synthetic washer closed conical section', call.args[0])
        self.assertEqual(parameters(self.job)['profile'], call.args[1])
        geometry.move.assert_called_once_with('Synthetic washer local axis placement',
                                             ['washer-solid'], [2.0, -3.0, 4.0])
        self.assertEqual('synthetic washer metadata write', geometry.metadata.call_args.args[0])

    def test_invalid_inputs_reject_before_geometry_factory(self):
        cases = [
            ('bore exceeds outside', lambda j: j['features'][1].update(value=7.0)),
            ('zero thickness', lambda j: j['features'][2].update(value=0.0)),
            ('height not greater than thickness', lambda j: j['features'][3].update(value=0.4)),
            ('no real shallow solution', lambda j: (j['features'][0].update(value=2.0),
                                                     j['features'][1].update(value=4.0),
                                                     j['features'][2].update(value=0.2),
                                                     j['features'][3].update(value=10.0))),
            ('strip length not greater than thickness', lambda j: (
                j['features'][0].update(value=1.0),
                j['features'][1].update(value=3.052),
                j['features'][2].update(value=1.0),
                j['features'][3].update(value=1.15))),
            ('unsupported angle branch', lambda j: j.update(angle_interval_degrees=[0.0, 60.0])),
            ('no root in declared interval', lambda j: j.update(angle_interval_degrees=[0.0, 5.0])),
            ('collapsed placement', lambda j: (j.update(z_origin=1e300),
                                               j['features'][3].update(value=1.0))),
            ('nonfinite axis centre', lambda j: j.update(center=[float('nan'), 0.0])),
            ('unrepresentably large centre', lambda j: j.update(center=[10**10000, 0.0])),
            ('unrepresentably large dimension', lambda j: j['features'][0].update(value=10**10000)),
            ('nonfinite linear tolerance', lambda j: j.update(readback_tolerance=float('inf'))),
            ('metadata application mismatch', lambda j: j.update(metadata_application='WRONG_APP')),
            ('unbound source digest', lambda j: j['features'][0].update(source_sha256='0'*64)),
        ]
        for name, mutate in cases:
            with self.subTest(name=name):
                job = copy.deepcopy(self.job)
                mutate(job)
                factory = Mock()
                with patch('conical_washer_profile.geometry', factory):
                    with self.assertRaises(ValueError):
                        build_conical_washer(object(), job)
                factory.assert_not_called()

    def test_profile_rejects_ambiguous_root_set(self):
        # A duplicate physical root indicates an indeterminate root-isolation
        # result and must fail closed rather than choose or silently deduplicate.
        root = math.tan(math.radians(9.964284250388442))
        with patch('conical_washer_profile._poly_roots_in_interval', return_value=[root, root]):
            with self.assertRaisesRegex(ValueError, 'exactly one physical strip solution'):
                parameters(self.job)

    def test_native_feature_checks_require_dimensions_angles_and_closed_body(self):
        result = verify(self._features(), self.job)
        self.assertEqual('PASS', result['result'])
        duplicate_seam = self._features()
        duplicate_seam['points'] += copy.deepcopy(duplicate_seam['points'])
        self.assertEqual('PASS', verify(duplicate_seam, self.job)['result'])
        extra_corner = self._features()
        extra_corner['points'].append([2.0 + 3.2, -3.0, 4.0 + 0.33])
        self.assertEqual('FAIL', verify(extra_corner, self.job)['result'])
        wrong = self._features()
        wrong['points'][0][0] += 0.02
        self.assertEqual('FAIL', verify(wrong, self.job)['result'])
        wrong = self._features()
        wrong['cones'][0]['sin_angle'] = math.sin(0.3)
        wrong['cones'][0]['cos_angle'] = math.cos(0.3)
        self.assertEqual('FAIL', verify(wrong, self.job)['result'])
        wrong = self._features()
        wrong['planes'] = [{'normal': [0,0,1]}]
        self.assertEqual('FAIL', verify(wrong, self.job)['result'])
        wrong = self._features()
        wrong['topology']['reciprocal_closed_partners'] = False
        self.assertEqual('FAIL', verify(wrong, self.job)['result'])

    def test_metadata_check_uses_fixed_application_and_handle(self):
        lines = parameters(self.job)['metadata']
        chunks = [line[i:i+100] for line in lines for i in range(0,len(line),100)]
        record = {'handle':'A1','properties':{'common':{'extended_data':{'records':[
            {'application_name':'CADTOOLS_SOURCE','values':[{'String':v} for v in chunks]}]}}}}
        self.assertEqual('PASS', verify_metadata(record,'A1',self.job)['result'])
        with self.assertRaisesRegex(ValueError,'handle'):
            verify_metadata(record,'B2',self.job)
        record['properties']['common']['extended_data']['records'][0]['values'][0] = {'String':'altered'}
        self.assertEqual('FAIL', verify_metadata(record,'A1',self.job)['result'])

    def test_installed_geometry_adapter_uses_existing_metadata_application(self):
        Geometry = importlib.import_module('cadtools.geometry').Geometry
        client = Mock()
        Geometry(client).metadata('request label', ['A1'], ['source line'])
        client.mutate.assert_called_once_with('request label','xdata_set',handles=['A1'],
            app='CADTOOLS_SOURCE',data=[{'code':1000,'value':'source line'}])

    def test_reopened_inspection_binds_record_and_revisions(self):
        lines = parameters(self.job)['metadata']
        chunks = [line[i:i+100] for line in lines for i in range(0,len(line),100)]
        record = {'handle':'A1','type':'Solid3D',
            'properties':{'acis_data':{'sab_data':b'synthetic sab'},
                'common':{'extended_data':{'records':[{'application_name':'CADTOOLS_SOURCE',
                    'values':[{'String':v} for v in chunks]}]}}}}
        class Client:
            document_id=17
            def __init__(self, record_revision=4):
                self.states=[{'document_id':17,'geometry_revision':4,'revision':9},
                             {'document_id':17,'geometry_revision':4,'revision':9}]
                self.record_revision=record_revision
            def read(self, operation, **kwargs):
                if operation=='state':return self.states.pop(0)
                if operation=='records':return {'document_id':17,'geometry_revision':self.record_revision,'records':[record]}
                raise AssertionError(operation)
        with patch('native_acis.sab_features',return_value=self._features()) as reader:
            _,result,found=inspect(Client(),'A1',self.job)
        self.assertEqual('PASS',result['result'])
        self.assertIs(record,found)
        reader.assert_called_once_with(b'synthetic sab',allow_rigid=True,
                                       allow_cones=True,include_loops=False)
        with patch('native_acis.sab_features',return_value=self._features()):
            with self.assertRaisesRegex(ValueError,'geometry_revision differs'):
                inspect(Client(record_revision=5),'A1',self.job)


if __name__ == '__main__':
    unittest.main()
