"""Synthetic regression cases for portable CAD helper extraction; no native writer."""
import copy
import hashlib
import json
import math
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock,patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))

from cadtools.geometry import Geometry, added
from cadtools.runtime import Client,Journal,CadError,Uncertain,new_owned_document,owned_document,RecoveringClient,bounded_request_namespace
from cadtools.records import iter_records,read_stable_entity
from cadtools.checkpoints import write_stage_checkpoint,save_checkpoint
from feature_checks import circular_trim_stations,cylinder_pattern,cylinder_wall_checks,axial_datum_chain,circular_opening_edge_land,round_ended_slot_tangents
from feature_checks import concentric_through_keyway_section, perpendicular_through_bore
from step_placements import native_matrix,classify_hand,eye,apply
from assembly_occurrences import expand_occurrences,recover_insert_sequence,write_occurrence_tables
from planar_profiles import annular_seat_with_radial_slot,round_ended_slot_profile,clip_circular_openings,bounded_extrusion,conservative_tool_polygon,two_circle_tangent_hull,two_circle_band_box_clearance
from plate_reference import build_plate,countersink_tool_profile,cylinder_cutter,cut_sidewalls,verify_plate,validate_outline,matching_countersink_fit
from native_views import sample,render_views,boundary_curves,placed_boundaries,xy_polyline_view_curves
from source_vector_paths import parse_path,page_point,local_point,cubic_point
from native_geometry import wcs_polyline_vertices,wcs_straight_polyline_segments,sat_structure,placed_circular_cylinders
from ocs_document_cleanup import cleanup_owned_documents
from retained_artifacts import verify_manifest
from assembly_verification import compare_axial_occurrences,directed_axial_span


class IndexedFitTests(unittest.TestCase):
    def test_moving_carrier_and_fixed_lock_at_two_settings(self):
        from assembly_verification import check_index_translation
        before = {name: eye() for name in ('carrier', 'lock', 'frame')}
        after = copy.deepcopy(before)
        for name in ('carrier', 'lock'):
            after[name][2][3] = -4
        def check():
            return check_index_translation(before, after, ['carrier', 'lock'], offset_mm=[0,0,-4],
                                           length_tolerance=.01, linear_tolerance=.0001)
        self.assertEqual(check()['result'], 'PASS')
        after['lock'][2][3] = 0
        self.assertEqual(check()['result'], 'FAIL')
        after['lock'][2][3] = -4
        after['frame'][0][0] = -1
        self.assertEqual(check()['result'], 'FAIL')
        del after['frame']
        with self.assertRaises(ValueError):
            check()

    def test_index_position_error_against_inclusive_tolerance(self):
        from assembly_verification import check_index_translation
        before = {'slide': eye(), 'frame': eye()}
        after = copy.deepcopy(before)
        for measured, error, expected in ((.005, 0, 'PASS'), (0, .005, 'PASS'),
                                          (-.005, .01, 'PASS'), (.025, .02, 'FAIL')):
            with self.subTest(measured=measured):
                after['slide'][0][3] = measured
                result = check_index_translation(before, after, ['slide'], offset_mm=[.005,0,0],
                                                 length_tolerance=.01, linear_tolerance=.0001)
                self.assertEqual(result['result'], expected)
                slide = next(row for row in result['checks'] if row['occurrence']=='slide')
                self.assertEqual(slide['measured_displacement_mm'], [measured,0,0])
                self.assertAlmostEqual(slide['position_error_mm'], error)
        after['slide'][0][3] = .005
        after['frame'][0][3] = 2
        self.assertEqual(check_index_translation(before, after, ['slide'], offset_mm=[.005,0,0],
                         length_tolerance=.01, linear_tolerance=.0001)['result'], 'FAIL')

    def test_seat_interference_both_head_directions(self):
        from plate_reference import pin_seat_relief
        for sign in (-1, 1):
            def plan(seat):
                return pin_seat_relief(shank_radius=4, bore_radius=4.2, head_radius=6,
                                       shoulder_station=sign*2, outer_station=sign*4,
                                       seat_station=sign*seat, axis_sign=sign)
            self.assertEqual(plan(2.25)['depth_mm'], .25)
            self.assertEqual(plan(2.25)['radial_span_mm'], [4, 6])
            self.assertEqual(plan(2.25)['remaining_head_mm'], 1.75)
            self.assertEqual(plan(2)['action'], 'retain')
            self.assertEqual(plan(1)['seat_gap_mm'], 1)
            with self.assertRaises(ValueError):
                plan(4)


class RoundEndedSlotTangents(unittest.TestCase):
    def test_both_faces_require_continuous_straight_tangents(self):
        edges = [dict(curve_type='straight-curve', points=[[x,10,z],[x,0,z]])
                 for z in (0,2) for x in (-3,3)]
        options = dict(axis=2,centres=[[0,0],[0,10]],radius=3,stations=[0,2],tolerance=.001)
        self.assertEqual(round_ended_slot_tangents('slot',edges,**options)['result'],'PASS')
        edges[-1]['curve_type'] = 'ellipse-curve'
        proof = round_ended_slot_tangents('slot',edges,**options)
        self.assertEqual(proof['result'],'FAIL')
        self.assertEqual(sum(line['passed'] for line in proof['tangents']),3)


class TwoCircleTangentHull(unittest.TestCase):
    def test_tangent_and_arc_endpoints_for_unequal_and_equal_radii(self):
        a, b = (4, -3), (10, 5)
        for ra, rb in ((5, 2), (2, 5), (4, 4)):
            with self.subTest(radii=(ra, rb)):
                points, bulges = two_circle_tangent_hull(a, b, ra, rb)
                self.assertEqual(set(bulges), {1, 2, 4, 5})
                self.assertAlmostEqual(8 * (math.atan(bulges[1]) + math.atan(bulges[4])), 2 * math.pi)
                for ia, ib in ((0, 1), (4, 3)):
                    pa, pb = points[ia], points[ib]
                    self.assertAlmostEqual(math.dist(a, pa), ra)
                    self.assertAlmostEqual(math.dist(b, pb), rb)
                    tangent = [v - u for u, v in zip(pa, pb, strict=True)]
                    for p, c in ((pa, a), (pb, b)):
                        self.assertAlmostEqual(sum(t * (x - y) for t, x, y in zip(tangent, p, c, strict=True)), 0)

    def test_rejects_nested_and_coincident_circles(self):
        for other in ((0, 0), (3, 0), (2, 0)):
            with self.subTest(other=other), self.assertRaises(ValueError):
                two_circle_tangent_hull((0, 0), other, 5, 2)

    def test_band_certifies_inner_and_outer_separation_only(self):
        args = (((0,0),(10,0)), (3,2), (4,3))
        inner = two_circle_band_box_clearance(((-1,-1),(1,1)),*args)
        self.assertEqual(inner['result'],'INSIDE_INNER_HULL')
        self.assertAlmostEqual(inner['gap_lower_bound'],3-math.sqrt(2))
        outside = two_circle_band_box_clearance(((13.5,-.25),(14,.25)),*args)
        self.assertEqual(outside,dict(result='OUTSIDE_OUTER_HULL',gap_lower_bound=.5))
        crossing = two_circle_band_box_clearance(((-.2,2.9),(.2,3.2)),*args)
        self.assertEqual(crossing,dict(result='CANDIDATE',gap_lower_bound=None))
        tangent = two_circle_band_box_clearance(((13,0),(14,0)),*args)
        self.assertEqual(tangent['result'],'CANDIDATE')


class ConcentricThroughKeyway(unittest.TestCase):
    def test_section_uses_bore_intersection_and_farthest_floor_corner(self):
        section = concentric_through_keyway_section(10, 20, 6, 2)
        self.assertEqual(section['half_width'], 3)
        self.assertEqual(section['mouth_from_axis'], 4)
        self.assertEqual(section['floor_from_axis'], 7)
        self.assertAlmostEqual(section['minimum_radial_wall'], 10-math.sqrt(58))

    def test_signed_remaining_wall_distinguishes_tangency_from_breakout(self):
        self.assertEqual(concentric_through_keyway_section(7, 10, 6, 0.5)['minimum_radial_wall'], 0)
        self.assertLess(concentric_through_keyway_section(8, 10, 6, 0.5)['minimum_radial_wall'], 0)

    def test_rejects_invalid_opening_dimensions(self):
        for inputs in ((10, 20, 10, 1), (10, 10, 5, 1), (10, 20, 5, -1),
                       (True, 20, 5, 1), (10, math.inf, 5, 1)):
            with self.subTest(dimensions=inputs), self.assertRaises(ValueError):
                concentric_through_keyway_section(*inputs)


