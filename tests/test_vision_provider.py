"""Check actual intake contracts for model boxes, path masks and restored model logits."""

import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import vision_provider as provider

HAS_VISION = all(importlib.util.find_spec(m) for m in ("PIL", "cv2", "numpy"))


@unittest.skipUnless(HAS_VISION, "image runtime required")
class VisionProviderTest(unittest.TestCase):
    def test_qwen_nested_reply_and_coordinates(self):
        cfg = dict(
            model="qwen-test",
            format="qwen",
            coordinate_units="normalized1000",
            response_path=["choices", 0, "message", "content"],
        )
        response = {
            "choices": [
                {
                    "message": {
                        "content": '```json\n[{"label":"nut","bbox_2d":[200,100,800,900]}]\n```'
                    }
                }
            ]
        }
        got = provider.decode(response, cfg, "hash", (100, 40))
        self.assertEqual(
            got["instances"][0]["points"], [[20, 4], [80, 4], [80, 36], [20, 36]]
        )
        cfg.update(provider_size_px=[20, 20])
        with self.assertRaisesRegex(ValueError, "inverse resize"):
            provider.decode(response, cfg, "hash", (100, 40))

    def test_yolo_segments_and_empty(self):
        cfg = dict(model="detect", format="yolo", coordinate_units="normalized")
        row = dict(
            name="pin",
            box=dict(x1=0.1, y1=0.2, x2=0.6, y2=0.9),
            segments=dict(x=[0.1, 0.6, 0.6], y=[0.2, 0.9, 0.2]),
        )
        objs = provider.decode([row], cfg, "hash", (80, 20))["instances"]
        self.assertEqual(objs[1]["points"], [[8, 4], [48, 18], [48, 4]])
        self.assertEqual(provider.decode([], cfg, "hash", (80, 20))["instances"], [])
        row["segments"]["x"].append(0.8)
        with self.assertRaises(ValueError):
            provider.decode([row], cfg, "hash", (80, 20))

    def test_source_bound_detector_to_sam_box(self):
        from vision_provider_sam2 import grounded_prompt

        obs = {
            "source_sha256": "abc",
            "size_px": [10, 8],
            "instances": [
                {
                    "id": "part-1",
                    "kind": "box",
                    "points_px": [[0, 0], [10, 0], [10, 8], [0, 8]],
                }
            ],
        }
        prompt = {"id": "plate", "box_observation_id": "part-1"}
        self.assertEqual(
            grounded_prompt(prompt, obs, "abc", 10, 8)["box"], [0, 0, 9, 7]
        )
        with self.assertRaisesRegex(ValueError, "another source"):
            grounded_prompt(prompt, obs, "obsolete", 10, 8)

    def test_lisa_multi_instance_logits(self):
        cfg = dict(model="reasoner", format="lisa", response_path=["pred_masks"])
        planes = [[[1, 0], [-1, 1]], [[0, -1], [2, 0]]]
        obs = provider.decode(dict(pred_masks=planes), cfg, "hash", (2, 2))["instances"]
        self.assertEqual(obs[0]["mask"], [[1, 0], [0, 1]])
        self.assertEqual(obs[1]["mask"], [[0, 0], [1, 0]])
        with self.assertRaisesRegex(ValueError, "finite"):
            provider.decode(dict(pred_masks=[[[float("nan")]]]), cfg, "hash", (1, 1))

    @unittest.skipUnless(
        importlib.util.find_spec("torch"), "optional LISA tensor runtime"
    )
    def test_lisa_model_evaluate_handoff(self):
        import torch

        class PreparedModel:
            def evaluate(self, clip, image, tokens, resize, original, **kwargs):
                if (resize, original) != ([(4, 4)], [(2, 2)]):
                    raise AssertionError("Image sizes lost")
                return tokens, [
                    torch.tensor(
                        [[[1.0, -1.0], [-2.0, 0.0]], [[-1.0, 0.0], [1.0, 2.0]]]
                    )
                ]

        output = provider.evaluate_lisa(
            PreparedModel(),
            None,
            None,
            torch.tensor([[1, 2, 3]]),
            (4, 4),
            (2, 2),
            object(),
        )
        got = provider.decode(
            output,
            dict(model="lisa-contract", format="lisa", response_path=["pred_masks"]),
            "hash",
            (2, 2),
        )
        self.assertEqual(output["token_ids"], [1, 2, 3])
        self.assertEqual(
            [obj["mask"] for obj in got["instances"]],
            [[[1, 0], [0, 0]], [[0, 0], [1, 1]]],
        )

    @unittest.skipUnless(importlib.util.find_spec("cairosvg"), "optional CairoSVG")
    def test_moondream_box_relative_path_and_hole(self):
        import numpy as np

        cfg = dict(model="segment", format="moondream", instance_id="washer")
        path = "M0 0H1V1H0Z M.25 .25V.75H.75V.25Z"
        record = provider.decode(
            dict(path=path, bbox=dict(x_min=0.25, y_min=0.25, x_max=0.75, y_max=0.75)),
            cfg,
            "hash",
            (80, 40),
        )
        mask = np.asarray(record["instances"][0]["mask"])
        self.assertEqual(mask.sum(), 600)
        self.assertEqual((mask[0, 0], mask[12, 25], mask[20, 40]), (0, 1, 0))

    def test_offline_cli_source_binding_and_overlay(self):
        from PIL import Image

        with tempfile.TemporaryDirectory() as tmp:
            job = Path(tmp)
            image = job / "source.png"
            Image.new("RGB", (10, 8)).save(image)
            reply = job / "data.json"
            reply.write_text('{"objects":[]}')
            cfg = dict(
                model="source-test",
                format="instances",
                response_path=["objects"],
                source_sha256="stale",
            )
            with self.assertRaisesRegex(ValueError, "matching"):
                provider.run(image, cfg, job / "result", reply)
            cfg["source_sha256"] = hashlib.sha256(image.read_bytes()).hexdigest()
            provider.run(image, cfg, job / "result", reply)
            result = json.loads((job / "result/observations.json").read_text())
            self.assertEqual(result["instances"], [])
            self.assertTrue((job / "result/overlay.png").is_file())
            with self.assertRaises(FileExistsError):
                provider.run(image, cfg, job / "result", reply)
