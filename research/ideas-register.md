# Ideas and research questions

Registered: 2026-11-12.

The records retain project proposals, experiment questions and the earlier implementation-plan ideas. Each record identifies its origin and supporting sources. Detailed records: [ideas-register.json](/home/leo/projects/3dmodeling/research/ideas-register.json).

## CAD-I01 — Feature-level evidence ledger

Status: proposal.

Link every model parameter and geometric feature to a source document, coordinate range, evidence status, units, transformation and uncertainty; keep solver constraints separate from measured inputs.

Original source: [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md)

Next check: Prototype a JSON schema that points from model parameter IDs to image/DXF entities and measured-value status.

## CAD-I02 — Two-channel raster interpretation

Status: proposal.

Keep OCR outputs and line/contour outputs in separate layers so OCR cleanup cannot erase geometric evidence and line extraction cannot silently reinterpret dimension text.

Original source: [https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html)

Original source: [https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html)

Next check: Compare extracted OCR boxes and line candidates against a raster-sketch fixture with known scale and dimensions.

## CAD-I03 — Orthographic reconstruction comparison fixture

Status: proposal.

Build a benchmark of simple prismatic, revolved and assembled parts with front/top/side views, dimensions, raster degradation and known CAD sources; compare rule-based, learned and human-assisted routes.

Original source: [https://www.sciencedirect.com/science/article/pii/S0097849323000766](https://www.sciencedirect.com/science/article/pii/S0097849323000766)

Original source: [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html)

Next check: Check research repositories and dataset licences for redistributable fixtures and whether output preserves editable CAD feature history.

## CAD-I04 — Representation-aware backend selection

Status: proposal.

Route each job using required outputs: OCS for the established session workflow, FreeCAD for constrained feature history, code-CAD for reproducible exact B-rep source, and Blender/OpenSCAD for mesh or scene routes; record when a format conversion changes representation.

Original source: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md)

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs)

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md)

Original source: [https://build123d.readthedocs.io/en/latest/operations.html](https://build123d.readthedocs.io/en/latest/operations.html)

Next check: Run a controlled exact solid and mesh fixture through each installed backend and record representation and history outcomes.

## CAD-I05 — Dimension and hidden-surface ambiguity queue

Status: proposal.

Keep inferred values, obscured surfaces, uncertain symbols and competing projection correspondences in a small question queue; proceed only on independent geometry that does not depend on those items.

Original source: [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html)

Original source: [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html)

Next check: Design test cases where two distinct solids satisfy the same incomplete views and verify that the workflow reports both candidates.

## REC-I01 — Pose and unit adapter fixture across tool frames

Status: proposal.

Create a small surveyed fixture with known 3D targets and images; round-trip pose matrices through OpenCV, COLMAP, Open3D, Blender and OCS, checking direction, handedness, units and projection error.

Original source: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html)

Original source: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html)

Next check: Confirm exact conventions and transform serialization supported by the installed versions.

## REC-I02 — Multi-sensor RGB-depth-LiDAR frame graph

Status: proposal.

Represent camera intrinsics, RGB-depth extrinsics, LiDAR-to-camera transform, world controls and frame timestamps as one provenance-linked transform graph before fusion.

Original source: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html)

Original source: [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html)

Next check: Define schema for transform direction, units, covariance/residual and calibration revision.

## REC-I03 — DA3 metric and COLMAP/MVS comparison on control object

Status: proposal.

Capture an object with distributed measured controls and compare DA3 estimated depth/pose/cloud against COLMAP/MVS and independent lengths, reporting regional residuals.

Original source: [https://github.com/ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3)

Original source: [https://github.com/colmap/colmap](https://github.com/colmap/colmap)

Next check: Select nonreflective textured object and set held-out control distances before capture.

## REC-I04 — Camera-anchored stroke primitive semantics

Status: proposal.

Use ray hits to anchor strokes and offer separate interpretations: surface trace, projected curve, selected planar sketch, or dimensioned datum annotation; store source component/face and camera state.

Original source: [https://docs.blender.org/api/current/bpy.types.Scene.html](https://docs.blender.org/api/current/bpy.types.Scene.html)

Original source: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html)

Next check: Specify user interaction for ambiguous occlusion and backface hits, then verify reprojected anchors.

## REC-I05 — Nerfstudio Splatfacto geometry export version test

Status: research_question.

Resolve generic `ns-export tsdf` documentation (states all models) against Splatfacto FAQ (states mesh/pointcloud unsupported) for selected release and checkpoint.

Original source: [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md)

Original source: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html)

Next check: At authorized implementation stage, identify version and test `ns-export tsdf` output existence, coverage, units and withheld control residuals.

## REC-I06 — Primitive-fitting method selection

Status: research_question.

Compare plane, circle/cylinder/axis candidate fitters on known reference geometry, retain inlier point IDs and residual distribution, and compare fit stability under threshold changes.

Original source: [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html)

Original source: [https://github.com/CloudCompare/CloudCompare](https://github.com/CloudCompare/CloudCompare)

Next check: Choose feature classes needed by actual scan-to-CAD fixture and document each fitter's objective and units.

## REC-I07 — CAD-to-cloud correspondence strategy

Status: proposal.

Compare CAD semantic landmarks/PnP against FPFH/RANSAC+ICP for aligning scan to an existing CAD revision, especially partial and symmetric shapes.

Original source: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html)

Original source: [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html)

Original source: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)

Next check: Use withheld datum targets and report alternate pose failure cases.

## REC-I08 — Splat plus independently checked mesh layered scene

Status: proposal.

Keep Gaussian splat for appearance, point cloud for sampled evidence, mesh for surface comparison and CAD solids for interpreted design as named layers carrying linked transforms and confidence/evidence labels.

Original source: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html)

Original source: [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md)

Next check: Define a scene manifest with representation role, transform, unit, source and checks for each layer.

## DOM-I01 — One canonical component schema with domain adapters

Status: proposal.

Store identity, source/license, geometry representations, units/frames and physical values once; generate IFC, URDF, MJCF and visual exports through explicit adapters.

Original source: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md)

Original source: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md)

Next check: Prototype one mechanical component and one IFC product; document representation loss in each export.

## DOM-I02 — Assembly to URDF workflow

Status: proposal.

Use explicit joints and interface frames from CAD assembly as robot-description inputs; keep automated joint inference as a reviewable suggestion.

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md)

Original source: [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial)

Original source: [https://github.com/boelnasr/CAD_TO_URDF](https://github.com/boelnasr/CAD_TO_URDF)

Next check: Compare FreeCAD assembly joint records to a URDF fixture and inspect one STEP-inference converter without treating its output as verified.

## DOM-I03 — Open-chain and closed-chain robot models

Status: research_question.

Use URDF for link/joint tree consumers; investigate MJCF native constraints or a multibody formulation for closed loops and parallel mechanisms.

Original source: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst)

Original source: [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial)

Next check: Find current primary documentation for closed-chain mechanisms in the chosen robot simulator and define a loop-conversion fixture.

## DOM-I04 — CAD solid to visual/collision/inertial triple

Status: proposal.

Every robot link has separately authored high-detail visual geometry, simplified collision pieces and sourced mass/inertia attached to explicit frames.

Original source: [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial)

Original source: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst)

Next check: Build a link with a non-convex opening and compare mesh collision, convex decomposition and primitive fit.

## DOM-I05 — Plan plus scan to IFC as-built model

Status: proposal.

Use measured scan alignment as surface evidence, plan interpretation for semantic element boundaries and IFC relationships for the building model.

Original source: [/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json](/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json)

Original source: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html)

Next check: Define registration-control/held-out-control split and document how uncertain wall/opening boundaries enter IFC.

## DOM-I06 — CAD/STEP/B-rep fidelity gates

Status: proposal.

Use STEP for geometry exchange while comparing the actual exporter/importer pair; source formats differ in whether they preserve analytic faces, assemblies and parametric history.

Original source: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md)

Original source: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html)

Next check: Use a cylinder, hole and two-part assembly fixture; report face types, names, bounds, volume and lost feature history.

## DOM-I07 — IFC parametric element versus mesh representation

Status: proposal.

Use parametric profiles/sweeps for elements where editability and quantities matter; use IFC mesh representations for complex as-built/furniture shapes and keep classification/property mapping explicit.

Original source: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html)

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html)

Next check: Export profile-extrusion and mesh forms of one element and compare import fidelity and IDS/property retention.

## DOM-I08 — Scan to CAD with evidence labels

Status: proposal.

