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
