"""Exercise correction reuse and inspect reopened geometry through the installed-style APIs."""
import importlib.util
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/"scripts"), str(ROOT/"format_translation")]
from correction_sequence import run
from mesh_repair_evidence import compare
from operation_catalogue import file_digest
from convert import convert


@unittest.skipUnless(importlib.util.find_spec("cadquery"), "requires local CadQuery")
class CorrectionTests(unittest.TestCase):
    def test_chain_and_independent_sources(self):
        import cadquery as cq
        from batch_modification import solid_difference

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shape = cq.Solid.makeBox(30, 16, 5)
            for x in (6, 18):
                shape = shape.cut(cq.Solid.makeCylinder(1,5,cq.Vector(x,6,0)))
            model = root/"source.step"
            cq.exporters.export(shape, str(model))

            def step(name,x,parent=None):
                edit = dict(unit="mm",operation="bore diameter",targets=[
                    dict(id=name,anchor="entry centre",diameter=2,depth=5,end="through",
                         entry=[x,6,5],direction=[0,0,-1])],value={"diameter":{"value":3,"unit":"mm"}})
                if parent:
                    return dict(id=name,after=parent,edit=edit)
                edit.update(model=model.name,revision=file_digest(model))
                return dict(id=name,edit=edit)

            steps = [step("first",6),step("second",18,"first"),step("independent",18)]
            plan = root/"plan.json"
            def execute(cache="cache"):
                plan.write_text(json.dumps(dict(steps=steps)))
                return run(plan,root/cache)
            initial = execute()
            self.assertTrue(all(r["status"]=="PASS" for r in initial.values()),initial)
            self.assertTrue(all(r["reused"] for r in execute().values()))
            steps[1]["edit"]["value"]["diameter"]["value"] = 3.5
            late = execute()
            self.assertEqual([r["reused"] for r in late.values()],[True,False,True])
            steps[0]["edit"]["value"]["diameter"]["value"] = 4
            early = execute()
            self.assertEqual([r["reused"] for r in early.values()],[False,False,True])
            fresh = execute("fresh")
            for key in fresh:
                a,b = [cq.importers.importStep(rows[key]["output"]).val() for rows in (early,fresh)]
                self.assertLess(solid_difference(a,b),1e-7)
            # A corrupt output cannot be reused or passed to dependent edits.
            Path(early["first"]["output"]).write_bytes(b"incomplete")
            corrupt = execute()
            self.assertEqual([r["status"] for r in corrupt.values()], ["FAILED","BLOCKED","PASS"])
            self.assertTrue(corrupt["independent"]["reused"])
            steps[0]["edit"]["targets"][0]["entry"] = [10,6,5]
            failure = execute()
            self.assertEqual([r["status"] for r in failure.values()],["FAILED","BLOCKED","PASS"])
            self.assertTrue(failure["independent"]["reused"])

    def test_reference_identity_on_reopened_plate(self):
        import cadquery as cq
        from batch_creation import measure_cut
        from batch_replacement import interface

        row = dict(id="selected", xyz=[4,5,5], value=dict(diameter=4,depth=5,end="through"))
        axis = cq.Vector(0,0,-1)
        def plate(holes):
            shape = cq.Solid.makeBox(20,10,5)
            for x,radius in holes:
                shape = shape.cut(cq.Solid.makeCylinder(radius,5,cq.Vector(x,5,0)))
            return shape

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/"plate.step"
            right = plate([(14,1),(4,2)])
            wrong = plate([(4,1),(14,2)])
            self.assertAlmostEqual(right.Volume(),wrong.Volume())
            for shape,valid in ((right,True),(wrong,False)):
                cq.exporters.export(shape,str(path))
                saved = cq.importers.importStep(str(path)).val()
                if valid:
                    self.assertEqual(measure_cut(saved,row,axis)["diameter"],4)
                else:
                    with self.assertRaisesRegex(ValueError,"different geometry"):
                        measure_cut(saved,row,axis)
        box = cq.Solid.makeBox(10,10,2)
        corners = [[0,0,2],[10,0,2],[0,10,2]]
        face = interface(box,corners)[2]
        with self.assertRaisesRegex(ValueError,"ambiguous"):
            interface(cq.Compound.makeCompound([face,face.copy()]),corners)
        split = cq.Compound.makeCompound([cq.Solid.makeBox(5,10,2),
                                         cq.Solid.makeBox(5,10,2,cq.Vector(5,0,0))])
        with self.assertRaisesRegex(ValueError,"ambiguous"):
            interface(split,corners)
        with self.assertRaisesRegex(ValueError,"missing"):
            interface(box,[[0,0,3],[10,0,3],[0,10,3]])

    def test_step_mixed_occurrences(self):
        import cadquery as cq
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            box = cq.Solid.makeBox(2,3,4)
            model = cq.Assembly(name="assembly")
            model.add(box,name="block")
            model.add(box.Faces()[0],name="surface",loc=cq.Location((8,0,0)))
            path = root/"assembly.step"
            model.export(str(path))
            convert("step-inspect",path,root/"report.json")
            rows = json.loads((root/"report.json").read_text())["components"]
            by_name = {r["occurrence"][-1]:r["bodies"][0] for r in rows}
            self.assertEqual(by_name["block"]["classification"],"closed solid")
            self.assertAlmostEqual(by_name["block"]["volume_mm3"],24)
            self.assertEqual(by_name["surface"]["classification"],"surface geometry")
            self.assertTrue(by_name["surface"]["planes"])
            self.assertNotIn("volume_mm3",by_name["surface"])


@unittest.skipUnless(importlib.util.find_spec("numpy"), "requires NumPy for cylinder fit")
class MeshRepairTests(unittest.TestCase):
    def test_cylindrical_wall_and_added_cap(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            vertices = [(round(2*math.cos(i*math.pi/4),12),round(2*math.sin(i*math.pi/4),12),z)
                        for z in (0,3) for i in range(8)]
            walls, cap = [], []
            for i in range(8):
                j = (i+1)%8
                walls.extend([(i,j,j+8),(i,j+8,i+8)])
                if 0<i<7:
                    cap.append((8,i+8,j+8))
            def write(name,faces):
                path = root/name
                path.write_text("".join("v %s %s %s\n"%p for p in vertices)
                                +"".join("f %s %s %s\n"%tuple(i+1 for i in f) for f in faces))
                return path
            source = write("source.obj",walls)
            repaired = write("saved.obj",cap+list(reversed(walls)))
            result = compare(source,repaired,cylinder=dict(source_triangles=list(range(16)),axis=[0,0,1]))
            self.assertEqual(len(result["original_triangles"]),16)
            self.assertEqual(result["repair"]["saved_triangles"],list(range(6)))
            self.assertEqual(len(result["repair"]["original_boundary_edges_mm"]),8)
            self.assertAlmostEqual(result["fit"]["radius_mm"],2)
            self.assertLess(result["fit"]["maximum_sampled_radial_error_mm"],1e-10)
