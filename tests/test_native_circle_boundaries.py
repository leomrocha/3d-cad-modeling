"""Synthetic ACIS boundary-curve tests; no component fixture or OCS session."""
import math
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch

ROOT = __import__('pathlib').Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
try:
    from ezdxf.acis.const import Tags
    from native_acis import sab_features
except ImportError:
    Tags = None
    sab_features = None


class Token:
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value


class Entity:
    def __init__(self, name, data=None):
        self.name = name
        self.data = list(data or [])


def ptr(value):
    return Token(Tags.POINTER, value)


def loc(value):
    return Token(Tags.LOCATION_VEC, tuple(value))


def direction(value):
    return Token(Tags.DIRECTION_VEC, tuple(value))


def double(value):
    return Token(Tags.DOUBLE, value)


def circle_pair(*, parameter_end=2 * math.pi, ratio=1.0, curve_name='ellipse-curve', transform=None):
    """Two synthetic cap faces sharing one circular boundary edge."""
    null = Entity('null-ptr')
    point_a = Entity('point', [ptr(null), loc((1.0, 0.0, 0.0))])
    point_b = Entity('point', [ptr(null), loc((1.0, 0.0, 0.0))])
    vertex_a = Entity('vertex', [ptr(null), ptr(point_a)])
    vertex_b = Entity('vertex', [ptr(null), ptr(point_b)])
    curve = Entity(curve_name, [
        ptr(null), loc((0.0, 0.0, 0.0)), direction((0.0, 0.0, 1.0)),
        direction((2.0, 0.0, 0.0)), double(ratio),
        Token(Tags.BOOL_FALSE, False), Token(Tags.BOOL_FALSE, False),
    ])
    edge = Entity('edge')
    co_a = Entity('coedge')
    co_b = Entity('coedge')
    edge.data = [ptr(null), ptr(vertex_a), double(0.0), ptr(vertex_b),
                 double(parameter_end), ptr(co_a), ptr(curve)]
    loop_a = Entity('loop')
    loop_b = Entity('loop')
    co_a.data = [ptr(null), ptr(co_a), ptr(null), ptr(co_b), ptr(edge),
                 Token(Tags.BOOL_TRUE, True), ptr(loop_a), ptr(null)]
    co_b.data = [ptr(null), ptr(co_b), ptr(null), ptr(co_a), ptr(edge),
                 Token(Tags.BOOL_FALSE, False), ptr(loop_b), ptr(null)]
    loop_a.data = [ptr(null), ptr(null), ptr(co_a)]
    loop_b.data = [ptr(null), ptr(null), ptr(co_b)]
    surf_a = Entity('plane-surface', [ptr(null), loc((0.0, 0.0, 0.0)), direction((0, 0, 1))])
    surf_b = Entity('plane-surface', [ptr(null), loc((0.0, 0.0, 1.0)), direction((0, 0, 1))])
    face_a = Entity('face', [ptr(null), ptr(null), ptr(loop_a), ptr(surf_a)])
    face_b = Entity('face', [ptr(null), ptr(null), ptr(loop_b), ptr(surf_b)])
    body_data = [ptr(face_a), ptr(face_b)]
    if transform is not None:
        body_data.append(ptr(Entity('transform', [
            direction((1, 0, 0)), direction((0, 1, 0)), direction((0, 0, 1)),
            direction(transform), double(1.0),
        ])))
    body = Entity('body', body_data)
    sab = SimpleNamespace(header=SimpleNamespace(version=700, units_in_mm=1),
                          entities=[body])
    return sab


