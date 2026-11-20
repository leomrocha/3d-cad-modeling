import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import batch_dxf_placement as placement
from operation_catalogue import file_digest, load, refresh
from step_placements import near

try:
    import ezdxf
except ImportError:
    ezdxf = None


@unittest.skipUnless(ezdxf, "requires installed ezdxf")
class ExistingPlacementTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.directory = Path(tmp.name)
        self.source = self.directory / "bars.dxf"
        doc = ezdxf.new(units=4)
        definition = doc.blocks.new("Bar", base_point=(2, 3, 0))
        definition.add_line((2, 3, 0), (12, 3, 0))
        owner = doc.blocks.new("Frame", base_point=(5, 4, 0))
        slots = [owner.add_blockref("Bar", (10*n, 4)) for n in range(3)]
        self.parent = doc.modelspace().add_blockref("Frame", (25, 7), dxfattribs={"rotation": 35}).dxf.handle
        self.paths = [self.parent + "/" + s.dxf.handle for s in slots]
        doc.saveas(self.source)
        self.request = dict(model=str(self.source), model_unit="mm", revision=file_digest(self.source),
                            selection=dict(scope=[self.parent], paths=[p.split("/") for p in self.paths[:2]]),
                            assignments=dict(zip(self.paths[:2], ["P2", "P1"])))
        self.positions = dict(unit="mm", reference="frame datum", frame={"x": [1,0,0], "y": [0,1,0]},
                              positions=[dict(id="P1", xyz=[20,0,0]), dict(id="P2", xyz=[40,0,0])])
        self.catalogue = self.directory / "operations.json"
        self.method = dict(name=placement.METHOD, input=placement.INPUT, output=placement.OUTPUT,
                           action="place", probe="guided")
        self.resources = [dict(id="local-dxf", location=placement.__file__, backend=placement.backend(),
                               kind="guided", methods=[self.method])]

    def prepare(self):
        refresh(self.catalogue, self.resources)
        return placement.review(self.request, self.positions, load(self.catalogue))

    def test_delivery_resumes_owning_method_before_an_alternative(self):
        from batch_delivery import deliver
        sample = self.directory / "sample"
        placement.start(self.prepare(), sample, "local-dxf", sample=True)
        placement.resume(sample)
        self.method["readback_file"] = "sample/evidence.json"
        preview = self.prepare()
        job = self.directory / "job"
        placement.start(preview, job, "local-dxf", self.catalogue)
        data = load(self.catalogue)
        data["resources"].insert(0, dict(data["resources"][0], id="other"))
        data["operations"].insert(0, dict(data["operations"][0], resource="other"))
        self.catalogue.write_text(json.dumps(data))
        request = self.directory / "review.json"
        request.write_text(preview.document)
        result = deliver(request, self.catalogue, job)
        self.assertEqual(result["remaining"], [])
        self.assertEqual([row["resource"] for row in result["attempts"]], ["local-dxf"])

    def test_thick_line_rejected_for_projected_edges(self):
        from batch_delivery import measure_row
        doc = ezdxf.readfile(self.source)
        edge = doc.modelspace().add_line((0,0),(100,0))
        list(doc.blocks["Bar"])[0].dxf.thickness = 3
        spec = self.prepare().read()
        spec["row_check"] = {"line": edge.dxf.handle}
        with self.assertRaisesRegex(ValueError, "Row edge offsets"):
            measure_row(spec, doc, planned=True)

    def test_nested_row_resume_without_repeated_move(self):
        sample = self.directory / "sample"
        placement.start(self.prepare(), sample, "local-dxf", sample=True)
        placement.resume(sample)
        self.method["readback_file"] = "sample/evidence.json"
        job = self.directory / "execute"
        placement.start(self.prepare(), job, "local-dxf", self.catalogue)

        def interrupt(target):
            raise InterruptedError(target)
        with self.assertRaises(InterruptedError):
            placement.resume(job, after_save=interrupt)
        calls = []
        results = placement.resume(job, after_save=calls.append)
        self.assertEqual(calls, [self.paths[1]])
        self.assertEqual(len({v["request_id"] for v in results.values()}), 2)
        before = file_digest(job / "result.dxf")
        placement.resume(job, after_save=calls.append)
        self.assertEqual(file_digest(job / "result.dxf"), before)
        self.assertEqual(calls, [self.paths[1]])
        readback = json.loads((job / "readback.json").read_text())["observed"]
        self.assertAlmostEqual(readback[self.paths[0]]["distance_from_previous_base"], 20)
        self.assertEqual(len(readback), 2)
        old = placement.drawing(self.source, "mm")
        new = placement.drawing(job / "result.dxf", "mm")
        self.assertTrue(near(placement.resolve_frame(old, self.paths[2])[2],
                             placement.resolve_frame(new, self.paths[2])[2]))

    def test_ordered_assignment_by_measured_block_base(self):
        doc = placement.drawing(self.source, "mm")
        datum = doc.modelspace().add_line((0,0), (100,0)).dxf.handle
        doc.saveas(self.source)
        self.request["revision"] = file_digest(self.source)
        self.request["selection"]["measurement"] = dict(reference_path=[datum], reference_kind="edge",
            reference_anchor="start", direction="along", side="positive", target_anchor="block base",
            measure_to="anchor")
        del self.request["assignments"]
        self.request["order_by"] = "decreasing measured distance"
        rows = self.prepare().read()["rows"]
        self.assertEqual([r["position_id"] for r in rows], ["P2", "P1"])

    def test_conflicting_position_reference(self):
        self.positions["positions"][0]["reference"] = "other datum"
        with self.assertRaisesRegex(ValueError, "different reference"):
            self.prepare()

    def test_resume_failed_target_and_continue_independent_move(self):
        job = self.directory / "failure"
        placement.start(self.prepare(), job, "local-dxf", sample=True)
        original = placement.write_one
        def fail_first(directory, doc, target, *args):
            if target == self.paths[0]:
                raise OSError("save failed at first occurrence")
            return original(directory, doc, target, *args)
        with patch.object(placement, "write_one", side_effect=fail_first):
            results = placement.resume(job)
        self.assertEqual(results[self.paths[0]]["effect"], "not_applied")
        self.assertEqual(results[self.paths[0]]["status"], "failed")
        self.assertIn("save failed", results[self.paths[0]]["detail"])
        self.assertEqual(results[self.paths[1]]["status"], "completed")
        self.assertFalse((job / "evidence.json").exists())
        calls = []
        placement.resume(job, after_save=calls.append)
        self.assertEqual(calls, self.paths[:1])

    def test_recheck_layer_and_withdraw_stale_completion(self):
        job = self.directory / "layer"
        placement.start(self.prepare(), job, "local-dxf", sample=True)
        placement.resume(job)
        doc = placement.drawing(job / "result.dxf", "mm")
        doc.layers.get("0").lock()
        doc.saveas(job / "result.dxf")
        results = placement.resume(job)
        self.assertTrue(all(v["status"] == "failed" for v in results.values()))
        self.assertTrue(all("locked" in v["detail"] for v in results.values()))
        self.assertFalse((job / "evidence.json").exists())
        self.assertFalse((job / "readback.json").exists())

    def test_reopened_units_and_version(self):
        for field in ("units", "dxfversion"):
            with self.subTest(field=field):
                job = self.directory / field
                placement.start(self.prepare(), job, "local-dxf", sample=True)
                placement.resume(job)
                doc = placement.drawing(job / "result.dxf", "mm")
                setattr(doc, field, 0 if field == "units" else "AC1018")
                doc.saveas(job / "result.dxf")
                with self.assertRaisesRegex(ValueError, "version or declared units"):
                    placement.resume(job)
                self.assertFalse((job / "evidence.json").exists())
                self.assertTrue(all(v["status"] == "failed"
                                    for v in json.loads((job / "results.json").read_text()).values()))

    def test_generic_insert_current_and_missing_dxf_base(self):
        snapshot = placement.read_inventory(str(self.source), "mm")
        child = next(c for c in snapshot["definitions"]["Frame"] if c["id"] == self.paths[0].split("/")[-1])
        child["current"] = {"native_state": "existing"}
        del child["anchors"]["block base"]
        req = dict(self.request, action="place", entity="native INSERT",
                   selection=dict(self.request["selection"], operation_reference="native anchor"))
        rows = placement.resolve_selection(req, snapshot)
        self.assertEqual(rows[0]["current"], {"native_state": "existing"})
        with self.assertRaisesRegex(ValueError, "measured block base"):
            placement.resolve_selection(dict(req, entity="DXF INSERT"), snapshot)

    def test_shared_parent_rejected_before_job_creation(self):
        doc = placement.drawing(self.source, "mm")
        doc.modelspace().add_blockref("Frame", (100, 100))
        doc.saveas(self.source)
        self.request["revision"] = file_digest(self.source)
        job = self.directory / "shared"
        with self.assertRaisesRegex(ValueError, "other occurrences"):
            placement.start(self.prepare(), job, "local-dxf", sample=True)
        self.assertFalse(job.exists())
