import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from orthographic_checks import compare_landmark


class DrawingViews(unittest.TestCase):
    def test_saved_asymmetric_landmark_and_reversed_side(self):
        receipt = Path(__file__).resolve().parent / "fixtures/orthographic-checks/views.json"
        sources = json.loads(receipt.read_text())
        views = {}
        for name, view in sources.items():
            point = view["measurement"]
            views[name] = dict(zip(view["axes"], zip(point["coordinates"], point["uncertainty_worst_case"])))
        result = compare_landmark(views)
        self.assertTrue(result["consistent"])
        self.assertEqual([c["axis"] for c in result["comparisons"]], ["X", "Y", "Z"])
        mirror = sources["side"]["mirrored_feature"]
        views["side"]["Y"] = (mirror["coordinates"][0], mirror["uncertainty_worst_case"][0])
        failures = [c for c in compare_landmark(views)["comparisons"] if not c["consistent"]]
        self.assertEqual([(c["axis"], set(c["views"])) for c in failures], [("Y", {"top", "side"})])

    def test_exact_interval_boundary_and_invalid_uncertainty(self):
        views = {"front": {"X": (10, 0.25), "Z": (1, 0)}, "top": {"X": (10.5, 0.25), "Y": (3, 0)}}
        self.assertTrue(compare_landmark(views)["consistent"])
        views["top"]["X"] = (10.5, -0.25)
        with self.assertRaises(ValueError):
            compare_landmark(views)
