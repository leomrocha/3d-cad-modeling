import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import standard_screw


class ScrewSelectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.variant = dict(standard="ISO 4017", size="M6", head_form="external-hex",
                            thread_series="coarse", edition="2022", grade="A", pitch_mm=1, length_mm=20,
                            representation="nominal-envelope")
        row = dict(self.variant, source="synthetic row", lengths_mm=[20, 30],
                   head_height_mm=[3, 5], across_flats_mm=[9, 11], min_across_corners_mm=10)
        raw = json.dumps(row).encode()
        (self.root / "row.json").write_bytes(raw)
        self.request = dict(self.variant, reference=dict(
            row_file="row.json", sha256=hashlib.sha256(raw).hexdigest()))
        self.review = dict(evidence="synthetic source", variant=self.variant,
                           geometry=dict(one_valid_solid=True, coaxial=True, evidence="synthetic measurement",
                                         underhead_mm=20, shaft_diameter_mm=6, head_height_mm=4,
                                         across_flats_mm=10, across_corners_mm=11))
        candidate = dict(sha256="digest", locator="asset.dwg", private_source=self.review)
        mock = patch.object(standard_screw, "search_saved",
                            return_value={"unavailable": {"error": "offline"}, "model": {"candidates": [candidate]}})
        mock.start()
        self.addCleanup(mock.stop)

    def select(self):
        spec = self.root / "request.json"
        spec.write_text(json.dumps(self.request))
        return standard_screw.generate(self.root, spec, self.root / "out")

    def test_exact_reuse_without_generator(self):
        result = self.select()
        self.assertEqual(result["route"], "reuse")
        self.assertEqual(result["catalogue_failures"], {"unavailable": "offline"})

    def test_exposed_length_parameter(self):
        self.request["length_mm"] = 30
        self.review["length_parameter"] = dict(name="underhead", lengths_mm=[20, 30])
        result = self.select()
        self.assertEqual((result["route"], result["requested_mm"]),
                         ("modify-length-parameter", 30))

    def test_rejects_mismatched_row(self):
        self.request["size"] = "M8"
        with self.assertRaisesRegex(ValueError, "mismatch: size"):
            self.select()

    def test_rejects_mismatched_pitch(self):
        self.request["reference"]["pitch_mm"] = 0.75
        with self.assertRaisesRegex(ValueError, "pitch"):
            self.select()


    def test_bad_shaft_measurement_skips_asset_and_retries_cleanly(self):
        self.review["geometry"]["shaft_diameter_mm"] = 2
        with self.assertRaisesRegex(ValueError, "No qualified"):
            self.select()
        self.assertFalse((self.root / "out").exists())
        self.review["geometry"]["shaft_diameter_mm"] = 6
        self.assertEqual(self.select()["route"], "reuse")

    def test_rejects_missing_head_limits_before_reuse(self):
        path = self.root / "row.json"
        row = json.loads(path.read_bytes())
        del row["head_height_mm"]
        path.write_text(json.dumps(row))
        self.request["reference"]["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        with self.assertRaisesRegex(ValueError, "head_height_mm"):
            self.select()

    def test_rejects_grade_b(self):
        self.request["grade"] = "B"
        with self.assertRaisesRegex(ValueError, "grade"):
            self.select()

    def test_search_falls_back_to_second_installed_method(self):
        import catalogue_candidates
        from unittest.mock import Mock

        methods = [dict(probe="parts", name=name, search_cli="search.py") for name in ("a", "b")]
        config = dict(resources=[dict(id="parts", location=".", methods=methods)],
                      operations=[dict(resource="parts", name=name, usable=True) for name in ("a", "b")])
        lookup = Mock(side_effect=[OSError("unavailable"), {"candidates": []}])
        with patch.object(catalogue_candidates, "load", return_value=config), patch.object(
            catalogue_candidates, "lookup", lookup
        ):
            result = catalogue_candidates.search_saved(self.root, "M6")
        self.assertEqual(result["parts"]["method_errors"], ["a: unavailable"])
        self.assertEqual(lookup.call_count, 2)

    def test_retry_after_publication_requires_same_receipt_and_request(self):
        expected = self.select()
        receipt = self.root / "out" / "receipt.json"
        original = receipt.read_bytes()
        with patch.object(standard_screw.subprocess, "run", side_effect=AssertionError("unexpected provider call")):
            self.assertEqual(self.select(), expected)
        self.assertEqual(receipt.read_bytes(), original)
        self.request["job_id"] = "different-request"
        with self.assertRaisesRegex(ValueError, "differs"):
            self.select()
        self.assertEqual(receipt.read_bytes(), original)
        del self.request["job_id"]
        receipt.write_text(json.dumps(dict(expected, sha256="changed")))
        with self.assertRaisesRegex(ValueError, "differs"):
            self.select()
        self.assertEqual(json.loads(receipt.read_bytes())["sha256"], "changed")


    def test_exact_cosmetic_catalogue_asset_without_provider(self):
        self.request["representation"] = "cosmetic"
        self.variant.update(representation="cosmetic", cosmetic_shaft_diameter_mm=5.35)
        self.review["geometry"]["shaft_diameter_mm"] = 5.35
        self.assertEqual(self.select()["route"], "reuse")
