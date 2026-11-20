import sys
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "scripts"), os.environ.get("NATIVE_READER_ROOT", str(Path(tempfile.gettempdir()) / "3dmodeling-native-reader"))]

from small_bms import compare_sat_sab


CASE = Path(__file__).resolve().parent / "fixtures" / "sat-sab-persistence"


class SmallBmsSavedGeometryTests(unittest.TestCase):
    def test_same_prism_matches_in_sat_and_reopened_sab(self):
        sat = (CASE / "before-save.sat").read_text()
        sab = (CASE / "after-reopen.sab").read_bytes()
        result = compare_sat_sab(sat, sab)
        self.assertEqual("PASS", result["result"])
        self.assertEqual(16, result["pre_save_unique_vertex_count"])
        self.assertEqual(16, result["reopened_unique_vertex_count"])
        self.assertTrue(result["topology"]["reciprocal_closed_partners"])
        self.assertEqual(["plane-surface"], result["surface_types"])

    def test_sat_transform_must_be_identity(self):
        sat = (CASE / "before-save.sat").read_text()
        sab = (CASE / "after-reopen.sab").read_bytes()
        altered = sat.replace("transform $-1 -1 1 0 0", "transform $-1 -1 1 0 1", 1)
        self.assertNotEqual(sat, altered)
        with self.assertRaisesRegex(ValueError, "Identity SAT transform required"):
            compare_sat_sab(altered, sab)

    def test_changed_sat_vertex_fails_with_identity_transform(self):
        sat = (CASE / "before-save.sat").read_text()
        sab = (CASE / "after-reopen.sab").read_bytes()
        lines = sat.splitlines()
        index = next(i for i, line in enumerate(lines) if line.startswith("point "))
        fields = lines[index].split()
        fields[4] = str(float(fields[4]) + 0.01)
        lines[index] = " ".join(fields)
        altered = "\n".join(lines) + "\n"
        result = compare_sat_sab(altered, sab)
        self.assertEqual("FAIL", result["result"])


if __name__ == "__main__":
    unittest.main()
