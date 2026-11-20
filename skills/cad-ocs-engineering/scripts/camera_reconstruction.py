"""Recover camera poses from photographs and align them to surveyed camera centres in metres."""

import argparse
import hashlib
import json
from pathlib import Path


def model_files(path):
    """Fingerprint every reconstruction file used by a COLMAP binary or text model."""
    return {
        f.name: hashlib.sha256(f.read_bytes()).hexdigest()
        for f in sorted(path.iterdir())
        if f.suffix in (".bin", ".txt") and f.is_file()
    }


def run(manifest, output, dense=False):
    import numpy as np
    import pycolmap as pc

    raw = manifest.read_bytes()
    job = json.loads(raw)
    images = manifest.parent / job["image_directory"]
    names = job["images"]
    cameras = job["controls_m"]
    checks = job["checks_m"]
    if (
        len(names) != len(set(names))
        or len(cameras) < 3
        or not checks
        or set(cameras) & set(checks)
        or not set(cameras) | set(checks) <= set(names)
    ):
        raise ValueError(
            "Supply distinct images, three or more control centres and independent check centres"
        )
    check_xyz = np.array(list(checks.values()), dtype=float)
    if check_xyz.shape != (len(checks), 3) or not np.isfinite(check_xyz).all():
        raise ValueError(
            "Each independent check needs a finite 3D world position in metres"
        )
    refs = np.array(list(cameras.values()), dtype=float)
    if (
        refs.shape != (len(cameras), 3)
        or not np.isfinite(refs).all()
        or np.linalg.matrix_rank(refs - refs.mean(axis=0)) < 2
    ):
        raise ValueError("Control centres must span at least a plane")
    tolerance = float(job["check_tolerance_mm"])
    if not np.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("Invalid check tolerance")
    if dense and not pc.has_cuda:
        raise ValueError(
            "COLMAP PatchMatch requires a CUDA-enabled pycolmap runtime and GPU"
        )
    hashes = {
        name: hashlib.sha256((images / name).read_bytes()).hexdigest() for name in names
    }
    output.mkdir(parents=True, exist_ok=False)
    db = output / "features.db"
    reader = pc.ImageReaderOptions()
    if "pinhole" in job:
        params = job["pinhole"]
        if len(params) != 4 or not np.isfinite(params).all() or min(params[:2]) <= 0:
            raise ValueError(
                "Expected fx, fy, cx, cy in pixels for an undistorted image"
            )
        reader.camera_model = "PINHOLE"
        reader.camera_params = ",".join(map(str, params))
    extract = pc.FeatureExtractionOptions()
    extract.num_threads = 2
    pc.extract_features(
        db,
        images,
        image_names=names,
        camera_mode=pc.CameraMode.SINGLE,
        reader_options=reader,
        extraction_options=extract,
        device=pc.Device.cpu,
    )
    matches = pc.FeatureMatchingOptions()
    matches.num_threads = 2
    pc.match_exhaustive(db, matching_options=matches, device=pc.Device.cpu)
    opts = pc.IncrementalPipelineOptions()
    opts.num_threads = 2
    opts.random_seed = 107
    if "pinhole" in job:
        opts.ba_refine_focal_length = False
        opts.ba_refine_extra_params = False
        opts.mapper.abs_pose_refine_focal_length = False
        opts.mapper.abs_pose_refine_extra_params = False
    sparse = output / "submodels"
    sparse.mkdir()
    models = pc.incremental_mapping(db, images, sparse, options=opts)
    required = set(cameras) | set(checks)
    candidates = [
        m
        for m in models.values()
        if required <= {m.image(i).name for i in m.reg_image_ids()}
    ]
    if not candidates:
        raise ValueError(
            "No reconstructed submodel contains every control and independent check"
        )
    model = max(candidates, key=lambda m: m.num_reg_images())
    centres = {
        model.image(i).name: model.image(i).projection_center()
        for i in model.reg_image_ids()
    }
    source = np.asarray([centres[n] for n in cameras])
    if np.linalg.matrix_rank(source - source.mean(axis=0)) < 2:
        raise ValueError("Reconstructed control centres are collinear")
    transform = pc.estimate_sim3d(source, refs)
    if transform is None or not np.isfinite(transform.scale) or transform.scale <= 0:
        raise ValueError("Failed to align control centres")
    model.transform(transform)
    aligned = output / "aligned"
    aligned.mkdir()
    model.write(aligned)
    restored = pc.Reconstruction(aligned)
    centres = {
        restored.image(i).name: restored.image(i).projection_center()
        for i in restored.reg_image_ids()
    }
    errors = {
        name: float(np.linalg.norm(centres[name] - xyz) * 1000)
        for name, xyz in checks.items()
    }
    if not np.isfinite(list(errors.values())).all():
        raise ValueError("Nonfinite independent check")
    passed = max(errors.values()) <= tolerance
    receipt = dict(
        model_files_sha256=model_files(aligned),
        version=pc.__version__,
        units="m",
        input_sha256=hashes,
        manifest_sha256=hashlib.sha256(raw).hexdigest(),
        world_from_sparse=transform.matrix().tolist(),
        registered_images=restored.num_reg_images(),
        points=restored.num_points3D(),
        mean_reprojection_px=restored.compute_mean_reprojection_error(),
        independent_errors_mm=errors,
        check_tolerance_mm=tolerance,
        passed=passed,
    )
    (output / "receipt.json").write_text(
        json.dumps(receipt, indent=2, allow_nan=False) + "\n"
    )
    if not passed:
        raise ValueError(
            "Aligned model exceeds independent check tolerance; see receipt.json"
        )
    if dense:
        workspace = output / "dense"
        pc.undistort_images(workspace, aligned, images)
        pc.patch_match_stereo(workspace)
        pc.stereo_fusion(workspace / "fused.ply", workspace)
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("new_output", type=Path)
    parser.add_argument("--dense", action="store_true")
    args = parser.parse_args()
    run(args.manifest, args.new_output, args.dense)
