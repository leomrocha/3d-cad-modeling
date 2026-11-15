"""Offline, geometry-bound assembly occurrence and world-vertex verification.

Inputs share caller-declared XYZ frames/length units. Matrix linear tolerances
are dimensionless; translation and point tolerances use the length unit.
"""
import math
from cadtools.geometry import finite,vector
from solid_transfer import verify_solid_transfer
from step_placements import solid_instances


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


def match_world_vertices(source,target,*,length_tolerance,max_instances=10000):
    """Match point sets, face counts and closed flags with repeated-instance multiplicity.

    Each row has id, points, face_count and closed. This compares vertices and
    topology observations; analytic surface equations retain separate checks.
    """
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
