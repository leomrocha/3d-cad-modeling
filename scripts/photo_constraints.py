"""Image-line constraints for a fixed pinhole camera, using pixel-distance bounds."""
import math


def _values(values, size):
    values = tuple(values)
    if len(values) != size or any(isinstance(x, bool) or not isinstance(x, (int, float))
                                  or not math.isfinite(x) for x in values):
        raise ValueError(f"Expected {size} finite numbers")
    return values


def direction_intervals(vanishing_point, picks, radius_px):
    """Closed angle intervals (radians modulo pi) of lines intersecting all pick disks."""
    vx, vy = _values(vanishing_point, 2)
    radius_px, = _values([radius_px], 1)
    if radius_px < 0:
        raise ValueError("Pixel radius must be nonnegative")
    picks = list(picks)
    if not picks:
        raise ValueError("At least one picked point is required")
    intervals = [(0.0, math.pi)]
    for point in picks:
        px, py = _values(point, 2)
        distance = math.hypot(px - vx, py - vy)
        if not math.isfinite(distance):
            raise ValueError("Pixel coordinates exceed floating point range")
        if distance <= radius_px:
            continue
        centre = math.atan2(py - vy, px - vx) % math.pi
        half = math.asin(radius_px / distance)
        allowed = [(centre + shift - half, centre + shift + half)
                   for shift in (-math.pi, 0.0, math.pi)]
        intervals = sorted({(max(lo, left), min(hi, right))
                            for lo, hi in intervals for left, right in allowed
                            if max(lo, left) <= min(hi, right)})
    return intervals


def backproject_line(camera, vanishing_point, angle):
    """Return world plane (a,b,c,d) for the image line through this vanishing point."""
    vx, vy = _values(vanishing_point, 2)
    angle, = _values([angle], 1)
    rows = [_values(row, 4) for row in camera]
    if len(rows) != 3:
        raise ValueError("Expected a 3 by 4 camera matrix")
    a, b = -math.sin(angle), math.cos(angle)
    line = a, b, -(a * vx + b * vy)
    plane = tuple(math.fsum(row[i] * weight for row, weight in zip(rows, line))
                  for i in range(4))
    if not all(map(math.isfinite, plane)) or not any(plane[:3]):
        raise ValueError("Image line does not define a finite world plane")
    return plane
