"""Generate reusable ordered CAD positions in a measured, oriented plane."""

import argparse
import bisect
import json
import math
from pathlib import Path

from cadtools.geometry import finite, pattern, positive, vector
from cadtools.runtime import CadError
from planar_profiles import add, scale, sub
from profile_reference import validate_profile

MAX_POSITIONS = 20_000
MAX_CIRCLE = 2_048
MAX_POLYGON = 512


def bounded(count, limit, label):
    if count > limit:
        raise ValueError(f"{label} exceeds the per-request limit of {limit}")
    return count


def direction(a, b):
    d = sub(b, a)
    length = math.hypot(*d)
    if not length:
        raise ValueError("A tangent needs a nonzero derivative")
    return scale(d, 1 / length)


class Segment:
    """Directed line, circular arc, or quadratic/cubic Bezier."""

    def __init__(self, spec, tolerance):
        self.kind = spec["kind"]
        self.tol = tolerance
        if self.kind == "arc":
            self.c = vector(spec["centre"], 2)
            self.r = positive(spec["radius"])
            self.start = math.radians(finite(spec["start_deg"]))
            self.sweep = math.radians(finite(spec["sweep_deg"]))
            if not 0 < abs(self.sweep) <= math.tau:
                raise ValueError("Arc sweep must be nonzero and at most one turn")
            self.length = self.r * abs(self.sweep)
        elif self.kind in ("line", "bezier"):
            points = [vector(p, 2) for p in spec["points"]]
            if self.kind == "line":
                self.a, self.b = points
                self.length = math.dist(self.a, self.b)
            else:
                try:
                    from numpy.polynomial import Polynomial
                    from scipy.integrate import quad
                except ImportError as exc:
                    raise ValueError(
                        "Bezier positions require local NumPy and SciPy; use an equipped interpreter or supply measured explicit positions"
                    ) from exc
                self.integrate = quad
                self.controls = points

                if len(points) not in (3, 4):
                    raise ValueError("Use three or four Bezier control points")
                t = Polynomial([0, 1])
                n = len(points) - 1
                basis = [
                    math.comb(n, i) * t**i * (1 - t) ** (n - i) for i in range(n + 1)
                ]
                self.xy = [sum(p[k] * b for p, b in zip(points, basis)) for k in (0, 1)]
                self.derivatives = [p.deriv() for p in self.xy]
                self.length = self.arc_length(1)
        else:
            raise ValueError("Unknown path segment")
        positive(self.length)

    def arc_length(self, t):
        if self.kind != "bezier":
            return t * self.length
        value, error = self.integrate(
            lambda u: math.hypot(*(d(u) for d in self.derivatives)),
            0,
            t,
            epsabs=self.tol / 8,
            epsrel=0,
        )
        if error > self.tol:
            raise ValueError("Bezier arc length exceeds the requested tolerance")
        return value

    def at_distance(self, s):
        if self.kind != "bezier" or s <= 0 or s >= self.length:
            return min(1, max(0, s / self.length))
        from scipy.optimize import brentq

        speed_bound = sum(sum(abs(c) for c in d.coef) for d in self.derivatives)
        return brentq(
            lambda t: self.arc_length(t) - s,
            0,
            1,
            xtol=min(1e-12, self.tol / (4 * speed_bound)),
        )

    def point(self, t):
        if self.kind == "line":
            return add(self.a, scale(sub(self.b, self.a), t))
        if self.kind == "bezier":
            return [float(p(t)) for p in self.xy]
        angle = self.start + t * self.sweep
        return add(self.c, scale([math.cos(angle), math.sin(angle)], self.r))

    def tangent(self, t):
        if self.kind == "line":
            return direction(self.a, self.b)
        if self.kind == "bezier":
            if t == 0:
                return direction(
                    self.controls[0],
                    next(p for p in self.controls if p != self.controls[0]),
                )
            if t == 1:
                return direction(
                    next(p for p in reversed(self.controls) if p != self.controls[-1]),
                    self.controls[-1],
                )
            return direction([0, 0], [d(t) for d in self.derivatives])
        angle = self.start + t * self.sweep
        return scale([-math.sin(angle), math.cos(angle)], math.copysign(1, self.sweep))

    def chord_hits(self, centre, pitch):
        """All intersections with the pitch circle, ordered later by travel."""
        if self.kind == "line":
            from planar_profiles import line_circle

            return line_circle(self.a, self.b, centre, pitch, 0)
        if self.kind == "bezier":
            x, y = [p - v for p, v in zip(self.xy, centre)]
            roots = (x * x + y * y - pitch**2).roots()
            return [float(r.real) for r in roots if abs(r.imag) < 1e-7]
        dx, dy = sub(centre, self.c)
        d = math.hypot(dx, dy)
        if not d:
            if abs(self.r - pitch) <= self.tol:
                return [0]
            return []
        cosine = (self.r**2 + d * d - pitch**2) / (2 * self.r * d)
        if abs(cosine) > 1 + 1e-14:
            return []
        offset = math.acos(max(-1, min(1, cosine)))
        angles = [math.atan2(dy, dx) + sign * offset for sign in (-1, 1)]
        sign = math.copysign(1, self.sweep)
        hits = [
            ((sign * (a - self.start)) % math.tau) / abs(self.sweep) for a in angles
        ]
        return (
            hits + [1]
            if abs(math.dist(self.point(1), centre) - pitch) <= self.tol
            else hits
        )


