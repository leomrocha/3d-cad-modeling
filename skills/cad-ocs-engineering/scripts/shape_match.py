"""Rank hashed mesh assets by partial-scan distances and named mating interfaces."""

import argparse
import json
import math
from pathlib import Path

from shape_recover import load_mesh


def points(value, minimum=1):
    import numpy as np

    xyz = np.asarray(value, dtype=float)
    if (
        xyz.ndim != 2
        or xyz.shape[1] != 3
        or len(xyz) < minimum
        or not np.isfinite(xyz).all()
    ):
        raise ValueError("Expected finite 3D coordinates in mm")
    return xyz


def rigid(value):
    import numpy as np

    matrix = np.array(value, dtype=float)
    if (
        matrix.shape != (4, 4)
        or not np.isfinite(matrix).all()
        or not np.allclose(matrix[3], [0, 0, 0, 1], atol=1e-8, rtol=0)
        or not np.allclose(matrix[:3, :3].T @ matrix[:3, :3], np.eye(3), atol=1e-6)
        or not np.isclose(np.linalg.det(matrix[:3, :3]), 1.0, atol=1e-6)
    ):
        raise ValueError("Expected a proper rigid world_from_candidate transform")
    return matrix


def nonnegative(value, name):
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError("Expected nonnegative finite " + name)
    return number


def unit_vector(value):
    import numpy as np

    vec = points([value])[0]
    length = np.linalg.norm(vec)
    if length <= 0:
        raise ValueError("A datum axis must be nonzero")
    return vec / length


def pose_from_anchors(anchors):
    import numpy as np

    local = points(anchors["candidate_mm"], 3)
    world = points(anchors["world_mm"], 3)
    if local.shape != world.shape:
        raise ValueError("Expected matching landmark correspondences")
    a = local - local.mean(axis=0)
    b = world - world.mean(axis=0)
    if min(np.linalg.matrix_rank(a), np.linalg.matrix_rank(b)) < 2:
        raise ValueError("Collinear anchors cannot define a 3D pose")
    u, _, vt = np.linalg.svd(a.T @ b)
    rotation = vt.T @ np.diag([1, 1, np.linalg.det(vt.T @ u.T)]) @ u.T
    pose = np.eye(4)
    pose[:3, :3] = rotation
    pose[:3, 3] = world.mean(axis=0) - rotation @ local.mean(axis=0)
    return rigid(pose)


def global_pose(mesh, observations, voxel, seeds):
    import numpy as np
    import open3d as o3d

    reg = o3d.pipelines.registration
    if not math.isfinite(voxel) or voxel <= 0:
        raise ValueError("Expected a positive feature sampling distance")
    if not seeds or len(seeds) > 8 or not all(type(s) is int for s in seeds):
        raise ValueError("Specify one to eight repeatable registration seeds")

    def prepare(cloud):
        down = cloud.voxel_down_sample(voxel)
        if len(down.points) < 6:
            raise ValueError("Too few distinct samples for global registration")
        down.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(2 * voxel, 30))
        # Orient neighbouring normals consistently before describing local surfaces.
        down.orient_normals_consistent_tangent_plane(min(15, len(down.points) - 1))
        features = reg.compute_fpfh_feature(
            down, o3d.geometry.KDTreeSearchParamHybrid(5 * voxel, 100)
        )
        return down, features

    scan = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(observations))
    patches, pf = prepare(scan)
    o3d.utility.random.seed(seeds[0])
    count = min(100000, max(1000, math.ceil(mesh.get_surface_area() / voxel**2 * 4)))
    model, mf = prepare(mesh.sample_points_uniformly(count))
    # Source is the partial scan: the absent part of the target should not drag ICP.
    poses = []
    for seed in seeds:
        o3d.utility.random.seed(seed)
        initial = reg.registration_ransac_based_on_feature_matching(
            patches,
            model,
            pf,
            mf,
            False,
            2 * voxel,
            reg.TransformationEstimationPointToPoint(False),
            3,
            [
                reg.CorrespondenceCheckerBasedOnEdgeLength(0.9),
                reg.CorrespondenceCheckerBasedOnDistance(2 * voxel),
            ],
            reg.RANSACConvergenceCriteria(50000, 0.995),
        )
        if initial.fitness > 0:
            refine = reg.registration_icp(
                patches,
                model,
                2 * voxel,
                initial.transformation,
                reg.TransformationEstimationPointToPlane(),
            )
            if refine.fitness > 0:
                pose = rigid(np.linalg.inv(refine.transformation))
                poses.append(pose)
    return poses


