import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from planar_profiles import bounded_extrusion, ellipse_arc_chord_error_bound, offset_bend_section, quarter_bend_section, reframe_planar_profile, revolve_profile_y
from cadtools.runtime import CadError
from planar_profiles import rolling_corner_offset, straight_profile_station_intervals


class RollingCornerOffsetTests(unittest.TestCase):
    def test_crest_to_flat_preserves_support_and_error(self):
        profile = [[0,0],[12,5],[12,-2],[0,-2]]
        result = rolling_corner_offset(profile,1,13,[0,1],max_chord_error=.001)
        self.assertAlmostEqual(result['centre_points'][0][0], 7)
        self.assertAlmostEqual(result['centre_points'][0][1], 17)
        self.assertAlmostEqual(result['centre_points'][-1][0], 12)
        self.assertAlmostEqual(result['centre_points'][-1][1], 18)
        self.assertLessEqual(result['chord_error'],.001)
        self.assertTrue(all(abs(math.hypot(x-12,z-5)-13) < 1e-10
                            for x,z in result['centre_points']))

    def test_reflection_preserves_arc_stations(self):
        profile = [[0,0],[12,5],[12,-2],[0,-2]]
        expected=rolling_corner_offset(profile,1,7,[0,1],max_chord_error=.005)
        reflected=rolling_corner_offset([[-x,y] for x,y in profile],1,7,[0,1],max_chord_error=.005)
        for (a,b),(c,d) in zip(expected['centre_points'],reflected['centre_points'],strict=True):
            self.assertAlmostEqual(a,-c)
            self.assertAlmostEqual(b,d)

    def test_rejects_normal_outside_cone_or_concave_corner(self):
        with self.assertRaisesRegex(ValueError,"convex corner"):
            rolling_corner_offset([[0,0],[12,5],[12,-2],[0,-2]],1,13,[-1,0],max_chord_error=.001)
        with self.assertRaisesRegex(ValueError,"convex corner"):
            rolling_corner_offset([[0,0],[5,0],[5,2],[2,2],[2,5],[0,5]],3,2,[0,1],max_chord_error=.001)


class StraightProfileStationTests(unittest.TestCase):
    def test_sloping_edges_and_axis_selection(self):
        section = [[0, 0], [4, 0], [6, 4], [0, 4]]
        self.assertEqual(straight_profile_station_intervals(section, 5), [(2, 4)])
        self.assertEqual(straight_profile_station_intervals(section, 2, axis=1), [(0, 5)])
        self.assertEqual(straight_profile_station_intervals(section, 7), [])

    def test_concave_profile_preserves_separate_material_intervals(self):
        section = [[0,0],[8,0],[8,2],[2,2],[2,6],[8,6],[8,8],[0,8]]
        self.assertEqual(straight_profile_station_intervals(section, 5), [(0,2),(6,8)])
        mirrored = [[x,-y] for x,y in section[::-1]]
        self.assertEqual(straight_profile_station_intervals(mirrored, 5), [(-8,-6),(-2,0)])

    def test_ambiguous_station_and_invalid_loop_fail(self):
        with self.assertRaisesRegex(ValueError, "profile vertex"):
            straight_profile_station_intervals([[0,0],[4,0],[4,5],[0,5]], 4+1e-8)
        with self.assertRaises(ValueError):
            straight_profile_station_intervals([[0,0],[3,3],[0,3],[3,0]], 1)


class QuarterBendSectionTests(unittest.TestCase):
    def test_tangent_stations_and_opposed_quarter_arcs(self):
        points, bulges = quarter_bend_section([10,20],2,1,7,9)
        self.assertEqual([list(point) for point in points],
            [[7,27],[7,20],[10,17],[19,17],[19,18],[10,18],[8,20],[8,27]])
        self.assertEqual(set(bulges), {1, 5})
        self.assertAlmostEqual(4 * math.atan(bulges[1]), math.pi / 2)
        self.assertAlmostEqual(4 * math.atan(bulges[5]), -math.pi / 2)

    def test_rejects_zero_length_and_collapsed_coordinates(self):
        for args in (([0,0],1,1,0,2), ([1e20,0],1,1,2,2)):
            with self.assertRaises(CadError):
                quarter_bend_section(*args)


