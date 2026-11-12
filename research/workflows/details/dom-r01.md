# DOM-R01 — Raster plan and site survey to registered IFC

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 5/5; setup 5/5; computing 4/5.**

Output: IFC4 project with site/building/storey hierarchy, explicit IfcWall and IfcOpeningElement records, a scan-to-building registration transform, IFC-derived mesh, and optional Blender/GLB inspection derivative.

## Comparison conditions

Full route assumes a correctly scaled plan, a modest static site, overlapped photos, calibrated depth frames, and surveyed controls in shared frames. IFC-only from a clean vector plan skips SfM/MVS and scan registration. The image/mesh route supplies appearance/surface evidence; it does not create valid building semantics without authored classifications.

## Registered starting artifact types

1. text
2. raster-plan
3. photo-set
4. depth-frames
5. dimensions
6. measurement-set
7. source-library

## Detailed source and preparation artifacts

1. Type: text; Formats: UTF-8 text/Markdown/JSON; Minimum quality: Named project, building use and intended elements; ambiguities recorded.; Required evidence: original text; revision/source; Handling: Normalize into model-brief; preserve wording and revisions.
2. Type: raster-plan; Formats: PDF; PNG; TIFF; Minimum quality: Readable plan view with known scale or surveyed control lengths, north/orientation and floor datum.; Required evidence: original page/image; scale source; control IDs; Handling: Do not scale from page display size.
3. Type: dimensions; Formats: JSON/CSV/field notes; Minimum quality: Units and datum beside each value; dimensions can be traced to plan pixels or survey.; Required evidence: value; unit; point/feature IDs; status; source; Handling: Input to geometry; no silent defaults.
4. Type: photo-set; Formats: JPG/PNG/HEIC converted with source retained; Minimum quality: Static scene with overlap, sharp exposure and sufficient texture; camera/lens metadata retained.; Required evidence: image IDs; timestamps; camera intrinsics if known; rights; Handling: Frames can be sampled from video but retain original frame mapping.
5. Type: depth-frames; Formats: sensor-native images; depth TIFF/PNG; PLY/PCD exports; Minimum quality: Depth scale, intrinsics, sensor-to-rig extrinsics, invalid-depth mask and capture pose/time.; Required evidence: sensor model; units; calibration; frame IDs; Handling: Preserve raw depth frames.
6. Type: measurement-set; Formats: JSON/CSV; Minimum quality: Independent control point coordinates and lengths in named frames, with uncertainty/status.; Required evidence: control IDs; source/target coordinates; units; uncertainty; Handling: Separate registration controls and held-out checks.
7. Type: source-library; Formats: IFC asset; native CAD; library record; Minimum quality: Exact asset file/revision and item-level terms.; Required evidence: URL/path; hash; licence/terms; part identity; units/frame; Handling: Do not treat catalog access as a blanket content licence.

## Reference points, datums and coordinate frames

1. Kind: project origin; Fields: origin identifier; project-local XYZ; north direction; vertical datum; Frame: Project-local engineering frame; X east, Y north, Z up only when explicitly selected.; Source status: author/surveyor supplied
2. Kind: site control point; Fields: point ID; E/N/H or local XYZ; uncertainty; survey method; Frame: survey/map frame ↔ project frame; Source status: measured control
3. Kind: storey datum; Fields: storey name; elevation_m; vertical datum; Frame: project Z; Source status: measured or plan source
4. Kind: wall axis; Fields: p1/p2 XYZ; height; thickness; local +X and +Y directions; Frame: project plan frame and wall-local frame; Source status: dimensioned input
5. Kind: opening frame; Fields: host wall ID; station along wall; sill elevation; width/height/depth; Frame: host wall-local frame; Source status: dimensioned input
6. Kind: camera/sensor transform; Fields: intrinsics; camera-to-rig; rig-to-world pose; timestamps; Frame: camera optical → rig → project/world; Source status: calibrated or estimated; store residual/status
7. Kind: IFC georeference; Fields: projected CRS; map conversion eastings/northings/height; X-axis abscissa/ordinate; scale; Frame: project engineering frame → map frame; Source status: survey/CRS authority; never inferred from image appearance

## Software, libraries and dependencies

