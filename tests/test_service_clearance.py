"""Continuous screening and exact same-definition witness regressions."""
import sys
from fractions import Fraction
from itertools import product
from math import cos, radians, sin
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from service_clearance import guided_circular_pilot_clearance, sampled_rotation_clearance
from service_clearance import axial_stack_witness, bounded_axial_section_clearance, cartesian_cylinder_bounds, orthogonal_sleeve_clearance, planar_translation_pieces, quarter_turn_box, rectangle_radial_bounds, rpy_world_x_bounds, shared_definition_coincidence, static_box_contact_dimension, static_box_gap, static_box_halfspace_gap, translated_box_group_margin, translation_box_window


def placement(x=0, y=0, z=0):
    return [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]


class ServiceClearance(unittest.TestCase):
    box = [[0, 0, 0], [1, 1, 1]]

    def test_sampled_rotation_accounts_for_motion_and_readback_error(self):
        check = sampled_rotation_clearance([(0, 8), (2, 7), (3, 10)],
                                           radius_bound=100, gap_error_bound=0.25,
                                           required_reserve=5)
        self.assertEqual(check["result"], "PASS_CONTINUOUS_RESERVE")
        self.assertEqual(check["limiting_angles_deg"], ["0", "2"])
        self.assertAlmostEqual(float(Fraction(check["lower_bound"])), 6.75 - 100*radians(1))

    def test_positive_endpoints_do_not_prove_mid_interval_clearance(self):
        check = sampled_rotation_clearance([(0, 5), (30, 5)],
                                           radius_bound=100, gap_error_bound=0)
        self.assertEqual(check["result"], "UNRESOLVED_RESERVE")

    def test_duplicate_and_nonfinite_rotation_samples_are_invalid(self):
        for rows in ([(0, 5), (0, 4)], [(0, 5), (2, float("inf"))], [(0, 5)]):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                sampled_rotation_clearance(rows, radius_bound=100, gap_error_bound=0.5)

    def test_cylinder_bounds_include_radius_missing_from_seam_vertices(self):
        box = cartesian_cylinder_bounds((20, 100, -4), axis=1, radius=5, span=(2, 40))
        self.assertEqual(box, [[15, 2, -9],[25, 40, 1]])
        wall = [[10, 0, -14],[30, 45, -11]]
        self.assertEqual(static_box_gap(box, wall)["squared_gap"], "4")

    def test_full_radius_boxes_screen_translating_shaft_against_perpendicular_guide(self):
        shaft = cartesian_cylinder_bounds((50, 0, 0), axis=1, radius=10, span=(-30, 30))
        blocked = cartesian_cylinder_bounds((40, 15, 0), axis=2, radius=8, span=(-10, 40))
        clear = cartesian_cylinder_bounds((31, 15, 0), axis=2, radius=8, span=(-10, 40))
        stroke = (0, 0, 30)
        self.assertEqual(translation_box_window(shaft, blocked, stroke)["result"], "CANDIDATE")
        self.assertEqual(translation_box_window(shaft, clear, stroke)["result"], "DISJOINT_BOUNDS")
        self.assertEqual(static_box_gap(shaft, clear)["axis_gaps"], ["1", "0", "0"])

    def test_cylinder_bounds_round_outward_and_check_inputs(self):
        from fractions import Fraction

        box = cartesian_cylinder_bounds((0.1, 0, 0), axis=2, radius=0.2, span=(1, 2))
        self.assertLessEqual(Fraction(box[0][0]), Fraction(0.1)-Fraction(0.2))
        self.assertGreaterEqual(Fraction(box[1][0]), Fraction(0.1)+Fraction(0.2))
        for options in (dict(axis=True,radius=1,span=(1,2)), dict(axis=0,radius=0,span=(1,2)),
                        dict(axis=0,radius=1,span=(1,1)), dict(axis=0,radius=float("nan"),span=(1,2))):
            with self.subTest(options=options), self.assertRaises(ValueError):
                cartesian_cylinder_bounds((0,0,0), **options)

    def test_guided_pilot_clears_slot_through_full_travel(self):
        report = guided_circular_pilot_clearance(
            slot_centres=(-8,8), slot_radius=26.8, travel_centres=(-8,8),
            pilot_radius=26, side_play=.3, minimum_reserve=.49)
        self.assertEqual(report["result"], "PASS_NOMINAL_CAPSULE_CLEARANCE")
        self.assertAlmostEqual(report["minimum_slot_gap"], .5)

    def test_guided_pilot_checks_both_end_and_side_play(self):
        options = dict(slot_centres=(0,8), slot_radius=4, travel_centres=(-3,8),
                       pilot_radius=2, side_play=.5)
        self.assertEqual(guided_circular_pilot_clearance(**options)["result"],
                         "FAIL_REQUIRED_CLEARANCE")
        options.update(travel_centres=(0,9), side_play=.75)
        report = guided_circular_pilot_clearance(**options, minimum_reserve=.75)
        self.assertEqual(report["result"], "PASS_NOMINAL_CAPSULE_CLEARANCE")
        self.assertEqual(report["minimum_slot_gap"], .75)

    def test_guided_pilot_rejects_reversed_stations(self):
        with self.assertRaises(ValueError):
            guided_circular_pilot_clearance(
                slot_centres=(1,1), slot_radius=5, travel_centres=(0,2),
                pilot_radius=2, side_play=.25)

    def test_symmetric_rpy_covers_all_box_corners_and_sampled_intermediate_poses(self):
        box = [(-42,-15,-7),(-13,7,19)]
        pivot = (-4,2,3)
        limits = (25,5,25)
        low, high = rpy_world_x_bounds(box, pivot=pivot, roll_deg=limits[0],
                                       pitch_deg=limits[1], yaw_deg=limits[2])
        domains = [(-m,-m/2,0,m/2,m) for m in limits]
        for roll, pitch, yaw in product(*domains):
            r, p, a = map(radians, (roll,pitch,yaw))
            for x, y, z in product(*zip(*box, strict=True)):
                x, y, z = x-pivot[0], y-pivot[1], z-pivot[2]
                rotated_y = cos(r)*y-sin(r)*z
                rotated_z = sin(r)*y+cos(r)*z
                pitched_x = cos(p)*x+sin(p)*rotated_z
                observed = pivot[0]+cos(a)*pitched_x-sin(a)*rotated_y
                self.assertLessEqual(low, observed)
                self.assertGreaterEqual(high, observed)

    def test_symmetric_rpy_zero_motion_and_input_limits(self):
        box = [(3,1,-2),(9,7,8)]
        self.assertEqual(rpy_world_x_bounds(box,pivot=(11,-20,30),roll_deg=0,
                                            pitch_deg=0,yaw_deg=0), (3,9))
        for invalid in (-1,91,float("nan")):
            with self.subTest(yaw_deg=invalid), self.assertRaises(ValueError):
                rpy_world_x_bounds(box,pivot=(0,0,0),roll_deg=0,pitch_deg=0,yaw_deg=invalid)

    def test_axial_section_resolves_only_fully_covered_box_candidates(self):
        full = [[-3,-1,-3],[3,9,3]]
        shank = [[-1,0,-1],[1,9,1]]
        obstacle = [[2,2,-1],[4,4,1]]
        self.assertEqual(bounded_axial_section_clearance(full,shank,obstacle,axis=1),
                         dict(result='DISJOINT_SECTION_BOUNDS', axial_overlap=['2','4'], transverse_axis_gap='1'))
        head_overlap = [[2,-.5,-1],[4,4,1]]
        self.assertEqual(bounded_axial_section_clearance(full,shank,head_overlap,axis=1)['result'],
                         'SECTION_DOES_NOT_COVER_OVERLAP')
        tangent = [[1,2,-1],[4,4,1]]
        self.assertEqual(bounded_axial_section_clearance(full,shank,tangent,axis=1)['result'],
                         'SECTION_CONTACT_CANDIDATE')
        disjoint = [[4,2,-1],[5,4,1]]
        self.assertEqual(bounded_axial_section_clearance(full,shank,disjoint,axis=1)['result'],
                         'DISJOINT_FULL_BOUNDS')

    def test_orthogonal_sleeves_find_material_witness_and_separation(self):
        vertical = dict(axis=2, centre=[0, 1, 0], span=[-6, 7], radii=[1, 3])
        transverse = dict(axis=1, centre=[6, 0, 2], span=[-4, 4], radii=[2, 4])
        self.assertEqual(orthogonal_sleeve_clearance(vertical, transverse),
                         dict(result='STRICT_MATERIAL_INTERSECTION', normal_axis=0,
                              signed_outer_gap='-1', witness=['5/2', '1', '2']))
        self.assertEqual(orthogonal_sleeve_clearance(transverse, vertical)['witness'], ['5/2', '1', '2'])
        shifted = dict(transverse, centre=[8, 0, 2])
        self.assertEqual(orthogonal_sleeve_clearance(vertical, shifted)['result'], 'DISJOINT_OUTER_CYLINDERS')

    def test_orthogonal_sleeves_hold_endpoints_and_tangency(self):
        vertical = dict(axis=2, centre=[0, 0, 0], span=[1, 7], radii=[1, 3])
        transverse = dict(axis=1, centre=[6, 0, 1], span=[-4, 4], radii=[2, 4])
        tangent = dict(transverse, centre=[7, 0, 2])
        for sleeve in (transverse, tangent):
            self.assertEqual(orthogonal_sleeve_clearance(vertical, sleeve)['result'], 'NEEDS_FINITE_SOLID_CHECK')
        with self.assertRaises(ValueError):
            orthogonal_sleeve_clearance(vertical, dict(transverse, axis=2))

    def test_rectangle_radial_bounds_report_nearest_edge_and_farthest_corner(self):
        self.assertEqual(rectangle_radial_bounds([[1,-2],[3,1]],[0,0]),
                         dict(min_radius_squared="1",max_radius_squared="13"))
        self.assertEqual(rectangle_radial_bounds([[0,0],[2,2]],[1,1]),
                         dict(min_radius_squared="0",max_radius_squared="2"))

    def test_rectangle_radial_bounds_reject_inverted_or_nonfinite_input(self):
        for bounds in ([[2,0],[1,1]], [[0,0],[float("inf"),1]]):
            with self.assertRaises(ValueError):
                rectangle_radial_bounds(bounds,[0,0])

    def test_box_group_margin_verifies_a_translated_pose_and_ties(self):
        a = [[0,0,0],[1,1,1]]
        b = [[5,0,0],[6,1,1]]
        c = [[2,3,0],[3,4,1]]
        proof=translated_box_group_margin([a], [b,c], [2,0,0])
        self.assertEqual(proof["minimum_axis_margin"], "2")
        self.assertEqual(proof["pair_count"], 2)
        self.assertEqual(proof["limiting_pairs"], [
            dict(moving_index=0,fixed_index=0,axes=[0]),
            dict(moving_index=0,fixed_index=1,axes=[1]),
        ])

    def test_box_group_margin_separates_touching_and_overlap_cases(self):
        a = [[0,0,0],[1,1,1]]
        b = [[1,0,0],[2,1,1]]
        for dx,expected in ((0,"0"),(.25,"-1/4")):
            self.assertEqual(translated_box_group_margin([a],[b],[dx,0,0])
                             ["minimum_axis_margin"], expected)
        with self.assertRaises(ValueError):
            translated_box_group_margin([], [b], [0,0,0])

    def test_axial_stack_witness_preserves_contacts_and_nominal_reach(self):
        expected = dict(seat_gap="0", interface_gaps=["0", "0"],
                        last_layer_overlap="6", tip_past_stack="1/2")
        self.assertEqual(axial_stack_witness([0, 10], [(0, 2), (2, 3.5), (3.5, 9.5)]), expected)
        self.assertEqual(axial_stack_witness([5, 15], [(5, 7), (7, 8.5), (8.5, 14.5)]), expected)

    def test_axial_stack_exact_decimal_stations_in_tenths(self):
        witness = axial_stack_witness([42, 151], [(114, 151), (78, 114), (21, 78)], axis_sign=-1)
        self.assertEqual(witness, dict(seat_gap="0", interface_gaps=["0", "0"],
                                      last_layer_overlap="36", tip_past_stack="-21"))

    def test_axial_stack_uses_signed_world_axis_and_preserves_layer_order(self):
        upward = axial_stack_witness([0,11], [(0,2),(2,5),(5,9)])
        downward = axial_stack_witness([89,100], [(98,100),(95,98),(91,95)], axis_sign=-1)
        self.assertEqual(downward, upward)
        self.assertEqual(downward["tip_past_stack"], "2")
        for direction in (0, 2, True):
            with self.assertRaises(ValueError):
                axial_stack_witness([89,100], [(98,100)], axis_sign=direction)

    def test_axial_stack_witness_detects_axial_gaps_overlap_and_insufficient_reach(self):
        witness = axial_stack_witness([0, 3], [(0.25, 1), (1.5, 2.5), (2, 4)])
        self.assertEqual(witness, dict(seat_gap="1/4", interface_gaps=["1/2", "-1/2"],
                                      last_layer_overlap="1", tip_past_stack="-1"))
        self.assertEqual(axial_stack_witness([0, 2], [(3, 4)])["last_layer_overlap"], "0")
        for shaft, layers in [([1, 0], [(1, 2)]), ([0, 2], []), ([0, 2], [(1, 1)])]:
            with self.assertRaises(ValueError):
                axial_stack_witness(shaft, layers)

    def test_oblique_plane_separates_overlapping_aabbs_without_scaling_the_gap(self):
        bounds = [[0, -6, 10], [1, -4, 11]]
        for normal, offset in (([0,-1,1],12),([0,-3,3],36)):
            proof = static_box_halfspace_gap(bounds,normal=normal,offset=offset)
            self.assertEqual((proof['result'],proof['gap_squared']),('DISJOINT_BOUNDS','2'))
        self.assertEqual(static_box_halfspace_gap(bounds,normal=[0,-1,1],offset=14)['result'],'CANDIDATE')
        with self.assertRaisesRegex(ValueError,'Nonzero'):
            static_box_halfspace_gap(bounds,normal=[0,0,0],offset=14)

    def test_quarter_turn_encloses_intermediate_poses_for_each_axis_and_sign(self):
        import itertools
        import math
        for axis, direction in itertools.product(range(3), (-1, 1)):
            pivot = [2, -3, 4]
            bounds = [[-2, -1, -3], [4, 3, 2]]
            box = quarter_turn_box(bounds,pivot=pivot,axis=axis,direction=direction)
            u,v = (axis+1)%3,(axis+2)%3
            for theta in (0,math.pi/8,math.pi/4,3*math.pi/8,math.pi/2):
                for corner in itertools.product(*zip(*bounds,strict=True)):
                    a,b=corner[u]-pivot[u],corner[v]-pivot[v]
                    angle=theta*direction
                    result=list(corner)
                    result[u]=pivot[u]+a*math.cos(angle)-b*math.sin(angle)
                    result[v]=pivot[v]+a*math.sin(angle)+b*math.cos(angle)
                    for i,x in enumerate(result):
                        self.assertLessEqual(box[0][i],x+1e-12)
                        self.assertGreaterEqual(box[1][i],x-1e-12)
            self.assertEqual([bound[axis] for bound in box],[bound[axis] for bound in bounds])

    def test_quarter_turn_rejects_invalid_axis_or_direction(self):
        with self.assertRaises(ValueError):
            quarter_turn_box(self.box,pivot=[0,0,0],axis=-1,direction=1)
        with self.assertRaises(ValueError):
            quarter_turn_box(self.box,pivot=[0,0,0],axis=2,direction=0)

    def test_planar_translation_keeps_endpoint_and_nonparallel_edges(self):
        ring = [(0,0),(2,0),(2,2),(1,1),(0,2)]
        pieces = planar_translation_pieces(ring+ring[:1], [0,-3])
        self.assertEqual(pieces[0],tuple(ring))
        self.assertEqual(pieces[1],((0,-3),(2,-3),(2,-1),(1,-2),(0,-1)))
        self.assertEqual(len(pieces),5)
        self.assertIn(((2,2),(1,1),(1,-2),(2,-1)),pieces)

    def test_planar_translation_rejects_invalid_vertices(self):
        with self.assertRaises(ValueError):
            planar_translation_pieces([(0,0),(0,0),(2,2)], [1,1])
        self.assertEqual(len(planar_translation_pieces([(0,0),(1,0),(0,1)], [0,0])),1)

    def test_between_pose_candidate_for_both_travel_signs(self):
        upper = [[0, 0, 2], [1, 1, 3]]
        for moving, fixed, travel in [(self.box, upper, 4), (upper, self.box, -4)]:
            self.assertEqual(
                translation_box_window(moving, fixed, [0, 0, travel])["candidate_fraction"],
                ["1/4", "3/4"],
            )

    def test_cross_axis_windows_must_intersect(self):
        fixed = [[2, 5, 0], [3, 6, 1]]
        self.assertEqual(translation_box_window(self.box, fixed, [6, 6, 0])["result"],
                         "DISJOINT_BOUNDS")

    def test_endpoint_touch_and_zero_thickness(self):
        fixed = [[1, 1, 3], [1, 1, 3]]
        self.assertEqual(translation_box_window(self.box, fixed, [0, 0, 2])["candidate_fraction"],
                         ["1", "1"])

    def test_static_separation_and_short_travel(self):
        for fixed, displacement in [([[2, 0, 0], [3, 1, 1]], [0, 0, 4]),
                                    ([[0, 0, 4], [1, 1, 5]], [0, 0, 2])]:
            self.assertEqual(translation_box_window(self.box, fixed, displacement)["result"],
                             "DISJOINT_BOUNDS")

    def test_static_box_gap_preserves_diagonal_distance_and_sign_symmetry(self):
        fixed = [[4, 5, 0], [6, 7, 1]]
        expected = dict(result='DISJOINT_BOUNDS', axis_gaps=['3','4','0'], squared_gap='25')
        self.assertEqual(static_box_gap(self.box, fixed), expected)
        self.assertEqual(static_box_gap(fixed, self.box), expected)

    def test_static_box_gap_leaves_touching_boxes_as_candidates(self):
        fixed = [[1, 0, 0], [2, 1, 1]]
        for candidate in (self.box, fixed):
            self.assertEqual(static_box_gap(self.box, candidate)['result'], 'CANDIDATE')
        with self.assertRaises(ValueError):
            static_box_gap(self.box[::-1], self.box)

    def test_static_box_contact_dimension_covers_touch_overlap_and_separation(self):
        for corner, dimension in [([1,1,1],0),([1,1,0],1),([1,0,0],2),([0,0,0],3),([2,0,0],None)]:
            with self.subTest(corner=corner):
                other = [corner,[n+1 for n in corner]]
                self.assertEqual(static_box_contact_dimension(self.box,other)['dimension'],dimension)
                self.assertEqual(static_box_contact_dimension(other,self.box)['dimension'],dimension)
        self.assertEqual(static_box_contact_dimension(self.box,[[1,0,0],[2,1,1]])['signed_axis_spans'],
                         ['0','1','1'])

    def test_static_overlap_covers_full_interval(self):
        self.assertEqual(translation_box_window(self.box, self.box, [0, 0, 0])["candidate_fraction"],
                         ["0", "1"])

    def test_witness_fraction_and_starting_coincidence(self):
        self.assertEqual(shared_definition_coincidence(placement(), placement(2, 0, 3),
                         [4, 0, 6])["travel_fraction"], "1/2")
        self.assertEqual(shared_definition_coincidence(placement(), placement(),
                         [0, 0, 0])["travel_fraction"], "0")

    def test_wrong_offset_linear_matrix_or_travel(self):
        changed = placement(z=3)
        changed[0][0] = 2
        for fixed in [placement(y=1, z=3), placement(z=7), changed]:
            self.assertEqual(shared_definition_coincidence(placement(), fixed, [0, 0, 6])["result"],
                             "NO_COINCIDENCE_WITNESS")
        self.assertEqual(shared_definition_coincidence(placement(), placement(2, 0, 3),
                         [4, 0, 5])["result"], "NO_COINCIDENCE_WITNESS")

    def test_rejects_invalid_data(self):
        with self.assertRaises(ValueError):
            translation_box_window(self.box[::-1], self.box, [0, 0, 1])
        with self.assertRaises(ValueError):
            translation_box_window(self.box, self.box, [True, 0, 1])
        singular = placement()
        singular[0][0] = 0
        with self.assertRaises(ValueError):
            shared_definition_coincidence(singular, singular, [0, 0, 1])