class ReframedPlanarProfileTests(unittest.TestCase):
    def test_rotation_preserves_arc_signs_and_reflection_reverses_them(self):
        points, bulges = quarter_bend_section([0,0],2,1,7,9)
        moved, turns = reframe_planar_profile(points, bulges, origin=[12,20],
                                                u_axis=[-1,0], v_axis=[0,-1])
        flipped, signs = reframe_planar_profile(points, bulges, origin=[12,20],
                                                u_axis=[-1,0], v_axis=[0,1])
        self.assertEqual([list(p) for p in moved], [[12-u,20-v] for u,v in points])
        self.assertEqual([list(p) for p in flipped], [[12-u,20+v] for u,v in points])
        self.assertEqual(turns, bulges)
        self.assertEqual(signs, {index:-b for index,b in bulges.items()})

    def test_invalid_axes_and_collapsed_result_are_rejected(self):
        for origin, u_axis, v_axis in (([0,0],[1,0],[1,0]), ([0,0],[2,0],[0,1]),
                                       ([1e20,1e20],[1,0],[0,1])):
            with self.assertRaises((CadError, ValueError)):
                reframe_planar_profile([[0,0],[2,0],[2,2],[0,2]], {},
                                      origin=origin, u_axis=u_axis, v_axis=v_axis)


class OffsetBendSectionTests(unittest.TestCase):
    def test_tangent_legs_web_and_arc_order(self):
        vertices, arcs = offset_bend_section([10,20],2,1,7,5,8)
        self.assertEqual([list(point) for point in vertices],
                         [[7,15],[8,15],[8,20],[10,22],[17,22],[20,25],
                          [20,33],[19,33],[19,25],[17,23],[10,23],[7,20]])
        self.assertEqual(set(arcs), {2,4,8,10})
        for index, sign in ((2,-1),(4,1),(8,-1),(10,1)):
            self.assertAlmostEqual(4*math.atan(arcs[index]),sign*math.pi/2)

    def test_invalid_or_unrepresentable_straights_are_rejected(self):
        for args in (([0,0],1,1,0,2,2), ([1e20,1e20],1,1,2,2,2)):
            with self.assertRaises(CadError):
                offset_bend_section(*args)


class ArcChordErrorTests(unittest.TestCase):
    def test_radius_and_step_give_the_circle_sagitta(self):
        self.assertAlmostEqual(ellipse_arc_chord_error_bound(2, math.pi/2),
                               2 - math.sqrt(2))
        self.assertGreater(ellipse_arc_chord_error_bound(5,1e-8),0)

    def test_bound_requires_a_positive_short_interval(self):
        for step in (0, -0.01, math.pi + 0.01, float('inf')):
            with self.assertRaises(CadError):
                ellipse_arc_chord_error_bound(10,step)


class NativeDrawing:
    def __init__(self):
        self.entities = {'stock': '3D Solid'}
        self.events = []

    def read(self, operation, **fields):
        if operation != 'query':
            raise AssertionError(operation)
        return {'entities': [
            {'handle': handle, 'type': kind} for handle, kind in self.entities.items()
        ]}

    def mutate(self, label, operation, **fields):
        self.events.append((label, operation))
        if operation == 'entities_create':
            handle = label
            self.entities[handle] = 'Polyline'
            return {'result': {'handles': [handle]}}
        if operation == 'select':
            return {'state': {'selection': []}}
        if operation == 'run' and fields['cmd'].startswith('PRESSPULL '):
            self.entities['body'] = '3D Solid'
            return {'request_id': 'extrusion'}
        if operation == 'entities_delete':
            for handle in fields['handles']:
                del self.entities[handle]
            return {}
        raise AssertionError(operation)


