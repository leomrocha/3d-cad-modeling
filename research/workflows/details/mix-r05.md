# MIX-R05 — Robot CAD + Menagerie MJCF + depth environment → combined simulation scene

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 4/5; setup 4/5; computing 3/5.**

Output: MuJoCo scene with explicit CAD-link mapping and scanned-environment collision geometry

## Comparison conditions

A selected Menagerie model and corresponding robot CAD, explicit joint mapping and a calibrated local depth environment. No robot motion is inferred from mesh appearance.

## Registered starting artifact types

1. mjcf
2. cad-assembly
3. joint-set
4. measurement-set
5. depth-frames
6. source-library

## Detailed source and preparation artifacts

1. Artifact: mjcf; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.
2. Artifact: cad-assembly; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.
3. Artifact: joint-set; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.
4. Artifact: measurement-set; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.
5. Artifact: depth-frames; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.
6. Artifact: source-library; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.

## Reference points, datums and coordinate frames

1. Menagerie body/joint frames and original asset scale
2. CAD occurrence-to-body transform mapping
3. Depth sensor calibration and environment-to-robot transform
4. Selected contact envelopes and clearance features

## Software, libraries and dependencies

1. Name: component registry/schema proposal; source license review; Role: Library asset intake and rights record; Source urls: https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://github.com/google-deepmind/mujoco_menagerie; https://polyhaven.com/license; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
2. Name: Open3D RGB-D odometry; Role: Register RGB and depth frames and estimate sequence poses; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
3. Name: sensor SDK calibration; Role: Register RGB and depth frames and estimate sequence poses; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
4. Name: Open3D camera intrinsics/trajectory; Role: Register RGB and depth frames and estimate sequence poses; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
5. Name: Open3D ScalableTSDFVolume; Role: Integrate calibrated RGB-D frames into point cloud or TSDF mesh; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
6. Name: Open3D RGBDImage; Role: Integrate calibrated RGB-D frames into point cloud or TSDF mesh; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
7. Name: Open3D marching-cubes extraction; Role: Integrate calibrated RGB-D frames into point cloud or TSDF mesh; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
8. Name: CoACD; V-HACD; primitive fitting; Role: Generate convex collision set; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
9. Name: documented adapter or explicit authoring step; Role: Map CAD link geometry to MJCF body tree; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
10. Name: Blender Python API; Blender MCP; background Blender scripts; Role: Assemble and inspect Blender scene; Source urls: https://www.blender.org/features/pipeline/; https://projects.blender.org/lab/blender_mcp/src/branch/main; https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst; https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.

## Procedure

