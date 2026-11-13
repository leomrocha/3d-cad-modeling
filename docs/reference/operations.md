# Operation contracts

[Workflow](../workflow.md) · [Documentation](../README.md)

Each record identifies the source-backed operation and its handoff. Capability/proposal status belongs to that operation; executed example results remain attributed to their specific records.

<a id="cad-01"></a>

## CAD-01 — Extract a model brief from text and dimensions

1. **Sources:** [Source contract](../../research/workflows/cad-paths.json); [Supporting source 1](../../research/implementation-plan.md); Registered local source 2: `${CODEX_HOME}/skills/ocs-engineering/SKILL.md`
2. **Evidence status:** proposed_composition
3. **Inputs:** ; alternatives: text; dimensions; text; dimensions
4. **Outputs:** model-brief
5. **Prerequisites:** Identify each value as supplied, measured, inferred, assumed, or calculated.; Declare units, origin, axes, component boundaries, intended output and source links.
6. **Tool/API:** model brief schema; human review; OCS engineering skill
7. **Geometry representation:** input: ; output: model-brief
8. **Units and frames:** Job length/angle units and named local/global frames are explicit inputs.
9. **Metric evidence:** Source-labelled dimensions and unit/frame declarations are the metric inputs; the proposed brief check requires every numeric parameter to resolve to a source.
10. **Information preserved:** Original text; Value-to-source associations; Author's unresolved choices
11. **Information changed/inferred:** Groups explicit requirements into named parameters and geometry constraints.; Does not infer hidden geometry from prose alone.
12. **Checks:** Every numerical parameter has units and provenance.; Ambiguities affecting geometry are listed separately.
13. **Alternatives:** Direct interactive OCS modeling after brief readback; Code-CAD generation from a validated brief
14. **Downstream operations:** CAD-09; CAD-10
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to CAD-09, CAD-10. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="cad-08"></a>

## CAD-08 — Read and clean vector drawing geometry

