# REC-R04 — Scan and dimensioned drawing to constrained CAD

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 4/5; setup 4/5; computing 3/5.**

Output: Reconciled dimensions, scan-backed surface reference and OCS parametric feature interpretation.

## Comparison conditions

Point cloud has declared units/frame; drawing revision and scale known; common datums or identifiable features; a human selects semantic CAD features.

## Registered starting artifact types

1. point-cloud
2. vector-drawing
3. measurement-set

## Detailed source and preparation artifacts

1. Artifact: point-cloud; Format and quality: PLY/PCD/E57 converted without changing coordinate provenance; calibrated units/frame and useful surface coverage.
2. Artifact: vector-drawing; Format and quality: DXF/SVG/PDF-derived linework with known scale, datums and drawing revision.
3. Artifact: measurement-set; Format and quality: Explicit drawing dimensions, scan datum correspondences and fit/validation labels.

## Reference points, datums and coordinate frames

Drawing dimensions and scan samples remain separate sources. Align shared datum points/planes/features; reserve dimensions and controls from fitting. Point-cloud primitive-fit residuals are candidate evidence; they do not name semantic design intent.

## Software, libraries and dependencies

1. Name: Open3D; Licence scope: MIT; Role and api: segment_plane, cluster_dbscan, registration_icp; Dependencies: Python open3d
2. Name: CloudCompare; Licence scope: GPL-2.0-or-later; Role and api: cloud alignment, distance maps and CLI; Dependencies: CloudCompare
3. Name: OCS; Licence scope: Existing local skill contract; Role and api: Constrained sketch/features, part units and readback; Dependencies: OpenCADStudio + OCS skill

## Procedure

1. Step: 1; Action: Check cloud bounds, units, frame and sample coverage; preserve original file.
2. Step: 2; Action: Segment planes/clusters and record indices, thresholds and fit residuals.
3. Step: 3; Action: Align drawing and cloud through datums; report per-region distances and retain source offsets.
4. Step: 4; Action: Create constrained sketches/features in OCS from dimensioned drawing and named evidence; mark fitted/assumed values separately.
5. Step: 5; Action: Read back CAD and compare against withheld drawing dimensions and original cloud.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-09; Name: Segment point clouds and fit candidate primitive evidence; Inputs: point-cloud; Outputs: point-cloud; measurement-set; Tools: Open3D segment_plane; Open3D DBSCAN; CloudCompare scalar-field and primitive tools; Source urls: https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html; https://github.com/CloudCompare/CloudCompare; Prerequisites: Scale/units and cloud frame declared; Segmentation thresholds expressed in cloud units; Target regions have enough spatial coverage; Preserves: Original cloud; Point indices for each segment and threshold parameters; Changes or infers: Classifies points into plane inliers/clusters; Primitive parameters are estimates from sampled observations; Checks: Plane/candidate feature residuals and inlier count; Repeat fit at alternative thresholds; Manual check for mixed surfaces and partial arcs; Alternatives: CloudCompare interactive segmentation; RANSAC/least-squares feature-specific fitters; Manual CAD measurements; Automation: mixed; Evidence status: documented_capability; Summary: Partition a cloud and obtain candidate planes/clusters; parameters are evidence for a feature interpretation, not automatically semantic CAD.
2. Id: REC-15; Name: Reconcile scan surfaces with dimensioned drawings; Inputs: measurement-set; Input choice groups: point-cloud; mesh; vector-drawing; raster-plan; raster-sketch; Outputs: measurement-set; Tools: CAD drawing datums; Open3D/CloudCompare registration and distance map; OCS constrained sketch; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode; Prerequisites: Drawing units/scale and revision known; Common datums, features or control targets; Scan coordinate frame recorded; Preserves: Drawing and scan as separate evidence sources; Source revision, units and alignment transform; Changes or infers: Aligns evidence and constrains CAD candidate features; Discrepancies may reflect drawing, manufactured part, scan or interpretation differences; Checks: Use some dimensions for fit and reserve others for validation; Report drawing-to-scan residuals and surface coverage; Inspect datum consistency and per-feature outliers; Alternatives: Calibrated image-to-CAD registration; Direct measurements; Separate variant models by source revision; Automation: mixed; Evidence status: proposed_composition; Summary: Use a drawing as dimension evidence and a scan as surface evidence; preserve disagreements and provenance instead of averaging incompatible values without an explicit rule.
3. Id: REC-14; Name: Remodel segmented scan evidence as parametric CAD; Inputs: measurement-set; Input alternatives: point-cloud; mesh; Outputs: constrained-sketch; parametric-source; cad-solid; Tools: Open3D feature fits; OpenCADStudio OCS skill; parametric CAD backend; Source urls: https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; Prerequisites: Registered scan and datum frame; Dimensions labeled measured/drawing/fit/assumed; Component boundaries and units stated; Preserves: Raw scan, segmentation indices and fit report; Dimension provenance for every feature; Changes or infers: Replaces noisy sampled boundaries with constrained feature model; Hidden surfaces/functional details require explicit assumptions; Checks: OCS readback of geometry/revision; Solid validity and independent dimensions; Scan-to-CAD residual maps by surface and withheld controls; Alternatives: Mesh kept as reference-only deliverable; Faceted mesh-derived solid when that is the required representation; Automation: mixed; Evidence status: proposed_composition; Summary: Use fitted scan geometry as evidence and reconstruct an editable feature history through the existing OCS workflow; fitted parameters must remain traceable and not silently become author dimensions.
4. Id: REC-16; Name: Iterate CAD edits against registered evidence; Inputs: measurement-set; Input alternatives: cad-solid; parametric-source; Input choice groups: point-cloud; mesh; Outputs: measurement-set; Tools: OCS revision-bound edit/readback; Open3D distance queries; CloudCompare distance command; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode; Prerequisites: Immutable source scan and transform; CAD revision identity; Comparison regions and thresholds with units; Preserves: Prior CAD and scan revisions; Check configuration and dimensional source links; Changes or infers: Applies bounded CAD edit and computes deltas; Checks: Read back edited model; Compare same registered scan/controls across revisions; Report regional max/RMS/quantiles and functional dimension changes; Alternatives: Manual visual compare; Independent target metrology; Cross-section comparison; Automation: mixed; Evidence status: proposed_composition; Summary: Use a repeatable scan-to-CAD comparison loop while preserving the source and tying every reported deviation to exact model revisions and regions.