class SourceSection(unittest.TestCase):
    def test_signed_travel_reverse_projection_and_reserve(self):
        from service_clearance import axial_section_window
        self.assertEqual(axial_section_window([0, 12], [2, 3], [-4, -1], clearance=0.25),
                         {'axial_gap_lower_bound': '0', 'source_section': ['11/4', '29/4']})

    def test_touch_at_first_or_last_and_narrow_miss(self):
        from service_clearance import axial_section_window
        result = axial_section_window([1, 2], [4, 5], [0, 1], clearance=1)
        self.assertEqual(result, {'axial_gap_lower_bound': '1', 'source_section': ['2', '2']})
        self.assertIsNone(axial_section_window([1, 2], [4, 5], [0, 0.5], clearance=1)['source_section'])
        with self.assertRaises(ValueError):
            axial_section_window([1, 2], [5, 4], [0, 1])


class EndpointAttribution(unittest.TestCase):
    def test_overlapping_candidate_definitions_do_not_identify_a_body(self):
        from assembly_verification import match_world_vertices
        def body(name, x):
            return dict(id=name, points=[[x,0,0]], face_count=4, closed=True)
        sources = [body('left', 0), body('right', 0)]
        saved = [body('one', 0), body('two', 0)]
        self.assertEqual(match_world_vertices(sources, saved, length_tolerance=0.01)['result'], 'PASS')
        proof = match_world_vertices(sources, saved, length_tolerance=0.01, require_unique_source=True)
        self.assertEqual(proof['result'], 'FAIL')
        self.assertEqual(proof['matches'], [])
        self.assertEqual(proof['unresolved_source_candidates'], {'one': ['left','right'], 'two': ['left','right']})
        sources[1], saved[1] = body('right', 1), body('two', 1)
        self.assertEqual(match_world_vertices(sources, saved, length_tolerance=0.01,
                                            require_unique_source=True)['result'], 'PASS')
