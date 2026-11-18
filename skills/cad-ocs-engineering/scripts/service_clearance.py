"""Offline straight-translation checks in one caller-declared world frame.

Inputs are finite Python integers or binary64 coordinates in one length unit.
Fractions keep comparisons and interval endpoints exact for the supplied data.
"""

from fractions import Fraction
import math


def _vector(values, size):
    if len(values) != size or any(
        type(value) not in (int, float)
        or (type(value) is float and not math.isfinite(value))
        for value in values
    ):
        raise ValueError(f"Expected {size} finite coordinates")
    return tuple(Fraction(value) for value in values)


def _bounds(bounds):
    if len(bounds) != 2:
        raise ValueError("Expected minimum and maximum XYZ corners")
    low, high = (_vector(point, 3) for point in bounds)
    if any(a > b for a, b in zip(low, high)):
        raise ValueError("Bounding-box minima must precede maxima")
    return low, high


def translation_box_window(moving_bounds, fixed_bounds, displacement):
    """Find the closed candidate interval over a finite straight translation.

    Bounds must conservatively enclose the represented geometry. Displacement
    is the full XYZ travel. Fractions of that travel are returned as exact
    strings. Touching boxes are candidates, including at either endpoint.
    """
    moving_low, moving_high = _bounds(moving_bounds)
    fixed_low, fixed_high = _bounds(fixed_bounds)
    start, end = Fraction(0), Fraction(1)
    for low, high, other_low, other_high, delta in zip(
        moving_low, moving_high, fixed_low, fixed_high, _vector(displacement, 3)
    ):
        if delta == 0:
            if high < other_low or other_high < low:
                return {"result": "DISJOINT_BOUNDS", "candidate_fraction": None}
            continue
        first = (other_low - high) / delta
        last = (other_high - low) / delta
        start = max(start, min(first, last))
        end = min(end, max(first, last))
        if start > end:
            return {"result": "DISJOINT_BOUNDS", "candidate_fraction": None}
    return {"result": "CANDIDATE", "candidate_fraction": [str(start), str(end)]}


def _affine(matrix):
    if len(matrix) != 4:
        raise ValueError("Expected a 4x4 affine placement")
    rows = tuple(_vector(row, 4) for row in matrix)
    if rows[3] != (0, 0, 0, 1):
        raise ValueError("Expected affine last row [0, 0, 0, 1]")
    a, b, c = (row[:3] for row in rows[:3])
    determinant = sum(a[i] * (b[(i+1)%3]*c[(i+2)%3] - b[(i+2)%3]*c[(i+1)%3])
                      for i in range(3))
    if determinant == 0:
        raise ValueError("Placement must be nonsingular")
    return rows[:3]


def shared_definition_coincidence(moving_matrix, fixed_matrix, displacement):
    """Find a pose of exact coincidence for a caller-verified shared definition.

    Both placements must map the same nonempty geometry definition into world
    coordinates. This test supplies a witness pose, with no first-contact time.
    """
    moving = _affine(moving_matrix)
    fixed = _affine(fixed_matrix)
    deltas = _vector(displacement, 3)
    if any(a[:3] != b[:3] for a, b in zip(moving, fixed)):
        return {"result": "NO_COINCIDENCE_WITNESS", "travel_fraction": None}

    fractions = set()
    for a, b, delta in zip(moving, fixed, deltas):
        offset = b[3] - a[3]
        if delta == 0:
            if offset:
                return {"result": "NO_COINCIDENCE_WITNESS", "travel_fraction": None}
        else:
            fractions.add(offset / delta)
    fraction = min(fractions, default=Fraction(0))
    if len(fractions) > 1 or not 0 <= fraction <= 1:
        return {"result": "NO_COINCIDENCE_WITNESS", "travel_fraction": None}
    return {"result": "COINCIDENCE_WITNESS", "travel_fraction": str(fraction)}
