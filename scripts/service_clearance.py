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


def sampled_rotation_clearance(samples, *, radius_bound, gap_error_bound,
                               required_reserve=0):
    """Bound continuous clearance for one body rotating about a fixed axis.

    Samples give increasing angles in degrees, including both sweep limits,
    and signed clearance witnesses to one stationary obstacle. Subtract the
    supplied gap error bound, which must cover geometry and readback error.
    The radius bound encloses every moving point's distance to the axis.
    Length inputs use one common unit. A non-positive demonstrated reserve
    leaves clearance unresolved, since the bound can be conservative.
    """
    radius, error, reserve = _vector((radius_bound, gap_error_bound, required_reserve), 3)
    witnesses = [_vector(row, 2) for row in samples]
    if len(witnesses) < 2 or min(radius, error, reserve) < 0:
        raise ValueError("Expected two or more samples and nonnegative bounds")
    # Rational upper bound on pi. Arc length bounds rigid displacement.
    upper_pi = Fraction("3.141592653589793239")
    intervals = []
    for (a, first_gap), (b, last_gap) in zip(witnesses, witnesses[1:]):
        if b <= a:
            raise ValueError("Sample angles must increase")
        half_interval_travel = radius * (b-a) * upper_pi / 360
        intervals.append((min(first_gap, last_gap)-error-half_interval_travel, a, b))
    lower, start, end = min(intervals)
    return dict(result="PASS_CONTINUOUS_RESERVE" if lower > reserve else "UNRESOLVED_RESERVE",
                lower_bound=str(lower), required_reserve=str(reserve),
                limiting_angles_deg=[str(start), str(end)])


def cartesian_cylinder_bounds(centre, *, axis, radius, span):
    """Enclose a finite cylinder with an axis parallel to a Cartesian axis.

    The caller supplies the maximum material radius and two measured absolute
    end stations in the same frame. The centre's coordinate along the axis
    does not affect the box. Use separately bounded heads and shoulders when
    checking clearance for only part of an assembly.
    """
    if type(axis) is not int or not 0 <= axis < 3:
        raise ValueError("Expected an XYZ axis index")
    centre = _vector(centre, 3)
    radius, = _vector((radius,), 1)
    start, stop = _vector(span, 2)
    if radius <= 0 or start >= stop:
        raise ValueError("Expected a positive radius and increasing end stations")
    low = [value - radius for value in centre]
    high = [value + radius for value in centre]
    low[axis], high[axis] = start, stop

    def round_outward(value, direction):
        try:
            result = float(value)
        except OverflowError as error:
            raise ValueError("Cylinder bounds exceed finite coordinates") from error
        rounded = Fraction(result)
        if (direction < 0 and rounded > value) or (direction > 0 and rounded < value):
            result = math.nextafter(result, direction)
        if not math.isfinite(result):
            raise ValueError("Cylinder bounds exceed finite coordinates")
        return result

    return [[round_outward(value, direction) for value in boundary]
            for boundary, direction in ((low, -math.inf), (high, math.inf))]


def guided_circular_pilot_clearance(*, slot_centres, slot_radius, travel_centres,
                                   pilot_radius, side_play, minimum_reserve=0):
    """Check a circular pilot constrained by separate straight guides.

    Longitudinal stations use the frame of the capsule slot's straight centre
    segment. The nominal transverse station is zero. Side play bounds the
    complete transverse displacement, including any tolerances supplied by
    the caller. Use the smallest slot and largest pilot bounding radii.
    """
    slot_start, slot_end = _vector(slot_centres, 2)
    start, end = _vector(travel_centres, 2)
    opening, pilot, play, reserve = _vector(
        (slot_radius, pilot_radius, side_play, minimum_reserve), 4)
    if slot_start >= slot_end or start > end or min(opening, pilot) <= 0 or min(play, reserve) < 0:
        raise ValueError("Expected increasing slot centres, ordered travel and positive radii")

    overrun = max(slot_start - start, end - slot_end, Fraction(0))
    squared_displacement = overrun**2 + play**2
    available = opening - pilot
    residual = available - reserve
    passes = residual >= 0 and squared_displacement <= residual**2
    return dict(
        result="PASS_NOMINAL_CAPSULE_CLEARANCE" if passes else "FAIL_REQUIRED_CLEARANCE",
        minimum_slot_gap=float(available) - math.hypot(float(overrun), float(play)),
        longitudinal_overrun=float(overrun),
        maximum_side_play=float(play),
        required_reserve=float(reserve),
    )


