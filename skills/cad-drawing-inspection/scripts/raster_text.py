"""Read one source-linked dimension crop with caller-supplied local PaddleOCR weights."""

import argparse
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import time


def recognize(raw, bounds, model_dir):
    import cv2
    import numpy as np
    from paddleocr import TextRecognition

    model_dir = Path(model_dir).resolve(strict=True)
    weights = model_dir / "inference.pdiparams"
    with weights.open("rb") as stream:
        model_hash = hashlib.file_digest(stream, "sha256").hexdigest()
    image = cv2.imdecode(
        np.frombuffer(raw, dtype=np.uint8),
        cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION,
    )
    if image is None:
        raise ValueError("Readable original image required")
    x0, y0, x1, y1 = bounds
    if not (0 <= x0 < x1 <= image.shape[1] and 0 <= y0 < y1 <= image.shape[0]):
        raise ValueError("Crop must lie within the stored source pixels")
    start = time.monotonic()
    model = TextRecognition(
        model_name=model_dir.name,
        model_dir=str(model_dir),
        device="cpu",
        enable_mkldnn=False,
        cpu_threads=1,
    )
    (prediction,) = model.predict(image[y0:y1, x0:x1].copy())
    w, h = x1 - x0, y1 - y0
    return dict(
        source_sha256=hashlib.sha256(raw).hexdigest(),
        provider=dict(
            model=model_dir.name,
            weights_sha256=model_hash,
            paddleocr=version("paddleocr"),
            device="cpu",
        ),
        provider_size_px=[w, h],
        source_from_provider=[[1, 0, x0], [0, 1, y0], [0, 0, 1]],
        instances=[
            dict(
                id="text-1",
                kind="text",
                text=prediction["rec_text"],
                points=[[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]],
                score=float(prediction["rec_score"]),
            )
        ],
        elapsed_s=time.monotonic() - start,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("model", type=Path)
    parser.add_argument(
        "--crop",
        type=int,
        nargs=4,
        metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
        required=True,
    )
    args = parser.parse_args()
    print(
        json.dumps(recognize(args.source.read_bytes(), args.crop, args.model), indent=2)
    )
