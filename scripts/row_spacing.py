"""Resolve physical stations and check measured planar surface clearances."""

import argparse
import json
import math
from pathlib import Path

from batch_request import LENGTH_MM, normalize
from planar_positions import MAX_POSITIONS, generate, region_boundary, Segment
from cadtools.geometry import vector
from cadtools.runtime import CadError


MAX_SURFACE_CHECKS = 4096
MAX_VERTEX_PAIRS = 100000


def length(value, unit):
    if isinstance(value, dict):
        amount = normalize(value, unit)
        if amount["unit"] != unit:
            raise ValueError("Expected a length quantity")
        value = amount["value"]
    if type(value) not in (float, int) or not math.isfinite(value) or value < 0:
        raise ValueError(f"Expected finite nonnegative length, got {value}")
    return value


def measure_shapes(first, second, direction):
    """Measure two placed plane profiles. Directed clearance is first contact under translation."""
    from shapely.geometry import MultiPoint, Point, LineString
    from shapely.ops import nearest_points

    a, ra = region_boundary(first)
    b, rb = region_boundary(second)
    radius = (ra or 0) + (rb or 0)
    if direction is None:
        return max(0, a.distance(b) - radius)
    dx, dy = direction
    norm = math.hypot(dx, dy)
    if not norm or not math.isfinite(norm):
        raise ValueError("Specify a finite in-plane measurement direction")
    dx, dy = dx / norm, dy / norm

    # Configuration obstacle for translating B toward A along -direction.
    def vertices(shape):
        if shape.geom_type == "Point":
            return list(shape.coords)
        if not shape.equals(shape.convex_hull):
            raise ValueError("Directed measurement requires convex outlines")
        return list(shape.exterior.coords)[:-1]

    av, bv = vertices(a), vertices(b)
    if len(av) * len(bv) > 100000:
        raise ValueError("Directed measurement exceeds 100000 vertex pairs")
    obstacle = MultiPoint([(x - u, y - v) for x, y in bv for u, v in av]).convex_hull
    if obstacle.distance(Point(0, 0)) <= radius:
        return 0.0
    extent = (
        max(
            math.hypot(x, y)
            for x in obstacle.bounds[::2]
            for y in obstacle.bounds[1::2]
        )
        + radius
        + 1
    )
    ray = LineString([(0, 0), (extent * dx, extent * dy)])
    if obstacle.distance(ray) > radius:
        raise ValueError("Facing surfaces do not meet along the named direction")
    hit = nearest_points(ray, obstacle)[0]
    hi = ray.project(hit)
    if radius == 0:
        return ray.project(nearest_points(Point(0, 0), ray.intersection(obstacle))[1])
    lo = 0.0
    for _ in range(64):
        mid = (lo + hi) / 2
        if obstacle.distance(Point(mid * dx, mid * dy)) <= radius:
            hi = mid
        else:
            lo = mid
    return hi


