from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from rational_surface import evaluate_rational_surface
from source_trim_loop import prepare_trim_loop


class TrimLoopTests(unittest.TestCase):
    def setUp(self):
        self.vertices = {'A': [0, 0, 0], 'B': [1, 0, 0], 'C': [0, 1, 0]}
        # Curve 1 runs opposite to its defined edge. Edge 2 is used backwards.
        self.edges = {
            1: dict(start='A', end='B', curve_id=11, same_sense=False,
                    curve_samples=[[1, 0, 0], [.5, 0, 0], [.001, 0, 0]]),
            2: dict(start='C', end='B', curve_id=12, same_sense=True,
                    curve_samples=[[0, 1, 0], [1, 0, 0]]),
            3: dict(start='C', end='A', curve_id=13, same_sense=True,
                    curve_samples=[[0, 1, 0], [0, 0, 0]])}
        self.called = []
        def inverse(xyz):
            self.called.append(xyz)
            return xyz[:2]
        surface = {'degree_u': 1, 'degree_v': 1, 'knots_u': [0, 0, 1, 1],
                   'knots_v': [0, 0, 1, 1], 'weights': [[1, 1], [1, 1]],
                   'control_points': [[[0, 0, 0], [0, 1, 0]], [[1, 0, 0], [1, 1, 0]]]}
        def evaluate(uv):
            return evaluate_rational_surface(surface, uv, precisions=[40, 80],
                                             transform=[[int(i == j) for j in range(4)] for i in range(4)])
        self.job = dict(face_id=1, support_id=2, vertices=self.vertices, edges=self.edges,
                        traversal=[{'edge_id': i, 'forward': i != 2} for i in (1, 2, 3)],
                        inverse_uv=inverse, evaluate_support=evaluate, parameter_bounds=[[0, 1]] * 2,
                        endpoint_limit_mm=.002, inverse_limit_mm=0)

    def test_shared_corners_and_curve_orientations(self):
        result = prepare_trim_loop(**self.job)
        self.assertEqual(result['result'], 'PASS')
        self.assertEqual(result['uv_polygon'], [[0, 0], [.5, 0], [1, 0], [0, 1]])
        self.assertEqual(len(self.called), 4)
        self.assertEqual(result['max_endpoint_to_vertex_mm'], .001)
        self.assertEqual(result['max_inverse_residual_mm'], 0)
        self.assertEqual(result['edges'][1]['oriented_vertices'], ['B', 'C'])

    def test_residual_limits_are_independent(self):
        self.job['endpoint_limit_mm'] = 0
        self.assertEqual(prepare_trim_loop(**self.job)['result'], 'FAIL')
        self.job['endpoint_limit_mm'] = .002
        self.edges[1]['curve_samples'][1][2] = .004
        result = prepare_trim_loop(**self.job)
        self.assertEqual(result['result'], 'FAIL')
        self.assertEqual(result['max_inverse_residual_mm'], .004)

    def test_coincident_distinct_ids_and_wrong_orientation(self):
        self.vertices['other'] = self.vertices['B']
        self.edges[2]['end'] = 'other'
        with self.assertRaisesRegex(ValueError, 'vertex IDs'):
            prepare_trim_loop(**self.job)
        self.edges[2]['end'] = 'B'
        self.job['traversal'][1]['forward'] = True
        with self.assertRaisesRegex(ValueError, 'vertex IDs'):
            prepare_trim_loop(**self.job)

    def test_uv_crossing_domain_and_evaluator_failure(self):
        self.edges[1]['curve_samples'][1] = [0, .5, 0]
        with self.assertRaisesRegex(ValueError, 'profile_points'):
            prepare_trim_loop(**self.job)
        self.job['inverse_uv'] = lambda xyz: [2, 0]
        with self.assertRaisesRegex(ValueError, 'chart'):
            prepare_trim_loop(**self.job)
        self.job['inverse_uv'] = lambda xyz: xyz[:2]
        self.job['evaluate_support'] = lambda uv: {'result': 'PRECISION_DISAGREEMENT'}
        with self.assertRaisesRegex(ValueError, 'Support evaluation'):
            prepare_trim_loop(**self.job)
