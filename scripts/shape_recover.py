"""Recover an axis-aligned prismatic mesh as editable planar profiles in mm."""

import argparse
import hashlib
import json
import math
from pathlib import Path


def load_mesh(path, unit):
    import numpy as np
    import open3d as o3d

    factor = {"mm": 1.0, "m": 1000.0, "inch": 25.4}[unit]
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    mesh = o3d.io.read_triangle_mesh(str(path))
    if not mesh.has_triangles() or not np.isfinite(np.asarray(mesh.vertices)).all():
        raise ValueError("A finite triangle mesh is required")
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise ValueError("Input mesh changed during reading")
    mesh.remove_duplicated_vertices()
    mesh.scale(factor, [0, 0, 0])
    return mesh, digest


def classify_ring(coords, tolerance):
    import numpy as np
    from shapely.geometry import Polygon

    points = np.array(coords[:-1])
    ring = {"kind": "polygon", "points_mm": points.tolist()}
    if len(points) < 8:
        return ring
    # Compare with the actual faceted circle that OpenSCAD will regenerate.
    mean = points.mean(axis=0)
    delta = points - mean
    design = np.column_stack([2 * delta, np.ones(len(points))])
    fit, _, rank, _ = np.linalg.lstsq(design, np.sum(delta**2, axis=1), rcond=None)
    if rank != 3:
        return ring
    centre = mean + fit[:2]
    delta = points - centre
    radius = np.linalg.norm(delta, axis=1).mean()
    angle = math.atan2(delta[0, 1], delta[0, 0])
    theta = angle + np.arange(len(points)) * (2 * math.pi / len(points))
    predicted = centre + radius * np.column_stack([np.cos(theta), np.sin(theta)])
    residual = Polygon(predicted).boundary.hausdorff_distance(Polygon(points).boundary)
    if residual > tolerance:
        return ring
    return dict(
        kind="faceted-circle",
        center_mm=centre.tolist(),
        diameter_mm=2 * radius,
        facets=len(points),
        start_angle_deg=math.degrees(angle),
        fit_error_mm=residual,
    )


def recover(path, unit, axis, tolerance):
    import numpy as np
    from shapely.geometry import LineString, Polygon
    from shapely.ops import unary_union
    from mesh_checks import triangle_mesh_check

    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("A positive finite surface tolerance in mm is required")
    mesh, digest = load_mesh(path, unit)
    if not mesh.is_watertight():
        raise ValueError("A watertight non-intersecting solid is required")
    vertices = np.asarray(mesh.vertices)
    faces = np.asarray(mesh.triangles)
    check = triangle_mesh_check(
        vertices.tolist(), faces.tolist(), minimum_area=0, require_closed=True
    )
    if check["result"] != "PASS":
        raise ValueError(
            "Mesh contains degenerate, duplicate or inconsistently oriented faces"
        )
    # Each cyclic permutation preserves handedness: local (u,v,w) -> mesh (x,y,z).
    axes = {"x": [1, 2, 0], "y": [2, 0, 1], "z": [0, 1, 2]}[axis]
    local = vertices[:, axes]
    low, high = local[:, 2].min(), local[:, 2].max()
    if high - low <= 2 * tolerance:
        raise ValueError("Extrusion thickness cannot be resolved at this tolerance")
    bottom = abs(local[:, 2] - low) <= tolerance
    top = abs(local[:, 2] - high) <= tolerance
    if not (bottom | top).all():
        raise ValueError("Intermediate levels require a different feature model")
    caps = []
    for side in (bottom, top):
        cap_faces = faces[side[faces].all(axis=1)]
        polygons = [Polygon(local[face, :2]) for face in cap_faces]
        cap = unary_union(polygons)
        if cap.geom_type != "Polygon" or cap.is_empty or not cap.is_valid:
            raise ValueError("Each cap must be a single connected profile")
        caps.append(cap)
    lower, upper = caps
    error = lower.boundary.hausdorff_distance(upper.boundary)
    if len(lower.interiors) != len(upper.interiors) or error > tolerance:
        raise ValueError("End profiles differ beyond the modeling tolerance")
    # A twist or crossed pairing may share cap profiles but have oblique walls.
    wall_band = lower.boundary.buffer(tolerance)
    wall_faces = faces[~(bottom[faces].all(axis=1) | top[faces].all(axis=1))]
    for face in wall_faces:
        xy = local[face, :2]
        if not wall_band.covers(LineString([*xy, xy[0]])):
            raise ValueError("Side facets do not follow the extruded cap boundary")
    rings = [
        classify_ring(r.coords, tolerance) for r in [lower.exterior, *lower.interiors]
    ]
    return dict(
        source_sha256=digest,
        unit="mm",
        input_unit=unit,
        extrusion_axis=axis,
        uvw_axes=["xyz"[i] for i in axes],
        base_mm=low,
        thickness_mm=high - low,
        cap_boundary_error_mm=error,
        tolerance_mm=tolerance,
        profiles=rings,
    )


def scad_source(features):
    # OpenSCAD apply a proper rotation from the recovered local axes to the mesh frame.
    # Matrix explicitly assigns each column of local (u,v,w) to its source axis.
    axes = features["uvw_axes"]
    matrix = [[int(name == axis) for name in axes] + [0] for axis in "xyz"] + [
        [0, 0, 0, 1]
    ]

    def compact(value):
        return json.dumps(value, allow_nan=False, separators=(",", ":"))

    lines = [f"thickness = {features['thickness_mm']};"]
    for i, ring in enumerate(features["profiles"]):
        if ring["kind"] == "faceted-circle":
            lines.extend(
                [
                    f"center_{i} = {compact(ring['center_mm'])};",
                    f"diameter_{i} = {ring['diameter_mm']};",
                ]
            )
        else:
            lines.append(f"points_{i} = {compact(ring['points_mm'])};")
    lines += [
        f"multmatrix({compact(matrix)}) translate([0,0,{features['base_mm']}])",
        "    linear_extrude(height=thickness) difference() {",
    ]
    for i, ring in enumerate(features["profiles"]):
        if ring["kind"] == "faceted-circle":
            lines.append(
                f"        translate(center_{i}) rotate({ring['start_angle_deg']}) "
                f"circle(d=diameter_{i}, $fn={ring['facets']});"
            )
        else:
            lines.append(f"        polygon(points_{i});")
    return "\n".join(lines + ["    }", ""])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mesh", type=Path)
    parser.add_argument("new_output", type=Path)
    parser.add_argument("--unit", required=True, choices=["mm", "inch", "m"])
    parser.add_argument("--axis", required=True, choices=["x", "y", "z"])
    parser.add_argument("--tolerance-mm", type=float, required=True)
    args = parser.parse_args()
    features = recover(args.mesh, args.unit, args.axis, args.tolerance_mm)
    code = scad_source(features)
    args.new_output.mkdir()
    (args.new_output / "profile.scad").write_text(code)
    (args.new_output / "features.json").write_text(
        json.dumps(features, indent=2, allow_nan=False) + "\n"
    )


if __name__ == "__main__":
    main()
