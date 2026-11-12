# DOM-R04 — CAD robot plus Menagerie model and scan environment to MJCF scene

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 5/5; setup 4/5; computing 3/5.**

Output: MJCF scene with a selected articulated robot, sourced environment collision geometry, cameras/visuals and explicit frame map.

## Comparison conditions

One named Menagerie robot at a pinned revision, compatible MuJoCo version, environment cloud registered to a measured scene frame, explicit robot-to-world placement.

## Registered starting artifact types

1. mjcf
2. cad-assembly
3. joint-set
4. measurement-set
5. photo-set
6. depth-frames
7. source-library

## Detailed source and preparation artifacts

1. Type: cad-assembly; Formats: FCStd; STEP + joint manifest; Minimum quality: Robot interface geometry and explicit frame records.; Required evidence: revision; mounting datums; units; Handling: Keep separate from Menagerie baseline.
2. Type: robot-assembly; Formats: Menagerie model folder/XML; Minimum quality: Per-model license and model revision retained.; Required evidence: robot ID; revision; license; MuJoCo version; Handling: Copy only under its terms.
3. Type: point-cloud; Formats: PLY/PCD; Minimum quality: Registered, metric environment cloud and transform provenance.; Required evidence: units; source frame; registration transform; Handling: Cloud alignment error recorded.
4. Type: measurement-set; Formats: JSON/CSV; Minimum quality: Robot mounting location and control points.; Required evidence: datum IDs; uncertainty; frame; Handling: Use independent checks.

## Reference points, datums and coordinate frames

1. Kind: robot base frame; Fields: base pose; mounting datum; Frame: robot base → world; Source status: survey/design
2. Kind: environment frame; Fields: point cloud origin; registration matrix; Frame: sensor/cloud → world; Source status: measured registration
3. Kind: joint frames; Fields: Menagerie joint bodies/axes; Frame: model-local joint → world via base pose; Source status: pinned XML

## Software, libraries and dependencies

1. Name: MuJoCo Menagerie; Role: reuse a model-specific robot MJCF; Software license: Apache-2.0 only for Franka Panda model; library is per-model licensed; Api or entrypoint: Pinned `franka_emika_panda/panda.xml`; README requires MuJoCo >=2.3.3; Environment dependencies: MuJoCo compatible release and licensed model assets; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Example Panda is only an example identity, not a selected robot.; Source urls: https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/README.md; https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/panda.xml
2. Name: Open3D; Role: cloud alignment and mesh/collision preparation; Software license: MIT code; cloud ownership remains separate; Api or entrypoint: Global registration then ICP refine; inspect `RegistrationResult.transformation`; Environment dependencies: Open3D + NumPy; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Registration cannot infer robot mounting intent.; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html
3. Name: MuJoCo; Role: compose scene and compile MJCF; Software license: Apache-2.0 software; assets per-item; Api or entrypoint: `MjSpec.from_file(...)` / XML model composition; `MjModel.from_xml_path(...)`; Environment dependencies: MuJoCo matching selected MJCF; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Check include/asset paths and namespaces for pinned version.; Source urls: https://mujoco.readthedocs.io/en/stable/programming/modeledit.html; https://mujoco.readthedocs.io/en/latest/XMLreference.html

## Procedure

