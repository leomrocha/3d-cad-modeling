"""Optional Open CASCADE finite solid interference checks in the caller's length unit."""
import math

from cadtools.geometry import finite, positive, vector


class _Unresolved(Exception):
    """The kernel did not produce enough evidence for a classification."""


def _entities(shape, kind):
    from OCP.TopExp import TopExp_Explorer

    cursor = TopExp_Explorer(shape, kind)
    while cursor.More():
        yield cursor.Current()
        cursor.Next()


def _oriented_copy(shape, classifier_tolerance):
    from OCP.Bnd import Bnd_Box
    from OCP.BRepBndLib import BRepBndLib
    from OCP.BRepClass3d import BRepClass3d_SolidClassifier
    from OCP.BRep import BRep_Tool
    from OCP.BRepBuilderAPI import BRepBuilderAPI_Copy
    from OCP.BRepCheck import BRepCheck_Analyzer
    from OCP.BRepLib import BRepLib
    from OCP.TopAbs import TopAbs_OUT, TopAbs_SHELL, TopAbs_SOLID
    from OCP.TopoDS import TopoDS

    if shape.IsNull() or shape.ShapeType() != TopAbs_SOLID:
        raise _Unresolved('Expected one finite solid per input')
    solid = TopoDS.Solid_s(BRepBuilderAPI_Copy(shape).Shape())
    bounds = Bnd_Box()
    BRepBndLib.Add_s(solid, bounds, False)
    if bounds.IsVoid() or bounds.IsOpen() or not all(math.isfinite(value) for value in bounds.Get()):
        raise _Unresolved('Solid boundary lacks finite bounds')
    shells = list(_entities(solid, TopAbs_SHELL))
    if not shells or not all(BRep_Tool.IsClosed_s(shell) for shell in shells):
        raise _Unresolved('Open or missing shell')
    if not BRepCheck_Analyzer(solid).IsValid() or not BRepLib.OrientClosedSolid_s(solid):
        raise _Unresolved('Invalid solid or inconsistent orientation')
    classifier = BRepClass3d_SolidClassifier(solid)
    classifier.PerformInfinitePoint(classifier_tolerance)
    if classifier.State() != TopAbs_OUT:
        raise _Unresolved('Oriented solid does not classify infinity as exterior')
    return solid


def _distance(first, second, deflection):
    from OCP.BRepExtrema import BRepExtrema_DistShapeShape

    distance = BRepExtrema_DistShapeShape(first, second, deflection)
    if not distance.IsDone() or not distance.NbSolution() or not math.isfinite(distance.Value()):
        raise _Unresolved('Distance computation failed')
    return distance.Value()


def _witnesses(points, solids, tolerance, deflection, margin):
    from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
    from OCP.BRepClass3d import BRepClass3d_SolidClassifier
    from OCP.TopAbs import TopAbs_IN, TopAbs_SHELL
    from OCP.gp import gp_Pnt

    classifiers = [BRepClass3d_SolidClassifier(solid) for solid in solids]
    walls = [list(_entities(solid, TopAbs_SHELL)) for solid in solids]
    result = []
    for xyz in points:
        point = gp_Pnt(*xyz)
        vertex = BRepBuilderAPI_MakeVertex(point).Vertex()
        distances, states = [], []
        for classifier, shells in zip(classifiers, walls):
            classifier.Perform(point, tolerance)
            states.append(classifier.State() == TopAbs_IN)
            distances.append(min(_distance(vertex, wall, deflection) for wall in shells))
        result.append(dict(point=xyz, inside=states, boundary_distances=distances,
                           strict_interior=all(states) and min(distances) > margin))
    return result


