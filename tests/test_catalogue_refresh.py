"""Verify local CAD Models snapshots against repository test fixtures."""
import importlib.util
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

TESTS = Path(__file__).resolve().parent
FIXTURES = TESTS / "fixtures"
sys.path.insert(0, str(TESTS.parent / "scripts"))
from catalogue_candidates import digest, lookup, variant_check
from private_catalogue import prepare


class CatalogueRefreshTests(unittest.TestCase):
    def test_snapshot_refresh_and_drawing_metadata(self):
        root = os.environ.get("CAD_MODELS_ROOT")
        if not root:
            self.skipTest("set CAD_MODELS_ROOT to an existing CAD Models installation")
        builder = Path(root) / "scripts/build.py"
        search = Path(root) / "scripts/search.py"
        if not (builder.is_file() and search.is_file()):
            self.skipTest("CAD_MODELS_ROOT lacks scripts/build.py or scripts/search.py")
        if not importlib.util.find_spec("duckdb"):
            self.skipTest("the local CAD Models builder requires DuckDB")
        original = FIXTURES / "mesh-position/plate-10.stl"
        revised = FIXTURES / "catalogue-refresh/plate-12.stl"
        drawing = FIXTURES / "catalogue-refresh/assembly-view.dxf"
        metadata = {
            "fixture.stl": dict(id="plate-fixture", name="Private plate fixture",
                                role="solid mesh", units="mm")
        }
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            source = folder / "source"
            independent = folder / "independent"
            source.mkdir()
            independent.mkdir()
            plate = source / "fixture.stl"
            shutil.copyfile(original, plate)
            shutil.copyfile(revised, independent / plate.name)

            def refresh(parts=source, snapshots="snapshots"):
                return prepare(parts, folder / snapshots, builder, sys.executable, metadata)

            def find(snapshot, query="Private plate fixture"):
                (candidate,) = lookup(search, snapshot, query)["candidates"]
                return candidate

            first = refresh()
            self.assertEqual(refresh(), first)
            hit = find(first)
            independent_hit = find(refresh(independent, "independent-snapshots"))
            self.assertEqual(hit["id"], "plate-fixture")
            self.assertEqual(independent_hit["id"], hit["id"])
            self.assertEqual(hit["sha256"], digest(original))
            self.assertEqual(independent_hit["sha256"], digest(revised))
            self.assertNotEqual(hit["sha256"], independent_hit["sha256"])
            self.assertEqual(hit["private_source"]["units"], "mm")

            shutil.copyfile(revised, plate)
            updated = refresh()
            self.assertNotEqual(updated, first)
            self.assertEqual(find(updated)["sha256"], digest(revised))
            self.assertEqual(find(first)["sha256"], digest(original))

            plate.rename(source / "renamed.stl")
            with self.assertRaisesRegex(ValueError, "Missing listed assets"):
                refresh()
            metadata["renamed.stl"] = metadata.pop(plate.name)
            renamed = find(refresh())
            self.assertEqual(renamed["private_source"]["path"], "renamed.stl")
            self.assertEqual(renamed["sha256"], digest(revised))

            shutil.copyfile(drawing, source / drawing.name)
            drawing_hit = find(refresh(), "assembly-view")
            self.assertEqual(drawing_hit["private_source"]["role"], "drawing")
            self.assertIsNone(drawing_hit["private_source"]["units"])
            self.assertEqual(drawing_hit["sha256"], digest(drawing))

    def test_variant_fields(self):
        for field, actual, requested in (
            ("seal", "ZZ", "2RS"),
            ("insert", "A", "B"),
            ("thread_pitch_mm", 1.0, 0.75),
        ):
            with self.subTest(field=field):
                candidate = dict(private_source=dict(
                    variant={field: actual}, evidence="synthetic designation sheet"
                ))
                self.assertEqual(variant_check(candidate, {field: requested})["status"],
                                 "different-variant")
                self.assertEqual(variant_check(candidate, {field: actual})["status"],
                                 "fields-match")
                self.assertEqual(variant_check(candidate, {"missing": actual})["status"],
                                 "needs-evidence")