class BoundedRequestNamespace(unittest.TestCase):
    def test_preserves_valid_existing_namespace(self):
        self.assertEqual(bounded_request_namespace('a'*64), 'a'*64)
        with self.assertRaises(CadError):
            bounded_request_namespace('')

    def test_shortens_utf8_without_cutting_a_character(self):
        original='fixture-'+'ø'*40
        namespace=bounded_request_namespace(original)
        self.assertLessEqual(len(namespace.encode('utf-8')),64)
        self.assertEqual(namespace,bounded_request_namespace(original))
        self.assertNotEqual(namespace,bounded_request_namespace(original+'-close'))

    def test_shared_prefix_keeps_distinct_request_namespaces(self):
        label='assembly-'*12
        self.assertNotEqual(bounded_request_namespace(label+'-save'),bounded_request_namespace(label+'-close'))


class DirectedAxialSpan(unittest.TestCase):
    def test_opposite_hands_share_outward_span(self):
        origin = [2,3,4]
        left = [[2,8,5],[2,13,5]]
        right = [[2,-2,5],[2,-7,5]]
        self.assertEqual(directed_axial_span(left,origin=origin,direction=[0,1,0]),[5,10])
        self.assertEqual(directed_axial_span(right,origin=origin,direction=[0,-1,0]),[5,10])

    def test_oblique_unit_and_negative_station(self):
        actual = directed_axial_span([[1,1,0],[-2,-2,0]],origin=[0,0,0],
                                     direction=[math.sqrt(.5),math.sqrt(.5),0])
        self.assertAlmostEqual(actual[0],-2*math.sqrt(2))
        self.assertAlmostEqual(actual[1],math.sqrt(2))

    def test_requires_observations_and_explicit_unit_direction(self):
        with self.assertRaises(ValueError):
            directed_axial_span([],origin=[0,0,0],direction=[1,0,0])
        with self.assertRaises(ValueError):
            directed_axial_span([[1,0,0]],origin=[0,0,0],direction=[2,0,0])


class AxialOccurrenceComparison(unittest.TestCase):
    def setUp(self):
        self.baseline = [
            dict(occurrence='first', role='spacer', axis_xy_mm=[10, 20], span_z_mm=[5, 9]),
            dict(occurrence='second', role='spacer', axis_xy_mm=[10, 20], span_z_mm=[5, 9]),
        ]

    def test_distinct_occurrences_can_share_an_axis(self):
        result = compare_axial_occurrences(self.baseline, list(reversed(self.baseline)), length_tolerance=.001)
        self.assertEqual(result['result'], 'PASS')
        self.assertEqual(len(result['checks']), 2)

    def test_reports_identity_role_axis_and_span_changes(self):
        updated = [
            dict(occurrence='first', role='washer', axis_xy_mm=[10, 22], span_z_mm=[6, 9]),
            dict(occurrence='third', role='spacer', axis_xy_mm=[10, 20], span_z_mm=[5, 9]),
        ]
        result = compare_axial_occurrences(self.baseline, updated, length_tolerance=.001)
        self.assertEqual(result['result'], 'FAIL')
        self.assertEqual(result['missing_occurrences'], ['second'])
        self.assertEqual(result['added_occurrences'], ['third'])
        self.assertEqual(result['checks'], [dict(occurrence='first', axis_error_mm=2.0,
                                                  span_error_mm=1.0, role_matches=False, passed=False)])

    def test_duplicate_occurrence_names_are_invalid(self):
        with self.assertRaises(ValueError):
            compare_axial_occurrences(self.baseline, self.baseline[:1]*2, length_tolerance=.001)


class CircularOpeningEdgeLand(unittest.TestCase):
    def test_keeps_signed_near_and_far_lands_after_asymmetric_resize(self):
        self.assertEqual(circular_opening_edge_land(3, 2, (-2, 6)),
                         dict(low=3, high=1, minimum=1))
        self.assertEqual(circular_opening_edge_land(103, 2, (98, 106)),
                         dict(low=3, high=1, minimum=1))

    def test_retains_tangency_and_breakout(self):
        self.assertEqual(circular_opening_edge_land(3, 3, (-2, 6))['minimum'], 0)
        self.assertEqual(circular_opening_edge_land(3, 4, (-2, 6))['minimum'], -1)

    def test_rejects_invalid_geometry(self):
        for inputs in ((3, 0, (-2, 6)), (3, 1, (6, -2)), (math.nan, 1, (-2, 6)),
                       (3, True, (-2, 6)), (3, 1, (6,))):
            with self.subTest(inputs=inputs), self.assertRaises(ValueError):
                circular_opening_edge_land(*inputs)


class AnnularSeatWithRadialSlot(unittest.TestCase):
    def test_retained_seat_matches_independent_midpoint_quadrature(self):
        result=annular_seat_with_radial_slot(10,20,4,12)
        dx=4/2000
        clipped=sum((12-math.sqrt(100-(-2+(i+.5)*dx)**2))*dx for i in range(2000))
        self.assertAlmostEqual(result['removed_area_mm2'],clipped,places=6)
        self.assertAlmostEqual(result['projected_overlap_mm2'],300*math.pi-clipped,places=6)
        for bad in ((10,20,4,9),(10,20,4,20),(10,20,20,12)):
            with self.subTest(parameters=bad),self.assertRaises(ValueError):
                annular_seat_with_radial_slot(*bad)


class RoundEndedSlotProfile(unittest.TestCase):
    def test_slot_ends_are_semicircles_inside_supplied_span(self):
        from ezdxf.math import bulge_to_arc

        points, bulges = round_ended_slot_profile(6, 10, 31)
        self.assertEqual(set(bulges),{0,2})
        bottom, start, end, low_radius = bulge_to_arc(points[0],points[1],bulges[0])
        top, a, b, high_radius = bulge_to_arc(points[2],points[3],bulges[2])
        self.assertAlmostEqual(bottom.y-low_radius,10)
        self.assertAlmostEqual(top.y+high_radius,31)
        self.assertAlmostEqual(low_radius,3)
        self.assertAlmostEqual(high_radius,3)
        self.assertEqual([p[0] for p in points],[-3,3,3,-3])
        for end_station in (10,16):
            with self.subTest(end=end_station), self.assertRaises(ValueError):
                round_ended_slot_profile(6,10,end_station)


class AxialDatumChain(unittest.TestCase):
    def test_source_lengths_bind_to_independent_axial_steps(self):
        result = axial_datum_chain('step and tip',[9,12,20],[3,8],.001)
        self.assertEqual(result['result'],'PASS')
        self.assertEqual(result['observed'],[3,8])
        self.assertEqual(axial_datum_chain('opposite hand',[-9,-12,-20],[-3,-8],.001)['result'],'PASS')
        self.assertEqual(axial_datum_chain('wrong tip datum',[9,12,17],[3,8],.001)['result'],'FAIL')
        with self.assertRaises(ValueError):
            axial_datum_chain('missing datum',[9,20],[3,8],.001)


class CircularTrimStations(unittest.TestCase):
    def test_entry_and_end_pass_only_with_distributed_native_samples(self):
        def ring(y):
            return [(4*math.cos(i*math.tau/16),y,4*math.sin(i*math.tau/16)) for i in range(16)]
        options = dict(axis=1,centres=[(0,0)],radius=4,stations=[0,8],tolerance=1e-6)
        entry, bottom = ring(0), ring(8)
        self.assertEqual(circular_trim_stations('Ring pair',entry+bottom,**options)['result'],'PASS')
        for short in (entry, entry+bottom[:8], entry+[bottom[0]]*16, entry+ring(9)):
            with self.subTest(points=len(short)):
                self.assertEqual(circular_trim_stations('Short ring',short,**options)['result'],'FAIL')


