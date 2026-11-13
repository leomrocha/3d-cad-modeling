# Photographs and scans

[Documentation](README.md) · [Project](../README.md)

Status: reconstruction routes are documented proposals; calibrated 2D image tracing has a local Python helper.

## Inputs and scale

1. A photograph with reference dimensions can support calibrated points and outlines in a stated plane.
2. Overlapping photographs or video frames can support a camera solution and reconstructed surfaces.
3. Depth captures can supply point samples with sensor calibration and scale metadata.
4. Independent measured control points establish scale and check registration to a CAD or building frame.

## Proposed reconstruction route

1. Preserve the original images, camera metadata and measured controls.
2. Estimate camera poses and reconstruct a point cloud or mesh with an identified pipeline.
3. Register the reconstruction to the target frame and compare independent check points.
4. Fit or redraw required engineering features using the measured evidence.
5. Retain the reconstructed surface and the resulting CAD model as linked outputs with their own checks.

Photogrammetry preserves observed surface information. CAD remodeling expresses selected dimensions, planes, cylinders and interfaces as engineering geometry. Record the fitting method and residuals for each remodeled feature.

## Implemented image tracing

`calibrated_trace.py` maps supplied image points through an explicit pixel origin and signed scale for each axis. It returns coordinates and worst-case uncertainty bounds from the supplied point, origin and scale uncertainties. [Helper source](../scripts/calibrated_trace.py).

Related pages: [building models](building-models.md), [modeling workflow](modeling-workflow.md) and [tools](tools.md).
