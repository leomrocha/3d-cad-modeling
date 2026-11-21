"""Offline, geometry-bound assembly occurrence and world-vertex verification.

Inputs share caller-declared XYZ frames/length units. Matrix linear tolerances
are dimensionless; translation and point tolerances use the length unit.
"""
import math
from cadtools.geometry import finite,vector
from solid_transfer import verify_solid_transfer
from step_placements import apply, solid_instances


def _tolerance(value):
    if finite(value)<=0:raise ValueError('Positive numerical tolerance required')
    return value


def _bijection(candidates,target_count):
    """Bounded augmenting paths preserve repeated coincident instances."""
    source_match={};target_match={}
    for start in range(len(candidates)):
        queue=[start];seen={start};parent_target={};free=None
        for source in queue:
            for target in candidates[source]:
                if target in parent_target:continue
                parent_target[target]=source
                if target not in target_match:free=target;break
                other=target_match[target]
                if other not in seen:seen.add(other);queue.append(other)
            if free is not None:break
        if free is None:continue
        while free is not None:
            source=parent_target[free];previous=source_match.get(source)
            source_match[source]=free;target_match[free]=source;free=previous
    passed=len(source_match)==len(candidates)==target_count
    return dict(result='PASS' if passed else 'FAIL',matching=source_match,
                unmatched_source=[i for i in range(len(candidates)) if i not in source_match],
                unmatched_target=[i for i in range(target_count) if i not in target_match])


def _matrix(m):
    if len(m)!=4 or any(len(r)!=4 for r in m):raise ValueError('4x4 placement required')
    for row in m:
        for v in row:finite(v)
    if list(m[3])!=[0,0,0,1]:raise ValueError('Affine placement last row required')
    return m


def check_axis_aligned_placement(local_bounds, target_bounds, matrix, *, length_tolerance):
    """Check corner-to-corner bounds for a signed axis permutation and translation."""
    tolerance = _tolerance(length_tolerance)
    matrix = _matrix(matrix)
    basis = [list(row[:3]) for row in matrix[:3]]
    if (any(value not in (-1, 0, 1) for row in basis for value in row)
            or any(sum(abs(value) for value in row) != 1 for row in basis)
            or any(sum(abs(value) for value in column) != 1
                   for column in zip(*basis))):
        raise ValueError('Exact signed axis permutation required')
    boxes = []
    for bounds in (local_bounds, target_bounds):
        if len(bounds) != 2:
            raise ValueError('Lower and upper three-dimensional bounds required')
        low, high = (vector(point) for point in bounds)
        if any(a >= b for a, b in zip(low, high)):
            raise ValueError('Positive box extents required')
        boxes.append((low, high))
    (low, high), target = boxes
    corners = [apply(matrix, [x, y, z]) for x in (low[0], high[0])
               for y in (low[1], high[1]) for z in (low[2], high[2])]
    observed = [[fn(point[i] for point in corners) for i in range(3)] for fn in (min, max)]
    errors = [[observed[i][j] - target[i][j] for j in range(3)] for i in range(2)]
    return dict(result='PASS' if all(abs(error) <= tolerance for row in errors for error in row) else 'FAIL',
                observed_bounds=observed, target_bounds=target, coordinate_errors=errors)


def compare_occurrence_matrices(source,target,bindings,*,translation_tolerance,linear_tolerance):
    lt,at=_tolerance(translation_tolerance),_tolerance(linear_tolerance)
    mapping={};target_handles=set()
    for row in bindings:
        a,b=row['source_handle'],row['target_handle']
        if a in mapping or b in target_handles:raise ValueError('Bijective geometry definition bindings required')
        mapping[a]=b;target_handles.add(b)
    if not source or not target or not mapping:raise ValueError('Nonempty occurrences and bindings required')
    for rows in (source,target):
        paths=set()
        for row in rows:
            path=tuple(row['path'])
            if not path or path in paths:raise ValueError('Unique nonempty occurrence paths required')
            paths.add(path);_matrix(row['matrix'])
    if {r['handle'] for r in source}!=set(mapping) or {r['handle'] for r in target}!=target_handles:
        return dict(result='FAIL',reason='Occurrence geometry bindings do not cover the requested scope')
    candidates=[]
    for row in source:
        options=[]
        for j,other in enumerate(target):
            if mapping[row['handle']]!=other['handle']:continue
            a,b=row['matrix'],other['matrix']
            if all(abs(a[i][j]-b[i][j])<=at for i in range(3) for j in range(3)) and all(abs(a[i][3]-b[i][3])<=lt for i in range(3)):
                options.append(j)
        candidates.append(options)
    proof=_bijection(candidates,len(target))
    proof.update(method='geometry-bound one-to-one nested matrix matching',translation_tolerance=lt,linear_tolerance=at)
    return proof