def static_box_gap(first_bounds, second_bounds):
    """Return exact squared separation for two axis-aligned boxes in one frame.

    Zero means the boxes touch or overlap. A positive gap between conservative
    enclosures bounds the separation of their enclosed geometry from below.
    """
    first_low, first_high = _bounds(first_bounds)
    second_low, second_high = _bounds(second_bounds)
    axis_gaps = tuple(max(a-d, c-b, Fraction(0))
                      for a,b,c,d in zip(first_low,first_high,second_low,second_high))
    squared_gap = sum(gap*gap for gap in axis_gaps)
    return dict(result='DISJOINT_BOUNDS' if squared_gap else 'CANDIDATE',
                axis_gaps=[str(gap) for gap in axis_gaps], squared_gap=str(squared_gap))


def static_box_contact_dimension(first_bounds, second_bounds):
    """Return the contact dimension of two closed XYZ boxes, or None if disjoint.

    Dimensions 0, 1, 2, and 3 mean a point, line, face, and volume respectively.
    For boxes enclosing solids, a result supplies a candidate for the geometry.
    """
    first_low, first_high = _bounds(first_bounds)
    second_low, second_high = _bounds(second_bounds)
    spans = [min(b,d)-max(a,c) for a,b,c,d in
             zip(first_low,first_high,second_low,second_high,strict=True)]
    return dict(dimension=None if min(spans)<0 else sum(span>0 for span in spans),
                signed_axis_spans=[str(span) for span in spans])


def bounded_axial_section_clearance(full_bounds, section_bounds, obstacle_bounds, *, axis):
    """Refine a box candidate using a verified material bound in one axial slab.

    The caller establishes that section_bounds encloses all source material
    between its two axial endpoints. The method uses that section only if it
    covers the entire axial overlap between the full source and obstacle boxes.
    """
    if type(axis) is not int or not 0 <= axis < 3:
        raise ValueError('Expected an XYZ axis index')
    full_low, full_high = _bounds(full_bounds)
    section_low, section_high = _bounds(section_bounds)
    obstacle_low, obstacle_high = _bounds(obstacle_bounds)
    if section_low[axis] >= section_high[axis]:
        raise ValueError('Expected a section of positive axial length')
    if static_box_gap(full_bounds, obstacle_bounds)['result'] == 'DISJOINT_BOUNDS':
        return dict(result='DISJOINT_FULL_BOUNDS', axial_overlap=None)
    lo = max(full_low[axis], obstacle_low[axis])
    hi = min(full_high[axis], obstacle_high[axis])
    overlap = [str(lo), str(hi)]
    if lo < section_low[axis] or hi > section_high[axis]:
        return dict(result='SECTION_DOES_NOT_COVER_OVERLAP', axial_overlap=overlap)
    # An axial gap at the slab boundary cannot prove transverse separation.
    transverse_gaps = [max(section_low[i]-obstacle_high[i], obstacle_low[i]-section_high[i], 0)
                       for i in range(3) if i != axis]
    gap = max(transverse_gaps)
    result = 'DISJOINT_SECTION_BOUNDS' if gap > 0 else 'SECTION_CONTACT_CANDIDATE'
    return dict(result=result, axial_overlap=overlap, transverse_axis_gap=str(gap))


