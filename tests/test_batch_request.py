from dataclasses import FrozenInstanceError
import copy
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from batch_request import execution_rows, prepare
import batch_dxf_lines as dxf
import build_skill_packages as packages
from operation_catalogue import file_digest, load, record_result, refresh

try:
    import ezdxf
except ImportError:
    ezdxf = None


def request(model="frame", revision=2):
    return dict(model=str(model), revision=revision, model_unit="mm", action="modify",
                entity=dxf.INPUT, output=dxf.OUTPUT, targets=[
                    dict(id=key, reference="fixed LINE start", current=dict(value=10, unit="mm"))
                    for key in ("A", "B")],
                values=dict(A=dict(value=15, unit="cm"), B=dict(value=0.18, unit="m")))


class BatchRequestTests(unittest.TestCase):
    def test_reject_invalid_values_and_revisions(self):
        for value in ({}, [], False, "unparseable", {"value": 1, "unit": "rad"},
                      {"value": 10 ** 400, "unit": "m"}, {"value": 1}, {"unit": 1}):
            with self.subTest(value=value):
                req = request()
                req["values"]["A"] = value
                with self.assertRaises(ValueError):
                    prepare(req, {"operations": []})
        for revision in (-1, True, {}, ""):
            with self.assertRaises(ValueError):
                prepare(request(revision=revision), {"operations": []})

    def test_group_value_and_copied_preview(self):
        req = request()
        del req["values"]
        req["value"] = {"value": 0.2, "unit": "m"}
        preview = prepare(req, {"operations": []})
        preview.read()["rows"][0]["requested"]["value"] = 7
        with self.assertRaises(FrozenInstanceError):
            preview.document = "replaced"
        self.assertEqual([r["requested"]["value"] for r in preview.read()["rows"]], [200, 200])

    def test_malformed_evidence_only_disables_its_method(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "bad.json").write_text("[]")
            method = dict(name=dxf.METHOD, input=dxf.INPUT, output=dxf.OUTPUT,
                          action="modify", probe="guided", readback_file="bad.json")
            other = dict(name="guide", input="part", output="guide", probe="guided")
            resources = [dict(id="fixture", backend="fixture/1", kind="guided", location=__file__,
                              methods=[method, other])]
            ops = refresh(root / "catalogue", resources)["operations"]
            self.assertFalse(ops[0]["usable"])
            self.assertTrue(ops[1]["usable"])
            self.assertEqual(method["readback_file"], str(root / "bad.json"))
            del method["readback_file"]
            self.assertFalse(refresh(root / "catalogue", resources)["operations"][0]["usable"])

    def test_package_closure_for_catalogue(self):
        for skill in packages.SKILLS:
            self.assertTrue({"scripts/operation_catalogue.py", "scripts/batch_request.py",
                             "scripts/batch_dxf_lines.py"}.issubset(packages.inputs(skill)), skill)

    @unittest.skipUnless(ezdxf, "requires local ezdxf")
    def test_real_writer_and_readback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            model = root / "two-bars.dxf"
            doc = ezdxf.new("R2010", units=4)
            space = doc.modelspace()
            entities = [space.add_line((x, 2, 3), (x, 12, 3)) for x in (0, 42, 98)]
            doc.saveas(model)
            req = request(model, file_digest(model))
            values = req.pop("values")
            req["values"] = {}
            for item, entity in zip(req["targets"], entities):
                key = item["id"]
                item["id"] = entity.dxf.handle
                req["values"][item["id"]] = values[key]
            path = root / "catalogue"
            method = dict(name=dxf.METHOD, input=dxf.INPUT, output=dxf.OUTPUT, action="modify", probe="guided")
            resources = [dict(id="local", backend=dxf.backend(), kind="guided", location=dxf.__file__, methods=[method])]
            refresh(path, resources)
            initial = prepare(req, load(path))
            with self.assertRaisesRegex(ValueError, "verified readback"):
                dxf.apply(initial, root / "unused", resource="local", catalogue_path=path)
            receipt = dxf.apply(initial, root / "sample", resource="local", sample=True)
            method["readback_file"] = receipt.relative_to(root).as_posix()
            refresh(path, resources)
            preview = prepare(req, load(path))
            evidence = dxf.apply(preview, root / "job", resource="local", catalogue_path=path)
            from batch_delivery import deliver
            reviewed = root / "reviewed.json"
            reviewed.write_text(preview.document)
            self.assertFalse(deliver(reviewed, path, root / "job")["remaining"])
            for field, replacement in (("reference", "fixed LINE end"), ("current", {"value": 999, "unit": "mm"})):
                revised = preview.read()
                revised["rows"][0][field] = replacement
                reviewed.write_text(json.dumps(revised))
                self.assertIn("blocker", deliver(reviewed, path, root / "job"))
            reviewed.write_text(preview.document)
            reader = root / "job/readback.json"
            original = reader.read_bytes()
            reader.write_text("{}")
            self.assertIn("blocker", deliver(reviewed, path, root / "job"))
            reader.write_bytes(original)
            op = json.loads((evidence.parent / "operation.json").read_text())
            self.assertEqual([item["length"] for item in op["expected"].values()],
                             [item["requested"]["value"] for item in preview.read()["rows"]])
            saved = ezdxf.readfile(root / "job/result.dxf")
            self.assertEqual([dxf.measured(dxf.line(saved, e.dxf.handle))[2] for e in entities], [150, 180, 10])
            self.assertEqual(req["revision"], file_digest(model))
            wrong_ref = copy.deepcopy(req)
            wrong_ref["targets"][0]["reference"] = "fixed LINE end"
            with self.assertRaisesRegex(ValueError, "requires reference"):
                dxf.apply(prepare(wrong_ref, load(path)), root / "wrong-anchor", resource="local", catalogue_path=path)
            self.assertFalse((root / "wrong-anchor").exists())
            unchanged = copy.deepcopy(req)
            unchanged["values"] = {item["id"]: item["current"] for item in unchanged["targets"]}
            unchanged_preview = prepare(unchanged, load(path))
            with self.assertRaisesRegex(ValueError, "demonstrate"):
                dxf.apply(unchanged_preview, root / "no-change", resource="local", sample=True)
            self.assertFalse((root / "no-change").exists())
            self.assertFalse(list(root.glob(".batch-lines-*")))
            dxf.apply(unchanged_preview, root / "no-change", resource="local", catalogue_path=path)
            reserved = root / "reserved"
            reserved.mkdir()
            with self.assertRaises(FileExistsError):
                dxf.apply(preview, reserved, resource="local", catalogue_path=path)
            self.assertEqual(list(reserved.iterdir()), [])
            modified = root / "unselected-line-change.dxf"
            dxf.line(saved, entities[-1].dxf.handle).dxf.end = (4, 10, 2)
            saved.saveas(modified)
            with self.assertRaisesRegex(ValueError, "Unselected LINE"):
                dxf.verify_sample(model, modified, op, op["expected"])
            # Re-label matching raw receipts as an unsupported backend with real artifacts.
            unsupported = root / "unsupported"
            unsupported.mkdir()
            manifest = {"operation": "operation.json", "readback": "readback.json"}
            for kind in ("operation", "readback"):
                record = json.loads((evidence.parent / manifest[kind]).read_text())
                record.update(backend="other/1", input="sketch dimension", result=str(evidence.parent / "result.dxf"))
                record_path = unsupported / manifest[kind]
                record_path.write_text(json.dumps(record))
                manifest[kind + "_sha256"] = file_digest(record_path)
            (unsupported / "evidence.json").write_text(json.dumps(manifest))
            alternative = copy.deepcopy(resources)
            alternative[0]["backend"] = "other/1"
            alternative[0]["methods"][0].update(input="sketch dimension", readback_file="unsupported/evidence.json")
            failed = refresh(root / "alternate-catalogue", alternative)["operations"][0]
            self.assertFalse(failed["usable"])
            self.assertIn("No backend artifact verification", failed["reason"])
            record_result(path, SimpleNamespace(resource="local", method=dxf.METHOD, reason="route failed"))
            with self.assertRaisesRegex(ValueError, "verified readback"):
                dxf.apply(preview, root / "disabled", resource="local", catalogue_path=path)
            refresh(path, resources)
            with self.assertRaisesRegex(ValueError, "revision"):
                execution_rows(preview, "local", dxf.METHOD, catalogue_path=path, read_revision=lambda _: "new")
            for key, value in (("entity", "sketch dimension"), ("output", "angle"), ("action", "replace")):
                self.assertFalse(prepare({**req, key: value}, load(path)).read()["routes"])
