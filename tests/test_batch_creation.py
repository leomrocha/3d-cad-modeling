"""Check creation on a sloping drawing plane and on a solid with a retained bore."""

import importlib.util
import json
import os
import subprocess
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from batch_creation import execute, load_solid  # noqa: E402
from operation_catalogue import file_digest  # noqa: E402


class CreationTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.request = self.root / "request.json"
        self.job = self.root / "job"
        self.pattern = dict(
            kind="explicit",
            unit="mm",
            tolerance=0.001,
            reference="plate datum",
            frame=dict(origin=[0, 0, 10], x=[1, 0, 0], y=[0, 1, 0]),
            positions=[dict(id="H1", xy=[10, 10]), dict(id="H2", xy=[30, 10])],
        )

    def prepare(self, source, operation, **extra):
        spec = dict(
            model=str(source),
            revision=file_digest(source),
            pattern=self.pattern,
            relationship="individual",
            operation=operation,
            **extra,
        )
        self.request.write_text(json.dumps(spec))
        return spec

    def interior(self):
        self.pattern.update(
            kind="interior", layout="rows", origin=[2,5], pitch_xy=[4,20],
            outer=dict(kind="polygon",vertices=[[0,0],[10,0],[10,10],[0,10]]),
            cutouts=[dict(kind="circle",centre=[8.75,5],radius=0.5)],
            containment="footprint", footprint=dict(kind="circle",centre=[0,0],radius=1),
            clearance=1)
        self.pattern.pop("positions")

    @unittest.skipUnless(all(importlib.util.find_spec(pkg) for pkg in ("ezdxf","cadquery","shapely")),
                         "requires local DXF and STEP providers")
    def test_qualification_and_delivery_of_legacy_footprint_jobs(self):
        import cadquery as cq
        import ezdxf
        import venv
        import batch_creation
        from batch_delivery import CONTRACTS, provider, verify_job_sample
        from batch_sample_readback import verify_creation
        venv.EnvBuilder(with_pip=False).create(self.root / "router")
        launcher = self.root / "router/bin/python"
        self.interior()
        self.pattern["frame"]["origin"] = [10,10,10]
        self.pattern["pitch_xy"] = [50,50]
        for op in ("circle","cut"):
            if op == "circle":
                source = self.root/"drawing.dxf"
                ezdxf.new("R2010",units=4).saveas(source)
                extra = {}
            else:
                source = self.root/"block.step"
                cq.exporters.export(cq.Solid.makeBox(30,30,10),str(source))
                extra = {"direction":"-normal"}
            for diameter in (2,8):
                job = self.root/f"{op}-{diameter}"
                self.request = self.root/(job.name+".json")
                value = {"diameter":diameter}
                if op == "cut":
                    value.update(depth=10,end="through")
                spec = self.prepare(source,op,value=value,**extra)
                # Exercise the former writer contract with native geometry and its complete manifest.
                with patch("batch_creation.measure_disk_clearances", return_value=None):
                    stored = execute(self.request,job)
                hashes = {p.name:file_digest(p) for p in job.iterdir()}
                action,entity,output = CONTRACTS[op]
                row = dict(name=op,action=action,input=entity,output=output)
                method = dict(**row,probe="guided",sample_request=str(self.request),readback_file=str(job/"manifest.json"))
                resource = dict(id="cad",location=batch_creation.__file__,python=sys.executable,
                                kind="guided",backend=provider(op),methods=[method])
                if diameter == 8:
                    with self.assertRaisesRegex(ValueError,r"P1 disk clearance to outer border is -2 mm"):
                        verify_job_sample(row,resource,job/"manifest.json",replay=False)
                else:
                    self.assertEqual(verify_job_sample(row,resource,job/"manifest.json",replay=False),
                                     hashes["manifest.json"])
                    newer = execute(self.request,job)
                    self.assertEqual(newer.pop("footprint_verification")["P1"]["outer_clearance"],1)
                    self.assertEqual(newer,stored)
                    resources = self.root/(op+"-resources.json")
                    catalogue = self.root/(op+"-catalogue.json")
                    resources.write_text(json.dumps([resource]))
                    subprocess.run([sys.executable,ROOT/"scripts/operation_catalogue.py","--catalogue",catalogue,
                                    "refresh","--resources",resources],check=True,capture_output=True)
                    result=subprocess.run([launcher,ROOT/"scripts/batch_delivery.py",self.request,job,
                                           "--catalogue",catalogue,"--request-sha256",file_digest(self.request)],
                                          check=True,capture_output=True,text=True)
                    report=json.loads(result.stdout)
                    self.assertEqual(report["readback"],stored)
                    self.assertEqual(report["footprint_verification"]["P1"]["outer_clearance"],1)
                self.assertEqual({p.name:file_digest(p) for p in job.iterdir()},hashes)
        with self.assertRaisesRegex(ValueError,"projected part outline"):
            verify_creation(dict(spec,operation="occurrence"),source,job,stored["elements"])

    @unittest.skipUnless(importlib.util.find_spec("ezdxf") and importlib.util.find_spec("shapely"),
                         "requires local ezdxf and Shapely")
    def test_interior_actual_circle_footprints(self):
        import ezdxf
        from batch_creation import circles
        self.interior()
        self.pattern["frame"] = dict(origin=[12,20,7],x=[0,0,1],y=[-1,0,0])
        source = self.root / "plane.dxf"
        ezdxf.new("R2010",units=4).saveas(source)
        values = {"P1":{"diameter":{"value":0.2,"unit":"cm"}},
                  "P2":{"diameter":{"value":0.25,"unit":"cm"}}}
        for key, diameter, boundary in (("P1",0.8,"outer border"),("P2",0.4,"cutout 1")):
            oversized = {**values,key:{"diameter":{"value":diameter,"unit":"cm"}}}
            self.prepare(source,"circle",values=oversized)
            with patch("batch_creation.circles",side_effect=AssertionError("writer called before clearance validation")):
                with self.assertRaisesRegex(ValueError, f"{key} disk clearance to {boundary}"):
                    execute(self.request,self.job)
            self.assertFalse(self.job.exists())
        self.prepare(source,"circle",values=values)
        def wrong_readback(*args):
            result = circles(*args)
            result[0]["centre"][2] -= 1
            return result
        with patch("batch_creation.circles",side_effect=wrong_readback):
            with self.assertRaisesRegex(ValueError,"P1 disk clearance to outer border"):
                execute(self.request,self.job)
        self.assertFalse(self.job.exists())
        receipt = execute(self.request,self.job)
        self.assertEqual([e["id"] for e in receipt["elements"]],["P1","P2"])
        saved = ezdxf.readfile(self.job/"result.dxf")
        for element, expected in zip(receipt["elements"],[2,2.5]):
            entity = saved.entitydb[element["handle"]]
            self.assertEqual(entity.dxf.radius*2,expected)
            self.assertEqual(list(entity.ocs().to_wcs(entity.dxf.center)),element["centre"])
        self.assertEqual(receipt["elements"][0]["outer_clearance"],1)
        self.assertEqual(receipt["elements"][1]["minimum_cutout_clearance"],1)
        self.assertEqual(execute(self.request,self.job),receipt)

    @unittest.skipUnless(importlib.util.find_spec("cadquery") and importlib.util.find_spec("shapely"),
                         "requires local CadQuery and Shapely")
    def test_interior_bore_disk_and_polygon_cutout(self):
        import cadquery as cq
        self.interior()
        self.pattern["outer"] = dict(kind="circle",centre=[5,5],radius=5)
        self.pattern["cutouts"] = [dict(kind="polygon",vertices=[[8.25,4],[9,4],[9,6],[8.25,6]])]
        source = self.root/"host.step"
        cq.exporters.export(cq.Solid.makeBox(15,15,10),str(source))
        values = {"P1":dict(diameter=2,end="blind",depth=2),
                  "P2":dict(diameter=4,end="through",depth=10)}
        self.prepare(source,"cut",direction="-normal",values=values)
        with self.assertRaisesRegex(ValueError,"P2 disk clearance to cutout 1"):
            execute(self.request,self.job)
        self.assertFalse(self.job.exists())
        values["P2"]["diameter"] = 2.5
        self.prepare(source,"cut",direction="-normal",values=values)
        a,b = execute(self.request,self.job)["elements"]
        self.assertEqual((a["outer_clearance"],b["minimum_cutout_clearance"]),(1,1))
        self.assertEqual((a["bottom"],b["exit"]),([2,5,8],[6,5,0]))
        self.assertTrue(load_solid(self.job/"result.step").isValid())

    @unittest.skipUnless(importlib.util.find_spec("ezdxf"), "requires a locally installed CAD provider")
    def test_dependency_free_launcher_uses_selected_interpreter(self):
        import ezdxf
        import venv
        import batch_creation
        from batch_delivery import CONTRACTS, provider

        source = self.root / "drawing.dxf"
        ezdxf.new("R2010", units=4).saveas(source)
        spec = self.prepare(source, "circle", value={"diameter": 3})
        spec["model"] = source.name
        self.request.write_text(json.dumps(spec))
        sample = self.root / "sample"
        execute(self.request, sample)
        venv.EnvBuilder(with_pip=False).create(self.root / "launcher")
        launcher = self.root / "launcher/bin/python"
        subprocess.run([launcher, "-I", "-c", "import importlib.util; assert importlib.util.find_spec('ezdxf') is None"], check=True)
        action, entity, output = CONTRACTS["circle"]
        method = dict(name="circle", probe="guided", action=action, input=entity, output=output,
                      sample_request=str(self.request), readback_file=str(sample/"manifest.json"))
        resource = dict(id="cad", location=batch_creation.__file__, python=sys.executable,
                        kind="guided", backend=provider("circle"), methods=[method])
        resources = self.root / "resources.json"
        resources.write_text(json.dumps([resource]))
        catalogue = self.root / "catalogue.json"
        subprocess.run([launcher, "-E", "-s", ROOT/"scripts/operation_catalogue.py", "--catalogue", catalogue,
                        "refresh", "--resources", resources], check=True, capture_output=True)
        self.assertTrue(json.loads(catalogue.read_bytes())["operations"][0]["usable"])
        command = [launcher,"-E","-s", ROOT/"scripts/batch_delivery.py", self.request,self.job,"--catalogue",catalogue,
                   "--request-sha256",file_digest(self.request)]
        for _ in range(2):
            result = subprocess.run(command, cwd="/", capture_output=True, text=True)
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
            self.assertEqual(json.loads(result.stdout)["completed"], ["H1","H2"])
        self.assertEqual(len(ezdxf.readfile(self.job/"result.dxf").modelspace().query("CIRCLE")),2)
        # A previously published result cannot stand in for a different reviewed pattern.
        from batch_delivery import published_readback
        wrong = json.loads(self.request.read_bytes())
        wrong["pattern"]["positions"][0]["id"] = "other"
        self.request.write_text(json.dumps(wrong))
        with self.assertRaisesRegex(ValueError,"reviewed request or targets"):
            published_readback(self.job,self.request,wrong,file_digest(self.request),["other","H2"],{})
        (self.job/"result.dxf").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError,"reviewed request or targets"):
            published_readback(self.job,self.request,spec,file_digest(self.job/"request.json"),["H1","H2"],{})


    @unittest.skipUnless(importlib.util.find_spec("ezdxf"), "requires local ezdxf")
    def test_oriented_drawing_publication_and_retry(self):
        import ezdxf

        doc = ezdxf.new("R2010", units=4)
        doc.modelspace().add_line([0, 0], [8, 0])
        source = self.root / "drawing.dxf"
        doc.saveas(source)
        self.pattern["frame"]["y"] = [0, 0, 1]
        spec = self.prepare(
            source, "circle", value={"diameter": {"value": 0.4, "unit": "cm"}}
        )
        spec["model"] = source.name
        self.request.write_text(json.dumps(spec))
        with patch("batch_creation.publish_directory", side_effect=InterruptedError):
            with self.assertRaises(InterruptedError):
                execute(self.request, self.job)
        self.assertFalse(self.job.exists())
        receipt = execute(self.request, self.job)
        self.assertEqual(receipt, execute(self.request, self.job))
        saved = ezdxf.readfile(self.job / "result.dxf")
        self.assertEqual(len(saved.modelspace().query("CIRCLE")), 2)
        self.assertEqual(len(saved.modelspace().query("LINE")), 1)
        self.assertEqual(receipt["elements"][1]["centre"], [30, 0, 20])
        self.assertEqual(receipt["elements"][0]["diameter"], 4)
        self.assertEqual(receipt["elements"][0]["normal"], [0, -1, 0])
        stored = self.job / "readback.json"
        changed = json.loads(stored.read_text())
        changed["elements"] = []
        stored.write_text(json.dumps(changed))
        with self.assertRaisesRegex(ValueError, "readback changed"):
            execute(self.request, self.job)

    @unittest.skipUnless(
        importlib.util.find_spec("cadquery"), "requires local CadQuery"
    )
    def test_through_and_blind_on_existing_host(self):
        import cadquery as cq

        source = self.root / "host.step"
        existing = cq.Workplane("XY").box(60, 40, 10, centered=(False, False, False))
        existing = existing.cut(cq.Workplane("XY").center(17, 23).circle(5).extrude(10))
        cq.exporters.export(existing, str(source))
        spec = self.prepare(
            source,
            "cut",
            direction="-normal",
            values={
                "H1": dict(end="through", diameter=3, depth=10),
                "H2": dict(end="blind", diameter=5, depth=3),
            },
        )
        self.assertEqual(
            execute(self.request, self.job)["elements"][1]["bottom"], [30, 10, 7]
        )
        self.assertEqual(file_digest(source), spec["revision"])
        saved = cq.importers.importStep(str(self.job / "result.step")).val()
        for xyz, expected in [
            ((17, 23, 5), False),
            ((10, 10, 0.1), False),
            ((30, 10, 8), False),
            ((30, 10, 6), True),
            ((40, 30, 5), True),
        ]:
            self.assertEqual(saved.Solids()[0].isInside(cq.Vector(*xyz)), expected)
        spec["values"]["H1"]["end"] = "blind"
        self.request.write_text(json.dumps(spec))
        invalid = self.root / "invalid"
        with self.assertRaisesRegex(ValueError, "bore rim|endpoint material"):
            execute(self.request, invalid)
        self.assertFalse(invalid.exists())

    @unittest.skipUnless(
        importlib.util.find_spec("cadquery"), "requires local CadQuery"
    )
    def test_membrane_and_entry_skin(self):
        import cadquery as cq

        source = self.root / "host.step"
        cq.exporters.export(
            cq.Workplane("XY").box(60, 40, 10, centered=(False, False, False)),
            str(source),
        )
        self.pattern["positions"] = [dict(id="H1", xy=[15, 15])]
        for z, depth, end in ((10, 9.995, "through"), (9.997, 4, "blind")):
            with self.subTest(z=z, depth=depth):
                self.pattern["frame"]["origin"][2] = z
                self.prepare(
                    source,
                    "cut",
                    direction="-normal",
                    value=dict(end=end, diameter=12, depth=depth),
                )
                with self.assertRaisesRegex(ValueError, "bore rim|endpoint material"):
                    execute(self.request, self.job)
                self.assertFalse(self.job.exists())

    @unittest.skipUnless(
        importlib.util.find_spec("cadquery"), "requires local CadQuery"
    )
    def test_reject_multiple_step_roots_and_independent_geometry(self):
        import cadquery as cq
        from OCP.STEPControl import STEPControl_Writer, STEPControl_AsIs
        from OCP.IFSelect import IFSelect_RetDone

        solid = cq.Solid.makeBox(20, 20, 10)
        edge = cq.Edge.makeLine((25, 25, 0), (25, 25, 10))
        vertex = cq.Vertex.makeVertex(25, 25, 0)
        source = self.root / "source.step"
        for shapes in [
            [solid, solid.translate((30, 0, 0))],
            [solid, edge],
            [cq.Compound.makeCompound([solid, edge])],
            [solid, vertex],
        ]:
            with self.subTest(types=[s.ShapeType() for s in shapes]):
                writer = STEPControl_Writer()
                for shape in shapes:
                    self.assertEqual(
                        writer.Transfer(shape.wrapped, STEPControl_AsIs),
                        IFSelect_RetDone,
                    )
                self.assertEqual(writer.Write(str(source)), IFSelect_RetDone)
                with self.assertRaisesRegex(
                    ValueError, "independent geometry|exactly one valid solid"
                ):
                    load_solid(source)

    @unittest.skipUnless(
        importlib.util.find_spec("cadquery"), "requires local CadQuery"
    )
    def test_selected_catalogue_occurrences(self):
        import cadquery as cq

        request = os.environ.get("CAD_CREATION_OCCURRENCE_REQUEST")
        if not request:
            self.skipTest(
                "set CAD_CREATION_OCCURRENCE_REQUEST to an existing catalogue occurrence request"
            )
        original = Path(request).resolve()
        spec = json.loads(original.read_bytes())
        self.assertEqual(spec["operation"], "occurrence")
        spec["model"] = os.path.relpath(original.parent / spec["model"], self.root)
        for field in ("data", "search_cli"):
            spec["part"][field] = os.path.relpath(
                original.parent / spec["part"][field], self.root
            )
        self.request.write_text(json.dumps(spec))
        run = [
            sys.executable,
            str(ROOT / "scripts/batch_creation.py"),
            str(self.request),
            str(self.job),
        ]
        first = subprocess.run(run, cwd="/", capture_output=True, text=True, check=True)
        again = subprocess.run(
            run, cwd=self.root, capture_output=True, text=True, check=True
        )
        self.assertEqual(json.loads(first.stdout), json.loads(again.stdout))
        self.assertEqual(
            (self.job / "request.json").read_bytes(), self.request.read_bytes()
        )
        saved = cq.Assembly.load(str(self.job / "result.xbf"))
        rows = json.loads(first.stdout)["elements"]
        self.assertGreaterEqual(len(saved.children), 2)
        self.assertEqual({c.name for c in saved.children}, {r["id"] for r in rows})
        self.assertTrue(
            all(
                saved.children[0].obj.wrapped.IsPartner(child.obj.wrapped)
                for child in saved.children[1:]
            )
        )
        self.assertGreater(len({tuple(row[3] for row in r["frame"]) for r in rows}), 1)
        self.assertTrue(
            any(
                any(abs(row[i] - float(i == j)) > 1e-8 for i in range(3))
                for r in rows
                for j, row in enumerate(r["frame"])
            )
        )
        spec["part"]["search_cli"] = "missing-search.py"
        self.request.write_text(json.dumps(spec))
        failed = subprocess.run(
            run[:-1] + [str(self.root / "failed")],
            cwd="/",
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(failed.returncode, 0)
        self.assertNotIn("Traceback", failed.stderr)
        self.assertFalse((self.root / "failed").exists())


if __name__ == "__main__":
    unittest.main()
