"""Verify that model clients use the supplied destination and existing resources."""

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from learned_cad_provider import chat
from local_model_runtime import inference_endpoint, offline_model_libraries


class OfflineModels(unittest.TestCase):
    def test_supplied_server(self):
        for url in (
            "https://models.example.invalid/api",
            "http://192.0.2.4:9000/infer",
            "http://[::1]:8080/infer",
        ):
            self.assertEqual(inference_endpoint(url).geturl(), url)
        with patch("http.client.HTTPSConnection") as connect:
            connect.return_value.getresponse.return_value.read.return_value = b"{}"
            chat("https://models.example.invalid:9000/chat", {}, None, 1)
            connect.assert_called_once_with("models.example.invalid", 9000, timeout=1)

    def test_invalid_destinations(self):
        for url in ("file:///tmp/model", "http://user@server", "http://host/#fragment"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                inference_endpoint(url)

    def test_offline_settings_override_environment(self):
        with patch.dict(os.environ, HF_HUB_OFFLINE="0"):
            offline_model_libraries()
            self.assertEqual(os.environ["HF_HUB_OFFLINE"], "1")
            self.assertEqual(os.environ["TRANSFORMERS_OFFLINE"], "1")
            self.assertEqual(
                os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"], "True"
            )

    def test_missing_local_yolo_checkpoint_fails_before_import(self):
        from tempfile import TemporaryDirectory
        from vision_provider import local_yolo_response

        with (
            TemporaryDirectory() as job,
            patch.dict(sys.modules, {"ultralytics": None}),
        ):
            with self.assertRaises(FileNotFoundError):
                local_yolo_response(None, Path(job) / "unavailable.pt")

    def test_vision_posts_to_user_supplied_server_without_local_yolo(self):
        import importlib.util
        from tempfile import TemporaryDirectory

        if not all(importlib.util.find_spec(name) for name in ("PIL", "numpy")):
            self.skipTest("Pillow and NumPy required")
        from PIL import Image
        from vision_provider import run

        with TemporaryDirectory() as job:
            source = Path(job) / "image.png"
            Image.new("RGB", (5, 5)).save(source)
            config = dict(
                url="https://vision.example.invalid:8443/predict",
                model="deployed",
                format="yolo",
                coordinate_units="pixels",
                payload={"image": "$image_base64"},
            )
            with (
                patch.dict(sys.modules, {"ultralytics": None}),
                patch("vision_provider.build_opener") as opener,
            ):
                opened = opener.return_value.open
                opened.return_value.__enter__.return_value.read.return_value = b"[]"
                run(source, config, Path(job) / "result")
                self.assertEqual(opened.call_args.args[0].full_url, config["url"])
