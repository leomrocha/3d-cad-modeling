"""Derive an exact circular-arc profile for a spherical-seat shaft transition.

The function is a geometry-only helper. Callers supply all dimensions and
decide whether its nominal blend radius is supported by their source evidence.
Returned points use the radial/axial plane (radius, z); bulges use the OCS
LWPOLYLINE convention and preserve the sign of each exact circular arc.
"""

import math


_INPUTS = (
    "sphere_radius", "sphere_center_z", "collar_radius", "collar_start_z",
    "shaft_radius", "blend_radius", "shaft_end_z",
)


def _finite_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(name + " must be a finite number")
    try:
        value = float(value)
    except (OverflowError, ValueError):
        raise ValueError(name + " must be a finite number") from None
    if not math.isfinite(value):
        raise ValueError(name + " must be a finite number")
    return value


def _finite_result(value, name):
    if not math.isfinite(value):
        raise ValueError(name + " overflowed or is nonfinite")
    return value


def _sweep(start, end, center, label):
    """Return the signed shortest circular sweep between two points."""
    sx, sy = start[0] - center[0], start[1] - center[1]
    ex, ey = end[0] - center[0], end[1] - center[1]
    cross = _finite_result(sx * ey - sy * ex, label + " cross product")
    dot = _finite_result(sx * ex + sy * ey, label + " dot product")
    sweep = math.atan2(cross, dot)
    if not math.isfinite(sweep) or sweep == 0 or abs(sweep) >= math.pi:
        raise ValueError(label + " arc sweep must be finite, nonzero and below 180 degrees")
    return sweep


def spherical_seat_profile(*, sphere_radius, sphere_center_z, collar_radius,
                            collar_start_z, shaft_radius, blend_radius,
                            shaft_end_z):
    """Return an ordered closed (radius, z) profile and exact arc bulges.

    Arc indices identify the outgoing segment from that point: index 2 is the
    spherical surface and index 3 is the shaft blend. All dimensions must use
    one consistent unit. The axial sequence follows the upper, right-side
    contour from the collar's lower edge toward the shaft tip.
    """
    supplied = {
        "sphere_radius": sphere_radius,
        "sphere_center_z": sphere_center_z,
        "collar_radius": collar_radius,
        "collar_start_z": collar_start_z,
        "shaft_radius": shaft_radius,
        "blend_radius": blend_radius,
        "shaft_end_z": shaft_end_z,
    }
    values = {name: _finite_number(supplied[name], name) for name in _INPUTS}
    R = values["sphere_radius"]
    zc = values["sphere_center_z"]
    collar = values["collar_radius"]
    z0 = values["collar_start_z"]
    shaft = values["shaft_radius"]
    blend = values["blend_radius"]
    ztip = values["shaft_end_z"]

    if R <= 0 or collar <= 0 or shaft <= 0 or blend <= 0:
        raise ValueError("sphere, collar, shaft and blend radii must be positive")
    if not shaft < collar < R:
        raise ValueError("radii must satisfy 0 < shaft_radius < collar_radius < sphere_radius")

    collar_sq = _finite_result(collar * collar, "collar radius square")
    sphere_sq = _finite_result(R * R, "sphere radius square")
    intersection_sq = _finite_result(sphere_sq - collar_sq,
                                     "sphere/collar intersection square")
    if intersection_sq <= 0:
        raise ValueError("sphere and collar intersection collapses")
    z_intersection = _finite_result(zc + math.sqrt(intersection_sq),
                                    "sphere/collar intersection z")

    rbc = _finite_result(shaft + blend, "blend centre radius")
    sum_radius = _finite_result(R + blend, "sphere/blend tangent radius")
    tangent_sq = _finite_result(sum_radius * sum_radius - rbc * rbc,
                                "sphere/blend tangent square")
    if tangent_sq <= 0:
        raise ValueError("sphere/blend tangent centre is invalid or collapsed")
    zbc = _finite_result(zc + math.sqrt(tangent_sq), "blend centre z")

    denominator = _finite_result(R + blend, "sphere/blend tangent denominator")
    sphere_contact_r = _finite_result(R * rbc / denominator,
                                      "sphere contact radius")
    sphere_contact_z = _finite_result(
        zc + R * (zbc - zc) / denominator, "sphere contact z")
    sphere_contact = [sphere_contact_r, sphere_contact_z]
    blend_contact = [shaft, zbc]

    if not shaft < sphere_contact_r < collar:
        raise ValueError("tangent contact radius does not lie between shaft and collar")
    if not z0 < z_intersection < sphere_contact_z < zbc < ztip:
        raise ValueError("profile axial stations must be strictly increasing")

    points = [
        [0.0, z0],
        [collar, z0],
        [collar, z_intersection],
        sphere_contact,
        blend_contact,
        [shaft, ztip],
        [0.0, ztip],
    ]
    if any(not math.isfinite(coord) for point in points for coord in point):
        raise ValueError("profile coordinates must be finite")
    if any(a == b for a, b in zip(points, points[1:])) or points[-1] == points[0]:
        raise ValueError("profile contains collapsed adjacent or closing vertices")

    sphere_center = [0.0, zc]
    blend_center = [rbc, zbc]
    sphere_sweep = _sweep(points[2], points[3], sphere_center, "sphere")
    blend_sweep = _sweep(points[3], points[4], blend_center, "blend")
    bulges = {
        2: _finite_result(math.tan(sphere_sweep / 4), "sphere arc bulge"),
        3: _finite_result(math.tan(blend_sweep / 4), "blend arc bulge"),
    }
    if bulges[2] <= 0 or bulges[3] >= 0:
        raise ValueError("expected a positive sphere arc and a negative blend arc")

    # Verify the two analytic circles meet with aligned tangents at their join.
    sphere_join = math.hypot(points[3][0], points[3][1] - zc)
    blend_join = math.hypot(points[3][0] - rbc, points[3][1] - zbc)
    _finite_result(sphere_join, "sphere contact distance")
    _finite_result(blend_join, "blend contact distance")
    if not math.isclose(sphere_join, R, rel_tol=2e-14, abs_tol=0.0):
        raise ValueError("sphere contact does not lie on the supplied sphere")
    if not math.isclose(blend_join, blend, rel_tol=2e-14, abs_tol=0.0):
        raise ValueError("sphere and blend circles are not tangent at their join")

    return {
        "points": points,
        "bulges": bulges,
        "arc_centers": {2: sphere_center, 3: blend_center},
        "sphere_start": points[2],
        "sphere_contact": sphere_contact,
        "blend_contact": blend_contact,
        "blend_center": blend_center,
        "derived": {
            "sphere_collar_intersection_z": z_intersection,
            "blend_center": blend_center,
            "sphere_contact": sphere_contact,
            "blend_contact": blend_contact,
            "sphere_sweep_radians": sphere_sweep,
            "blend_sweep_radians": blend_sweep,
        },
    }
