# DOM-R03 — CAD robot assembly to URDF and MJCF

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 4/5; setup 4/5; computing 2/5.**

Output: Editable source CAD assembly plus URDF tree package and a separately authored MJCF model when simulation is required.

## Comparison conditions

Known rigid links and explicit tree joints, clean CAD assembly and sourced mass properties. Closed-loop mechanisms need a separate constraint model; conversion is not automatic.

## Registered starting artifact types

1. cad-assembly
2. joint-set
3. measurement-set
4. material-set

## Detailed source and preparation artifacts

1. Type: cad-assembly; Formats: FreeCAD FCStd; STEP assembly + assembly manifest; Minimum quality: Distinct parts, units and placements, with stable part IDs.; Required evidence: source revision/hash; part tree; units; placements; Handling: Keep neutral original immutable.
2. Type: measurement-set; Formats: CSV/JSON/drawings; Minimum quality: Joint centers, axes, limits and link interfaces tied to datum IDs.; Required evidence: frame; axis; range/unit; measurement evidence; Handling: No visual joint inference.
3. Type: robot-assembly; Formats: JSON joint graph; Minimum quality: Parent-child tree and joint types explicitly authored.; Required evidence: links; joints; source IDs; Handling: Do not infer missing joints.
4. Type: material-set; Formats: supplier/test record; Minimum quality: Mass, COM and inertia tensor expressed in stated link/body frames.; Required evidence: units; frame; source/status; Handling: Never fill absent properties with guessed defaults.

## Reference points, datums and coordinate frames

1. Kind: CAD assembly datum; Fields: part origin; placement transform; Frame: part-local → assembly frame; Source status: CAD source
2. Kind: joint frame; Fields: origin, axis, limits; Frame: child link → parent link; Source status: joint authoring record
3. Kind: inertial frame; Fields: mass, COM, tensor; Frame: body frame; SI; Source status: supplier/test/calculation evidence

## Software, libraries and dependencies

1. Name: FreeCAD Assembly Workbench; Role: review rigid parts and authored joint graph; Software license: LGPL project; imported asset rights separate; Api or entrypoint: Assembly Workbench; inspect placements and constraints; Environment dependencies: FreeCAD build and assembly workbench; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Exchange exporters may not preserve all assembly semantics.; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md
2. Name: ROS URDF/urdfdom; Role: tree robot description; Software license: Tutorial BSD-3-Clause; asset rights separate; Api or entrypoint: URDF XML; `check_urdf <robot.urdf>`; Environment dependencies: urdfdom/ROS consumer as applicable; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: URDF is a tree; richer loops/extensions are consumer-specific.; Source urls: https://github.com/ros/urdf_tutorial
3. Name: MuJoCo; Role: compile and simulate explicit MJCF; Software license: Apache-2.0 software; each asset separate; Api or entrypoint: `mujoco.MjModel.from_xml_path(path)`; Environment dependencies: MuJoCo Python/C runtime; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: MJCF and URDF have different semantics.; Source urls: https://github.com/google-deepmind/mujoco; https://mujoco.readthedocs.io/en/latest/XMLreference.html

## Procedure

