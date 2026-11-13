"""Plan a drawing-unit change for explicit native assembly root inserts.

This module is read-only. It scales each root insertion point and its three
uniform positive scale fields by the same unit ratio, while retaining the
insert orientation and all block-internal geometry. The caller supplies both
unit definitions from the source job; no unit code implies a conversion.
"""
import copy
import math

from step_placements import native_matrix


def _unit(unit, name):
    if not isinstance(unit, dict):
        raise ValueError(name + " unit definition must be a mapping")
    label = unit.get("label")
    code = unit.get("code")
    mm_per_unit = unit.get("millimetres_per_drawing_unit")
    if not isinstance(label, str) or not label.strip():
        raise ValueError(name + " unit label required")
    if isinstance(code, bool) or not isinstance(code, int) or code < 0:
        raise ValueError(name + " unit code must be a nonnegative integer")
    if isinstance(mm_per_unit, bool) or not isinstance(mm_per_unit, (int, float)):
        raise ValueError(name + " millimetres-per-unit value required")
    if not math.isfinite(mm_per_unit) or mm_per_unit <= 0:
        raise ValueError(name + " millimetres-per-unit value must be positive and finite")
    return {"label": label, "code": code,
            "millimetres_per_drawing_unit": float(mm_per_unit)}


def _scaled_point(point, factor):
    if not isinstance(point, dict):
        raise ValueError("Root insert point must be a coordinate mapping")
    result = {}
    for axis in "xyz":
        value = point.get(axis)
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError("Root insert point must contain finite x/y/z values")
        scaled = value * factor
        if not math.isfinite(scaled):
            raise ValueError("Scaled root insert point must remain finite")
        result[axis] = scaled
    return result


def _validate_matrix(matrix, label):
    if any(not math.isfinite(value) for row in matrix for value in row):
        raise ValueError(label + " insert transform must be finite")


def plan_root_unit_change(root_inserts, *, source_unit, destination_unit):
    """Return an all-roots plan for a source-to-destination drawing unit change.

    Each root record has ``handle`` and native ``properties`` fields. The
    properties must be accepted by ``step_placements.native_matrix`` with
    ``allow_uniform_scale=True``. Array inserts, reflections, zero/nonfinite or
    nonuniform scales are rejected. Returned fields scale the root insert
    point and x/y/z scales by source-mm-per-unit / destination-mm-per-unit;
    normal and rotation remain unchanged. No CAD writes are performed.
    """
    src = _unit(source_unit, "Source")
    dst = _unit(destination_unit, "Destination")
    if not isinstance(root_inserts, (list, tuple)) or not root_inserts:
        raise ValueError("At least one root insert record is required")
    factor = src["millimetres_per_drawing_unit"] / dst["millimetres_per_drawing_unit"]
    if not math.isfinite(factor) or factor <= 0:
        raise ValueError("Unit ratio must be positive and finite")

    seen = set()
    changes = []
    for root in root_inserts:
        if (not isinstance(root, dict) or root.get("type") != "Insert"
                or not isinstance(root.get("handle"), str)
                or not root.get("handle")):
            raise ValueError("Each supported root must be an Insert record with a string handle")
        handle = root["handle"]
        if handle in seen:
            raise ValueError("Duplicate root insert handle " + handle)
        seen.add(handle)
        props = root.get("properties")
        if not isinstance(props, dict):
            raise ValueError("Root insert properties required for " + handle)
        before_matrix = native_matrix(props, allow_uniform_scale=True)
        _validate_matrix(before_matrix, "Before")
        after = copy.deepcopy(props)
        after["insert_point"] = _scaled_point(props.get("insert_point"), factor)
        for key in ("x_scale", "y_scale", "z_scale"):
            value = props.get(key)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError("Root scale must be finite for " + handle)
            scaled = value * factor
            if not math.isfinite(scaled) or scaled <= 0:
                raise ValueError("Scaled root scale must be positive and finite for " + handle)
            after[key] = scaled
        after_matrix = native_matrix(after, allow_uniform_scale=True)
        _validate_matrix(after_matrix, "Planned")
        expected_matrix = [[value * factor for value in row[:3]] + [row[3] * factor]
                           for row in before_matrix[:3]] + [[0.0, 0.0, 0.0, 1.0]]
        _validate_matrix(expected_matrix, "Expected")
        if any(abs(after_matrix[i][j] - expected_matrix[i][j]) > 1e-7
               for i in range(4) for j in range(4)):
            raise ValueError("Planned root fields do not produce the expected unit transform for " + handle)
        changes.append({"handle": handle, "before": copy.deepcopy(props),
                        "after": after, "matrix_before": before_matrix,
                        "matrix_expected": expected_matrix})

    return {"operation": "plan_only", "source_unit": src,
            "destination_unit": dst, "scale_factor": factor,
            "root_count": len(changes), "changes": changes}