class GeometryAdapterContract(unittest.TestCase):
    def test_cone_binds_base_radius_height_and_returns_native_handle(self):
        client = Mock()
        client.mutate.return_value = {'changes':[{'kind':'Added','handle':'C1'}]}
        geom = Geometry(client)
        self.assertEqual(geom.cone('point tool',[0,0,5],2.5,3.0),'C1')
        client.mutate.assert_called_once_with('point tool','run',cmd='CONE 0,0,5 2.5 3.0')
        with self.assertRaisesRegex(CadError,'Positive dimension required'):
            geom.cone('invalid',[0,0,5],2.5,0)
        self.assertEqual(client.mutate.call_count,1)


    def test_cylinder_handle_and_raw_command_response_have_distinct_types(self):
        response = {'changes': [{'kind': 'Added', 'handle': 'A2'}]}
        client = Mock()
        client.mutate.return_value = response
        handle = Geometry(client).cylinder('stock', [0, 0, 0], 5, 7)
        self.assertEqual(added(response), handle)
        with self.assertRaisesRegex(CadError, 'use a geometry helper'):
            added(handle)
        client.mutate.assert_called_once()


    def union_client(self, changes, live, *, response_revision=7, selected=("A1","A2")):
        client = Mock(document_id=1)
        current = dict(ok=True, document_id=1, revision=7, geometry_revision=45)
        client.mutate.side_effect = [{"state": {"selection": list(selected)}}, {"changes": changes, "state": dict(current, revision=response_revision)}]

        def read(op, **fields):
            if op == "state":
                return current
            self.assertEqual(op, "records")
            self.assertEqual(fields["collection"], "entities")
            self.assertLessEqual(len(fields["handles"]), 3)
            return {"records": [live[handle] for handle in fields["handles"] if handle in live]}

        client.read.side_effect = read
        return client

    def test_union_reads_high_result_handle_in_a_large_drawing(self):
        live = {f"{i:X}": dict(handle=f"{i:X}", type="Solid3D") for i in range(0x100, 0x1000)}
        for consumed in ("FF0", "FF5"):
            del live[consumed]
        changes = [dict(kind="Added", handle="FF9"),
                   dict(kind="Removed", handle="FF0"), dict(kind="Removed", handle="FF5")]
        client = self.union_client(changes, live, selected=("FF0","FF5"))
        self.assertEqual(Geometry(client).combine("union", ["FF0", "FF5"]), "FF9")
        client.read.assert_any_call("records", collection="entities", offset=0, limit=8,
                                    handles=["FF0", "FF5", "FF9"])

    def test_union_returns_exact_surviving_original_and_rejects_ambiguity(self):
        live = {"A1": dict(handle="A1", type="Solid3D")}
        changes = [dict(kind="Removed", handle="A2"), dict(kind="Modified", handle="A1")]
        self.assertEqual(Geometry(self.union_client(changes, live)).combine("union", ["A1", "A2"]), "A1")
        partial = self.union_client(changes, live, selected=("A1",))
        with self.assertRaisesRegex(CadError, "Union selection"):
            Geometry(partial).combine("union", ["A1", "A2"])
        self.assertEqual(partial.mutate.call_count, 1)
        result = [dict(kind="Added", handle="A3"), *changes]
        for invalid in (
                self.union_client(result, dict(live, A3=dict(handle="A3", type="Solid3D"))),
                self.union_client(result, live),
                self.union_client([], live),
                self.union_client(changes[:1], live),
                self.union_client([*changes, dict(kind="Removed", handle="unrelated")], live),
                self.union_client(changes, {"A1": dict(handle="A1", type="Line")}),
                self.union_client(changes, live, response_revision=6)):
            with self.subTest(readback=invalid), self.assertRaisesRegex(CadError, "Union result"):
                Geometry(invalid).combine("union", ["A1", "A2"])


class Patterns(unittest.TestCase):
    def features(self,points,radius=3):
        return {'cylinders':[dict(radius=radius,axis=[0,1,0],origin=[x,0,y]) for x,y in points]}
    def check(self,points,expected,**kw):return cylinder_pattern('pattern',self.features(points,**kw),6,1,expected,1e-6)
    def test_exact_equal_x_failure_witness(self):
        expected=[[-126.03073792140916,298.7979856674331],[-126.03073792140916,367.2020143325669],[-120,333]]
        observed=[[-126.03073792190915,367.2020143325669],[-126.03073792090916,298.7979856674331],[-120,333]]
        self.assertGreater(abs(sorted(observed)[0][1]-sorted(expected)[0][1]),60)
        result=self.check(observed,expected);self.assertEqual(result['result'],'PASS');self.assertEqual(len(result['matched_pairs']),3)
    def test_patch_deduplication_and_axis_sign(self):
        f=self.features([[1,2],[1,2]]);f['cylinders'][1]['axis']=[0,-1,0]
        self.assertEqual(cylinder_pattern('p',f,6,1,[[1,2]],1e-6)['result'],'PASS')
    def test_missing_extra_radius_and_direction(self):
        for points in ([],[[0,0],[2,2]]):self.assertEqual(self.check(points,[[0,0]])['result'],'FAIL')
        self.assertEqual(self.check([[0,0]],[[0,0]],radius=3.1)['result'],'FAIL')
        f=self.features([[0,0]]);f['cylinders'][0]['axis']=[1,0,0]
        self.assertEqual(cylinder_pattern('p',f,6,1,[[0,0]],1e-6)['result'],'FAIL')
    def test_inclusive_tolerance_and_ambiguity(self):
        self.assertEqual(self.check([[1e-6,0]],[[0,0]])['result'],'PASS')
        self.assertEqual(self.check([[1.000001e-6,0]],[[0,0]])['result'],'FAIL')
        self.assertEqual(self.check([[-.9e-6,0],[.9e-6,0]],[[0,0],[1.5e-6,0]])['result'],'FAIL')
    def test_nonfinite_observation(self):
        with self.assertRaises(ValueError):self.check([[math.nan,0]],[[0,0]])
    def test_actual_wall_vertices(self):
        face=dict(surface_type='cone-surface',support=dict(radius=2,axis=[1,0,0],origin=[0,0,0]),loops=[dict(edges=[dict(endpoints=[[5,2,0],[3,2,0]])])])
        args=dict(axis=0,centre=[0,0],radius=2,side=1,outer=5,inner_limit=3,tolerance=1e-6)
        self.assertEqual(cylinder_wall_checks('wall',[face],**args)['result'],'PASS')
        face['loops'][0]['edges'][0]['endpoints'][1]=[4,2,0]
        self.assertEqual(cylinder_wall_checks('wall',[face],**args)['result'],'FAIL')


class Records(unittest.TestCase):
    def client(self):
        c=SimpleNamespace(document_id=1)
        c.calls=[];state=dict(ok=True,document_id=1,revision=3,geometry_revision=4)
        def read(op,**fields):
            c.calls.append((op,fields))
            if op=='state':return state.copy()
            if fields['limit']>2:raise CadError('OCS response exceeds 16 MiB; query a narrower scope')
            offset=fields['offset'];return dict(records=[dict(handle=str(i)) for i in range(offset,min(offset+2,3))],next_offset=2 if offset==0 else None,**state)
        c.read=read
        return c
    def test_reduces_limit_without_advancing_offset(self):
        c=self.client();self.assertEqual([r['handle'] for r in iter_records(c,'entities')],['0','1','2'])
        self.assertEqual([(f['offset'],f['limit']) for op,f in c.calls if op=='records'],[(0,8),(0,4),(0,2),(2,2)])
    def test_single_record_oversize_fails(self):
        c=self.client();c.read=Mock(side_effect=lambda op,**kw:dict(ok=True,document_id=1,revision=1,geometry_revision=1) if op=='state' else (_ for _ in ()).throw(ValueError('response exceeds 16 MiB')))
        with self.assertRaises(ValueError):list(iter_records(c,'entities',page_size=1))
    def test_duplicate_and_nonprogressing_offset(self):
        for response in [dict(records=[dict(handle='a')],next_offset=0),dict(records=[dict(handle='a'),dict(handle='a')],next_offset=None)]:
            c=self.client();c.read=lambda op,**kw:dict(ok=True,document_id=1,revision=1,geometry_revision=1) if op=='state' else response
            with self.assertRaises(CadError):list(iter_records(c,'entities'))
    def test_external_activation_during_read_stops(self):
        c=self.client();old=c.read;calls=[0]
        def read(op,**kw):
            if op=='state':
                calls[0]+=1
                if calls[0]>2:return dict(ok=True,document_id=2,revision=3,geometry_revision=4)
            return old(op,**kw)
        c.read=read
        with self.assertRaises(CadError):list(iter_records(c,'entities',page_size=2))