def rpy_world_x_bounds(bounds, *, pivot, roll_deg, pitch_deg, yaw_deg):
    """Bound world X for a box under symmetric Rz(yaw) Ry(pitch) Rx(roll).

    The input box encloses the component at zero angles. Each stated limit
    covers both signs. The result covers the whole independent angle domain.
    """
    low, high = _bounds(bounds)
    centre = _vector(pivot, 3)
    angles = _vector((roll_deg, pitch_deg, yaw_deg), 3)
    if any(angle < 0 or angle > 90 for angle in angles):
        raise ValueError("Expected symmetric roll, pitch and yaw limits from zero to 90 degrees")
    roll, pitch, yaw = (math.radians(float(angle)) for angle in angles)
    sr, sp, sy = (math.sin(angle) for angle in (roll, pitch, yaw))
    minimum_x_coefficient = math.cos(pitch) * math.cos(yaw)
    relative_low = tuple(float(value - origin) for value, origin in zip(low, centre, strict=True))
    relative_high = tuple(float(value - origin) for value, origin in zip(high, centre, strict=True))
    x_low, y_low, z_low = relative_low
    x_high, y_high, z_high = relative_high
    lateral = (sy + sp * sr) * max(abs(y_low), abs(y_high))
    vertical = (sp + sy * sr) * max(abs(z_low), abs(z_high))
    l = float(centre[0]) + min(x_low, minimum_x_coefficient * x_low) - lateral - vertical
    h = float(centre[0]) + max(x_high, minimum_x_coefficient * x_high) + lateral + vertical
    if not math.isfinite(l) or not math.isfinite(h):
        raise ValueError("Motion bound exceeds representable coordinates")
    return l, h


def orthogonal_sleeve_clearance(first, second):
    """Screen two square-ended annular cylinders parallel to distinct XYZ axes.

    Each sleeve supplies axis (0, 1 or 2), centre (XYZ), span on its axis,
    and inner and outer radii. The line through their nearest axis points
    supplies a strict material witness only when it crosses both open spans.
    """
    axes = (first['axis'], second['axis'])
    if any(type(axis) is not int or not 0 <= axis < 3 for axis in axes) or axes[0] == axes[1]:
        raise ValueError('Expected two distinct XYZ axes')
    centres, spans, radii = [], [], []
    for sleeve in (first, second):
        centres.append(_vector(sleeve['centre'], 3))
        span = _vector(sleeve['span'], 2)
        radial = _vector(sleeve['radii'], 2)
        if span[0] >= span[1] or not 0 <= radial[0] < radial[1]:
            raise ValueError('Expected an increasing axial span and inner/outer radii')
        spans.append(span)
        radii.append(radial)

    normal = 3 - sum(axes)
    locations = [centre[normal] for centre in centres]
    gap = abs(locations[0] - locations[1]) - radii[0][1] - radii[1][1]
    result = dict(signed_outer_gap=str(gap), normal_axis=normal, witness=None)
    if gap > 0:
        return dict(result, result='DISJOINT_OUTER_CYLINDERS')
    for axis, span, other in zip(axes, spans, reversed(centres), strict=True):
        if not span[0] < other[axis] < span[1]:
            return dict(result, result='NEEDS_FINITE_SOLID_CHECK')

    def material_intervals(centre, radius):
        inner, outer = radius
        return ((centre - outer, centre - inner), (centre + inner, centre + outer))

    first_walls, second_walls = (material_intervals(c, r) for c, r in zip(locations, radii, strict=True))
    for lo, hi in first_walls:
        for other_lo, other_hi in second_walls:
            lower, upper = max(lo, other_lo), min(hi, other_hi)
            if lower < upper:
                witness = [None] * 3
                witness[axes[0]] = centres[1][axes[0]]
                witness[axes[1]] = centres[0][axes[1]]
                witness[normal] = (lower + upper) / 2
                return dict(result, result='STRICT_MATERIAL_INTERSECTION', witness=list(map(str,witness)))
    return dict(result, result='NEEDS_FINITE_SOLID_CHECK')


def translated_box_group_margin(moving, fixed, displacement):
    """Return the smallest signed separating-axis margin at one pose.

    Both groups provide ordered boxes in one Cartesian frame. A positive
    margin separates all pairs, zero permits boundary contact, and a
    negative result identifies a pair of overlapping enclosures.
    """
    delta = _vector(displacement, 3)
    movers = [tuple(tuple(x + d for x, d in zip(point, delta)) for point in _bounds(box))
              for box in moving]
    obstacles = [_bounds(box) for box in fixed]
    if not movers or not obstacles:
        raise ValueError("Both box groups must contain at least one box")
    minimum = None
    limiting = []
    for i, (a0, a1) in enumerate(movers):
        for j, (b0, b1) in enumerate(obstacles):
            axes = [max(lo - end, start - hi) for lo, end, start, hi in zip(a0, b1, b0, a1)]
            margin = max(axes)
            if minimum is None or margin < minimum:
                minimum = margin
                limiting = []
            if margin == minimum:
                limiting.append(dict(moving_index=i, fixed_index=j,
                                     axes=[k for k, value in enumerate(axes) if value == margin]))
    return dict(minimum_axis_margin=str(minimum), pair_count=len(movers) * len(obstacles),
                limiting_pairs=limiting)


