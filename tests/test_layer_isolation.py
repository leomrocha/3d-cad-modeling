"""Exercise exact flag preservation across adjacent nested isolation groups."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from layer_isolation import plan_isolation_transition


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


if __name__ == "__main__":
    unittest.main()