def resolve(spec):
    unit = spec["unit"]
    if unit not in LENGTH_MM:
        raise ValueError("Unsupported length unit")

    def quantity(key):
        return length(spec[key], unit)

    tol = quantity("tolerance")
    if not tol:
        raise ValueError("Tolerance must be positive")
    path = Segment(spec["segment"], tol)
    span = path.length
    if not math.isfinite(span):
        raise ValueError("Path length exceeds numeric range")
    closed = (path.kind == "arc" and abs(path.sweep) == math.tau) or (
        path.kind == "bezier" and math.dist(path.controls[0], path.controls[-1]) <= tol
    )
    count = spec.get("count")
    if "count" in spec and (type(count) is not int or not 1 <= count <= MAX_POSITIONS):
        raise ValueError("Count must be a positive integer within the position limit")
    start, end = [length(v, unit) for v in spec["margins"]]
    faces = spec["margin_reference"] == "face"
    if spec["margin_reference"] not in ("face", "centre"):
        raise ValueError("Choose face or centre margins")
    if closed and (start or end or faces):
        raise ValueError("Closed rows have a seam and zero centre margins")
    raw = spec.get("width", 0)
    if isinstance(raw, list) and (not raw or len(raw) != count):
        raise ValueError(
            "Supply one width per counted element or a shared scalar width"
        )
    widths = [length(v, unit) for v in (raw if isinstance(raw, list) else [raw])]
    if path.kind != "line" and any(widths):
        raise ValueError(
            "Widths along a curved reference require placed profile checks"
        )
    endpoints = spec["include_endpoints"]
    if (
        not isinstance(endpoints, list)
        or len(endpoints) != 2
        or any(type(e) is not bool for e in endpoints)
    ):
        raise ValueError("Specify start and end inclusion as two booleans")
    if closed and endpoints != [True, False]:
        raise ValueError("Include the starting seam once")
    fixed = "pitch" in spec or "gap" in spec
    face_gap = "gap" in spec
    if (
        face_gap or faces or spec.get("containment") == "complete"
    ) and "width" not in spec:
        raise ValueError(
            "Face measurements and complete containment require a measured width"
        )
    if face_gap and path.kind != "line":
        raise ValueError("Use measured placed outlines for curved-element clearance")
    if spec.get("containment", "centre") not in ("centre", "complete"):
        raise ValueError("Choose centre or complete containment")
    if face_gap and "pitch" in spec:
        raise ValueError(
            f"Conflicting pitch {spec['pitch']} and face gap {spec['gap']}"
        )
    value = quantity("gap" if face_gap else "pitch") if fixed else None
    policy = spec["remainder"]
    if policy not in ("end", "split", "fit"):
        raise ValueError("Choose end, split or fit remainder")
    if not fixed and (count is None or policy != "fit"):
        raise ValueError("Fitted pitch requires count and fit remainder")
    left = start + (widths[0] / 2 if faces else 0)
    right = span - end - (widths[-1] / 2 if faces else 0)
    available = right - left
    excluded = 0 if closed else endpoints.count(False)
    if face_gap and excluded:
        raise ValueError(
            "Use explicit border margins for a face gap with excluded anchors"
        )
    if count is None:
        if policy == "fit":
            raise ValueError("Fit requires an explicit count")
        step = value + (widths[0] if face_gap else 0)
        if step <= tol:
            raise ValueError("Repeat pitch must exceed tolerance")
        count = math.floor((available + tol) / step) + (0 if closed else 1 - excluded)
        if not 1 <= count <= MAX_POSITIONS:
            raise ValueError(f"Repeat count {count} outside supported range")
    if len(widths) == 1:
        widths *= count
    intervals = count if closed else count - 1
    if count == 1 and not closed:
        anchor = spec.get("anchor")
        if anchor not in ("start", "centre", "end"):
            raise ValueError("A single element needs a start, centre or end anchor")
        if (anchor == "start" and not endpoints[0]) or (
            anchor == "end" and not endpoints[1]
        ):
            raise ValueError("Single anchor conflicts with endpoint exclusion")
        if available < -tol:
            raise ValueError("Element exceeds border span")
        stations = [left + {"start": 0, "centre": 0.5, "end": 1}[anchor] * available]
    else:
        if not fixed:
            value = available / (intervals + excluded)
        steps = [
            value + ((widths[i] / 2 + widths[(i + 1) % count] / 2) if face_gap else 0)
            for i in range(intervals)
        ]
        if min(steps) <= tol:
            raise ValueError("Centre spacing must exceed tolerance")
        unused = available - math.fsum(steps) - excluded * value
        if unused < -tol or policy == "fit" and abs(unused) > tol:
            raise ValueError(
                f"Span {available} conflicts with count {count}, spacing {value}, residual {unused} {unit}"
            )
        if closed and policy == "split" and count > 1:
            steps[0] += unused / 2
        stations = [
            left
            + (value if not endpoints[0] else 0)
            + (unused / 2 if policy == "split" and not closed else 0)
        ]
        for step in steps[: count - 1]:
            stations.append(stations[-1] + step)
    if any(not math.isfinite(s) or s < -tol or s > span + tol for s in stations):
        raise ValueError("Computed station exceeds the measured span")
    stations = [min(span, max(0, s)) for s in stations]
    positions = [
        {"id": f"P{i + 1}", "xy": path.point(path.at_distance(s))}
        for i, s in enumerate(stations)
    ]
    result = generate(dict(spec, kind="explicit", positions=positions, tolerance=tol))
    frame = result["frame"]
    for row in result["positions"]:
        offset = [v - u for v, u in zip(row["xyz"], frame["origin"])]
        reconstructed = [
            math.fsum(v * d for v, d in zip(offset, frame[axis])) for axis in ("x", "y")
        ]
        error = math.dist(reconstructed, row["xy"])
        if not math.isfinite(error) or error > tol:
            raise ValueError(
                f"World coordinates of {row['id']} exceed the placement tolerance"
            )
    rows = result["positions"]
    pairs = list(zip(rows, rows[1:]))
    if closed and count > 1:
        pairs.append((rows[-1], rows[0]))
    for first, second in pairs:
        local_chord = math.dist(first["xy"], second["xy"])
        world_chord = math.dist(first["xyz"], second["xyz"])
        if not math.isfinite(world_chord) or abs(local_chord - world_chord) > tol:
            raise ValueError(
                f"World spacing of {first['id']} and {second['id']} exceeds tolerance"
            )
    pitches = [b - a for a, b in zip(stations, stations[1:])]
    if closed:
        pitches.append(span - stations[-1] + stations[0])
    margins = [
        stations[0] - (widths[0] / 2 if faces else 0),
        span - stations[-1] - (widths[-1] / 2 if faces else 0),
    ]
    if spec.get("containment") == "complete" and any(
        s - w / 2 < -tol or s + w / 2 > span + tol for s, w in zip(stations, widths)
    ):
        raise ValueError("Complete element crosses a border")
    result.update(
        count=count,
        stations=stations,
        pitches=pitches,
        intervals=len(pitches),
        margins=margins,
        gaps=[
            p - (widths[i] / 2 + widths[(i + 1) % count] / 2)
            for i, p in enumerate(pitches)
        ]
        if path.kind == "line" and "width" in spec
        else [],
    )
    return result


