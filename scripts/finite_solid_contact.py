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