1. Name: IfcOpenShell; Role: semantic IFC creation, geometry and unit API; Software license: LGPL-3.0-or-later for Python library per repository; Bonsai add-on is GPL-3.0-or-later; Api or entrypoint: ifcopenshell.api.project.create_file; root.create_entity; unit.assign_unit; context.add_context; geometry.create_2pt_wall; feature.add_feature; aggregate.assign_object; spatial.assign_container; georeference.edit_georeferencing; Environment dependencies: Python + IfcOpenShell wheel/native geometry backend; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: IFC creation uses explicitly supplied geometry and semantic classes; retain source-specific asset rights.; Source urls: https://github.com/IfcOpenShell/IfcOpenShell; https://docs.ifcopenshell.org/ifcopenshell-python/code_examples.html; https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html
2. Name: COLMAP; Role: image feature matching, camera solution, sparse and dense reconstruction; Software license: BSD-3-Clause software; dependencies separately licensed; Api or entrypoint: colmap feature_extractor; exhaustive_matcher; mapper; image_undistorter; patch_match_stereo; stereo_fusion; Environment dependencies: COLMAP binary; CUDA GPU for dense PatchMatch route; CPU feature/matching options; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Monocular camera solve has arbitrary scale until external control. Dense route increases GPU-memory and storage demand.; Source urls: https://colmap.github.io/cli.html; https://colmap.github.io/faq.html; https://github.com/colmap/colmap/blob/main/doc/license.rst
3. Name: Open3D; Role: point-cloud I/O and scan registration/refinement; Software license: MIT software; Api or entrypoint: open3d.pipelines.registration.registration_icp; evaluate_registration; Environment dependencies: Python Open3D + NumPy; initial transform must be supplied; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: ICP is local refinement and may converge to wrong surface without a good initial alignment and held-out controls.; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html; https://github.com/isl-org/Open3D/blob/main/LICENSE
4. Name: Blender + Bonsai; Role: IFC display/authoring inspection and scene view; Software license: Blender GPL-3.0-or-later; Bonsai GPL-3.0-or-later; asset licences independent; Api or entrypoint: Blender `--background --python`; Bonsai IFC import/export UI; bpy scene/object APIs; Environment dependencies: Blender build, matching Bonsai add-on and compatible IfcOpenShell; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: GLB is display-oriented and can omit/remap IFC classifications, relationships and property sets.; Source urls: https://docs.blender.org/manual/en/latest/advanced/command_line/; https://github.com/IfcOpenShell/IfcOpenShell; https://www.blender.org/features/pipeline/

## Procedure

