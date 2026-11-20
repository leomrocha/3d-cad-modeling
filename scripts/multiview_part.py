"""Infer a named solid feature sequence from calibrated top and front coverage masks."""

import argparse
import hashlib
import json
import math
from pathlib import Path

# Original learned parameters. Regenerate using the repository multiview-part training trial.
WEIGHTS = {
    "span": [
        0.12209247187015061,
        0.30851521243941293,
        0.5362262692386169,
        -0.017563443128858252,
    ],
    "diameter": [
        -1.9667141331996407,
        -0.12210442190595848,
        2.924931589002239,
        -1.0693149373944306,
    ],
    "width_fusion": 0.4405676110322907,
    "bore_logit": [
        13.642936840825893,
        66.16589445381375,
        -61.592827285966486,
        -176.7377362078404,
        70.70603785837928,
    ],
}

FAMILY = "rectangular-prism-with-z-through-bores"


def scale(view, shape):
    import numpy as np

    limits = []
    for field in ("scale_control", "held_out_control"):
        ctl = view[field]
        points = np.asarray(ctl["pixels"], dtype=float)
        length = float(ctl["length_mm"])
        if (
            points.shape != (2, 2)
            or not np.isfinite(points).all()
            or not np.isfinite(length)
            or length <= 0
            or np.any(points < 0)
            or np.any(points > np.asarray(shape[::-1]) - 1)
        ):
            raise ValueError(
                "Each scale check requires two on-image points and a positive length"
            )
        span = float(np.linalg.norm(points[0] - points[1]))
        if span == 0:
            raise ValueError("Zero pixel reference span")
        limits.append((points, span, length))
    (a, span, length), (b, held_span, held_length) = limits
    # A repeated segment cannot detect wrong scale perpendicular to the first reference.
    cos_angle = abs(float((a[1] - a[0]) @ (b[1] - b[0]) / (span * held_span)))
    if cos_angle > 0.5:
        raise ValueError(
            "Supply scale controls in two directions at least 60 degrees apart"
        )
    s = length / span
    residual = abs(held_span * s - held_length)
    tolerance = float(view["held_out_limit_mm"])
    if not math.isfinite(tolerance) or tolerance < 0 or residual > tolerance:
        raise ValueError("The held-out dimension exceeds its limit")
    return s, residual


def moments(ink, pixel_mm):
    import cv2
    import numpy as np

    # Grayscale encodes foreground coverage (white material, black background).
    # Work in local crops but keep the original origin for bore centers.
    mask = np.uint8(ink >= 0.5)
    outlines, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if hierarchy is None:
        raise ValueError("Empty foreground")
    parents = hierarchy[0, :, 3]
    ids = np.flatnonzero(parents == -1)
    if len(ids) != 1:
        raise ValueError("Expected one separated component per view")
    root = int(ids[0])
    x, y, w, h = cv2.boundingRect(outlines[root])
    if (
        x < 2
        or y < 2
        or x + w >= mask.shape[1] - 1
        or y + h >= mask.shape[0] - 1
        or min(w, h) < 4
    ):
        raise ValueError("Clipped or unresolved outer bounds")
    area = cv2.contourArea(outlines[root])
    if abs(area - (w - 1) * (h - 1)) > max(2, 0.01 * (w - 1) * (h - 1)):
        raise ValueError("Outer feature is not an axis-aligned rectangle")
    holes = []
    for i in range(len(outlines)):
        if i == root:
            continue
        if parents[i] != root:
            raise ValueError("Nested material islands outside the supported family")
        # Inspect the connected dark pixels on the inside of this contour.
        canvas = np.zeros_like(mask)
        cv2.drawContours(canvas, [outlines[i]], -1, 1, -1)
        inside = canvas.astype(bool) & (mask == 0)
        yy, xx = np.where(inside)
        if len(xx) < 8:
            raise ValueError("Unresolved round hole")
        bx, ex, by, ey = xx.min() - 1, xx.max() + 2, yy.min() - 1, yy.max() + 2
        if bx <= x or by <= y or ex >= x + w or ey >= y + h:
            raise ValueError("Hole boundary touches the exterior")
        patch = 1 - ink[by:ey, bx:ex]
        hard = inside[by:ey, bx:ex]
        # Distinguish round through-bores from slots and polygonal cutouts.
        centroid = np.array([xx.mean(), yy.mean()])
        dist = np.linalg.norm(outlines[i][:, 0, :] - centroid, axis=1)
        cov = np.linalg.eigvalsh(np.cov(np.c_[xx, yy].T))
        if cov[0] <= 0:
            raise ValueError("Degenerate hole contour")
        ratio = math.sqrt(cov[-1] / cov[0])
        cap = outlines[i]
        perimeter = cv2.arcLength(cap, closed=True)
        shape_features = [
            1,
            float(np.std(dist) / dist.mean()),
            ratio - 1,
            1 - 4 * math.pi * cv2.contourArea(cap) / perimeter**2,
            1 / dist.mean(),
        ]
        py, px = np.indices(patch.shape)
        if patch.sum() <= 0:
            raise ValueError("Hole coverage is empty")
        dc = 2 * np.sqrt(
            np.array([hard.sum(), patch.sum(), (patch**2).sum(), np.sqrt(patch).sum()])
            / np.pi
        )
        dc = dc * pixel_mm
        holes.append(
            dict(
                xy_px=[
                    float(bx + (px * patch).sum() / patch.sum()),
                    float(by + (py * patch).sum() / patch.sum()),
                ],
                diameter_features=dc.tolist() + [pixel_mm],
                shape_features=shape_features,
            )
        )
    # Max projections go through solid bands around the openings.
    crop = ink[y - 1 : y + h + 1, x - 1 : x + w + 1]
    projections = [crop.max(axis=0), crop.max(axis=1)]
    spans = []
    centers = []
    for offset, vec in zip((x - 1, y - 1), projections):
        lengths = (
            np.array(
                [(vec >= 0.5).sum(), vec.sum(), (vec**2).sum(), np.sqrt(vec).sum()]
            )
            * pixel_mm
        )
        spans.append(lengths.tolist() + [pixel_mm])
        centers.append(float(offset + np.average(np.arange(len(vec)), weights=vec)))
    return spans, centers, holes


