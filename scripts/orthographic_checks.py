"""Check one physical landmark in named orthographic views, in common datum mm."""
import math
from itertools import combinations

from cadtools.geometry import finite


def compare_landmark(views):
    """Each view maps a world axis to (signed coordinate, worst-case uncertainty).

    Call once per source revision, frame and physical landmark after transforming
    picks into that frame. Shared-axis agreement checks consistency only.
    """
    if len(views) < 2:
        raise ValueError("At least two named views are required")
    readings = {}
    for name, axes in views.items():
        if not isinstance(name, str) or not name.strip() or len(axes) != 2 or set(axes) - {"X", "Y", "Z"}:
            raise ValueError("Each named view requires two distinct world axes")
        for axis, (coordinate, uncertainty) in axes.items():
            coordinate, uncertainty = finite(coordinate), finite(uncertainty)
            if uncertainty < 0:
                raise ValueError("Expected non-negative uncertainty in mm")
            readings.setdefault(axis, []).append((name, coordinate, uncertainty))
    checks = []
    for axis, entries in sorted(readings.items()):
        for (a, x, ux), (b, y, uy) in combinations(entries, 2):
            residual, bound = abs(x - y), ux + uy
            if not all(map(math.isfinite, (residual, bound))):
                raise ValueError("Coordinate difference or uncertainty sum overflowed")
            checks.append(dict(axis=axis, views=[a, b], difference_mm=residual,
                               combined_bound_mm=bound, consistent=residual <= bound))
    return dict(consistent=all(check["consistent"] for check in checks), comparisons=checks)
