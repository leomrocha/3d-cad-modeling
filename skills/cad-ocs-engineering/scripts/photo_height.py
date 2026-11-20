"""Transfer a reference height between two vertical lines on a common base plane."""

import argparse
import json
import math
from pathlib import Path


def measure(job):
    import numpy as np

    def point(name):
        coords = np.asarray(job[name], dtype=float)
        if coords.shape != (2,) or not np.isfinite(coords).all():
            raise ValueError("Expected two image coordinates for " + name)
        return np.r_[coords, 1.0]

    def direction(name):
        v = np.asarray(job[name], dtype=float)
        if v.shape != (3,) or not np.isfinite(v).all() or np.linalg.norm(v) == 0:
            raise ValueError("Expected nonzero homogeneous coordinates for " + name)
        return v / np.linalg.norm(v)

    def intersection(line1, line2):
        v = np.cross(line1, line2)
        if np.linalg.norm(v) <= 1e-10 * np.linalg.norm(line1) * np.linalg.norm(line2):
            raise ValueError("Degenerate lines in height transfer")
        return v

    horizon = direction("base_vanishing_line")
    vp = direction("vertical_vanishing_point")
    if abs(np.dot(horizon, vp)) < 1e-10:
        raise ValueError("Vertical direction lies in the base plane")
    if not job.get("plane_evidence") or not job.get("direction_evidence"):
        raise ValueError(
            "Identify the common base plane and parallel height directions"
        )
    height = float(job["reference_height_mm"])
    tolerance = float(job["max_line_error_px"])
    if (
        not math.isfinite(height)
        or height <= 0
        or not math.isfinite(tolerance)
        or tolerance < 0
    ):
        raise ValueError("Invalid reference height or pick tolerance")
    ref, top, base, target = map(
        point, ("reference_base", "reference_top", "target_base", "target_top")
    )
    errors = []
    for b, t in [(ref, top), (base, target)]:
        vertical = np.cross(b, vp)
        length = np.linalg.norm(vertical[:2])
        if length < 1e-12:
            raise ValueError("Base coincides with vertical vanishing point")
        errors.append(float(abs(np.dot(t, vertical)) / length))
    if max(errors) > tolerance:
        raise ValueError("Selected top exceeds its vertical-line pick tolerance")
    along_base = intersection(np.cross(ref, base), horizon)
    equal = intersection(np.cross(top, along_base), np.cross(base, vp))
    if abs(equal[2]) < 1e-10 * np.linalg.norm(equal):
        raise ValueError("Transferred reference height lies at infinity")
    delta = equal[:2] / equal[2] - base[:2]
    if np.linalg.norm(delta) < 1e-7:
        raise ValueError("Reference height projects to zero at the target")
    unit = delta / np.linalg.norm(delta)
    t = np.dot(target[:2] - base[:2], unit)
    q = np.linalg.norm(delta)
    v = np.dot(vp[:2] - vp[2] * base[:2], unit)
    denominator = q * (v - vp[2] * t)
    if abs(denominator) < 1e-12:
        raise ValueError("Target height projects at the vanishing point")
    ratio = t * (v - vp[2] * q) / denominator
    return dict(
        target_height_mm=float(height * ratio),
        vertical_line_residuals_px=errors,
        transferred_reference_top_px=(base[:2] + delta).tolist(),
    )


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("spec", type=Path)
    p.add_argument("new_receipt", type=Path)
    args = p.parse_args()
    job = json.loads(args.spec.read_text())
    result = measure(job)
    with args.new_receipt.open("x") as stream:
        json.dump(dict(inputs=job, **result), stream, indent=2, allow_nan=False)
        stream.write("\n")
