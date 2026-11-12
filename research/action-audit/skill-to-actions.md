# Proposed skills linked to reviewed action procedures

Date: 12 November 2026. Status: proposed packaging map for the fifteen workflow skills already listed in the [skill catalogue](/home/leo/projects/3dmodeling/skills/README.md) and [implementation plan](/home/leo/projects/3dmodeling/research/implementation-plan.md). The existing local OCS skill supplies its documented current capability. The other rows group detailed implementation specifications and existing software dependencies.

1. **Read an action contract:** each linked point records input/output, source evidence, supported software/API, agent interpretation, user decisions, ordered procedure, validation, recovery, resources and proposed helper interface.
2. **Choose execution:** agent-led, combined software/agent, software with exception handling and complete-software options are conditional on the actual action/input class and checks.
3. **Reuse modules:** operations can serve several skills. Their operation/action IDs retain a single detailed definition. The view-synthesis skill row includes the related NeRF branch as an explicit packaging proposal while preserving the original skill name.
4. **Validation:** all operations retain their own numerical/source/semantic checks. CAD-13/14 provide the cross-cutting saved-artifact and recovery procedures.

## model-brief

Bind purpose, source claims, dimensions, feature criteria and candidate branches.

1. **CAD-01 — Extract a model brief from text and dimensions:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md).
2. **DOM-01 — Normalize model brief:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md).

## ocs-engineering

Reuse the existing session, native geometry, source/frame and readback contract for supported OCS capabilities. Alternate backend requirements retain their own procedure.

1. **CAD-09 — Build and constrain an editable planar sketch:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
2. **CAD-10 — Create a kernel solid and native model document from confirmed parameters:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
3. **CAD-12 — Assemble existing CAD or source-library components:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json).
4. **CAD-13 — Verify model geometry and saved output:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
5. **CAD-14 — Recover from failed interpretation or geometry construction:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
6. **DOM-05 — Export STEP solid:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
7. **DOM-07 — Place reusable component in assembly:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json).
8. **DOM-25 — Create fabrication package:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
9. **DOM-26 — Version and reuse component revision:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json).

## parametric-solid-modeling

Build constrained/source-defined geometry and preserve actual native/source/solid outputs.

1. **CAD-09 — Build and constrain an editable planar sketch:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
2. **CAD-10 — Create a kernel solid and native model document from confirmed parameters:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
3. **CAD-15 — Render source-defined CSG as a mesh:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
4. **DOM-03 — DXF/SVG drawing to constrained profile:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
5. **DOM-04 — Brief/profile to native CAD solid:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
6. **DOM-25 — Create fabrication package:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
7. **REC-14 — Remodel segmented scan evidence as parametric CAD:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
8. **DOM-23 — Scan or mesh to parametric CAD remodeling:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).

## drawing-to-cad

Rectify drawings, associate annotations/features, establish view correspondence and author checked profiles/solids.

1. **CAD-02 — Rectify a raster drawing plane from known dimensions:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
2. **CAD-03 — Recognize dimension text with OCR:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
3. **CAD-04 — Extract raster edges, lines and contours:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
4. **CAD-05 — Convert raster floor-plan candidates into a wall and opening graph:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
5. **CAD-06 — Register orthographic drawing views in a shared coordinate frame:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
6. **CAD-07 — Reconstruct a candidate 3D wireframe and surface from orthographic views:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
7. **CAD-08 — Read and clean vector drawing geometry:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
8. **CAD-09 — Build and constrain an editable planar sketch:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
9. **CAD-17 — Build wall and opening solids from a confirmed floor-plan graph:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
10. **DOM-02 — Raster sketch to constrained sketch:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
11. **DOM-18 — Raster floor plan to IFC building:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).

## blender-modeling

Compose supported scene/mesh/camera derivatives with explicit input adapters and asset identity.

1. **DOM-12 — Export mesh assets for MuJoCo:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
2. **DOM-17 — IFC to GLB display scene:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
3. **DOM-24 — Assemble and inspect Blender scene:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).

## capture-and-calibration

Prepare image/depth evidence, camera calibration, timing and explicit pose/control roles.

1. **CAD-02B — Calibrate camera poses from photographs and known controls:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
2. **REC-01 — Calibrate camera intrinsics and distortion:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
3. **REC-02 — Solve camera pose from known 3D-to-2D correspondences:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
4. **REC-04 — Convert video into an image reconstruction dataset:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
5. **REC-05 — Register RGB and depth frames and estimate sequence poses:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
6. **DOM-21 — Depth frames to registered point cloud or mesh:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).

## photogrammetry

Recover sparse/dense observed geometry with explicit scale controls and separate meshing.

1. **CAD-16 — Reconstruct camera poses and dense visible geometry from overlapping photos:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
2. **REC-03 — Estimate camera poses and sparse structure from overlapping photos:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
3. **REC-17 — Build dense point cloud and mesh from SfM camera solution:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
4. **DOM-20 — Photos/video to camera solution, point cloud and mesh:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
5. **DOM-28 — Dense multi-view stereo to point cloud and mesh:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).