1. Operation id: DOM-06; Action: Library asset intake and rights record; Inputs: source-library; Input alternatives: ; Input choice groups: ; Tools: component registry/schema proposal; source license review; Outputs: component-record; Human interpretation: Original source identity and item-level license/terms available or explicitly unknown.; Preserves: Original file, URL, retrieved date, hash, attribution, license text/terms and source claims.; Changes or infers: Normalize metadata; derived conversions become separate assets with lineage.; Checks: License status per file; duplicate hash; units/frame; source part number and revision when stated.; Source urls: https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://github.com/google-deepmind/mujoco_menagerie; https://polyhaven.com/license; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280
2. Operation id: REC-05; Action: Register RGB and depth frames and estimate sequence poses; Inputs: depth-frames; Input alternatives: ; Input choice groups: ; Tools: Open3D RGB-D odometry; sensor SDK calibration; Open3D camera intrinsics/trajectory; Outputs: camera-solution; point-cloud; Human interpretation: Color/depth camera intrinsics; Depth scale and units; RGB-to-depth extrinsic transform; Pose convention recorded; Preserves: Raw color/depth frames; Sensor calibration and per-frame transforms; Changes or infers: Estimates frame-to-frame motion if poses are not provided; Depth samples are projected into camera coordinates; Checks: Known-depth/range baseline residuals; Frame registration residuals and loop closure; Check synchronized frames and depth/color alignment; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html
3. Operation id: REC-06; Action: Integrate calibrated RGB-D frames into point cloud or TSDF mesh; Inputs: depth-frames; camera-solution; Input alternatives: ; Input choice groups: ; Tools: Open3D ScalableTSDFVolume; Open3D RGBDImage; Open3D marching-cubes extraction; Outputs: point-cloud; mesh; Human interpretation: REC-05 calibration and pose trajectory; Depth units/range threshold; Voxel length and truncation distance chosen in stated units; Preserves: Raw depth frames and integration trajectory; Color data and TSDF settings; Changes or infers: Fuses samples into voxel representation and interpolated surface; Occluded regions remain unobserved or become algorithmically filled; Checks: Independent dimensions and loop-closure drift; Compare two voxel lengths against the same controls; Report registration and surface residual distributions; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html
4. Operation id: DOM-13; Action: Generate convex collision set; Inputs: mesh; Input alternatives: ; Input choice groups: ; Tools: CoACD; V-HACD; primitive fitting; Outputs: collision-set; Human interpretation: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst
5. Operation id: DOM-32; Action: Map CAD link geometry to MJCF body tree; Inputs: mjcf; cad-assembly; joint-set; measurement-set; component-record; Input alternatives: ; Input choice groups: ; Tools: documented adapter or explicit authoring step; Outputs: mjcf; Human interpretation: Selected MJCF model and per-asset rights record are identified; CAD part-to-body map and frame transforms are reviewed.; Preserves: MJCF joint topology, actuator/sensor declarations and model source revision.; Changes or infers: Adds/replaces geometry and may alter visual appearance or collision representation.; Checks: All mapped parts resolve; compare body transforms and bounds; compile model; inspect visual and collision roles separately.; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst
6. Operation id: DOM-33; Action: Add environment collision geometry to MJCF; Inputs: mjcf; mesh; collision-set; Input alternatives: ; Input choice groups: ; Tools: documented adapter or explicit authoring step; Outputs: mjcf; Human interpretation: Source MJCF/environment frames are named; collision-set approximation and transform are recorded.; Preserves: Robot body/joint graph and source scan/mesh.; Changes or infers: Adds static environment geoms and collision pieces.; Checks: Compile model; compare environment bounds and transforms; inspect passage openings and contact fixtures.; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst
7. Operation id: DOM-24; Action: Assemble and inspect Blender scene; Inputs: ; Input alternatives: cad-solid; mesh; ifc; robot-assembly; camera-solution; Input choice groups: ; Tools: Blender Python API; Blender MCP; background Blender scripts; Outputs: visual-scene; Human interpretation: Input adapters resolve; transform, units, geometry role and licenses recorded.; Preserves: Source files, object/component IDs, import mapping, unit and axis transforms.; Changes or infers: Builds a render scene, materials/cameras, mesh derivatives; scene-only outputs can drop CAD/BIM/robot semantics.; Checks: Transform/numeric bounds, linked asset paths, representative camera views, exported GLB reopen and object mapping.; Source urls: https://www.blender.org/features/pipeline/; https://projects.blender.org/lab/blender_mcp/src/branch/main; https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst; https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-06; Name: Library asset intake and rights record; Inputs: source-library; Outputs: component-record; Tools: component registry/schema proposal; source license review; Source urls: https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://github.com/google-deepmind/mujoco_menagerie; https://polyhaven.com/license; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280; Prerequisites: Original source identity and item-level license/terms available or explicitly unknown.; Preserves: Original file, URL, retrieved date, hash, attribution, license text/terms and source claims.; Changes or infers: Normalize metadata; derived conversions become separate assets with lineage.; Checks: License status per file; duplicate hash; units/frame; source part number and revision when stated.; Alternatives: Keep external link only where local caching/redistribution terms are unclear.; Automation: mixed; Evidence status: proposed_composition; Summary: Create immutable, rights-aware component records instead of treating catalogs as a common license.; Source ids: DSRC-07; DSRC-08; DSRC-09; DSRC-10; DSRC-11
2. Id: REC-05; Name: Register RGB and depth frames and estimate sequence poses; Inputs: depth-frames; Outputs: camera-solution; point-cloud; Tools: Open3D RGB-D odometry; sensor SDK calibration; Open3D camera intrinsics/trajectory; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Prerequisites: Color/depth camera intrinsics; Depth scale and units; RGB-to-depth extrinsic transform; Pose convention recorded; Preserves: Raw color/depth frames; Sensor calibration and per-frame transforms; Changes or infers: Estimates frame-to-frame motion if poses are not provided; Depth samples are projected into camera coordinates; Checks: Known-depth/range baseline residuals; Frame registration residuals and loop closure; Check synchronized frames and depth/color alignment; Alternatives: Hardware SLAM trajectory; Surveyed poses; LiDAR/target registration; Automation: scripted; Evidence status: existing_report_registered; Summary: Associate color and depth in a shared camera model, then estimate or import frame poses for fusion. Sensor metric units do not remove calibration bias or trajectory drift.
3. Id: REC-06; Name: Integrate calibrated RGB-D frames into point cloud or TSDF mesh; Inputs: depth-frames; camera-solution; Outputs: point-cloud; mesh; Tools: Open3D ScalableTSDFVolume; Open3D RGBDImage; Open3D marching-cubes extraction; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Prerequisites: REC-05 calibration and pose trajectory; Depth units/range threshold; Voxel length and truncation distance chosen in stated units; Preserves: Raw depth frames and integration trajectory; Color data and TSDF settings; Changes or infers: Fuses samples into voxel representation and interpolated surface; Occluded regions remain unobserved or become algorithmically filled; Checks: Independent dimensions and loop-closure drift; Compare two voxel lengths against the same controls; Report registration and surface residual distributions; Alternatives: Point-cloud accumulation without TSDF; Sensor-native mesh; COLMAP/MVS surface from RGB; Automation: scripted; Evidence status: documented_capability; Summary: Fuse RGB-D into a scalable TSDF and extract a triangle mesh; voxel length controls discretization and noise response, not measured accuracy.
4. Id: DOM-13; Name: Generate convex collision set; Inputs: mesh; Outputs: collision-set; Tools: CoACD; V-HACD; primitive fitting; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Prerequisites: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Alternatives: Primitive colliders; single convex hull for coarse bounding; use original mesh only where supported and semantics understood.; Automation: scripted; Evidence status: documented_capability; Summary: Derive a collision-specific approximation and review topology-sensitive errors.; Source ids: DSRC-23; DSRC-24; DSRC-20
5. Id: DOM-32; Name: Map CAD link geometry to MJCF body tree; Tools: documented adapter or explicit authoring step; Prerequisites: Selected MJCF model and per-asset rights record are identified; CAD part-to-body map and frame transforms are reviewed.; Preserves: MJCF joint topology, actuator/sensor declarations and model source revision.; Changes or infers: Adds/replaces geometry and may alter visual appearance or collision representation.; Checks: All mapped parts resolve; compare body transforms and bounds; compile model; inspect visual and collision roles separately.; Alternatives: Rebuild the MJCF body tree directly when the selected seed model cannot accept a geometry mapping.; Automation: assisted; Evidence status: proposed_composition; Inputs: mjcf; cad-assembly; joint-set; measurement-set; component-record; Outputs: mjcf; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Summary: Map a rights-recorded CAD component to existing MJCF bodies and replace/add geometry while preserving declared body/joint topology; require explicit part-to-body mapping.; Source ids: DSRC-19; DSRC-20
6. Id: DOM-33; Name: Add environment collision geometry to MJCF; Tools: documented adapter or explicit authoring step; Prerequisites: Source MJCF/environment frames are named; collision-set approximation and transform are recorded.; Preserves: Robot body/joint graph and source scan/mesh.; Changes or infers: Adds static environment geoms and collision pieces.; Checks: Compile model; compare environment bounds and transforms; inspect passage openings and contact fixtures.; Alternatives: Use primitives, analytic shapes or simulator-native geoms when the environment does not need mesh colliders.; Automation: assisted; Evidence status: proposed_composition; Inputs: mjcf; mesh; collision-set; Outputs: mjcf; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; Summary: Add registered environment geometry and colliders to an existing MJCF scene, preserving scene frame and explicit collision approximation.; Source ids: DSRC-20; DSRC-19
7. Id: DOM-24; Name: Assemble and inspect Blender scene; Inputs: ; Outputs: visual-scene; Tools: Blender Python API; Blender MCP; background Blender scripts; Source urls: https://www.blender.org/features/pipeline/; https://projects.blender.org/lab/blender_mcp/src/branch/main; https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst; https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0; Prerequisites: Input adapters resolve; transform, units, geometry role and licenses recorded.; Preserves: Source files, object/component IDs, import mapping, unit and axis transforms.; Changes or infers: Builds a render scene, materials/cameras, mesh derivatives; scene-only outputs can drop CAD/BIM/robot semantics.; Checks: Transform/numeric bounds, linked asset paths, representative camera views, exported GLB reopen and object mapping.; Alternatives: Direct scripted background processing for repeatability; MCP for iterative live inspection; OCS remains engineering baseline.; Automation: mixed; Evidence status: documented_capability; Summary: Use Blender for visual composition, mesh work and inspection while retaining native domain models; a camera-solution input alone can produce a camera-only scene.; Source ids: DSRC-31; DSRC-34; DSRC-35; DSRC-39; Input alternatives: cad-solid; mesh; ifc; robot-assembly; camera-solution

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Entrypoint: `Open3D registration_icp(source, target, max_correspondence_distance, init, estimation_method): provide source/target clouds in compatible units and a source-to-target initialization; inspect transformation, fitness and inlier_rmse.`; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html
2. Status: existing_tool_entrypoint; Entrypoint: `MuJoCo MJCF body, joint, inertial, mesh and geom elements describe explicitly supplied frames, geometry and physical properties. MuJoCo MjModel.from_xml_path is the documented model compilation entry point.`; Source urls: https://mujoco.readthedocs.io/en/latest/XMLreference.html; https://github.com/google-deepmind/mujoco
3. Entrypoint: `Native application/API operations in the recorded recipe`; Status: existing_tool_entrypoint; Role: Complete the remaining source-backed CAD, reconstruction, IFC or robot steps with their explicit human interpretation points.; Source urls: https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco_menagerie; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://polyhaven.com/license; https://projects.blender.org/lab/blender_mcp/src/branch/main; https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0; https://www.blender.org/features/pipeline/; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280; https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html