def path_rows(spec, segments, tolerance, closed=False):
    pitch = positive(spec["pitch"])
    if tolerance >= pitch / 2:
        raise ValueError("Tolerance must be less than half the pitch")
    ends = [0.0]
    for i, segment in enumerate(segments):
        if i and math.dist(segments[i - 1].point(1), segment.point(0)) > tolerance:
            raise ValueError("Disconnected path segments")
        ends.append(ends[-1] + segment.length)
    if not segments:
        raise ValueError("Empty path")
    length = ends[-1]
    if spec["measure"] == "path":
        bounded(length / pitch, MAX_POSITIONS, "Path stations")
    s, step = 0.0, 0
    intersections = 0
    while s <= length + tolerance:
        j = bisect.bisect_left(ends, s - tolerance)
        corner = j if j < len(ends) and abs(ends[j] - s) <= tolerance else None
        if corner is not None:
            s = ends[corner]
        if closed and corner == len(segments) and not spec.get("duplicates", False):
            break
        i = min(len(segments) - 1, bisect.bisect_right(ends, s) - 1)
        t = segments[i].at_distance(s - ends[i])
        point = segments[i].point(t)
        tangent = None
        if spec.get("orientation") == "tangent":
            tangent = segments[i].tangent(t)
            if corner is not None and (closed or 0 < corner < len(segments)):
                incoming = segments[(corner - 1) % len(segments)].tangent(1)
                outgoing = segments[corner % len(segments)].tangent(0)
                if math.dist(incoming, outgoing) > 1e-10:
                    side = spec.get("corner_tangent")
                    if side not in ("incoming", "outgoing"):
                        raise ValueError("Specify incoming or outgoing corner_tangent")
                    tangent = incoming if side == "incoming" else outgoing
        bounded(step + 1, MAX_POSITIONS, "Path stations")
        yield point, tangent, {"station": s}
        step += 1
        if spec["measure"] == "path":
            s = step * pitch
        elif spec["measure"] == "chord":
            if s == length:
                break
            for k in range(i, len(segments)):
                intersections += 1
                bounded(intersections, 10 * MAX_POSITIONS, "Chord segment checks")
                seg = segments[k]
                for u in sorted(seg.chord_hits(point, pitch)):
                    if not -1e-12 <= u <= 1 + 1e-12:
                        continue
                    u = min(1, max(0, u))
                    distance = ends[k] + seg.arc_length(u)
                    if (
                        distance > s + tolerance
                        and abs(math.dist(point, seg.point(u)) - pitch) <= tolerance
                    ):
                        break
                else:
                    continue
                s = distance
                break
            else:
                break
        else:
            raise ValueError("Specify path or chord distance")