def finite_solid_contact(first, second, *, relative_integration_target,
                         distance_deflection, classifier_tolerance, contact_tolerance,
                         witness_margin, points=()):
    """Check one static pair with explicit numerical controls.

    Points are optional interior witness candidates in the solids' common frame.
    CONTACT_WITHIN_TOLERANCE includes unresolved gaps within contact_tolerance.
    A strict witness independently verifies overlap when the Boolean returns no
    solid. Reported volumes use the cube of the supplied coordinate unit.
    """
    from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    from OCP.Standard import Standard_Failure
    from OCP.TopAbs import TopAbs_SOLID

    if not 0 < finite(relative_integration_target) <= 0.001:
        raise ValueError('Adaptive integration target must be in (0, 0.001]')
    positive(distance_deflection)
    positive(classifier_tolerance)
    if finite(contact_tolerance) < distance_deflection or finite(witness_margin) < max(classifier_tolerance, distance_deflection):
        raise ValueError('Contact and witness thresholds must cover their numerical tolerances')
    points = [vector(point) for point in points]
    receipt = dict(state='UNKNOWN', relative_integration_target=relative_integration_target,
                   distance_deflection=distance_deflection, contact_tolerance=contact_tolerance,
                   classifier_tolerance=classifier_tolerance, witness_margin=witness_margin)
    try:
        a, b = _oriented_copy(first, classifier_tolerance), _oriented_copy(second, classifier_tolerance)
        operation = BRepAlgoAPI_Common(a, b)
        receipt['boolean_fuzzy_tolerance'] = operation.FuzzyValue()
        if not operation.IsDone() or operation.Shape().IsNull():
            raise _Unresolved('Boolean common did not produce a shape')
        pieces = []
        for shape in _entities(operation.Shape(), TopAbs_SOLID):
            solid = _oriented_copy(shape, classifier_tolerance)
            properties = GProp_GProps()
            error = BRepGProp.VolumeProperties_s(solid, properties, relative_integration_target, True, False)
            volume = properties.Mass()
            if not math.isfinite(volume) or volume <= 0 or not 0 <= error <= relative_integration_target:
                raise _Unresolved('Positive common volume within integration target unavailable')
            pieces.append(dict(volume=volume, relative_error_estimate=error))
        gap = _distance(a, b, distance_deflection)
        evidence = _witnesses(points, [a, b], classifier_tolerance, distance_deflection, witness_margin)
        receipt.update(common_pieces=pieces, boolean_common_volume=math.fsum(p['volume'] for p in pieces),
                       solid_distance=gap, witnesses=evidence)
        if pieces or any(point['strict_interior'] for point in evidence):
            if gap > contact_tolerance:
                raise _Unresolved('Positive overlap and positive separation evidence conflict')
            receipt['state'] = 'POSITIVE_OVERLAP'
        elif gap > contact_tolerance:
            receipt['state'] = 'SEPARATED'
        else:
            receipt['state'] = 'CONTACT_WITHIN_TOLERANCE'
    except (_Unresolved, RuntimeError, Standard_Failure) as error:
        receipt['reason'] = str(error)
    return receipt