def rectangle_radial_bounds(bounds, centre):
    """Return exact squared radial extrema over a closed planar rectangle."""
    low, high = (_vector(corner, 2) for corner in bounds)
    centre = _vector(centre, 2)
    if any(a > b for a, b in zip(low, high)):
        raise ValueError("Rectangle minima must precede maxima")
    near = [max(a - c, c - b, 0) for a, b, c in zip(low, high, centre)]
    far = [max(abs(a - c), abs(b - c)) for a, b, c in zip(low, high, centre)]
    return dict(min_radius_squared=str(sum(d * d for d in near)),
                max_radius_squared=str(sum(d * d for d in far)))


def static_box_halfspace_gap(bounds, *, normal, offset):
    """Screen a box against a part contained in normal · point <= offset."""
    low, high = _bounds(bounds)
    direction = _vector(normal, 3)
    station, = _vector((offset,), 1)
    squared_length = sum(term**2 for term in direction)
    if not squared_length:
        raise ValueError('Nonzero plane normal required')
    nearest = sum(n*(a if n >= 0 else b)
                  for n,a,b in zip(direction,low,high,strict=True))
    excess = nearest - station
    return dict(result='DISJOINT_BOUNDS' if excess > 0 else 'CANDIDATE',
                minimum_plane_excess=str(excess),
                gap_squared=str(max(excess,0)**2/squared_length))


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


def translation_box_contact(moving_bounds, fixed_bounds, displacement):
    """Classify the maximum enclosure contact dimension over straight travel.

    A boundary-only result rules out positive-volume overlap of the supplied
    conservative boxes. Check the required separation and permission for
    contact separately. A volume candidate requires a more precise check.
    """
    window = translation_box_window(moving_bounds, fixed_bounds, displacement)
    interval = window["candidate_fraction"]
    if interval is None:
        return dict(window, dimension=None)

    # Within the relative interior of the closed contact interval, each
    # axis has either a positive overlap or a persistent boundary contact.
    start, end = map(Fraction, interval)
    witness = (start + end) / 2
    low, high = _bounds(moving_bounds)
    fixed_low, fixed_high = _bounds(fixed_bounds)
    offset = [witness * delta for delta in _vector(displacement, 3)]
    spans = [
        min(b + d, v) - max(a + d, u)
        for a, b, u, v, d in zip(low, high, fixed_low, fixed_high, offset, strict=True)
    ]
    dimension = sum(span > 0 for span in spans)
    return dict(result="VOLUME_CANDIDATE" if dimension == 3 else "BOUNDARY_ONLY",
                candidate_fraction=interval, dimension=dimension,
                witness_fraction=str(witness))


def quarter_turn_box(bounds, *, pivot, axis, direction):
    """Conservatively enclose an axis-aligned box over a signed 90° turn.

    The pivot is any point on the fixed world-coordinate axis. The output
    is an axis-aligned screening envelope, including the closed start and
    end poses. Intersections remain candidates for a narrower check.
    """
    if type(axis) is not int or axis not in (0, 1, 2):
        raise ValueError("Expected Cartesian axis 0, 1 or 2")
    if type(direction) is not int or direction not in (-1, 1):
        raise ValueError("Expected quarter-turn direction -1 or 1")
    minimum, maximum = _bounds(bounds)
    origin = _vector(pivot, 3)
    u, v = (axis + 1) % 3, (axis + 2) % 3
    un, up = max(0, origin[u]-minimum[u]), max(0, maximum[u]-origin[u])
    vn, vp = max(0, origin[v]-minimum[v]), max(0, maximum[v]-origin[v])
    if direction == 1:
        limits = ((un, vp, up, vn), (vn, un, vp, up))
    else:
        limits = ((un, vn, up, vp), (vn, up, vp, un))
    result = [list(map(float, minimum)), list(map(float, maximum))]
    for dimension, (n1,n2,p1,p2) in zip((u,v),limits,strict=True):
        result[0][dimension] = math.nextafter(float(origin[dimension])-math.hypot(n1,n2), -math.inf)
        result[1][dimension] = math.nextafter(float(origin[dimension])+math.hypot(p1,p2), math.inf)
    return result


