import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from bearing_variant import evaluate, FAMILY


class BearingVariantTests(unittest.TestCase):
    def setUp(self):
        self.fixture = ROOT / "execution/modeling-capabilities/bearing-variant/catalogue-result.json"

    def run_matcher(self, *args, closure="contact-seal", sides=2, check=True):
        return subprocess.run(
            [sys.executable, ROOT / "scripts/bearing_variant.py", *args,
             "--base", "6205", "--closure", closure, "--sides", str(sides)],
            text=True, capture_output=True, check=check,
        )

    def test_six_requests_through_catalogue_receipt_cli(self):
        for closure in ("shield", "contact-seal", "non-contact-seal"):
            for sides in (1, 2):
                with self.subTest(closure=closure, sides=sides):
                    result = json.loads(self.run_matcher(self.fixture, closure=closure, sides=sides).stdout)
                    rows = result["sources"]["fixture"]
                    matches = [row for row in rows if row["status"] == "fields-match"]
                    expected_count = 3 if (closure, sides) == ("contact-seal", 2) else 1
                    self.assertEqual(len(matches), expected_count)
                    for match in matches:
                        self.assertEqual(match["catalogue_source"], "fixture")
                        self.assertIn("closure", match["evidence"])
                    self.assertEqual([row["designation"] for row in rows if row["status"] == "needs-evidence"],
                                     ["6205", "6205DDUC3"])

    def test_other_and_missing_manufacturer_match_and_shield_fails(self):
        result = json.loads(self.run_matcher(self.fixture).stdout)
        rows = {row["id"]: row for row in result["sources"]["fixture"]}
        other = rows["fixture-other-6205-2rs"]
        self.assertEqual(other["status"], "fields-match")
        self.assertEqual(other["manufacturer"], "OTHER")
        self.assertEqual(other["evidence"]["closure"], "Synthetic exact part-number source")
        self.assertEqual(rows["fixture-no-manufacturer"]["status"], "fields-match")
        self.assertNotIn("manufacturer", rows["fixture-no-manufacturer"])
        shield = rows["fixture-nsk-6205z"]
        self.assertEqual(shield["status"], "different-variant")
        self.assertEqual(shield["mismatches"], {"closure": "shield", "sides": 1})

    def test_missing_conflicting_and_separate_family_evidence(self):
        for changed, expected, missing in (
            ({"family": None}, "needs-evidence", ["family"]),
            ({"family": "angular-contact"}, "different-variant", []),
            ({"sides": None}, "needs-evidence", ["sides"]),
            ({"designation_evidence": dict(designation="6205DDU", source="Documented row", sides=1)}, "needs-evidence", []),
            ({}, "fields-match", []),
        ):
            with self.subTest(changed=changed):
                variant = dict(family=FAMILY, designation="6205DDU", closure="contact-seal", sides=2)
                variant.update(changed)
                candidate = dict(id="fixture", private_source=dict(variant=variant, evidence="row"))
                result = evaluate(candidate, "6205", "contact-seal", 2)
                self.assertEqual(result["status"], expected)
                self.assertEqual(result["missing"], missing)

    def test_suffix_without_evidence_or_with_other_designation_remains_unresolved(self):
        candidate = dict(id="fixture", family=FAMILY, designation="6205DDU", evidence="row",
                         designation_evidence=dict(designation="6305DDU", closure="contact-seal",
                                                   sides=2, source="Different part"))
        result = evaluate(candidate, "6205", "contact-seal", 2)
        self.assertEqual(result["status"], "needs-evidence")
        self.assertEqual(result["missing"], ["closure", "sides"])

    def test_saved_catalogue_queries_two_sources_and_preserves_unavailable_status(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            search = root / "search.py"
            search.write_text(
                "import json, pathlib, sys\n"
                "assert sys.argv[-2:] == ['--', '6205']\n"
                "records = json.loads((pathlib.Path(sys.argv[2])/'catalogue.json').read_text())\n"
                "print(json.dumps([dict(row, exact=True) for row in records if row['name'] == '6205 bearing']))\n"
            )
            resources, operations = [], []
            for name, manufacturer, usable in (("cad-models", "OTHER", True), ("shop", None, True),
                                                ("unavailable", None, False)):
                data = root / name
                data.mkdir()
                row = dict(id=name + "-bearing", name="6205 bearing" if name == "cad-models" else "Bearing",
                           family=FAMILY, part_number="6205X", closure="contact-seal", sides=2)
                if manufacturer:
                    row["manufacturer"] = manufacturer
                (data / "catalogue.json").write_text(json.dumps([row]))
                (data / "catalogue.sqlite").write_bytes(b"synthetic search index")
                method = dict(name="search", probe="parts", search_cli=str(search))
                resources.append(dict(id=name, location=str(data), methods=[method]))
                operations.append(dict(resource=name, name="search", usable=usable, reason="Missing snapshot"))
            config = root / "operations.json"
            config.write_text(json.dumps(dict(version=2, resources=resources, operations=operations)))
            process = self.run_matcher("--catalogue", config, check=False)
            self.assertEqual(process.returncode, 1, process.stderr)
            sources = json.loads(process.stdout)["sources"]
            for name in ("cad-models", "shop"):
                self.assertEqual(sources[name][0]["status"], "fields-match")
                self.assertEqual(sources[name][0]["evidence"]["closure"]["catalogue_source"], name)
            self.assertNotIn("manufacturer", sources["shop"][0])
            self.assertEqual(sources["unavailable"], {"error": "Missing snapshot"})