1. Action: Pin Menagerie model revision and read its per-model terms/version.; Tool: Menagerie; Command or api: Use Panda `panda.xml` as a documented sample only, or select another permitted model explicitly.; Preserves: Upstream XML and source license; Changes or infers: Robot MJCF base.; Check: Verify XML, mesh hashes and revision.; Code status: existing_tool_entrypoint
2. Action: Register environment scan and robot mount to measured world controls.; Tool: Open3D + survey data; Command or api: Global registration then ICP with explicit initial transform; record matrix.; Preserves: Point cloud and controls; Changes or infers: Transform and aligned cloud.; Check: Held-out controls and residual map.; Code status: existing_tool_entrypoint
3. Action: Create collision environment geometry separately from visual surface.; Tool: Open3D / CoACD; Command or api: Downsample/simplify; decompose concave environment objects only if collision needs it.; Preserves: Registered cloud; Changes or infers: Collision meshes approximate; keep visual cloud/mesh.; Check: Bounds, scale, watertightness and contact test cases.; Code status: assisted
4. Action: Compose MJCF and compile.; Tool: MuJoCo; Command or api: Add robot at measured base pose, environment geoms and explicit assets; `MjModel.from_xml_path`.; Preserves: Pinned robot and transforms; Changes or infers: MJCF scene.; Check: Compile, asset resolution, base/joint frame checks.; Code status: assisted

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-06; Name: Library asset intake and rights record; Inputs: source-library; Outputs: component-record; Tools: component registry/schema proposal; source license review; Source urls: https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://github.com/google-deepmind/mujoco_menagerie; https://polyhaven.com/license; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280; Prerequisites: Original source identity and item-level license/terms available or explicitly unknown.; Preserves: Original file, URL, retrieved date, hash, attribution, license text/terms and source claims.; Changes or infers: Normalize metadata; derived conversions become separate assets with lineage.; Checks: License status per file; duplicate hash; units/frame; source part number and revision when stated.; Alternatives: Keep external link only where local caching/redistribution terms are unclear.; Automation: mixed; Evidence status: proposed_composition; Summary: Create immutable, rights-aware component records instead of treating catalogs as a common license.; Source ids: DSRC-07; DSRC-08; DSRC-09; DSRC-10; DSRC-11
2. Id: DOM-08; Name: CAD assembly to articulated robot structure; Inputs: cad-assembly; joint-set; measurement-set; Outputs: robot-assembly; Tools: FreeCAD Assembly Workbench; explicit robot-description authoring; CAD-to-URDF scripts as candidates; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md; https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md; https://github.com/boelnasr/CAD_TO_URDF; Prerequisites: Rigid link groups, parent-child relation, joint type, axis/frame/limits and fixed connections are explicit or reviewed.; Preserves: CAD part IDs, geometry, named joint frames, source measurements and assembly transforms.; Changes or infers: Groups occurrences into links; assembly constraints are mapped to robot joints; inferred joint types remain hypotheses.; Checks: Graph connectivity, tree/loop identification, frame transforms, axis signs and limit source.; Alternatives: Author URDF joint records directly; export FreeCAD Assembly4 through community script; inspect CAD_TO_URDF inferred tree.; Automation: mixed; Evidence status: documented_capability; Summary: Translate a mechanical assembly into explicit link and joint semantics; CAD hierarchy alone is insufficient.; Source ids: DSRC-12; DSRC-14; DSRC-15
3. Id: DOM-12; Name: Export mesh assets for MuJoCo; Inputs: ; Outputs: mesh; Tools: CAD mesh exporter; Blender; Open CASCADE tessellation; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst; [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); Prerequisites: Tessellation settings and mesh local frame/units chosen.; Preserves: Source CAD/B-rep and conversion parameters.; Changes or infers: Surface geometry becomes triangles; MuJoCo supports OBJ and binary STL; material assignment is separate.; Checks: Bounds, scale, normals, topology, source/mesh overlay and referenced geom role.; Alternatives: MuJoCo primitives for simple geometry; custom decoder plugin for other asset formats.; Automation: scripted; Evidence status: documented_capability; Summary: Create simulation mesh files and retain their source frame and approximation settings.; Input alternatives: cad-solid; b-rep; visual-scene; robot-assembly; Source ids: DSRC-20; DSRC-22; DSRC-13
4. Id: DOM-20; Name: Photos/video to camera solution, point cloud and mesh; Inputs: photo-set; Outputs: camera-solution; point-cloud; Tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG/OpenMVS; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); Prerequisites: Overlapping sharp views, camera metadata/calibration where available, scene motion/lighting assessed and scale controls identified.; Preserves: Original frames, camera solution, control points, reconstruction settings, sparse/dense outputs.; Changes or infers: Videos sampled into images; camera poses and dense surfaces are estimated from image correspondences.; Checks: Registered-view coverage, reprojection residuals, independent scale distances, surface holes and withheld checks.; Alternatives: RGB-D/LiDAR for metric depth; single-image learned mesh only for visual proposal.; Automation: scripted; Evidence status: documented_capability; Summary: Reconstruct visible geometry and camera poses from image sequences; monocular scale requires external controls.; Source ids: DSRC-33
5. Id: DOM-21; Name: Depth frames to registered point cloud or mesh; Inputs: depth-frames; measurement-set; Outputs: point-cloud; Tools: Open3D; CloudCompare; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); Prerequisites: Sensor model, calibration, units, extrinsics and depth validity/range known.; Preserves: Raw depth/color, frame timestamps, sensor coordinates and transforms.; Changes or infers: Registration, filtering and surface fusion combine depth samples into new geometry.; Checks: Loop closure, registration residual, independent lengths, depth noise and coverage.; Alternatives: Photogrammetry for passive optical scenes; per-frame point cloud where fusion is inappropriate.; Automation: mixed; Evidence status: documented_capability; Summary: Fuse calibrated depth observations into metric geometry while retaining the raw sensor frames.; Source ids: DSRC-33
6. Id: DOM-28; Name: Dense multi-view stereo to point cloud and mesh; Inputs: photo-set; camera-solution; Outputs: point-cloud; mesh; Tools: COLMAP dense reconstruction; AliceVision/Meshroom; OpenMVS; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); Prerequisites: Camera solution and image set correspond; scale/control transform is available for metric results.; Preserves: Sparse camera solution, source images, dense settings and intermediate depth maps where available.; Changes or infers: Estimates visible depth/surfaces and fuses points; mesh topology and texture are derived.; Checks: Coverage, holes, reprojection, independent dimensions and surface residuals.; Alternatives: Depth sensor integration via DOM-21; visual scene via DOM-22/30.; Automation: scripted; Evidence status: documented_capability; Summary: Compute dense surfaces from a previously estimated camera solution.; Source ids: DSRC-33
7. Id: DOM-29; Name: Point cloud to surface mesh; Inputs: point-cloud; Outputs: mesh; Tools: Open3D surface reconstruction; CloudCompare mesh reconstruction; Blender mesh cleanup; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); Prerequisites: Point cloud has known frame, scale, normals if required, and density/noise characteristics.; Preserves: Input cloud, processing parameters, local frame and mesh lineage.; Changes or infers: Interpolates surfaces between samples; fills and smooths gaps depending on method.; Checks: Surface deviation to source cloud, holes, components, normals and over-smoothed features.; Alternatives: Keep point cloud if no surface fill is justified; direct CAD remodeling via DOM-23.; Automation: mixed; Evidence status: documented_capability; Summary: Create a mesh surface from point samples and retain the interpolation as an inferred derivative.; Source ids: DSRC-33
8. Id: DOM-13; Name: Generate convex collision set; Inputs: mesh; Outputs: collision-set; Tools: CoACD; V-HACD; primitive fitting; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Prerequisites: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Alternatives: Primitive colliders; single convex hull for coarse bounding; use original mesh only where supported and semantics understood.; Automation: scripted; Evidence status: documented_capability; Summary: Derive a collision-specific approximation and review topology-sensitive errors.; Source ids: DSRC-23; DSRC-24; DSRC-20
9. Id: DOM-32; Name: Map CAD link geometry to MJCF body tree; Tools: documented adapter or explicit authoring step; Prerequisites: Selected MJCF model and per-asset rights record are identified; CAD part-to-body map and frame transforms are reviewed.; Preserves: MJCF joint topology, actuator/sensor declarations and model source revision.; Changes or infers: Adds/replaces geometry and may alter visual appearance or collision representation.; Checks: All mapped parts resolve; compare body transforms and bounds; compile model; inspect visual and collision roles separately.; Alternatives: Rebuild the MJCF body tree directly when the selected seed model cannot accept a geometry mapping.; Automation: assisted; Evidence status: proposed_composition; Inputs: mjcf; cad-assembly; joint-set; measurement-set; component-record; Outputs: mjcf; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Summary: Map a rights-recorded CAD component to existing MJCF bodies and replace/add geometry while preserving declared body/joint topology; require explicit part-to-body mapping.; Source ids: DSRC-19; DSRC-20
10. Id: DOM-33; Name: Add environment collision geometry to MJCF; Tools: documented adapter or explicit authoring step; Prerequisites: Source MJCF/environment frames are named; collision-set approximation and transform are recorded.; Preserves: Robot body/joint graph and source scan/mesh.; Changes or infers: Adds static environment geoms and collision pieces.; Checks: Compile model; compare environment bounds and transforms; inspect passage openings and contact fixtures.; Alternatives: Use primitives, analytic shapes or simulator-native geoms when the environment does not need mesh colliders.; Automation: assisted; Evidence status: proposed_composition; Inputs: mjcf; mesh; collision-set; Outputs: mjcf; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; Summary: Add registered environment geometry and colliders to an existing MJCF scene, preserving scene frame and explicit collision approximation.; Source ids: DSRC-20; DSRC-19