@unittest.skipUnless(Tags is not None, 'Requires the native ACIS reader dependency')
class NativeCircleBoundaryTests(unittest.TestCase):
    def read(self, sab, **kwargs):
        with patch('ezdxf.acis.sab.parse_sab', return_value=sab):
            return sab_features(b'synthetic-sab', **kwargs)

    def test_default_output_does_not_add_boundary_edge_records(self):
        result = self.read(circle_pair())
        self.assertNotIn('face_boundary_edges', result)

    def test_opt_in_reads_full_circle_and_reciprocal_face_association(self):
        result = self.read(circle_pair(), include_edge_curves=True)
        self.assertEqual(len(result['face_boundary_edges']), 2)
        edge = result['face_boundary_edges'][0]['loops'][0]['edges'][0]
        self.assertEqual(edge['curve_type'], 'ellipse-curve')
        self.assertTrue(edge['full_period_2pi'])
        self.assertAlmostEqual(edge['parameter_span'], 2 * math.pi)
        self.assertEqual(edge['ellipse']['center'], [0.0, 0.0, 0.0])
        self.assertEqual(edge['ellipse']['major_axis'], [2.0, 0.0, 0.0])
        self.assertAlmostEqual(edge['ellipse']['major_radius'], 2.0)
        self.assertAlmostEqual(edge['ellipse']['minor_radius'], 2.0)
        self.assertTrue(edge['ellipse']['is_circle'])
        self.assertEqual(edge['partner_face_index'], 1)
        self.assertEqual(edge['partner_surface_type'], 'plane-surface')
        self.assertEqual(result['face_boundary_edges'][1]['loops'][0]['edges'][0]['partner_face_index'], 0)

    def test_partial_ellipse_is_reported_as_partial(self):
        result = self.read(circle_pair(parameter_end=math.pi), include_edge_curves=True)
        edge = result['face_boundary_edges'][0]['loops'][0]['edges'][0]
        self.assertFalse(edge['full_period_2pi'])
        self.assertAlmostEqual(edge['parameter_span'], math.pi)

    def test_rigid_transform_requires_explicit_option_and_transforms_centers(self):
        with self.assertRaisesRegex(ValueError, 'rigid-frame'):
            self.read(circle_pair(transform=(5, 0, 0)), include_edge_curves=True)
        result = self.read(circle_pair(transform=(5, 0, 0)),
                           allow_rigid=True, include_edge_curves=True)
        self.assertEqual(result['face_boundary_edges'][0]['loops'][0]['edges'][0]
                         ['ellipse']['center'], [5.0, 0.0, 0.0])

    def test_non_circular_ellipse_retains_ratio_without_circle_claim(self):
        result = self.read(circle_pair(ratio=0.5), include_edge_curves=True)
        ellipse = result['face_boundary_edges'][0]['loops'][0]['edges'][0]['ellipse']
        self.assertFalse(ellipse['is_circle'])
        self.assertAlmostEqual(ellipse['minor_to_major_ratio'], 0.5)
        self.assertAlmostEqual(ellipse['minor_radius'], 1.0)

    def test_observed_straight_curve_layout_reports_world_line(self):
        sab = circle_pair(curve_name='straight-curve')
        body = sab.entities[0]
        face = next(t.value for t in body.data if t.tag == Tags.POINTER)
        edge = face.data[2].value.data[2].value.data[4].value
        curve = next(t.value for t in edge.data if t.tag == Tags.POINTER
                     and t.value.name == 'straight-curve')
        null = curve.data[0].value
        curve.data = [ptr(null), loc((0.0, 0.0, 0.0)), direction((0.0, 0.0, 1.0)),
                      Token(Tags.BOOL_FALSE, False), Token(Tags.BOOL_FALSE, False)]
        result = self.read(sab, include_edge_curves=True)
        line = result['face_boundary_edges'][0]['loops'][0]['edges'][0]['line']
        self.assertEqual(line, {'origin': [0.0, 0.0, 0.0], 'direction': [0.0, 0.0, 1.0]})

    def test_unsupported_straight_curve_layout_fails_closed(self):
        sab = circle_pair(curve_name='straight-curve')
        body = sab.entities[0]
        face = next(t.value for t in body.data if t.tag == Tags.POINTER)
        edge = face.data[2].value.data[2].value.data[4].value
        curve = next(t.value for t in edge.data if t.tag == Tags.POINTER
                     and t.value.name == 'straight-curve')
        curve.data = [ptr(curve.data[0].value), loc((0, 0, 0)), direction((0, 0, 1))]
        with self.assertRaisesRegex(ValueError, 'straight-curve token layout'):
            self.read(sab, include_edge_curves=True)

    def test_unknown_curve_fails_closed_when_opted_in(self):
        with self.assertRaisesRegex(ValueError, 'Unsupported boundary curve'):
            self.read(circle_pair(curve_name='spline-curve'), include_edge_curves=True)

    def test_unsupported_curve_token_layout_fails_closed(self):
        sab = circle_pair()
        body = sab.entities[0]
        face = next(t.value for t in body.data if t.tag == Tags.POINTER)
        coedge = face.data[2].value.data[2].value
        curve = next(t.value for t in coedge.data[4].value.data
                     if t.tag == Tags.POINTER and t.value.name == 'ellipse-curve')
        curve.data[3] = double(2.0)
        with self.assertRaisesRegex(ValueError, 'ellipse-curve token layout'):
            self.read(sab, include_edge_curves=True)

    def test_unowned_partner_coedge_fails_closed(self):
        sab = circle_pair()
        body = sab.entities[0]
        first_face = next(t.value for t in body.data if t.tag == Tags.POINTER)
        loop = first_face.data[2].value
        coedge = loop.data[2].value
        edge = coedge.data[4].value
        orphan = Entity('coedge')
        orphan.data = [ptr(Entity('null-ptr')), ptr(orphan), ptr(Entity('null-ptr')),
                       ptr(coedge), ptr(edge), Token(Tags.BOOL_FALSE, False),
                       ptr(Entity('null-ptr')), ptr(Entity('null-ptr'))]
        coedge.data[3] = ptr(orphan)
        with self.assertRaises(ValueError):
            self.read(sab, include_edge_curves=True)

    def test_partner_must_share_the_same_edge(self):
        sab = circle_pair()
        body = sab.entities[0]
        face = next(t.value for t in body.data if t.tag == Tags.POINTER)
        coedge = face.data[2].value.data[2].value
        partner = coedge.data[3].value
        edge = coedge.data[4].value
        partner.data[4] = ptr(Entity('edge', list(edge.data)))
        with self.assertRaisesRegex(ValueError, 'partner must belong'):
            self.read(sab, include_edge_curves=True)

    def test_nonfinite_or_invalid_curve_parameters_fail_closed(self):
        sab = circle_pair(ratio=float('nan'))
        with self.assertRaisesRegex(ValueError, 'ellipse-curve parameters'):
            self.read(sab, include_edge_curves=True)
        with self.assertRaisesRegex(ValueError, 'parameter interval must be finite'):
            self.read(circle_pair(parameter_end=float('inf')), include_edge_curves=True)
        sab = circle_pair(parameter_end=1e308)
        body = sab.entities[0]
        face = next(t.value for t in body.data if t.tag == Tags.POINTER)
        coedge = face.data[2].value.data[2].value
        edge = coedge.data[4].value
        edge.data[2] = double(-1e308)
        with self.assertRaisesRegex(ValueError, 'parameter span must be finite'):
            self.read(sab, include_edge_curves=True)


if __name__ == '__main__':
    unittest.main()