1. Action: Inspect CAD units, tree and transforms.; Tool: FreeCAD; Command or api: Open source assembly; record each part local frame.; Preserves: Original CAD; Changes or infers: Assembly metadata.; Check: Part count/bounds vs source.; Code status: existing_tool_entrypoint
2. Action: Author joints and limits from design or measurements.; Tool: Assembly graph authoring; Command or api: Enter parent/child, joint origin/axis/type/range explicitly.; Preserves: Datum evidence; Changes or infers: Robot assembly graph.; Check: Graph connectedness, cycles and axis frame review.; Code status: manual
3. Action: Export URDF tree and mesh package.; Tool: URDF adapter; Command or api: Write visual/collision/inertial separately; run `check_urdf`.; Preserves: Graph and meshes; Changes or infers: URDF tree; CAD feature history lost.; Check: Parse, resolve mesh URI, compare FK transforms.; Code status: assisted
4. Action: Author equivalent MJCF when needed.; Tool: MuJoCo XML/API; Command or api: Create `<body>`, `<joint>`, `<inertial>`, `<geom>` with frames and sourced values; compile using `MjModel.from_xml_path`.; Preserves: Same graph and data; Changes or infers: MJCF model; actuators/contact options are new model choices.; Check: Compile, compare body/joint transforms and mass properties.; Code status: assisted

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-08; Name: CAD assembly to articulated robot structure; Inputs: cad-assembly; joint-set; measurement-set; Outputs: robot-assembly; Tools: FreeCAD Assembly Workbench; explicit robot-description authoring; CAD-to-URDF scripts as candidates; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md; https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md; https://github.com/boelnasr/CAD_TO_URDF; Prerequisites: Rigid link groups, parent-child relation, joint type, axis/frame/limits and fixed connections are explicit or reviewed.; Preserves: CAD part IDs, geometry, named joint frames, source measurements and assembly transforms.; Changes or infers: Groups occurrences into links; assembly constraints are mapped to robot joints; inferred joint types remain hypotheses.; Checks: Graph connectivity, tree/loop identification, frame transforms, axis signs and limit source.; Alternatives: Author URDF joint records directly; export FreeCAD Assembly4 through community script; inspect CAD_TO_URDF inferred tree.; Automation: mixed; Evidence status: documented_capability; Summary: Translate a mechanical assembly into explicit link and joint semantics; CAD hierarchy alone is insufficient.; Source ids: DSRC-12; DSRC-14; DSRC-15
2. Id: DOM-12; Name: Export mesh assets for MuJoCo; Inputs: ; Outputs: mesh; Tools: CAD mesh exporter; Blender; Open CASCADE tessellation; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst; [domains-and-components.md](../../domains-and-components.md); Prerequisites: Tessellation settings and mesh local frame/units chosen.; Preserves: Source CAD/B-rep and conversion parameters.; Changes or infers: Surface geometry becomes triangles; MuJoCo supports OBJ and binary STL; material assignment is separate.; Checks: Bounds, scale, normals, topology, source/mesh overlay and referenced geom role.; Alternatives: MuJoCo primitives for simple geometry; custom decoder plugin for other asset formats.; Automation: scripted; Evidence status: documented_capability; Summary: Create simulation mesh files and retain their source frame and approximation settings.; Input alternatives: cad-solid; b-rep; visual-scene; robot-assembly; Source ids: DSRC-20; DSRC-22; DSRC-13
3. Id: DOM-13; Name: Generate convex collision set; Inputs: mesh; Outputs: collision-set; Tools: CoACD; V-HACD; primitive fitting; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Prerequisites: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Alternatives: Primitive colliders; single convex hull for coarse bounding; use original mesh only where supported and semantics understood.; Automation: scripted; Evidence status: documented_capability; Summary: Derive a collision-specific approximation and review topology-sensitive errors.; Source ids: DSRC-23; DSRC-24; DSRC-20
4. Id: DOM-14; Name: Calculate or import physical mass properties; Inputs: ; Outputs: mass-properties; Tools: CAD kernel mass properties; MuJoCo compiler geom inference; measured scale; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; [implementation-plan.md](../../implementation-plan.md); Prerequisites: Geometry scale/frame and density or measured mass stated; inertia reference frame defined.; Preserves: Raw input values, source evidence, units and chosen frame.; Changes or infers: Computes volume/COM/inertia from B-rep or mesh and density, or assigns measured values.; Checks: Mass positive; tensor symmetric/positive-definite and triangle inequalities; compare independent mass where available; confirm mesh watertightness.; Alternatives: Measured mass and center of gravity; manufacturer data; calculated mass with explicit density assumption.; Automation: mixed; Evidence status: documented_capability; Summary: Attach physical properties to the exact geometry revision and label calculation assumptions.; Input alternatives: physical-measurement-set; material-set; cad-solid; material-set; b-rep; material-set; mesh; material-set; cad-assembly; Source ids: DSRC-20; DSRC-19; DSRC-01
5. Id: DOM-09; Name: Robot assembly to URDF package; Inputs: robot-assembly; joint-set; mass-properties; Outputs: urdf; mesh; Tools: URDF XML/Xacro authoring; ROS urdf_tutorial; CAD-to-URDF adapter proposal; Source urls: https://github.com/ros/urdf_tutorial; https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html; https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF; Prerequisites: Robot link/joint tree defined; mesh units and origins known; mass/inertia records have source and frame.; Preserves: Part IDs, joint axes, limits, mesh lineage, mass/inertia provenance.; Changes or infers: CAD links become URDF links; supported tree joints are mapped; CAD history/material layers may be omitted.; Checks: Parse URDF; graph tree; positive mass and valid inertia; FK transforms; mesh path resolution and RViz/model consumer load.; Alternatives: URDF for ROS ecosystem; direct MJCF for simulator-rich model.; Automation: mixed; Evidence status: documented_capability; Summary: Export a reviewed robot assembly into ROS link/joint XML and mesh assets.; Source ids: DSRC-16; DSRC-17; DSRC-18; Input alternatives: visual-scene; collision-set
6. Id: DOM-10; Name: URDF import and MJCF conversion; Inputs: urdf; mesh; Outputs: mjcf; Tools: MuJoCo URDF parser/compiler; mjSpec API; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst; Prerequisites: URDF files and referenced meshes resolve; mass/inertia and units are coherent.; Preserves: Original URDF; input meshes; declared mapping and MuJoCo version.; Changes or infers: URDF subset compiles into MJCF/mjSpec; actuator model absent in URDF; unsupported features require authoring.; Checks: Load/compile; compare joint count/limits/axes and FK; inspect dropped or defaulted fields; validate XML extensions separately.; Alternatives: Author MJCF directly; retain URDF plus MJCF extension if ROS remains source consumer.; Automation: scripted; Evidence status: documented_capability; Summary: Use MuJoCo's URDF parser as a conversion bridge and record its subset/losses.; Source ids: DSRC-19; DSRC-20; DSRC-21

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Path: See the selected tool/variant contract.; Summary: Use the software/API entry points below in the recorded procedure; manual CAD, joint and semantic authoring steps use the explicit frames and source data recorded for that step.; Related entrypoints: ; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md; https://github.com/ros/urdf_tutorial; https://github.com/google-deepmind/mujoco; https://mujoco.readthedocs.io/en/latest/XMLreference.html; Entrypoints: Assembly Workbench; inspect placements and constraints; URDF XML; `check_urdf <robot.urdf>`; `mujoco.MjModel.from_xml_path(path)`