1. Action: Normalize the source brief; resolve explicit units, local axis convention, storeys and source IDs.; Tool: Project intake; Command or api: DOM-01 model-brief contract; preserve original text and dimensions.; Preserves: Raw wording, measurement provenance.; Changes or infers: Typed requirements, names and unit normalization.; Check: Reject required values without source/unit/status; record questions instead of assigning geometry.; Code status: existing_tool_entrypoint
2. Action: Create IFC project, units, contexts and spatial hierarchy.; Tool: IfcOpenShell API; Command or api: IfcOpenShell project.create_file(version="IFC4"), unit.assign_unit, root.create_entity and aggregate.assign_object.; Preserves: Source plan, controls and IDs.; Changes or infers: New IFC4 file and relationships.; Check: Inspect schema, units, project/site/building/storey aggregates, unique GlobalIds.; Code status: existing_tool_entrypoint
3. Action: Author each wall from its measured endpoints; author rectangular openings only from explicit dimensions.; Tool: IfcOpenShell API; Command or api: `geometry.create_2pt_wall(..., is_si=True)`, `geometry.add_wall_representation`, `geometry.assign_representation`, `feature.add_feature`, `spatial.assign_container`.; Preserves: Dimension records and named wall/opening IDs.; Changes or infers: Parametric wall-like extrusion and void relationship.; Check: Compare wall axes, thickness and opening station/sill/clear dimensions to source.; Code status: existing_tool_entrypoint
4. Action: Solve image cameras and dense surface evidence when photos are in scope.; Tool: COLMAP CLI; Command or api: `colmap feature_extractor --database_path <db> --image_path <images>`; `colmap exhaustive_matcher --database_path <db>`; `colmap mapper --database_path <db> --image_path <images> --output_path <sparse>`; `colmap image_undistorter --image_path <images> --input_path <sparse-model> --output_path <dense>`; `colmap patch_match_stereo --workspace_path <dense>`; `colmap stereo_fusion --workspace_path <dense> --output_path <dense>/fused.ply`.; Preserves: Original images, frame IDs, camera metadata and sparse reconstruction.; Changes or infers: Camera poses and dense point cloud; monocular scale remains unknown absent controls.; Check: Reprojection, component coverage, independent scale controls, holes and withheld dimensions.; Code status: existing_tool_entrypoint
5. Action: Register depth/image cloud to the project/building frame from measured controls, then refine only with a checked initialization.; Tool: Open3D; Command or api: `registration_icp(source, target, max_correspondence_distance, init)`; record `RegistrationResult.transformation`, fitness and inlier RMSE.; Preserves: Original clouds, control IDs and frame names.; Changes or infers: Registration transform and aligned cloud.; Check: Use held-out point/length controls, local residual maps and frame/unit readback.; Code status: existing_tool_entrypoint
6. Action: Convert IFC elements to triangle geometry or B-rep for downstream visualization/analysis.; Tool: IfcOpenShell geometry API / IfcConvert; Command or api: `ifcopenshell.geom.iterator(settings, ifc_file)` or `ifcopenshell.geom.create_shape(settings, element)`; retain IFC GlobalId-to-output mapping.; Preserves: IFC source and element identities.; Changes or infers: Tessellated or B-rep derivative; semantics are not carried as full IFC relations.; Check: Compare element count, bounds, units and placement against source IFC.; Code status: existing_tool_entrypoint
7. Action: Inspect semantic model and visual derivatives.; Tool: Blender/Bonsai; Command or api: Open IFC in Bonsai; or `blender --background --python <review_scene.py>` for a scripted display scene.; Preserves: IFC source and conversion manifest.; Changes or infers: Scene/render/GLB derivative.; Check: Reopen exported file; retain element IDs and transform manifest.; Code status: existing_tool_entrypoint

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-01; Name: Normalize model brief; Inputs: text; Outputs: model-brief; Tools: existing OCS engineering skill; structured project schema proposal; Source urls: [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); Prerequisites: Input sources retained with identity and access terms.; Preserves: Original wording, measurements, source units, source frame and evidence status.; Changes or infers: Normalize names and units; separate measured values, source claims, assumptions and calculated values.; Checks: Every required parameter has value/status/unit/source or a recorded ambiguity.; Alternatives: Manual brief review; schema-driven intake form.; Automation: mixed; Evidence status: local_source_inspected; Summary: Create a source-linked requirements record before geometry operations.; Source ids: DSRC-01; DSRC-02; Input alternatives: dimensions; measurement-set
2. Id: DOM-18; Name: Raster floor plan to IFC building; Inputs: raster-plan; dimensions; measurement-set; source-library; model-brief; Outputs: ifc; Tools: Image calibration; OCS/FreeCAD sketching; Bonsai/IfcOpenShell; Source urls: [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html; Prerequisites: Known plan scale/control lengths, orientation, floor elevation and interpretation rules for walls/openings.; Preserves: Original raster, scale transform, interpreted linework, dimension sources and uncertain regions.; Changes or infers: Pixels interpreted as boundaries and building elements; semantic classification is human/model inference.; Checks: Wall thickness, openings, elevations, spatial containment, area/element checks and IFC validation.; Alternatives: Vector drawing to sketch if original CAD exists; manual IFC authoring for high-confidence boundaries.; Automation: assisted; Evidence status: documented_capability; Summary: Build semantic IFC from a raster plan, normalized building brief, dimensions, measured controls and licensed component sources; document scale, axes, elevations and interpretation decisions.; Source ids: DSRC-01; DSRC-25
3. Id: DOM-20; Name: Photos/video to camera solution, point cloud and mesh; Inputs: photo-set; Outputs: camera-solution; point-cloud; Tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG/OpenMVS; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); Prerequisites: Overlapping sharp views, camera metadata/calibration where available, scene motion/lighting assessed and scale controls identified.; Preserves: Original frames, camera solution, control points, reconstruction settings, sparse/dense outputs.; Changes or infers: Videos sampled into images; camera poses and dense surfaces are estimated from image correspondences.; Checks: Registered-view coverage, reprojection residuals, independent scale distances, surface holes and withheld checks.; Alternatives: RGB-D/LiDAR for metric depth; single-image learned mesh only for visual proposal.; Automation: scripted; Evidence status: documented_capability; Summary: Reconstruct visible geometry and camera poses from image sequences; monocular scale requires external controls.; Source ids: DSRC-33
4. Id: DOM-21; Name: Depth frames to registered point cloud or mesh; Inputs: depth-frames; measurement-set; Outputs: point-cloud; Tools: Open3D; CloudCompare; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); Prerequisites: Sensor model, calibration, units, extrinsics and depth validity/range known.; Preserves: Raw depth/color, frame timestamps, sensor coordinates and transforms.; Changes or infers: Registration, filtering and surface fusion combine depth samples into new geometry.; Checks: Loop closure, registration residual, independent lengths, depth noise and coverage.; Alternatives: Photogrammetry for passive optical scenes; per-frame point cloud where fusion is inappropriate.; Automation: mixed; Evidence status: documented_capability; Summary: Fuse calibrated depth observations into metric geometry while retaining the raw sensor frames.; Source ids: DSRC-33
5. Id: DOM-19; Name: Register scan to building frame; Inputs: ifc; measurement-set; point-cloud; Outputs: registration-transform; point-cloud; Tools: COLMAP/AliceVision; Open3D/CloudCompare; IFC geometry as reference; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); Prerequisites: At least one common frame datum and distributed control points/lengths; scan sensor calibration available.; Preserves: Raw images/depth, capture settings, raw reconstruction and all transforms.; Changes or infers: Aligns the scan to IFC coordinates; registration adjusts pose/scale, not building semantics.; Checks: Registration residuals and held-out distances; check local regions separately and flag occlusion.; Alternatives: Surveyed control transformation; ICP refinement after coarse frame alignment.; Automation: mixed; Evidence status: documented_capability; Summary: Register the scan point cloud to the IFC/building frame using measured controls; output the transform and aligned point cloud. Camera poses are not created unless camera observations are supplied.; Source ids: DSRC-33; DSRC-13
6. Id: DOM-16; Name: Extract IFC geometry as triangles; Inputs: ifc; Outputs: mesh; Tools: IfcOpenShell geom.create_shape/iterator; IfcConvert; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html; Prerequisites: IFC schema and length units read; target representation chosen.; Preserves: IFC source, GlobalId/entity map, item/material IDs and object placement.; Changes or infers: Geometry API can emit tessellated triangles or OpenCASCADE B-rep; extraction is a derived geometry view.; Checks: Element ID mapping, bounds, face/solid count, volume and units against source; relationships remain in IFC.; Alternatives: Triangulation for display/clash; B-rep where analytic editing/surface inspection is required.; Automation: scripted; Evidence status: documented_capability; Summary: Extract IFC geometry as tessellated triangles and retain its element mapping.; Source ids: DSRC-28; DSRC-29
7. Id: DOM-17; Name: IFC to GLB display scene; Inputs: ifc; Outputs: visual-scene; Tools: IfcOpenShell IfcConvert; Blender; GLB export; Source urls: https://docs.ifcopenshell.org/introduction.html; https://www.blender.org/features/pipeline/; [provenance.json](/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json); Prerequisites: Element-to-display mapping and length/orientation conversion are declared.; Preserves: IFC source/hash; stable element IDs; source properties in sidecar mapping where GLB cannot retain them.; Changes or infers: BIM objects become render nodes/meshes; semantic/relationship data may be reduced or remapped.; Checks: ID-to-node coverage, bounds, orientation, selected geometry hashes or residuals, output hashes.; Alternatives: Use IFC-native viewer when BIM relationships/properties are the primary task.; Automation: scripted; Evidence status: documented_capability; Summary: Create a visual GLB derivative with provenance and object mapping, not a replacement IFC.; Source ids: DSRC-30; DSRC-31; DSRC-32

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Entrypoint: `IfcOpenShell API: project.create_file, root.create_entity, unit.assign_unit, aggregate.assign_object, geometry.create_2pt_wall, geometry.edit_object_placement and feature.add_feature; author supplied building dimensions and semantic relationships.`; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html