class Ownership(unittest.TestCase):
    def test_proxy_uses_one_total_query_budget(self):
        with tempfile.TemporaryDirectory() as tmp:
            h=Mock();h.READ_OPS={'state'}
            h.request.side_effect=lambda d,p,t:dict(ok=True,document_id=1,revision=0) if p['op']=='state' else dict(ok=True,status='running')
            h.execute_checked.return_value=dict(ok=True,status='running')
            c=Client(h,{'session_id':'s'},1,'job',Journal(Path(tmp)/'journal'),allow_write=True,max_queries=2)
            with self.assertRaises(Uncertain):RecoveringClient(c).mutate('one','run',cmd='BOX')
            self.assertEqual(sum(call.args[1]['op']=='operation' for call in h.request.call_args_list),2)
            self.assertEqual(h.execute_checked.call_count,1)
    def test_waiting_input_and_definitive_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            h=Mock();c=Client(h,{'session_id':'s'},1,'job',Journal(Path(tmp)/'journal'))
            response=dict(ok=True,status='waiting_input')
            self.assertEqual(c._finish('key',response,True),response)
            with self.assertRaises(CadError):c._finish('key',response,False)
            with self.assertRaises(CadError):c._finish('key',dict(ok=False,status='failed'),True)
            h.request.assert_not_called()
    def test_new_binding_and_restart_use_original_intent(self):
        with tempfile.TemporaryDirectory() as tmp:
            h=Mock();h.READ_OPS={'state'};state=dict(ok=True,document_id=1,revision=0,geometry_revision=0,documents=[dict(id=1,path=None)])
            def request(d,payload,timeout):return state.copy() if payload['op']=='state' else dict(ok=True,status='completed',state=dict(document_id=2))
            h.request.side_effect=request
            def execute(*args,**kw):
                state.update(document_id=2,documents=[dict(id=1,path=None),dict(id=2,path=None)])
                return dict(ok=True,status='completed',state=dict(document_id=2))
            h.execute_checked.side_effect=execute
            c=Client(h,{'session_id':'s'},1,'job',Journal(Path(tmp)/'journal'),allow_write=True)
            new_owned_document(c);self.assertEqual(c.document_id,2)
            restart=Client(h,{'session_id':'s'},2,'job',Journal(Path(tmp)/'journal'),allow_write=True)
            new_owned_document(restart)
            self.assertEqual(h.execute_checked.call_count,1)
            self.assertEqual([x.args[1]['document_id'] for x in h.request.call_args_list if x.args[1]['op']=='operation'],[1])
    def test_pending_open_recovery_preserves_poll_interval_and_deadline(self):
        with tempfile.TemporaryDirectory() as tmp, patch('cadtools.runtime.time.sleep') as wait:
            helper = Mock()
            journal = Journal(Path(tmp) / 'journal')
            source = str(Path(tmp) / 'assembly.dwg')
            key = 'job:open-model'
            journal.intent(dict(op='open', path=source, request_id=key, document_id=1, revision=0),
                           dict(session_id='s', document_id=1))
            helper.request.side_effect = [
                dict(ok=True, status='running'),
                dict(ok=True, status='completed', state=dict(document_id=2)),
                dict(ok=True, document_id=2, geometry_revision=3, documents=[dict(id=2, path=source)]),
            ]
            client = Client(helper, {'session_id':'s'}, 1, 'job', journal, allow_write=True,
                            timeout=60, max_queries=2, poll_interval=.75, recovery_deadline=5)
            owned_document(client, 'open-model', 'open', path=source)
            wait.assert_called_once_with(.75)
            self.assertEqual(client.document_id, 2)
            self.assertLessEqual(helper.request.call_args_list[1].args[2], 5)
            self.assertEqual([call.args[1]['request_id'] for call in helper.request.call_args_list[:2]],
                             [key,key])
            helper.execute_checked.assert_not_called()

    def test_new_response_never_adopts_foreign_active_document(self):
        c=Mock();c.namespace='job';c.document_id=1;c.journal.requests={};c.timeout=1
        c.mutate.return_value=dict(ok=True,status='completed',state=dict(document_id=2))
        c.helper.request.return_value=dict(ok=True,document_id=3,documents=[dict(id=3,path=None)])
        with self.assertRaises(CadError):new_owned_document(c)
        self.assertEqual(c.document_id,1)