class BoundedExtrusionCheckpointTests(unittest.TestCase):
    boundaries = [
        {'points': [[0, 0], [5, 0], [5, 5], [0, 5]]},
        {'points': [[2, 2], [2, 3], [3, 3], [3, 2]]},
    ]

    def build(self, drawing, **kwargs):
        return bounded_extrusion(
            drawing, self.boundaries, [1, 1, 0], 3, label='example', **kwargs,
        )

    def test_callback_sees_each_stage_and_only_owned_handles(self):
        drawing = NativeDrawing()
        stages = []

        def checkpoint(stage, handles):
            self.assertEqual(set(handles), drawing.entities.keys() - {'stock'})
            stages.append(stage)

        result = self.build(drawing, checkpoint=checkpoint)
        self.assertEqual(stages, [
            'example-boundary-0', 'example-boundary-1',
            'example-solid', 'example-profiles-cleared',
        ])
        self.assertEqual(result['body'], 'body')
        self.assertEqual(drawing.entities, {'stock': '3D Solid', 'body': '3D Solid'})

    def test_uncertain_save_stops_before_deleting_profiles(self):
        drawing = NativeDrawing()

        def checkpoint(stage, handles):
            if stage == 'example-solid':
                raise RuntimeError('Save completion unknown')

        with self.assertRaisesRegex(RuntimeError, 'Save completion unknown'):
            self.build(drawing, checkpoint=checkpoint)
        self.assertEqual(len(drawing.entities), 4)
        self.assertNotIn('entities_delete', [operation for _, operation in drawing.events])

    def test_existing_call_without_callback_still_removes_only_owned_profiles(self):
        drawing = NativeDrawing()
        result = self.build(drawing)
        self.assertEqual(result['request_id'], 'extrusion')
        self.assertEqual(drawing.entities, {'stock': '3D Solid', 'body': '3D Solid'})

class RevolveDrawing(NativeDrawing):
    def __init__(self, consume):
        super().__init__()
        self.consume = consume

    def mutate(self, label, operation, **fields):
        if operation == 'select':
            self.events.append((label, operation))
            return {'state': {'selection': fields['handles']}}
        if operation == 'run':
            self.events.append((label, operation))
            if fields['cmd'] != 'REVOLVE Y 360':
                raise AssertionError(fields['cmd'])
            self.entities['body'] = '3D Solid'
            if self.consume:
                del self.entities['ring-section-profile']
            return {
                'changes': [{'kind': 'Added', 'handle': 'body'}],
                'request_id': label,
            }
        return super().mutate(label, operation, **fields)


class RevolveProfileCheckpointTests(unittest.TestCase):
    section = [[3, -2], [5, -2], [5, 2], [3, 2]]

    def build(self, drawing, checkpoint):
        return revolve_profile_y(drawing, self.section, label='ring', checkpoint=checkpoint)

    def test_consumed_sketch_checkpoints_only_live_handles(self):
        drawing = RevolveDrawing(consume=True)
        saves = []
        result = self.build(drawing, lambda stage, handles: saves.append((stage, handles)))
        self.assertEqual(saves, [
            ('ring-section', ('ring-section-profile',)), ('ring-solid', ('body',)),
        ])
        self.assertEqual(result['request_id'], 'ring-revolve')
        self.assertEqual(drawing.entities, {'stock': '3D Solid', 'body': '3D Solid'})

    def test_retained_sketch_checked_before_owned_cleanup(self):
        drawing = RevolveDrawing(consume=False)
        saves = []
        def checkpoint(stage, handles):
            saves.append(stage)
            self.assertEqual(set(handles), drawing.entities.keys() - {'stock'})
        self.build(drawing, checkpoint)
        self.assertEqual(saves, ['ring-section', 'ring-solid', 'ring-section-cleared'])
        self.assertEqual(drawing.entities, {'stock': '3D Solid', 'body': '3D Solid'})

    def test_failed_solid_save_preserves_owned_sketch(self):
        drawing = RevolveDrawing(consume=False)
        def checkpoint(stage, handles):
            if stage == 'ring-solid':
                raise RuntimeError('Save unknown')
        with self.assertRaisesRegex(RuntimeError, 'Save unknown'):
            self.build(drawing, checkpoint)
        self.assertIn('ring-section-profile', drawing.entities)
        self.assertIn('body', drawing.entities)
        self.assertNotIn('entities_delete', [operation for _, operation in drawing.events])