1. **Sources:** [Source contract](../../research/workflows/cad-paths.json); [Supporting source 1](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md); [Supporting source 2](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md); [Supporting source 3](https://ezdxf.readthedocs.io/en/stable/); Registered local source 4: `${OCS_ROOT}/docs/automation/README.md`; Registered local source 5: `${OCS_ROOT}/README.md`
2. **Evidence status:** documented_capability
3. **Inputs:** vector-drawing
4. **Outputs:** vector-drawing
5. **Prerequisites:** Preserve source file and hash.; Determine drawing units, model/paper space, layer selection, block transforms, origin and target sketch plane.; Read DXF/SVG import option and unsupported entity behavior.
6. **Tool/API:** OpenCADStudio DWG/DXF/MCP; FreeCAD Draft DXF/SVG import; ezdxf; geometry audit
7. **Geometry representation:** input: vector-drawing; output: vector-drawing
8. **Units and frames:** Retain drawing INSUNITS, source entity OCS and nested WCS transforms; convert only in a recorded derivative.
9. **Metric evidence:** Read drawing unit headers and source dimensions; inspection returns source counts/transforms. Compare selected profile extents with independently dimensioned features before construction.
10. **Information preserved:** Original file; Entity types, layers, blocks, annotations and source coordinates where supported
11. **Information changed/inferred:** Selects profile entities, normalizes transforms and may join, discretize, or repair curves.
12. **Checks:** Count input/output entities by type and layer.; Find duplicate/open/self-intersecting edges.; Compare profile bounds, area and source dimensions.; For SVG, verify viewBox and physical scale; FreeCAD importer flattens Z.
13. **Alternatives:** Use the source DXF unchanged in OCS; Use FreeCAD native DXF or legacy importer; Parse DXF with ezdxf and build clean geometry separately
14. **Downstream operations:** CAD-09
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to CAD-09. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="cad-09"></a>

## CAD-09 — Build and constrain an editable planar sketch

1. **Sources:** [Source contract](../../research/workflows/cad-paths.json); [Supporting source 1](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md); [Supporting source 2](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md); Registered local source 3: `${CODEX_HOME}/skills/ocs-engineering/SKILL.md`
2. **Evidence status:** documented_capability
3. **Inputs:** vector-drawing; alternatives: model-brief; dimensions; measurement-set
4. **Outputs:** constrained-sketch
5. **Prerequisites:** Specify units, support plane and datum.; Resolve profile closure/repair and record which source curves changed.; Associate each dimensional constraint with measured/source/inferred status.
6. **Tool/API:** FreeCAD Sketcher scripting; FreeCAD Draft-to-Sketch; OpenCADStudio sketch/constraint capability as discovered in session
7. **Geometry representation:** input: vector-drawing; output: constrained-sketch
8. **Units and frames:** Use the confirmed source length unit and sketch-plane frame.
9. **Metric evidence:** Use explicit dimension/angle constraints in the sketch unit; check constraint residuals and degrees of freedom against the job criteria.
10. **Information preserved:** 2D profile geometry; Named dimensions and geometric constraints; Constraint provenance in the project evidence ledger
11. **Information changed/inferred:** Adds constraints and may alter underconstrained geometry to satisfy them.
12. **Checks:** Solver state/degrees of freedom; Residuals and overconstraints; Source-to-constraint numeric comparison; Profile closedness and intersections
13. **Alternatives:** Keep vector geometry as non-parametric Draft/OCS drawing entities; Generate sketch geometry from code-CAD source
14. **Downstream operations:** CAD-10
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to CAD-10. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="cad-10"></a>

## CAD-10 — Create a kernel solid and native model document from confirmed parameters

1. **Sources:** [Source contract](../../research/workflows/cad-paths.json); [Supporting source 1](https://build123d.readthedocs.io/en/latest/operations.html); [Supporting source 2](https://cadquery.readthedocs.io/en/stable/); [Supporting source 3](https://openscad.org/documentation); [Supporting source 4](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md); Registered local source 5: `${OCS_ROOT}/docs/cadkernel-body-path.md`
2. **Evidence status:** documented_capability
3. **Inputs:** ; alternatives: constrained-sketch; parametric-source; model-brief; dimensions
4. **Outputs:** cad-solid; native-model-document
5. **Prerequisites:** Declare units, feature parameters, direction/axis and part boundary.; Use exact B-rep backend if exact surfaces/export are required.; Preserve native feature document or code source.
6. **Tool/API:** OpenCADStudio kernel tools; FreeCAD PartDesign/Part; build123d; CadQuery
7. **Geometry representation:** input: ; output: cad-solid; native-model-document
8. **Units and frames:** Use the source job units and construction frame; native examples use mm.
9. **Metric evidence:** Compare analytic feature dimensions, bounds and solid topology with the source job; FERME examples link retained source-bound native checks.
10. **Information preserved:** Input dimensions and feature parameters; Native feature tree or executable parametric source; Part names and component boundaries; Editable native model document; feature history depends on the selected CAD application
11. **Information changed/inferred:** Creates exact kernel geometry from the confirmed profile/feature instructions; unsupported features may require alternatives.
12. **Checks:** Kernel shape validity and solid count; Bounds, volume, hole/shaft dimensions and units; Recompute or regenerate after one parameter change; Save/reopen and independent import
13. **Alternatives:** FreeCAD feature-history model; build123d/CadQuery Python source; OCS native body; separate exact STEP exporter if needed
14. **Downstream operations:** CAD-13; CAD-12
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to CAD-13, CAD-12. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="cad-12"></a>

## CAD-12 — Assemble existing CAD or source-library components

1. **Sources:** [Source contract](../../research/workflows/cad-paths.json); [Supporting source 1](../../research/domains-and-components.md); Registered local source 2: `${OCS_ROOT}/docs/automation/README.md`; [Supporting source 3](https://cadquery.readthedocs.io/en/stable/)
2. **Evidence status:** proposed_composition
3. **Inputs:** cad-solid; alternatives: source-library; cad-solid
4. **Outputs:** cad-assembly
5. **Prerequisites:** Record component source/license/hash and representation.; Establish local units, origin, axis directions and interface frames for each part.; Separate source components from placeholders.; Provide a distinct base cad-solid plus either a source-library component or one or more additional cad-solid component files; identify each occurrence separately.
6. **Tool/API:** OCS blocks/groups; FreeCAD App::Link/Assembly; build123d/CadQuery Assembly; unit and frame mapping
7. **Geometry representation:** input: cad-solid; output: cad-assembly
8. **Units and frames:** Use each component local frame and explicit occurrence-to-assembly transforms.
9. **Metric evidence:** Check occurrence transforms and named interface coordinates in the assembly frame against source-defined placements.
10. **Information preserved:** Component identities and source files; Occurrence transforms and assembly hierarchy; Native component boundaries
11. **Information changed/inferred:** Places parts using declared mating frames; inferred contact or fastener geometry is proposal unless sourced.
12. **Checks:** Frame/transform consistency; Interface dimension agreement; Component counts and source hashes; Collision/clearance only with supported exact geometry and query
13. **Alternatives:** Visual-only assembly in Blender; OCS block/group drawing arrangement; Full parametric assembly in FreeCAD or Python code-CAD
14. **Downstream operations:** CAD-13; SIM-01
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to CAD-13, SIM-01. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="cad-13"></a>

## CAD-13 — Verify model geometry and saved output

1. **Sources:** [Bearing result](../examples/files/ferme/bearing-result.json); [Battery result](../examples/files/ferme/battery-result.json); [Source contract](../../research/workflows/cad-paths.json); Registered local source 1: `${OCS_ROOT}/docs/automation/README.md`; Registered local source 2: `${OCS_ROOT}/src/io/step.rs`; Registered local source 3: `${CODEX_HOME}/skills/ocs-engineering/SKILL.md`; [Supporting source 4](https://build123d.readthedocs.io/en/stable/)
2. **Evidence status:** proposed_composition
3. **Inputs:** ; alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document
4. **Outputs:** measurement-set; verification-report
5. **Prerequisites:** Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.
6. **Tool/API:** OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation
7. **Geometry representation:** input: ; output: measurement-set; verification-report
8. **Units and frames:** Compare in the same source/model units and frame; each tolerance has its unit.
9. **Metric evidence:** Recorded bearing example: 62 native checks PASS; battery example: 29 native checks PASS; each retained result also records persistence PASS. Other jobs supply their own criteria.
10. **Information preserved:** Source revision and hash; Output hash and conversion settings; Measured check results and failed checks
11. **Information changed/inferred:** Reads or reopens derivatives and calculates verification measurements; does not repair by itself.
12. **Checks:** Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.
13. **Alternatives:** Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip
14. **Downstream operations:** SIM-01; DOM-17
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to SIM-01, DOM-17. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="rec-01"></a>

## REC-01 — Calibrate camera intrinsics and distortion

1. **Sources:** [Source contract](../../research/workflows/reconstruction-paths.json); [Supporting source 1](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
2. **Evidence status:** documented_capability
3. **Inputs:** photo-set; measurement-set
4. **Outputs:** camera-solution
5. **Prerequisites:** Known target geometry and units; Images cover target orientations and image field; Camera/lens/focus state recorded
6. **Tool/API:** OpenCV calibrateCamera; checkerboard or Charuco target
7. **Geometry representation:** input: photo-set; measurement-set; output: camera-solution
8. **Units and frames:** Image coordinates in pixels; target coordinates in their measured length unit; retain camera intrinsics and distortion conventions.
9. **Metric evidence:** Calibration target coordinates supply metric evidence. Record reprojection RMS/per-image residuals in pixels and held-out target checks; this page registers the proposed method.
10. **Information preserved:** Original images; Target dimensions and capture metadata
11. **Information changed/inferred:** Estimates intrinsics and lens-distortion coefficients; Undistorted images are derivatives
12. **Checks:** Calibration reprojection RMS and per-image residuals; Undistort a held-out target image and compare straight edges; Keep calibration target coordinates in declared units
13. **Alternatives:** COLMAP self-calibration for capture-derived focal/intrinsic estimates; Manufacturer calibration only when specific camera/lens state is known
14. **Downstream operations:** REC-03
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to REC-03. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="rec-03"></a>

## REC-03 — Estimate camera poses and sparse structure from overlapping photos

1. **Sources:** [Source contract](../../research/workflows/reconstruction-paths.json); [Supporting source 1](https://github.com/colmap/colmap/blob/main/doc/cli.rst); [Supporting source 2](https://alicevision.org/); [Supporting source 3](https://github.com/openMVG/openMVG)
2. **Evidence status:** existing_report_registered
3. **Inputs:** photo-set
4. **Outputs:** camera-solution; point-cloud
5. **Prerequisites:** Static scene or moving objects masked; Overlap and texture sufficient for feature matching; Camera model/preprocessing documented
6. **Tool/API:** COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG
7. **Geometry representation:** input: photo-set; output: camera-solution; point-cloud
8. **Units and frames:** Camera/image coordinates and sparse world frame; scale derives from stated controls or calibrated metric camera data.
9. **Metric evidence:** Metric scale comes from measured controls or documented metric camera information. Record image reprojection residuals and withheld control-length errors for the particular reconstruction.
10. **Information preserved:** Input images; Feature and match database, camera model, sparse reconstruction and settings
11. **Information changed/inferred:** Estimates camera poses and sparse 3D points; Monocular reconstruction scale is arbitrary absent controls/metric sensor
12. **Checks:** Registered image fraction and component connectivity; Reprojection residual distribution; Camera path and sparse outliers; At least two separated scale controls for local distortion detection
13. **Alternatives:** OpenMVG+OpenMVS; Depth Anything 3 multi-view pose/depth estimate; Surveyed camera poses when available
14. **Downstream operations:** REC-17
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to REC-17. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="rec-08"></a>

## REC-08 — Refine registration and compare point-cloud surfaces

1. **Sources:** [Source contract](../../research/workflows/reconstruction-paths.json); [Supporting source 1](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html); [Supporting source 2](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode)
2. **Evidence status:** documented_capability
3. **Inputs:** measurement-set; point-cloud
4. **Outputs:** measurement-set
5. **Prerequisites:** Coarse transform; Overlap and consistent units; ICP threshold selected from expected sampling/noise scale
6. **Tool/API:** Open3D point-to-plane ICP; Open3D evaluate_registration; CloudCompare cloud-to-cloud distance
7. **Geometry representation:** input: measurement-set; point-cloud; output: measurement-set
8. **Units and frames:** Cloud coordinates use one declared length unit; retain moving-to-fixed transform and independent controls.
9. **Metric evidence:** Record cloud-registration fitness, inlier RMS distance in the cloud length unit and independent control-point residuals; keep fit points separate from checks.
10. **Information preserved:** Source clouds and original transforms; Correspondence threshold and final transform
11. **Information changed/inferred:** Refines transform to minimize selected correspondence objective; Distance map depends on chosen correspondence and sampling rule
12. **Checks:** Fitness and inlier RMSE with units; Independent control residuals; Inspect residual map and non-overlap separately
13. **Alternatives:** Robust kernels; Multiway pose graph registration; Target-based transformation
14. **Downstream operations:** REC-14
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to REC-14. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="rec-14"></a>

## REC-14 — Remodel segmented scan evidence as parametric CAD

1. **Sources:** [Source contract](../../research/workflows/reconstruction-paths.json); [Supporting source 1](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html); [Supporting source 2](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)
2. **Evidence status:** proposed_composition
3. **Inputs:** measurement-set; alternatives: point-cloud; mesh
4. **Outputs:** constrained-sketch; parametric-source; cad-solid
5. **Prerequisites:** Registered scan and datum frame; Dimensions labeled measured/drawing/fit/assumed; Component boundaries and units stated
6. **Tool/API:** Open3D feature fits; OpenCADStudio OCS skill; parametric CAD backend
7. **Geometry representation:** input: measurement-set; output: constrained-sketch; parametric-source; cad-solid
8. **Units and frames:** Registered evidence in a named datum frame; CAD length units and feature provenance are explicit.
9. **Metric evidence:** Feature dimensions retain measured/drawing/fit/assumed provenance; record source-to-CAD surface residuals and withheld dimensions in the declared length unit.
10. **Information preserved:** Raw scan, segmentation indices and fit report; Dimension provenance for every feature
11. **Information changed/inferred:** Replaces noisy sampled boundaries with constrained feature model; Hidden surfaces/functional details require explicit assumptions
12. **Checks:** OCS readback of geometry/revision; Solid validity and independent dimensions; Scan-to-CAD residual maps by surface and withheld controls
13. **Alternatives:** Mesh kept as reference-only deliverable; Faceted mesh-derived solid when that is the required representation
14. **Downstream operations:** REC-16; CAD-13
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to REC-16, CAD-13. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="rec-16"></a>

## REC-16 — Iterate CAD edits against registered evidence

1. **Sources:** [Source contract](../../research/workflows/reconstruction-paths.json); [Supporting source 1](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html); [Supporting source 2](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode)
2. **Evidence status:** proposed_composition
3. **Inputs:** measurement-set; alternatives: cad-solid; parametric-source; choice groups: point-cloud; mesh
4. **Outputs:** measurement-set
5. **Prerequisites:** Immutable source scan and transform; CAD revision identity; Comparison regions and thresholds with units
6. **Tool/API:** OCS revision-bound edit/readback; Open3D distance queries; CloudCompare distance command
7. **Geometry representation:** input: measurement-set; output: measurement-set
8. **Units and frames:** Same registered frame, length units, comparison regions and CAD revisions across the iteration.
9. **Metric evidence:** Compare regional max/RMS/quantile distances and functional-dimension changes against the same registered evidence, CAD revisions and source-bound criteria.
10. **Information preserved:** Prior CAD and scan revisions; Check configuration and dimensional source links
11. **Information changed/inferred:** Applies bounded CAD edit and computes deltas
12. **Checks:** Read back edited model; Compare same registered scan/controls across revisions; Report regional max/RMS/quantiles and functional dimension changes
13. **Alternatives:** Manual visual compare; Independent target metrology; Cross-section comparison
14. **Downstream operations:** CAD-13
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to CAD-13. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="rec-17"></a>

## REC-17 — Build dense point cloud and mesh from SfM camera solution

1. **Sources:** [Source contract](../../research/workflows/reconstruction-paths.json); [Supporting source 1](https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/); [Supporting source 2](https://github.com/colmap/colmap/blob/main/doc/cli.rst)
2. **Evidence status:** existing_report_registered
3. **Inputs:** photo-set; camera-solution
4. **Outputs:** point-cloud; mesh
5. **Prerequisites:** REC-03 sparse camera solution or equivalent calibrated poses; Overlap, exposure and scene masks retained; Scale supplied by control or metric camera data for dimensional use
6. **Tool/API:** OpenMVS DensifyPointCloud; OpenMVS ReconstructMesh; COLMAP dense workspace
7. **Geometry representation:** input: photo-set; camera-solution; output: point-cloud; mesh
8. **Units and frames:** Dense mesh/cloud inherits calibrated camera frame and scale; keep the scale transform explicit.
9. **Metric evidence:** Dense geometry inherits the camera scale; record withheld control-length errors, mesh-to-cloud distances and coverage for the reconstructed surface.
10. **Information preserved:** Sparse scene, images, camera poses and dense reconstruction settings
11. **Information changed/inferred:** Estimates dense visible surface and interpolated mesh; Unseen and occluded surfaces are not recovered from images
12. **Checks:** Image reprojection and dense coverage; Withheld control lengths and independent cloud residuals; Compare mesh-to-cloud distances and disconnected components
13. **Alternatives:** Open3D TSDF from calibrated RGB-D; Nerfstudio geometry extraction only where model support is established
14. **Downstream operations:** REC-08
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to REC-08. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="dom-15"></a>

## DOM-15 — Author semantic IFC building

1. **Sources:** [Source contract](../../research/workflows/domain-paths.json); [Supporting source 1](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html); [Supporting source 2](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html); [Supporting source 3](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html)
2. **Evidence status:** documented_capability
3. **Inputs:** model-brief
4. **Outputs:** ifc
5. **Prerequisites:** Storey/frame, element classes, openings, spatial relations and property requirements declared.
6. **Tool/API:** Bonsai; IfcOpenShell API
7. **Geometry representation:** input: model-brief; output: ifc
8. **Units and frames:** Retain IFC project units, local placements and building/storey coordinate frames.
9. **Metric evidence:** Validate IFC element identities, placements, properties and source-bound dimensions in declared project units; building execution remains a proposed route.
10. **Information preserved:** Element IDs, semantic relationships, object placements, source dimensions, property values and geometry representation type.
11. **Information changed/inferred:** Creates IfcProduct relationships and representations; parametric profiles or mesh representations are distinct IFC options.
12. **Checks:** Schema validation, unique GlobalIds, placement, property-set and relationship checks, IDS requirements.
13. **Alternatives:** Bonsai authoring UI; scripted IfcOpenShell creation; IFC import followed by semantic enrichment.
14. **Downstream operations:** DOM-17
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to DOM-17. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="dom-17"></a>

## DOM-17 — IFC to GLB display scene

1. **Sources:** [Source contract](../../research/workflows/domain-paths.json); [Supporting source 1](https://docs.ifcopenshell.org/introduction.html); [Supporting source 2](https://www.blender.org/features/pipeline/); Registered local source 3: `${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json`
2. **Evidence status:** documented_capability
3. **Inputs:** ifc
4. **Outputs:** visual-scene
5. **Prerequisites:** Element-to-display mapping and length/orientation conversion are declared.
6. **Tool/API:** IfcOpenShell IfcConvert; Blender; GLB export
7. **Geometry representation:** input: ifc; output: visual-scene
8. **Units and frames:** Retain IFC-to-display transform, output unit and object-to-element identity mapping.
9. **Metric evidence:** Check the IFC-to-display transform, element identity mapping and representative bounds in declared units against the source IFC.
10. **Information preserved:** IFC source/hash; stable element IDs; source properties in sidecar mapping where GLB cannot retain them.
11. **Information changed/inferred:** BIM objects become render nodes/meshes; semantic/relationship data may be reduced or remapped.
12. **Checks:** ID-to-node coverage, bounds, orientation, selected geometry hashes or residuals, output hashes.
13. **Alternatives:** Use IFC-native viewer when BIM relationships/properties are the primary task.
14. **Downstream operations:** Display/inspection consumer
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to the identified display consumer. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="dom-18"></a>

## DOM-18 — Raster floor plan to IFC building

1. **Sources:** [Source contract](../../research/workflows/domain-paths.json); [Supporting source 1](../../research/implementation-plan.md); [Supporting source 2](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html)
2. **Evidence status:** documented_capability
3. **Inputs:** raster-plan; dimensions; measurement-set; source-library; model-brief
4. **Outputs:** ifc
5. **Prerequisites:** Known plan scale/control lengths, orientation, floor elevation and interpretation rules for walls/openings.
6. **Tool/API:** Image calibration; OCS/FreeCAD sketching; Bonsai/IfcOpenShell
7. **Geometry representation:** input: raster-plan; dimensions; measurement-set; source-library; model-brief; output: ifc
8. **Units and frames:** Record plan scale, length units, axes, elevation references and IFC placements.
9. **Metric evidence:** Plan dimensions and measured controls supply length/elevation evidence; compare interpreted wall/opening geometry and storey assignments with those sources.
10. **Information preserved:** Original raster, scale transform, interpreted linework, dimension sources and uncertain regions.
11. **Information changed/inferred:** Pixels interpreted as boundaries and building elements; semantic classification is human/model inference.
12. **Checks:** Wall thickness, openings, elevations, spatial containment, area/element checks and IFC validation.
13. **Alternatives:** Vector drawing to sketch if original CAD exists; manual IFC authoring for high-confidence boundaries.
14. **Downstream operations:** DOM-15
15. **Handoff conditions:** Pass the named outputs, original source hashes, unit/frame record and operation check results to DOM-15. Preserve proposal/source status and reconcile any failed dimensional or frame checks before dependent use.

<a id="job-01"></a>

## JOB-01 — Record source files and scope

1. **Sources:** [Source contract](../../scripts/source_intake.py); [Supporting source 1](../../scripts/source_intake.py); [Supporting source 2](../../skills/source-intake/SKILL.md)
2. **Evidence status:** existing_implementation_or_execution_record_inspected
3. **Inputs:** job specification; original source files
4. **Outputs:** protected source revision; source index; scope receipt
5. **Prerequisites:** Authorized job scope; Readable source files; New output destination
6. **Tool/API:** source_intake.run; component_records.observe_file
7. **Geometry representation:** input: job specification; original source files; output: protected source revision; source index; scope receipt
8. **Units and frames:** Retain declared source units and frames as metadata.
9. **Metric evidence:** Original byte count and SHA-256; protected revision receipt.
10. **Information preserved:** Original input bytes, source identity and attributed units/frames
11. **Information changed/inferred:** Adds revision/index metadata
12. **Checks:** Parse source index; Verify source hashes; Protect prior revisions
13. **Alternatives:** Existing protected revision reused after verification
14. **Downstream operations:** JOB-02; CAD-01
15. **Handoff conditions:** Supply protected source revision, source index, scope receipt with source hashes and check results to JOB-02, CAD-01. Preserve the specific source scope and current revision.

<a id="job-02"></a>

## JOB-02 — Locate existing attributed models

1. **Sources:** [Source contract](../../scripts/model_inventory.py); [Supporting source 1](../../scripts/model_inventory.py)
2. **Evidence status:** existing_implementation_or_execution_record_inspected
3. **Inputs:** component index; work index; CAD/project roots
4. **Outputs:** model inventory; component identity review
5. **Prerequisites:** Explicit root/index paths; Component ID/name
6. **Tool/API:** inventory_models; start_check; audit
7. **Geometry representation:** input: component index; work index; CAD/project roots; output: model inventory; component identity review
8. **Units and frames:** Retain the original files and their recorded units/frames.
9. **Metric evidence:** File identity, suffix, byte count, SHA-256 and attributed component links.
10. **Information preserved:** Original input bytes, source identity and attributed units/frames
11. **Information changed/inferred:** Adds lookup classifications
12. **Checks:** Review filename candidates against component identity; Distinguish source drawings and reference components
13. **Alternatives:** Read matching model index and prior work records
14. **Downstream operations:** CAD-13; CAD-01
15. **Handoff conditions:** Supply model inventory, component identity review with source hashes and check results to CAD-13, CAD-01. Preserve the specific source scope and current revision.

<a id="job-03"></a>

## JOB-03 — Map image points into calibrated coordinates

1. **Sources:** [Source contract](../../scripts/calibrated_trace.py); [Supporting source 1](../../scripts/calibrated_trace.py); [Supporting source 2](../../tests/test_calibrated_trace.py)
2. **Evidence status:** existing_implementation_or_execution_record_inspected
3. **Inputs:** pixel points; pixel origin; signed axis scales; input uncertainties
4. **Outputs:** calibrated 2D coordinates; worst-case uncertainty bounds
5. **Prerequisites:** Calibrated planar interpretation; Explicit scale and length unit
6. **Tool/API:** calibrated_trace
7. **Geometry representation:** input: pixel points; pixel origin; signed axis scales; input uncertainties; output: calibrated 2D coordinates; worst-case uncertainty bounds
8. **Units and frames:** Pixels mapped to the supplied length unit in the declared 2D frame; signed scales retain axis reversal.
9. **Metric evidence:** Uncertainty bounds derive from the supplied point/origin/scale uncertainties.
10. **Information preserved:** Original input bytes, source identity and attributed units/frames
11. **Information changed/inferred:** Applies signed scaling and origin translation; propagates stated uncertainty
12. **Checks:** Finite inputs and nonzero scales; Independent control dimensions; Retain pixel-to-model mapping
13. **Alternatives:** Dimensioned vector source; Measured target coordinates
14. **Downstream operations:** CAD-09
15. **Handoff conditions:** Supply calibrated 2D coordinates, worst-case uncertainty bounds with source hashes and check results to CAD-09. Preserve the specific source scope and current revision.

<a id="sim-01"></a>

## SIM-01 — Prepare the source-bound mast idealization

1. **Sources:** [Source contract](../examples/files/wind-generator/simulation-handoff.md); [Supporting source 1](../examples/files/wind-generator/simulation-handoff.md); [Supporting source 2](../examples/files/wind-generator/0deg-job.json); [Supporting source 3](../examples/files/wind-generator/input-register.json); [Supporting source 4](../examples/files/wind-generator/ideal-base-screening.md)
2. **Evidence status:** existing_implementation_or_execution_record_inspected
3. **Inputs:** native mast CAD; geometry/mesh metadata; source-classified loads/materials
4. **Outputs:** beam/plate/cable model; solver job and input record
5. **Prerequisites:** Selected square-mast geometry; Existing connection/material evidence; Authorized support idealization
6. **Tool/API:** Existing build_mesh.py; prepare_job.py; screening_job.py
7. **Geometry representation:** input: native mast CAD; geometry/mesh metadata; source-classified loads/materials; output: beam/plate/cable model; solver job and input record
8. **Units and frames:** CAD mm; structural mesh m; loads N; stress Pa; retain global coordinates and wind direction.
9. **Metric evidence:** Native mast hash matches the 0-degree job source_native_sha256; source-classified elastic and yield inputs accompany the model.
10. **Information preserved:** Original input bytes, source identity and attributed units/frames
11. **Information changed/inferred:** Idealizes upper members as beams/plates and replaces local base mechanics with the authorized rigid assembled support
12. **Checks:** Verify units, mesh connections and welded coupling; Check supports/load locations; Bind job to CAD and geometry hashes
13. **Alternatives:** Detailed solid/contact base model retained in source project
14. **Downstream operations:** SIM-02
15. **Handoff conditions:** Supply beam/plate/cable model, solver job and input record with source hashes and check results to SIM-02. Preserve the specific source scope and current revision.

<a id="sim-02"></a>

## SIM-02 — Solve retained mast load cases and extract fields

1. **Sources:** [Source contract](../examples/files/wind-generator/ideal-base-screening.md); [Supporting source 1](../examples/files/wind-generator/ideal-base-screening.md); [Supporting source 2](../examples/files/wind-generator/0deg-metrics.json); [Supporting source 3](../examples/files/wind-generator/45deg-metrics.json)
2. **Evidence status:** existing_implementation_or_execution_record_inspected
3. **Inputs:** source-bound solver job; gravity and pretension state; 15 m/s wind direction
4. **Outputs:** saved displacement/force/stress metrics; native MED fields
5. **Prerequisites:** Prepared model and exact case identity; Recorded loads/materials; Existing equilibrium state
6. **Tool/API:** Code_Aster 17.4.0; Existing run_wind_baseline.py; extract_results.py
7. **Geometry representation:** input: source-bound solver job; gravity and pretension state; 15 m/s wind direction; output: saved displacement/force/stress metrics; native MED fields
8. **Units and frames:** m, N, Pa in the job global frame; incoming directions 0 and 45 degrees.
9. **Metric evidence:** Retained completed cases: mast-top horizontal displacement 0.04001972618323231 m at 0 degrees and 0.03315978721065512 m at 45 degrees.
10. **Information preserved:** Original input bytes, source identity and attributed units/frames
11. **Information changed/inferred:** Calculates elastic equilibrium and source-defined stress comparisons
12. **Checks:** Native input checks; Equilibrium and extraction outcome; Assigned member-yield comparison; Keep plate resultants distinct from surface stresses
13. **Alternatives:** Read saved metrics without rerunning a solver
14. **Downstream operations:** SIM-03
15. **Handoff conditions:** Supply saved displacement/force/stress metrics, native MED fields with source hashes and check results to SIM-03. Preserve the specific source scope and current revision.

<a id="sim-03"></a>

## SIM-03 — Inspect mast fields and compare cases

1. **Sources:** [Source contract](../examples/files/wind-generator/ideal-base-screening.md); [Supporting source 1](../examples/files/wind-generator/ideal-base-screening.md); [Supporting source 2](../images/manifest.json)
2. **Evidence status:** existing_implementation_or_execution_record_inspected
3. **Inputs:** saved MED fields; case identities; member comparison arrays
4. **Outputs:** displacement capture; yield-comparison capture
5. **Prerequisites:** Saved fields and source metrics; Verified case-to-panel mapping
6. **Tool/API:** ParaView MEDReader; Existing prepare_comparison_view.py; export_stress_limits.py
7. **Geometry representation:** input: saved MED fields; case identities; member comparison arrays; output: displacement capture; yield-comparison capture
8. **Units and frames:** Displacement colours in m; displayed deformation scale 1; yield/stress ratio dimensionless.
9. **Metric evidence:** Existing images show two incoming directions with consistent scales and stated coefficient bands.
10. **Information preserved:** Original input bytes, source identity and attributed units/frames
11. **Information changed/inferred:** Maps saved quantities to colours and captures; retains numerical result data
12. **Checks:** Match case/cell identity; Verify scalar units and deformation scale; Preserve unevaluated-element labels
13. **Alternatives:** Saved magnified-displacement view with explicit display multiplier
14. **Downstream operations:** Example documentation
15. **Handoff conditions:** Supply displacement capture, yield-comparison capture with source hashes and check results to Example documentation. Preserve the specific source scope and current revision.
