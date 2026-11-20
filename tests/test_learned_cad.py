"""Regression cases for source-bound feature sequences and named sketch conflicts."""

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import learned_cad_provider as provider
import learned_cad_sequence as sequence
import learned_cad_solver as solver

FIXTURE = ROOT / "execution/modeling-capabilities/learned-completion"


class LearnedCadTest(unittest.TestCase):
    def test_generated_geometry_is_data_only(self):
        good = {
            "op": "cut",
            "shape": "circle",
            "diameter": 4,
            "depth": 5,
            "center": [0, 0, 0],
        }
        with self.assertRaises(ValueError):
            provider.expand(json.dumps([good]), "fixture", {})
        good["op"] = "add"
        self.assertEqual(
            provider.expand(json.dumps([good]), "fixture", {})["features"][0]["id"],
            "feature1",
        )
        with self.assertRaises(ValueError):
            provider.expand(json.dumps([dict(good, code="invalid")]), "fixture", {})
        with self.assertRaises(ValueError):
            provider.expand("[]", "fixture", {})
        with self.assertRaises(ValueError):
            provider.expand("null", "fixture", {})

    def test_inference_parameters_are_finite(self):
        for value in (float("nan"), float("inf"), True):
            with self.assertRaises(ValueError):
                sequence.finite(value)

    @unittest.skipUnless(
        importlib.util.find_spec("cadquery"), "requires optional CadQuery"
    )
    def test_edit_preserves_original_and_rejects_stale_source(self):
        source = FIXTURE / "text-sequence.json"
        original = json.loads(source.read_text())
        paths = {"prompt": FIXTURE / "prompt.txt"}
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            with self.assertRaisesRegex(ValueError, "Source revision mismatch"):
                sequence.run(source, directory / "stale", {"prompt": source})
            a = sequence.run(source, directory / "a", paths)
            original["parameters"]["diameter"]["value_mm"] = 10
            edited = directory / "edited.json"
            edited.write_text(json.dumps(original))
            b = sequence.run(edited, directory / "b", paths)
            self.assertTrue(a["geometry"]["valid"] and b["geometry"]["valid"])
            self.assertEqual(a["geometry"]["bounds_mm"], b["geometry"]["bounds_mm"])
            self.assertGreater(a["geometry"]["volume_mm3"], b["geometry"]["volume_mm3"])
            with self.assertRaises(FileExistsError):
                sequence.run(edited, directory / "a", paths)

    @unittest.skipUnless(
        importlib.util.find_spec("slvs"), "requires optional SolveSpace"
    )
    def test_native_constraint_handles_and_revision(self):
        a = FIXTURE / "conflicted-sketch.json"
        b = FIXTURE / "corrected-sketch.json"
        result = solver.run(a, b)
        self.assertEqual(
            set(result["before"]["failed_constraints"]),
            {"nominal-span", "alternate-span"},
        )
        self.assertEqual(result["after"]["degrees_of_freedom"], 0)
        self.assertEqual(result["after"]["points_mm"]["end"], [5.0, 0.0])
        self.assertEqual(
            solver.run(FIXTURE / "free-sketch.json")["before"]["degrees_of_freedom"], 1
        )
        with self.assertRaisesRegex(ValueError, "another original"):
            solver.run(FIXTURE / "free-sketch.json", b)
