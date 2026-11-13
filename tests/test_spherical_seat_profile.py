"""Synthetic math checks for exact spherical-seat circular profile arcs."""

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from spherical_seat_profile import spherical_seat_profile


def sample(scale=1.0):
    return spherical_seat_profile(
        sphere_radius=12.0 * scale,
        sphere_center_z=0.0,
        collar_radius=11.0 * scale,
        collar_start_z=-20.0 * scale,
        shaft_radius=6.0 * scale,
        blend_radius=1.0 * scale,
        shaft_end_z=16.0 * scale,
    )


def center_from_bulge(start, end, bulge):
    dx, dy = end[0] - start[0], end[1] - start[1]
    chord = math.hypot(dx, dy)
    offset = chord * (1.0 - bulge * bulge) / (4.0 * bulge)
    midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    return (midpoint[0] - dy / chord * offset,
            midpoint[1] + dx / chord * offset)


class SphericalSeatProfileTests(unittest.TestCase):
    def test_returns_monotonic_closed_profile_and_exact_signed_arc_centres(self):
        result = sample()
        points = result["points"]
        self.assertEqual(7, len(points))
        self.assertEqual(points[0][1], points[1][1])  # lower cap is radial
        self.assertTrue(all(a[1] < b[1] for a, b in zip(points[1:6], points[2:6])))
        self.assertEqual(points[5][1], points[6][1])  # upper cap is radial
        self.assertEqual({2, 3}, set(result["bulges"]))
        self.assertGreater(result["bulges"][2], 0)
        self.assertLess(result["bulges"][3], 0)
        for index in (2, 3):
            found = center_from_bulge(points[index], points[index + 1],
                                      result["bulges"][index])
            expected = result["arc_centers"][index]
            self.assertAlmostEqual(expected[0], found[0], places=11)
            self.assertAlmostEqual(expected[1], found[1], places=11)

    def test_sphere_and_blend_contacts_satisfy_independent_tangency_equations(self):
        p = sample()
        sphere = p["derived"]["sphere_contact"]
        blend = p["derived"]["blend_contact"]
        sphere_center = [0.0, 0.0]
        blend_center = p["derived"]["blend_center"]
        sphere_vector = (sphere[0] - sphere_center[0],
                         sphere[1] - sphere_center[1])
        blend_vector = (sphere[0] - blend_center[0],
                        sphere[1] - blend_center[1])
        self.assertAlmostEqual(12.0, math.hypot(*sphere_vector), places=11)
        self.assertAlmostEqual(1.0, math.hypot(*blend_vector), places=11)
        dot = sphere_vector[0] * blend_vector[0] + sphere_vector[1] * blend_vector[1]
        self.assertAlmostEqual(-12.0, dot, places=10)
        self.assertAlmostEqual(6.0, blend[0])
        self.assertAlmostEqual(p["derived"]["blend_center"][1], blend[1])

    def test_profile_scales_without_component_specific_values(self):
        small, normal, large = sample(1e-3), sample(), sample(1e3)
        for result, scale in ((small, 1e-3), (normal, 1.0), (large, 1e3)):
            self.assertAlmostEqual(11.0 * scale, result["points"][2][0])
            self.assertAlmostEqual(6.0 * scale, result["points"][4][0])
            self.assertGreater(result["bulges"][2], 0)
            self.assertLess(result["bulges"][3], 0)
        self.assertAlmostEqual(normal["bulges"][2], small["bulges"][2], places=13)
        self.assertAlmostEqual(normal["bulges"][3], large["bulges"][3], places=13)

    def test_rejects_invalid_radii_order_tangent_and_axial_sequence(self):
        valid = dict(sphere_radius=12.0, sphere_center_z=0.0,
                     collar_radius=11.0, collar_start_z=-20.0,
                     shaft_radius=6.0, blend_radius=1.0, shaft_end_z=16.0)
        cases = [
            {"sphere_radius": 11.0},
            {"collar_radius": 12.0},
            {"shaft_radius": 11.0},
            {"blend_radius": 0.0},
            {"shaft_radius": 10.9, "blend_radius": 5.0},
            {"collar_start_z": 5.0},
            {"shaft_end_z": 10.0},
            {"sphere_radius": True},
            {"sphere_center_z": float("nan")},
            {"sphere_radius": 10 ** 1000},
        ]
        for changes in cases:
            with self.subTest(changes=changes):
                args = valid | changes
                with self.assertRaises(ValueError):
                    spherical_seat_profile(**args)

    def test_rejects_numeric_overflow_and_underflow_collapse(self):
        with self.assertRaises(ValueError):
            spherical_seat_profile(
                sphere_radius=1e200, sphere_center_z=0,
                collar_radius=1e199, collar_start_z=-1e201,
                shaft_radius=1e198, blend_radius=1e197, shaft_end_z=1e201)
        with self.assertRaises(ValueError):
            spherical_seat_profile(
                sphere_radius=1e-200, sphere_center_z=0,
                collar_radius=1e-201, collar_start_z=-1e-199,
                shaft_radius=1e-202, blend_radius=1e-203, shaft_end_z=1e-199)


if __name__ == "__main__":
    unittest.main()
