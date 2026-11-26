"""Exercise exact flag preservation across adjacent nested isolation groups."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from layer_isolation import plan_exact_isolation_masks, plan_isolation_transition, verify_ancestor_appearance


class LayerIsolation(unittest.TestCase):
    def setUp(self):
        self.original = {
            name: dict(off=name == "hidden", frozen=name == "frozen", locked=name == "parent")
            for name in ("parent", "edge", "skin", "stock", "hidden", "frozen")
        }

    def test_differential_transition_and_restore(self):
        flags = deepcopy(self.original)
        dependencies = {
            "insert/edge": ("parent", "edge"),
            "insert/skin": ("parent", "skin"),
            "stationary": ("stock",),
            "hidden-insert/edge": ("hidden", "edge"),
            "frozen-insert/skin": ("frozen", "skin"),
        }
        steps = [
            (set(), {"skin", "stock"}, {"insert/edge"}, 2),
            ({"skin", "stock"}, {"edge", "stock"}, {"insert/skin"}, 2),
            ({"edge", "stock"}, set(), {"insert/edge", "insert/skin", "stationary"}, 2),
        ]
        for previous, target, wanted, count in steps:
            edits = plan_isolation_transition(self.original, flags, previous, target)
            self.assertEqual(len(edits), count)
            if previous and target:
                self.assertEqual(edits, [("edge", False, True), ("skin", True, False)])
            for name, old, new in edits:
                self.assertIs(flags[name]["off"], old)
                flags[name]["off"] = new
            visible = {
                path for path, layers in dependencies.items()
                if all(not (flags[layer]["off"] or flags[layer]["frozen"]) for layer in layers)
            }
            self.assertEqual(visible, wanted)
        self.assertEqual(flags, self.original)

    def test_rejects_unverified_or_changed_flag_table(self):
        for key, field, value in (("stock", "off", False), ("frozen", "frozen", False),
                                  ("parent", "locked", False)):
            with self.subTest(field=field):
                flags = deepcopy(self.original)
                flags["stock"]["off"] = True
                flags[key][field] = value
                with self.assertRaisesRegex(ValueError, "differs from the verified"):
                    plan_isolation_transition(self.original, flags, {"stock"}, {"skin"})
        flags = deepcopy(self.original)
        del flags["hidden"]
        with self.assertRaisesRegex(ValueError, "differs from the verified"):
            plan_isolation_transition(self.original, flags, set(), set())

    def test_rejects_already_off_frozen_or_unknown_targets(self):
        for layer in ("hidden", "frozen", "absent"):
            with self.subTest(layer=layer):
                with self.assertRaisesRegex(ValueError, "not originally on and thawed"):
                    plan_isolation_transition(self.original, self.original, set(), {layer})


class AncestorIsolation(unittest.TestCase):
    def test_single_gate_passes_whole_assembly_and_named_roles(self):
        flags = {layer: dict(off=False, frozen=False) for layer in ("0", "gate", "edge", "cover")}
        dependencies = {("tool", "edge"): {"gate", "edge"}, ("tool", "cover"): {"gate", "cover"},
                        ("host", "cover"): {"0", "cover"}}
        groups = {"assembly": {("tool", "edge"), ("tool", "cover")}, "guarding": {("tool", "cover")}}
        self.assertEqual(plan_exact_isolation_masks(flags, dependencies, groups),
                         {"assembly": {"0"}, "guarding": {"0", "edge"}})

    def test_whole_group_can_pass_while_prior_role_needs_second_gate(self):
        flags = {layer: dict(off=False, frozen=False) for layer in ("gate", "shared", "scoped", "wheel")}
        tyre, screw = ("tool", "wheel", "tyre"), ("tool", "wheel", "screw")
        dependencies = {tyre: {"gate", "wheel"}, screw: {"gate", "wheel"}}
        self.assertEqual(plan_exact_isolation_masks(flags, dependencies, {"whole": {tyre, screw}}), {"whole": set()})
        groups = {"whole": {tyre, screw}, "tyre": {tyre}}
        with self.assertRaisesRegex(ValueError, "tyre.*extra.*screw"):
            plan_exact_isolation_masks(flags, dependencies, groups)
        dependencies[screw] = {"gate", "scoped"}
        dependencies[("host", "screw")] = {"shared"}
        self.assertEqual(plan_exact_isolation_masks(flags, dependencies, groups),
                         {"whole": {"shared"}, "tyre": {"scoped", "shared"}})

    def test_hidden_dependency_blocks_a_requested_role(self):
        flags = {"hidden": dict(off=True, frozen=False), "on": dict(off=False, frozen=False)}
        with self.assertRaisesRegex(ValueError, "guarding.*missing.*guard"):
            plan_exact_isolation_masks(flags, {("tool", "guard"): {"hidden", "on"}},
                                       {"guarding": {("tool", "guard")}})

    def test_shared_insert_use_outside_scope_is_rejected(self):
        tool, other = ("tool", "insert"), ("other", "insert")
        views = {tool: ((12, 20, 30), "0", ()), other: ((12, 20, 30), "0", ())}
        with self.assertRaisesRegex(ValueError, "outside scope.*other"):
            verify_ancestor_appearance(views, views, {tool}, {"insert"}, {})

    def test_raw_zero_protected_descendant_preserves_effective_layer_and_colour(self):
        root, ref = ("tool",), ("tool", "protected")
        original = {root: ((12, 20, 30), "0", ()), ref: ((12, 20, 30), "0", ("hidden",))}
        moved = {root: ((12, 20, 30), "gate", ()), ref: ((12, 20, 30), "gate", ("hidden",))}
        with self.assertRaisesRegex(ValueError, "effective appearance.*protected"):
            verify_ancestor_appearance(original, moved, {root, ref}, {"tool"}, {root: "gate"})
        moved[ref] = original[ref]
        verify_ancestor_appearance(original, moved, {root, ref}, {"tool"}, {root: "gate"})
        moved[ref] = ((30, 20, 12), "0", ("hidden",))
        with self.assertRaisesRegex(ValueError, "effective appearance.*protected"):
            verify_ancestor_appearance(original, moved, {root, ref}, {"tool"}, {root: "gate"})


if __name__ == "__main__":
    unittest.main()