## Code and tool entry points

1. Status: existing_tool_entrypoint; Path: See the selected tool/variant contract.; Summary: Use the software/API entry points below in the recorded procedure; manual CAD, joint and semantic authoring steps use the explicit frames and source data recorded for that step.; Related entrypoints: ; Source urls: https://github.com/google-deepmind/mujoco_menagerie; https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/README.md; https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://mujoco.readthedocs.io/en/latest/XMLreference.html; Entrypoints: Pinned `franka_emika_panda/panda.xml`; README requires MuJoCo >=2.3.3; Global registration then ICP refine; inspect `RegistrationResult.transformation`; `MjSpec.from_file(...)` / XML model composition; `MjModel.from_xml_path(...)`

## Output artifacts

1. Type: mjcf; Format: MJCF XML + asset directory; Retained: Robot body tree and environment collision/visual geometry.; Loss or inference: Mesh environment loses IFC semantics and scan uncertainty unless retained in manifest.
2. Type: visual-scene; Format: MJCF viewer/render scene; Retained: Camera and rendered surfaces.; Loss or inference: Appearance does not prove collision or physical accuracy.
3. Type: collision-set; Format: OBJ/STL/primitive collision geoms; Retained: Explicit collision objects in registered frame.; Loss or inference: Simplification may remove narrow openings and surface detail.

