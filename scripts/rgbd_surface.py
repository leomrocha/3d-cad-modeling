"""Fuse registered RGB-D frames, reopen the mesh, and evaluate held-out depth by region."""

import argparse
import hashlib
import json
import math
from pathlib import Path
from time import perf_counter


def positive(value, name):
    if type(value) not in (int, float) or not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")
    return float(value)


def source_file(root, name, hashes):
    path = root / name
    with path.open("rb") as stream:
        hashes[name] = hashlib.file_digest(stream, "sha256").hexdigest()
    return path


def evaluate(predicted, reference, region):
    import numpy as np

    hits = region & np.isfinite(predicted)
    errors = np.abs(predicted[hits] - reference[hits])
    count = int(region.sum())
    return dict(
        reference_pixels=count,
        hits=int(hits.sum()),
        coverage=float(hits.sum() / count) if count else None,
        median_abs_mm=float(np.median(errors)) if errors.size else None,
        p95_abs_mm=float(np.percentile(errors, 95)) if errors.size else None,
    )


def run(manifest, output):
    import numpy as np
    import open3d as o3d

    raw = manifest.read_bytes()
    job = json.loads(raw)
    root = manifest.parent
    camera = np.array(job["camera_matrix"], dtype=float)
    if (
        camera.shape != (3, 3)
        or not np.isfinite(camera).all()
        or not np.allclose(camera[2], [0, 0, 1])
        or camera[0, 1]
        or camera[1, 0]
        or min(camera[0, 0], camera[1, 1]) <= 0
    ):
        raise ValueError(
            "Expected pinhole camera matrix for registered, undistorted frames"
        )
    width, height = job["size_px"]
    if any(type(i) is not int or i <= 0 for i in [width, height]):
        raise ValueError("Expected positive integer width and height")
    scale = positive(job["depth_units_per_m"], "depth scale")
    limit = positive(job["max_depth_m"], "maximum depth")
    voxel = positive(job["voxel_mm"], "voxel length")
    frames = job["frames"]
    if {f["role"] for f in frames} != {"integrate", "check"}:
        raise ValueError("Supply both integration and held-out check frames")
    ids = [f["id"] for f in frames]
    if not all(isinstance(i, str) and i for i in ids) or len(set(ids)) != len(ids):
        raise ValueError("Each frame needs a distinct ID")
    hashes = {}
    depth_roles = {}
    poses = {}
    for frame in frames:
        pose = np.array(frame["world_to_camera"], dtype=float)
        if (
            pose.shape != (4, 4)
            or not np.isfinite(pose).all()
            or not np.allclose(pose[3], [0, 0, 0, 1])
            or not np.allclose(pose[:3, :3].T @ pose[:3, :3], np.eye(3), atol=1e-5)
            or not np.isclose(np.linalg.det(pose[:3, :3]), 1)
        ):
            raise ValueError(
                "Expected rigid world-to-camera transform with translation in metres"
            )
        poses[frame["id"]] = pose
        source_file(root, frame["depth"], hashes)
        digest = hashes[frame["depth"]]
        if depth_roles.setdefault(digest, frame["role"]) != frame["role"]:
            raise ValueError(
                "Same depth image used for integration and held-out checking"
            )
    volume = o3d.t.geometry.VoxelBlockGrid(
        ("tsdf", "weight", "color"),
        (o3d.core.float32,) * 3,
        ((1,), (1,), (3,)),
        voxel / 1000,
        16,
        1000,
    )
    intrinsic = o3d.core.Tensor(camera)

    def read_image(name):
        path = source_file(root, name, hashes)
        image = o3d.io.read_image(str(path))
        if np.asarray(image).shape[:2] != (height, width):
            raise ValueError(f"Frame size mismatch for {name}")
        return image

    start = perf_counter()
    for frame in frames:
        if frame["role"] == "integrate":
            z = o3d.t.geometry.Image.from_legacy(read_image(frame["depth"]))
            color = o3d.t.geometry.Image.from_legacy(read_image(frame["color"]))
            pose = o3d.core.Tensor(poses[frame["id"]])
            blocks = volume.compute_unique_block_coordinates(
                z, intrinsic, pose, scale, limit
            )
            volume.integrate(blocks, z, color, intrinsic, pose, scale, limit)
    mesh = volume.extract_triangle_mesh(weight_threshold=0.0).to_legacy()
    if mesh.is_empty() or not mesh.has_triangles():
        raise ValueError("No triangulated surface")
    output.mkdir(parents=True, exist_ok=False)
    target = output / "surface-m.ply"
    if not o3d.io.write_triangle_mesh(str(target), mesh):
        raise OSError("Mesh write failed")
    restored = o3d.io.read_triangle_mesh(str(target))
    if len(restored.triangles) != len(mesh.triangles):
        raise ValueError("Mesh readback triangle count changed")
    elapsed = perf_counter() - start
    scene = o3d.t.geometry.RaycastingScene()
    scene.add_triangles(o3d.t.geometry.TriangleMesh.from_legacy(restored))
    checks = {}
    for frame in frames:
        if frame["role"] == "check":
            rays = scene.create_rays_pinhole(camera, poses[frame["id"]], width, height)
            predicted = scene.cast_rays(rays)["t_hit"].numpy() * 1000
            reference = (
                np.asarray(read_image(frame["depth"])).astype(float) * 1000 / scale
            )
            valid = (reference > 0) & (reference < limit * 1000)
            metrics = {"whole_view": evaluate(predicted, reference, valid)}
            for label, name in frame.get("region_masks", {}).items():
                mask = np.asarray(read_image(name))
                if mask.ndim != 2 or label == "whole_view":
                    raise ValueError(
                        "Each labelled region needs its own scalar mask and name"
                    )
                metrics[label] = evaluate(predicted, reference, valid & (mask != 0))
            checks[frame["id"]] = metrics
    result = dict(
        manifest_sha256=hashlib.sha256(raw).hexdigest(),
        inputs_sha256=hashes,
        mesh="surface-m.ply",
        mesh_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
        units="m",
        triangles=len(restored.triangles),
        open3d=o3d.__version__,
        voxel_mm=voxel,
        depth_units_per_m=scale,
        elapsed_through_reopen_s=elapsed,
        held_out=checks,
    )
    (output / "receipt.json").write_text(
        json.dumps(result, indent=2, allow_nan=False) + "\n"
    )
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("new_output", type=Path)
    args = parser.parse_args()
    run(args.manifest, args.new_output)
