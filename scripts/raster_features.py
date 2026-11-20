"""Trace a binary foreground and optionally map its samples to a controlled plane."""

import argparse
import hashlib
import json
from pathlib import Path


def projection(points, h):
    import numpy as np

    points = np.asarray(points, dtype=float).reshape(-1, 2)
    homogeneous = np.column_stack((points, np.ones(len(points)))) @ h.T
    if not np.isfinite(homogeneous).all() or (abs(homogeneous[:, 2]) < 1e-12).any():
        raise ValueError("Point outside finite projective frame")
    return homogeneous[:, :2] / homogeneous[:, 2, None]


def calibration(controls):
    import cv2
    import numpy as np

    src, dst = (
        np.asarray(controls[key], dtype=float) for key in ("pixels", "plane_mm")
    )
    if src.shape != dst.shape or src.ndim != 2 or src.shape[1] != 2 or len(src) < 4:
        raise ValueError("Supply paired controls for the same plane")
    check, truth = (
        np.asarray(controls[k], dtype=float) for k in ("held_pixels", "held_mm")
    )
    if (
        check.shape != truth.shape
        or check.ndim != 2
        or check.shape[1] != 2
        or not len(check)
        or any(np.allclose(a, b) for a in check for b in src)
    ):
        raise ValueError("Independent held-out control required")
    limit = float(controls["limit_mm"])
    if not np.isfinite(limit) or limit < 0:
        raise ValueError("Finite nonnegative control uncertainty required")
    h, _ = cv2.findHomography(src, dst, 0)
    if h is None or np.linalg.matrix_rank(h) < 3:
        raise ValueError("Degenerate plane controls")
    residual = np.linalg.norm(projection(check, h) - truth, axis=1)
    fitted = np.linalg.norm(projection(src, h) - dst, axis=1)
    if not np.isfinite([*residual, *fitted]).all() or max(*residual, *fitted) > limit:
        raise ValueError("Control residual exceeds supplied limit")
    return h, dict(
        controls=controls,
        forward=h.tolist(),
        inverse=np.linalg.inv(h).tolist(),
        held_errors_mm=residual.tolist(),
        fit_errors_mm=fitted.tolist(),
    )


def fit_samples(samples):
    """Fit observed points, including an open arc or line picked on a source image."""
    import cv2
    import numpy as np

    samples = np.asarray(samples, dtype=np.float32)
    if (
        samples.ndim != 2
        or samples.shape[1] != 2
        or not np.isfinite(samples).all()
        or len(np.unique(samples, axis=0)) < 2
    ):
        raise ValueError("At least two distinct finite pixel positions required")
    vx, vy, x, y = cv2.fitLine(samples, cv2.DIST_L2, 0, 0.01, 0.01).ravel()
    delta = samples - [x, y]
    normal_error = delta[:, 0] * vy - delta[:, 1] * vx
    result = dict(
        line_candidate=dict(
            origin_px=[float(x), float(y)],
            direction=[float(vx), float(vy)],
            perpendicular_rms_px=float(np.sqrt(np.mean(normal_error**2))),
        )
    )
    if len(np.unique(samples, axis=0)) < 5 or np.linalg.matrix_rank(delta) < 2:
        return result
    (x, y), (a, b), angle = cv2.fitEllipseAMS(samples)
    if min(a, b) <= 0 or not np.isfinite([x, y, a, b, angle]).all():
        return result
    theta = np.deg2rad(angle)
    dx, dy = (samples - [x, y]).T
    u = 2 * (dx * np.cos(theta) + dy * np.sin(theta)) / a
    v = 2 * (-dx * np.sin(theta) + dy * np.cos(theta)) / b
    angles = np.sort(np.arctan2(v, u))
    span = 360 - np.rad2deg(np.diff(np.r_[angles, angles[0] + 2 * np.pi]).max())
    result["ellipse_candidate"] = dict(
        center_px=[x, y],
        diameters_px=[a, b],
        angle_deg=angle,
        normalized_radial_rms=float(np.mean((np.hypot(u, v) - 1) ** 2) ** 0.5),
        sample_span_deg=float(span),
    )
    return result


def trace(raw, threshold, dark=False, controls=None):
    import cv2
    import numpy as np

    gray = cv2.imdecode(
        np.frombuffer(raw, np.uint8),
        cv2.IMREAD_GRAYSCALE | cv2.IMREAD_IGNORE_ORIENTATION,
    )
    if gray is None or not 0 <= threshold <= 255:
        raise ValueError("Readable image and threshold in [0,255] required")
    mask = cv2.threshold(
        gray, threshold, 255, cv2.THRESH_BINARY_INV if dark else cv2.THRESH_BINARY
    )[1]
    loops, tree = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    overlay = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    output = dict(
        source_sha256=hashlib.sha256(raw).hexdigest(),
        size_px=list(gray.shape[::-1]),
        frame="stored pixels, top-left pixel center (0,0), x right, y down",
        threshold=threshold,
        dark=dark,
        cv2=cv2.__version__,
        loops=[],
    )
    if controls is not None:
        if controls.get("source_sha256") != output["source_sha256"]:
            raise ValueError("Plane controls reference another image revision")
        h, output["plane"] = calibration(controls)
    for i, loop in enumerate(loops):
        samples = loop[:, 0]
        parent = int(tree[0, i, 3])
        depth, ancestor = 0, parent
        while ancestor >= 0:
            depth += 1
            ancestor = tree[0, ancestor, 3]
        feature = dict(
            id=i,
            parent=None if parent < 0 else parent,
            depth=depth,
            role="hole" if depth % 2 else "foreground",
            samples_px=samples.tolist(),
        )
        if controls:
            polygon = projection(samples, h)
            area = cv2.contourArea(polygon.astype(np.float32), oriented=True)
            if (area < 0) != bool(depth % 2):
                polygon = polygon[::-1]
            feature["loop_mm"] = polygon.tolist()
        if len(samples) >= 5:
            feature.update(fit_samples(samples))
        cv2.drawContours(
            overlay, loops, i, (0, 0, 255) if depth % 2 else (0, 180, 0), 1
        )
        cv2.putText(
            overlay,
            str(i),
            tuple(samples[0]),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (255, 0, 0),
            1,
        )
        output["loops"].append(feature)
    return output, cv2.imencode(".png", overlay)[1].tobytes()


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("source", type=Path)
    p.add_argument("output", type=Path, help="New result directory")
    p.add_argument("--threshold", type=int, required=True)
    p.add_argument("--dark", action="store_true")
    p.add_argument("--controls", type=Path)
    args = p.parse_args()
    report, overlay = trace(
        args.source.read_bytes(),
        args.threshold,
        args.dark,
        json.loads(args.controls.read_text()) if args.controls else None,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "features.json").write_text(json.dumps(report, allow_nan=False))
    (args.output / "overlay.png").write_bytes(overlay)
