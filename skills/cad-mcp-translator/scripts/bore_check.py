"""Check the readback mesh for the 60 x 40 x 10 mm OpenSCAD plate fixture."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path


SEGMENTS = 96
CENTRE = (17.0, 23.0)
TOLERANCE_MM = 0.001
PLATE_CORNERS = ((0, 0), (60, 0), (60, 40), (0, 40))


def triangles(data):
    lines = iter(line.strip() for line in data.decode("ascii").splitlines() if line.strip())

    def take():
        return next(lines, "").split()

    if take()[:1] != ["solid"]:
        raise ValueError("Expected one ASCII STL solid")
    while True:
        head = take()
        if head[:1] == ["endsolid"]:
            if take():
                raise ValueError("Unexpected data after solid")
            return
        if len(head) != 5 or head[:2] != ["facet", "normal"] or take() != ["outer", "loop"]:
            raise ValueError("Malformed STL facet")
        points = []
        for _ in range(3):
            vertex = take()
            if len(vertex) != 4 or vertex[0] != "vertex":
                raise ValueError("Malformed STL vertex")
            point = tuple(map(float, vertex[1:]))
            if not all(map(math.isfinite, point)):
                raise ValueError("Nonfinite STL coordinate")
            points.append(point)
        if take() != ["endloop"] or take() != ["endfacet"]:
            raise ValueError("Incomplete STL facet")
        yield points


def fixture_vertex(point, diameter):
    x, y, z = point
    layer = 0 if z < 5 else 1
    if abs(z - 10 * layer) > TOLERANCE_MM:
        raise ValueError("Unexpected surface between the two rim planes")
    for index, corner in enumerate(PLATE_CORNERS):
        if math.dist((x, y), corner) <= TOLERANCE_MM:
            return (layer, "outer", index)
    dx, dy = x - CENTRE[0], y - CENTRE[1]
    index = round(math.atan2(dy, dx) * SEGMENTS / math.tau) % SEGMENTS
    angle = math.tau * index / SEGMENTS
    radial = diameter / 2
    if math.hypot(dx - radial * math.cos(angle), dy - radial * math.sin(angle)) > TOLERANCE_MM:
        raise ValueError("Vertex outside expected plate corners and bore rims")
    return (layer, "rim", index)


def verify_bytes(data, diameter):
    """Require both perforated caps and every oriented vertical wall of this fixture.

    The fixture has only end-plane corners and rim vertices. Extra subdivisions are
    outside this checker's supported triangulations. STL coordinates are in job mm.
    """
    if diameter not in (10, 12):
        raise ValueError("Fixture diameter must be 10 or 12 mm")
    walls = defaultdict(list)
    rings = defaultdict(dict)
    directed = Counter()
    observed = {}
    for points in triangles(data):
        ids = tuple(fixture_vertex(p, diameter) for p in points)
        if len(set(ids)) != 3:
            raise ValueError("Collapsed triangle")
        for key, point in zip(ids, points):
            if observed.setdefault(key, point) != point:
                raise ValueError("Cracked edge at a fixture vertex")
            if key[1] == "rim":
                rings[key[0]][key[2]] = point[:2]
        directed.update(zip(ids, ids[1:] + ids[:1]))
        layers = {key[0] for key in ids}
        if len(layers) == 1:
            a, b, c = points
            signed = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
            if signed * (1 if ids[0][0] else -1) <= 0:
                raise ValueError("Reversed or degenerate cap triangle")
            continue
        kinds = {key[1] for key in ids}
        if len(kinds) != 1:
            raise ValueError("Interior facet crossing between bore and exterior")
        kind = ids[0][1]
        count = SEGMENTS if kind == "rim" else 4
        indices = {key[2] for key in ids}
        starts = [i for i in indices if (i+1) % count in indices]
        if len(indices) != 2 or len(starts) != 1:
            raise ValueError("Unexpected vertical wall")
        walls[kind, starts[0]].append(ids)

    if any(n != 1 or directed[b, a] != 1 for (a, b), n in directed.items()):
        raise ValueError("Nonmanifold, duplicate or open edge")

    for kind, count in (("rim", SEGMENTS), ("outer", 4)):
        for i in range(count):
            facets = walls[kind, i]
            if len(facets) != 2 or len(set().union(*facets)) != 4:
                raise ValueError("Missing part of a full-height wall")
            # The top edge of an inner wall runs counterclockwise; for an
            # outer wall it runs clockwise, opposite its corresponding cap.
            j = (i + 1) % count
            first, second = (i, j) if kind == "rim" else (j, i)
            edge = ((1, kind, first), (1, kind, second))
            if not any(edge in zip(ids, ids[1:] + ids[:1]) for ids in facets):
                raise ValueError("Inconsistent wall winding")
    across = []
    vertices = []
    for layer in (0, 1):
        rim = rings[layer]
        widths = [math.dist(rim[i], rim[i+SEGMENTS//2]) for i in range(SEGMENTS//2)]
        vertices += widths
        mids = [tuple((a+b)/2 for a,b in zip(rim[i],rim[(i+1)%SEGMENTS])) for i in range(SEGMENTS)]
        across += [math.dist(mids[i], mids[i+SEGMENTS//2]) for i in range(SEGMENTS//2)]
    return {"result": "PASS", "stl_sha256": hashlib.sha256(data).hexdigest(),
            "unit": "mm", "rim_count": 2, "continuous_bore_panels": SEGMENTS,
            "vertex_diameter_range_mm": [min(vertices), max(vertices)],
            "across_flats_range_mm": [min(across), max(across)]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mesh", type=Path)
    parser.add_argument("--diameter-mm", required=True, type=float, choices=[10, 12])
    args = parser.parse_args()
    try:
        result = verify_bytes(args.mesh.read_bytes(), args.diameter_mm)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Fixture check failed: {exc}\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
