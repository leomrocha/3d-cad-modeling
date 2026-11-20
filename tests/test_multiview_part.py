import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from multiview_part import infer  # noqa: E402


@unittest.skipUnless(importlib.util.find_spec("cv2"), "optional OpenCV")
class CalibratedMultiView(unittest.TestCase):
    def test_source_revision_wrong_scale_and_family(self):
        source = ROOT / "execution/modeling-capabilities/multiview-part/views.json"
        fixture = json.loads(source.read_text())
        for name in ("top", "front"):
            fixture[name]["path"] = str(source.parent / fixture[name]["path"])
        with tempfile.TemporaryDirectory() as tmp:
            job = Path(tmp) / "views.json"
            for change, expected in [
                ("family", "Declare"),
                ("sha", "revision"),
                ("scale", "held-out"),
                ("width", "disagree"),
            ]:
                data = json.loads(json.dumps(fixture))
                if change == "family":
                    data["family"] = "unspecified"
                elif change == "sha":
                    data["top"]["sha256"] = hashlib.sha256(b"another mask").hexdigest()
                elif change == "scale":
                    data["front"]["held_out_control"]["length_mm"] *= 2
                else:
                    for ctl in ("scale_control", "held_out_control"):
                        data["front"][ctl]["length_mm"] *= 2
                job.write_text(json.dumps(data))
                with (
                    self.subTest(change=change),
                    self.assertRaisesRegex(ValueError, expected),
                ):
                    infer(job)

    def test_held_out_layout_produces_editable_hole_sequence(self):
        seq, result = infer(
            ROOT / "execution/modeling-capabilities/multiview-part/views.json"
        )
        self.assertEqual(
            [f["operation"] for f in seq["features"]], ["add", "cut", "cut", "cut"]
        )
        self.assertIn("bore_2_diameter", seq["parameters"])
        self.assertLess(result["measurement"]["width_disagreement_mm"], 0.30)
