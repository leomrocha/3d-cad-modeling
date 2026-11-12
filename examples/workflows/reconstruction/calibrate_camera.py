#!/usr/bin/env python3
"""Reference checkerboard calibration using OpenCV; no image capture or scale guessing."""
import argparse
import glob
import json
import math
from pathlib import Path

import cv2
import numpy as np


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--images', nargs='+', required=True,
                    help='Image paths and/or glob patterns for views of the same checkerboard.')
    ap.add_argument('--inner-corners', nargs=2, type=int, metavar=('COLS', 'ROWS'), required=True,
                    help='Number of internal checkerboard corners, as printed by the board specification.')
    ap.add_argument('--square-size', type=float, required=True,
                    help='Measured physical side length of one square; never infer from pixels.')
    ap.add_argument('--unit', choices=('mm', 'cm', 'm', 'in'), required=True,
                    help='Unit used for square-size and target object coordinates.')
    ap.add_argument('--output', type=Path, required=True, help='Calibration JSON output path.')
    args = ap.parse_args()
    cols, rows = args.inner_corners
    if cols < 2 or rows < 2 or not math.isfinite(args.square_size) or args.square_size <= 0:
        ap.error('corner counts must be >=2 and square-size must be positive')
    paths = sorted({p for spec in args.images for p in glob.glob(spec)})
    if not paths:
        ap.error('no input images matched')
    input_paths = {Path(p).resolve() for p in paths}
    if args.output.resolve() in input_paths:
        ap.error('output path must not overwrite an input image')
    # OpenCV's calibration tutorial recommends at least ten pattern views.
    if len(paths) < 10:
        ap.error(f'found {len(paths)} views; provide at least 10 distinct target views as recommended by OpenCV')

    obj = np.zeros((rows * cols, 3), np.float32)
    obj[:, :2] = np.mgrid[0:cols, 0:rows].T.reshape(-1, 2) * args.square_size
    object_points, image_points, image_records = [], [], []
    image_size = None
    for name in paths:
        image = cv2.imread(name, cv2.IMREAD_COLOR)
        if image is None:
            raise SystemExit(f'cannot read image: {name}')
        size = (image.shape[1], image.shape[0])
        if image_size is not None and size != image_size:
            raise SystemExit(f'image size mismatch: {name} is {size}, expected {image_size}')
        image_size = size
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        found, corners = cv2.findChessboardCornersSB(
            gray, (cols, rows), flags=cv2.CALIB_CB_NORMALIZE_IMAGE)
        if not found:
            image_records.append({'image': str(Path(name).resolve()), 'used': False,
                                  'reason': 'checkerboard corners not detected'})
            continue
        object_points.append(obj.copy())
        image_points.append(corners.astype(np.float32))
        image_records.append({'image': str(Path(name).resolve()), 'used': True,
                              'corner_count': int(len(corners))})
    if len(object_points) < 10:
        raise SystemExit(f'only {len(object_points)} usable views; OpenCV tutorial recommends at least 10')

    rms, camera_matrix, distortion, rvecs, tvecs = cv2.calibrateCamera(
        object_points, image_points, image_size, None, None)
    if not math.isfinite(float(rms)) or not np.isfinite(camera_matrix).all() or not np.isfinite(distortion).all():
        raise SystemExit('calibration returned non-finite parameters or residuals')
    for rec, obj_i, img_i, rvec, tvec in zip(
            [x for x in image_records if x['used']], object_points, image_points, rvecs, tvecs):
        projected, _ = cv2.projectPoints(obj_i, rvec, tvec, camera_matrix, distortion)
        delta = projected.reshape(-1, 2) - img_i.reshape(-1, 2)
        rec['reprojection_rms_px'] = float(np.sqrt(np.mean(np.sum(delta * delta, axis=1))))
        rec['reprojection_max_px'] = float(np.max(np.linalg.norm(delta, axis=1)))
        rec['object_to_camera_rvec'] = np.asarray(rvec).reshape(-1).tolist()
        rec['object_to_camera_tvec'] = np.asarray(tvec).reshape(-1).tolist()
    result = {
        'method': 'OpenCV chessboard calibrateCamera + projectPoints residuals',
        'image_size_px': list(image_size),
        'checkerboard_inner_corners_cols_rows': [cols, rows],
        'square_size': args.square_size,
        'length_unit': args.unit,
        'camera_matrix': camera_matrix.tolist(),
        'distortion_coefficients': distortion.reshape(-1).tolist(),
        'calibration_rms_px': float(rms),
        'views': image_records,
        'interpretation': 'Calibration estimates camera intrinsics/distortion. Scene scale still needs explicit measured controls or a metric sensor; target units describe board poses.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