def predicted(field, values, weights):
    import numpy as np

    # Regress the offset from a hard pixel count using coverage at several powers.
    v = np.asarray(values, dtype=float)
    return float(v[0] + np.asarray(weights[field]) @ np.r_[v[1:4] - v[0], v[4]])


def estimate(data, weights):
    import numpy as np

    (top, top_center, holes, s_top), (front, _, front_holes, s_front) = data
    if front_holes:
        raise ValueError(
            "A front-face opening falls outside the declared through-bore family"
        )
    wx = [predicted("span", v, weights) for v in (top[0], front[0])]
    blend = weights["width_fusion"]
    width = wx[0] * blend + wx[1] * (1 - blend)
    depth = predicted("span", top[1], weights)
    height = predicted("span", front[1], weights)
    bores = []
    for hole in holes:
        if np.dot(hole["shape_features"], weights["bore_logit"]) < 0:
            raise ValueError(
                "Learned bore classifier rejected a noncircular or unresolved opening"
            )
        x, y = (np.asarray(hole["xy_px"]) - top_center) * s_top
        diameter = predicted("diameter", hole["diameter_features"], weights)
        if (
            diameter <= 0
            or abs(x) + diameter / 2 >= width / 2
            or abs(y) + diameter / 2 >= depth / 2
        ):
            raise ValueError("Predicted bore must be enclosed by the block")
        bores.append([float(x), float(-y), diameter])
    bores.sort()
    for i, (x, y, d) in enumerate(bores):
        if any(math.hypot(x - u, y - v) <= (d + e) / 2 for u, v, e in bores[:i]):
            raise ValueError("Predicted bores overlap; inspect the source")
    return dict(
        width_mm=width,
        depth_mm=depth,
        height_mm=height,
        bores_xy_diameter_mm=bores,
        width_disagreement_mm=abs(wx[0] - wx[1]),
    )


def sequence(part, sources):
    def parameter(value, source, basis="inferred"):
        return dict(value_mm=value, source=source, basis=basis)

    params = {
        "zero": parameter(0, "job", "explicit"),
        "width": parameter(part["width_mm"], "job"),
        "depth": parameter(part["depth_mm"], "top"),
        "height": parameter(part["height_mm"], "front"),
    }
    features = [
        dict(
            id="plate",
            plane="XY",
            origin_xyz=["zero"] * 3,
            depth="height",
            operation="add",
            profile=dict(kind="rectangle", width="width", height="depth"),
        )
    ]
    for i, values in enumerate(part["bores_xy_diameter_mm"], 1):
        key = f"bore_{i}"
        for suffix, num in zip(("x", "y", "diameter"), values):
            params[f"{key}_{suffix}"] = parameter(num, "top")
        features.append(
            dict(
                id=key,
                plane="XY",
                origin_xyz=[key + "_x", key + "_y", "zero"],
                depth="height",
                operation="cut",
                profile=dict(kind="circle", diameter=key + "_diameter"),
            )
        )
    return dict(
        model="multiview-prismatic-regression-v1",
        units="mm",
        sources=sources,
        parameters=params,
        features=features,
    )


def infer(job_file):
    import cv2
    import numpy as np

    raw = job_file.read_bytes()
    job = json.loads(raw)
    if job["family"] != FAMILY:
        raise ValueError(
            "Declare the rectangular prism and through-bore family explicitly"
        )
    sources = {"job": dict(sha256=hashlib.sha256(raw).hexdigest())}
    data = []
    residuals = {}
    for role in ("top", "front"):
        view = job[role]
        pixels = (job_file.parent / view["path"]).read_bytes()
        digest = hashlib.sha256(pixels).hexdigest()
        if digest != view["sha256"]:
            raise ValueError("View revision changed: " + role)
        im = cv2.imdecode(
            np.frombuffer(pixels, np.uint8),
            cv2.IMREAD_GRAYSCALE | cv2.IMREAD_IGNORE_ORIENTATION,
        )
        if im is None:
            raise ValueError("Unreadable calibrated view: " + role)
        s, residuals[role] = scale(view, im.shape)
        sources[role] = dict(sha256=digest)
        data.append((*moments(im.astype(float) / 255, s), s))
    part = estimate(data, WEIGHTS)
    allowed = float(job["width_agreement_mm"])
    if (
        not math.isfinite(allowed)
        or allowed < 0
        or part["width_disagreement_mm"] > allowed
    ):
        raise ValueError(
            "Top/front widths disagree; check scale, view axes and variant"
        )
    return sequence(part, sources), dict(
        measurement=part,
        held_out_residual_mm=residuals,
        family=FAMILY,
        inferred_topology="one XY extrusion and the visible Z-axis through-bores",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("calibrated_views", type=Path)
    parser.add_argument("new_directory", type=Path)
    args = parser.parse_args()
    seq, report = infer(args.calibrated_views)
    args.new_directory.mkdir()
    for name, doc in (("sequence.json", seq), ("inference.json", report)):
        (args.new_directory / name).write_text(
            json.dumps(doc, indent=2, allow_nan=False) + "\n"
        )
