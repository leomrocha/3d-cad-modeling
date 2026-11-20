"""Vectorize sketch ink, retain branch topology and solve reviewed relation proposals in pixels."""

import argparse
import hashlib
import json
import math
from pathlib import Path


# Original coefficients fitted on distorted synthetic strokes and angles.
TRAINED_MODEL = {
    "ink_logit": [
        -13.31045150756836,
        24.622472763061523,
        70.4392318725586,
        34.52581024169922,
    ],
    "angle_logit": [10.399668725001709, -1.924036865916522],
}


def pixel_features(gray):
    import cv2
    import numpy as np

    g = gray.astype(np.float32) / 255
    return np.stack(
        [
            np.ones_like(g),
            1 - g,
            cv2.GaussianBlur(g, (0, 0), 6) - g,
            cv2.GaussianBlur(g, (0, 0), 2) - g,
        ],
        axis=-1,
    )


def skeleton(mask):
    # Parallel two-subiteration thinning. Removing simple points preserves 8-connected ink.
    import numpy as np

    pixels = np.pad(mask.astype(bool), 1)
    while True:
        removed = 0
        for phase in (0, 1):
            neighbours = [
                pixels[:-2, 1:-1],
                pixels[:-2, 2:],
                pixels[1:-1, 2:],
                pixels[2:, 2:],
                pixels[2:, 1:-1],
                pixels[2:, :-2],
                pixels[1:-1, :-2],
                pixels[:-2, :-2],
            ]
            n, e, s, w = neighbours[::2]
            count = np.sum(neighbours, axis=0)
            starts = np.sum(
                [~a & b for a, b in zip(neighbours, neighbours[1:] + neighbours[:1])],
                axis=0,
            )
            keep = (
                (n & e & s) | (e & s & w) if phase == 0 else (n & e & w) | (n & s & w)
            )
            erase = (
                pixels[1:-1, 1:-1] & (count >= 2) & (count <= 6) & (starts == 1) & ~keep
            )
            pixels[1:-1, 1:-1][erase] = False
            removed += erase.sum()
        if removed == 0:
            return pixels[1:-1, 1:-1]


def paths_from_ink(mask):
    import numpy as np

    ink = set(zip(*np.where(skeleton(mask))))
    graph = {}
    for y, x in ink:
        neighbors = []
        for dy, dx in (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ):
            other = (y + dy, x + dx)
            if other not in ink:
                continue
            if dx and dy and ((y, x + dx) in ink or (y + dy, x) in ink):
                continue
            neighbors.append(other)
        graph[y, x] = neighbors
    # Collapse adjacent branch pixels into one crossing. Keep isolated endpoints distinct.
    branches = {p for p, v in graph.items() if len(v) > 2}
    rep = {p: p for p in ink}
    while branches:
        group = {branches.pop()}
        active = list(group)
        while active:
            p = active.pop()
            for q in graph[p]:
                if q in branches:
                    branches.remove(q)
                    group.add(q)
                    active.append(q)
        centroid = np.mean(list(group), axis=0)
        center = min(group, key=lambda p: (np.linalg.norm(np.asarray(p) - centroid), p))
        rep.update((p, center) for p in group)
    edges = {
        tuple(sorted((rep[p], rep[q])))
        for p in graph
        for q in graph[p]
        if rep[p] != rep[q]
    }
    adj = {}
    for p, q in edges:
        adj.setdefault(p, set()).add(q)
        adj.setdefault(q, set()).add(p)
    ends = sorted(p for p, v in adj.items() if len(v) != 2)
    tracks = []

    def follow(p, q):
        path = [p]
        while True:
            edges.remove(tuple(sorted((p, q))))
            path.append(q)
            if len(adj[q]) != 2 or path[0] == q:
                break
            (nxt,) = adj[q] - {p}
            p, q = q, nxt
        tracks.append([[int(x), int(y)] for y, x in path])

    for p in ends:
        for q in sorted(adj[p]):
            if tuple(sorted((p, q))) in edges:
                follow(p, q)
    while edges:
        follow(*min(edges))
    return tracks, sum(len(v) > 2 for v in adj.values())