def line_segments(points, sides):
    return [
        {"kind": "line", "points": [points[i], points[(i + 1) % len(points)]]}
        for i in sides
    ]


def polygon_rows(spec, tolerance):
    bounded(len(spec["vertices"]), MAX_POLYGON, "Polygon vertices")
    points = validate_profile(spec["vertices"])
    sides = spec.get("sides", list(range(len(points))))
    if not sides or any(type(i) is not int or not 0 <= i < len(points) for i in sides):
        raise ValueError("Invalid polygon side index")
    selected = set(sides)
    if len(selected) != len(sides):
        raise ValueError("Repeated polygon side index")
    segments = [Segment(s, tolerance) for s in line_segments(points, sides)]
    if spec["mode"] == "vertices":
        if spec.get("sides") is not None:
            raise ValueError("Vertex mode uses the polygon vertices")
        for i, p in enumerate(points):
            tangent = None
            if spec.get("orientation") == "tangent":
                side = spec.get("corner_tangent")
                if side not in ("incoming", "outgoing"):
                    raise ValueError("Specify incoming or outgoing corner_tangent")
                tangent = (
                    segments[i - 1].tangent(1)
                    if side == "incoming"
                    else segments[i].tangent(0)
                )
            yield p, tangent, {"vertex": i}
    elif spec["mode"] == "sides":
        if spec["spacing"] == "continuous":
            closed = (sides[-1] + 1) % len(points) == sides[0]
            yield from path_rows(spec, segments, tolerance, closed)
        elif spec["spacing"] == "restart":
            seen = set()
            for i, segment in zip(sides, segments):
                for p, tangent, info in path_rows(spec, [segment], tolerance):
                    vertex = None
                    if info["station"] == 0:
                        vertex = i
                    elif info["station"] == segment.length:
                        vertex = (i + 1) % len(points)
                    if vertex is not None:
                        if vertex in seen and not spec.get("duplicates", False):
                            continue
                        seen.add(vertex)
                        if (
                            spec.get("orientation") == "tangent"
                            and vertex in selected
                            and (vertex - 1) % len(points) in selected
                        ):
                            side = spec.get("corner_tangent")
                            if side not in ("incoming", "outgoing"):
                                raise ValueError(
                                    "Specify incoming or outgoing corner_tangent"
                                )
                            a = (
                                (vertex - 1) % len(points)
                                if side == "incoming"
                                else vertex
                            )
                            tangent = direction(
                                points[a], points[(a + 1) % len(points)]
                            )
                    yield p, tangent, dict(info, side=i)
        else:
            raise ValueError("Specify continuous or restart spacing")
    else:
        raise ValueError("Specify sides or vertices")


def circle_rows(spec):
    centre = vector(spec["centre"], 2)
    start = finite(spec["start_deg"])
    order = {"cw": -1, "ccw": 1}[spec["order"]]
    if spec.get("orientation") not in (None, "tangent"):
        raise ValueError("Unsupported ring orientation")
    if sum(k in spec for k in ("angles_deg", "count", "increment_deg")) != 1:
        raise ValueError("Specify angles_deg, count or increment_deg")
    if "angles_deg" in spec:
        bounded(len(spec["angles_deg"]), MAX_CIRCLE + 1, "Circle angles")
        offsets = [finite(v) for v in spec["angles_deg"]]
        if len(offsets) > 1 and (offsets[-1] - offsets[0]) % 360 == 0:
            offsets.pop()
        if any(not 0 < b - a < 360 for a, b in zip(offsets, offsets[1:])) or (
            offsets and offsets[-1] - offsets[0] >= 360
        ):
            raise ValueError("Specify increasing offsets within one turn")
    elif "count" in spec:
        n = spec["count"]
        if type(n) is not int or n < 1:
            raise ValueError("Positive circle count required")
        bounded(n, MAX_CIRCLE, "Circle positions")
        offsets = [i * 360 / n for i in range(n)]
    else:
        step = positive(spec["increment_deg"])
        bounded(360 / step, MAX_CIRCLE, "Circle positions")
        offsets = [
            i * step for i in range(math.ceil(360 / step)) if i * step < 360 - 1e-12
        ]
    bounded(len(offsets), MAX_CIRCLE, "Circle positions")
    angles = [start + order * v for v in offsets]
    radius = positive(spec["radius"])
    for angle, p in zip(angles, pattern(2 * radius, angles)):
        tangent = (
            scale([-p[1], p[0]], order / radius)
            if spec.get("orientation") == "tangent"
            else None
        )
        yield add(centre, p), tangent, {"angle_deg": angle}