## Output artifacts

1. Type: ifc; Format: IFC4 STEP physical file; Retained: IfcProject/site/building/storeys, IfcWall entities, IfcOpeningElement voids, placements, declared metre units, GlobalIds and optional supplied CRS/map conversion.; Loss or inference: This helper lacks material/property sets, room/space topology, door/window fillings, arbitrary wall polygons, plan interpretation and IFC validation report.
2. Type: point-cloud; Format: PLY/PCD or sensor-native; Retained: Measured/scanned XYZ and registered source transform.; Loss or inference: Registration refines but does not change source point observations; filtering/fusion must be a separately versioned derivative.
3. Type: visual-scene; Format: Blender .blend or GLB/glTF; Retained: Displayed IFC-derived object IDs and scene transforms when adapter records them.; Loss or inference: Display meshes do not retain complete IFC semantic graph; GLB material/render settings may differ.

## Checks

1. IFC schema parse and expected IFC4 file header.
2. Project length/area/volume units equal declared inputs.
3. Every wall has a unique GlobalId and storey containment; each opening has a unique GlobalId and expected representation.
4. `IfcRelVoidsElement` connects each opening to exactly its host wall; opening/wall local transforms agree.
5. Bonsai/IfcConvert independent reopen; compare bounds, volume, orientation and IDs.
6. Registration controls vs held-out control residuals, in local regions and units.
7. COLMAP camera reprojection and depth/photogrammetry overlap; metric scale only with source controls.

