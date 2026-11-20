"""A stale mesh frame or unchecked camera model cannot silently supply metric landmarks."""

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from calibrated_views import verify_calibration
from camera_reconstruction import model_files


class CameraHandoff(unittest.TestCase):
    def test_reject_changed_camera_model_source_image_and_failed_alignment(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            model = root / "aligned"
            model.mkdir()
            (model / "cameras.bin").write_bytes(b"first calibration")
            (root / "left.png").write_bytes(b"image bytes")
            receipt = root / "receipt.json"
            job = {"landmarks": {"corner": {"views": [{"image": "left.png"}]}}}
            record = {
                "units": "m",
                "passed": True,
                "model_files_sha256": model_files(model),
                "input_sha256": {
                    "left.png": hashlib.sha256(b"image bytes").hexdigest()
                },
            }
            receipt.write_text(json.dumps(record))
            verify_calibration(model, root, job, receipt)
            (root / "left.png").write_bytes(b"revision")
            with self.assertRaisesRegex(ValueError, "image differs"):
                verify_calibration(model, root, job, receipt)
            (model / "cameras.bin").write_bytes(b"other calibration")
            with self.assertRaisesRegex(ValueError, "model differs"):
                verify_calibration(model, root, job, receipt)
            record.update(passed=False, model_files_sha256=model_files(model))
            receipt.write_text(json.dumps(record))
            with self.assertRaisesRegex(ValueError, "model differs"):
                verify_calibration(model, root, job, receipt)
