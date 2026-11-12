# Existing operation inventory and detailed-review state

Date: 12 November 2026. All 77 existing operation records are inventoried. Detailed action definitions proceed in the order recorded in the [execution plan](/home/leo/projects/3dmodeling/research/action-audit/plan.md). The first shared point covers CAD-01 and DOM-01. Original automation labels are retained as historical classifications.

| Operation | Existing family | Original automation label | Current audit state | Original record |
| --- | --- | --- | --- | --- |
| CAD-01 — Extract a model brief from text and dimensions | cad | assisted | Proposed action definition reviewed | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-02 — Rectify a raster drawing plane from known dimensions | cad | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-03 — Recognize dimension text with OCR | cad | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-04 — Extract raster edges, lines and contours | cad | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-05 — Convert raster floor-plan candidates into a wall and opening graph | cad | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-06 — Register orthographic drawing views in a shared coordinate frame | cad | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-07 — Reconstruct a candidate 3D wireframe and surface from orthographic views | cad | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-08 — Read and clean vector drawing geometry | cad | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-09 — Build and constrain an editable planar sketch | cad | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-10 — Create a kernel solid and native model document from confirmed parameters | cad | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-11 — Fit analytic features to scans or image-derived point clouds | cad | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-12 — Assemble existing CAD or source-library components | cad | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-13 — Verify model geometry and saved output | cad | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-14 — Recover from failed interpretation or geometry construction | cad | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-02B — Calibrate camera poses from photographs and known controls | cad | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-15 — Render source-defined CSG as a mesh | cad | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-16 — Reconstruct camera poses and dense visible geometry from overlapping photos | cad | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| CAD-17 — Build wall and opening solids from a confirmed floor-plan graph | cad | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) |
| REC-01 — Calibrate camera intrinsics and distortion | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-02 — Solve camera pose from known 3D-to-2D correspondences | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-03 — Estimate camera poses and sparse structure from overlapping photos | reconstruction | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-04 — Convert video into an image reconstruction dataset | reconstruction | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-05 — Register RGB and depth frames and estimate sequence poses | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-06 — Integrate calibrated RGB-D frames into point cloud or TSDF mesh | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-07 — Estimate coarse transform between point clouds | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-08 — Refine registration and compare point-cloud surfaces | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-09 — Segment point clouds and fit candidate primitive evidence | reconstruction | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-10 — Estimate multi-view depth, camera poses and Gaussian outputs | reconstruction | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-11 — Train NeRF or Gaussian scene for view synthesis | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-12 — Register existing CAD to calibrated photographs or scan points | reconstruction | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-13 — Anchor a screen sketch to a 3D surface | reconstruction | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-14 — Remodel segmented scan evidence as parametric CAD | reconstruction | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-15 — Reconcile scan surfaces with dimensioned drawings | reconstruction | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-16 — Iterate CAD edits against registered evidence | reconstruction | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-17 — Build dense point cloud and mesh from SfM camera solution | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-18 — Generate a single-image mesh proxy | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-19 — Train and export a Gaussian splat scene | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| REC-20 — Train and export a NeRF scene | reconstruction | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json) |
| DOM-01 — Normalize model brief | domain | mixed | Proposed action definition reviewed | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-02 — Raster sketch to constrained sketch | domain | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-03 — DXF/SVG drawing to constrained profile | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-04 — Brief/profile to native CAD solid | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-05 — Export STEP solid | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-06 — Library asset intake and rights record | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-07 — Place reusable component in assembly | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-08 — CAD assembly to articulated robot structure | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-09 — Robot assembly to URDF package | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-10 — URDF import and MJCF conversion | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-11 — Author native MJCF simulation model | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-12 — Export mesh assets for MuJoCo | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-13 — Generate convex collision set | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-14 — Calculate or import physical mass properties | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-15 — Author semantic IFC building | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-16 — Extract IFC geometry as triangles | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-17 — IFC to GLB display scene | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-18 — Raster floor plan to IFC building | domain | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-19 — Register scan to building frame | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-20 — Photos/video to camera solution, point cloud and mesh | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-21 — Depth frames to registered point cloud or mesh | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-22 — Photographs to Gaussian/NeRF visual scene | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-23 — Scan or mesh to parametric CAD remodeling | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-24 — Assemble and inspect Blender scene | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-25 — Create fabrication package | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-26 — Version and reuse component revision | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-27 — Extract IFC geometry as OpenCASCADE B-rep | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-28 — Dense multi-view stereo to point cloud and mesh | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-29 — Point cloud to surface mesh | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-30 — Photos to NeRF visual scene | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-31 — Author assembly graph and joint set | domain | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-32 — Map CAD link geometry to MJCF body tree | domain | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-33 — Add environment collision geometry to MJCF | domain | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-34 — Author static MuJoCo environment from BIM mesh | domain | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-35 — Place library component in semantic IFC | domain | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-37 — Author robot assembly from CAD component | domain | assisted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-38 — Import STEP solid into CAD representation | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-39 — Export STEP assembly | domain | mixed | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
| DOM-40 — Script-parametric CAD authoring | domain | scripted | Existing operation inventoried | [operation/source record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) |
