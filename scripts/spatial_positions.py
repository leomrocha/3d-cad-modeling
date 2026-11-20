"""Generate read-only placement transforms in measured model frames."""

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

from cadtools.geometry import finite, positive, vector
from cadtools.runtime import CadError
from planar_positions import MAX_POLYGON, MAX_POSITIONS, bounded
from planar_profiles import inside
from profile_reference import validate_profile
from step_placements import apply, classify_hand, cross, dot, eye, multiply, unit

X, Y, Z = [1, 0, 0], [0, 1, 0], [0, 0, 1]


def values(spec, key):
    items = spec[key]
    if not isinstance(items, list) or not items:
        raise ValueError(f"{key} requires a nonempty list")
    bounded(len(items), MAX_POSITIONS, key)
    numbers = [finite(v) for v in items]
    if len(set(numbers)) != len(numbers):
        raise ValueError(f"Repeated {key}")
    return numbers


def between(items, low, high):
    if any(v < low or v > high for v in items):
        raise ValueError(f"Coordinate outside [{low}, {high}]")
    return items


def direction(values):
    components = vector(values)
    scale = max(abs(c) for c in components)
    if not scale:
        raise ValueError("Nonzero direction required")
    return unit([c / scale for c in components])


def frame(origin, z, x_hint, fallback=None, roll=0):
    z = direction(z)
    x = direction(x_hint)
    if math.hypot(*cross(z, x)) < 1e-10:
        if fallback is None:
            raise ValueError(
                "Mounting axis and second direction parallel; supply fallback_x"
            )
        x = direction(fallback)
    y = unit(cross(z, x))
    x = cross(y, z)
    angle = math.radians(finite(roll))
    x = [a * math.cos(angle) + b * math.sin(angle) for a, b in zip(x, y)]
    matrix = [list(row) for row in zip(x, cross(z, x), z, origin)] + [[0, 0, 0, 1]]
    classify_hand(matrix)
    return matrix


def prism(spec):
    height = positive(spec["height"])
    vertices = spec["vertices"]
    bounded(len(vertices), MAX_POLYGON, "Prism vertices")
    vertices = validate_profile(vertices)
    mode = spec["mode"]
    if mode in ("side", "rim", "upright"):
        side = spec["side"]
        if type(side) is not int or not 0 <= side < len(vertices):
            raise ValueError("Invalid prism side")
        a, b = vertices[side], vertices[(side + 1) % len(vertices)]
        tangent = direction([b[0] - a[0], b[1] - a[1], 0])
        origin = vertices[0]
        span = max(abs(v[i] - origin[i]) for v in vertices for i in range(2))
        relative = [[(v[i] - origin[i]) / span for i in range(2)] for v in vertices]
        area2 = math.fsum(
            p[0] * q[1] - p[1] * q[0]
            for p, q in zip(relative, relative[1:] + relative[:1])
        )
        sign = 1 if area2 > 0 else -1
        normal = [sign * tangent[1], -sign * tangent[0], 0] if mode == "side" else None
        stations = (
            [0]
            if mode == "upright"
            else between(values(spec, "stations"), 0, math.dist(a, b))
        )
        levels = between(values(spec, "levels"), 0, height)
        if mode == "rim" and any(z not in (0, height) for z in levels):
            raise ValueError("Rim level must select an end face")
        bounded(len(stations) * len(levels), MAX_POSITIONS, "Face candidates")
        for z in levels:
            for s in stations:
                yield (
                    [a[0] + s * tangent[0], a[1] + s * tangent[1], z],
                    normal,
                    Z if mode == "upright" else tangent,
                )
    elif mode in ("volume", "cap"):
        xs, ys = values(spec, "columns"), values(spec, "rows")
        levels = between(values(spec, "levels"), 0, height)
        if mode == "cap" and any(z not in (0, height) for z in levels):
            raise ValueError("Cap level must select an end face")
        bounded(len(xs) * len(ys) * len(levels), MAX_POSITIONS, "Volume candidates")
        edges = list(zip(vertices, vertices[1:] + vertices[:1]))
        for z in levels:
            normal = ([0, 0, -1] if z == 0 else Z) if mode == "cap" else None
            for y in ys:
                for x in xs:
                    if inside([x, y], vertices) or any(
                        on_edge(x, y, a, b) for a, b in edges
                    ):
                        yield [x, y, z], normal, X
    else:
        raise ValueError("Unknown prism selection")