## Output artifacts

1. MuJoCo scene with explicit CAD-link mapping and scanned-environment collision geometry
2. Native/source artifacts and role-specific derivatives linked by source revision and hash.

## Checks

1. The supplied MJCF is a named model revision with its own licence record.
2. CAD-to-body mapping checks transforms and joints before modifying a derivative.
3. Environment mesh and colliders have separate assets and aligned frames.
4. Source robot dynamics retain their recorded source/model-fidelity status.
5. Compare reference lengths with model coordinates in declared units; record residuals in mm separately for fit and check controls.
6. Inspect actual saved/imported geometry, component identities and source-to-output mapping.

## Failure recovery

1. Return to the operation whose calibration, identity, geometry or interpretation check failed; preserve its inputs and previous outputs.
2. Resolve the affected source correspondence or feature meaning explicitly before regenerating downstream derivatives.

## Effort and computing classification

1. **Human:** 4
2. **Setup:** 4
3. **Compute:** 3
4. **Human reason:** Match CAD parts to supplied robot bodies and reconcile environment and robot coordinate frames.
5. **Setup reason:** Combine a simulation asset package, CAD geometry mapping, sensor capture and collider generation.
6. **Compute reason:** Depth meshes and convex decomposition drive CPU/RAM use; a small supplied MJCF is a separate simulation asset.

