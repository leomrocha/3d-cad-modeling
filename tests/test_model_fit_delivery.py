"""Regression coverage for catalogue reuse, measured fit and viewport delivery."""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from assembly_verification import indexed_feature_heights, solve_feature_height
from catalogue_candidates import digest, lookup, variant_check
from retained_artifacts import verify_gallery_capture
from service_clearance import extruded_profile_gap, sampled_lock_withdrawal


class ModelFitTests(unittest.TestCase):
    def test_catalogue_metadata_survives_lookup(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            cli = root / "search.py"
            variants = ["Extended position", {"extension_mm": 7}]
            rows = [dict(id=str(i), name="Slide", variant=v, revision=2, state="Draft",
                         needs_information=False) for i, v in enumerate(variants)]
            hits = [dict(id=row["id"], name="Slide", exact=True) for row in rows]
            cli.write_text("print(" + repr(json.dumps(hits)) + ")")
            (root / "catalogue.json").write_text(json.dumps(rows))
            (root / "catalogue.sqlite").touch()
            for row, candidate in zip(rows, lookup(cli, root, "Slide")["candidates"], strict=True):
                for field in ("variant", "revision", "state", "needs_information"):
                    self.assertEqual(candidate[field], row[field])
                self.assertEqual(variant_check(candidate, {"extension_mm": 7})["status"], "needs-evidence")

    def test_height_settings(self):
        def descending(setting):
            return 12 - setting * 2
        rows = indexed_feature_heights([0, 2, 4], descending, target_mm=7, tolerance_mm=1)
        self.assertEqual([r["height_mm"] for r in rows], [12, 8, 4])
        self.assertEqual([r["within_tolerance"] for r in rows], [False, True, False])
        for measure, target in ((descending, 7), (lambda setting: setting * 2, 5)):
            solved = solve_feature_height((0, 4), measure, target_mm=target, tolerance_mm=0)
            self.assertEqual((solved["result"], solved["setting"]), ("PASS", 2.5))
        self.assertEqual(solve_feature_height((0, 4), descending, target_mm=14,
                                              tolerance_mm=0)["result"], "UNREACHABLE")

    def test_retainer_must_obstruct_the_named_part(self):
        # One-dimensional overlapping solids with a unit square cross section.
        def probe(retainer_start, guard_start):
            def volume(state, moving, obstacle, displacement):
                x, y, z = displacement
                self.assertEqual((moving, y, z), ("slide", 0, 0))
                if obstacle == "guard":
                    start = guard_start
                else:
                    start = retainer_start if state == "engaged" else 20
                return max(0, min(x + 1, start + 1) - max(x, start))
            return sampled_lock_withdrawal("slide", "pin", ["guard", "pin"], direction=(2, 0, 0),
                                           stations_mm=[0, 1, 2, 3], free_travel_mm=1,
                                           volume_tolerance_mm3=0, common_volume=volume)
        locked = probe(2, 20)
        self.assertEqual((locked["result"], locked["first_sampled_retainer_obstruction_mm"]), ("PASS", 2))
        self.assertEqual(probe(20, 20)["result"], "FAIL")
        self.assertEqual(probe(20, 2)["result"], "FAIL")
        self.assertEqual(probe(1, 20)["result"], "FAIL")

    @unittest.skipUnless(importlib.util.find_spec("shapely"), "Requires local planar polygon operations")
    def test_prismatic_clearance(self):
        from shapely.geometry import box
        first = ("base", box(0, 0, 1, 1), (0, 2), "boundary")
        for x, span, expected in [(0, (6, 7), 4), (4, (6, 7), 5), (1, (0, 1), 0)]:
            other = ("slide", box(x, 0, x+1, 1), span, "envelope")
            gap = extruded_profile_gap(first, other, pose="extended")
            self.assertEqual(gap["clearance_mm"], expected)
            self.assertEqual(gap["basis"], ["boundary", "envelope"])

    def test_gallery_compares_record_assets_and_receipts(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            model, image = root / "model.dxf", root / "view.png"
            model.write_bytes(b"saved revision")
            image.write_bytes(b"captured image")
            identity = dict(result="PASS", document_id=2, geometry_revision=4, session_id="local")
            saved, capture = [dict(identity, sha256=digest(p)) for p in (model, image)]
            preview = dict(view="Top", file=image.name)
            record = dict(id="plate", revision=3, file=model.name, previews=[preview])
            def verify():
                return verify_gallery_capture(root, record, view="Top", checkpoint=saved, capture=capture)
            self.assertEqual(verify()["image_sha256"], capture["sha256"])
            for previews in ([], [preview, preview]):
                record["previews"] = previews
                with self.assertRaisesRegex(ValueError, "one gallery entry"):
                    verify()
            record["previews"] = [preview]
            image.write_bytes(b"older image")
            with self.assertRaisesRegex(ValueError, "view.png"):
                verify()
            capture["session_id"] = "another"
            with self.assertRaisesRegex(ValueError, "sessions differ"):
                verify()
