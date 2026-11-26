"""Check a repeated nested group's layer isolation and inherited appearance."""
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

import ezdxf

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/cad-model-navigation/scripts"
sys.path.insert(0, str(SCRIPTS))
from dxf_styles import inventory


class NestedLayerIsolation(unittest.TestCase):
    def test_parent_layer_move_preserves_explicit_colour_but_not_all_inheritance(self):
        doc = ezdxf.new()
        doc.layers.new("Support", dxfattribs={"color": 1})
        doc.layers.new("Wheel", dxfattribs={"color": 5})
        block = doc.blocks.new("WheelDefinition")
        block.add_line((0, 0), (1, 0), dxfattribs={"layer": "Wheel"})
        space = doc.modelspace()
        inserts = [space.add_blockref(block.name, (offset, 0), dxfattribs={"layer": "Support"})
                   for offset in (0, 5)]
        sibling = space.add_line((0, 2), (1, 2), dxfattribs={"layer": "Support"})

        with TemporaryDirectory() as tmp:
            drawing = Path(tmp) / "fixture.dxf"

            def leaves():
                doc.saveas(drawing)
                return {tuple(row["path"]): (row["display_colour"], row["visible"])
                        for row in inventory(drawing)["entities"] if row["type"] == "LINE"}

            original = leaves()
            target = {path for path in original if len(path) == 3}
            self.assertEqual(len(target), 2)
            sibling_path = ("Model", sibling.dxf.handle)
            self.assertTrue(original[sibling_path][1])
            for insert in inserts:
                insert.dxf.layer = "0"
            self.assertEqual(original, leaves())
            doc.layers.get("Support").off()
            self.assertEqual({p for p, (_, visible) in leaves().items() if visible}, target)
            doc.layers.get("Support").on()
            self.assertEqual(original, leaves())

            inherited = block.add_line((0, 1), (1, 1), dxfattribs={"layer": "0", "color": 0})
            neutral_colours = leaves()
            for insert in inserts:
                insert.dxf.layer = "Support"
            support_colours = leaves()
            for insert in inserts:
                path = ("Model", insert.dxf.handle, inherited.dxf.handle)
                self.assertNotEqual(neutral_colours[path][0], support_colours[path][0])


    def test_shared_layer_rgb_change_reaches_unmapped_visible_and_hidden_leaves(self):
        doc = ezdxf.new()
        shared = doc.layers.new("Shared", dxfattribs={"color": 1})
        shared.rgb = (190, 110, 30)
        approved = doc.layers.new("Approved", dxfattribs={"color": 5})
        approved.rgb = (90, 120, 150)
        hidden = doc.layers.new("Reference", dxfattribs={"color": 7})
        hidden.off()
        model = doc.modelspace()
        target = model.add_line((0, 0), (1, 0), dxfattribs={"layer": "Shared"})
        sibling = model.add_line((0, 1), (1, 1), dxfattribs={"layer": "Shared"})
        block = doc.blocks.new("ReferenceDefinition")
        reference = block.add_line((0, 2), (1, 2), dxfattribs={"layer": "Reference", "color": 0})
        insert = model.add_blockref(block.name, (0, 0), dxfattribs={"layer": "Shared"})

        target_path = ("Model", target.dxf.handle)
        sibling_path = ("Model", sibling.dxf.handle)
        hidden_path = ("Model", insert.dxf.handle, reference.dxf.handle)

        with TemporaryDirectory() as tmp:
            drawing = Path(tmp) / "fixture.dxf"

            def leaves():
                doc.saveas(drawing)
                return {tuple(row["path"]): (row["display_colour"], row["visible"])
                        for row in inventory(drawing)["entities"] if row["type"] == "LINE"}

            original = leaves()
            self.assertEqual({p for p, (_, visible) in original.items() if visible},
                             {target_path, sibling_path})

            shared.rgb = approved.rgb
            broad_edit = leaves()
            self.assertEqual({p for p in original if broad_edit[p][0] != original[p][0]},
                             {target_path, sibling_path, hidden_path})
            self.assertFalse(broad_edit[hidden_path][1])

            shared.rgb = (190, 110, 30)
            target.dxf.layer = "Approved"
            scoped_edit = leaves()
            self.assertEqual({p for p in original if scoped_edit[p] != original[p]}, {target_path})
            self.assertEqual(scoped_edit[target_path], broad_edit[target_path])


if __name__ == "__main__":
    unittest.main()
