"""Synthetic validation for read-only assembly root unit planning."""
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from assembly_units import plan_root_unit_change
from step_placements import native_matrix


def unit(label, code, mm_per_unit):
    return {"label": label, "code": code,
            "millimetres_per_drawing_unit": mm_per_unit}


def root(handle="A", **overrides):
    props = {"column_count": 1, "row_count": 1,
             "normal": {"x": 0.0, "y": 0.0, "z": 1.0},
             "rotation": math.pi / 2,
             "insert_point": {"x": 3.0, "y": -4.0, "z": 2.0},
             "x_scale": 0.001, "y_scale": 0.001, "z_scale": 0.001}
    props.update(overrides)
    return {"type": "Insert", "handle": handle, "properties": props}


class AssemblyUnitPlanTests(unittest.TestCase):
    def test_scales_root_translation_and_axes_but_keeps_orientation(self):
        original = root()
        plan = plan_root_unit_change(
            [original], source_unit=unit("metre", 6, 1000),
            destination_unit=unit("millimetre", 4, 1))
        change = plan["changes"][0]
        self.assertEqual(plan["scale_factor"], 1000)
        self.assertEqual(change["after"]["insert_point"],
                         {"x": 3000.0, "y": -4000.0, "z": 2000.0})
        self.assertEqual([change["after"][k] for k in
                          ("x_scale", "y_scale", "z_scale")], [1.0, 1.0, 1.0])
        self.assertEqual(change["after"]["normal"], original["properties"]["normal"])
        self.assertEqual(change["after"]["rotation"], original["properties"]["rotation"])
        actual = native_matrix(change["after"])
        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(actual[i][j], change["matrix_expected"][i][j])
        self.assertEqual(original["properties"]["insert_point"],
                         {"x": 3.0, "y": -4.0, "z": 2.0})

    def test_zero_translation_and_scale_only_root(self):
        props = root(insert_point={"x": 0.0, "y": 0.0, "z": 0.0},
                     rotation=0.0, x_scale=0.0254, y_scale=0.0254, z_scale=0.0254)
        plan = plan_root_unit_change(
            [props], source_unit=unit("source", 1, 1),
            destination_unit=unit("target", 2, 1000))
        change = plan["changes"][0]
        self.assertEqual(change["after"]["insert_point"],
                         {"x": 0.0, "y": 0.0, "z": 0.0})
        self.assertEqual([change["after"][k] for k in
                          ("x_scale", "y_scale", "z_scale")],
                         [0.0000254] * 3)

    def test_rejects_arrays_nonuniform_and_invalid_scales(self):
        bad = [root(column_count=2), root(z_scale=0.002), root(x_scale=-0.001),
               root(y_scale=0), root(z_scale=float("nan"))]
        for item in bad:
            with self.subTest(properties=item["properties"]):
                with self.assertRaises(ValueError):
                    plan_root_unit_change(
                        [item], source_unit=unit("a", 1, 1),
                        destination_unit=unit("b", 2, 2))

    def test_rejects_invalid_units_roots_and_duplicate_handles(self):
        with self.assertRaisesRegex(ValueError, "millimetres-per-unit"):
            plan_root_unit_change([root()], source_unit=unit("a", 1, 0),
                                  destination_unit=unit("b", 2, 1))
        with self.assertRaisesRegex(ValueError, "unit code"):
            plan_root_unit_change([root()], source_unit=unit("a", -1, 1),
                                  destination_unit=unit("b", 2, 1))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            plan_root_unit_change([root(), root()], source_unit=unit("a", 1, 1),
                                  destination_unit=unit("b", 2, 1))
        with self.assertRaisesRegex(ValueError, "string handle"):
            plan_root_unit_change([{"type": "Insert", "handle": 1,
                                    "properties": root()["properties"]}],
                                  source_unit=unit("a", 1, 1),
                                  destination_unit=unit("b", 2, 1))
        with self.assertRaisesRegex(ValueError, "supported root"):
            plan_root_unit_change([{"type": "Solid3D", "handle": "S",
                                    "properties": root()["properties"]}],
                                  source_unit=unit("a", 1, 1),
                                  destination_unit=unit("b", 2, 1))
        with self.assertRaisesRegex(ValueError, "supported root"):
            plan_root_unit_change([root("")], source_unit=unit("a", 1, 1),
                                  destination_unit=unit("b", 2, 1))

    def test_validates_all_roots_before_returning_plan(self):
        roots = [root("A"), root("B", y_scale=0.002)]
        with self.assertRaises(ValueError):
            plan_root_unit_change(roots, source_unit=unit("a", 1, 1),
                                  destination_unit=unit("b", 2, 1))

    def test_rejects_nonfinite_transform_from_nan_rotation(self):
        with self.assertRaisesRegex(ValueError, "transform must be finite"):
            plan_root_unit_change([root(rotation=float("nan"))],
                                  source_unit=unit("a", 1, 1),
                                  destination_unit=unit("b", 2, 1))


if __name__ == "__main__":
    unittest.main()
