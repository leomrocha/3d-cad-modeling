"""Run a local SAM 2 image checkpoint with box/point prompts and optional prior logits."""

from local_model_runtime import offline_model_libraries

import argparse
import base64
import hashlib
import io
import json
import math
from pathlib import Path
from time import perf_counter
import zlib

from sam_mask import digest


def grounded_prompt(prompt, observations, source_hash, width, height):
    """Resolve one source-frame detection into a pixel-centre SAM prompt."""
    identifier = prompt["box_observation_id"]
    if "box" in prompt:
        raise ValueError("Choose either a grounded observation or a supplied box")
    if observations["source_sha256"] != source_hash or observations["size_px"] != [
        width,
        height,
    ]:
        raise ValueError("Grounded detection belongs to another source or frame")
    matching = [
        i
        for i in observations["instances"]
        if i["id"] == identifier and i["kind"] == "box"
    ]
    if len(matching) != 1:
        raise ValueError("Require exactly one matching box observation")
    points = matching[0]["points_px"]
    if len(points) != 4 or any(
        len(p) != 2 or not all(math.isfinite(v) for v in p) for p in points
    ):
        raise ValueError("Expected four finite source-frame box corners")
    xs, ys = zip(*points)
    return dict(
        prompt,
        box=[
            max(0, min(xs)),
            max(0, min(ys)),
            min(width - 1, max(xs)),
            min(height - 1, max(ys)),
        ],
    )


def predict(source, model_dir, prompt, parent=None, threads=2, grounding=None):
    offline_model_libraries()
    import numpy as np
    from PIL import Image
    import torch
    import transformers
    from transformers import Sam2Model, Sam2Processor

    if threads <= 0:
        raise ValueError("Use a positive CPU thread count")
    raw = source.read_bytes()
    source_hash = digest(raw)
    image = Image.open(io.BytesIO(raw)).convert("RGB")
    width, height = image.size
    grounding_hash = None
    if grounding:
        source_observations = grounding.read_bytes()
        prompt = grounded_prompt(
            prompt, json.loads(source_observations), source_hash, width, height
        )
        grounding_hash = digest(source_observations)
    identifier = prompt.get("id")
    if not isinstance(identifier, str) or not identifier:
        raise ValueError("Provide an instance ID")

    def xy(x, y):
        if not all(isinstance(v, (float, int)) and math.isfinite(v) for v in (x, y)):
            raise ValueError("Finite source-pixel coordinates required")
        if not (0 <= x < width and 0 <= y < height):
            raise ValueError("Prompt must lie within the original image")
        return [x, y]

    args = {}
    if "box" in prompt:
        x1, y1, x2, y2 = prompt["box"]
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Expected ordered box corners")
        args["input_boxes"] = [[xy(x1, y1) + xy(x2, y2)]]
    if prompt.get("points"):
        points, labels = [], []
        for x, y, label in prompt["points"]:
            if label not in (0, 1):
                raise ValueError("Point label must be foreground 1 or background 0")
            points.append(xy(x, y))
            labels.append(label)
        args.update(input_points=[[points]], input_labels=[[labels]])
    if not args:
        raise ValueError("Provide a box or labelled points")
    file_names = (
        "config.json",
        "model.safetensors",
        "preprocessor_config.json",
        "processor_config.json",
    )
    files = {}
    for name in file_names:
        with (model_dir / name).open("rb") as f:
            files[name] = hashlib.file_digest(f, "sha256").hexdigest()
    prior_hash = None
    prior_logits = None
    if parent:
        previous = parent.read_bytes()
        record = json.loads(previous)
        if (
            record["source_sha256"] != source_hash
            or record["checkpoint_sha256"] != files
            or [i["id"] for i in record["instances"]] != [identifier]
        ):
            raise ValueError(
                "Correction requires the same source, instance and checkpoint"
            )
        prior_hash = digest(previous)
        state = record["selected_logits"]
        shape = state["shape"]
        if len(shape) != 2 or any(type(x) != int or not 0 < x <= 2048 for x in shape):
            raise ValueError("Invalid selected-logit shape")
        size = 4 * math.prod(shape)
        decoder = zlib.decompressobj()
        floats = decoder.decompress(
            base64.b64decode(state["zlib_f32le"], validate=True), size + 1
        )
        if (
            not decoder.eof
            or decoder.unused_data
            or len(floats) != size
            or digest(floats) != state["sha256"]
        ):
            raise ValueError("Invalid selected-logit payload")
        array = np.frombuffer(floats, dtype="<f4").reshape(shape).copy()
        if not np.isfinite(array).all():
            raise ValueError("Nonfinite previous logits")
        prior_logits = torch.from_numpy(array)[None, None]
    torch.set_num_threads(threads)
    start = perf_counter()
    processor = Sam2Processor.from_pretrained(model_dir, local_files_only=True)
    model = Sam2Model.from_pretrained(
        model_dir, local_files_only=True, use_safetensors=True
    ).eval()
    loaded = perf_counter()
    inputs = processor(images=image, return_tensors="pt", **args)
    with torch.inference_mode():
        output = model(**inputs, input_masks=prior_logits, multimask_output=True)
    scores = output.iou_scores[0, 0]
    best = int(scores.argmax())
    masks = processor.post_process_masks(output.pred_masks, inputs["original_sizes"])
    mask = masks[0][0, best].to(torch.uint8)
    if tuple(mask.shape) != (height, width):
        raise ValueError("Invalid restored mask frame")
    logits = output.pred_masks[0, 0, best].cpu().numpy().astype("<f4")
    state = logits.tobytes()
    return dict(
        source_sha256=source_hash,
        provider="Transformers Sam2Model",
        runtime=dict(
            transformers=transformers.__version__,
            torch=torch.__version__,
            threads=threads,
            device="cpu",
        ),
        checkpoint_sha256=files,
        parent_response_sha256=prior_hash,
        provider_size_px=[width, height],
        source_from_provider=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        prompt=prompt,
        grounding_sha256=grounding_hash,
        model_scores=scores.tolist(),
        selected_candidate=best,
        selected_logits=dict(
            shape=list(logits.shape),
            sha256=digest(state),
            zlib_f32le=base64.b64encode(zlib.compress(state)).decode("ascii"),
        ),
        elapsed_seconds=dict(
            load=loaded - start, inference_and_restore=perf_counter() - loaded
        ),
        instances=[dict(id=identifier, kind="mask", mask=mask.tolist())],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("source", "model_dir", "prompt", "output"):
        parser.add_argument(name, type=Path)
    parser.add_argument("--grounding", type=Path)
    parser.add_argument("--parent", type=Path)
    parser.add_argument("--threads", type=int, default=2)
    args = parser.parse_args()
    result = predict(
        args.source,
        args.model_dir,
        json.loads(args.prompt.read_text()),
        args.parent,
        args.threads,
        args.grounding,
    )
    with args.output.open("x") as f:
        json.dump(result, f, allow_nan=False, separators=(",", ":"))
