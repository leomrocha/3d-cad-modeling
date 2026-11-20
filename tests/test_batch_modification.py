"""Reopen bore edits and selected child variants in a genuinely shared assembly."""

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from batch_modification import execute, sync_path
from batch_xcaf_bars import (
    box_limits,
    occurrence_name,
    children,
    open_document,
    referred,
    save_document,
)
from operation_catalogue import file_digest


@unittest.skipUnless(
    importlib.util.find_spec("cadquery"), "requires local CadQuery and XCAF"
)
class BatchModificationTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.request = self.root / "request.json"
        self.job = self.root / "job"

    def request_for(self, source, kind, targets, **values):
        self.request.write_text(
            json.dumps(
                dict(
                    model=source.name,
                    revision=file_digest(source),
                    unit="mm",
                    operation=kind,
                    targets=targets,
                    **values,
                )
            )
        )

    def test_bores(self):
        import cadquery as cq

        plate = cq.Solid.makeBox(30, 15, 5)
        for x in (5, 15, 25):
            plate = plate.cut(cq.Solid.makeCylinder(1, 5, cq.Vector(x, 7, 0)))
        source = self.root / "bores.step"
        cq.exporters.export(plate, str(source))
        targets = [
            dict(
                id=f"H{x}",
                anchor="entry centre",
                diameter=2,
                depth=5,
                end="through",
                entry=[x, 7, 5],
                direction=[0, 0, -1],
            )
            for x in (5, 15)
        ]
        self.request_for(
            source,
            "bore diameter",
            targets,
            value={"diameter": {"value": 0.4, "unit": "cm"}},
        )
        with patch(
            "batch_modification.publish_directory", side_effect=InterruptedError
        ):
            with self.assertRaises(InterruptedError):
                execute(self.request, self.job)
        self.assertFalse(self.job.exists())
        receipt = execute(self.request, self.job)
        self.assertEqual(receipt, execute(self.request, self.job))
        saved = cq.importers.importStep(str(self.job / "result.step")).val()
        radii = sorted(
            (round(e.arcCenter().x), round(e.radius(), 6))
            for e in saved.Edges()
            if e.geomType() == "CIRCLE" and abs(e.arcCenter().z - 5) < 1e-6
        )
        self.assertEqual(radii, [(5, 2), (15, 2), (25, 1)])
        (self.job / "readback.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "Published"):
            execute(self.request, self.job)

    def shared_parent(self):
        import cadquery as cq

        rack = cq.Assembly(name="rack")
        bar = cq.Solid.makeBox(20, 3, 4)
        for name, y in (("inner", 0), ("outer", 8)):
            rack.add(bar, name=name, loc=cq.Location((0, y, 0)))
        scratch = self.root / "seed.xbf"
        cq.Assembly(name="frame").add(rack).export(str(scratch))
        app, doc, tool, root = open_document(scratch)
        definition = referred(tool, children(tool, root)["1"])
        tool.AddComponent(
            root, definition, cq.Location((0, 40, 0), (0, 0, 1), 90).wrapped
        )
        # The third instance keeps the original shared assembly and leaf definitions.
        tool.AddComponent(root, definition, cq.Location((0, 80, 0)).wrapped)
        source = self.root / "shared.xbf"
        save_document(app, doc, tool, source)
        return source

    def test_shared_assembly_and_seats(self):
        source = self.shared_parent()
        targets = [
            dict(id="1/1", axis="x", anchor="start"),
            dict(id="1/2", axis="x", anchor="end"),
            dict(id="2/1", axis="x", anchor="centre"),
        ]
        values = {
            row["id"]: dict(length=dict(value=n, unit="mm"))
            for row, n in zip(targets, (32, 14, 12))
        }
        self.request_for(source, "bar length", targets, values=values)
        result = execute(self.request, self.job)["elements"]
        for row, length in zip(result, (32, 14, 12)):
            self.assertEqual(row["after"]["length"], length)
            self.assertEqual(row["after"]["seat"], row["before"]["seat"])
            self.assertEqual({peer["length"] for peer in row["unselected"]}, {20})
            self.assertEqual(
                {peer["id"] for peer in row["unselected"]}, {"2/2", "3/1", "3/2"}
            )
        self.assertAlmostEqual(result[2]["after"]["seat"][0], -1.5)
        self.assertAlmostEqual(result[2]["after"]["seat"][1], 50)

    def test_shared_occurrence_property(self):
        source = self.shared_parent()
        self.request_for(
            source, "occurrence name", [dict(id="1/1")], value={"name": "long rail"}
        )
        result = execute(self.request, self.job)["elements"]
        self.assertEqual(result[0]["before"], {"name": "inner"})
        self.assertEqual(result[0]["after"], {"name": "long rail"})

    def test_tapered_solid_with_small_volume(self):
        import cadquery as cq

        shape = cq.Solid.makeWedge(0.1, 0.01, 0.01, 0, 0, 0.095, 0.01)
        self.assertEqual(len(shape.Faces()), 6)
        self.assertLess(0.1 * 0.01 * 0.01 - shape.Volume(), 1e-6)
        with self.assertRaisesRegex(ValueError, "rectangular solid"):
            box_limits(shape, "x")

    def test_unicode_paths_labels_and_interrupted_directory_sync(self):
        source = self.shared_parent()
        directory = self.root / "révisions"
        directory.mkdir()
        source = source.rename(directory / "châssis.xbf")
        self.request = directory / "édition.json"
        self.job = directory / "pièce"
        label = "Côté forêt – 左"
        self.request_for(
            source, "occurrence name", [{"id": "1/1"}], value={"name": label}
        )
        flushed = []

        def interrupt(path):
            if path == directory and self.job.is_dir():
                raise InterruptedError("published directory sync interrupted")
            sync_path(path)
            flushed.append(path.name)

        with patch("batch_modification.sync_path", side_effect=interrupt):
            with self.assertRaises(InterruptedError):
                execute(self.request, self.job)
        self.assertTrue(
            {"result.xbf", "manifest.json", "readback.json", "request.json", "job"}
            <= set(flushed)
        )
        with patch("batch_modification.sync_path", wraps=sync_path) as flush:
            result = execute(self.request, self.job)
            flush.assert_called_with(directory)
        self.assertEqual(result["elements"][0]["after"]["name"], label)
        app, doc, tool, root = open_document(self.job / "result.xbf")
        part = referred(tool, children(tool, root)["1"])
        self.assertEqual(occurrence_name(children(tool, part)["1"]), label)