def geometry(gray, mask, epsilon):
    import cv2
    import numpy as np

    if not np.isfinite(epsilon) or epsilon <= 0:
        raise ValueError("Positive vector error in px required")
    tracks, junctions = paths_from_ink(mask)
    vertices = []
    index = {}
    lines = []
    loops = []

    def vertex(p):
        point = tuple(map(float, p))
        if point not in index:
            index[point] = len(vertices)
            vertices.append(point)
        return index[point]

    for track in tracks:
        closed = track[0] == track[-1]
        samples = np.asarray(track, np.int32)
        poly = cv2.approxPolyDP(samples, epsilon, closed).reshape(-1, 2)
        if closed and len(poly) >= 3:
            from raster_features import fit_samples

            fits = fit_samples(samples[:-1]) if len(track) >= 6 else {}
            loops.append(dict(id=len(loops), points_px=poly.tolist(), fits=fits))
        elif not closed:
            for a, b in zip(poly, poly[1:]):
                lines.append([vertex(a), vertex(b)])
    return dict(
        vertices_px=vertices, lines=lines, closed_strokes=loops, junctions=junctions
    )


def proposals(graph, angle_limit, model):
    import numpy as np

    if not 0 < angle_limit < 45:
        raise ValueError("Angular proposal limit must be between 0 and 45 degrees")
    vertices = np.asarray(graph["vertices_px"])
    segments = graph["lines"]
    items = []

    def add(kind, ids, error):
        if error > angle_limit:
            return
        score = None
        if model:
            b, w = model["angle_logit"]
            score = 1 / (1 + math.exp(-max(-60, min(60, b + w * error))))
            if score < 0.5:
                return
        items.append(
            dict(
                id=kind + "-" + "-".join(map(str, ids)),
                kind=kind,
                lines=ids,
                observed_error_deg=error,
                learned_probability=score,
            )
        )

    angles = []
    for i, (a, b) in enumerate(segments):
        delta = vertices[b] - vertices[a]
        heading = math.degrees(math.atan2(delta[1], delta[0])) % 180
        angles.append(heading)
        add("horizontal", [i], min(heading, 180 - heading))
        add("vertical", [i], abs(90 - heading))
    incident = {}
    for i, (a, b) in enumerate(segments):
        for j in sorted(incident.get(a, set()) | incident.get(b, set())):
            angle = abs(angles[i] - angles[j])
            angle = min(angle, 180 - angle)
            add("parallel", [j, i], angle)
            add("perpendicular", [j, i], abs(90 - angle))
        incident.setdefault(a, set()).add(i)
        incident.setdefault(b, set()).add(i)
    return items


def solve(graph, proposed, reviewed, limit):
    import numpy as np
    from scipy.optimize import least_squares

    if not math.isfinite(limit) or limit <= 0:
        raise ValueError("Positive edit limit required")
    ids = {r["id"]: r for r in proposed}
    if len(set(reviewed)) != len(reviewed) or set(reviewed) - ids.keys():
        raise ValueError("Unknown or repeated relation")
    if not reviewed:
        return dict(vertices_px=graph["vertices_px"], max_shift_px=0)
    original = np.array(graph["vertices_px"])
    lines = graph["lines"]
    selected = [ids[key] for key in reviewed]

    def residuals(x):
        v = x.reshape(-1, 2)
        vectors = [v[b] - v[a] for a, b in lines]
        directions = [delta / max(np.linalg.norm(delta), 1e-12) for delta in vectors]
        r = []
        for item in selected:
            angles = [directions[i] for i in item["lines"]]
            a = angles[0]
            kind = item["kind"]
            if kind == "horizontal":
                r.append(a[1])
            elif kind == "vertical":
                r.append(a[0])
            elif kind == "parallel":
                r.append(a[0] * angles[1][1] - a[1] * angles[1][0])
            else:
                r.append(a @ angles[1])
        return np.asarray(r)

    result = least_squares(
        lambda x: np.r_[x - original.ravel(), 1e5 * residuals(x)], original.ravel()
    )
    final = result.x.reshape(-1, 2)
    shift = np.linalg.norm(final - original, axis=1).max()
    if (
        not result.success
        or shift > limit
        or np.max(abs(residuals(result.x))) > 1e-4
        or any(np.linalg.norm(final[b] - final[a]) < 0.5 for a, b in lines)
    ):
        raise ValueError("Reviewed relations exceed edit limit or cannot be solved")
    return dict(
        vertices_px=final.tolist(),
        max_shift_px=float(shift),
        max_direction_residual=float(max(abs(residuals(result.x)))),
    )


