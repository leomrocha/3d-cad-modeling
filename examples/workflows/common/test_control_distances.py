"""Numerical/contract tests for the supplied-point comparison helper."""
import copy
import unittest
from check_control_distances import compare_distances


class ControlDistanceTests(unittest.TestCase):
    def setUp(self):
        self.model = {'length_unit': 'm', 'model_revision': 'test-revision',
                      'coordinate_frame': 'test-frame',
                      'points': [{'id': 'a', 'xyz': [0, 0, 0]},
                                 {'id': 'b', 'xyz': [0.102, 0, 0]},
                                 {'id': 'c', 'xyz': [0, 0.1, 0]}]}
        self.refs = {'distances': [
            {'id': 'fitted-length', 'from': 'a', 'to': 'c', 'value': 100,
             'unit': 'mm', 'role': 'fit', 'source': 'synthetic fit fixture'},
            {'id': 'held-out-length', 'from': 'a', 'to': 'b', 'value': 10,
             'unit': 'cm', 'role': 'check', 'source': 'synthetic check fixture'}]}

    def test_units_and_separate_roles(self):
        report = compare_distances(self.refs, self.model, True)
        self.assertAlmostEqual(report['distances'][1]['signed_residual_mm'], 2.0)
        self.assertAlmostEqual(report['groups']['fit']['maximum_absolute_residual_mm'], 0.0)
        self.assertAlmostEqual(report['groups']['check']['mean_absolute_residual_mm'], 2.0)

    def test_mm_model_coordinates(self):
        model = copy.deepcopy(self.model)
        model['length_unit'] = 'mm'
        for point in model['points']:
            point['xyz'] = [v * 1000 for v in point['xyz']]
        self.assertAlmostEqual(compare_distances(self.refs, model)['distances'][1]['model_m'], 0.102)

    def test_rejects_duplicate_points(self):
        self.model['points'].append(self.model['points'][0])
        with self.assertRaises(ValueError):
            compare_distances(self.refs, self.model)

    def test_requires_check_control_when_requested(self):
        self.refs['distances'] = self.refs['distances'][:1]
        with self.assertRaises(ValueError):
            compare_distances(self.refs, self.model, True)

    def test_rejects_nonfinite_coordinate(self):
        self.model['points'][0]['xyz'][0] = float('nan')
        with self.assertRaises(ValueError):
            compare_distances(self.refs, self.model)

    def test_source_and_units_are_required(self):
        self.refs['distances'][0]['source'] = ''
        with self.assertRaises(ValueError):
            compare_distances(self.refs, self.model)


if __name__ == '__main__':
    unittest.main()
