"""The provider route still restores source coordinates when OpenCV is absent."""
import hashlib
import importlib.util
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from image_observations import normalize


@unittest.skipUnless(all(importlib.util.find_spec(m) for m in ("PIL", "numpy")),
                     "Pillow and NumPy required for image normalization")
class WithoutOpenCV(unittest.TestCase):
    def test_rotated_mask_and_point_in_source_pixels(self):
        from PIL import Image

        stream = io.BytesIO()
        Image.new("L", (6, 5)).save(stream, format="PNG")
        raw = stream.getvalue()
        receipt = dict(source_sha256=hashlib.sha256(raw).hexdigest(),
                       provider="fixture", provider_size_px=[3, 2],
                       source_from_provider=[[0, -1, 4], [1, 0, 1], [0, 0, 1]],
                       instances=[dict(id="a", kind="mask", mask=[[0, 1, 0], [1, 0, 0]]),
                                  dict(id="b", kind="point", points=[[2, 1]])])
        with patch.dict(sys.modules, {"cv2": None}):
            result, png = normalize(raw, receipt)
        mask = result["instances"][0]["mask"]
        self.assertEqual({(x, y) for y, row in enumerate(mask)
                          for x, pixel in enumerate(row) if pixel}, {(4, 2), (3, 1)})
        self.assertEqual(result["instances"][1]["points_px"], [[3, 3]])
        with Image.open(io.BytesIO(png)) as overlay:
            self.assertEqual(overlay.getpixel((4, 2)), (0, 170, 0))