## Code and tool entry points

1. Path: [register_clouds.py](/home/leo/projects/3dmodeling/examples/workflows/reconstruction/register_clouds.py); Status: reference_code; Entrypoint: `python register_clouds.py --source source.ply --target target.ply --initial-transform init.json --max-correspondence-distance <value-in-model-units> --unit <unit> --output-report result.json --output-source-ply registered_source.ply`; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html

## Output artifacts

1. Representation: Reconciled dimensions, scan-backed surface reference and OCS parametric feature interpretation.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: OCS remodeling is a separate feature-interpretation stage requiring explicit dimensions, coordinate frame, constraints and readback.

## Checks

Drawing unit and revision; datum residuals; fit point count/coverage; hold-out drawing dimensions; regional scan-CAD distance distribution; OCS readback.

## Failure recovery

If datums do not align, separate drawing revision/part variant instead of averaging. If partial arcs produce unstable cylinders, use explicit measurement/feature context. If scan coverage is incomplete, retain missing surfaces as unknown/inferred.

## Effort and computing classification

1. **Human:** 4
2. **Setup:** 4
3. **Compute:** 3
4. **Human reason:** Scan/drawing reconciliation and deciding feature semantics require substantial engineering interpretation.
5. **Setup reason:** Needs cloud tools, drawing parser and OCS workflow.
6. **Compute reason:** Cloud operations scale with point count; OCS part construction is modest CPU work.

## Resources and scaling

1. **Cpu:** Open3D segmentation, ICP and CAD authoring can use CPU.
2. **Gpu:** No GPU requirement for listed operations.
3. **Ram:** Scales with cloud point count and application geometry.
4. **Storage:** Cloud originals, derived segments, meshes and CAD revisions.
5. **Scaling drivers:** Point count, surface coverage, registration threshold and mesh density.
6. **Variants:** Clean vector drawing reduces tracing work; raster drawing requires scale/datum extraction.

## Original sources

1. [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html)
2. [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)
3. [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode)
4. [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