## Checks

1. Pinned robot model and license record.
2. Frame transform composition and held-out survey residuals.
3. MJCF compiles; all mesh assets resolve.
4. Robot mount pose matches survey datums; collision geometry visually overlays source cloud.
5. Check contact geometry separately from visual geometry.

## Failure recovery

1. Model/version mismatch: pin compatible MuJoCo and Menagerie revision.
2. Registration ambiguous: add measured controls or keep cloud in separate frame.
3. Collision mesh too dense: simplify/decompose as versioned derivative and compare against source.
4. Asset terms disallow packaging: reference permitted source or replace with rights-cleared asset.

## Effort and computing classification

1. **Human:** 5
2. **Setup:** 4
3. **Compute:** 3
4. **Human reason:** Combines robotics frames, registration, collision and rights decisions.
5. **Setup reason:** Multiple data and model tools but existing robot XML reduces authoring.
6. **Compute reason:** Moderate scene clouds and collision meshes; very dense scans increase memory.

## Resources and scaling

1. **Cpu:** CPU registration and MuJoCo compile.
2. **Gpu:** No GPU required; GPU optional for scan/model route.
3. **Ram:** Cloud points, mesh triangles and robot assets.
4. **Storage:** Robot assets, scan originals, registered cloud, collisions and MJCF.
5. **Scaling drivers:** point count; mesh complexity; robot asset count
6. **Variants:** Existing registered cloud reduces setup.; Panda sample is model example only.

## Detailed branch procedures

1. [rec-r01.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r01.md)
2. [rec-r09.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r09.md)
3. [dom-r08.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r08.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. [https://github.com/google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie)
2. [https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/README.md](https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/README.md)
3. [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html)
4. [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)
5. [https://mujoco.readthedocs.io/en/latest/XMLreference.html](https://mujoco.readthedocs.io/en/latest/XMLreference.html)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
