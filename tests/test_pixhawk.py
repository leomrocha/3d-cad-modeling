"""Source-bound Pixhawk 6C envelope and mounting-feature checks."""
import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from pixhawk import build_envelope, parameters, verify


FEATURE_VALUES = {
    'case length X': 84.8,
    'case width Y': 44.0,
    'case thickness Z': 12.4,
    'mount hole X pitch': 60.0,
    'mount hole Y pitch': 32.0,
    'mount thread nominal designation': 'M2',
    'mount thread depth': 6.0,
}


def plane(x, y, z, normal=(0, 0, -1)):
    return {'origin': [x, y, z], 'normal': list(normal)}


def cylinder(x, y, z):
    return {'origin': [x, y, z], 'axis': [0, 0, 1], 'radius': 1.0}


def source_job(values=None):
    values = values or FEATURE_VALUES
    return {
        'part_id': 'C052',
        'part_name': 'Holybro Pixhawk 6C controller case reference',
        'units': 'mm',
        'features': [{'name': key, 'value': value} for key, value in values.items()],
        'construction': {'construction_overrun_mm': 0.01},
    }


def native_case():
    x, y, z = 42.4, 22.0, 12.4
    points = [[sx * x, sy * y, sz * z]
              for sx in (-1, 1) for sy in (-1, 1) for sz in (0, 1)]
    centres = [(sx * 30.0, sy * 16.0) for sx in (-1, 1) for sy in (-1, 1)]
    return {
        'points': points,
        'cylinders': [cylinder(a, b, 3.0) for a, b in centres],
        'planes': [plane(a, b, 6.0) for a, b in centres],
    }


class PixhawkChecks(unittest.TestCase):
    def setUp(self):
        self.guard = patch('pixhawk.require_ready')
        self.guard.start()
        self.addCleanup(self.guard.stop)
        self.job = source_job()
        self.features = {'case': native_case()}

    def test_source_dimensioned_case_envelope_and_mount_pattern_pass(self):
        self.assertEqual(verify(self.features, self.job)['result'], 'PASS')

    def test_changed_case_width_fails(self):
        case = copy.deepcopy(self.features)
        for point in case['case']['points']:
            point[1] *= 0.99
        self.assertEqual(verify(case, self.job)['result'], 'FAIL')

    def test_missing_mount_thread_axis_fails(self):
        case = copy.deepcopy(self.features)
        case['case']['cylinders'].pop()
        self.assertEqual(verify(case, self.job)['result'], 'FAIL')

    def test_wrong_blind_thread_depth_fails(self):
        case = copy.deepcopy(self.features)
        case['case']['planes'][0]['origin'][2] = 5.8
        self.assertEqual(verify(case, self.job)['result'], 'FAIL')

    def test_wrong_mount_pitch_fails(self):
        case = copy.deepcopy(self.features)
        case['case']['cylinders'][0]['origin'][0] = -29.0
        self.assertEqual(verify(case, self.job)['result'], 'FAIL')

    def test_invalid_overrun_is_rejected_before_native_geometry_adapter(self):
        job = copy.deepcopy(self.job)
        job['construction']['construction_overrun_mm'] = 0
        with patch('pixhawk.geometry') as geometry_factory:
            with self.assertRaises(ValueError):
                build_envelope(object(), job)
        geometry_factory.assert_not_called()

    def test_mount_pattern_outside_case_is_rejected_before_build(self):
        job = copy.deepcopy(self.job)
        next(f for f in job['features'] if f['name'] == 'mount hole X pitch')['value'] = 84.0
        with patch('pixhawk.geometry') as geometry_factory:
            with self.assertRaises(ValueError):
                build_envelope(object(), job)
        geometry_factory.assert_not_called()

    def test_duplicate_required_source_feature_is_rejected(self):
        job = copy.deepcopy(self.job)
        job['features'].append({'name': 'case length X', 'value': 90.0})
        with self.assertRaises(ValueError):
            parameters(job)

    def test_wrong_identity_units_and_thread_callout_are_rejected(self):
        for field, value in [('part_id', 'C055'), ('units', 'inch')]:
            job = copy.deepcopy(self.job)
            job[field] = value
            with self.assertRaises(ValueError):
                parameters(job)
        job = copy.deepcopy(self.job)
        job['features'][-2]['value'] = 'M2.5'
        with self.assertRaises(ValueError):
            parameters(job)


if __name__ == '__main__':
    unittest.main()