## Failure recovery

1. Plan scale or north conflict: keep input unchanged; fix the calibration record, regenerate a new IFC path and compare reports.
2. Missing openings or invalid IFC feature relation: inspect per-wall opening dimensions and rerun against new target, not the old file.
3. COLMAP disconnected camera clusters: separate reconstruction components, add overlap images or supply known camera poses; do not merge by visual guess.
4. ICP drift: return to survey control correspondences and global registration; do not accept local RMSE alone.
5. Low memory: reduce image resolution/patch source count or omit MVS; keep the sparse camera solve and label result as surface-incomplete.

## Effort and computing classification

1. **Human:** 5
2. **Setup:** 5
3. **Compute:** 4
4. **Human reason:** Plan interpretation, element classification, multi-source registration and georeferencing require expert decisions. IFC-only from an already vectorized/dimensioned plan is substantially easier.
5. **Setup reason:** Combines IFC authoring, camera solve/MVS, point-cloud registration, model licensing and geometry/display adapters.
6. **Compute reason:** Sparse reconstruction and IFC creation are CPU/modest; dense multi-view stereo, multiple image batches and large point clouds dominate. DOM contract rates the complete plan+survey+registered IFC path.

## Resources and scaling

1. **Cpu:** CPU for API/IFC parsing and controls; multithreading for geometry/reconstruction.
2. **Gpu:** COLMAP dense PatchMatch benefits from CUDA-capable GPU; CPU-only feature/matching path exists; depth registration can remain CPU.
3. **Ram:** IFC graph size, raster dimensions, number of cameras, dense depth maps and point count drive RAM.
4. **Storage:** Original images/depth frames, SfM database, dense depth maps, clouds, IFC and display derivatives; preserve separate source and output trees.
5. **Scaling drivers:** pixel dimensions and photo count; depth frame count/resolution; mesh/cloud points and IFC element count; camera graph connectedness; stored copies of intermediate depth maps
6. **Variants:** Vectorized plan and no survey MVS lower effort and compute.; Photos without control points yield reconstruction with arbitrary scale.; Depth frames calibrated to survey frame reduce SfM workload.; BIM semantics remain human-authored even with high-quality surfaces.

## Detailed branch procedures

1. [cad-r03.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r03.md)
2. [rec-r01.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r01.md)
3. [rec-r09.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r09.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. [https://docs.ifcopenshell.org/ifcopenshell-python/code_examples.html](https://docs.ifcopenshell.org/ifcopenshell-python/code_examples.html)
2. [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html)
3. [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html)
4. [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/unit/assign_unit/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/unit/assign_unit/index.html)
5. [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/edit_object_placement/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/edit_object_placement/index.html)
6. [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/georeference/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/georeference/index.html)
7. [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html)
8. [https://github.com/IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)
9. [https://docs.bonsaibim.org/guides/authoring/georeferencing.html](https://docs.bonsaibim.org/guides/authoring/georeferencing.html)
10. [https://colmap.github.io/cli.html](https://colmap.github.io/cli.html)
11. [https://colmap.github.io/faq.html](https://colmap.github.io/faq.html)
12. [https://github.com/colmap/colmap/blob/main/doc/license.rst](https://github.com/colmap/colmap/blob/main/doc/license.rst)
13. [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)
14. [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html)
15. [https://github.com/isl-org/Open3D/blob/main/LICENSE](https://github.com/isl-org/Open3D/blob/main/LICENSE)
16. [https://docs.blender.org/manual/en/latest/advanced/command_line/](https://docs.blender.org/manual/en/latest/advanced/command_line/)
17. [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