## Output artifacts

1. Type: cad-assembly; Format: FCStd + immutable STEP; Retained: Editable source assembly and part identifiers.; Loss or inference: Neutral formats may omit feature history.
2. Type: urdf; Format: URDF + meshes; Retained: Tree links, joints, visuals, collisions and sourced inertia.; Loss or inference: Closed loops, CAD feature history and some joint semantics may be lost.
3. Type: mjcf; Format: MJCF XML + external assets; Retained: Explicit MuJoCo body/joint/geom/inertial tree.; Loss or inference: Not guaranteed equivalent to URDF physics or controls.

## Checks

1. CAD part units and placements; graph parent uniqueness; all movable axes/ranges have evidence.
2. URDF parse, mesh URIs and forward-kinematics check.
3. MJCF compile, assets resolve, inertia tensor and frame checks.
4. Cross-compare selected joint configurations and source CAD datum locations.

## Failure recovery

1. CAD importer changes units: revert to source and set units explicitly.
2. Graph has cycle: identify closed-chain method or select supported tree submodel with documented omitted links.
3. URDF/MJCF differs: compare frame transforms and axis conventions, correct adapter mapping, preserve source.
4. No inertia evidence: leave model as kinematic-only where consumer supports, or stop physical simulation.

## Effort and computing classification

1. **Human:** 4
2. **Setup:** 4
3. **Compute:** 2
4. **Human reason:** Joint graph authoring and cross-format semantics require review.
5. **Setup reason:** CAD, URDF and simulator tooling plus adapters.
6. **Compute reason:** Small tree and XML operations; large meshes dominate.

## Resources and scaling

1. **Cpu:** CPU geometry/XML operations.
2. **Gpu:** No GPU for format conversion.
3. **Ram:** Part count, mesh triangles and CAD tessellation.
4. **Storage:** Native CAD, URDF/MJCF and meshes; retain source and hashes.
5. **Scaling drivers:** link count; mesh triangles; collision hulls
6. **Variants:** Known tree easiest.; Closed loop requires specialized modeling.

## Detailed branch procedures

1. [dom-r02.md](dom-r02.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md)
2. [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial)
3. [https://github.com/google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)
4. [https://mujoco.readthedocs.io/en/latest/XMLreference.html](https://mujoco.readthedocs.io/en/latest/XMLreference.html)

Full source summaries: [source register](../../sources/source-register.md).
