"""Check drawing text and metric hole locations with controlled raster inputs."""

import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from image_observations import normalize
from raster_features import projection, trace
from raster_text import recognize


@unittest.skipUnless(
    importlib.util.find_spec("cv2") and importlib.util.find_spec("numpy"),
    "requires local OpenCV and NumPy",
)
class DrawingSkillInputTests(unittest.TestCase):
    def test_recognizes_dimension_and_maps_crop_origin(self):
        for module in ("paddle", "paddleocr"):
            if not importlib.util.find_spec(module):
                self.skipTest(f"requires local {module}")
        model_dir = os.environ.get("CAD_OCR_MODEL_DIR")
        if not model_dir:
            self.skipTest("set CAD_OCR_MODEL_DIR to an existing local model directory")
        model = Path(model_dir)
        if not (model / "inference.pdiparams").is_file():
            self.skipTest("CAD_OCR_MODEL_DIR is missing inference.pdiparams")

        import cv2
        import numpy as np

        image = np.full((64, 230, 3), 255, np.uint8)
        cv2.putText(
            image, "12.00 mm", (8, 46), cv2.FONT_HERSHEY_SIMPLEX, 1.3,
            (0, 0, 0), 2, cv2.LINE_AA,
        )
        raw = cv2.imencode(".png", image)[1].tobytes()
        observed, _ = normalize(raw, recognize(raw, [1, 1, 230, 64], model))

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "recognized-dimension.json"
            output.write_text(json.dumps(observed))
            rows = json.loads(output.read_text())["instances"]

        self.assertTrue(rows, "OCR returned no dimension")
        self.assertEqual(rows[0]["points_px"][0], [1, 1])
        self.assertEqual(rows[0]["text"].replace(" ", ""), "12.00mm")

    def test_reported_hole_centres_use_drawing_millimetres(self):
        import cv2
        import numpy as np

        holes = ((10, (88, 88), (17, 23)), (6, (208, 132), (47, 12)))
        image = np.zeros((201, 281), np.uint8)
        cv2.rectangle(image, (20, 20), (260, 180), 255, -1)
        for diameter, pixel, _ in holes:
            cv2.circle(image, pixel, diameter * 2, 0, -1)
        cv2.rectangle(image, (164, 48), (212, 64), 0, -1)
        raw = cv2.imencode(".png", image)[1].tobytes()
        controls = dict(
            source_sha256=hashlib.sha256(raw).hexdigest(),
            pixels=[[20, 180], [260, 180], [260, 20], [20, 20]],
            plane_mm=[[0, 0], [60, 0], [60, 40], [0, 40]],
            held_pixels=[[76, 136], [232, 76]],
            held_mm=[[14, 11], [53, 26]],
            limit_mm=0.13,
        )
        report, _ = trace(raw, 127, controls=controls)
        inner_loops = [loop for loop in report["loops"] if loop["role"] == "hole"]
        self.assertEqual(len(inner_loops), 3)
        centers = [
            loop["ellipse_candidate"]["center_px"]
            for loop in inner_loops if "ellipse_candidate" in loop
        ]
        observed_pixels = []
        for diameter, pixel, _ in holes:
            matches = [center for center in centers if math.dist(center, pixel) < 0.1]
            self.assertEqual(len(matches), 1, f"{diameter} mm hole at {pixel} px")
            observed_pixels.append(matches[0])

        measured = projection(observed_pixels, np.array(report["plane"]["forward"]))
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "handoff.json"
            output.write_text(json.dumps({"bore_centers_mm": measured.round(6).tolist()}))
            saved = json.loads(output.read_text())["bore_centers_mm"]

        self.assertEqual(len(saved), len(holes))
        for (diameter, _, expected), actual in zip(holes, saved, strict=True):
            self.assertLessEqual(
                math.dist(actual, expected), controls["limit_mm"],
                f"{diameter} mm hole: expected {expected} mm, reported {actual} mm",
            )
