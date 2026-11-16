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