def region_boundary(shape):
    from shapely.geometry import Point, Polygon

    if shape["kind"] == "circle":
        return Point(vector(shape["centre"], 2)), positive(shape["radius"])
    if shape["kind"] != "polygon":
        raise ValueError("Specify a circle or polygon boundary")
    bounded(len(shape["vertices"]), MAX_POSITIONS, "Boundary vertices")
    poly = Polygon([vector(p, 2) for p in shape["vertices"]])
    if not poly.is_valid or poly.area <= 0:
        raise ValueError("Invalid polygon")
    return poly, None


def interior_rows(spec):
    try:
        from shapely.affinity import rotate, translate
        from shapely.geometry import Point
    except ImportError as exc:
        raise ValueError(
            "Interior positions require local Shapely; use an equipped interpreter or supply explicitly measured and clearance-checked positions"
        ) from exc

    outer, radius = region_boundary(spec["outer"])
    cutouts = [region_boundary(s) for s in spec.get("cutouts", [])]
    clearance = finite(spec["clearance"])
    if clearance < 0:
        raise ValueError("Negative border clearance")
    footprint = spec["containment"]
    local, padding = Point(0, 0), 0
    if footprint == "footprint":
        local, padding = region_boundary(spec["footprint"])
        padding = padding or 0
    elif footprint != "centre":
        raise ValueError("Specify centre or footprint containment")
    if spec["layout"] == "rows":
        xmin, ymin, xmax, ymax = outer.bounds
        if radius:
            xmin, ymin, xmax, ymax = (
                xmin - radius,
                ymin - radius,
                xmax + radius,
                ymax + radius,
            )
        margin = clearance + padding
        lx, ly, hx, hy = local.bounds
        xmin, ymin = xmin + margin - lx, ymin + margin - ly
        xmax, ymax = xmax - margin - hx, ymax - margin - hy
        x0, y0 = vector(spec["origin"], 2)
        dx, dy = [positive(d) for d in vector(spec["pitch_xy"], 2)]
        limits = [
            (xmin - x0) / dx,
            (xmax - x0) / dx,
            (ymin - y0) / dy,
            (ymax - y0) / dy,
        ]
        if not all(math.isfinite(value) for value in limits):
            raise ValueError("Grid indices exceed the numeric range")
        ix = range(math.ceil(limits[0]), math.floor(limits[1]) + 1)
        iy = range(math.ceil(limits[2]), math.floor(limits[3]) + 1)
        bounded(
            max(0, ix.stop - ix.start) * max(0, iy.stop - iy.start),
            MAX_POSITIONS,
            "Grid candidates",
        )
        if ix.stop <= ix.start or iy.stop <= iy.start:
            return
        tangent = [1.0, 0.0] if spec.get("orientation") == "tangent" else None
        candidates = (
            ([x0 + i * dx, y0 + j * dy], tangent, {"column": i, "row": j})
            for j in iy
            for i in ix
        )
    elif spec["layout"] == "rings":
        bounded(len(spec["rings"]), MAX_POSITIONS, "Rings")
        candidates = (
            (p, tangent, dict(info, ring=i))
            for i, ring in enumerate(spec["rings"])
            for p, tangent, info in circle_rows(
                {"orientation": spec.get("orientation"), **ring}
            )
        )
    else:
        raise ValueError("Specify rows or rings")
    for index, (p, tangent, info) in enumerate(candidates, 1):
        bounded(index, MAX_POSITIONS, "Interior candidates")
        oriented = local
        if tangent is not None:
            oriented = rotate(
                local,
                math.atan2(tangent[1], tangent[0]),
                origin=(0, 0),
                use_radians=True,
            )
        shape = translate(oriented, xoff=p[0], yoff=p[1])
        margin = clearance + padding
        if radius:
            vertices = (
                shape.exterior.coords if shape.geom_type == "Polygon" else shape.coords
            )
            if max(math.dist(outer.coords[0], v) for v in vertices) + margin > radius:
                continue
        elif not outer.covers(shape) or outer.boundary.distance(shape) < margin:
            continue
        if any(
            (
                shape.distance(hole) < r + margin
                if r
                else shape.relate_pattern(hole, "T********")
                or shape.distance(hole) < margin
            )
            for hole, r in cutouts
        ):
            continue
        yield p, tangent, info