def round_gap(a, b, direction, unit):
    dimensions = 3 if a["kind"] == "sphere" else 2
    centres = [vector(shape["centre"], dimensions) for shape in (a, b)]
    delta = [v - u for u, v in zip(*centres)]
    radius = sum(length(shape["radius"], unit) for shape in (a, b))
    distance = math.hypot(*delta)
    if not all(math.isfinite(v) for v in (distance, radius)):
        raise ValueError("Profile separation exceeds numeric range")
    if direction is None:
        return max(0, distance - radius)
    axis = vector(direction, dimensions)
    norm = math.hypot(*axis)
    if not math.isfinite(norm) or not norm:
        raise ValueError("Specify a nonzero world direction")
    if distance <= radius:
        return 0.0
    axis = [x / norm for x in axis]
    along = sum(x * y for x, y in zip(delta, axis))
    across = math.hypot(*(x - along * y for x, y in zip(delta, axis)))
    if across > radius or along < 0:
        raise ValueError("Facing spheres do not meet along the named direction")
    axial_contact = (
        (radius * math.sqrt((1 - across / radius) * (1 + across / radius)))
        if radius
        else 0.0
    )
    return max(0.0, along - axial_contact)


def run(spec):
    if spec.get("kind") != "surface_check":
        return resolve(spec)
    if spec["unit"] not in LENGTH_MM:
        raise ValueError("Unsupported length unit")
    if (
        not isinstance(spec["reference"], str)
        or not spec["reference"].strip()
        or not spec["checks"]
    ):
        raise ValueError("Supply the placed geometry reference and at least one pair")
    checks = spec["checks"]
    if not isinstance(checks, list) or len(checks) > MAX_SURFACE_CHECKS:
        raise ValueError(f"Surface checks exceed {MAX_SURFACE_CHECKS}")
    work = 0
    for check in checks:
        pair = check["pair"]
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError("Select exactly two profile IDs")
        profiles = [spec["profiles"][key] for key in pair]
        work += math.prod(
            len(p["vertices"]) if p["kind"] == "polygon" else 1 for p in profiles
        )
        if work > MAX_VERTEX_PAIRS:
            raise ValueError(
                f"Surface checks exceed {MAX_VERTEX_PAIRS} aggregate vertex pairs"
            )
    tolerance = length(spec["tolerance"], spec["unit"])
    result = []
    for check in spec["checks"]:
        a, b = check["pair"]
        if a == b:
            raise ValueError("Select two different profiles")
        metric = check["metric"]
        if metric not in ("directed", "shortest"):
            raise ValueError("Specify directed or shortest clearance")
        direction = check["direction"] if metric == "directed" else None
        if metric == "directed" and direction is None:
            raise ValueError("Supply the named measurement direction")
        first, second = (spec["profiles"][key] for key in (a, b))
        if first["kind"] == second["kind"] and first["kind"] in ("sphere", "circle"):
            measured = round_gap(first, second, direction, spec["unit"])
        else:
            measured = measure_shapes(first, second, direction)
        expected = length(check["expected"], spec["unit"])
        if not math.isfinite(measured) or abs(measured - expected) > tolerance:
            raise ValueError(
                f"{a} to {b}: measured {measured}, requested {expected} {spec['unit']}"
            )
        result.append(
            dict(
                pair=[a, b],
                metric=metric,
                measured=measured,
                expected=expected,
                tolerance=tolerance,
                direction=direction,
            )
        )
    return dict(reference=spec["reference"], unit=spec["unit"], checks=result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    args = parser.parse_args()
    try:
        print(
            json.dumps(
                run(json.loads(args.request.read_text())), indent=2, allow_nan=False
            )
        )
    except (
        ValueError,
        TypeError,
        KeyError,
        OSError,
        ImportError,
        OverflowError,
        CadError,
    ) as exc:
        parser.exit(2, f"Spacing request: {exc}\n")
