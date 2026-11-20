"""Exercise actual DXF insertion, interruption, journal reuse and stale seats."""
import importlib.util
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import batch_insert_recovery as recovery


@unittest.skipUnless(importlib.util.find_spec("ezdxf"), "ezdxf required for real DXF round trips")
class InsertRecoveryTest(unittest.TestCase):
    def setUp(self):
        import ezdxf
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.source = root / "original.dxf"
        doc = ezdxf.new()
        doc.units = 4
        doc.blocks.new("pin", base_point=(2, 3, 1)).add_circle((2, 3, 1), 1)
        doc.modelspace().add_line((1, 1), (2, 3))
        doc.saveas(self.source)
        self.job = root / "job"
        rows = [dict(id=name, block="pin", point=[x, 0, 0], depends_on=deps)
                for x, (name, deps) in enumerate([("first", []), ("dependent", ["first"]),
                                                  ("independent", [])])]
        recovery.start(self.source, self.job, dict(targets=rows, unit="mm",
                       source_sha256=recovery.file_digest(self.source)))

    def test_lost_ack_and_repeat(self):
        with self.assertRaises(InterruptedError):
            recovery.resume(self.job, after_save=lambda _: self.interrupt())
        journal = recovery.Journal(self.job / "requests.jsonl")
        key, = journal.requests
        results = recovery.resume(self.job)
        self.assertEqual(results["first"]["request_id"], key)
        self.assertEqual(results["first"]["count"], 1)
        self.assertEqual(recovery.resume(self.job), results)
        self.assertEqual(len(recovery.Journal(self.job / "requests.jsonl").requests), 3)

    def interrupt(self):
        raise InterruptedError

    def test_same_intent_before_write_and_stale_edit(self):
        with patch.object(recovery, "insert_one", side_effect=InterruptedError):
            with self.assertRaises(InterruptedError):
                recovery.resume(self.job)
        key, = recovery.Journal(self.job / "requests.jsonl").requests
        result = recovery.resume(self.job)
        self.assertEqual(result["first"]["request_id"], key)
        import ezdxf
        model = self.job / "model.dxf"
        doc = ezdxf.readfile(model)
        doc.modelspace().delete_entity(doc.entitydb[result["first"]["handles"][0]])
        doc.saveas(model)
        after = recovery.resume(self.job)
        self.assertEqual(after["first"]["effect"], "unknown")
        self.assertEqual(after["dependent"]["status"], "completed")
        self.assertEqual(after["independent"]["status"], "completed")
        self.assertEqual(recovery.resume(self.job)["first"]["count"], 0)

    def test_conflicting_seat_allows_independent_write(self):
        import ezdxf
        model = self.job / "model.dxf"
        doc = ezdxf.readfile(model)
        doc.modelspace().add_blockref("pin", (0, 0, 0))
        doc.saveas(model)
        results = recovery.resume(self.job)
        self.assertEqual(results["first"]["effect"], "unknown")
        self.assertEqual(results["dependent"]["count"], 0)
        self.assertEqual(results["independent"]["effect"], "applied")

    def test_substituted_drawing_and_changed_independent_geometry(self):
        import ezdxf
        import shutil
        model = self.job / "model.dxf"
        owned = model.read_bytes()
        shutil.copyfile(self.source, model)
        with self.assertRaisesRegex(ValueError, "identity"):
            recovery.resume(self.job)
        model.write_bytes(owned)
        recovery.resume(self.job)
        doc = ezdxf.readfile(model)
        doc.modelspace().query("LINE").first.dxf.end = (5, 5, 5)
        doc.saveas(model)
        with self.assertRaisesRegex(ValueError, "Independent"):
            recovery.resume(self.job)
        self.assertIn("Independent", (self.job / "drawing-check.json").read_text())

    def test_rotated_extruded_array_duplicate(self):
        import ezdxf
        from ezdxf.math import OCS, Vec3
        result = recovery.resume(self.job)
        model = self.job / "model.dxf"
        doc = ezdxf.readfile(model)
        normal = (0, 1, 0)
        ocs = OCS(normal)
        base = ocs.from_wcs(Vec3(0, 0, 0)) - Vec3(3, 0, 0).rotate_deg(90)
        doc.modelspace().add_blockref("pin", base, dxfattribs={
            "extrusion": normal, "column_count": 2, "column_spacing": 3, "rotation": 90})
        doc.saveas(model)
        rows = recovery.resume(self.job)
        self.assertEqual(rows["first"]["count"], 2)
        self.assertEqual(rows["first"]["effect"], "unknown")
        self.assertEqual(rows["dependent"], result["dependent"])

    def test_failed_write_continues_independent_then_resumes(self):
        insert = recovery.insert_one
        def fail_one(directory, doc, target, unit, revision):
            if target["id"] == "first":
                raise ValueError("Writer refused target")
            return insert(directory, doc, target, unit, revision)
        with patch.object(recovery, "insert_one", side_effect=fail_one):
            rows = recovery.resume(self.job)
        self.assertEqual(rows["first"]["detail"], "Writer refused target")
        self.assertEqual(rows["first"]["effect"], "not_applied")
        self.assertEqual(rows["dependent"]["status"], "pending")
        self.assertEqual(rows["independent"]["status"], "completed")
        retried = recovery.resume(self.job)
        self.assertEqual(retried["first"]["request_id"], rows["first"]["request_id"])
        self.assertEqual(retried["first"]["count"], 1)

    def test_lost_reply_then_moved_marked_occurrence(self):
        import ezdxf
        with self.assertRaises(InterruptedError):
            recovery.resume(self.job, after_save=lambda _: self.interrupt())
        model = self.job / "model.dxf"
        doc = ezdxf.readfile(model)
        moved = doc.modelspace().query("INSERT").first
        handle = moved.dxf.handle
        moved.dxf.insert = (16, 7, 0)
        doc.saveas(model)
        rows = recovery.resume(self.job)
        self.assertEqual(rows["first"]["effect"], "unknown")
        self.assertEqual(rows["dependent"]["status"], "pending")
        self.assertEqual(rows["independent"]["count"], 1)
        self.assertEqual(rows["independent"]["status"], "completed")
        self.assertEqual(recovery.resume(self.job), rows)
        reopened = ezdxf.readfile(model)
        self.assertEqual(reopened.entitydb[handle].dxf.insert, (16, 7, 0))
        self.assertEqual(len(reopened.modelspace().query("INSERT")), 2)
