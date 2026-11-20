import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from bearing_variant import evaluate, FAMILY


class BearingVariantTests(unittest.TestCase):
    def setUp(self):
        self.fixture = ROOT / "execution/modeling-capabilities/bearing-variant/catalogue-result.json"

    def test_six_requests_through_catalogue_cli(self):
        for closure, sides, expected in (
            ("shield", 1, "Z"), ("shield", 2, "ZZ"),
            ("non-contact-seal", 1, "V"), ("non-contact-seal", 2, "VV"),
            ("contact-seal", 1, "DU"), ("contact-seal", 2, "DDU"),
        ):
            with self.subTest(closure=closure, sides=sides):
                raw = subprocess.check_output([sys.executable, ROOT / "scripts/bearing_variant.py",
                                               self.fixture, "--base", "6205", "--closure", closure,
                                               "--sides", str(sides)])
                rows = json.loads(raw)["sources"]["fixture"]
                self.assertEqual([r["id"] for r in rows if r["status"] == "fields-match"],
                                 ["fixture-nsk-6205" + expected.lower()])
                self.assertEqual([r["designation"] for r in rows if r["status"] == "needs-evidence"],
                                 ["6205", "6205DDUC3"])

    def test_incomplete_conflicting_and_separate_family_evidence(self):
        for changed, evidence, expected in (
            ({"family": None}, "row", "needs-evidence"),
            ({"suffix": "VV"}, "row", "needs-evidence"),
            ({"family": "angular-contact"}, "row", "different-variant"),
            ({}, "", "needs-evidence"),
            ({"designation": "6205-DDU"}, "row", "fields-match"),
        ):
            with self.subTest(changed=changed, evidence=evidence):
                variant = dict(manufacturer="NSK", family=FAMILY, designation="6205DDU")
                variant.update(changed)
                candidate = dict(id="fixture", private_source=dict(variant=variant, evidence=evidence))
                self.assertEqual(evaluate(candidate, "6205", "contact-seal", 2)["status"], expected)
