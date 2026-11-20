"""Run a local Transformers SAM checkpoint for one prompted source-image instance."""

from local_model_runtime import offline_model_libraries

import argparse
import hashlib
import io
import json
import math
from pathlib import Path
from time import perf_counter


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def predict(source, model_dir, prompt, parent=None, threads=2):
    offline_model_libraries()
    import torch
    import transformers
    from PIL import Image
    from transformers import SamModel, SamProcessor

    if threads < 1:
        raise ValueError("CPU thread count must be positive")
    torch.set_num_threads(threads)
    raw = source.read_bytes()
    source_hash = digest(raw)
    image = Image.open(io.BytesIO(raw)).convert("RGB")
    width, height = image.size
    key = prompt["id"]
    if not isinstance(key, str) or not key:
        raise ValueError("Provide an instance id")
    parent_hash = None
    if parent is not None:
        previous = parent.read_bytes()
        receipt = json.loads(previous)
        if receipt["source_sha256"] != source_hash or [
            i["id"] for i in receipt["instances"]
        ] != [key]:
            raise ValueError("Correction requires the same source and instance")
        parent_hash = digest(previous)

    def point(x, y):
        if not (
            math.isfinite(x) and math.isfinite(y) and 0 <= x < width and 0 <= y < height
        ):
            raise ValueError("Prompt coordinates must be inside the stored image")
        return [x, y]

    arguments = {}
    if "box" in prompt:
        x1, y1, x2, y2 = prompt["box"]
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Expected box as left, top, right, bottom")
        arguments["input_boxes"] = [[point(x1, y1) + point(x2, y2)]]
    if prompt.get("points"):
        points, labels = [], []
        for x, y, label in prompt["points"]:
            if label not in (0, 1):
                raise ValueError("Use 1 for foreground and 0 for background")
            points.append(point(x, y))
            labels.append(label)
        arguments.update(input_points=[[points]], input_labels=[[labels]])
    if not arguments:
        raise ValueError("Supply a box or labelled points")
    files = ("config.json", "preprocessor_config.json", "model.safetensors")
    hashes = {f: digest((model_dir / f).read_bytes()) for f in files}
    start = perf_counter()
    processor = SamProcessor.from_pretrained(model_dir, local_files_only=True)
    model = SamModel.from_pretrained(
        model_dir, local_files_only=True, use_safetensors=True
    ).eval()
    loaded = perf_counter()
    inputs = processor(images=image, return_tensors="pt", **arguments)
    with torch.inference_mode():
        output = model(**inputs, multimask_output=True)
    scores = output.iou_scores[0, 0]
    best = int(scores.argmax())
    masks = processor.post_process_masks(
        output.pred_masks, inputs["original_sizes"], inputs["reshaped_input_sizes"]
    )
    mask = masks[0][0, best].to(torch.uint8)
    if tuple(mask.shape) != (height, width):
        raise ValueError("Unexpected restored mask dimensions")
    return dict(
        provider="Transformers SamModel",
        checkpoint_sha256=hashes,
        runtime=dict(
            torch=torch.__version__,
            transformers=transformers.__version__,
            device="cpu",
            threads=threads,
        ),
        source_sha256=source_hash,
        provider_size_px=[width, height],
        source_from_provider=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        parent_response_sha256=parent_hash,
        prompt=prompt,
        model_scores=scores.tolist(),
        selected_candidate=best,
        elapsed_seconds=dict(
            load=loaded - start, inference_and_restore=perf_counter() - loaded
        ),
        instances=[dict(kind="mask", id=key, mask=mask.tolist())],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("source", "model_dir", "prompt", "output"):
        parser.add_argument(name, type=Path)
    parser.add_argument("--parent", type=Path)
    parser.add_argument("--threads", type=int, default=2)
    args = parser.parse_args()
    result = predict(
        args.source,
        args.model_dir,
        json.loads(args.prompt.read_text()),
        args.parent,
        args.threads,
    )
    encoded = json.dumps(result, allow_nan=False, separators=(",", ":"))
    with args.output.open("x") as handle:
        handle.write(encoded)
