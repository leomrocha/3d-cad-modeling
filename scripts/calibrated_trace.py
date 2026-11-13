"""Map source-image points into calibrated 2D coordinates with uncertainty."""

from __future__ import annotations

import math
from collections.abc import Iterable, Sequence
from numbers import Real
from typing import Any


def _pair(value: Sequence[Real], name: str) -> tuple[float, float]:
    if isinstance(value, (str, bytes)) or len(value) != 2:
        raise ValueError(f"{name} must contain exactly two numeric values")
    result = []
    for item in value:
        if isinstance(item, bool) or not isinstance(item, Real) or not math.isfinite(item):
            raise ValueError(f"{name} values must be finite numbers")
        result.append(float(item))
    return result[0], result[1]


def _uncertainty_pair(value: Real | Sequence[Real], name: str) -> tuple[float, float]:
    if isinstance(value, Real) and not isinstance(value, bool):
        pair = (float(value), float(value))
    else:
        pair = _pair(value, name)  # type: ignore[arg-type]
    if any(not math.isfinite(item) or item < 0 for item in pair):
        raise ValueError(f"{name} values must be finite and non-negative")
    return pair


def calibrated_scale_from_reference(
    reference_length_mm: Real,
    measured_pixel_span: Real,
    *,
    length_uncertainty_mm: Real = 0,
    span_uncertainty_px: Real = 0,
) -> dict[str, float | list[float]]:
    """Calibrate millimetres per pixel from a dimensioned raster reference.

    The nominal scale is ``reference_length_mm / measured_pixel_span``.
    Endpoint ratios bound independent uncertainty in the reference length and
    traced pixel span. The returned symmetric uncertainty is the larger
    distance from the nominal scale to either conservative endpoint.
    """
    def finite_number(value: Real, name: str) -> float:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise ValueError(f"{name} must be a finite number")
        try:
            converted = float(value)
        except (OverflowError, ValueError):
            raise ValueError(f"{name} must be a finite number") from None
        if not math.isfinite(converted):
            raise ValueError(f"{name} must be a finite number")
        return converted

    length = finite_number(reference_length_mm, "reference_length_mm")
    span = finite_number(measured_pixel_span, "measured_pixel_span")
    length_u = finite_number(length_uncertainty_mm, "length_uncertainty_mm")
    span_u = finite_number(span_uncertainty_px, "span_uncertainty_px")
    if length <= 0 or span <= 0:
        raise ValueError("reference length and pixel span must be positive")
    if length_u < 0 or span_u < 0:
        raise ValueError("uncertainties must be non-negative")
    length_low, length_high = length - length_u, length + length_u
    span_low, span_high = span - span_u, span + span_u
    endpoints = (length_low, length_high, span_low, span_high)
    if any(not math.isfinite(value) for value in endpoints):
        raise ValueError("uncertainty endpoints must remain finite")
    if length_low <= 0 or span_low <= 0:
        raise ValueError("lower uncertainty endpoints must remain strictly positive")

    nominal = length / span
    lower = length_low / span_high
    upper = length_high / span_low
    uncertainty = max(nominal - lower, upper - nominal)
    if not all(math.isfinite(value) and value > 0 for value in (nominal, lower, upper)):
        raise ValueError("calibration produces a nonfinite or zero scale or bound")
    if not math.isfinite(uncertainty):
        raise ValueError("calibration produces nonfinite scale or bounds")
    return {
        "nominal_scale_mm_per_px": nominal,
        "scale_interval_mm_per_px": [lower, upper],
        "scale_uncertainty_mm_per_px": uncertainty,
    }


def calibrated_trace(
    points: Iterable[Sequence[Real]],
    pixel_origin: Sequence[Real],
    signed_scale: Sequence[Real],
    *,
    point_uncertainty_px: Real | Sequence[Real] = 0,
    origin_uncertainty_px: Real | Sequence[Real] = 0,
    scale_uncertainty_per_px: Real | Sequence[Real] = 0,
    units: str | None = None,
) -> list[dict[str, Any]]:
    """Transform 2D image points using signed per-axis scale.

    Let ``u_delta = point_px + origin_px``. The worst-case coordinate
    uncertainty for axis *i* is ``abs(scale[i])*u_delta +
    abs(point[i]-origin[i])*scale_uncertainty +
    u_delta*scale_uncertainty``. The final cross-term covers simultaneous
    endpoint variation of the pixel difference and scale.
    Signed scales support axis reversal; uncertainty always uses absolute
    magnitudes. Inputs must be finite, scale must be nonzero, and all stated
    uncertainties must be non-negative.
    """
    origin = _pair(pixel_origin, "pixel_origin")
    scale = _pair(signed_scale, "signed_scale")
    if any(value == 0 for value in scale):
        raise ValueError("signed_scale values must be nonzero")
    point_u = _uncertainty_pair(point_uncertainty_px, "point_uncertainty_px")
    origin_u = _uncertainty_pair(origin_uncertainty_px, "origin_uncertainty_px")
    scale_u = _uncertainty_pair(scale_uncertainty_per_px, "scale_uncertainty_per_px")
    if units is not None and (not isinstance(units, str) or not units.strip()):
        raise ValueError("units must be a non-empty string when provided")

    result = []
    for index, point in enumerate(points):
        px = _pair(point, f"points[{index}]")
        delta = (px[0] - origin[0], px[1] - origin[1])
        coordinates = (delta[0] * scale[0], delta[1] * scale[1])
        delta_u = (point_u[0] + origin_u[0], point_u[1] + origin_u[1])
        uncertainty = tuple(
            delta_u[i] * abs(scale[i])
            + abs(delta[i]) * scale_u[i]
            + delta_u[i] * scale_u[i]
            for i in range(2)
        )
        if any(not math.isfinite(value) for value in (*delta, *coordinates, *uncertainty)):
            raise ValueError(f"points[{index}] produce nonfinite calibrated coordinates or bounds")
        record: dict[str, Any] = {
            "source_pixel": [px[0], px[1]],
            "coordinates": [coordinates[0], coordinates[1]],
            "uncertainty_worst_case": [uncertainty[0], uncertainty[1]],
        }
        if units is not None:
            record["units"] = units
        result.append(record)
    return result
