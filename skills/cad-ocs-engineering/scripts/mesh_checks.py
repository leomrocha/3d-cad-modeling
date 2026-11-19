"""Offline triangular mesh gates; observations retain caller units and UV frame."""
import math
from collections import Counter
from cadtools.geometry import vector, finite


def triangle_mesh_check(vertices, faces, *, minimum_area, uv_vertices=None,
                        minimum_signed_uv_area=0, require_closed=False):
    """Check finite arrays, indices, duplicates, area and oriented edge incidence.

    Areas use length-unit squared; UV areas use parameter-unit squared. Open
    meshes are supported explicitly. Closure is edge-incidence evidence only;
    self-intersections and global surface/trim coverage have separate checks.
    """
    threshold=finite(minimum_area); uv_threshold=finite(minimum_signed_uv_area)
    if threshold < 0 or uv_threshold < 0 or type(require_closed) is not bool:
        raise ValueError('Nonnegative area criteria and explicit closure flag required')
    xyz=[vector(p) for p in vertices]
    if not xyz or not faces: raise ValueError('Nonempty mesh required')
    uv=None if uv_vertices is None else [vector(p,2) for p in uv_vertices]
    if uv is not None and len(uv) != len(xyz): raise ValueError('UV must correspond to every vertex')
    areas=[]; uv_areas=[]; invalid=[]; zero=[]; collapsed=[]; duplicate=[]; seen=set(); edges=Counter(); oriented=Counter()
    for index,face in enumerate(faces):
        if len(face)!=3 or any(type(i) is not int or not 0<=i<len(xyz) for i in face):
            raise ValueError('Triangle indices must be valid integers')
        a,b,c=face; key=tuple(sorted(face))
        if key in seen: duplicate.append(index)
        seen.add(key)
        x=[xyz[b][k]-xyz[a][k] for k in range(3)]; y=[xyz[c][k]-xyz[a][k] for k in range(3)]
        cross=[x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]
        area=math.hypot(*cross)/2
        if not math.isfinite(area): raise ValueError('Triangle area overflow')
        areas.append(area)
        if area<=threshold: invalid.append(index)
        if area==0: zero.append(index)
        if uv is not None:
            u,v=uv[a],uv[b];w=uv[c]
            signed=((v[0]-u[0])*(w[1]-u[1])-(v[1]-u[1])*(w[0]-u[0]))/2
            if not math.isfinite(signed): raise ValueError('UV area overflow')
            uv_areas.append(signed)
            if signed>uv_threshold and area==0: collapsed.append(index)
        for i,j in ((a,b),(b,c),(c,a)):
            edges[tuple(sorted((i,j)))]+=1;oriented[i,j]+=1
    boundary=sum(v==1 for v in edges.values()); nonmanifold=sum(v>2 for v in edges.values())
    reversed_edges=[list(edge) for edge,count in edges.items() if count==2 and not oriented[edge]==oriented[edge[::-1]]==1]
    closed=bool(edges) and all(v==2 for v in edges.values()) and all(oriented[a,b]==oriented[b,a]==1 for a,b in edges)
    wrong_uv=[i for i,a in enumerate(uv_areas) if a<=uv_threshold]
    passed=not(invalid or duplicate or wrong_uv or nonmanifold or reversed_edges) and (not require_closed or closed)
    return dict(result='PASS' if passed else 'FAIL',vertices=len(xyz),triangles=len(faces),minimum_area=min(areas),
                invalid_area_triangles=invalid,zero_area_triangles=zero,duplicate_triangles=duplicate,
                nonpositive_uv_triangles=wrong_uv,positive_uv_zero_3d_triangles=collapsed,
                boundary_edges=boundary,nonmanifold_edges=nonmanifold,inconsistent_edges=reversed_edges,oriented_edge_closed=closed,
                scope='triangle arrays, numerical area and oriented edge incidence')


def _reachable(adjacency, start):
    seen = {start}
    pending = [start]
    while pending:
        for node in adjacency[pending.pop()]:
            if node not in seen:
                seen.add(node)
                pending.append(node)
    return seen


def _tetrahedron_volume(a, b, c, origin):
    x, y, z = ([p[i] - origin[i] for i in range(3)] for p in (a, b, c))
    return math.fsum((
        x[0] * (y[1] * z[2] - y[2] * z[1]),
        x[1] * (y[2] * z[0] - y[0] * z[2]),
        x[2] * (y[0] * z[1] - y[1] * z[0]),
    )) / 6


def shell_components(vertices, faces, *, minimum_area=0):
    """Inspect already indexed triangular shells in a right-handed Cartesian frame.

    Components use shared vertex indices. A closed manifold requires a single
    cycle in every vertex link as well as oppositely oriented incident faces.
    Signed volumes have units of input length cubed. Their signs characterize
    winding in embedded shells; self-intersections and nesting are separate tests.
    """
    from collections import defaultdict

    vertices = [vector(point) for point in vertices]
    faces = [tuple(face) for face in faces]
    gate = triangle_mesh_check(vertices, faces, minimum_area=minimum_area, require_closed=True)
    vertex_faces = defaultdict(list)
    neighbours = defaultdict(set)
    links = defaultdict(list)
    for index, (a, b, c) in enumerate(faces):
        for v, x, y in ((a, b, c), (b, c, a), (c, a, b)):
            vertex_faces[v].append(index)
            neighbours[v].update((x, y))
            links[v].append((x, y))

    pending = set(vertex_faces)
    components = []
    for first in vertex_faces:
        if first not in pending:
            continue
        used = _reachable(neighbours, first)
        pending.difference_update(used)
        indices = sorted({i for v in used for i in vertex_faces[v]})
        edges = sum(len(neighbours[v]) for v in used) // 2
        singular = []
        for v in sorted(used):
            link = defaultdict(set)
            for x, y in links[v]:
                link[x].add(y)
                link[y].add(x)
            if any(len(adj) != 2 for adj in link.values()) or len(_reachable(link, next(iter(link)))) != len(link):
                singular.append(v)
        # Each component receives its own gate even when another component fails.
        subset = [faces[i] for i in indices]
        if len(subset) == len(faces):
            local_gate = gate
        else:
            local_vertices = sorted(used)
            local_index = {v: i for i, v in enumerate(local_vertices)}
            local_gate = triangle_mesh_check(
                [vertices[v] for v in local_vertices],
                [tuple(local_index[v] for v in tri) for tri in subset],
                minimum_area=minimum_area, require_closed=True)
        closed = local_gate['result'] == 'PASS' and not singular
        volume = None
        if closed:
            volume = math.fsum(_tetrahedron_volume(vertices[a], vertices[b], vertices[c], vertices[first])
                               for a, b, c in subset)
            if not math.isfinite(volume):
                raise ValueError('Nonfinite component volume')
        winding = 'UNDETERMINED'
        if volume is not None:
            winding = 'POSITIVE' if volume > 0 else 'NEGATIVE' if volume < 0 else 'ZERO'
        components.append(dict(first_face=indices[0], vertices=len(used), edges=edges,
                               triangles=len(indices), euler_characteristic=len(used)-edges+len(indices),
                               noncycle_vertex_links=singular, closed_manifold=closed,
                               signed_volume=volume, winding=winding))
    return dict(components=components, unused_vertex_count=len(vertices)-len(vertex_faces))