def axial_bore_clearance(moving, fixed, *, axis_xy, travel_z, moving_radius,
                         bore_radius, reserve, classifier_tolerance, fixed_ceiling=None):
    """Check continuous fixed-XY translation against one stationary solid.

    Localize stationary material to an XY box around the entire moving solid.
    Clip the moving solid to every source Z that can approach this material.
    Check radial containment of this section and an empty coaxial bore in the
    fixed material. Lengths use one common unit. The numerical budget covers
    imported topology and Boolean fuzz only.
    """
    from fractions import Fraction
    from OCP.Bnd import Bnd_Box
    from OCP.BRep import BRep_Tool
    from OCP.BRepAlgoAPI import BRepAlgoAPI_Common, BRepAlgoAPI_Cut
    from OCP.BRepBndLib import BRepBndLib
    from OCP.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
    from OCP.Standard import Standard_Failure
    from OCP.TopAbs import TopAbs_EDGE, TopAbs_FACE, TopAbs_SOLID, TopAbs_VERTEX
    from OCP.gp import gp_Ax2, gp_Dir, gp_Pnt
    from service_clearance import axial_section_window

    x, y = vector(axis_xy, 2)
    start, end = vector(travel_z, 2)
    for length in (moving_radius, bore_radius, reserve, classifier_tolerance):
        positive(length)
    if fixed_ceiling is not None:
        finite(fixed_ceiling)
    if start > end or moving_radius >= bore_radius:
        raise ValueError('Ordered Z travel and strictly nested radii required')
    def bounds(shape):
        box = Bnd_Box()
        BRepBndLib.Add_s(shape, box, False)
        return box.Get()

    def boolean(operation, first, second):
        result = operation(first, second)
        if not result.IsDone() or result.Shape().IsNull() or not BRepCheck_Analyzer(result.Shape()).IsValid():
            raise _Unresolved('Invalid or incomplete section Boolean')
        return list(_entities(result.Shape(), TopAbs_SOLID))

    def cylinder(radius, low, high):
        axis = gp_Ax2(gp_Pnt(x, y, low), gp_Dir(0, 0, 1))
        return BRepPrimAPI_MakeCylinder(axis, radius, high - low).Shape()

    from OCP.BRepCheck import BRepCheck_Analyzer
    evidence = dict(state='UNKNOWN', travel_z=[start, end], reserve=reserve,
                    axis_xy=[x, y], moving_radius=moving_radius, bore_radius=bore_radius)
    try:
        moving = _oriented_copy(moving, classifier_tolerance)
        fixed = _oriented_copy(fixed, classifier_tolerance)
        kinds = [TopAbs_VERTEX, TopAbs_EDGE, TopAbs_FACE]
        tolerances = [max(BRep_Tool.MaxTolerance_s(body, k) for k in kinds)
                      for body in (moving, fixed)]
        fuzz = BRepAlgoAPI_Common().FuzzyValue()
        budget = math.fsum([*tolerances, fuzz])
        evidence.update(topology_tolerance_maxima=tolerances, boolean_fuzz=fuzz,
                        topology_and_fuzz_budget=budget)
        if reserve <= budget or Fraction(bore_radius) - Fraction(moving_radius) < Fraction(reserve):
            raise _Unresolved('Requested reserve exceeds radial separation or fails to exceed the numerical budget')
        ml, mb, mz, mr, mt, mh = bounds(moving)
        _, _, fz, _, _, fh = bounds(fixed)
        # Round enclosure coordinates outwards after binary64 arithmetic.
        def outer(value, offset):
            return math.nextafter(value + offset, math.inf if offset > 0 else -math.inf)

        xl, yl, xh, yh = outer(ml, -reserve), outer(mb, -reserve), outer(mr, reserve), outer(mt, reserve)
        def box(low, high):
            return BRepPrimAPI_MakeBox(gp_Pnt(xl, yl, low), gp_Pnt(xh, yh, high)).Shape()

        local = boolean(BRepAlgoAPI_Common, fixed, box(outer(fz, -reserve), outer(fh, reserve)))
        evidence['localized_fixed_solids'] = len(local)
        if local:
            fixed_spans = [bounds(s) for s in local]
            bottom, top = min(s[2] for s in fixed_spans), max(s[5] for s in fixed_spans)
            if fixed_ceiling is not None and fixed_ceiling < top:
                above = box(fixed_ceiling, outer(top, reserve))
                upper_pieces = sum(len(boolean(BRepAlgoAPI_Common, s, above)) for s in local)
                evidence.update(fixed_ceiling=fixed_ceiling, fixed_solids_above_ceiling=upper_pieces)
                if upper_pieces or fixed_ceiling <= bottom:
                    raise _Unresolved('Localized fixed solid exceeds the supplied ceiling')
                top = fixed_ceiling
            window = axial_section_window((mz, mh), (bottom, top), (start, end), clearance=reserve)
            evidence.update(window)
            if window['source_section'] is not None:
                low, high = (float(Fraction(s)) for s in window['source_section'])
                # Positive padding also covers a zero-width limiting section.
                low = outer(low, -classifier_tolerance)
                high = outer(high, classifier_tolerance)
                clipped = boolean(BRepAlgoAPI_Common, moving, box(low, high))
                inside_limit = cylinder(moving_radius, outer(low, -reserve), outer(high, reserve))
                guard = cylinder(bore_radius, outer(bottom, -reserve), outer(top, reserve))
                outside = sum(len(boolean(BRepAlgoAPI_Cut, s, inside_limit)) for s in clipped)
                blocked = sum(len(boolean(BRepAlgoAPI_Common, s, guard)) for s in local)
                evidence.update(moving_section_solids=len(clipped), outside_moving_limit=outside,
                                inside_fixed_guard=blocked)
                if not clipped or outside or blocked:
                    raise _Unresolved('Nested radial containment evidence is inconclusive')
        evidence['state'] = 'CLEAR_WITH_NUMERICAL_RESERVE'
    except (_Unresolved, RuntimeError, Standard_Failure) as error:
        evidence['reason'] = str(error)
    return evidence