## Resources and scaling

1. **Cpu:** CAD construction, parsing, transforms, semantic authoring and validation run in their selected application/library processes.
2. **Gpu:** Required by the selected dense-stereo/Gaussian/learned backend when included; otherwise optional for display.
3. **Ram:** Scales with images, points, triangles, CAD topology and retained representations. Record actual peak use during execution.
4. **Storage:** Preserve originals, native models, cameras/transforms, intermediate clouds/meshes and final derivatives separately.
5. **Scaling drivers:** Source artifact count and resolution; CAD feature/body count; Point/triangle count and collider count; Number of tool boundaries and evidence reconciliation steps
6. **Variants:** Already calibrated/registered inputs reduce preparation work.; Pre-existing components with explicit interfaces reduce geometry authoring.; Large scenes or high-resolution images increase computing demand independently of manual effort.

## Detailed branch procedures

1. [dom-r04.md](dom-r04.md)
2. [dom-r08.md](dom-r08.md)
3. [rec-r09.md](rec-r09.md)

The software lists include alternatives per operation. Select one compatible backend for each branch; follow the linked branch dossier for library/API dependencies and preserve the explicit operation handoff checks.

## Original sources

1. [https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst](https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst)
2. [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst)
3. [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst)
4. [https://github.com/google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie)
5. [https://github.com/kmammou/v-hacd/blob/master/LICENSE](https://github.com/kmammou/v-hacd/blob/master/LICENSE)
6. [https://polyhaven.com/license](https://polyhaven.com/license)
7. [https://projects.blender.org/lab/blender_mcp/src/branch/main](https://projects.blender.org/lab/blender_mcp/src/branch/main)
8. [https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE)
9. [https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0](https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0)
10. [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/)
11. [https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280)
12. [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN)
13. [https://www.kicad.org/libraries/license/](https://www.kicad.org/libraries/license/)
14. [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html)
15. [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html)

Full source summaries: [source register](../../sources/source-register.md).