def directed_axial_span(points, *, origin, direction):
    """Measure the signed axial span of observed points in a declared unit direction."""
    origin = vector(origin)
    direction = vector(direction)
    if not math.isclose(math.hypot(*direction),1,rel_tol=0,abs_tol=1e-9):
        raise ValueError('Unit axial direction required')
    stations = []
    for point in points:
        point = vector(point)
        stations.append(finite(sum((p-o)*d for p,o,d in zip(point,origin,direction,strict=True))))
    if not stations:
        raise ValueError('Observed axial points required')
    return [min(stations),max(stations)]


def compare_axial_occurrences(before, after, *, length_tolerance):
    """Match named, Z-aligned occurrences by role, XY axis and finite Z span."""
    tolerance = _tolerance(length_tolerance)

    def index(rows):
        indexed = {}
        for row in rows:
            name, role = row['occurrence'], row['role']
            if not isinstance(name, str) or not name.strip() or name in indexed:
                raise ValueError('Unique nonempty occurrence names required')
            if not isinstance(role, str) or not role.strip():
                raise ValueError('Named occurrence role required')
            axis = tuple(row['axis_xy_mm'])
            span = tuple(row['span_z_mm'])
            if len(axis)!=2 or len(span)!=2:
                raise ValueError('Expected two XY coordinates and two Z limits')
            for value in (*axis, *span):
                finite(value)
            if span[0] >= span[1]:
                raise ValueError('Expected ordered axial span with positive length')
            indexed[name] = (role, axis, span)
        if not indexed:
            raise ValueError('Nonempty occurrence records required')
        return indexed

    expected, observed = index(before), index(after)
    checks = []
    for name in sorted(expected.keys() & observed.keys()):
        role, axis, span = expected[name]
        found_role, found_axis, found_span = observed[name]
        axis_error = math.dist(axis, found_axis)
        span_error = math.dist(span, found_span)
        checks.append(dict(occurrence=name, axis_error_mm=axis_error, span_error_mm=span_error,
                           role_matches=role==found_role,
                           passed=role==found_role and max(axis_error, span_error)<=tolerance))
    missing = sorted(expected.keys()-observed.keys())
    added = sorted(observed.keys()-expected.keys())
    passed = not missing and not added and all(row['passed'] for row in checks)
    return dict(result='PASS' if passed else 'FAIL', length_tolerance_mm=tolerance,
                missing_occurrences=missing, added_occurrences=added, checks=checks)


def verify_nested_placements(source_records,source_blocks,source_roots,
                             target_records,target_blocks,target_roots,bindings,*,
                             translation_tolerance,linear_tolerance,
                             allow_unit_reflection=False,allow_uniform_scale=False,
                             max_instances=10000,added_metadata_apps=()):
    options=dict(max_instances=max_instances,allow_unit_reflection=allow_unit_reflection,allow_uniform_scale=allow_uniform_scale)
    source=solid_instances(source_records,source_blocks,source_roots,**options)
    target=solid_instances(target_records,target_blocks,target_roots,**options)
    sh={r['handle'] for r in source};th={r['handle'] for r in target}
    geometry=verify_solid_transfer([r for r in source_records if r['handle'] in sh],
        [r for r in target_records if r['handle'] in th],bindings,added_metadata_apps=added_metadata_apps)
    placements=compare_occurrence_matrices(source,target,bindings,translation_tolerance=translation_tolerance,linear_tolerance=linear_tolerance)
    return dict(result='PASS' if geometry['result']==placements['result']=='PASS' else 'FAIL',
                source_instances=len(source),target_instances=len(target),geometry=geometry,placements=placements)