Maintain scan, controls, fitted primitive/features, independent residuals and CAD source as separate linked representations.

Original source: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md)

Original source: [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

Next check: Test one manufactured mechanical component with held-out interface dimensions.

## DOM-I09 — Menagerie robot model reuse

Status: proposal.

Reuse licensed MJCF structures and collision/visual examples as simulator fixtures or references, while checking each model's license and model-specific fidelity statement.

Original source: [https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md)

Next check: Select a model whose license permits the intended use and inspect its README, assets and revision before intake.

## DOM-I10 — Rights-aware reusable asset catalog

Status: proposal.

Store vendor CAD and community models with item-level rights and immutable source hashes; separate asset licenses from tool licenses and project license.

Original source: [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN)

Original source: [https://www.kicad.org/libraries/license/](https://www.kicad.org/libraries/license/)

Original source: [https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280)

Next check: Create an intake record for one CC-BY component and one restricted manufacturer STEP download.

## DOM-I11 — Poly Haven visual environment library

Status: proposal.

Use CC0 assets and HDRIs to construct architectural and product rendering contexts; do not use asset dimensions as component specifications.

Original source: [https://polyhaven.com/license](https://polyhaven.com/license)

Next check: Assess asset metadata, scale indicators and dependency size for a visual scene fixture.

## DOM-I12 — Blender scripting and MCP orchestration

Status: proposal.

Keep OCS as engineering baseline; use deterministic Blender background scripts for repeatable conversion and checks, with MCP live inspection as a later interactive layer.

Original source: [https://projects.blender.org/lab/blender_mcp/src/branch/main](https://projects.blender.org/lab/blender_mcp/src/branch/main)

Original source: [https://github.com/ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)

Original source: [https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst](https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst)

Original source: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md)

Next check: Compare scripted and MCP scene edits once the local Blender 5.0.1 compatibility constraint is resolved or a compatible integration chosen.

## DOM-I13 — Menagerie robot plus scan environment simulation

Status: proposal.

Combine an articulated robot description with a registered room or terrain mesh, then derive a simplified collision scene while keeping source coordinates and body frames linked.

Original source: [https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md)

Original source: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md)

Next check: Create a miniature scene with one articulated robot and one scanned obstacle; verify frame transforms and collision envelope.

## DOM-I14 — Sketch-over-model revision workflow

Status: proposal.

Align new sketch/image dimensions to an existing model datum, revise its native source, and regenerate geometry and visual exports without losing unrelated component identity.

Original source: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md)

Original source: [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

Next check: Exercise a changed hole position against a pinned source model and compare a before/after measurement manifest.

## DOM-I15 — Engineering asset quality classes

Status: proposal.

Distinguish visual-only assets, approximate component geometry, dimensioned supplier CAD, measured parts and verified simulation models with explicit source evidence.

Original source: [https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md)

Original source: [https://polyhaven.com/license](https://polyhaven.com/license)

Original source: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md)

Next check: Define permitted downstream operations for each asset evidence class without presenting a license or visual source as engineering validation.

## MIX-I01 — Shared frame and anchor record

Status: research_question.

Use one versioned record to relate pixels, camera rays, scan coordinates, CAD datums and component IDs.

Original source: [/home/leo/projects/3dmodeling/research/workflows/composition-rules.md](/home/leo/projects/3dmodeling/research/workflows/composition-rules.md)

Next check: Compare transform direction, units and anchor round trips in the selected tools.

## MIX-I02 — Source-to-feature association

Status: research_question.

Retain each fitted or interpreted surface region and the exact CAD feature it supports.

Original source: [/home/leo/projects/3dmodeling/research/workflows/composition-rules.md](/home/leo/projects/3dmodeling/research/workflows/composition-rules.md)

Next check: Compare fitted-plane/cylinder evidence with saved feature and dimension readback.

## MIX-I03 — Importer/exporter field mapping

Status: research_question.

Maintain actual preserved/transformed/discarded field mappings per tool/version.

Original source: [/home/leo/projects/3dmodeling/research/workflows/composition-rules.md](/home/leo/projects/3dmodeling/research/workflows/composition-rules.md)

Next check: Run the same component and assembly fixtures through the intended consumers.

## MIX-I04 — Ambiguous-view comparison

Status: research_question.

Retain several geometrically consistent interpretations until source evidence distinguishes them.

Original source: [/home/leo/projects/3dmodeling/research/workflows/composition-rules.md](/home/leo/projects/3dmodeling/research/workflows/composition-rules.md)

Next check: Compare projected views and independent dimensions, with inference labels by feature.

## MIX-I05 — Dependency-driven revision updates

Status: research_question.

Record which branch depends on each measurement, component revision and interpretation.

Original source: [/home/leo/projects/3dmodeling/research/workflows/composition-rules.md](/home/leo/projects/3dmodeling/research/workflows/composition-rules.md)

Next check: Trace a single input change through affected recipes and derivative revisions.

## MIX-I06 — Text-to-concept-image-to-mesh route

Status: research_question.

Register a possible branch from text or sketch through a concept image to an image-conditioned mesh, then measured CAD remodeling.

Original source: [/home/leo/projects/3dmodeling/research/workflows/combined-paths.json](/home/leo/projects/3dmodeling/research/workflows/combined-paths.json)

Next check: Research an open image-generation backend and its exact weight/output terms before defining the first transition.

## MIX-I07 — Procedural field geometry supplement

Status: proposal.

Evaluate PicoGK/ShapeKernel as a separate source-driven geometry branch with explicit field/mesh resolution and OCS interchange checks.

Original source: [/home/leo/projects/3dmodeling/research/workflows/combined-paths.json](/home/leo/projects/3dmodeling/research/workflows/combined-paths.json)

Original source: [https://github.com/leap71/PicoGK](https://github.com/leap71/PicoGK)

Original source: [https://github.com/leap71/LEAP71_ShapeKernel](https://github.com/leap71/LEAP71_ShapeKernel)

Original source: [https://picogk.org/doc/](https://picogk.org/doc/)

Next check: Use the existing archived sources to define runtime/platform, output representation and comparison experiments.

## NEXT-I01 — Targeted first-pilot handoff review

Status: proposal.

Resolve exact tools, representations, editable sources, unit/frame mappings and prerequisites for four route cards before the pilot experiments.

Original source: [/home/leo/projects/3dmodeling/research/next-step-proposal.md](/home/leo/projects/3dmodeling/research/next-step-proposal.md)

Next check: Produce four route cards and a bounded source-linked experiment list.

## NEXT-I02 — Shared records and fixture briefs

Status: proposal.

Define model/evidence/artifact/component/check records and three dimensioned fixture briefs.

Original source: [/home/leo/projects/3dmodeling/research/next-step-proposal.md](/home/leo/projects/3dmodeling/research/next-step-proposal.md)

Next check: Check representation, identity and evidence fields against the selected routes.

## NEXT-I03 — OCS baseline pilot

Status: proposal.

Exercise the existing OCS skill on a bracket and mating plate, including a revision, native save/reopen and measured derivative checks.

Original source: [/home/leo/projects/3dmodeling/research/next-step-proposal.md](/home/leo/projects/3dmodeling/research/next-step-proposal.md)

Next check: Record the actual installed capabilities and saved geometry for that fixture.

## NEXT-I04 — Text and drawing CAD pilot

Status: proposal.

Compare text, raster sketch and DXF/SVG routes using the same dimensioned fixture and a complementary procedural-solid backend.

Original source: [/home/leo/projects/3dmodeling/research/next-step-proposal.md](/home/leo/projects/3dmodeling/research/next-step-proposal.md)

Next check: Compare dimensions, topology, editable source and importer readback.

## NEXT-I05 — Reconstruction and mixed-input pilot

Status: proposal.

Combine photographs, controls, drawings or identified components into registered references and source-linked CAD remodeling, including anchored annotations.

Original source: [/home/leo/projects/3dmodeling/research/next-step-proposal.md](/home/leo/projects/3dmodeling/research/next-step-proposal.md)

Next check: Compare held-out measurements and regional scan-to-CAD deviations.

## NEXT-I06 — Architecture robotics and component pilot

Status: proposal.

Exercise IFC building semantics, robot joint/physical-property handoffs and a pilot reusable component library.

Original source: [/home/leo/projects/3dmodeling/research/next-step-proposal.md](/home/leo/projects/3dmodeling/research/next-step-proposal.md)

Next check: Check loaded domain models, frames, geometry roles and source identities.

## NEXT-I07 — Package exercised skills and helpers

Status: proposal.

Package exercised workflows with skills, scripts, examples, dependency records and shared CLI operations.

Original source: [/home/leo/projects/3dmodeling/research/next-step-proposal.md](/home/leo/projects/3dmodeling/research/next-step-proposal.md)

Next check: Run the relevant fixture and preserve actual execution evidence for each supported route.

## AUDIT-I01 — Per-action software and AI options

Status: proposal.

Define agent-led, hybrid, software-first exception and deterministic alternatives per action and supported input class.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md)

Original proposal: [research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md), line 5.

Next check: Review the point-01 assignment of software, model and user responsibilities.

## AUDIT-I02 — Evidence-based candidate comparison and merge

Status: proposal.

Run alternative interpretations or software routes where useful; align their records, compare evidence and preserve per-feature provenance when a reasoning VLM proposes selection or combination.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md)

Original proposal: [research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md), line 40.

Next check: Review conflict, source-precedence and post-merge validation cases.

## AUDIT-I03 — Per-feature tolerance and intended-use requirements

Status: proposal.

Separate dimensional accuracy, geometry detail, appearance, function, simulation and manufacturing requirements; attach tolerances to individual features and relationships.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md)

Original proposal: [research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md), line 50.

Next check: Review the first-point requirement and tolerance record without introducing a sample design.

## AUDIT-I04 — Tested replacement of specific agent actions

Status: proposal.

Specify and test repeatable software functions for particular input classes while preserving agent-assisted exception routes.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md)

Original proposal: [research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md), line 58.

Next check: Review proposed representative and failure cases before any implementation.

## AUDIT-I05 — Local-compute-first point order

Status: proposal.

Define source briefs and existing geometry before processing-heavy reconstruction; record local and remote resources separately.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md)

Original proposal: [research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md), line 83.

Next check: Review each point in the plan order with its stated data size and output purpose.

## AUDIT-I06 — Procedure design and independent review roles

Status: proposal.

Use the requested Astra, Sol, Terra and Luna assignments for design, visual reasoning, independent review, software assessment and primary-source lookup.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md)