## point-cloud-and-mesh-processing

Register samples, integrate depth, fit supported models, infer surfaces and check approximation.

1. **CAD-11 — Fit analytic features to scans or image-derived point clouds:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
2. **REC-05 — Register RGB and depth frames and estimate sequence poses:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
3. **REC-06 — Integrate calibrated RGB-D frames into point cloud or TSDF mesh:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
4. **REC-07 — Estimate coarse transform between point clouds:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
5. **REC-08 — Refine registration and compare point-cloud surfaces:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
6. **REC-09 — Segment point clouds and fit candidate primitive evidence:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
7. **DOM-19 — Register scan to building frame:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
8. **DOM-21 — Depth frames to registered point cloud or mesh:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
9. **DOM-29 — Point cloud to surface mesh:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).

## scan-to-cad

Relate CAD, scans, drawings and camera annotations, then remodel or compare source-linked features.

1. **CAD-11 — Fit analytic features to scans or image-derived point clouds:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
2. **REC-12 — Register existing CAD to calibrated photographs or scan points:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
3. **REC-13 — Anchor a screen sketch to a 3D surface:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
4. **REC-14 — Remodel segmented scan evidence as parametric CAD:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
5. **REC-15 — Reconcile scan surfaces with dimensioned drawings:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
6. **REC-16 — Iterate CAD edits against registered evidence:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
7. **DOM-23 — Scan or mesh to parametric CAD remodeling:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).

## generative-3d-reference

Use the selected learned-depth or image-generated proxy branch with model-specific outputs, rights and scale evidence.

1. **REC-10 — Estimate multi-view depth, camera poses and Gaussian outputs:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
2. **REC-18 — Generate a single-image mesh proxy:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).

## gaussian-scene-reference

Reconstruct view-synthesis scenes; Gaussian and related NeRF branches retain separate payloads, renderers and geometry-extraction conditions.

1. **REC-11 — Train NeRF or Gaussian scene for view synthesis:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
2. **REC-19 — Train and export a Gaussian splat scene:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
3. **REC-20 — Train and export a NeRF scene:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
4. **DOM-22 — Photographs to Gaussian/NeRF visual scene:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).
5. **DOM-30 — Photos to NeRF visual scene:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json).

## architecture-ifc

Author semantic building relationships and preserve element/frame identity through geometry/display/environment derivatives.

1. **DOM-02 — Raster sketch to constrained sketch:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
2. **DOM-15 — Author semantic IFC building:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
3. **DOM-16 — Extract IFC geometry as triangles:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
4. **DOM-17 — IFC to GLB display scene:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
5. **DOM-18 — Raster floor plan to IFC building:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json).
6. **DOM-19 — Register scan to building frame:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json).
7. **DOM-27 — Extract IFC geometry as OpenCASCADE B-rep:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
8. **DOM-34 — Author static MuJoCo environment from BIM mesh:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
9. **DOM-35 — Place library component in semantic IFC:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).

## robot-model-handoff

Author link/joint graphs and physical/collision roles, serialize robot descriptions and check the named consumer.

1. **DOM-08 — CAD assembly to articulated robot structure:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
2. **DOM-09 — Robot assembly to URDF package:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
3. **DOM-10 — URDF import and MJCF conversion:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
4. **DOM-11 — Author native MJCF simulation model:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
5. **DOM-12 — Export mesh assets for MuJoCo:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
6. **DOM-13 — Generate convex collision set:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
7. **DOM-14 — Calculate or import physical mass properties:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
8. **DOM-31 — Author assembly graph and joint set:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
9. **DOM-32 — Map CAD link geometry to MJCF body tree:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
10. **DOM-33 — Add environment collision geometry to MJCF:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
11. **DOM-34 — Author static MuJoCo environment from BIM mesh:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
12. **DOM-37 — Author robot assembly from CAD component:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).

## component-library

Identify exact source assets/terms and revisions, import/place instances and retain reusable derivative manifests.

1. **CAD-12 — Assemble existing CAD or source-library components:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json).
2. **DOM-05 — Export STEP solid:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
3. **DOM-06 — Library asset intake and rights record:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json).
4. **DOM-07 — Place reusable component in assembly:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json).
5. **DOM-26 — Version and reuse component revision:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json).
6. **DOM-35 — Place library component in semantic IFC:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
7. **DOM-37 — Author robot assembly from CAD component:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json).
8. **DOM-38 — Import STEP solid into CAD representation:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json).
9. **DOM-39 — Export STEP assembly:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json).
10. **DOM-40 — Script-parametric CAD authoring:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).

## model-verification

Check actual saved artifacts and recover affected descendants; action-specific validation is also present throughout all 77 operations.

1. **CAD-13 — Verify model geometry and saved output:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
2. **CAD-14 — Recover from failed interpretation or geometry construction:** [procedure](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md); [action/helper contracts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json).