class Checkpoints(unittest.TestCase):
    def test_order_job_identity_and_previous_file_survive_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'state.json'
            write_stage_checkpoint(p,'job','pre_save',dict(result='PASS'));before=p.read_bytes()
            for job,stage,payload in [('other','save_reopen',{}),('job','reopened',{}),('job','save_reopen',{'bad':math.nan})]:
                with self.assertRaises((ValueError,CadError)):write_stage_checkpoint(p,job,stage,payload)
                self.assertEqual(p.read_bytes(),before)
            write_stage_checkpoint(p,'job','save_reopen',{});write_stage_checkpoint(p,'job','reopened',{})
            self.assertEqual(list(json.loads(p.read_text())['stages']),['pre_save','save_reopen','reopened'])
    def test_native_progress_save_verifies_file_without_reopen(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'progress.dwg';receipt=Path(tmp)/'progress.json';journal=SimpleNamespace(requests={})
            state=dict(ok=True,document_id=1,revision=0,geometry_revision=5,command=None,modal=None)
            manifest={'by_type':{'3D Solid':1}}
            c=Mock();c.namespace='job';c.journal=journal;c.document_id=1
            c.read.side_effect=lambda op,**kw:state.copy() if op=='state' else dict(document_id=1,summary={'errors':0,'warnings':0},manifest=manifest)
            def mutate(label,op,**kw):
                audit_requests = [request.kwargs for request in c.read.call_args_list if request.args == ("audit",)]
                self.assertEqual(audit_requests, [{"path": str(path), "target_format": "dwg", "target_version": "2018"}])
                self.assertEqual(kw["path"], str(path))
                path.write_bytes(b'native transport fixture')
                return dict(result=dict(saved=str(path),verified=True,dropped_on_save=0,manifest=manifest,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
            c.mutate.side_effect=mutate
            result=save_checkpoint(c,path,label='stage-1',expected_counts={'3D Solid':1},receipt_path=receipt,roots={'JOB_ROOT':Path(tmp)})
            self.assertEqual(result['state'],'IN_PROGRESS');self.assertEqual(json.loads(receipt.read_text())['sha256'],result['sha256'])
            self.assertNotIn(tmp,receipt.read_text())
            self.assertEqual(c.mutate.call_args.args[1],'save_verified');self.assertEqual(c.mutate.call_count,1)
            with self.assertRaises(CadError):save_checkpoint(c,path,label='stage-2',expected_counts={'3D Solid':1})


class Assemblies(unittest.TestCase):
    def props(self):return dict(normal=dict(x=0,y=0,z=1),rotation=math.pi/2,insert_point=dict(x=3,y=4,z=5),x_scale=1,y_scale=-1,z_scale=1)
    def test_reflection_opt_in_and_rigid_matrix_validation(self):
        p=self.props()
        with self.assertRaises(ValueError):native_matrix(p)
        m=native_matrix(p,allow_unit_reflection=True);self.assertEqual(classify_hand(m),'MIRRORED')
        self.assertEqual([round(v,6) for v in apply(m,[0,1,0])],[4,4,5])
        shear=eye();shear[0][1]=1
        with self.assertRaises(ValueError):classify_hand(shear)
        p['insert_point']['x']=math.nan
        with self.assertRaises(ValueError):native_matrix(p,allow_unit_reflection=True)
    def groups(self):
        leaf=dict(name='part',source='part',source_sha256='a'*64,yscale=-1)
        return {'root':dict(sha256='c'*64,children=[dict(name='sub',source='sub',source_sha256='b'*64),dict(name='other',source='sub',source_sha256='b'*64,yscale=-1)]),'sub':dict(sha256='b'*64,children=[leaf])}
    def test_repeated_nested_group_keeps_occurrences_and_reflection_parity(self):
        r=expand_occurrences('root',self.groups());self.assertEqual(len(r['occurrences']),2)
        self.assertEqual({q['hand'] for q in r['quantities']},{'SOURCE_HAND','MIRRORED'})
        with tempfile.TemporaryDirectory() as tmp:
            tables=write_occurrence_tables(tmp,'assembly',r)
            self.assertEqual(tables['instances']['rows'],2)
            original=Path(tables['parts']['path']).read_bytes()
            with self.assertRaises(ValueError):write_occurrence_tables(tmp,'assembly',r)
            self.assertEqual(Path(tables['parts']['path']).read_bytes(),original)
    def test_cycle_stale_insert_hash_and_bounds_rejected(self):
        groups=self.groups();groups['sub']['sha256']='d'*64
        with self.assertRaises(ValueError):expand_occurrences('root',groups)
        with self.assertRaises(ValueError):expand_occurrences('root',self.groups(),max_occurrences=1)
        groups=self.groups();groups['sub']['children']=[dict(name='back',source='root',source_sha256='c'*64)]
        with self.assertRaises(ValueError):expand_occurrences('root',groups)
    def test_recover_completed_insert_and_reject_conflicting_response(self):
        events=[];digest='a'*64;values=dict(file={'text':'part.dwg'},point={'point':[1,2,3]},xscale={'text':'1'},yscale={'text':'-1'},rotation={'text':'0'},provenance={'data':[dict(code=1000,value='Source DWG SHA256 '+digest)]})
        for name,value in values.items():
            key='j:member-0-'+name;events.extend([dict(event='intent',request=dict(request_id=key,**value)),dict(event='response',request_id=key,response=dict(ok=True,status='completed'))])
        self.assertEqual(recover_insert_sequence(events,prefix='j',count=1,source_digest=lambda p:digest)[0]['yscale'],-1)
        events.append(dict(event='response',request_id='j:member-0-rotation',response=dict(ok=True,status='completed',result={'different':True})))
        with self.assertRaises(ValueError):recover_insert_sequence(events,prefix='j',count=1,source_digest=lambda p:digest)


class Profiles(unittest.TestCase):
    def test_tool_reduction_checks_containment_vertex_budget_and_enlargement(self):
        source = Mock(geom_type='Polygon',is_valid=True,is_empty=False,interiors=[],area=4.)
        tool = Mock(geom_type='Polygon',is_valid=True,is_empty=False,interiors=[],area=4.2)
        tool.exterior.coords = [[0,0],[2,0],[2,2],[0,2],[0,0]]
        tool.covers.return_value = True
        source.buffer.return_value.simplify.return_value = tool
        settings = dict(margin=.04,tolerance=.01,max_vertices=4,max_added_area=.25)
        self.assertIs(conservative_tool_polygon(source,**settings),tool)
        source.buffer.assert_called_once_with(.04,quad_segs=2)
        tool.covers.assert_called_once_with(source)
        tool.covers.return_value = False
        with self.assertRaisesRegex(ValueError,'fully contain'):
            conservative_tool_polygon(source,**settings)
        tool.covers.return_value = True
        with self.assertRaisesRegex(ValueError,'vertex limit'):
            conservative_tool_polygon(source,**dict(settings,max_vertices=3))
        with self.assertRaisesRegex(ValueError,'area growth'):
            conservative_tool_polygon(source,**dict(settings,max_added_area=.1))

    def test_tube_subtraction_requires_explicit_overrun_before_writes(self):
        from rounded_tube import construct
        c=Mock()
        with patch('rounded_tube.dimensions',return_value={}):
            with self.assertRaises(ValueError):construct(c,{},route='solid-subtract')
        c.mutate.assert_not_called()
    def test_bounded_extrusion_deletes_only_its_own_profiles(self):
        c=Mock();c.read.side_effect=[dict(entities=[dict(handle='OLD',type='3D Solid')]),dict(entities=[dict(handle='OLD',type='3D Solid'),dict(handle='PROFILE',type='Polyline'),dict(handle='BODY',type='3D Solid')])]
        g=Mock();g.profile.return_value='PROFILE'
        with patch('planar_profiles.Geometry',return_value=g):
            r=bounded_extrusion(c,[dict(points=[[0,0],[4,0],[4,4],[0,4]])],[1,1,0],2,label='stock')
        self.assertEqual(r['body'],'BODY')
        self.assertEqual(c.mutate.call_args_list[-1].kwargs['handles'],['PROFILE'])
        self.assertNotIn('OLD',c.mutate.call_args_list[-1].kwargs['handles'])
    def test_internal_circular_opening_exact_area(self):
        loops=clip_circular_openings([[-5,-5],[5,-5],[5,5],[-5,5]],[[0,0]],2,tolerance=1e-8)
        self.assertEqual(len(loops),2);self.assertAlmostEqual(sum(x['signed_area_mm2'] for x in loops),100-4*math.pi)
        self.assertEqual({x['boundary_role'] for x in loops},{'outer','opening'})
        hole=next(x for x in loops if x['boundary_role']=='opening')
        points,bulges=validate_outline(hole['points_mm'],hole['bulges'])
        self.assertGreaterEqual(len(points),3)
        for point in points:self.assertAlmostEqual(math.hypot(*point),2)
    def test_clipped_overlapping_circles_and_duplicate_rejection(self):
        loops=clip_circular_openings([[-5,-5],[5,-5],[5,5],[-5,5]],[[4,-1],[4,1]],2,tolerance=1e-8)
        self.assertTrue(loops);self.assertLess(sum(x['signed_area_mm2'] for x in loops),100)
        with self.assertRaises(ValueError):clip_circular_openings([[0,0],[5,0],[5,5],[0,5]],[[1,1],[1,1]],1,tolerance=1e-8)
    def test_plate_preflight_fails_before_writes(self):
        c=Mock();spec=dict(outline=[[0,0],[3,0],[3,3],[0,3]],sketch_bounds=[[0,3],[0,3],[0,1]],cutter_overrun_mm=1,holes=[dict(axis=5,diameter=1,centres=[[1,1]])])
        with self.assertRaises(ValueError):build_plate(c,spec)
        c.mutate.assert_not_called()
    def test_axis_cutter_transforms_and_wall_intervals(self):
        g=Mock();g.cylinder.return_value='solid'
        cylinder_cutter(g,'cut',0,[2,3],4,[0,5],1)
        g.cylinder.assert_called_once_with('cut',[-3,2,-1],2,7);g.rotate.assert_called_once_with('cut-axis',['solid'],'Y',90)
        c=Mock()
        with self.assertRaises(ValueError):cut_sidewalls(c,'body',axis=0,centre=[0,0],diameter=2,intervals=[[0,3],[2,4]],label='cut')
        c.mutate.assert_not_called()

    def test_sidewall_stages_preserve_tool_and_result_handles(self):
        c=Mock()
        g=Mock()
        g.cylinder.side_effect=['left','right']
        checkpoint=Mock()
        with patch('plate_reference.Geometry',return_value=g):
            result=cut_sidewalls(c,'body',axis=0,centre=[-2,140],diameter=30,
                                 intervals=[[-26,-19],[19,26]],label='cut',checkpoint=checkpoint)
        self.assertEqual(result,'body')
        self.assertEqual([call.args for call in checkpoint.call_args_list], [
            ('cut-0-cutter',('body','left')), ('cut-0-aligned',('body','left')), ('cut-0-wall',('body',)),
            ('cut-1-cutter',('body','right')), ('cut-1-aligned',('body','right')), ('cut-1-wall',('body',)),
        ])
        self.assertEqual([call.args[1:] for call in g.subtract.call_args_list],
                         [('body',['left']),('body',['right'])])

    def test_sidewall_failed_alignment_save_stops_before_cut(self):
        c=Mock()
        g=Mock()
        g.cylinder.return_value='cutter'
        def checkpoint(stage, handles):
            if stage.endswith('-aligned'):
                raise OSError('Uncertain save')
        with patch('plate_reference.Geometry',return_value=g):
            with self.assertRaisesRegex(OSError,'Uncertain save'):
                cut_sidewalls(c,'body',axis=0,centre=[-2,140],diameter=30,
                              intervals=[[-26,-19],[19,26]],label='cut',checkpoint=checkpoint)
        g.cylinder.assert_called_once()
        g.subtract.assert_not_called()


class PlacedCircularCylinders(unittest.TestCase):
    def test_unit_rotation_preserves_radius_and_transforms_axis_as_direction(self):
        fixture = dict(origin=[2,3,4], axis=[2,0,0], radius=3.25)
        transform = [[0,0,1,200],[0,1,0,20],[-1,0,0,40],[0,0,0,1]]
        checked = placed_circular_cylinders([fixture], transform)
        self.assertEqual(checked,[dict(origin=[204,23,38],axis=[0,0,-1],radius=3.25)])
        self.assertEqual(fixture['axis'],[2,0,0])

    def test_declared_reflection_and_scale_rejection(self):
        fixture = dict(origin=[0,150,0],axis=[0,1,0],radius=3)
        reflection = [[1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1]]
        with self.assertRaisesRegex(ValueError,'Explicit unit reflection'):
            placed_circular_cylinders([fixture],reflection)
        [observed] = placed_circular_cylinders([fixture],reflection,allow_unit_reflection=True)
        self.assertEqual(observed['origin'],[0,-150,0])
        self.assertEqual(observed['axis'],[0,-1,0])
        reflection[0][0] = 2
        with self.assertRaisesRegex(ValueError,'Orthonormal unit'):
            placed_circular_cylinders([fixture],reflection,allow_unit_reflection=True)


class ViewsAndVectors(unittest.TestCase):
    def test_mirrored_nested_display_matrices(self):
        props=dict(normal=dict(x=0,y=0,z=1),rotation=0,insert_point=dict(x=0,y=3,z=0),x_scale=1,y_scale=-1,z_scale=1,block_name='block')
        records=[dict(handle='A',type='Insert',properties=props),dict(handle='B',type='Solid3D',properties={'acis_data':{'sab_data':[1]}})]
        blocks=[dict(name='*Model_Space',properties=dict(entity_handles=[10])),dict(name='block',properties=dict(base_point=dict(x=0,y=0,z=0),entity_handles=[11]))]
        with patch('native_views.boundary_curves',return_value=[dict(curve_type='straight-curve',endpoints=[[0,1,0],[1,1,0]])]):
            edges,instances=placed_boundaries(records,blocks)
        self.assertEqual(edges[0]['points'],[[0,2,0],[1,2,0]]);self.assertEqual(len(instances),1)
    def test_native_line_endpoints_follow_mirrored_block_placement(self):
        insert = dict(handle='A', type='Insert', properties=dict(
            normal=dict(x=0, y=0, z=1), rotation=0, insert_point=dict(x=5, y=10, z=1),
            x_scale=1, y_scale=-1, z_scale=1, block_name='child',
        ))
        line = dict(handle='B', type='Line', properties=dict(
            start=dict(x=0, y=2, z=3), end=dict(x=4, y=5, z=6),
        ))
        blocks = [
            dict(name='*Model_Space', properties=dict(entity_handles=['A'])),
            dict(name='child', properties=dict(base_point=dict(x=0, y=0, z=0), entity_handles=['B'])),
        ]
        edges, instances = placed_boundaries([insert, line], blocks)
        self.assertEqual(edges[0]['points'], [[5, 8, 4], [9, 5, 7]])
        self.assertEqual(instances[0]['handle'], 'B')
        line['properties']['end']['x'] = float('inf')
        with self.assertRaisesRegex(ValueError, 'Finite native line endpoints'):
            placed_boundaries([insert, line], blocks)

    def test_sat_reader_uses_reachable_vertices_and_closed_partner_graph(self):
        from types import SimpleNamespace as E
        null=E(name='null-ptr',data=[]);point=E(name='point',data=[null,'1','2','3']);vertex=E(name='vertex',data=[point]);a=E(name='coedge');b=E(name='coedge');edge=E(name='edge',data=[vertex]);a.data=[null,null,null,b,edge];b.data=[null,null,null,a,edge]
        plane=E(name='plane-surface',data=[null,'0','0','0','0','0','1']);body=E(name='body',data=[a,b,plane]);parsed=E(entities=[body,E(name='point',data=[null,'99','99','99'])],header=E(units_in_mm=1))
        with patch('ezdxf.acis.sat.parse_sat',return_value=parsed),patch('native_geometry.identity_sat_vertices',return_value=[[99,99,99]]):
            result=sat_structure('synthetic')
        self.assertEqual(result['points'],[[1,2,3]]);self.assertTrue(result['topology']['reciprocal_closed_partners'])
    def test_circular_sampling_and_endpoint_fallback(self):
        edge=dict(curve_type='ellipse-curve',endpoints=[[2,0,0],[2,0,0]],ellipse=dict(center=[0,0,0],normal=[0,0,1],major_axis=[2,0,0],minor_to_major_ratio=1),start_parameter=0,end_parameter=2*math.pi)
        points,fallback=sample(edge);self.assertEqual(len(points),129);self.assertFalse(fallback)
        edge['endpoints']=[[1,0,0],[1,0,0]];self.assertTrue(sample(edge)[1])
        edge['end_parameter']=1e10
        with self.assertRaises(ValueError):sample(edge)
    def test_native_arc_density_ignores_roundoff_at_integral_interval_count(self):
        arc=dict(curve_type='ellipse-curve',endpoints=[[2,0,0],[0,2,0]],
                 ellipse=dict(center=[0,0,0],normal=[0,0,1],major_axis=[2,0,0],minor_to_major_ratio=1),
                 start_parameter=0,end_parameter=math.pi/2)
        rounded_up=dict(arc,end_parameter=math.nextafter(math.pi/2, math.inf))
        for edge in (arc,rounded_up):
            points,fallback=sample(edge)
            self.assertEqual(len(points),33)
            self.assertFalse(fallback)
        longer=dict(arc,end_parameter=math.pi/2+1e-8)
        self.assertEqual(len(sample(longer)[0]),34)

    def test_svg_projections_and_existing_file_protection(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=render_views([dict(points=[[0,0,0],[4,5,6]],endpoints_only=False),dict(points=[[1,2,3]],endpoints_only=True)],tmp,stem='model',title='Synthetic <native>')
            self.assertEqual({x['projection'] for x in out},{'XY','XZ','YZ','isometric'})
            for row in out:self.assertEqual(hashlib.sha256(Path(row['path']).read_bytes()).hexdigest(),row['sha256'])
            with self.assertRaises(ValueError):render_views([dict(points=[[0,0,0]],endpoints_only=True)],tmp,stem='model',title='same')
    def test_svg_grammar_ids_transforms_and_cubic(self):
        paths=parse_path(7,'m 1 2 3 0 c 1 0 1 1 0 1 z')
        self.assertEqual(paths[0]['path_index'],7);self.assertEqual(paths[0]['segments'][0]['end'],[4,2]);self.assertTrue(paths[0]['closed'])
        self.assertEqual(local_point([1,2],[1,0,0,1,3,4],[10,20],units_per_page_unit=2),[18,8])
        self.assertEqual(cubic_point([[0,0],[0,1],[1,1],[1,0]],.5),[.5,.75])
        for text in ('M0 0 Q1 2 3 4','M0 0 L1','M0 0 @ L1 2','M0 0 L1e999 2'):
            with self.assertRaises(ValueError):parse_path(0,text)
    def test_sab_display_preserves_unknown_trim_endpoints(self):
        from test_native_circle_boundaries import circle_pair
        from native_acis import sab_features
        with patch('ezdxf.acis.sab.parse_sab',return_value=circle_pair(curve_name='intcurve-curve')):
            self.assertEqual(boundary_curves(b'fixture')[0]['representation'],'native trim endpoints')
            result=sab_features(b'fixture',include_edge_curves=True,edge_policy='endpoints')
            self.assertEqual(result['face_boundary_edges'][0]['loops'][0]['edges'][0]['representation'],'native trim endpoints')
            with self.assertRaises(ValueError):sab_features(b'fixture',include_edge_curves=True)
    @staticmethod
    def polyline(closed):
        return dict(handle='B', type='LwPolyline', properties=dict(
            normal=dict(x=0, y=1, z=0), elevation=3, is_closed=closed,
            vertices=[dict(location=dict(x=x, y=y), bulge=0)
                      for x, y in [(0, 0), (4, 0), (4, 2), (0, 2)]],
        ))

    def test_straight_polyline_open_and_closed_in_wcs(self):
        open_path = wcs_straight_polyline_segments(self.polyline(False))
        closed_path = wcs_straight_polyline_segments(self.polyline(True))
        self.assertEqual(open_path, [
            [[0, 3, 0], [-4, 3, 0]], [[-4, 3, 0], [-4, 3, 2]], [[-4, 3, 2], [0, 3, 2]],
        ])
        self.assertEqual(closed_path, open_path + [[[0, 3, 2], [0, 3, 0]]])

    def test_polyline_placement_preserves_closure_and_ignores_circle(self):
        insert = dict(handle='A', type='Insert', properties=dict(
            normal=dict(x=0, y=0, z=1), rotation=0, insert_point=dict(x=5, y=10, z=0),
            x_scale=1, y_scale=-1, z_scale=1, block_name='child',
        ))
        blocks = [
            dict(name='*Model_Space', properties=dict(entity_handles=['A', 'C'])),
            dict(name='child', properties=dict(base_point=dict(x=0, y=0, z=0), entity_handles=[11])),
        ]
        edges, instances = placed_boundaries(
            [insert, self.polyline(True), dict(handle='C', type='Circle')], blocks,
        )
        self.assertEqual([i['handle'] for i in instances], ['B'])
        self.assertEqual(len(edges), 4)
        self.assertEqual(edges[-1]['points'], [[5, 7, 2], [5, 7, 0]])
        self.assertTrue(all(e['curve_type'] == 'straight-curve' and not e['endpoints_only'] for e in edges))

    def test_positive_z_circle_resolves_through_mirrored_block(self):
        insert = dict(handle='A', type='Insert', properties=dict(
            normal=dict(x=0, y=0, z=1), rotation=0, insert_point=dict(x=5, y=10, z=20),
            x_scale=1, y_scale=-1, z_scale=1, block_name='child',
        ))
        circle = dict(handle='B', type='Circle', properties=dict(
            center=dict(x=2, y=3, z=4), normal=dict(x=0, y=0, z=1), radius=7, thickness=0,
        ))
        blocks = [
            dict(name='*Model_Space', properties=dict(entity_handles=['A'])),
            dict(name='child', properties=dict(base_point=dict(x=0, y=0, z=0), entity_handles=['B'])),
        ]
        edges, instances = placed_boundaries([insert, circle], blocks, include_xy_circles=True)
        self.assertEqual(instances[0]['path'], ['A'])
        self.assertEqual(instances[0]['handle'], 'B')
        edge, = edges
        self.assertFalse(edge['endpoints_only'])
        self.assertEqual(edge['points'][0], [14, 7, 24])
        self.assertAlmostEqual(min(point[0] for point in edge['points']), 0)
        self.assertAlmostEqual(max(point[1] for point in edge['points']), 14)
        self.assertTrue(all(point[2] == 24 for point in edge['points']))
        circle['properties']['thickness'] = 2
        with self.assertRaisesRegex(ValueError,'zero thickness'):
            placed_boundaries([insert, circle],blocks,include_xy_circles=True)
        circle['properties']['thickness'] = 0
        circle['properties']['normal']['z'] = -1
        with self.assertRaisesRegex(ValueError,'positive-Z plane'):
            placed_boundaries([insert, circle],blocks,include_xy_circles=True)

    def test_countersink_profile_extends_past_bore_and_top(self):
        result = countersink_tool_profile(bore=8,mouth=18,angle_degrees=90,inner_radius=2,overrun=.5)
        self.assertAlmostEqual(result['depth_mm'],5)
        for pair, expected in zip(result['profile'],[[2,-.5],[3.5,-.5],[9.5,5.5],[2,5.5]]):
            for value, target in zip(pair, expected):
                self.assertAlmostEqual(value,target)
        with self.assertRaisesRegex(ValueError,'clear the inner radius'):
            countersink_tool_profile(bore=8,mouth=18,angle_degrees=90,inner_radius=3.9,overrun=.5)

    def test_matching_countersinks_check_signed_setback_and_face_overlap(self):
        nominal = dict(seat_bore=5,seat_mouth=10,head_shank=4,head_outer=8,angle_degrees=90)
        fit = matching_countersink_fit(**nominal)
        self.assertAlmostEqual(fit['head_setback_mm'],1)
        self.assertAlmostEqual(fit['facing_cone_axial_span_mm'],1.5)
        fit = matching_countersink_fit(**dict(nominal,head_outer=12,angle_degrees=60))
        self.assertAlmostEqual(fit['head_setback_mm'],-3**.5)
        self.assertAlmostEqual(fit['facing_cone_axial_span_mm'],2.5*3**.5)
        with self.assertRaisesRegex(ValueError,'ranges must overlap'):
            matching_countersink_fit(**dict(nominal,head_outer=5))

    def test_xy_bulges_preserve_arc_direction_and_elevation(self):
        row = self.polyline(False)
        row['properties']['normal'] = dict(x=0,y=0,z=1)
        first = row['properties']['vertices'][0]
        for bulge, midpoint_y in [(1,-2),(-1,2),(.5,-1)]:
            first['bulge'] = bulge
            arc = xy_polyline_view_curves(row)[0]
            points, fallback = sample(arc,points_per_revolution=64)
            nearest = min(points,key=lambda point:abs(point[0]-2))
            self.assertFalse(fallback)
            self.assertAlmostEqual(nearest[1],midpoint_y,places=2)
            self.assertAlmostEqual(nearest[2],3)
            self.assertEqual(arc['endpoints'],[[0,0,3],[4,0,3]])
        row['properties']['normal'] = dict(x=0,y=1,z=0)
        with self.assertRaises(ValueError):
            xy_polyline_view_curves(row)

    def test_placed_bulged_polylines_require_opt_in_and_close(self):
        row = self.polyline(True)
        row['properties']['normal'] = dict(x=0,y=0,z=1)
        row['properties']['vertices'][-1]['bulge'] = 1
        blocks = [dict(name='*Model_Space',properties=dict(entity_handles=['B']))]
        with self.assertRaises(ValueError):
            placed_boundaries([row],blocks)
        edges,_ = placed_boundaries([row],blocks,include_xy_bulges=True)
        self.assertEqual(len(edges),4)
        self.assertAlmostEqual(min(p[0] for p in edges[-1]['points']),-1)
        self.assertFalse(edges[-1]['endpoints_only'])

    def test_polyline_rejects_bulge_and_legacy_closure_field(self):
        row = self.polyline(True)
        row['properties']['vertices'][0]['bulge'] = 0.25
        with self.assertRaisesRegex(ValueError, 'zero-bulge'):
            wcs_straight_polyline_segments(row)
        row['properties']['vertices'][0]['bulge'] = 0
        row['properties']['closed'] = row['properties'].pop('is_closed')
        with self.assertRaisesRegex(ValueError, 'is_closed'):
            wcs_straight_polyline_segments(row)

    def test_ocs_polyline_points(self):
        row=dict(type='LwPolyline',properties=dict(normal=dict(x=0,y=0,z=1),elevation=3,vertices=[dict(location=dict(x=1,y=2))]))
        self.assertEqual(wcs_polyline_vertices(row),[[1,2,3]])


class Relationships(unittest.TestCase):
    def test_stale_model_image_relationship_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);model=root/'model.dwg';model.write_bytes(b'model')
            record=root/'view.json';record.write_text(json.dumps({'source_sha256':hashlib.sha256(model.read_bytes()).hexdigest()}))
            manifest=root/'manifest.json'
            def write():
                manifest.write_text(json.dumps(dict(files=[dict(path=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in (model,record)],relationships=[dict(record='view.json',artifact='model.dwg',field='/source_sha256')])))
            write();self.assertEqual(len(verify_manifest(manifest,{})['verified_relationships']),1)
            model.write_bytes(b'new revision');write()
            with self.assertRaises(ValueError):verify_manifest(manifest,{})


class CleanupAndInsertion(unittest.TestCase):
    def test_active_cleanup_preserves_unknown_outcome(self):
        with tempfile.TemporaryDirectory() as tmp:
            c,e,state,docs,_=self.cleanup_fixture(tmp)
            def active_state():
                value=state();value['document_id']=2;return value
            with patch('ocs_document_cleanup.cleanup_active_owned_document',side_effect=Uncertain('pending original close')):
                result=cleanup_owned_documents(state_reader=active_state,client=c,owned_documents=[e],namespace='cleanup')
            self.assertEqual(result['results'][0]['cleanup_status'],'UNKNOWN')
            self.assertIn(2,docs);c.helper.request.assert_not_called()
    def cleanup_fixture(self,tmp,*,lose=False,change_other=False,pending=False):
        path=Path(tmp)/'saved.dwg';path.write_bytes(b'saved')
        digest=hashlib.sha256(path.read_bytes()).hexdigest();docs={1:dict(id=1,path='other',dirty=True),2:dict(id=2,path=str(path),dirty=False)}
        state=lambda:dict(ok=True,document_id=1,revision=5,geometry_revision=30,command=None,modal=None,documents=[v.copy() for v in docs.values()])
        completed=dict(ok=True,status='completed',result=dict(closed=True,closed_document_id=2))
        h=Mock();h.READ_OPS={'state'}
        def request(descriptor,payload,timeout):
            if payload['op']=='state':return state()
            if payload['op']=='close':
                docs.pop(2)
                if change_other:docs[1]['dirty']=False
                if lose:raise TimeoutError()
                return dict(ok=True,status='accepted') if pending else completed
            return dict(ok=True,status='running') if pending else completed
        h.request.side_effect=request
        c=Client(h,{'session_id':'s'},1,'job',Journal(Path(tmp)/'journal'),allow_write=True,max_queries=1)
        e=dict(document_id=2,expected_path=str(path),expected_geometry_revision=20,construction_copy=False,dirty_discard_allowed=False,saved_model_path=str(path),saved_model_sha256=digest,persistence_receipt=dict(result='PASS',saved_path=str(path),sha256=digest))
        return c,e,state,docs,completed
    def test_inactive_lost_reply_recovers_same_id_and_preserves_other_tabs(self):
        with tempfile.TemporaryDirectory() as tmp:
            c,e,state,docs,_=self.cleanup_fixture(tmp,lose=True)
            result=cleanup_owned_documents(state_reader=state,client=c,owned_documents=[e],namespace='cleanup',exclusive_interval=True,allow_inactive_clean=True)
            self.assertEqual(result['result'],'PASS');self.assertTrue(docs[1]['dirty'])
            requests=[call.args[1] for call in c.helper.request.call_args_list]
            self.assertEqual(sum(r['op']=='close' for r in requests),1)
            self.assertEqual(requests[-1]['request_id'],requests[0]['request_id'])
    def test_inactive_route_requires_serialization_and_checks_other_changes(self):
        for serialize,changed in [(False,False),(True,True)]:
            with tempfile.TemporaryDirectory() as tmp:
                c,e,state,docs,_=self.cleanup_fixture(tmp,change_other=changed)
                r=cleanup_owned_documents(state_reader=state,client=c,owned_documents=[e],namespace='cleanup',exclusive_interval=serialize,allow_inactive_clean=True)
                self.assertEqual(r['result'],'INCOMPLETE')
                if not serialize:c.helper.request.assert_not_called()
                else:self.assertTrue(r['results'][0]['close_confirmed'])
    def test_inactive_restart_recovers_absent_target_without_reclose(self):
        with tempfile.TemporaryDirectory() as tmp:
            c,e,state,docs,completed=self.cleanup_fixture(tmp,pending=True)
            r=cleanup_owned_documents(state_reader=state,client=c,owned_documents=[e],namespace='cleanup',exclusive_interval=True,allow_inactive_clean=True)
            self.assertEqual(r['results'][0]['cleanup_status'],'UNKNOWN')
            c.journal=Journal(c.journal.path);c.helper.request.return_value=completed;c.helper.request.side_effect=None
            r=cleanup_owned_documents(state_reader=state,client=c,owned_documents=[e],namespace='cleanup',exclusive_interval=True,allow_inactive_clean=True)
            self.assertEqual(r['result'],'PASS')
            self.assertEqual(sum(call.args[1]['op']=='close' for call in c.helper.request.call_args_list),1)
    def test_wrong_insert_prompt_stops_before_file_input(self):
        from assembly_build import insert_component
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'part.dwg';path.write_bytes(b'source')
            c=Mock();c.document_id=1;c.read.return_value=dict(document_id=1,command=dict(name='SLICE',prompt='first point'))
            with self.assertRaises(CadError):insert_component(c,'part',path,source_locator='part.dwg')
            self.assertEqual(c.mutate.call_count,1)
            self.assertEqual(c.mutate.call_args.args[1],'start')




class FiniteCrossDrillTests(unittest.TestCase):
    def test_decimal_endpoints_and_each_uncovered_end(self):
        sizes = dict(shaft_axis=1, shaft_centre=[0, .2], shaft_radius=.1,
                     shaft_stations=[-2, 2], bore_axis=2, bore_centre=[0, 0],
                     bore_radius=.03, tolerance=.001)
        for stations, overrun, expected in (([.1, .3], [0, 0], "PASS"),
                                            ([.15, .3], [-.05, 0], "FAIL"),
                                            ([.1, .25], [0, -.05], "FAIL")):
            with self.subTest(stations=stations):
                check = perpendicular_through_bore("bore", **sizes, cutter_stations=stations)
                self.assertEqual(check["result"], expected)
                self.assertEqual(check["required_cutter_stations"], [.1, .3])
                self.assertEqual(check["cutter_overrun"], overrun)

    def test_shifted_shaft_requires_world_cutter_stations(self):
        sizes = dict(shaft_axis=1, shaft_centre=[0, 460], shaft_radius=9.5,
                     shaft_stations=[-52, 52], bore_axis=2, bore_centre=[0, 46],
                     bore_radius=3, tolerance=1e-6)
        missed = perpendicular_through_bore("keeper", **sizes, cutter_stations=[-9.5, 9.5])
        self.assertEqual(missed["result"], "FAIL")
        self.assertEqual(missed["required_cutter_stations"], [450.5, 469.5])
        through = perpendicular_through_bore("keeper", **sizes, cutter_stations=[449.5, 470.5])
        self.assertEqual(through["result"], "PASS")
        self.assertEqual(through["cutter_overrun"], [1, 1])
        self.assertEqual(through["remaining_end_land"]["minimum"], 3)
        for stations, expected in (([450.55, 469.45], "FAIL"), ([450.5, 469.5], "PASS")):
            self.assertEqual(perpendicular_through_bore("keeper", **dict(sizes, tolerance=.1),
                             cutter_stations=stations)["result"], expected)
        for invalid_centre in ([1, 46], [0, 50]):
            wrong = dict(sizes, bore_centre=invalid_centre)
            self.assertEqual(perpendicular_through_bore("keeper", **wrong,
                             cutter_stations=[449.5, 470.5])["result"], "FAIL")


if __name__=='__main__':unittest.main()
