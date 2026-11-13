import sys
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "scripts"), os.environ.get("NATIVE_READER_ROOT", str(Path(tempfile.gettempdir()) / "3dmodeling-native-reader"))]

from small_bms import compare_sat_sab


CASE = ROOT / "execution/component-followups-2026-11-13/c054"


class SmallBmsSavedGeometryTests(unittest.TestCase):
    def test_actual_c054_sticker_body_survives_dwg_save_and_reopen(self):
        sat = (CASE / "c054-real-pre-save.sat").read_text()
        sab = (CASE / "c054-real-reopened.sab").read_bytes()
        result = compare_sat_sab(sat, sab)
        self.assertEqual("PASS", result["result"])
        self.assertEqual(16, result["pre_save_unique_vertex_count"])
        self.assertEqual(16, result["reopened_unique_vertex_count"])
        self.assertTrue(result["topology"]["reciprocal_closed_partners"])
        self.assertEqual(["cone-surface", "plane-surface"], result["surface_types"])

    def test_actual_case_requires_the_observed_identity_sat_transform(self):
        sat = (CASE / "c054-real-pre-save.sat").read_text()
        sab = (CASE / "c054-real-reopened.sab").read_bytes()
        altered = sat.replace("transform $-1 -1 1 0 0", "transform $-1 -1 1 0 1", 1)
        with self.assertRaises(ValueError):
            compare_sat_sab(altered, sab)

    def test_actual_pre_save_vertex_change_fails_with_transform_unchanged(self):
        sat = (CASE / "c054-real-pre-save.sat").read_text()
        sab = (CASE / "c054-real-reopened.sab").read_bytes()
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
