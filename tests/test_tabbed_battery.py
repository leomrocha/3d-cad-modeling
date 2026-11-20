"""Check planar recess boundaries with an authored feature payload."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from feature_checks import planar_boundary_pattern


class RecessPatternTests(unittest.TestCase):
    def setUp(self):
        self.centres = [[0, 0], [8, 0]]
        self.components = [
            {"bounds": {"min": [x - 2, y - 1, 5], "max": [x + 2, y + 1, 5]},
             "closed_degree_two": True}
            for x, y in self.centres
        ]
        self.features = {"planar_boundary_components": [
            {"plane_normal": [0, 0, 1], "plane_offset": 5, "components": self.components}
        ]}

    def pattern(self, level=5, centres=None):
        return planar_boundary_pattern(
            "recesses", self.features, 2, level, [4, 2],
            self.centres if centres is None else centres, 1e-6,
        )

    def test_closed_recesses_match_expected_pattern(self):
        result = self.pattern()
        self.assertEqual(result["result"], "PASS")
        self.assertEqual(len(result["observed"]), 2)

    def test_shifted_recess_pattern_is_detected(self):
        self.assertEqual(self.pattern(centres=[[1, 0], [9, 0]])["result"], "FAIL")

    def test_missing_native_recess_boundary_is_detected(self):
        self.components.pop()
        self.assertEqual(self.pattern()["result"], "FAIL")

    def test_wrong_floor_level_is_detected(self):
        self.assertEqual(self.pattern(level=6)["result"], "FAIL")

    def test_open_native_boundary_is_detected(self):
        self.components[0]["closed_degree_two"] = False
        self.assertEqual(self.pattern()["result"], "FAIL")


if __name__ == "__main__":
    unittest.main()
