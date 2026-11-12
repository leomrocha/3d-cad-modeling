#!/usr/bin/env python3
"""Reference source-to-target point-cloud ICP registration with explicit initialization."""
import argparse
import json
import math
from pathlib import Path

import numpy as np
import open3d as o3d


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source', type=Path, required=True, help='Source point cloud (PLY).')
    ap.add_argument('--target', type=Path, required=True, help='Target point cloud (PLY).')
    ap.add_argument('--initial-transform', type=Path, required=True,
                    help='JSON with source_to_target 4x4 matrix; axes/units must match cloud metadata.')
    ap.add_argument('--max-correspondence-distance', type=float, required=True,
                    help='ICP distance threshold in the cloud coordinate length unit.')
    ap.add_argument('--unit', choices=('mm', 'cm', 'm', 'in'), required=True)
    ap.add_argument('--max-iterations', type=int, default=30)
    ap.add_argument('--point-to-plane', action='store_true', help='Use point-to-plane; requires normals below.')
    ap.add_argument('--normal-radius', type=float,
                    help='Neighborhood radius in coordinate units, required for point-to-plane normal estimation.')
    ap.add_argument('--normal-max-nn', type=int, default=30)
    ap.add_argument('--output-report', type=Path, required=True, help='JSON report with transform and fit metrics.')
    ap.add_argument('--output-source-ply', type=Path, required=True,
                    help='Transformed derivative; original source and target files remain untouched.')
    args = ap.parse_args()
    if not math.isfinite(args.max_correspondence_distance) or args.max_correspondence_distance <= 0 or args.max_iterations < 1:
        ap.error('distance must be positive and max-iterations >=1')
    if args.point_to_plane and (args.normal_radius is None or not math.isfinite(args.normal_radius) or args.normal_radius <= 0):
        ap.error('--point-to-plane requires a positive --normal-radius')
    if args.normal_max_nn < 1:
        ap.error('--normal-max-nn must be >=1')
    inputs = {p.resolve() for p in (args.source, args.target, args.initial_transform)}
    outputs = {args.output_report.resolve(), args.output_source_ply.resolve()}
    if len(inputs) < 3:
        ap.error('source, target and initial-transform must be separate files')
    if len(outputs) != 2:
        ap.error('report and transformed-cloud outputs must be separate files')
    if inputs & outputs:
        ap.error('output paths must not overwrite source, target or initial-transform inputs')
    init_doc = json.loads(args.initial_transform.read_text(encoding='utf-8'))
    init = np.asarray(init_doc['source_to_target'], dtype=float)
    if init.shape != (4, 4) or not np.all(np.isfinite(init)):
        ap.error('source_to_target must be a finite 4x4 matrix')
    if not np.allclose(init[3], [0, 0, 0, 1], atol=1e-8):
        ap.error('transform last row must be [0, 0, 0, 1]')
    rotation = init[:3, :3]
    if not np.allclose(rotation.T @ rotation, np.eye(3), rtol=0.0, atol=1e-6):
        ap.error('initial transform rotation must be orthonormal (rigid; no scale or shear)')
    if not math.isclose(float(np.linalg.det(rotation)), 1.0, rel_tol=0.0, abs_tol=1e-6):
        ap.error('initial transform rotation determinant must be +1')

    source = o3d.io.read_point_cloud(str(args.source))
    target = o3d.io.read_point_cloud(str(args.target))
    if source.is_empty() or target.is_empty():
        raise SystemExit('source and target PLY must each contain points')
    if args.point_to_plane:
        search = o3d.geometry.KDTreeSearchParamHybrid(radius=args.normal_radius, max_nn=args.normal_max_nn)
        source.estimate_normals(search)
        target.estimate_normals(search)
        estimator = o3d.pipelines.registration.TransformationEstimationPointToPlane()
        method = 'point_to_plane'
    else:
        estimator = o3d.pipelines.registration.TransformationEstimationPointToPoint()
        method = 'point_to_point'
    criteria = o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=args.max_iterations)
    result = o3d.pipelines.registration.registration_icp(
        source, target, args.max_correspondence_distance, init, estimator, criteria)
    if (len(result.correspondence_set) == 0 or not math.isfinite(float(result.fitness))
            or not math.isfinite(float(result.inlier_rmse))
            or not np.isfinite(result.transformation).all()):
        raise SystemExit('ICP returned no finite correspondence result; no output files written')
    transformed = o3d.geometry.PointCloud(source)
    transformed.transform(result.transformation)
    args.output_source_ply.parent.mkdir(parents=True, exist_ok=True)
    args.output_report.parent.mkdir(parents=True, exist_ok=True)
    if not o3d.io.write_point_cloud(str(args.output_source_ply), transformed):
        raise SystemExit(f'failed writing transformed derivative: {args.output_source_ply}')
    report = {
        'method': method,
        'source_path': str(args.source.resolve()),
        'target_path': str(args.target.resolve()),
        'transform_direction': 'source_to_target',
        'coordinate_unit': args.unit,
        'initial_transform': init.tolist(),
        'final_transform': result.transformation.tolist(),
        'max_correspondence_distance': args.max_correspondence_distance,
        'max_iterations': args.max_iterations,
        'fitness': float(result.fitness),
        'inlier_rmse': float(result.inlier_rmse),
        'inlier_rmse_unit': args.unit,
        'correspondence_count': int(len(result.correspondence_set)),
        'source_point_count': int(len(source.points)),
        'target_point_count': int(len(target.points)),
        'transformed_source_derivative': str(args.output_source_ply.resolve()),
        'interpretation': 'ICP refines the supplied source-to-target initial transform. Clouds must have compatible scale; fitness and inlier RMSE describe participating correspondences, not independent dimensional accuracy.'
    }
    args.output_report.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
