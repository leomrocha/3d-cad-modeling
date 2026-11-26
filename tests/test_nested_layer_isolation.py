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


if __name__ == "__main__":
    unittest.main()
