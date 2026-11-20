"""Extract metric landmarks and dense CPU stereo surfaces from an aligned camera model."""

import argparse
import hashlib
import json
from pathlib import Path


def matrices(model, name):
    image = model.find_image_with_name(name)
    if image is None or not image.has_pose:
        raise ValueError("Missing aligned camera pose for " + name)
    camera = model.camera(image.camera_id)
    if camera.model.name not in ("PINHOLE", "SIMPLE_PINHOLE"):
        raise ValueError("Use undistorted pinhole images and matching camera model")
    intrinsic = camera.calibration_matrix().copy()
    # COLMAP measures the first pixel centre at (0.5, 0.5), OpenCV at (0, 0).
    intrinsic[:2, 2] -= 0.5
    return (
        intrinsic,
        image.cam_from_world().matrix(),
        (camera.width, camera.height),
    )


def triangulate(model, item):
    import numpy as np
    import cv2

    views = item["views"]
    if len(views) != 2 or views[0]["image"] == views[1]["image"]:
        raise ValueError("Use two distinct views of the same physical landmark")
    projections = []
    coordinates = []
    for view in views:
        k, pose, size = matrices(model, view["image"])
        uv = np.asarray(view["pixel"], dtype=float)
        if (
            uv.shape != (2,)
            or not np.isfinite(uv).all()
            or np.any(uv < 0)
            or np.any(uv >= size)
        ):
            raise ValueError("Landmark outside image")
        projections.append(k @ pose)
        coordinates.append(uv)

    def solve(a, b):
        pt = cv2.triangulatePoints(
            *projections, a.reshape(2, 1), b.reshape(2, 1)
        ).ravel()
        if abs(pt[3]) < 1e-12:
            raise ValueError("Triangulation at infinity")
        point = pt[:3] / pt[3]
        predictions = [p @ np.r_[point, 1] for p in projections]
        if any(q[2] <= 0 for q in predictions):
            raise ValueError("Landmark is behind a camera")
        return point, [q[:2] / q[2] for q in predictions]

    point, uv = solve(*coordinates)
    radius = float(item["pick_radius_px"])
    if not np.isfinite(radius) or radius < 0:
        raise ValueError("Invalid pixel pick radius")
    variants = []
    for i in range(4):
        for sign in [-1, 1]:
            trial = np.asarray(coordinates).copy()
            trial[i // 2, i % 2] += sign * radius
            candidate, _ = solve(*trial)
            variants.append(float(np.linalg.norm(candidate - point)) * 1000)
    return dict(
        world_m=point.tolist(),
        reprojection_errors_px=[
            float(np.linalg.norm(a - b)) for a, b in zip(uv, coordinates)
        ],
        max_single_coordinate_perturbation_mm=max(variants),
        pick_radius_px=radius,
    )


def dense_pair(model, source, pair, job, out, index):
    import cv2
    import numpy as np
    from registered_stereo import run
    import open3d as o3d

    names = [pair["left"], pair["right"]]
    (k1, p1, size), (k2, p2, size2) = [matrices(model, n) for n in names]
    if size != size2 or names[0] == names[1]:
        raise ValueError("Dense stereo requires distinct images of the same size")
    rot = p2[:, :3] @ p1[:, :3].T
    translation = p2[:, 3] - rot @ p1[:, 3]
    r1, r2, proj1, proj2, Q, _, _ = cv2.stereoRectify(
        k1,
        None,
        k2,
        None,
        size,
        rot,
        translation.reshape(3, 1),
        flags=cv2.CALIB_ZERO_DISPARITY,
        alpha=0,
    )
    if abs(proj2[1, 3]) > abs(proj2[0, 3]) or proj2[0, 3] >= 0:
        raise ValueError("Use a predominantly horizontal pair ordered left to right")
    directory = out / f"pair-{index}"
    directory.mkdir()
    rectified = []
    for i, (name, k, rect, p) in enumerate(
        zip(names, [k1, k2], [r1, r2], [proj1, proj2])
    ):
        src = cv2.imread(
            str(source / name), cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION
        )
        if src is None or src.shape[:2] != size[::-1]:
            raise ValueError("Source size differs from reconstruction for " + name)
        maps = cv2.initUndistortRectifyMap(k, None, rect, p, size, cv2.CV_32FC1)
        view = cv2.remap(src, *maps, cv2.INTER_LINEAR)
        rectified.append(view)
        if not cv2.imwrite(str(directory / f"{i}.png"), view):
            raise OSError("Cannot write rectified image")
    spec = dict(
        left="0.png",
        right="1.png",
        rectified=True,
        focal_px=proj1[0, 0],
        baseline_m=-proj2[0, 3] / proj2[0, 0],
        methods=["SGBM"],
        block_size=job["block_size"],
        num_disparities=job["num_disparities"],
    )
    manifest = directory / "pair.json"
    manifest.write_text(json.dumps(spec))
    run(manifest, directory / "depth")
    depth = np.load(directory / "depth/SGBM-depth-m.npy")
    valid = np.isfinite(depth) & (depth <= job["max_depth_m"])
    if not valid.any():
        raise ValueError("No dense observations within requested depth range")
    yy, xx = np.nonzero(valid)
    # OpenCV rectification uses image pixel centres at integer locations.
    z = depth[valid]
    x = (xx - proj1[0, 2]) * z / proj1[0, 0]
    y = (yy - proj1[1, 2]) * z / proj1[1, 1]
    camera_xyz = np.column_stack((x, y, z)) @ r1
    world = (camera_xyz - p1[:, 3]) @ p1[:, :3]
    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(world)
    cloud.colors = o3d.utility.Vector3dVector(rectified[0][valid][:, ::-1] / 255)
    return cloud


def verify_calibration(model_path, images, job, receipt):
    from camera_reconstruction import model_files

    raw = receipt.read_bytes()
    checked = json.loads(raw)
    if (
        checked.get("passed") is not True
        or checked.get("units") != "m"
        or not checked.get("model_files_sha256")
        or checked["model_files_sha256"] != model_files(model_path)
    ):
        raise ValueError(
            "Selected model differs from the checked metric camera solution"
        )
    names = {
        v["image"] for row in job.get("landmarks", {}).values() for v in row["views"]
    }
    for pair in job.get("pairs", []):
        names.update((pair["left"], pair["right"]))
    for name in names:
        if hashlib.sha256((images / name).read_bytes()).hexdigest() != checked[
            "input_sha256"
        ].get(name):
            raise ValueError(
                "Source image differs from the checked camera input: " + name
            )
    return hashlib.sha256(raw).hexdigest()


def run(model_path, images, spec, out, receipt=None):
    import pycolmap as pc

    job = json.loads(spec.read_text())
    calibration = verify_calibration(
        model_path, images, job, receipt or model_path.parent / "receipt.json"
    )
    model = pc.Reconstruction(model_path)
    out.mkdir(parents=True, exist_ok=False)
    landmarks = {
        n: triangulate(model, record) for n, record in job.get("landmarks", {}).items()
    }
    result = dict(
        units="m", calibration_receipt_sha256=calibration, landmarks=landmarks
    )
    if job.get("pairs"):
        import open3d as o3d
        import numpy as np
        from rgbd_surface import positive

        positive(job["max_depth_m"], "max_depth_m")
        voxel = positive(job["voxel_mm"], "voxel_mm") / 1000
        cloud = o3d.geometry.PointCloud()
        for i, pair in enumerate(job["pairs"]):
            cloud += dense_pair(model, images, pair, job, out, i)
        reduced = cloud.voxel_down_sample(voxel)
        target = out / "dense-m.ply"
        if not o3d.io.write_point_cloud(str(target), reduced):
            raise OSError("Failed to write dense point cloud")
        points = np.asarray(o3d.io.read_point_cloud(str(target)).points)
        if len(points) != len(reduced.points) or not np.isfinite(points).all():
            raise ValueError("Dense point cloud failed readback")
        result.update(
            raw_points=len(cloud.points),
            reopened_points=len(points),
            voxel_mm=job["voxel_mm"],
        )
    if not landmarks and not job.get("pairs"):
        raise ValueError("Specify landmarks or stereo pairs")
    (out / "receipt.json").write_text(
        json.dumps(result, indent=2, allow_nan=False) + "\n"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("aligned_model", "images", "spec", "new_output"):
        parser.add_argument(name, type=Path)
    parser.add_argument("--calibration-receipt", type=Path)
    args = parser.parse_args()
    run(
        args.aligned_model,
        args.images,
        args.spec,
        args.new_output,
        args.calibration_receipt,
    )