def planar_translation_pieces(vertices, displacement):
    """Return polygon pieces whose union is one planar linear sweep.

    Provide an ordered, simple, filled polygon ring without holes and a
    finite displacement in its plane. Validate ring topology with the
    input geometry provider. The first and last positions and the swept
    nonparallel boundary segments cover the entire movement.
    """
    points = tuple(tuple(point) for point in vertices)
    if points and points[0] == points[-1]:
        points = points[:-1]
    exact = tuple(_vector(point, 2) for point in points)
    delta = _vector(displacement, 2)
    if len(exact) < 3 or len(set(exact)) != len(exact):
        raise ValueError("Expected at least three distinct ring vertices")
    if not any(delta):
        return (points,)
    translated = tuple(tuple(float(a+b) for a,b in zip(point,delta)) for point in exact)
    sides = []
    for end in range(len(points)):
        start = end-1
        dx,dy = (b-a for a,b in zip(exact[start],exact[end]))
        if dx*delta[1] != dy*delta[0]:
            sides.append((points[start],points[end],translated[end],translated[start]))
    return (points,translated,*sides)


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


def axial_section_window(moving_span, fixed_span, travel, *, clearance=0):
    """Bound source stations that can approach a fixed slab during axial travel.

    Inputs are ordered station intervals on the same axis. Travel gives the
    least and greatest signed displacement from the moving source pose.
    Output strings are exact rationals in the caller's length unit.
    """
    moving_low, moving_high = _vector(moving_span, 2)
    fixed_low, fixed_high = _vector(fixed_span, 2)
    first, last = _vector(travel, 2)
    margin, = _vector([clearance], 1)
    if moving_low > moving_high or fixed_low > fixed_high or first > last or margin < 0:
        raise ValueError("Ordered spans, ordered travel and nonnegative clearance required")
    gap = max(fixed_low - moving_high - last, moving_low + first - fixed_high, 0)
    low = max(moving_low, fixed_low - margin - last)
    high = min(moving_high, fixed_high + margin - first)
    return dict(axial_gap_lower_bound=str(gap),
                source_section=[str(low), str(high)] if low <= high else None)


def axial_stack_witness(shaft_span, layers, *, axis_sign=1):
    """Compare consecutive axial layers against a shaft's modeled reach.

    Supply increasing coordinate spans in one model axis. Layer order
    follows the shaft from shoulder to tip. Set axis_sign=-1 when the
    shaft points along the decreasing model coordinate. Positive seat
    and interface gaps mean separation. Negative gaps mean axial overlap.
    Last-layer shaft overlap measures geometric reach. Return exact
    rational station differences.
    """
    if type(axis_sign) is not int or axis_sign not in (-1, 1):
        raise ValueError("Shaft axis sign must be 1 or -1")
    first, last = _vector(shaft_span, 2)
    spans = [_vector(layer, 2) for layer in layers]
    if first >= last or not spans or any(low >= high for low, high in spans):
        raise ValueError("Positive shaft length and one or more positive layer spans required")
    shoulder, tip = first, last
    if axis_sign == -1:
        shoulder, tip = -last, -first
        spans = [(-high, -low) for low, high in spans]
    last_entry, last_exit = spans[-1]
    overlap = max(Fraction(0), min(tip, last_exit) - max(shoulder, last_entry))
    return {
        "seat_gap": str(spans[0][0] - shoulder),
        "interface_gaps": [str(right[0] - left[1]) for left, right in zip(spans, spans[1:])],
        "last_layer_overlap": str(overlap),
        "tip_past_stack": str(tip - last_exit),
    }
