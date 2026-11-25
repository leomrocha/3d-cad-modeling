# Tools

## Reusable native construction and recovery

1. [Stable record pagination](../scripts/cadtools/records.py) — bounded page-size recovery and native document/revision binding.
2. [Durable progress checkpoints](../scripts/cadtools/checkpoints.py) — ordered stage evidence and verified IN_PROGRESS saves that audit the intended DWG path.
3. [Plate operations](../scripts/plate_reference.py) — supplied outlines, bulges, holes, transforms, actual sidewall checks, flat pin-seat relief, equal-angle countersunk fit and tangent runs with equal-radius belt wraps.
4. [Planar profiles](../scripts/planar_profiles.py) — bounded native extrusion, analytic circular opening clipping, rectangular-face overlap, hollow-section end perimeters, two-circle tangent hulls and round-ended slots. Includes concentric quarter-bend and offset Z sections, signed cardinal profile reframing, annular seat area interrupted by a radial slot and an ellipse chord error bound for sampled trims. The two-circle band test checks a projected box against the inner opening and the outer boundary. The straight-profile section helper returns all material intervals at a named station and preserves gaps in concave outlines. The rolling-corner helper returns a supported round-body centre arc and a bound for its chord approximation.
5. [Component insertion](../scripts/assembly_build.py) — source hashes, exact interactive prompts, native metadata and saved placements.
6. [Assembly occurrences](../scripts/assembly_occurrences.py) — nested part quantities, revision-pinned catalogue BOMs, mirrored hands and original insertion-journal recovery.
7. [Native views](../scripts/native_views.py) — native SAT/SAB boundary samples, native lines and straight polyline centrelines, nested placements and hashed SVG/PNG orthographic/isometric views. PNG rendering batches edge paths and endpoint markers into separate collections without joining paths.
8. [Encoding-aware native geometry](../scripts/native_geometry.py) — stable SAT/SAB readback, OCS points, straight polyline segments, placed vertex extrema and circular cylinder supports in assembly coordinates.
9. [Source vector paths](../scripts/source_vector_paths.py) — bounded SVG segment grammar, affine frames and explicit unit conversion.
10. [batch_request.py](../scripts/batch_request.py) prepares ordered CAD operation rows from shared or per-target values, normalizes lengths and angles, and supplies execution rows for an operation with verified readback. [CAD batch procedure](../skills/cad-ocs-engineering/SKILL.md#prepare-a-batch-of-cad-operations).
11. [batch_dxf_lines.py](../scripts/batch_dxf_lines.py) applies reviewed lengths to modelspace DXF LINE entities with ezdxf. It preserves each start and direction, writes a new DXF, and reopens it to measure the selected lines. [CAD batch procedure](../skills/cad-ocs-engineering/SKILL.md#prepare-a-batch-of-cad-operations).
12. [batch_selection.py](../scripts/batch_selection.py) resolves occurrence paths, named selections and measured conditions against a model inventory. It records local geometry and composed placements, then checks target and reference identity and measurements after reopening. [Batch selection procedure](../skills/cad-ocs-engineering/SKILL.md#resolve-batch-targets-against-measured-geometry).
13. [batch_dxf_inventory.py](../scripts/batch_dxf_inventory.py) reads DXF modelspace groups, LINE, CIRCLE, POINT and LWPOLYLINE geometry, and block definitions reached by single rigid INSERT entities. It binds the inventory to the drawing SHA-256. [Batch selection procedure](../skills/cad-ocs-engineering/SKILL.md#resolve-batch-targets-against-measured-geometry).
14. [planar_positions.py](../scripts/planar_positions.py) generates ordered plane and world coordinates from explicit positions, paths, polygons, circles or bounded regions with cutouts. Path spacing supports distance along the curve or direct distance between points. Results carry position IDs and can include direction vectors. [Planar positions procedure](../skills/cad-ocs-engineering/references/planar-positions.md).
15. [spatial_positions.py](../scripts/spatial_positions.py) generates parent and world placement transforms for occurrences on prisms, cylinders and spheres or inside prism volumes. It checks requested distances between position pairs. [3D placement procedure](../skills/cad-ocs-engineering/references/spatial-positions.md).
16. [row_spacing.py](../scripts/row_spacing.py) calculates row stations, adjacent pitches and border margins along a line, circular arc or Bézier segment. It also checks shortest and directed gaps between supplied profiles or spheres. [Row spacing procedure](../skills/cad-ocs-engineering/references/row-spacing.md).
17. [batch_dxf_placement.py](../scripts/batch_dxf_placement.py) previews, applies and resumes moves of existing DXF INSERT entities in a job-owned drawing. [Existing occurrence placement procedure](../skills/cad-ocs-engineering/references/existing-batch-placement.md).
18. [batch_dxf_frames.py](../scripts/batch_dxf_frames.py) measures the block-base position and axes of rigid DXF INSERT entities and verifies saved placements, entity identities, block definitions and independent geometry.

19. [batch_creation.py](../scripts/batch_creation.py) creates and verifies oriented DXF circles, STEP through-holes and blind bores, and XCAF assemblies of catalogue-selected STEP solids. [Batch creation procedure](../skills/cad-ocs-engineering/references/batch-creation.md).
20. [batch_modification.py](../scripts/batch_modification.py) enlarges selected STEP bores, applies reviewed XCAF bar length and occurrence name changes, and runs the `replace occurrence` action. [Batch modification procedure](../skills/cad-ocs-engineering/references/batch-modification.md).
21. [batch_xcaf_bars.py](../scripts/batch_xcaf_bars.py) isolates selected XCAF occurrence paths, resizes plain rectangular bars about a fixed anchor and edits occurrence names.
22. [batch_replacement.py](../scripts/batch_replacement.py) replaces selected XCAF leaf definitions with a catalogue-selected STEP solid and aligns measured rectangular keyed seats. [Batch replacement procedure](../skills/cad-ocs-engineering/references/batch-replacement.md).

23. [batch_delivery.py](../scripts/batch_delivery.py) runs qualified batch writers and reports measured results and remaining targets. [Batch delivery procedure](../skills/cad-ocs-engineering/references/batch-delivery.md).

24. [batch_sample_readback.py](../scripts/batch_sample_readback.py) reopens the source and saved CAD sample to verify the registered method changed the requested geometry or property.

The [reusable integration procedure](../skills/cad-ocs-engineering/references/generic-integration.md) defines inputs, outputs, units, representation limits and recovery conditions. Component data remains caller supplied.

## Software

1. **Python** runs the helper scripts. Dependencies are pinned in [requirements-native.txt](../requirements-native.txt).
2. **OpenCADStudio** provides the native CAD session via MCP server used by the construction and inspection skills.

## Skills

1. [cad-ocs-engineering](../skills/cad-ocs-engineering/SKILL.md) — combines the full OCS modeling contract, session control, component iteration, geometry checks, saved-model verification and computational handoff instructions.
2. [cad-drawing-inspection](../skills/cad-drawing-inspection/SKILL.md) — guides the agent through reading a DXF's units, layers, blocks and source shapes.
3. [cad-source-intake](../skills/cad-source-intake/SKILL.md) — records the request, source files, hashes and corrections as a new input revision.

4. [CAD MCP translator](../skills/cad-mcp-translator/SKILL.md) — maps and verifies native operations for the chosen bridge.

The [skill catalogue](../skills/README.md) separates these installed skills from proposed workflows. Component-specific procedures are indexed in [cad-ocs-engineering](../skills/cad-ocs-engineering/SKILL.md).

## Files, sources and component records

1. [part_index.py](../scripts/part_index.py) — reads and searches a supplied parts index.
2. [model_inventory.py](../scripts/model_inventory.py) — finds attributed models and filename candidates before a new build, retains exact path/hash-bound different-component reviews, supports exact configuration selection, and preserves known 2D drawing roles through retained-copy hashes. [Start-check procedure](../skills/cad-ocs-engineering/references/existing-model-start-check.md).
3. [source_intake.py](../scripts/source_intake.py) — saves source indexes, request scope and revision receipts.
4. [component_records.py](../scripts/component_records.py) — checks required source values and records individual modeling actions.
5. [source_metadata.py](../scripts/source_metadata.py) — compares expected source labels with the strings stored on a CAD entity.
6. [source_variant_table.py](../scripts/source_variant_table.py) — selects a value from a reviewed table for the specified product variant. The [source procedure](../skills/cad-ocs-engineering/references/source-variant-tables.md) also binds fastener dimensions to the exact standard edition, grade, row and drawing symbol.

7. [retained_artifacts.py](../scripts/retained_artifacts.py) — verifies retained-file hashes, JSON/JSONL syntax, manifest paths and same-name asset sets for model package revisions. [Manifest procedure](../skills/cad-ocs-engineering/references/retained-artifact-checks.md).

## Drawings and construction

1. [dxf_inspect.py](../scripts/dxf_inspect.py) — lists DXF entities, units, layouts, layers and nested block transforms.
2. [calibrated_trace.py](../scripts/calibrated_trace.py) — converts image points to measured 2D coordinates using reference dimensions, scale and stated uncertainties.
3. [profile_reference.py](../scripts/profile_reference.py) — checks a supplied polygon, extrudes it as reference geometry and inspects the result.
4. [rounded_tube.py](../scripts/rounded_tube.py) — builds and checks a rounded hollow section from supplied dimensions.
5. [axial_motor.py](../scripts/axial_motor.py) — builds and checks the supported housing, shaft and mounting features of a source-bound motor job.
6. [envelope_reference.py](../scripts/envelope_reference.py) — builds and checks a rectangular reference volume from source dimensions.
7. [pixhawk.py](../scripts/pixhawk.py) — builds and checks the Pixhawk 6C mechanical envelope and nominal mounting-thread references.

8. [envelope_job_runner.py](../scripts/envelope_job_runner.py) — runs read-only preflight by default; an authorized write run builds a source-bound rectangular envelope, checks saved geometry and metadata, and closes its completed owned document. [Runner procedure](../skills/cad-ocs-engineering/references/envelope-job-runner.md).

9. [annular_reference.py](../scripts/annular_reference.py) — constructs a plain ring from source-bound bore diameter, outside diameter and thickness in millimetres. Checks analytic cylinder surfaces, end-face loops, closed-body topology and stored source metadata. [Annular-reference procedure](../skills/cad-ocs-engineering/references/annular-reference.md).
   [annular_job_runner.py](../scripts/annular_job_runner.py) executes caller-supplied source-bound annular jobs through preflight, guarded construction, readback, save/reopen and owned-document cleanup. [Annular job procedure](../skills/cad-ocs-engineering/references/annular-job-runner.md).

10. [hexagonal_reference.py](../scripts/hexagonal_reference.py) — constructs a regular hexagonal prism from source-bound across-flats dimension, height and a placement frame, with an optional source-bound bore. Checks side and cap planes, bore surfaces, topology and metadata. [Hexagonal-reference procedure](../skills/cad-ocs-engineering/references/hexagonal-reference.md).

11. [spherical_seat_profile.py](../scripts/spherical_seat_profile.py) — calculates a closed spherical-seat, collar, shaft and tangent-blend profile from caller-supplied dimensions. [Profile procedure](../skills/cad-ocs-engineering/references/spherical-seat-profile.md).

12. [conical_washer_profile.py](../scripts/conical_washer_profile.py) — constructs and checks a free conical washer from source-bound normal material thickness and radial/axial dimensions. [Conical-washer procedure](../skills/cad-ocs-engineering/references/conical-washer-profile.md).

## Circular-section ring geometry

1. [toroidal_reference.py](../scripts/toroidal_reference.py) — constructs and checks a nominal circular-section ring from source-bound inside and section diameters. [Toroidal-reference procedure](../skills/cad-ocs-engineering/references/toroidal-reference.md).

## Geometry, assemblies and component checks

Some of these are specialized tools for particular geometries. I still have work to do on these things.

1. [native_acis.py](../scripts/native_acis.py) — reads ACIS700 SAT topology and trimmed edge samples, plus SAB analytic surfaces and optional [circular boundary curves and adjacent faces](../skills/cad-ocs-engineering/references/circular-boundary-checks.md).
2. [step_solid_inventory.py](../scripts/step_solid_inventory.py) — inventories STEP solid definitions without counting nested shells as additional solids.
3. [step_placements.py](../scripts/step_placements.py) — reads supported STEP/native placement matrices, compares component positions and derives a root pose from a verified nested target frame, and plans guarded world-space translations for zero-base native INSERTs.
4. [assembly_units.py](../scripts/assembly_units.py) — prepares a unit-change plan for specified assembly root inserts, preserving internal geometry.
5. [assembly_repair.py](../scripts/assembly_repair.py) — applies a reviewed component-placement correction through the guarded CAD client.
6. [feature_checks.py](../scripts/feature_checks.py) — compares measured boundaries, cylinders and other native features with supplied expectations. The round-ended slot check matches native straight tangents on each requested face. Axis-aligned edge coverage compares split straight edges. `planar_bore_ligaments` checks material between circular bores through a common wall. `rectangular_plate_openings` verifies both face loops and their shared straight side faces. `orthogonal_plate_boundaries` extends the same check to polygonal plates with through notches and openings.
7. [small_bms.py](../scripts/small_bms.py) — compares supported solid points and assembly instances before and after saving.
8. [pillow_block.py](../scripts/pillow_block.py) — checks the supported bearing housing, rings, mounting slots and associated parts.
9. [battery_module.py](../scripts/battery_module.py) — checks the supported battery shells, terminals and tabbed-case patterns.
10. [driver_checks.py](../scripts/driver_checks.py) — checks the supported Sumitomo driver exterior and component features.
11. [cadtools/geometry.py](../scripts/cadtools/geometry.py) — native geometry adapter with guarded cylindrical and conical tools.

## CAD document cleanup

1. [ocs_document_cleanup.py](../scripts/ocs_document_cleanup.py) — closes the active owned document after matching its saved-file hash, persistence receipt and geometry revision; checks that unrelated documents retain their paths and dirty states. [Cleanup procedure](../skills/cad-ocs-engineering/references/document-cleanup.md).

## Installed packages and maintenance

1. [build_skill_packages.py](../scripts/build_skill_packages.py) — generates per-skill copies and source/hash manifests; `--finalize` regenerates and requires registration and isolated-installation checks, `--verify` performs final validation, and `--check` checks package synchronisation. [Completion procedure](../skills/cad-ocs-engineering/references/package-completion.md).
2. [package_check.py](../scripts/package_check.py) — verifies installed package hashes, imports and pinned dependency versions; component CAD also accepts a selected OCS session for a read-only state check.
3. [ocs_control.py](../scripts/ocs_control.py) — reads an existing authenticated native session and guards explicitly authorized mutation requests.
4. [check_contract.py](../scripts/check_contract.py) — checks caller-supplied point, axis and plane measurements against an explicit coordinate contract.
5. [cadtools runtime](../scripts/cadtools/runtime.py), [geometry](../scripts/cadtools/geometry.py) and [save/reopen verification](../scripts/cadtools/verification.py) — shared OCS adapters included in the component package. [Package contents and maintenance](skill-packaging.md).

## Running the tools

The file, index and DXF command-line helpers can be run from a terminal. Construction and check modules are imported by component jobs with their source values, model records and CAD client. [Setup and command examples](../README.md#installing).

## Source-bound screw reference

1. [hex_screw_reference.py](../scripts/hex_screw_reference.py) — constructs and inspects a caller-defined regular-hex head joined to a nominal cylindrical shaft. [Procedure](../skills/cad-ocs-engineering/references/hex-screw-reference.md).

## Exact source and partial-work checks

1. [exact_profiles.py](../scripts/exact_profiles.py) — complete ordered Line/Arc/clamped-NURBS loop matching and signed source extrusion direction.
2. [source_solid_checks.py](../scripts/source_solid_checks.py) — ACIS face sense, retained halfspaces, convex planar cell boundary volume and planar bilinear corner correspondence.
3. [Capture checks](../scripts/cadtools/captures.py) — document, revision, rendered frame, PNG integrity and stale-image diagnostics.
4. [Component records](../scripts/component_records.py) — completion gate binding final model evidence to an applied verified reusable change.

## Reversible source workflows

1. [profile_conditioning.py](../scripts/profile_conditioning.py) — caller-specified positive uniform profile/seed/depth conditioning and input roundtrip checks.
2. [solid_transfer.py](../scripts/solid_transfer.py) — complete unchanged native payload and original metadata verification with explicit bijective mappings.
3. [exact_profiles.py](../scripts/exact_profiles.py) — exact-fraction straight cubic certificates and explicitly allowed Line equivalence while preserving strict results.

## Insertion recovery, resume and assembly verification

1. [insert_recovery.py](../scripts/insert_recovery.py) — exact native INSERT default contracts, durable same-request continuation and completion checkpoints.
2. [assembly_verification.py](../scripts/assembly_verification.py) — indexed moving and fixed occurrence checks, geometry-bound nested occurrence matching, native geometry and placement differences across saved revisions, repeated source-world vertex matching, boundary sample matching with effective RGB and layer, optional unique endpoint attribution, signed axis-aligned placement checks and caller-defined envelope checks.
3. [assembly_build.py](../scripts/assembly_build.py) — guarded insertion-point compare-and-set correction with complete placement readback.
4. [cadtools/checkpoints.py](../scripts/cadtools/checkpoints.py) — source-pin merging, source-pinned incremental saves, exact same-document mutation recovery and verified resume gates.
5. [batch_insert_recovery.py](../scripts/batch_insert_recovery.py) starts or resumes modelspace block insertions in a job-owned DXF. It matches saved occurrences to journaled requests and checks dependencies before writing. [DXF insertion recovery procedure](../skills/cad-ocs-engineering/references/insertion-resume-verification.md#recover-a-batch-of-dxf-block-insertions).

[Correction sequence](../scripts/correction_sequence.py) reuses verified STEP or XCAF edits and executes dependent corrections.

## Rational surfaces and open mesh derivatives

1. [rational_surface.py](../scripts/rational_surface.py) — caller-bound rational B-spline evaluation at two precisions with transform before final rounding.
2. [mesh_checks.py](../scripts/mesh_checks.py) — triangle/UV numerical area, duplicate and oriented edge-incidence checks.
3. [mesh_dxf.py](../scripts/mesh_dxf.py) — source-pinned MESH-only DXF layer declarations with exact entity-tag readback.
4. [insert_recovery.py](../scripts/insert_recovery.py) — offline verification of a recorded cancellation and unchanged caller snapshots.

[Mesh repair evidence](../scripts/mesh_repair_evidence.py) compares original and added triangles in saved OBJ files and measures cylinder fit on selected original vertices.

## Translator-only helpers

1. [Operation planner](../translator/translator.py) validates a documented mapping against a captured tool inventory and selected connection.
2. [Local state ledger](../translator/state.py) stores verified revisions and unresolved native write intents.
3. [Bore fixture checker](../translator/bore_check.py) checks the fixture’s bore rims and wall against ASCII STL triangles.
4. [Installed package checker](../translator/package_check.py) checks the translator’s complete file inventory and hashes.

## CAD format translation

1. [Capability route planner](../format_translation/routes.py) checks directional tool declarations, argument bindings, dependencies and required properties across any selected connection.
2. [Conversion command](../format_translation/convert.py) generates verified STL, STEP or translated Python with optional local runtimes.
3. [SCAD source translator](../format_translation/scad_source.py) translates supported source constructs to editable CadQuery Python and reports unsupported source locations.
4. [Blender mesh exchange](../format_translation/blend_exchange.py) reads and writes native Blender scenes and STL meshes with explicit units or a measured reference.

[Native feature comparisons](../scripts/feature_checks.py) include `axial_datum_chain` for independently checked distances between consecutive axial datums and `feature_vertices(name, observed, expected, tolerance)`. Supply corners from one reopened solid and distinct source corners in the same millimetre frame. The result records each nearest vertex and its distance. Missing corners, a shared nearest vertex and out-of-tolerance matches fail the check.

[Recording checker](../skills/cad-model-navigation/scripts/check_recording.py) checks constant-rate video timing, chapter bounds and decoding using the installed ffprobe and ffmpeg commands.

[Native record readback](../scripts/cadtools/records.py) binds consumed EXTRUDE and REVOLVE profiles to completed command receipts.

## Service clearance

For a fixed-axis rotation sampled at increasing angles, `sampled_rotation_clearance` subtracts a bound on between-sample displacement and the supplied readback error to certify a continuous separation reserve.

1. [service_clearance.py](../scripts/service_clearance.py) checks static box and half-space separation, candidate contact dimension, rectangular support footprints on perforated plates, continuous planar linkage axis bounds, rectangular radial extrema for bend clearance, translated box-group margins, continuous box overlap and contact dimension, and axial source-section coverage and supplies exact coincidence witnesses for verified shared definitions. Includes planar translation pieces for checking a projected swept region against a saved wall opening and continuous axis-aligned quarter-turn hinge envelopes and a longitudinal bound over symmetric roll, pitch and yaw. The coaxial stack witness accepts either shaft direction and reports signed seat and interface gaps, final-layer reach and tip protrusion. The orthogonal sleeve check uses measured outer and inner radii and finite axial spans to prove separation or find a point inside both sleeve walls. The axial section clearance check refines a whole-part box candidate with a verified enclosure covering the full axial overlap. The finite Cartesian cylinder method builds conservative bounds from measured radius and end stations. The parallel-axis bore check verifies circular aperture clearance across a finite wall and the whole intersecting sweep. The guided pilot check bounds a circular section inside a round-ended slot throughout longitudinal travel and transverse guide play. The staged translation check carries poses forward and releases only the named occurrences that have completed their removal stages.

## Source assembly recovery and evidence

- [Job history archive](../scripts/job_history_archive.py) stores all regular files in a revision directory and verifies the manifest by streaming a read-only inventory.
- [Photo constraints](../scripts/photo_constraints.py) bounds undirected lines through a vanishing point using pick disks and back-projects a feasible line into its world plane.
- [Mounting patterns](../scripts/mounting_pattern.py) screens injective assignments against distance bounds and checks finite pin clearance at a supplied planar pose.
- [Mesh checks](../scripts/mesh_checks.py) reports shell components, closed-manifold vertex links, Euler characteristic and signed volume.
- [Source trim loops](../scripts/source_trim_loop.py) follows oriented edge uses, computes shared trim corners and independently checks curve endpoint and surface inverse residuals.
- [Finite solid contact](../scripts/finite_solid_contact.py) classifies finite solid pairs, checks inside witnesses and tests axial bore withdrawal with a numerical reserve with a caller-supplied OpenCascade environment.
- [STEP entity graph](../scripts/step_entity_graph.py) fingerprints simple STEP instance graphs and renumbers original simple or complex assignment payloads for a caller-owned wrapper.

[Orthographic landmark checks](../scripts/orthographic_checks.py) compare shared world coordinates and their worst-case uncertainty bounds across named drawing views.

[Catalogue candidate lookup](../scripts/catalogue_candidates.py) uses the configured CAD Models search helpers and resolves candidate IDs to hashed assets. [Job path resolution](../scripts/job_paths.py) derives portable path origins from the installed skill, selected job files and saved parts catalogue.

- [OpenCV probe and isolated setup](../skills/cad-opencv-setup/scripts/opencv_env.py) checks a named image operation and prepares a separate interpreter on request.
- [Private catalogue preparation](../scripts/private_catalogue.py) runs the CAD Models builder against supplied assets.
- [Raster feature extraction](../scripts/raster_features.py) returns pixel loops, ellipse candidates, an overlay and optional controlled plane coordinates.
- [Image observations](../scripts/image_observations.py) maps decoded instance masks and points into the original frame and finds leader endpoint candidates.
- [Local dimension text recognition](../scripts/raster_text.py) uses a supplied PaddleOCR model on a cropped text line and returns a source-linked receipt.

- [Prompted SAM segmentation](../scripts/sam_mask.py) runs a local SAM checkpoint on one source image and returns a source-linked instance mask with the prompt and model hashes.

## Modeling feature delivery

- [Find single-row deep-groove ball bearings by sourced designation, closure and side count](../scripts/bearing_variant.py)
- [standard_screw.py](../scripts/standard_screw.py) checks ISO 4017 screw variants against reviewed dimensions. It returns a catalogue asset or its length parameter when qualified, or generates and checks a cosmetic-thread STEP.
- [Fuse registered RGB-D surface measurements](../scripts/rgbd_surface.py)
- [Recover metric stereo depth and compare material regions](../scripts/registered_stereo.py)
- [Reconstruct and align camera locations](../scripts/camera_reconstruction.py)
- [Triangulate source landmarks and recover a dense surface](../scripts/calibrated_views.py)
- [Transfer a reference height between vertical landmarks](../scripts/photo_height.py)
- [Search partial meshes and mating interfaces](../scripts/shape_match.py)
- [Recover editable prismatic profile features](../scripts/shape_recover.py)
- [Vectorize freehand ink and propose sketch relations](../scripts/shape_sketch.py)
- [Infer an editable prismatic part from calibrated masks](../scripts/multiview_part.py)
- [Call and interpret deployed image providers](../scripts/vision_provider.py)
- [Run local SAM 2 with point or box corrections](../scripts/vision_provider_sam2.py)
- [Request an editable feature sequence from a selected model](../scripts/learned_cad_provider.py)
- [local_model_runtime.py](../scripts/local_model_runtime.py) applies offline model-library settings and validates user-supplied HTTP(S) inference addresses.
- [Build and verify source-bound feature sequences](../scripts/learned_cad_sequence.py)
- [Read native constraint conflicts and solve a corrected sketch](../scripts/learned_cad_solver.py)
- [Invoke a supplied Text2CAD runtime and decode its operations](../scripts/learned_cad_text2cad.py)

- [operation_catalogue.py](../scripts/operation_catalogue.py) checks approved modeling operations, lists available outputs and records method failures in the user’s local catalogue.
- [opencv_probe.py](../scripts/opencv_probe.py) checks the OpenCV functions for contours, four-point calibration and skeleton thinning in a selected interpreter.
