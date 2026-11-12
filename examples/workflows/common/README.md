# Reference lengths against exported model points

The [comparison helper](/home/leo/projects/3dmodeling/examples/workflows/common/check_control_distances.py) compares supplied reference lengths with coordinates exported from a named CAD or reconstruction revision. It reports signed residuals in millimetres and separate fit/check statistics. Dependencies: Python standard library.

## Inputs

1. Model-points JSON: `length_unit` (`m`, `cm`, `mm`), `model_revision`, `coordinate_frame`, and `points` containing unique `id` values and three finite `xyz` coordinates.
2. Reference JSON: `distances` containing unique `id`, `from`/`to` point IDs, positive `value`, explicit `unit`, `role` (`fit` or `check`) and nonempty `source`.
3. The referenced coordinates must represent the same features as the named reference lengths. Capture and measurement provenance establish which controls are independent of fitting.

## Command

```sh
python3 /home/leo/projects/3dmodeling/examples/workflows/common/check_control_distances.py \
  --references /absolute/path/reference-lengths.json \
  --model-points /absolute/path/exported-model-points.json \
  --out /absolute/path/distance-report.json \
  --require-check-controls
```

The helper preserves both inputs, records their hashes, converts stated units to metres for calculation and reports residuals in millimetres. It compares supplied point coordinates; CAD/scan extraction and frame alignment belong to their respective workflow steps.

## Verification

[Unit tests](/home/leo/projects/3dmodeling/examples/workflows/common/test_control_distances.py) exercise mixed input units, separate fit/check statistics, duplicate-point rejection, required assessment controls, finite coordinates and source requirements. The fixtures are synthetic numbers for software verification.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 /home/leo/projects/3dmodeling/examples/workflows/common/test_control_distances.py
```