def generate(spec):
    unit = spec["unit"]
    if unit not in ("mm", "cm", "m", "in", "ft"):
        raise ValueError("Unsupported length unit")
    reference = spec["reference"]
    if not isinstance(reference, str) or not reference.strip():
        raise ValueError("Identify the measured reference")
    frame = spec["frame"]
    origin, x, y = [vector(frame[k]) for k in ("origin", "x", "y")]
    if (
        any(abs(math.hypot(*v) - 1) > 1e-10 for v in (x, y))
        or abs(sum(a * b for a, b in zip(x, y))) > 1e-10
    ):
        raise ValueError("Plane axes must be orthonormal")

    def world(uv):
        return [a * uv[0] + b * uv[1] for a, b in zip(x, y)]

    tol = positive(spec["tolerance"])
    kind = spec["kind"]
    if spec.get("orientation") not in (None, "tangent"):
        raise ValueError("Unsupported orientation")
    if kind == "explicit":
        bounded(len(spec["positions"]), MAX_POSITIONS, "Explicit positions")
        rows = (
            (
                vector(p["xy"], 2),
                direction([0, 0], vector(p["direction"], 2))
                if "direction" in p
                else None,
                {"id": p["id"]},
            )
            for p in spec["positions"]
        )
    elif kind == "path":
        bounded(len(spec["segments"]), MAX_POSITIONS, "Path segments")
        segments = [
            Segment(s, tol / max(1, len(spec["segments"]))) for s in spec["segments"]
        ]
        closed = (
            bool(segments)
            and math.dist(segments[0].point(0), segments[-1].point(1)) <= tol
        )
        rows = path_rows(spec, segments, tol, closed)
    elif kind == "polygon":
        rows = polygon_rows(spec, tol)
    elif kind == "circle":
        rows = circle_rows(spec)
    elif kind == "interior":
        rows = interior_rows(spec)
    else:
        raise ValueError("Unknown position pattern")
    positions, ids = [], set()
    for i, (p, tangent, detail) in enumerate(rows, 1):
        bounded(i, MAX_POSITIONS, "Positions")
        identifier = detail.pop("id", f"P{i}")
        if (
            not isinstance(identifier, str)
            or not identifier.strip()
            or identifier in ids
        ):
            raise ValueError("Position IDs must be unique nonempty strings")
        ids.add(identifier)
        row = dict(
            id=identifier,
            xy=p,
            xyz=[a + b for a, b in zip(origin, world(p))],
            reference=reference,
            **detail,
        )
        if tangent is not None:
            row["direction_xyz"] = world(tangent)
        positions.append(row)
    return dict(
        unit=unit, frame=frame, reference=reference, tolerance=tol, positions=positions
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    args = parser.parse_args()
    try:
        result = generate(json.loads(args.request.read_text()))
        encoded = json.dumps(result, indent=2, allow_nan=False)
    except (OSError, ValueError, TypeError, KeyError, OverflowError, CadError) as exc:
        parser.exit(2, f"Planar position request: {exc}\n")
    print(encoded)