def mate_check(model, target, pose):
    import numpy as np

    if {model["kind"], target["kind"]} != {"pin", "bore"}:
        return {"passed": False, "reason": "Expected one pin and one bore"}
    point = pose[:3, :3] @ points([model["center_mm"]])[0] + pose[:3, 3]
    axis = unit_vector(target["axis"])
    delta = point - points([target["center_mm"]])[0]
    axial = float(delta @ axis)
    lateral = float(np.linalg.norm(delta - axial * axis))
    sign = {"parallel": 1, "opposed": -1}[target["direction"]]
    alignment = np.clip(
        sign * (pose[:3, :3] @ unit_vector(model["axis"])) @ axis, -1, 1
    )
    angle = math.degrees(math.acos(alignment))
    dm, dt = [nonnegative(row["diameter_mm"], "diameter") for row in (model, target)]
    if min(dm, dt) <= 0:
        raise ValueError("A mating diameter must be positive")
    clearance = dt - dm if model["kind"] == "pin" else dm - dt
    lo, hi = map(float, target["diametral_clearance_mm"])
    if not (math.isfinite(lo) and math.isfinite(hi) and lo <= hi):
        raise ValueError("Invalid diametral clearance interval")
    passed = (
        lo <= clearance <= hi
        and abs(axial) <= nonnegative(target["axial_limit_mm"], "axial limit")
        and lateral <= nonnegative(target["lateral_limit_mm"], "lateral limit")
        and angle <= nonnegative(target["angle_limit_deg"], "angle limit")
    )
    return dict(
        axial_mm=axial,
        lateral_mm=lateral,
        angle_deg=angle,
        diametral_clearance_mm=clearance,
        passed=bool(passed),
    )


def unique_ranked_poses(ranked):
    """Keep the best-ranked transform in each asset-local numerical neighbourhood."""
    import numpy as np

    # The Frobenius rotation distance is 2 sqrt(2) sin(relative angle/2).
    rotation_limit = 2 * math.sqrt(2) * math.sin(math.radians(1e-6) / 2)
    retained = []
    by_asset = {}
    for row in ranked:
        pose = np.asarray(row["world_from_candidate"])
        group = by_asset.setdefault(row["id"], [])
        for representative, kept in group:
            displacement = np.linalg.norm(pose[:3, 3] - representative[:3, 3])
            rotation = np.linalg.norm(pose[:3, :3] - representative[:3, :3])
            if displacement <= 1e-6 and rotation <= rotation_limit:
                kept["hypothesis_count"] += 1
                break
        else:
            kept = dict(row, hypothesis_count=1)
            group.append((pose, kept))
            retained.append(kept)
    return retained


def match(job, directory):
    import numpy as np
    import open3d as o3d

    witnesses = points(job["world_check_points_mm"])
    tolerance = nonnegative(job["max_point_error_mm"], "witness error limit")
    ranked, rejected = [], []
    seen = set()
    for row in job["candidates"]:
        key = row["id"]
        if not isinstance(key, str) or not key or key in seen:
            raise ValueError("Distinct catalogue asset IDs required")
        seen.add(key)
        mesh, digest = load_mesh(directory / row["path"], row["unit"])
        if digest != row["sha256"]:
            raise ValueError(f"Mesh hash changed for {key}")
        poses = [rigid(p) for p in row.get("poses", [])]
        poses.extend(pose_from_anchors(a) for a in row.get("anchors", []))
        if "registration" in job:
            cfg = job["registration"]
            poses.extend(
                global_pose(
                    mesh, points(cfg["world_scan_mm"], 6), cfg["voxel_mm"], cfg["seeds"]
                )
            )
        if not poses:
            rejected.append({"id": key, "reason": "No pose supplied or recovered"})
            continue
        scene = o3d.t.geometry.RaycastingScene()
        scene.add_triangles(o3d.t.geometry.TriangleMesh.from_legacy(mesh))
        for pose in poses:
            local = (witnesses - pose[:3, 3]) @ pose[:3, :3]
            errors = (
                scene.compute_distance(local.astype(np.float32)).numpy().astype(float)
            )
            if not np.isfinite(errors).all():
                raise ValueError("Invalid surface distance")
            checks = []
            for target in job.get("mates", []):
                name = target["name"]
                declared = row.get("interfaces", {}).get(name)
                if declared is None:
                    checks.append(
                        {
                            "name": name,
                            "passed": False,
                            "reason": "No corresponding interface datum",
                        }
                    )
                else:
                    checks.append({"name": name, **mate_check(declared, target, pose)})
            worst = float(errors.max())
            ranked.append(
                dict(
                    id=key,
                    sha256=digest,
                    world_from_candidate=pose.tolist(),
                    rms_mm=float(np.sqrt((errors**2).mean())),
                    max_mm=worst,
                    witness_count=len(errors),
                    mates=checks,
                    passed=worst <= tolerance
                    and all(c.get("passed", False) for c in checks),
                )
            )
    ranked.sort(key=lambda row: (not row["passed"], row["rms_mm"]))
    ranked = unique_ranked_poses(ranked)
    accepted = [r for r in ranked if r["passed"]]
    candidates = sorted({r["id"] for r in accepted})
    return dict(
        status="no-match"
        if not accepted
        else "ambiguous"
        if len(accepted) > 1
        else "one-tested-pose",
        candidate_ids=candidates,
        ranked=ranked,
        rejected=rejected,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("job", type=Path)
    parser.add_argument("new_result", type=Path)
    args = parser.parse_args()
    result = match(json.loads(args.job.read_text()), args.job.parent)
    with args.new_result.open("x") as stream:
        json.dump(result, stream, allow_nan=False, indent=2)
        stream.write("\n")
