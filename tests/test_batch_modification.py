"""Reopen bore edits and selected child variants in a genuinely shared assembly."""

import importlib.util
import json
import os
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
        for row in receipt["elements"]:
            self.assertEqual(len(row["unselected"]), 1)
            peer = row["unselected"][0]
            self.assertEqual(peer["before"], peer["after"])
            self.assertEqual(peer["after"]["diameter"], 2)
            self.assertEqual(peer["after"]["entry"][0], 25)
        import batch_modification
        from batch_delivery import CONTRACTS, provider, verify_job_sample
        from operation_catalogue import verify_method
        action, entity, output = CONTRACTS["bore diameter"]
        method = dict(name="resize", sample_request=str(self.request))
        resource = dict(location=batch_modification.__file__, backend=provider("bore diameter"),
                        methods=[method], python=sys.executable)
        row = dict(name="resize", action=action, input=entity, output=output)
        self.assertEqual(verify_method(row,resource,self.job/"manifest.json"),
                         file_digest(self.job/"manifest.json"))
        # The standalone catalogue can verify through the approved CAD interpreter without importing the engineering package.
        import subprocess
        import shutil
        import operation_catalogue
        isolated = self.root / "standalone"
        isolated.mkdir()
        shutil.copyfile(operation_catalogue.__file__, isolated / "operation_catalogue.py")
        probe = isolated / "verify.py"
        probe.write_text("import sys,json;from pathlib import Path;from operation_catalogue import verify_method;"
                         "row,resource,sample=json.load(sys.stdin);print(verify_method(row,resource,Path(sample)))")
        outcome = subprocess.run([sys.executable, "-E", "-s", str(probe)],
                                 input=json.dumps([row,resource,str(self.job/"manifest.json")]),
                                 capture_output=True,text=True,check=True)
        self.assertEqual(outcome.stdout.strip(),file_digest(self.job/"manifest.json"))
        noop = self.root/"noop"
        resource["methods"][0]["sample_request"]=str(self.root/"noop-request.json")
        noop_request=self.root/"noop-request.json"
        original=json.loads(self.request.read_bytes())
        original["value"]["diameter"]={"unit":"mm","value":2}
        noop_request.write_text(json.dumps(original))
        execute(noop_request,noop)
        with self.assertRaisesRegex(ValueError,"did not change"):
            verify_job_sample(row,resource,noop/"manifest.json",replay=False)
        (self.job / "readback.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "Published"):
            execute(self.request, self.job)

    def shared_parent(self, with_partner=False):
        import cadquery as cq

        rack = cq.Assembly(name="rack")
        bar = cq.Solid.makeBox(20, 3, 4)
        for name, y in (("inner", 0), ("outer", 8)):
            rack.add(bar, name=name, loc=cq.Location((0, y, 0)))
        if with_partner:
            rack.add(
                cq.Solid.makeBox(20, 3, 2), name="mount", loc=cq.Location((0, 0, 4))
            )
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

    def test_catalogue_replacement_and_lost_reply(self):
        import cadquery as cq
        from private_catalogue import prepare as index_parts

        cli = os.environ.get("CAD_MODELS_SEARCH_CLI")
        if not cli:
            self.skipTest(
                "set CAD_MODELS_SEARCH_CLI to the installed catalogue search.py"
            )
        cli = Path(cli).resolve()
        source = self.shared_parent(with_partner=True)
        assets = self.root / "assets"
        assets.mkdir()
        replacement = assets / "keyed.step"
        # Old seat is the +Z face. Catalogue seat is the +X face at a different origin.
        part = cq.Solid.makeBox(7, 20, 3, cq.Vector(7, 10, 15))
        cq.exporters.export(part, str(replacement))
        data = index_parts(
            assets,
            self.root / "snapshots",
            cli.with_name("build.py"),
            os.environ.get("CAD_CATALOGUE_PYTHON", sys.executable),
            {"keyed.step": {"id": "keyed", "units": "mm"}},
        )
        selected = json.loads((data / "catalogue.json").read_text())[0]
        asset = dict(
            model=str(data / "packages" / selected["file"]),
            revision=file_digest(replacement),
            part=dict(id="keyed", data=str(data), search_cli=str(cli), query="keyed"),
            corners=[[14, 10, 15], [14, 30, 15], [14, 10, 18]],
        )
        targets = [
            dict(id=key, corners=[[0, 0, 4], [20, 0, 4], [0, 3, 4]])
            for key in ("1/1", "2/1")
        ]
        for target in targets:
            target["partner"] = dict(
                id=target["id"].split("/")[0] + "/3",
                corners=[[0, 3, 0], [20, 3, 0], [0, 0, 0]],
            )
        self.request_for(
            source,
            "replace occurrence",
            targets,
            replacement=asset,
            mates=["fixed keyed seat"],
        )

        def lost_reply(path):
            if self.job.exists():
                raise InterruptedError("lost reply")
            sync_path(path)

        with patch("batch_modification.sync_path", side_effect=lost_reply):
            with self.assertRaises(InterruptedError):
                execute(self.request, self.job)
        report = execute(self.request, self.job)
        fresh = execute(self.request, self.root / "fresh")
        self.assertEqual(report["elements"], fresh["elements"])
        self.assertEqual(fresh, execute(self.request, self.root / "fresh"))
        self.assertEqual([r["id"] for r in report["elements"]], ["1/1", "2/1"])
        self.assertTrue(
            all(
                r["occupants"] == 1 and r["interface_mm"] == [20, 3]
                for r in report["elements"]
            )
        )
        self.assertEqual(len({r["saved_definition"] for r in report["elements"]}), 1)
        asset["corners"][1] = [14, 29, 15]
        self.request_for(
            source,
            "replace occurrence",
            targets,
            replacement=asset,
            mates=["fixed keyed seat"],
        )
        with self.assertRaisesRegex(ValueError, "seating face"):
            execute(self.request, self.root / "invalid")

    def test_contact_regions_and_interference(self):
        import cadquery as cq
        from batch_replacement import (
            check_interference,
            check_partner,
            interface,
            occupants,
        )

        identity = cq.Location()

        def entry(shape):
            return 1, identity, shape

        block = cq.Solid.makeBox(20, 3, 4)
        corners = [[0, 0, 4], [20, 0, 4], [0, 3, 4]]
        seat, dims, face = interface(block, corners)
        offset = block.translate((1, 0, 0))
        _, _, overlap = interface(offset, [[1, 0, 4], [21, 0, 4], [1, 3, 4]])
        self.assertAlmostEqual(face.intersect(overlap).Area(), 57)
        centre = cq.Vector(10, 1.5, 0)
        ring = cq.Solid.makeCylinder(15, 4, centre).cut(
            cq.Solid.makeCylinder(12, 4, centre)
        )
        self.assertEqual(
            occupants(
                {
                    "target": entry(block),
                    "overlap": entry(offset),
                    "annulus": entry(ring),
                },
                face,
            ),
            ["target", "overlap"],
        )
        tiny = cq.Solid.makeBox(2, 1, 2, cq.Vector(9, 1, 4))
        with self.assertRaisesRegex(ValueError, "Partner interface dimensions"):
            check_partner(
                entry(tiny),
                [[9, 2, 4], [11, 2, 4], [9, 1, 4]],
                cq.Location((0, 0, 0), (1, 0, 0), 180),
                seat,
                dims,
                "target",
            )
        neighbour = cq.Solid.makeBox(5, 2, 1, cq.Vector(0, 0, -1))
        taller = cq.Solid.makeBox(20, 3, 5, cq.Vector(0, 0, -1))
        initial = {"target": entry(block), "neighbour": entry(neighbour)}
        final = dict(initial, target=entry(taller))
        for selected in (["target"], ["target", "neighbour"]):
            with self.assertRaisesRegex(ValueError, "10 mm³"):
                check_interference(initial, final, selected)

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
