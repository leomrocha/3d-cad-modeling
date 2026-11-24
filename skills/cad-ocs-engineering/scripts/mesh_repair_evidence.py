"""Compare saved triangular OBJ meshes in a common millimetre frame after additive repair."""
import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

from mesh_checks import triangle_mesh_check


def read_mesh(path):
    raw = path.read_bytes()
    points, faces = [], []
    for line in raw.decode().splitlines():
        fields = line.partition("#")[0].split()
        if not fields:
            continue
        if fields[0] == "v":
            if len(fields) != 4:
                raise ValueError("Three millimetre coordinates per vertex required")
            points.append(tuple(map(float, fields[1:])))
        elif fields[0] == "f":
            ids = [int(token.split("/")[0]) for token in fields[1:]]
            if len(ids) != 3 or any(i <= 0 or i > len(points) for i in ids):
                raise ValueError("Expected indexed triangles with positive existing vertex IDs")
            faces.append([i-1 for i in ids])
        elif fields[0] not in {"o", "g", "vn", "vt", "s", "mtllib", "usemtl"}:
            raise ValueError("Unsupported OBJ record: " + fields[0])
    if triangle_mesh_check(points, faces, minimum_area=0)["result"] != "PASS":
        raise ValueError("Invalid source or derivative triangle connectivity")
    return points, faces, hashlib.sha256(raw).hexdigest()


def oriented_key(triangle):
    return min(tuple(triangle[i:] + triangle[:i]) for i in range(3))


def fit_cylinder(points, faces, region):
    """Fit a circle perpendicular to the supplied axis; sample original vertices only."""
    import numpy as np

    ids = region["source_triangles"]
    if not ids or len(set(ids)) != len(ids) or any(type(i) != int or not 0 <= i < len(faces) for i in ids):
        raise ValueError("Expected unique zero-based source triangle indices")
    axis = np.asarray(region["axis"], dtype=float)
    if axis.shape != (3,) or not math.isclose(float(np.linalg.norm(axis)), 1, abs_tol=1e-9):
        raise ValueError("Expected a unit cylinder axis")
    xyz = np.array([points[i] for i in sorted({i for f in ids for i in faces[f]})])
    origin = xyz.mean(axis=0)
    u = np.cross(axis, np.eye(3)[np.argmin(abs(axis))])
    u /= np.linalg.norm(u)
    v = np.cross(axis, u)
    xy = (xyz - origin) @ np.stack((u, v), axis=1)
    if np.ptp((xyz - origin) @ axis) <= 0:
        raise ValueError("Cylinder region needs axial extent")
    system = np.column_stack((2*xy, np.ones(len(xy))))
    solution, _, rank, _ = np.linalg.lstsq(system, (xy*xy).sum(axis=1), rcond=None)
    if rank != 3:
        raise ValueError("Source region does not determine a circular section")
    centre = solution[:2]
    samples = np.linalg.norm(xy-centre, axis=1)
    radius = float(samples.mean())
    return dict(origin="fitted surface", source_triangles=ids, axis=axis.tolist(),
                axis_point_mm=(origin+u*centre[0]+v*centre[1]).tolist(), radius_mm=radius,
                method="circle fit on source vertices perpendicular to supplied axis",
                maximum_sampled_radial_error_mm=float(abs(samples-radius).max()))


def compare(source, derivative, *, cylinder=None):
    points, faces, initial = read_mesh(source)
    saved, result, final = read_mesh(derivative)
    original = {}
    boundary = Counter()
    for i, face in enumerate(faces):
        tri = [points[j] for j in face]
        key = oriented_key(tri)
        if key in original:
            raise ValueError("Ambiguous coincident source triangles")
        original[key] = i
        boundary.update(tuple(sorted((a,b))) for a,b in zip(tri,tri[1:]+tri[:1]))
    retained, added = [], []
    patch_edges = Counter()
    adjacent = {}
    retained_edges = set()
    saved_edges = {}
    for i, face in enumerate(result):
        tri = [saved[j] for j in face]
        old = original.pop(oriented_key(tri), None)
        if old is None:
            added.append(i)
            for corner, (a, b) in enumerate(zip(tri, tri[1:] + tri[:1])):
                saved_edge = tuple(sorted((face[corner], face[(corner+1)%3])))
                edge = tuple(sorted((a, b)))
                saved_edges[edge] = saved_edge
                patch_edges[edge] += 1
                adjacent.setdefault(edge, []).append(i)
        else:
            retained.append(dict(source_triangle=old, saved_triangle=i))
            retained_edges.update(tuple(sorted(pair)) for pair in zip(face,face[1:]+face[:1]))
    if original:
        raise ValueError("Source triangles were moved, removed or reversed")
    rim = sorted(edge for edge,count in patch_edges.items() if count == 1)
    if added and (not rim or any(boundary[edge] != 1 or saved_edges[edge] not in retained_edges for edge in rim)):
        raise ValueError("Added geometry must meet original open boundary edges")
    # Every patch must connect by shared edges to an original opening.
    neighbours = {i:set() for i in added}
    for owners in adjacent.values():
        for i in owners:
            neighbours[i].update(owners)
    pending = [i for edge in rim for i in adjacent[edge]]
    reachable = set()
    while pending:
        i = pending.pop()
        if i not in reachable:
            reachable.add(i)
            pending.extend(neighbours[i] - reachable)
    if reachable != set(added):
        raise ValueError("Detached added geometry has no original boundary")
    evidence = dict(unit="mm", frame="shared OBJ coordinates", source_sha256=initial,
                    saved_sha256=final, index_base=0, original_triangles=retained,
                    repair=dict(operation="added triangles", saved_triangles=added,
                                original_boundary_edges_mm=rim))
    if cylinder is not None:
        evidence["fit"] = fit_cylinder(points, faces, cylinder)
    return evidence


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("derivative", type=Path)
    parser.add_argument("--cylinder", type=Path, help="JSON with source_triangles and a unit axis")
    args = parser.parse_args()
    region = json.loads(args.cylinder.read_bytes()) if args.cylinder else None
    print(json.dumps(compare(args.source, args.derivative, cylinder=region), allow_nan=False))
