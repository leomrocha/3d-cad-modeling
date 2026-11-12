#!/usr/bin/env python3
"""Reference CadQuery generator for an explicitly dimensioned drilled plate.

Input dimensions are required in JSON and millimetres. This file is reference
code; it has not been run against a CadQuery installation in this project.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import cadquery as cq


def number(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a numeric value")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{label} must be finite")
    return result


def build(parameters: dict[str, Any]) -> cq.Workplane:
    if parameters.get("units") != "mm":
        raise ValueError("units must be explicitly set to 'mm'")
    part = parameters.get("part")
    if not isinstance(part, dict):
        raise ValueError("part object is required")
    name = part.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("part.name is required")
    length = number(part.get("length"), "part.length")
    width = number(part.get("width"), "part.width")
    thickness = number(part.get("thickness"), "part.thickness")
    if min(length, width, thickness) <= 0:
        raise ValueError("length, width and thickness must be positive")

    holes = parameters.get("through_holes")
    if not isinstance(holes, list):
        raise ValueError("through_holes must be present as a list; use [] explicitly")

    normalized: list[tuple[float, float, float]] = []
    for index, hole in enumerate(holes):
        if not isinstance(hole, dict):
            raise ValueError(f"through_holes[{index}] must be an object")
        x = number(hole.get("x"), f"through_holes[{index}].x")
        y = number(hole.get("y"), f"through_holes[{index}].y")
        diameter = number(hole.get("diameter"), f"through_holes[{index}].diameter")
        radius = diameter / 2.0
        if diameter <= 0:
            raise ValueError(f"through_holes[{index}].diameter must be positive")
        if abs(x) + radius >= length / 2 or abs(y) + radius >= width / 2:
            raise ValueError(f"through_holes[{index}] does not fit inside the plate")
        for old_x, old_y, old_radius in normalized:
            if math.hypot(x - old_x, y - old_y) <= radius + old_radius:
                raise ValueError(f"through_holes[{index}] overlaps or touches another hole")
        normalized.append((x, y, radius))

    # Datum: XY origin is the plate plan center; Z=0 is the bottom face.
    result = cq.Workplane("XY").box(
        length, width, thickness, centered=(True, True, False)
    )
    for x, y, radius in normalized:
        cutter = cq.Workplane("XY").center(x, y).circle(radius).extrude(thickness)
        result = result.cut(cutter)

    shape = result.val()
    if not shape.isValid():
        raise ValueError("CadQuery/OCCT reports an invalid result shape")
    if result.solids().size() != 1:
        raise ValueError("expected exactly one connected solid")
    bounds = shape.BoundingBox()
    tolerance = 1e-7  # millimetres; numerical comparison only
    expected = (length, width, thickness)
    actual = (bounds.xlen, bounds.ylen, bounds.zlen)
    if any(abs(a - e) > tolerance for a, e in zip(actual, expected)):
        raise ValueError(f"bounding dimensions {actual} mm differ from {expected} mm")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parameters", type=Path, required=True, help="source-linked JSON dimensions")
    parser.add_argument("--step", type=Path, required=True, help="new .step output path")
    parser.add_argument("--overwrite", action="store_true", help="allow replacing an existing STEP output")
    args = parser.parse_args()

    input_path = args.parameters.resolve(strict=True)
    output_path = args.step.resolve()
    if input_path == output_path:
        raise SystemExit("parameter JSON and STEP output must be separate files")
    if output_path.suffix.lower() != ".step":
        raise SystemExit("output path must use the .step extension")
    if output_path.exists() and not args.overwrite:
        raise SystemExit(f"output exists; pass --overwrite to replace it: {output_path}")

    parameters = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(parameters, dict):
        raise SystemExit("parameter JSON root must be an object")
    result = build(parameters)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.export(str(output_path), unit="MM", outputUnit="MM")

    # Read the neutral exchange file back through CadQuery before reporting it.
    reopened = cq.importers.importStep(str(output_path), unit="MM")
    if not reopened.val().isValid() or reopened.solids().size() != 1:
        raise SystemExit("STEP readback failed validity or single-solid check")
    print(json.dumps({
        "status": "reference-code-result",
        "units": "mm",
        "parameter_file": str(input_path),
        "parameter_file_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
        "step_file": str(output_path),
        "solid_count": reopened.solids().size(),
        "bounding_box_mm": {
            "x": reopened.val().BoundingBox().xlen,
            "y": reopened.val().BoundingBox().ylen,
            "z": reopened.val().BoundingBox().zlen,
        },
        "volume_mm3": reopened.val().Volume(),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
