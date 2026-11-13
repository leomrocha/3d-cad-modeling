import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from envelope_reference import build_envelope, verify


class EnvelopeReferenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        source = Path(self.tmp.name) / 'source.txt'
        source.write_text('synthetic dimensions used by this isolated test\n')
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        self.job = {
            'job_id': 'synthetic-reference-test',
            'part_id': 'TEST-ONLY',
            'part_name': 'synthetic reference object',
            'representation': 'synthetic axis-aligned reference envelope',
            'geometry_role': 'reference_envelope',
            'geometry_name': 'synthetic source envelope',
            'units': 'mm',
            'frame': 'local envelope coordinates',
            'local_frame': 'lower-corner origin; +X, +Y, +Z follow supplied dimensions',
            'origin': [1, 2, 3],
            'dimension_features': {'x': 'width', 'y': 'height', 'z': 'depth'},
            'features': [
                {'name': 'width', 'value': 10, 'unit': 'mm', 'required': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic test fixture',
                 'evidence_status': 'synthetic test input'},
                {'name': 'height', 'value': 5, 'unit': 'mm', 'required': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic test fixture',
                 'evidence_status': 'synthetic test input'},
                {'name': 'depth', 'value': 3, 'unit': 'mm', 'required': True,
                 'source': str(source), 'source_sha256': digest,
                 'source_location': 'synthetic test fixture',
                 'evidence_status': 'synthetic test input'},
            ],
        }

    def test_build_sends_parameterized_profile_and_extrusion(self):
        fake_geometry = Mock()
        fake_geometry.extrude.return_value = 'solid-handle'
        with patch('envelope_reference.geometry', return_value=fake_geometry):
            result = build_envelope(object(), self.job)
        self.assertEqual('solid-handle', result)
        fake_geometry.extrude.assert_called_once_with(
            'synthetic source envelope',
            [[1.0, 2.0], [11.0, 2.0], [11.0, 7.0], [1.0, 7.0]], 3.0, 3.0)
        fake_geometry.metadata.assert_called_once()

    def test_invalid_zero_dimension_is_rejected_before_geometry_or_write(self):
        self.job['features'][2]['value'] = 0
        fake_geometry_factory = Mock()
        with patch('envelope_reference.geometry', fake_geometry_factory):
            with self.assertRaisesRegex(ValueError, 'Positive finite envelope dimension'):
                build_envelope(object(), self.job)
        fake_geometry_factory.assert_not_called()

    def test_detailed_body_role_is_rejected_before_geometry_or_write(self):
        self.job['geometry_role'] = 'detailed_body'
        fake_geometry_factory = Mock()
        with patch('envelope_reference.geometry', fake_geometry_factory):
            with self.assertRaisesRegex(ValueError, 'reference_envelope'):
                build_envelope(object(), self.job)
        fake_geometry_factory.assert_not_called()

    def test_native_vertex_extrema_pass_and_changed_extent_fail(self):
        points = [[x, y, z] for x in (1, 11) for y in (2, 7) for z in (3, 6)]
        self.assertEqual('PASS', verify({'points': points}, self.job)['result'])
        altered = [[x, y, z] for x in (1, 10.99) for y in (2, 7) for z in (3, 6)]
        self.assertEqual('FAIL', verify({'points': altered}, self.job)['result'])


if __name__ == '__main__':
    unittest.main()