def on_edge(x, y, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    span = max(abs(dx), abs(dy))
    left = (dx / span) * ((y - a[1]) / span)
    right = (dy / span) * ((x - a[0]) / span)
    # Subtracting decimal coordinates and multiplying rounds both products.
    error = 8 * math.ulp(max(abs(left), abs(right)))
    return (
        abs(left - right) <= error
        and min(a[0], b[0]) <= x <= max(a[0], b[0])
        and min(a[1], b[1]) <= y <= max(a[1], b[1])
    )


def curved(spec):
    radius = positive(spec["radius"])
    sphere = spec["kind"] == "sphere"
    if sphere:
        rings = spec["rings"]
        bounded(len(rings), MAX_POSITIONS, "Sphere rings")
    else:
        levels = between(values(spec, "levels"), 0, positive(spec["height"]))
        rings = [{"level": z} for z in levels]
    seen = set()
    examined = 0
    for ring in rings:
        coordinate = (
            between([finite(ring["latitude_deg"])], -90, 90)[0]
            if sphere
            else ring["level"]
        )
        pole = sphere and abs(coordinate) == 90
        angles = ring.get("angles_deg", spec.get("angles_deg"))
        if not isinstance(angles, list) or not angles:
            raise ValueError("Supply angular coordinates")
        examined += len(angles)
        bounded(examined, MAX_POSITIONS, "Angular candidates")
        lat = math.radians(coordinate) if sphere else 0
        for raw in angles:
            # Reduce decimal input before conversion to a binary angle.
            angle = float(Fraction(str(finite(raw))) % 360) % 360
            # All meridians at a pole use the zero meridian frame.
            key = (coordinate, 0 if pole else angle)
            if key in seen:
                continue
            seen.add(key)
            lon = math.radians(key[1])
            radial = [math.cos(lon), math.sin(lon), 0]
            tangent = [-radial[1], radial[0], 0]
            if sphere:
                normal = (
                    [0, 0, math.copysign(1, coordinate)]
                    if pole
                    else [
                        radial[0] * math.cos(lat),
                        radial[1] * math.cos(lat),
                        math.sin(lat),
                    ]
                )
                point = [radius * a for a in normal]
            else:
                normal = radial
                point = [radius * radial[0], radius * radial[1], coordinate]
            yield point, normal, tangent


def generate(spec):
    if (
        spec["unit"] not in ("mm", "cm", "m", "in", "ft")
        or not isinstance(spec["reference"], str)
        or not spec["reference"].strip()
    ):
        raise ValueError("Supply length unit and measured reference")
    reference = spec["frame"]
    host = frame(vector(reference["origin"]), reference["axis"], reference["meridian"])
    parent = spec.get("parent_to_world", eye())
    classify_hand(parent)
    kind = spec["kind"]
    if kind not in ("prism", "cylinder", "sphere"):
        raise ValueError("Unsupported geometry")
    samples = prism(spec) if kind == "prism" else curved(spec)
    orientation = spec["orientation"]
    positions = []
    for i, (point, normal, tangent) in enumerate(samples, 1):
        radial = [point[0], point[1], 0]
        centre = vector(orientation.get("centre", [0, 0, 0]))
        from_centre = [a - b for a, b in zip(point, centre)]
        path = orientation.get("path", "azimuth")
        along = tangent
        if orientation["mode"] == "tangent" and kind != "prism":
            if path == "axial" and kind == "cylinder":
                along = Z
            elif path == "meridian" and kind == "sphere":
                along = cross(normal, tangent)
            elif path != "azimuth":
                raise ValueError("Unsupported tangent path")
        directions = {
            "fixed": orientation.get("z"),
            "normal": normal,
            "tangent": along,
            "away_axis": radial,
            "toward_axis": [-v for v in radial],
            "away_centre": from_centre,
            "toward_centre": [-v for v in from_centre],
        }
        z = directions.get(orientation["mode"])
        if z is None:
            raise ValueError(
                "Requested mounting direction unavailable for selected geometry"
            )
        second = orientation["x"]
        if second == "azimuth":
            if kind == "prism":
                raise ValueError("Azimuth direction requires a cylinder or sphere")
            second = tangent
        local = frame(
            point,
            z,
            second,
            orientation.get("fallback_x"),
            orientation.get("roll_deg", 0),
        )
        in_parent = multiply(host, local)
        world = multiply(parent, in_parent)
        positions.append(
            {
                "id": f"P{i:04d}",
                "local_xyz": point,
                "xyz": apply(world, [0, 0, 0]),
                "parent_transform": in_parent,
                "world_transform": world,
                "hand": classify_hand(world),
            }
        )
    if not positions:
        raise ValueError("Selection produced zero positions")
    return {
        "unit": spec["unit"],
        "reference": spec["reference"],
        "positions": positions,
        "measurements": measure(spec, positions),
    }


def measure(spec, positions):
    points = {p["id"]: p for p in positions}
    checks = spec.get("checks", [])
    bounded(len(checks), MAX_POSITIONS, "Neighbour checks")
    result = []
    for check in checks:
        first, second = [points[k] for k in check["pair"]]
        a, b = first["local_xyz"], second["local_xyz"]
        metric = check["metric"]
        if metric == "chord":
            distance = math.dist(first["xyz"], second["xyz"])
        elif metric == "great_circle" and spec["kind"] == "sphere":
            u, v = direction(a), direction(b)
            distance = spec["radius"] * math.atan2(math.hypot(*cross(u, v)), dot(u, v))
        elif metric == "latitude_arc" and spec["kind"] == "sphere" and a[2] == b[2]:
            distance = azimuth_arc(a, b)
        elif metric == "cylinder_surface" and spec["kind"] == "cylinder":
            distance = math.hypot(azimuth_arc(a, b), a[2] - b[2])
        else:
            raise ValueError("Metric incompatible with selected geometry or pair")
        target = finite(check["distance"])
        tolerance = finite(check["tolerance"])
        if (
            not math.isfinite(distance)
            or min(target, tolerance) < 0
            or abs(distance - target) > tolerance
        ):
            raise ValueError(
                f"{check['pair']} {metric}: measured {distance}, requested {target} +/- {tolerance}"
            )
        result.append({"pair": check["pair"], "metric": metric, "distance": distance})
    return result


def azimuth_arc(a, b):
    delta = math.atan2(a[1], a[0]) - math.atan2(b[1], b[0])
    return math.hypot(*a[:2]) * abs(math.remainder(delta, math.tau))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    args = parser.parse_args()
    try:
        print(
            json.dumps(generate(json.loads(args.request.read_text())), allow_nan=False)
        )
    except (ArithmeticError, ValueError, TypeError, KeyError, OSError, CadError) as exc:
        parser.exit(2, f"Spatial positions: {exc}\n")
