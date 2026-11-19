"""Rigid planar mounting-pattern checks. Coordinates and radii share one length unit."""
from itertools import combinations, permutations
import math

from cadtools.geometry import finite, vector


def _circles(rows):
    circles = []
    for centre, radius in rows:
        if finite(radius) < 0:
            raise ValueError('Circle radius must be nonnegative')
        circles.append((vector(centre, 2), radius))
    if not circles:
        raise ValueError('Pattern must contain at least one feature')
    return circles


def screen_assignments(board, openings, *, tolerance, max_assignments=100000):
    """Test every injection using spans invariant under rigid placement.

    Each row is (centre_xy, enclosing_radius). The enclosure may overestimate
    a compound opening. A survivor permits further testing. The tolerance
    is an additional nonnegative length allowance on each span comparison.
    """
    board, openings = _circles(board), _circles(openings)
    if finite(tolerance) < 0 or type(max_assignments) is not int or max_assignments < 1:
        raise ValueError('Require nonnegative tolerance and positive assignment limit')
    total = math.perm(len(openings), len(board))
    if total > max_assignments:
        raise ValueError('Assignment count exceeds explicit search budget')
    spans = [(i, j, math.dist(board[i][0], board[j][0]), board[i][1] + board[j][1])
             for i, j in combinations(range(len(board)), 2)]
    survivors = []
    for assignment in permutations(range(len(openings)), len(board)):
        for i, j, span, allowance in spans:
            a, b = openings[assignment[i]], openings[assignment[j]]
            mismatch = abs(span - math.dist(a[0], b[0]))
            if mismatch > allowance + a[1] + b[1] + tolerance:
                break
        else:
            survivors.append(assignment)
    return dict(tested=total, survivors=survivors,
                state='NECESSARY_CONDITIONS_MET' if survivors else 'ALL_ASSIGNMENTS_EXCLUDED')


def finite_pin_witness(board, bores, assignment, *, angle_degrees, translation,
                       pin_axes, pin_radius, minimum_gap=0):
    """Verify one supplied pose and finite pin axes against actual circular bores.

    Assignment indexes the fixed bores in moving board order. Pin axes and
    translation are expressed in the fixed frame. Each pin requires strictly
    more radial clearance than minimum_gap through both projected circles.
    """
    board, bores = _circles(board), _circles(bores)
    if len(assignment) != len(board) or len(pin_axes) != len(board):
        raise ValueError('Require one fixed bore and pin axis per board feature')
    if any(type(i) is not int or not 0 <= i < len(bores) for i in assignment) or len(set(assignment)) != len(board):
        raise ValueError('Require distinct valid fixed-bore indices')
    if finite(pin_radius) <= 0 or finite(minimum_gap) < 0:
        raise ValueError('Require positive pin radius and nonnegative clearance')
    tx, ty = vector(translation, 2)
    theta = math.radians(finite(angle_degrees))
    c, s = math.cos(theta), math.sin(theta)
    pairs = []
    for ((x, y), radius), idx, axis in zip(board, assignment, pin_axes):
        axis = vector(axis, 2)
        placed = (c*x-s*y+tx, s*x+c*y+ty)
        fixed, fixed_radius = bores[idx]
        pairs.append(dict(bore=idx, axis=axis, placed_board_center=placed,
                          board_gap=radius-math.dist(axis, placed)-pin_radius,
                          bore_gap=fixed_radius-math.dist(axis, fixed)-pin_radius))
    smallest = min(min(pair['board_gap'], pair['bore_gap']) for pair in pairs)
    return dict(state='STRICT_PLANAR_CLEARANCE' if smallest > minimum_gap else 'POSE_FAILS_CLEARANCE',
                minimum_radial_gap=smallest, pairs=pairs)
