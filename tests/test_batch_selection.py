from pathlib import Path
import copy
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import batch_dxf_lines as dxf
from batch_request import prepare
from batch_selection import verify_reopened
from batch_dxf_inventory import read_inventory
from operation_catalogue import file_digest, load, refresh

try:
    import ezdxf
except ImportError:
    ezdxf = None


@unittest.skipUnless(ezdxf, "requires local ezdxf")
class SelectionTests(unittest.TestCase):
    def test_execute_saved_group(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            model = root / "group.dxf"
            doc = ezdxf.new(units=4)
            lines = [doc.modelspace().add_line((x, 0), (x, 10)) for x in [0, 1, 2]]
            block = doc.blocks.new("unused")
            block.add_line((0, 0), (2, 0))
            scaled = doc.modelspace().add_blockref("unused", (0, 0), dxfattribs={"xscale": 2})
            doc.modelspace().add_blockref("unused", (0, 0), dxfattribs={"column_count": 3, "column_spacing": 5})
            doc.groups.new("outer-lines").set_data([lines[2], lines[0]])
            doc.saveas(model)
            req = dict(model=str(model), revision=file_digest(model), model_unit="mm",
                       action="modify", entity=dxf.INPUT, output=dxf.OUTPUT,
                       selection=dict(scope=[], named="outer-lines", operation_reference=dxf.REFERENCE),
                       value=dict(value=13, unit="mm"))
            paths = [[line.dxf.handle] for line in (lines[2], lines[0])]
            for selector in ({"named": "outer-lines"}, {"paths": paths}):
                with self.subTest(selector=selector):
                    selection = dict(selector, scope=[], measurement=None, operation_reference=dxf.REFERENCE)
                    preview = prepare(dict(req, selection=selection), {"operations": []})
                    self.assertEqual(verify_reopened(preview, read_inventory(str(model), "mm")), paths)
            fake = read_inventory(str(model), "mm")
            fake["named"]["outer-lines"] = [[lines[1].dxf.handle]]
            with self.assertRaisesRegex(ValueError, "saved drawing"):
                prepare(dict(req, inventory=fake), {"operations": []})
            wrong = dict(scope=[], paths=[[scaled.dxf.handle]], operation_reference=dxf.REFERENCE)
            with self.assertRaisesRegex(ValueError, "Unsupported target"):
                prepare(dict(req, selection=wrong), {"operations": []})
            catalogue = root / "catalogue"
            method = dict(name=dxf.METHOD, input=dxf.INPUT, output=dxf.OUTPUT, action="modify", probe="guided")
            resources = [dict(id="test", backend=dxf.backend(), kind="guided", location=dxf.__file__, methods=[method])]
            refresh(catalogue, resources)
            sample = dxf.apply(prepare(req, load(catalogue)), root / "sample", resource="test", sample=True)
            method["readback_file"] = str(sample)
            refresh(catalogue, resources)
            dxf.apply(prepare(req, load(catalogue)), root / "job", resource="test", catalogue_path=catalogue)
            saved = ezdxf.readfile(root / "job/result.dxf")
            self.assertEqual([dxf.measured(dxf.line(saved, e.dxf.handle))[2] for e in lines], [13, 10, 13])

    def test_rotated_and_reopened(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "rack.dxf"
            doc = ezdxf.new(units=4)
            block = doc.blocks.new("carrier")
            edge = block.add_line((0, 0), (0, -10))
            hole = block.add_circle((5, -2), 2)
            outer = doc.blocks.new("rack")
            child = outer.add_blockref("carrier", (2, 0))
            first = doc.modelspace().add_blockref("rack", (0, 0))
            rotated = doc.modelspace().add_blockref("rack", (25, 8), dxfattribs={"rotation": 90})
            doc.saveas(path)
            scope = [rotated.dxf.handle, child.dxf.handle]
            target = scope + [hole.dxf.handle]
            rule = dict(reference_path=scope + [edge.dxf.handle], reference_kind="edge",
                        reference_anchor="start", direction="left", side="positive",
                        target_anchor="centre", measure_to="anchor")
            spec = dict(scope=scope, measurement=rule, condition=dict(kind="CIRCLE", range=[4, 6]),
                        operation_reference="circle centre")
            req = dict(model=str(path), revision=file_digest(path), model_unit="mm",
                       action="modify", entity="circle radius", output="radius",
                       selection=spec, value=dict(value=4, unit="mm"))
            preview = prepare(req, {"operations": []})
            row, = preview.read()["rows"]
            self.assertEqual(row["target"], "/".join(target))
            actual = row["selection"]["measurement"]
            for value, expected in zip(actual["target_point"], (27, 15, 0)):
                self.assertAlmostEqual(value, expected)
            self.assertAlmostEqual(actual["distance"], 5)
            rule["measure_to"] = "wall"
            with self.assertRaisesRegex(ValueError, "no elements"):
                prepare(req, {"operations": []})
            spec["condition"]["range"] = [2.9, 3.1]
            row, = prepare(req, {"operations": []}).read()["rows"]
            self.assertAlmostEqual(row["selection"]["measurement"]["distance"], 3)
            measurement = row["selection"]["measurement"]
            for field, expected in (("reference_point", (27, 10, 0)), ("target_point", (27, 13, 0)),
                                    ("target_anchor_point", (27, 15, 0)), ("reference_anchor_point", (25, 10, 0))):
                for actual, coordinate in zip(measurement[field], expected):
                    self.assertAlmostEqual(actual, coordinate)
            snapshot = read_inventory(str(path), "mm")
            supplied = copy.deepcopy(snapshot)
            supplied["definitions"]["carrier"].pop()
            with self.assertRaisesRegex(ValueError, "saved drawing"):
                prepare(dict(req, inventory=supplied), {"operations": []})
            self.assertEqual(verify_reopened(preview, snapshot), [target])
            root = snapshot["definitions"][snapshot["root"]]
            root[1]["id"], root[0]["id"] = root[0]["id"], root[1]["id"]
            self.assertEqual(verify_reopened(preview, snapshot), [[first.dxf.handle, *target[1:]]])
            root[1]["id"] = "RENUMBERED"
            self.assertEqual(verify_reopened(preview, snapshot), [["RENUMBERED", *target[1:]]])
            root.append(dict(root[1], id="OTHER"))
            with self.assertRaisesRegex(ValueError, "ambiguous"):
                verify_reopened(preview, snapshot)
            snapshot = read_inventory(str(path), "mm")
            # A native backend can expose a stable document revision across handle reassignment.
            req["model"] = snapshot["model"] = "native-rack"
            req["inventory"] = snapshot
            condition_preview = prepare(req, {"operations": []})
            extra = copy.deepcopy(snapshot["definitions"]["carrier"][-1])
            extra.update(id="new-feature", name="another hole")
            snapshot["definitions"]["carrier"].append(extra)
            with self.assertRaisesRegex(ValueError, "membership"):
                verify_reopened(condition_preview, snapshot)
            snapshot["definitions"]["carrier"].pop()
            del spec["condition"]
            snapshot["named"]["second carrier hole"] = [target]
            spec["named"] = "second carrier hole"
            self.assertEqual(prepare(req, {"operations": []}).read()["rows"][0]["target"], "/".join(target))
            group_preview = prepare(req, {"operations": []})
            snapshot["named"]["second carrier hole"] = [scope + [edge.dxf.handle]]
            with self.assertRaises((ValueError, KeyError)):
                verify_reopened(group_preview, snapshot)
            del spec["named"]
            spec["paths"] = [target]
            rule["side"] = "negative"
            with self.assertRaisesRegex(ValueError, "opposite"):
                prepare(req, {"operations": []})
            rule["side"] = "positive"
            spec["paths"] = [target, target]
            with self.assertRaisesRegex(ValueError, "Repeated"):
                prepare(req, {"operations": []})
            spec["paths"] = [[first.dxf.handle, *target[1:]]]
            with self.assertRaisesRegex(ValueError, "outside"):
                prepare(req, {"operations": []})
