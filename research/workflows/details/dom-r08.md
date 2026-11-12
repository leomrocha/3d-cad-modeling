# DOM-R08 — Scanned environment to collision geometry in existing MJCF

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 3/5; computing 2/5.**

Output: New collision geometry package and MJCF scene revision overlaid on the registered scan; source MJCF remains untouched.

## Comparison conditions

Existing MJCF scene and scale-registered scan in same named world frame; static environment objects, with measured transform and boundaries.

## Registered starting artifact types

1. point-cloud
2. mjcf

## Detailed source and preparation artifacts

1. Type: mjcf; Formats: MJCF XML + asset package; Minimum quality: Compiles and current asset paths resolve.; Required evidence: MuJoCo version; model hash; world frame; Handling: Preserve base XML.
2. Type: point-cloud; Formats: PLY/PCD/depth fusion; Minimum quality: Metric registered cloud; noise/outlier and sensor origin retained.; Required evidence: units; transform; scan coverage; source sensors; Handling: Keep raw and filtered clouds.
3. Type: measurement-set; Formats: survey control JSON/CSV; Minimum quality: Independent frame checks and extents.; Required evidence: control IDs; unit; uncertainty; Handling: Do not use scan alignment score alone.

## Reference points, datums and coordinate frames

1. Kind: scan transform; Fields: 4x4 registration transform; Frame: scan sensor → MJCF world; Source status: survey control/registration
2. Kind: collision proxy frame; Fields: mesh origin/scale; Frame: mesh-local → world; Source status: export manifest
3. Kind: sensor pose; Fields: camera/lidar extrinsics; Frame: sensor → scan frame; Source status: calibration record

## Software, libraries and dependencies

1. Name: Open3D; Role: registration, filtering and mesh conversion; Software license: MIT software; scan rights separate; Api or entrypoint: Global registration; ICP refinement; point cloud and TriangleMesh API; Environment dependencies: Open3D Python + NumPy; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: ICP needs initial transform; meshing infers unobserved surfaces.; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://www.open3d.org/docs/latest/python_api/open3d.geometry.TriangleMesh.html
2. Name: CoACD; Role: convex pieces for concave obstacle collision; Software license: MIT code; scan-derived geometry terms separate; Api or entrypoint: Pinned CLI per repo `--help`; record all settings; Environment dependencies: CoACD executable/library; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Approximation changes geometry; validate contact clearances.; Source urls: https://github.com/SarahWeiii/CoACD; https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE
3. Name: MuJoCo; Role: add collision-only obstacle geoms; Software license: Apache-2.0 engine; assets separate; Api or entrypoint: MJCF `<asset><mesh>` and `<worldbody><geom>`; compile model; Environment dependencies: MuJoCo Python/XML; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Visual and collision geoms should remain distinct.; Source urls: https://github.com/google-deepmind/mujoco; https://mujoco.readthedocs.io/en/latest/XMLreference.html

## Procedure

1. Action: Load existing model and scan; verify shared units/frame.; Tool: MuJoCo/Open3D; Command or api: Read MJCF via `MjModel.from_xml_path`; load cloud and manifest.; Preserves: Existing XML and raw cloud; Changes or infers: Review scene only.; Check: Check bounds and coordinate convention.; Code status: existing_tool_entrypoint
2. Action: Register or validate cloud in world frame.; Tool: Open3D + controls; Command or api: Use survey transform or global-registration initialization; refine with ICP.; Preserves: Cloud and controls; Changes or infers: Registration matrix.; Check: Held-out residuals and overlap.; Code status: existing_tool_entrypoint
3. Action: Prepare distinct visual and collision representations.; Tool: Open3D/CoACD; Command or api: Filter noise; choose primitives or convex decomposition; record settings.; Preserves: Registered cloud; Changes or infers: Collision proxy.; Check: Bounds, holes, contact envelopes and source overlay.; Code status: assisted
4. Action: Add collision asset and visual overlay in new MJCF.; Tool: MuJoCo; Command or api: Add external mesh geom with explicit world transform; keep visual scan separately.; Preserves: Base MJCF, asset package; Changes or infers: New XML and assets.; Check: Compile and inspect contact locations and frame IDs.; Code status: assisted

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-29; Name: Point cloud to surface mesh; Inputs: point-cloud; Outputs: mesh; Tools: Open3D surface reconstruction; CloudCompare mesh reconstruction; Blender mesh cleanup; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); Prerequisites: Point cloud has known frame, scale, normals if required, and density/noise characteristics.; Preserves: Input cloud, processing parameters, local frame and mesh lineage.; Changes or infers: Interpolates surfaces between samples; fills and smooths gaps depending on method.; Checks: Surface deviation to source cloud, holes, components, normals and over-smoothed features.; Alternatives: Keep point cloud if no surface fill is justified; direct CAD remodeling via DOM-23.; Automation: mixed; Evidence status: documented_capability; Summary: Create a mesh surface from point samples and retain the interpolation as an inferred derivative.; Source ids: DSRC-33
2. Id: DOM-13; Name: Generate convex collision set; Inputs: mesh; Outputs: collision-set; Tools: CoACD; V-HACD; primitive fitting; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Prerequisites: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Alternatives: Primitive colliders; single convex hull for coarse bounding; use original mesh only where supported and semantics understood.; Automation: scripted; Evidence status: documented_capability; Summary: Derive a collision-specific approximation and review topology-sensitive errors.; Source ids: DSRC-23; DSRC-24; DSRC-20
3. Id: DOM-33; Name: Add environment collision geometry to MJCF; Tools: documented adapter or explicit authoring step; Prerequisites: Source MJCF/environment frames are named; collision-set approximation and transform are recorded.; Preserves: Robot body/joint graph and source scan/mesh.; Changes or infers: Adds static environment geoms and collision pieces.; Checks: Compile model; compare environment bounds and transforms; inspect passage openings and contact fixtures.; Alternatives: Use primitives, analytic shapes or simulator-native geoms when the environment does not need mesh colliders.; Automation: assisted; Evidence status: proposed_composition; Inputs: mjcf; mesh; collision-set; Outputs: mjcf; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; Summary: Add registered environment geometry and colliders to an existing MJCF scene, preserving scene frame and explicit collision approximation.; Source ids: DSRC-20; DSRC-19

