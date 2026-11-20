"""Portable ACIS700 graph, analytic trim and mixed-placement regressions."""
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from cadtools.records import audit_type_counts
from native_acis import sat_readback, solid_acis_payload
from native_views import boundary_curves, placed_boundaries, sample

try:
    from ezdxf.acis import api
    from ezdxf.render.forms import cube
except ImportError:
    api = None


@unittest.skipIf(api is None, 'Native reader dependencies required')
class NativeSatTests(unittest.TestCase):
    def setUp(self):
        body = api.body_from_mesh(cube().translate(3, 4, 5))
        self.sat = '\n'.join(api.export_sat([body], version=700))
        self.sab = api.export_sab([api.body_from_mesh(cube())], version=700)

    def test_sab_and_sat_vertex_edges_match(self):
        result = sat_readback(self.sat, allow_rigid=True)
        self.assertEqual(result['topology']['faces'], 6)
        self.assertEqual(result['topology']['coedges'], 24)
        self.assertTrue(result['topology']['reciprocal_closed_partners'])
        self.assertEqual(len(result['edges']), 12)
        self.assertEqual(result['cylinders'], [])
        self.assertEqual(min(result['points']), [2.5, 3.5, 4.5])
        self.assertEqual(max(result['points']), [3.5, 4.5, 5.5])
        normalize = lambda edges: sorted(sorted(edge['endpoints']) for edge in edges)
        centered = []
        for edge in result['edges']:
            centered.append(dict(endpoints=[
                [p[0] - 3, p[1] - 4, p[2] - 5] for p in edge['endpoints']
            ]))
        self.assertEqual(normalize(centered), normalize(boundary_curves(self.sab)))

    def test_transforms_require_opt_in_and_reject_improper_determinant(self):
        with self.assertRaisesRegex(ValueError, 'rigid-frame'):
            sat_readback(self.sat)
        existing = next(line for line in self.sat.splitlines() if line.startswith('transform '))
        reflected = existing.replace('1 0 0 0 1 0 0 0 1 ', '-1 0 0 0 1 0 0 0 1 ', 1)
        with self.assertRaisesRegex(ValueError, 'Reflected'):
            sat_readback(self.sat.replace(existing, reflected), allow_rigid=True)

    def test_nonreciprocal_edges_fail_display(self):
        existing = next(line for line in self.sat.splitlines() if line.startswith('coedge '))
        fields = existing.split()
        fields[6] = '$-1'
        malformed = self.sat.replace(existing, ' '.join(fields))
        self.assertFalse(sat_readback(malformed, allow_rigid=True)['topology']['reciprocal_closed_partners'])
        with self.assertRaisesRegex(ValueError, 'Reciprocal'):
            boundary_curves(malformed)

    def test_non_analytic_boundary_retains_endpoints(self):
        sat = self.sat.replace('straight-curve ', 'intcurve-curve ', 1)
        curve, = [row for row in boundary_curves(sat) if row['curve_type'] == 'intcurve-curve']
        self.assertEqual(sample(curve), (curve['endpoints'], True))

    def test_ellipse_uses_parameters_and_exact_body_transform(self):
        existing = sat_readback(self.sat, allow_rigid=True)
        record_lines = self.sat.splitlines()[3:-1]
        edge_index = next(i for i, r in enumerate(record_lines) if r.startswith('edge '))
        fields = record_lines[edge_index].split()
        curve_index = int(fields[9][1:])
        curve_line = record_lines[curve_index].split()
        local_start = [float(v) for v in curve_line[4:7]]
        direction = [float(v) for v in curve_line[7:10]]
        major = [-v / 2 for v in direction]
        center = [p - a for p, a in zip(local_start, major)]
        normal = [0, 0, 1] if abs(direction[2]) < 0.5 else [1, 0, 0]
        fields[7] = str(math.pi)
        record_lines[edge_index] = ' '.join(fields)
        record_lines[curve_index] = ' '.join(
            ['ellipse-curve', *curve_line[1:4], *map(str, center + normal + major), '1', 'I', 'I', '#']
        )
        lines = self.sat.splitlines()
        sat = '\n'.join(lines[:3] + record_lines + lines[-1:])
        curve, = [row for row in boundary_curves(sat) if row['curve_type'] == 'ellipse-curve']
        self.assertEqual(curve['ellipse']['center'], [
            a + b for a, b in zip(center, existing['body_transform']['translation'])
        ])
        points, fallback = sample(curve)
        self.assertFalse(fallback)
        self.assertEqual(len(points), 65)
        for endpoint in (points[0], points[-1]):
            self.assertLess(min(math.dist(endpoint, target) for target in curve['endpoints']), 1e-12)

    def test_nested_display_mixes_live_sat_and_saved_sab(self):
        def xyz(x, y, z):
            return dict(x=x, y=y, z=z)

        records = [
            dict(handle='A', type='Insert', properties=dict(
                normal=xyz(0, 0, 1), insert_point=xyz(0, 10, 0), rotation=0,
                block_name='child', x_scale=1, y_scale=-1, z_scale=1,
            )),
            dict(handle='B', type='Solid3D', properties=dict(acis_data={
                'is_binary': False, 'sat_data': self.sat, 'sab_data': [],
            })),
            dict(handle='C', type='Solid3D', properties=dict(acis_data={'sab_data': list(self.sab)})),
        ]
        blocks = [
            dict(name='*Model_Space', properties=dict(entity_handles=['A', 'C'])),
            dict(name='child', properties=dict(base_point=xyz(0, 0, 0), entity_handles=['B'])),
        ]
        edges, instances = placed_boundaries(records, blocks)
        self.assertEqual(len(instances), 2)
        self.assertEqual(len(edges), 24)
        self.assertEqual({p[1] for edge in edges if edge['handle'] == 'B' for p in edge['points']}, {5.5, 6.5})
        self.assertEqual({p[1] for edge in edges if edge['handle'] == 'C' for p in edge['points']}, {-0.5, 0.5})
        self.assertEqual(audit_type_counts(records), {'3D Solid': 2, 'Block Reference': 1})

    def test_explicit_flags_select_encoding(self):
        record = dict(type='Solid3D', properties=dict(acis_data={
            'is_binary': False, 'sat_data': self.sat, 'sab_data': [1],
        }))
        self.assertEqual(solid_acis_payload(record), self.sat)
        record['properties']['acis_data']['sat_data'] = ''
        with self.assertRaisesRegex(ValueError, 'Nonempty'):
            solid_acis_payload(record)