def vectorize(raw, threshold, model, epsilon, angle, mask_record=None):
    import cv2
    import numpy as np

    gray = cv2.imdecode(
        np.frombuffer(raw, np.uint8),
        cv2.IMREAD_GRAYSCALE | cv2.IMREAD_IGNORE_ORIENTATION,
    )
    if gray is None:
        raise ValueError("Expected a readable raster")
    sha = hashlib.sha256(raw).hexdigest()
    if mask_record is not None:
        if mask_record["source_sha256"] != sha:
            raise ValueError("Mask references another sketch")
        mask = np.asarray(mask_record["mask"])
        if mask.shape != gray.shape or not np.isin(mask, [0, 1]).all():
            raise ValueError("Expected binary original-page mask")
    elif model:
        weights = np.asarray(model["ink_logit"], float)
        if weights.shape != (4,) or not np.isfinite(weights).all():
            raise ValueError("Invalid ink classifier")
        mask = pixel_features(gray) @ weights >= 0
    else:
        if not 0 <= threshold <= 255:
            raise ValueError("Threshold must be a pixel intensity")
        mask = gray <= threshold
    graph = geometry(gray, mask, epsilon)
    suggested = proposals(graph, angle, model)
    return dict(
        source_sha256=sha,
        size_px=list(gray.shape[::-1]),
        frame="stored pixels, x right and y down",
        graph=graph,
        proposed_relations=suggested,
    )


def svg(record, vertices):
    width, height = record["size_px"]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<g stroke="black" fill="none">',
    ]
    for i, (a, b) in enumerate(record["graph"]["lines"]):
        x, y = vertices[a]
        u, v = vertices[b]
        parts.append(f'<line id="L{i}" x1="{x}" y1="{y}" x2="{u}" y2="{v}"/>')
    for loop in record["graph"]["closed_strokes"]:
        coords = " ".join(f"{x},{y}" for x, y in loop["points_px"])
        parts.append(f'<polygon id="C{loop["id"]}" points="{coords}"/>')
    return "\n".join(parts + ["</g></svg>", ""])


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("image", type=Path)
    p.add_argument("new_output", type=Path)
    p.add_argument("--threshold", type=int, default=127)
    method = p.add_mutually_exclusive_group()
    method.add_argument(
        "--learned",
        action="store_true",
        help="Use original synthetic-trained ink and relation classifiers",
    )
    method.add_argument(
        "--model", type=Path, help="Trained ink and angle coefficients JSON"
    )
    p.add_argument(
        "--mask",
        type=Path,
        help="Original-frame normalized single ink mask with source_sha256 and mask",
    )
    p.add_argument("--epsilon-px", type=float, required=True)
    p.add_argument("--angle-deg", type=float, required=True)
    p.add_argument(
        "--review",
        type=Path,
        help="JSON with proposal_sha256, accepted_ids and max_shift_px",
    )
    a = p.parse_args()
    raw = a.image.read_bytes()
    model = (
        json.loads(a.model.read_text())
        if a.model
        else TRAINED_MODEL
        if a.learned
        else None
    )
    record = vectorize(
        raw,
        a.threshold,
        model,
        a.epsilon_px,
        a.angle_deg,
        json.loads(a.mask.read_text()) if a.mask else None,
    )
    record["input_settings"] = {
        "threshold": a.threshold,
        "built_in_training": "synthetic-ink-angle-v1" if a.learned else None,
        "epsilon_px": a.epsilon_px,
        "angle_deg": a.angle_deg,
        "model_sha256": hashlib.sha256(a.model.read_bytes()).hexdigest()
        if a.model
        else None,
        "mask_sha256": hashlib.sha256(a.mask.read_bytes()).hexdigest()
        if a.mask
        else None,
    }
    tag = hashlib.sha256(
        json.dumps(record, sort_keys=True, allow_nan=False).encode()
    ).hexdigest()
    record["proposal_sha256"] = tag
    vertices = record["graph"]["vertices_px"]
    if a.review:
        review = json.loads(a.review.read_text())
        if review["proposal_sha256"] != tag:
            raise ValueError("Review refers to another proposal")
        record["review"] = review
        record["solution"] = solve(
            record["graph"],
            record["proposed_relations"],
            review["accepted_ids"],
            review["max_shift_px"],
        )
        vertices = record["solution"]["vertices_px"]
    a.new_output.mkdir()
    (a.new_output / "vectors.svg").write_text(svg(record, vertices))
    (a.new_output / "proposals.json").write_text(
        json.dumps(record, allow_nan=False, indent=2) + "\n"
    )