def _bounds(points):
    return [[min(p[i] for p in points),max(p[i] for p in points)] for i in range(3)]


def match_world_vertices(source,target,*,length_tolerance,max_instances=10000,
                         require_unique_source=False):
    """Match point sets, face counts and closed flags with repeated-instance multiplicity.

    Each row has id, points, face_count and closed. This compares vertices and
    topology observations; analytic surface equations retain separate checks.
    """
    if type(require_unique_source) is not bool:
        raise ValueError('Expected a boolean source attribution option')
    tolerance=_tolerance(length_tolerance)
    if type(max_instances) is not int or max_instances<1 or max(len(source),len(target))>max_instances:
        raise ValueError('Positive instance bound exceeded')
    if not source or not target:raise ValueError('Nonempty world-geometry observations required')
    prepared=[]
    for rows in (source,target):
        seen=set();out=[]
        for row in rows:
            if not isinstance(row.get('id'),str) or not row['id'] or row['id'] in seen:raise ValueError('Unique readable occurrence identities required')
            seen.add(row['id']);points=[vector(p) for p in row['points']]
            if not points or type(row.get('face_count')) is not int or row['face_count']<1 or type(row.get('closed')) is not bool:raise ValueError('Points, face count and explicit closed flag required')
            out.append(dict(row,points=points,bounds=_bounds(points)))
        prepared.append(out)
    candidates=[];residuals={}
    for i,row in enumerate(prepared[0]):
        hits=[]
        for j,other in enumerate(prepared[1]):
            if not row['closed'] or not other['closed'] or row['face_count']!=other['face_count']:continue
            if max(abs(x-y) for a,b in zip(row['bounds'],other['bounds']) for x,y in zip(a,b))>tolerance:continue
            a,b=row['points'],other['points']
            error=max(max(min(math.dist(p,q) for q in b) for p in a),max(min(math.dist(p,q) for q in a) for p in b))
            if error<=tolerance:hits.append(j);residuals[i,j]=error
        candidates.append(hits)
    proof=_bijection(candidates,len(target))
    if require_unique_source:
        alternatives = {row['id']: [] for row in target}
        for i, hits in enumerate(candidates):
            for j in hits:
                alternatives[target[j]['id']].append(source[i]['id'])
        ambiguous = {key: ids for key, ids in alternatives.items() if len(ids) != 1}
        proof['unresolved_source_candidates'] = ambiguous
        if ambiguous:
            proof.update(result='FAIL', reason='Target occurrences require unique geometric source identities')
            proof['matching'] = {}
    proof.update(scope='world vertex sets, face counts and closed-topology observations',length_tolerance=tolerance,
                 matches=[dict(source_id=source[i]['id'],target_id=target[j]['id'],residual=residuals[i,j]) for i,j in proof['matching'].items()])
    return proof


def check_world_envelope(points,allowed_bounds,*,length_tolerance):
    """Report caller-defined source-envelope conditions; never delete/classify a part."""
    tolerance=_tolerance(length_tolerance);points=[vector(p) for p in points]
    if not points or len(allowed_bounds)!=3:raise ValueError('Points and three explicit bounds required')
    bounds=[vector(v,2) for v in allowed_bounds]
    if any(a>b for a,b in bounds):raise ValueError('Ordered source-envelope bounds required')
    actual=_bounds(points)
    contained=all(a>=lo-tolerance and b<=hi+tolerance for (a,b),(lo,hi) in zip(actual,bounds))
    disjoint=any(b<lo-tolerance or a>hi+tolerance for (a,b),(lo,hi) in zip(actual,bounds))
    return dict(result='PASS' if contained else 'SOURCE_REVIEW_REQUIRED',actual_bounds=actual,
                allowed_bounds=bounds,disjoint=disjoint,action='Preserve source geometry and record caller review')
