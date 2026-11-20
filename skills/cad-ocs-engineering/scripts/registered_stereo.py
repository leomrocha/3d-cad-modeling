"""Recover metric depth from a rectified pair and score optional labelled reference regions."""

import argparse
import hashlib
import json
from pathlib import Path


def run(job_path, out):
    import cv2
    import numpy as np

    raw = job_path.read_bytes()
    spec = json.loads(raw)
    root = job_path.parent
    hashes = {}

    def load(side):
        path = root / spec[side]
        data = path.read_bytes()
        hashes[side] = hashlib.sha256(data).hexdigest()
        im = cv2.imdecode(
            np.frombuffer(data, np.uint8),
            cv2.IMREAD_GRAYSCALE | cv2.IMREAD_IGNORE_ORIENTATION,
        )
        if im is None:
            raise ValueError(f"Invalid image for {side}")
        return im

    left, right = load("left"), load("right")
    if left.shape != right.shape or spec["rectified"] is not True:
        raise ValueError(
            "Supply a registered, rectified left/right pair at the same resolution"
        )
    focal, baseline = float(spec["focal_px"]), float(spec["baseline_m"])
    count, block = spec["num_disparities"], spec["block_size"]
    if (
        not np.isfinite([focal, baseline]).all()
        or min(focal, baseline) <= 0
        or type(count) is not int
        or count <= 0
        or count % 16
        or type(block) is not int
        or block % 2 != 1
        or not 5 <= block <= 255
        or min(left.shape) < block
        or left.shape[1] <= count + block
    ):
        raise ValueError("Invalid scale, disparity range, image size or odd block size")
    methods = spec["methods"]
    if (
        not isinstance(methods, list)
        or not methods
        or any(m not in ("BM", "SGBM") for m in methods)
        or len(methods) != len(set(methods))
    ):
        raise ValueError("Supply a nonempty list of distinct stereo methods")
    reference = None
    if "reference" in spec:
        refpath = root / spec["reference"]
        hashes["reference"] = hashlib.sha256(refpath.read_bytes()).hexdigest()
        with np.load(refpath, allow_pickle=False) as archive:
            reference = archive["depth_m"]
            labels = archive["labels"]
        if reference.shape != left.shape or labels.shape != left.shape:
            raise ValueError("Reference depth and labels must match source image")
    out.mkdir(parents=True, exist_ok=False)
    results = {}
    for method in methods:
        if method == "BM":
            matcher = cv2.StereoBM_create(count, block)
        elif method == "SGBM":
            matcher = cv2.StereoSGBM_create(
                minDisparity=0,
                numDisparities=count,
                blockSize=block,
                P1=8 * block**2,
                P2=32 * block**2,
                uniquenessRatio=10,
                speckleWindowSize=0,
            )
        else:
            raise ValueError("Supported methods: BM and SGBM")
        disparity = matcher.compute(left, right).astype(float) / 16
        depth = np.full(left.shape, np.nan, dtype=np.float32)
        hits = disparity > 0
        depth[hits] = focal * baseline / disparity[hits]
        np.save(out / (method + "-depth-m.npy"), depth)
        scores = {}
        if reference is not None:
            from rgbd_surface import evaluate

            for label, name in spec["class_ids"].items():
                roi = (labels == int(label)) & np.isfinite(reference) & (reference > 0)
                scores[name] = evaluate(depth * 1000, reference * 1000, roi)
        results[method] = dict(
            valid_pixels=int(hits.sum()),
            depth_file=method + "-depth-m.npy",
            regions=scores,
        )
    receipt = dict(
        opencv=cv2.__version__,
        depth_units="m",
        input_sha256=hashes,
        spec_sha256=hashlib.sha256(raw).hexdigest(),
        methods=results,
    )
    (out / "receipt.json").write_text(
        json.dumps(receipt, indent=2, allow_nan=False) + "\n"
    )
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("job", type=Path)
    parser.add_argument("new_output", type=Path)
    args = parser.parse_args()
    run(args.job, args.new_output)