## Code and tool entry points

1. Status: existing_tool_entrypoint; Path: See the selected tool/variant contract.; Summary: Use the software/API entry points below in the recorded procedure; manual CAD, joint and semantic authoring steps use the explicit frames and source data recorded for that step.; Related entrypoints: ; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://github.com/SarahWeiii/CoACD; https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://mujoco.readthedocs.io/en/latest/XMLreference.html; Entrypoints: Global registration; ICP refinement; point cloud and TriangleMesh API; Pinned CLI per repo `--help`; record all settings; MJCF `<asset><mesh>` and `<worldbody><geom>`; compile model

## Output artifacts

1. Type: mjcf; Format: MJCF revision; Retained: Original articulated robot plus new static obstacle geometry.; Loss or inference: No scan semantics; collision simplification loses surface detail.
2. Type: collision-set; Format: OBJ/STL convex pieces or primitives; Retained: Approximation settings, local frame and source scan hash.; Loss or inference: Unobserved/occluded surfaces are inferred.
3. Type: visual-scene; Format: PLY/OBJ overlay or viewer scene; Retained: Observed scan visualization.; Loss or inference: Visual surface is not collision-authoritative.

## Checks

1. Existing MJCF compiles before change.
2. Scan and model use same unit/frame, held-out control residuals pass.
3. Collision mesh paths resolve and compilation succeeds.
4. Visual overlay and collision proxies align with scan and clearances.
5. Run authored static/dynamic contact cases as software checks only.

## Failure recovery

1. Poor alignment: add independent controls or re-register; preserve source scan.
2. Noisy cloud: filter a derivative and compare against raw before collision generation.
3. Collision penetrates robot or misses obstacle: adjust proxy from measured boundaries and rerun contact case.
4. Compile failure: revert new XML derivative, inspect asset path/mesh scale.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 3
3. **Compute:** 2
4. **Human reason:** Registered scan and existing robot reduce authoring; collision review remains needed.
5. **Setup reason:** Point cloud and simulator tools plus asset packaging.
6. **Compute reason:** Moderate geometry CPU; large scans/collision decomposition scale with triangles.

## Resources and scaling

1. **Cpu:** CPU registration and model compilation.
2. **Gpu:** No GPU necessary for registration/decomposition; optional scan acceleration.
3. **Ram:** Point count, mesh triangles and collision hull count.
4. **Storage:** Raw scan, filtered cloud, visual mesh, collision parts and MJCF assets.
5. **Scaling drivers:** scan point count; mesh triangles; decomposition hulls; model contacts
6. **Variants:** Clean scan and primitive obstacles reduce work.; Dense unstructured scan requires cleanup and decomposition.

## Detailed branch procedures

1. [rec-r04.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r04.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html)
2. [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)
3. [https://github.com/SarahWeiii/CoACD](https://github.com/SarahWeiii/CoACD)
4. [https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE)
5. [https://mujoco.readthedocs.io/en/latest/XMLreference.html](https://mujoco.readthedocs.io/en/latest/XMLreference.html)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