Original proposal: [research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md), line 68.

Next check: Record actual task execution, source findings and reviewer dispositions separately from dispatch settings.

## AUDIT-CAD-12 — Assemble existing CAD or source-library components — detailed execution options

Status: proposal.

Point 02 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Assemble existing CAD or source-library components. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json)

Original proposal: [research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-06 — Library asset intake and rights record — detailed execution options

Status: proposal.

Point 02 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Library asset intake and rights record. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json)

Original proposal: [research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-07 — Place reusable component in assembly — detailed execution options

Status: proposal.

Point 02 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Place reusable component in assembly. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json)

Original proposal: [research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-26 — Version and reuse component revision — detailed execution options

Status: proposal.

Point 02 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Version and reuse component revision. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json)

Original proposal: [research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-38 — Import STEP solid into CAD representation — detailed execution options

Status: proposal.

Point 02 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Import STEP solid into CAD representation. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json)

Original proposal: [research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-39 — Export STEP assembly — detailed execution options

Status: proposal.

Point 02 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Export STEP assembly. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json)

Original proposal: [research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-08 — Read and clean vector drawing geometry — detailed execution options

Status: proposal.

Point 03 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Read and clean vector drawing geometry. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-09 — Build and constrain an editable planar sketch — detailed execution options

Status: proposal.

Point 03 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Build and constrain an editable planar sketch. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-10 — Create a kernel solid and native model document from confirmed parameters — detailed execution options

Status: proposal.

Point 03 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Create a kernel solid and native model document from confirmed parameters. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-13 — Verify model geometry and saved output — detailed execution options

Status: proposal.

Point 03 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Verify model geometry and saved output. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-14 — Recover from failed interpretation or geometry construction — detailed execution options

Status: proposal.

Point 03 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Recover from failed interpretation or geometry construction. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-15 — Render source-defined CSG as a mesh — detailed execution options

Status: proposal.

Point 03 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Render source-defined CSG as a mesh. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-03 — DXF/SVG drawing to constrained profile — detailed execution options

Status: proposal.

Point 03 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for DXF/SVG drawing to constrained profile. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-04 — Brief/profile to native CAD solid — detailed execution options

Status: proposal.

Point 03 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Brief/profile to native CAD solid. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-05 — Export STEP solid — detailed execution options

Status: proposal.

Point 03 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Export STEP solid. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-40 — Script-parametric CAD authoring — detailed execution options

Status: proposal.

Point 03 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Script-parametric CAD authoring. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Original proposal: [research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-02 — Rectify a raster drawing plane from known dimensions — detailed execution options

Status: proposal.

Point 04 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Rectify a raster drawing plane from known dimensions. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Original proposal: [research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-03 — Recognize dimension text with OCR — detailed execution options

Status: proposal.

Point 04 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Recognize dimension text with OCR. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Original proposal: [research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-04 — Extract raster edges, lines and contours — detailed execution options

Status: proposal.

Point 04 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Extract raster edges, lines and contours. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Original proposal: [research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-05 — Convert raster floor-plan candidates into a wall and opening graph — detailed execution options

Status: proposal.

Point 04 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Convert raster floor-plan candidates into a wall and opening graph. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Original proposal: [research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-06 — Register orthographic drawing views in a shared coordinate frame — detailed execution options

Status: proposal.

Point 04 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Register orthographic drawing views in a shared coordinate frame. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Original proposal: [research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-07 — Reconstruct a candidate 3D wireframe and surface from orthographic views — detailed execution options

Status: proposal.

Point 04 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Reconstruct a candidate 3D wireframe and surface from orthographic views. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Original proposal: [research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-17 — Build wall and opening solids from a confirmed floor-plan graph — detailed execution options

Status: proposal.

Point 04 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Build wall and opening solids from a confirmed floor-plan graph. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Original proposal: [research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-02 — Raster sketch to constrained sketch — detailed execution options

Status: proposal.

Point 04 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Raster sketch to constrained sketch. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Original proposal: [research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-18 — Raster floor plan to IFC building — detailed execution options

Status: proposal.

Point 04 defines 4 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Raster floor plan to IFC building. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Original proposal: [research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-02B — Calibrate camera poses from photographs and known controls — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Calibrate camera poses from photographs and known controls. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-01 — Calibrate camera intrinsics and distortion — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Calibrate camera intrinsics and distortion. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-02 — Solve camera pose from known 3D-to-2D correspondences — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Solve camera pose from known 3D-to-2D correspondences. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-07 — Estimate coarse transform between point clouds — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Estimate coarse transform between point clouds. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-08 — Refine registration and compare point-cloud surfaces — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Refine registration and compare point-cloud surfaces. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-09 — Segment point clouds and fit candidate primitive evidence — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Segment point clouds and fit candidate primitive evidence. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-11 — Fit analytic features to scans or image-derived point clouds — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Fit analytic features to scans or image-derived point clouds. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-12 — Register existing CAD to calibrated photographs or scan points — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Register existing CAD to calibrated photographs or scan points. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-13 — Anchor a screen sketch to a 3D surface — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Anchor a screen sketch to a 3D surface. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-14 — Remodel segmented scan evidence as parametric CAD — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Remodel segmented scan evidence as parametric CAD. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-15 — Reconcile scan surfaces with dimensioned drawings — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Reconcile scan surfaces with dimensioned drawings. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-16 — Iterate CAD edits against registered evidence — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Iterate CAD edits against registered evidence. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-19 — Register scan to building frame — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Register scan to building frame. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-23 — Scan or mesh to parametric CAD remodeling — detailed execution options

Status: proposal.

Point 05 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Scan or mesh to parametric CAD remodeling. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Original proposal: [research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-31 — Author assembly graph and joint set — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Author assembly graph and joint set. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-37 — Author robot assembly from CAD component — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Author robot assembly from CAD component. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-08 — CAD assembly to articulated robot structure — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for CAD assembly to articulated robot structure. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-14 — Calculate or import physical mass properties — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Calculate or import physical mass properties. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-12 — Export mesh assets for MuJoCo — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Export mesh assets for MuJoCo. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-13 — Generate convex collision set — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Generate convex collision set. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-09 — Robot assembly to URDF package — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Robot assembly to URDF package. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-10 — URDF import and MJCF conversion — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for URDF import and MJCF conversion. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-11 — Author native MJCF simulation model — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Author native MJCF simulation model. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-15 — Author semantic IFC building — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Author semantic IFC building. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-16 — Extract IFC geometry as triangles — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Extract IFC geometry as triangles. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-27 — Extract IFC geometry as OpenCASCADE B-rep — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Extract IFC geometry as OpenCASCADE B-rep. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-17 — IFC to GLB display scene — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for IFC to GLB display scene. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-32 — Map CAD link geometry to MJCF body tree — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Map CAD link geometry to MJCF body tree. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-33 — Add environment collision geometry to MJCF — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Add environment collision geometry to MJCF. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-34 — Author static MuJoCo environment from BIM mesh — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Author static MuJoCo environment from BIM mesh. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-24 — Assemble and inspect Blender scene — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Assemble and inspect Blender scene. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-35 — Place library component in semantic IFC — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Place library component in semantic IFC. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-25 — Create fabrication package — detailed execution options

Status: proposal.

Point 06 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Create fabrication package. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

Original proposal: [research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-I07 — Reuse reviewed action contracts across the fifteen workflow skills

Status: proposal.

Group existing operation/action/helper specifications under the fifteen catalogue skill names; preserve one operation definition where several skills reuse it. Include Gaussian and related NeRF view-synthesis branches with distinct payloads and backend conditions.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/skill-to-actions.md](/home/leo/projects/3dmodeling/research/action-audit/skill-to-actions.md)

Original source: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md)

Original proposal: [research/action-audit/skill-to-actions.md](/home/leo/projects/3dmodeling/research/action-audit/skill-to-actions.md), line 1.

Next check: Use the linked supported-input, backend and future-case contracts when implementing or composing that workflow.

## AUDIT-I08 — Link original routes to detailed actions and additional operations

Status: proposal.

Connect the 38 retained route step lists to 220 detailed operation references, and explicitly expose the eight audited operations outside those lists for conditional future compositions.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/workflow-to-actions.md](/home/leo/projects/3dmodeling/research/action-audit/workflow-to-actions.md)

Original source: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md)

Original proposal: [research/action-audit/workflow-to-actions.md](/home/leo/projects/3dmodeling/research/action-audit/workflow-to-actions.md), line 1.

Next check: Use the linked supported-input, backend and future-case contracts when implementing or composing that workflow.

## AUDIT-REC-04 — Convert video into an image reconstruction dataset — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Convert video into an image reconstruction dataset. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-03 — Estimate camera poses and sparse structure from overlapping photos — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Estimate camera poses and sparse structure from overlapping photos. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-CAD-16 — Reconstruct camera poses and dense visible geometry from overlapping photos — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Reconstruct camera poses and dense visible geometry from overlapping photos. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-05 — Register RGB and depth frames and estimate sequence poses — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Register RGB and depth frames and estimate sequence poses. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-06 — Integrate calibrated RGB-D frames into point cloud or TSDF mesh — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Integrate calibrated RGB-D frames into point cloud or TSDF mesh. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-21 — Depth frames to registered point cloud or mesh — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Depth frames to registered point cloud or mesh. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-17 — Build dense point cloud and mesh from SfM camera solution — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Build dense point cloud and mesh from SfM camera solution. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-28 — Dense multi-view stereo to point cloud and mesh — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Dense multi-view stereo to point cloud and mesh. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-29 — Point cloud to surface mesh — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Point cloud to surface mesh. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-20 — Photos/video to camera solution, point cloud and mesh — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Photos/video to camera solution, point cloud and mesh. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-10 — Estimate multi-view depth, camera poses and Gaussian outputs — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Estimate multi-view depth, camera poses and Gaussian outputs. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-18 — Generate a single-image mesh proxy — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Generate a single-image mesh proxy. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-19 — Train and export a Gaussian splat scene — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Train and export a Gaussian splat scene. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-20 — Train and export a NeRF scene — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Train and export a NeRF scene. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-REC-11 — Train NeRF or Gaussian scene for view synthesis — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Train NeRF or Gaussian scene for view synthesis. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-22 — Photographs to Gaussian/NeRF visual scene — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Photographs to Gaussian/NeRF visual scene. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## AUDIT-DOM-30 — Photos to NeRF visual scene — detailed execution options

Status: proposal.

Point 07 defines 3 actions, four software/AI modes, evidence-based alternative selection/merge, proposed helpers and future validation cases for Photos to NeRF visual scene. Detailed contracts and conditions are retained in the linked operation record.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

Original proposal: [research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md), line 1.

Next check: Exercise the specified implementation cases under the corresponding implementation scope.

## IMPL-I01 — Evidence-linked implementation queue

Status: proposal.

Link each existing action to inspected code/skill subsets, original result records and required integration changes; preserve the original graph and full operation contracts.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.json](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.json)

Original proposal: [research/action-audit/implementation-queue/queue.json](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.json), line 1.

Next check: Execute the named action implementation plan and retain actual tests under its separately scoped implementation batch.

## IMPL-I02 — Dependency-respecting implementation order

Status: proposal.

Use proposed action resource/effort classes and exact original-route reuse after preceding action dependencies. Preserve original route classifications and conditional upstream prerequisites separately.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.md](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.md)

Original proposal: [research/action-audit/implementation-queue/queue.md](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.md), line 1.

Next check: Execute the named action implementation plan and retain actual tests under its separately scoped implementation batch.

## IMPL-I03 — Per-job source revision and scope record

Status: proposal.

Implement the existing first shared intake action as a per-job source index plus agent-authored scope statement with revision/correction links, streaming hashes and action-specific tests.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/first-action-plan.md](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/first-action-plan.md)

Original proposal: [research/action-audit/implementation-queue/first-action-plan.md](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/first-action-plan.md), line 1.

Next check: Execute the named action implementation plan and retain actual tests under its separately scoped implementation batch.

## PARTS-I01 — Shared reusable parts catalogue

Status: proposal.

Register stable item identity, readable/formal names, descriptions, manufacturer/supplier/project codes, attributed standards and source/CAD/physical locations; connect parts to component outputs and action/tool records.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md)

Original proposal: [research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md), line 1.

Next check: Review the documented catalogue structure and relationships before catalogue implementation.

## PARTS-I02 — Text-file catalogue storage alternatives

Status: proposal.

Compare one CSV plus descriptions, linked CSV files plus generated Markdown, and Markdown-first pages; linked files preserve multiple standards, aliases and artifact revisions.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md)

Original proposal: [research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md), line 1.

Next check: Review the documented catalogue structure and relationships before catalogue implementation.

## PARTS-I03 — Parts field search and future database import

Status: proposal.

Propose initial name/code/standard/category search over text records; retain IDs/relationships for future SQLite/DuckDB import and separately specified vector similarity indexing.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md)

Original proposal: [research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md), line 1.

Next check: Review the documented catalogue structure and relationships before catalogue implementation.

## PARTS-I04 — Future part material and resistance properties

Status: future_work.

Future work requested by the user: add material and resistance properties to each part with sourced values, units and applicability conditions.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md)

Original proposal: [research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md), line 1.

Next check: Define this extension when future work is taken up.

## PARTS-I05 — Future classification by kind of work

Status: future_work.

Future work requested by the user: classification including wood, metal, architecture, mechanical and industrial; define taxonomy and multi-domain relationships in that future extension.

Original source: [/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md)

Original proposal: [research/action-audit/parts-catalogue-proposal.md](/home/leo/projects/3dmodeling/research/action-audit/parts-catalogue-proposal.md), line 1.

Next check: Define this extension when future work is taken up.

## COMP-I01 — Component-led CAD and tooling iterations

Status: proposal.

Use the real ferme component jobs as the development sequence; each job produces geometry/checks and an applied verified improvement to current skills/procedures or Python helpers.

Original source: [/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md)

Original source: [/home/leo/projects/3dmodeling/research/component-development-coverage.md](/home/leo/projects/3dmodeling/research/component-development-coverage.md)

Original proposal: [COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md), line 1.

Next check: Execute the selected component iteration, apply and verify its actual tooling improvement, and retain the three linked records.

## COMP-I02 — Linked component action and parts records

Status: proposal.

FERME owns CAD, component/action occurrence evidence and parts catalogue/database data. This project owns reusable skills, Python helpers/tests, action definitions and instructions for consuming FERME data, linked by exact source/model/tool revisions.

Original source: [/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md)

Original source: [/home/leo/projects/3dmodeling/research/component-development-coverage.md](/home/leo/projects/3dmodeling/research/component-development-coverage.md)

Original proposal: [COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md), line 1.

Next check: Execute the selected component iteration, apply and verify its actual tooling improvement, and retain the three linked records.

## COMP-I03 — Observed procedure before Python extraction

Status: proposal.

Record action inputs, outputs, representations, units/frames, changed information, alternatives, recovery and handoff conditions; document repeated successful procedures before extracting or extending tested Python functions.

Original source: [/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md)

Original source: [/home/leo/projects/3dmodeling/research/component-development-coverage.md](/home/leo/projects/3dmodeling/research/component-development-coverage.md)

Original proposal: [COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md), line 1.

Next check: Execute the selected component iteration, apply and verify its actual tooling improvement, and retain the three linked records.

## COMP-I04 — Rail and crossmember first iterations

Status: proposal.

Propose the main frame longitudinal rail followed by the dependent crossmember as initial component jobs using their existing proposed 40x40x3 mm sections and separate sourced cut lengths.

Original source: [/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md)

Original source: [/home/leo/projects/3dmodeling/research/component-development-coverage.md](/home/leo/projects/3dmodeling/research/component-development-coverage.md)

Original proposal: [COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md), line 1.

Next check: Execute the selected component iteration, apply and verify its actual tooling improvement, and retain the three linked records.

## COMP-I05 — Dependency and evidence led component priority

Status: proposal.

Preserve all 103 source inputs and route alternatives; select ready jobs by geometric inputs, source evidence, local computation and useful repeated actions; use the existing graph/queue as action definitions and integration references.

Original source: [/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md)

Original source: [/home/leo/projects/3dmodeling/research/component-development-coverage.md](/home/leo/projects/3dmodeling/research/component-development-coverage.md)

Original proposal: [COMPONENT_DEVELOPMENT_PLAN.md](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md), line 1.

Next check: Execute the selected component iteration, apply and verify its actual tooling improvement, and retain the three linked records.

## COMP-I06 — Required tube corner-profile input

Status: proposal.

Observed rail preflight requires a sourced tube corner profile or explicit nominal representation decision before dependent native construction.

Original source: [/home/leo/projects/3dmodeling/execution/2026-11-12-component-led.md](/home/leo/projects/3dmodeling/execution/2026-11-12-component-led.md)

Original proposal: [execution/2026-11-12-component-led.md](/home/leo/projects/3dmodeling/execution/2026-11-12-component-led.md), line 1.

Next check: Resolve the named feature input and exercise the matching native component actions with their own checks.

## COMP-I07 — Reuse the newly extracted FERME CAD modules

Status: proposal.

Current FERME Client/Journal/Geometry/recipe and verification modules replace temporary-wrapper reuse assumptions for matching native operations; retain their existing tests and explicit data ownership.

Original source: [/home/leo/projects/3dmodeling/execution/2026-11-12-component-led.md](/home/leo/projects/3dmodeling/execution/2026-11-12-component-led.md)

Original proposal: [execution/2026-11-12-component-led.md](/home/leo/projects/3dmodeling/execution/2026-11-12-component-led.md), line 1.

Next check: Resolve the named feature input and exercise the matching native component actions with their own checks.

## COMP-I08 — Cold-formed tube nominal corner geometry

Status: proposal.

For the proposed 40×40×3 mm main-frame rail and crossmember, EN 10219-2:2019 Annex A.3 provides nominal section-property radii of 6 mm outside and 3 mm inside. Table 3 separately gives the 4.8–7.2 mm external manufacturing profile interval. A CAD reference representation can carry this named calculation basis; supplier conformity requires its own product evidence.

Original source: [/home/leo/projects/3dmodeling/research/tube-corner-research.md](/home/leo/projects/3dmodeling/research/tube-corner-research.md)

Original proposal: [research/tube-corner-research.md](/home/leo/projects/3dmodeling/research/tube-corner-research.md), line 1.

Next check: Use the source-defined nominal model label when this calculation convention is the chosen representation; preserve supplier process evidence separately.

## COMP-I09 — Hot-finished tube nominal corner geometry

Status: proposal.

EN 10210-2:2019 Annex A.3 supplies the alternative nominal section-property radii of 4.5 mm outside and 3 mm inside at 3 mm nominal wall thickness. Table 2 supplies a 9 mm default external maximum, with a 6 mm maximum under order option 2.2. Keep this process-specific branch linked to the same rail/crossmember source sheets.

Original source: [/home/leo/projects/3dmodeling/research/tube-corner-research.md](/home/leo/projects/3dmodeling/research/tube-corner-research.md)

Original proposal: [research/tube-corner-research.md](/home/leo/projects/3dmodeling/research/tube-corner-research.md), line 1.

Next check: Match the hot-finished branch to product evidence before assigning it as actual supply geometry.

## COMP-I10 — Measured tube corner geometry

Status: proposal.

For a model representing actual stock geometry, EN 10219-2:2019 clause 7.7 describes external profile measurement using a radius gauge or corner offsets. Record actual stock measurements as a separate input revision linked to the supplier item and the main-frame component records.

Original source: [/home/leo/projects/3dmodeling/research/tube-corner-research.md](/home/leo/projects/3dmodeling/research/tube-corner-research.md)

Original proposal: [research/tube-corner-research.md](/home/leo/projects/3dmodeling/research/tube-corner-research.md), line 1.

Next check: Retain measurement locations, units, method and observed values when measurements are available.

## COMP-I11 — Record source research as separate component actions

Status: proposal.

Four source-preparation definitions and their actual supplier/standard/access/calculation occurrences are implemented and linked to the original intake/solid-route actions. Each retains software/agent responsibilities and evidence.

Original source: [/home/leo/projects/3dmodeling/execution/p01-rail-build.md](/home/leo/projects/3dmodeling/execution/p01-rail-build.md)

Original proposal: [execution/p01-rail-build.md](/home/leo/projects/3dmodeling/execution/p01-rail-build.md), line 1.

Next check: Use the recorded P01 evidence and its next required reopened feature action; retain original graph and source revisions.

## COMP-I12 — Check explicit native selections before dependent commands

Status: proposal.

Live P01 execution exposed clear-only selection semantics. A reusable adapter corrects nonempty explicit selection and verifies actual handles; live resumed extrusion and regression tests exercise the fix.

Original source: [/home/leo/projects/3dmodeling/execution/p01-rail-build.md](/home/leo/projects/3dmodeling/execution/p01-rail-build.md)

Original proposal: [execution/p01-rail-build.md](/home/leo/projects/3dmodeling/execution/p01-rail-build.md), line 1.

Next check: Use the recorded P01 evidence and its next required reopened feature action; retain original graph and source revisions.

## COMP-I13 — Extrude the bounded hollow section directly

Status: proposal.

P01 solid subtraction and planar-region subtraction returned CutRefused. Direct bounded-area extrusion produced the source-defined hollow rail and passed five native feature check groups; preserve all three route outcomes.

Original source: [/home/leo/projects/3dmodeling/execution/p01-rail-build.md](/home/leo/projects/3dmodeling/execution/p01-rail-build.md)

Original proposal: [execution/p01-rail-build.md](/home/leo/projects/3dmodeling/execution/p01-rail-build.md), line 1.

Next check: Use the recorded P01 evidence and its next required reopened feature action; retain original graph and source revisions.

## COMP-I14 — Read reopened binary solid features and resolve native bounds discrepancy

Status: proposal.

P01 saved/reopened DWG stores SAB binary while the current feature reader supports SAT text. Native API bounds are zero beside visible nonzero-volume mesh geometry. Next checker implementation should reuse a supported decoder/query route and repeat required saved-feature checks.

Original source: [/home/leo/projects/3dmodeling/execution/p01-rail-build.md](/home/leo/projects/3dmodeling/execution/p01-rail-build.md)

Original proposal: [execution/p01-rail-build.md](/home/leo/projects/3dmodeling/execution/p01-rail-build.md), line 1.

Next check: Use the recorded P01 evidence and its next required reopened feature action; retain original graph and source revisions.

## COMP-I15 — Reuse an existing SAB parser for saved-body measurements

Status: proposal.

Implemented ezdxf-backed reading of the source-linked saved P01 body graph. Native dimensions and closed topology pass; the prior binary-reader gap now has a successful occurrence while the OCS zero-bounds discrepancy remains attributed.

Original source: [/home/leo/projects/3dmodeling/execution/p01-saved-verification.md](/home/leo/projects/3dmodeling/execution/p01-saved-verification.md)

Original proposal: [execution/p01-saved-verification.md](/home/leo/projects/3dmodeling/execution/p01-saved-verification.md), line 1.

Next check: Apply the supported reader to the next component’s saved geometry and preserve any new exceptions.

## COMP-I16 — Check repeated section lengths against their mating layout and local datum

Status: proposal.

Implemented a nominal rail-gap and crossmember-midpoint check using actual saved native P01/P02 features and the sourced340mm frame outside width. The260mm gap and Z130mm midpoint pass; wrong-width and shifted-origin regression cases fail.

Original source: [/home/leo/projects/3dmodeling/execution/p02-crossmember.md](/home/leo/projects/3dmodeling/execution/p02-crossmember.md)

Original proposal: [execution/p02-crossmember.md](/home/leo/projects/3dmodeling/execution/p02-crossmember.md), line 1.

Next check: Reuse the check only for the documented parallel-rail/local-frame conditions and keep assembly transforms separate.

## COMP-I17 — Check reused detailed components against actual native geometry and source dimensions

Status: proposal.

Applied a source-bound bearing checker to an existingSKFmodel, detected32mmvs21mmcrown and corrected only its housing in a separate derivative. Native reader now handles explicit rigid transforms, spheres,cones and mounting-slot boundaries split by coplanarBooleanfragments;62savedchecks and40testsPASS.

Original source: [/home/leo/projects/3dmodeling/execution/c009-bearing.md](/home/leo/projects/3dmodeling/execution/c009-bearing.md)

Original proposal: [execution/c009-bearing.md](/home/leo/projects/3dmodeling/execution/c009-bearing.md), line 1.

Next check: Use the documented component-label and source-bound dimension conditions for each other component before reusing this reader.

## COMP-I18 — Share strict native component identity reading across checked assemblies

Status: proposal.

Extracted a shared named-solid reader after SKF and Leaf models used Component: labels with different optional spacing. Added an external-job-bound saved Leaf shell, mounting-hole and terminal checker. All 29 saved-geometry checks and 44 helper tests pass; existing drawing bytes remain preserved.

Original source: [/home/leo/projects/3dmodeling/execution/c021-leaf-module.md](/home/leo/projects/3dmodeling/execution/c021-leaf-module.md)

Original proposal: [execution/c021-leaf-module.md](/home/leo/projects/3dmodeling/execution/c021-leaf-module.md), line 1.

Next check: Keep exact required component sets and sourcebound features for each new assembly; reject unknown identities before reusing geometry checks.

## COMP-I19 — Extract measured-feature checks across component families

Status: proposal.

Shared finite comparison, connectivity, vertex-range and Cartesian-cylinder-pattern functions now serve actual Sumitomo driver and Leaf module checks using separate source dimensions. The driver iteration detects and corrects a connector span error; all50 helper tests pass. Spline graph/vertex reading retains its explicit measurement scope.

Original source: [/home/leo/projects/3dmodeling/execution/c012-driver.md](/home/leo/projects/3dmodeling/execution/c012-driver.md)

Original proposal: [execution/c012-driver.md](/home/leo/projects/3dmodeling/execution/c012-driver.md), line 1.

Next check: Reuse only the documented measurement conditions; each next component supplies independent source expectations and native observations.

## COMP-I20 — Measure axial interfaces from analytic surfaces and individual blind bottoms

Status: proposal.

Executed ME0907 recipe and18 saved checks use cylinder radii and planar stations. The observed rear cylinder has two seam vertices atX82mm; vertex transverse span alone cannot provide its164mm diameter. Eight focused cases verify success and wrong/missing features.

Original source: [/home/leo/projects/3dmodeling/execution/c005-me0907.md](/home/leo/projects/3dmodeling/execution/c005-me0907.md)

Original proposal: [execution/c005-me0907.md](/home/leo/projects/3dmodeling/execution/c005-me0907.md), line 1.

Next check: Reuse for source-bound axial cylinder/plane jobs with explicit nominal-thread and keyway representation.

## COMP-I21 — Compare imported assembly placements to original source matrices

Status: proposal.

Executed Victron battery import diagnosed13 reversed placements against original STEP frames,changed only native insertion fields and preserved21 solid definitions.35 saved checks preserve source placements,definition vertices and39 instance paths; current source limits and open-partner records remain explicit.

Original source: [/home/leo/projects/3dmodeling/execution/c023-victron-battery.md](/home/leo/projects/3dmodeling/execution/c023-victron-battery.md)

Original proposal: [execution/c023-victron-battery.md](/home/leo/projects/3dmodeling/execution/c023-victron-battery.md), line 1.

Next check: Reuse only after exact source-frame/native-matrix comparison and supported unit-scale zero-base single-insert conditions.

## COMP-I22 — Reuse a shared mechanical family exterior while retaining exact target identity

Status: proposal.

Littelfuse20EV manufacturer datasheet provides one M6 outline for20EVxxx.ZXBDMC60–150A. The available adjacent60A STEP is a proposed exterior reference for the100A target; source identity,electrical properties and download rights remain separate fields.

Original source: [/home/leo/projects/3dmodeling/execution/c030-fuse-source.md](/home/leo/projects/3dmodeling/execution/c030-fuse-source.md)

Original proposal: [execution/c030-fuse-source.md](/home/leo/projects/3dmodeling/execution/c030-fuse-source.md), line 1.

Next check: Acquire readable family geometry with appropriate access rights;compare mechanical interfaces against the shared manufacturer outline before any variant-specific CAD handoff.

## COMP-I23 — Reconstruct source-labelled case profiles from retained PDF vectors

Status: proposal.

Pilz774310 manufacturer STEP download returned403. Existing Poppler extraction produced47SVG paths fromthe retained dimension drawing. Proposed next interpretation separates case/cover segments,verifies units against dimension leaders anddefines explicit joining rules before native extrusion;terminal andrail-clip features keep separate actions.

Original source: [/home/leo/projects/3dmodeling/execution/c048-pilz-source.md](/home/leo/projects/3dmodeling/execution/c048-pilz-source.md)

Original source: [https://www.pilz.com/download/open/P9745_2009094_-.pdf](https://www.pilz.com/download/open/P9745_2009094_-.pdf)

Original proposal: [execution/c048-pilz-source.md](/home/leo/projects/3dmodeling/execution/c048-pilz-source.md), line 1.

Next check: Verify SVG units,part boundaries andendpoint treatment against the sourced dimensions before constructing any dependent native geometry.

## PLAN-4689b53189 — Native editable source

Status: proposal.

**Native editable source:** Preserve the OCS document, FreeCAD document, procedural Python/OpenSCAD source or IFC model used to create the geometry. Record backend and version.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 34.

Next check: Use the associated workflow operation and stage checks.

## PLAN-56caaa829b — Analytic solid

Status: proposal.

**Analytic solid:** Use a supported boundary-representation route for exact planes, cylinders and topology. Record export settings and reopen measurements. STEP exchange preserves the content its exporter writes; feature history remains in the native source or generator.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 35.

Next check: Use the associated workflow operation and stage checks.

## PLAN-8c55cab9f4 — Polygon mesh

Status: proposal.

**Polygon mesh:** Keep visual and collision meshes as separate derivatives. Record tessellation, simplification, normals, watertightness and unit conversion. Use GLB for packaged visual assets, with consumer-specific STL/OBJ/PLY where appropriate.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 36.

Next check: Use the associated workflow operation and stage checks.

## PLAN-2ba2a4e78b — Point cloud

Status: proposal.

**Point cloud:** Preserve sample positions, coordinate frame, colour, normals and measurement provenance when available. Store filtering and registration transforms.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 37.

Next check: Use the associated workflow operation and stage checks.

## PLAN-e66b1d6316 — Gaussian/NeRF scene

Status: proposal.

**Gaussian/NeRF scene:** Preserve cameras and reconstruction settings with the native representation. Extracted meshes become separately tracked derivatives with their own checks.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 38.

Next check: Use the associated workflow operation and stage checks.

## PLAN-f5a004771a — Building model

Status: proposal.

**Building model:** Use IFC classes, placements, property sets, material assignments, spatial hierarchy and stable element IDs for architecture.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 39.

Next check: Use the associated workflow operation and stage checks.

## PLAN-232d9565fe — Robot model

Status: proposal.

**Robot model:** Preserve the kinematic tree, joint axes, limits, inertial properties, visual/collision mapping and source part IDs in MJCF/URDF packages.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 40.

Next check: Use the associated workflow operation and stage checks.

## PLAN-aa23d7fa31 — Job brief and source intake. A small Python CLI reads a structured model brief and reference files. It records units, fr

Status: proposal.

**Job brief and source intake.** A small Python CLI reads a structured model brief and reference files. It records units, frames, part IDs, required dimensions, intended use, input rights and output formats. Keep the original images, drawings and supplied measurements with hashes.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 46.

Next check: Use the associated workflow operation and stage checks.

## PLAN-ded1d45d0b — Geometry adapters. Reuse the local OCS session-control skill and revision-aware operations. Evaluate build123d and CadQu

Status: proposal.

**Geometry adapters.** Reuse the local OCS session-control skill and revision-aware operations. Evaluate build123d and CadQuery on the same solid fixtures, then retain the one whose API and saved results fit the jobs. Use FreeCAD where an interactive feature tree and constrained sketches are required. Use OpenSCAD for concise CSG and suitable library components.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 47.

Next check: Use the associated workflow operation and stage checks.

## PLAN-6793afc942 — Blender adapter. Execute bounded Python scripts using Blender's native API for scene assembly, visual inspection, meshes

Status: proposal.

**Blender adapter.** Execute bounded Python scripts using Blender's native API for scene assembly, visual inspection, meshes, materials and rendering. Assess MCP bridges against direct scripts for session preservation and reproducibility.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 48.

Next check: Use the associated workflow operation and stage checks.

## PLAN-50542af23f — Reconstruction adapters. Begin with a calibrated photogrammetry route and Open3D/CloudCompare processing. Add a separate

Status: proposal.

**Reconstruction adapters.** Begin with a calibrated photogrammetry route and Open3D/CloudCompare processing. Add a separate GPU experiment for Gaussian scenes and learned object reconstruction after licence and hardware assessment.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 49.

Next check: Use the associated workflow operation and stage checks.

## PLAN-3e1758060e — Domain exporters. Use IfcOpenShell/Bonsai for building semantics and MuJoCo's native loader/compiler for simulation chec

Status: proposal.

**Domain exporters.** Use IfcOpenShell/Bonsai for building semantics and MuJoCo's native loader/compiler for simulation checks. Add URDF exchange when the robot consumer requires it.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 50.

Next check: Use the associated workflow operation and stage checks.

## PLAN-bb44bbceea — Component registry. Store small metadata and procedural sources in Git; select binary storage after measuring fixture si

Status: proposal.

**Component registry.** Store small metadata and procedural sources in Git; select binary storage after measuring fixture sizes and update frequency. Resolve components by stable ID, revision and content hash. Keep supplier models and scanned/generative assets traceable to their respective sources.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 51.

Next check: Use the associated workflow operation and stage checks.

## PLAN-73d65f1f63 — Verification and reports. Each adapter writes its actual execution state, logs, model revision, measured properties and

Status: proposal.

**Verification and reports.** Each adapter writes its actual execution state, logs, model revision, measured properties and output hashes. A readable report links dimensions and component names to the exact model being checked.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 52.

Next check: Use the associated workflow operation and stage checks.

## PLAN-38d9264de7 — Identity

Status: proposal.

**Identity:** `component_id`, readable name, family, revision, source revision, author/manufacturer and part number where applicable.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 84.

Next check: Use the associated workflow operation and stage checks.

## PLAN-dbcd207c9e — Evidence

Status: proposal.

**Evidence:** source URL or file, retrieval date, source hash, licence identifier, licence text path, attribution, redistribution terms and provenance status.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 85.

Next check: Use the associated workflow operation and stage checks.

## PLAN-ceef0f7d05 — Representation

Status: proposal.

**Representation:** native source, generator and parameters, analytic solid, visual mesh, collision mesh, point cloud and their hashes.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 86.

Next check: Use the associated workflow operation and stage checks.

## PLAN-f9c1ac1e06 — Geometry

Status: proposal.

**Geometry:** length unit, local frame, origin, axes, bounding dimensions, interface frames, mounting features and declared tolerances with their sources.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 87.

Next check: Use the associated workflow operation and stage checks.

## PLAN-4fdebd216c — Assembly

Status: proposal.

**Assembly:** child component IDs, occurrence transforms, connection references and joint metadata where applicable.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 88.

Next check: Use the associated workflow operation and stage checks.

## PLAN-87e37a5d5b — Physical properties

Status: proposal.

**Physical properties:** mass, centre of mass, inertia tensor, material and density, each with units, frame and measured/manufacturer/calculated/assumed status.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 89.

Next check: Use the associated workflow operation and stage checks.

## PLAN-bbae17f3cf — Verification

Status: proposal.

**Verification:** backend/version, solid validity, mesh checks, dimensions, importer results and check date tied to the exact revision.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 90.

Next check: Use the associated workflow operation and stage checks.

## PLAN-b010e231c8 — Use and discovery

Status: proposal.

**Use and discovery:** tags, preview paths, permitted uses and consumer formats.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 91.

Next check: Use the associated workflow operation and stage checks.

## PLAN-7710f7d982 — Record the installed OCS build/session capabilities and retain the current local skill behaviour that already works.

Status: proposal.

Record the installed OCS build/session capabilities and retain the current local skill behaviour that already works.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 117.

Next check: Use the associated workflow operation and stage checks.

## PLAN-c61bc50c7e — Exercise one dimensioned bracket with a bore and multiple named parts using the authorized CAD route.

Status: proposal.

Exercise one dimensioned bracket with a bore and multiple named parts using the authorized CAD route.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 118.

Next check: Use the associated workflow operation and stage checks.

## PLAN-512a965fb7 — Compare a curved solid from build123d and CadQuery using identical declared dimensions; assess edits, export, analytic s

Status: proposal.

Compare a curved solid from build123d and CadQuery using identical declared dimensions; assess edits, export, analytic surfaces and saved-file readback.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 119.

Next check: Use the associated workflow operation and stage checks.

## PLAN-09a8ba8a7a — Reopen derivatives in an independent supported importer and inspect part count, bounds, bore size and volume.

Status: proposal.

Reopen derivatives in an independent supported importer and inspect part count, bounds, bore size and volume.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 120.

Next check: Use the associated workflow operation and stage checks.

## PLAN-1a6551fb9c — Deliver the existing-skill capability receipt, one selected procedural-solid adapter, model brief schema and an example

Status: proposal.

Deliver the existing-skill capability receipt, one selected procedural-solid adapter, model brief schema and an example with measured checks.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 121.

Next check: Use the associated workflow operation and stage checks.

## PLAN-901b771935 — Run a dimensioned DXF profile with a hole, a dimensioned raster sketch and a text brief through the intake contract.

Status: proposal.

Run a dimensioned DXF profile with a hole, a dimensioned raster sketch and a text brief through the intake contract.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 127.

Next check: Use the associated workflow operation and stage checks.

## PLAN-f28d152a81 — Create a corresponding part and a simple room with a wall opening; validate the supplied dimensions and geometry feature

Status: proposal.

Create a corresponding part and a simple room with a wall opening; validate the supplied dimensions and geometry features.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 128.

Next check: Use the associated workflow operation and stage checks.

## PLAN-cbefa3284f — Derive Blender visual assets from those same revisions and verify unit/axis mapping numerically.

Status: proposal.

Derive Blender visual assets from those same revisions and verify unit/axis mapping numerically.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 129.

Next check: Use the associated workflow operation and stage checks.

## PLAN-1a8bd7ea9a — Add a small pilot catalogue spanning a mechanical part, an assembly, and an architectural element. Preserve licences, in

Status: proposal.

Add a small pilot catalogue spanning a mechanical part, an assembly, and an architectural element. Preserve licences, interfaces and source dimensions.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 130.

Next check: Use the associated workflow operation and stage checks.

## PLAN-0be37388a9 — Deliver `drawing-to-cad`, `blender-modeling` and `component-library` skills backed by exercised scripts.

Status: proposal.

Deliver `drawing-to-cad`, `blender-modeling` and `component-library` skills backed by exercised scripts.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 131.

Next check: Use the associated workflow operation and stage checks.

## PLAN-ec8f4933ac — Capture or reuse an authorized photo set with calibration evidence and measured control distances.

Status: proposal.

Capture or reuse an authorized photo set with calibration evidence and measured control distances.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 135.

Next check: Use the associated workflow operation and stage checks.

## PLAN-4dcc7a66f0 — Reconstruct cameras and surfaces, then align scale/frame using a subset of controls.

Status: proposal.

Reconstruct cameras and surfaces, then align scale/frame using a subset of controls.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 136.

Next check: Use the associated workflow operation and stage checks.

## PLAN-9656816b09 — Reserve independent measurements for error evaluation. Report per-control residuals in millimetres and surface-fit resid

Status: proposal.

Reserve independent measurements for error evaluation. Report per-control residuals in millimetres and surface-fit residuals over defined regions.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 137.

Next check: Use the associated workflow operation and stage checks.

## PLAN-0f1a7d8855 — Fit relevant planes/cylinders and rebuild a selected part as CAD. Inspect functional dimensions and scan-to-CAD distance

Status: proposal.

Fit relevant planes/cylinders and rebuild a selected part as CAD. Inspect functional dimensions and scan-to-CAD distances.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 138.

Next check: Use the associated workflow operation and stage checks.

## PLAN-18a224b403 — Deliver the capture, photogrammetry, cloud/mesh and scan-to-CAD skills with original images, transformations and measure

Status: proposal.

Deliver the capture, photogrammetry, cloud/mesh and scan-to-CAD skills with original images, transformations and measurements.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 139.

Next check: Use the associated workflow operation and stage checks.

## PLAN-6483ee9ca2 — Create an IFC example with a wall, opening, door/window and storey placement. Check semantic classes, geometric dimensio

Status: proposal.

Create an IFC example with a wall, opening, door/window and storey placement. Check semantic classes, geometric dimensions and a consumer import.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 143.

Next check: Use the associated workflow operation and stage checks.

## PLAN-27cd6e70f2 — Create an articulated robot example with separate links, defined joints and known physical-property inputs.

Status: proposal.

Create an articulated robot example with separate links, defined joints and known physical-property inputs.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 144.

Next check: Use the associated workflow operation and stage checks.

## PLAN-4801fd76a7 — Export visual and collision geometry, compile the MJCF model and check frame transforms, joint ranges and intended conta

Status: proposal.

Export visual and collision geometry, compile the MJCF model and check frame transforms, joint ranges and intended contacts.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 145.

Next check: Use the associated workflow operation and stage checks.

## PLAN-62d81bb930 — Export URDF if the selected robot consumer uses it; compare the imported kinematics and inertial metadata against the so

Status: proposal.

Export URDF if the selected robot consumer uses it; compare the imported kinematics and inertial metadata against the source.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 146.

Next check: Use the associated workflow operation and stage checks.

## PLAN-77b2c7b11e — Deliver `architecture-ifc` and `robot-model-handoff` skills with source-linked verification reports.

Status: proposal.

Deliver `architecture-ifc` and `robot-model-handoff` skills with source-linked verification reports.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 147.

Next check: Use the associated workflow operation and stage checks.

## PLAN-48cc874fa4 — Select a specific tool/model from the licence assessment and record compatible hardware, dependencies and weights.

Status: proposal.

Select a specific tool/model from the licence assessment and record compatible hardware, dependencies and weights.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 151.

Next check: Use the associated workflow operation and stage checks.

## PLAN-a32f23bdee — Benchmark Gaussian scene reconstruction on the metric photo fixture, retaining cameras and transforms.

Status: proposal.

Benchmark Gaussian scene reconstruction on the metric photo fixture, retaining cameras and transforms.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 152.

Next check: Use the associated workflow operation and stage checks.

## PLAN-813e9fa805 — Benchmark learned image-to-3D on an object with known independent dimensions and multi-view references.

Status: proposal.

Benchmark learned image-to-3D on an object with known independent dimensions and multi-view references.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 153.

Next check: Use the associated workflow operation and stage checks.

## PLAN-964bbe8fa0 — Compare runtime, peak memory, output representation, appearance and measured geometry errors. Keep inferred surfaces tag

Status: proposal.

Compare runtime, peak memory, output representation, appearance and measured geometry errors. Keep inferred surfaces tagged through remodeling.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 154.

Next check: Use the associated workflow operation and stage checks.

## PLAN-8406b09c70 — Deliver optional reference-generation skills whose outputs enter the same asset registry and verification process.

Status: proposal.

Deliver optional reference-generation skills whose outputs enter the same asset registry and verification process.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 155.

Next check: Use the associated workflow operation and stage checks.

## PLAN-45cf7dadaf — Provide one CLI entrypoint for intake, adapter execution, inspection and export.

Status: proposal.

Provide one CLI entrypoint for intake, adapter execution, inspection and export.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 159.

Next check: Use the associated workflow operation and stage checks.

## PLAN-9e97c0a279 — Add capability discovery per installed tool and versioned adapter configuration.

Status: proposal.

Add capability discovery per installed tool and versioned adapter configuration.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 160.

Next check: Use the associated workflow operation and stage checks.

## PLAN-08a9699ffb — Record job state, partial outputs and restart points for long reconstruction operations.

Status: proposal.

Record job state, partial outputs and restart points for long reconstruction operations.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 161.

Next check: Use the associated workflow operation and stage checks.

## PLAN-c4065bcf61 — Package exercised skills and pinned environment definitions by workflow family.

Status: proposal.

Package exercised skills and pinned environment definitions by workflow family.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 162.

Next check: Use the associated workflow operation and stage checks.

## PLAN-03f3162f7e — Document examples from each supported input type through its native source and downstream consumer.

Status: proposal.

Document examples from each supported input type through its native source and downstream consumer.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 163.

Next check: Use the associated workflow operation and stage checks.

## PLAN-9792b1d64a — Geometry

Status: proposal.

**Geometry:** Controlling dimensions and allowed errors come from the task brief and intended use. Measure the actual saved geometry. For solids, inspect validity, count, topology, volume, surface types and interfaces. For meshes, inspect scale, normals, disconnected components, degeneracy and watertightness where required.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 167.

Next check: Use the associated workflow operation and stage checks.

## PLAN-c3b188aeb0 — Reconstruction

Status: proposal.

**Reconstruction:** Separate controls used to estimate the transformation from controls used to assess error. Record camera/image coverage, calibrated parameters, registration residuals, point/mesh coverage and local error distributions. Compare inferred and observed regions separately.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 168.

Next check: Use the associated workflow operation and stage checks.

## PLAN-01a11c500a — Interchange

Status: proposal.

**Interchange:** Reopen each supported output using its actual consumer and compare IDs/counts, placements, dimensions and available properties. Retain a numerical conversion factor and explicit source/target frames.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 169.

Next check: Use the associated workflow operation and stage checks.

## PLAN-2174b2591f — Robot dynamics

Status: proposal.

**Robot dynamics:** Record the source of mass and inertia. Test loader compilation, joint-axis direction, limits and defined contact cases. A numerical simulation report describes that specified model and operating conditions.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 170.

Next check: Use the associated workflow operation and stage checks.

## PLAN-75aa388009 — Architecture

Status: proposal.

**Architecture:** Check IFC schema validity, class/property assignments, placements, openings and quantities against the example brief. Exercise the selected architecture consumer.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 171.

Next check: Use the associated workflow operation and stage checks.

## PLAN-c775fed14a — Reproducibility

Status: proposal.

**Reproducibility:** Record tool versions, dependency locks, model-weight revisions, parameters, seeds where relevant, original input hashes, execution logs and output hashes.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 172.

Next check: Use the associated workflow operation and stage checks.

## PLAN-6bf044cba2 — Start with existing OCS use, dimensioned text/sketch modeling and Blender derivatives

Status: proposal.

Start with existing OCS use, dimensioned text/sketch modeling and Blender derivatives: these provide a direct route to CAD on the observed local setup.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 176.

Next check: Use the associated workflow operation and stage checks.

## PLAN-3064c65346 — Add source-backed component reuse and drawing intake

Status: proposal.

Add source-backed component reuse and drawing intake: these reduce repeated modeling and support architecture and robotics together.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 177.

Next check: Use the associated workflow operation and stage checks.

## PLAN-8388d87d3e — Establish metric reconstruction and scan-to-CAD with independent controls

Status: proposal.

Establish metric reconstruction and scan-to-CAD with independent controls: this connects photographic evidence to dimensional geometry.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 178.

Next check: Use the associated workflow operation and stage checks.

## PLAN-656eeb74d7 — Add IFC and MJCF consumers

Status: proposal.

Add IFC and MJCF consumers: these demonstrate the two named application domains.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 179.

Next check: Use the associated workflow operation and stage checks.

## PLAN-7467029c5a — Add GPU reference-generation options against the same fixtures

Status: proposal.

Add GPU reference-generation options against the same fixtures: this provides a measured comparison of appearance and geometry for the additional methods.

Original proposal: [research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), line 180.

Next check: Use the associated workflow operation and stage checks.
