# Point 06 — Building and robot structure and properties

Date: 2026-11-12. Status: **procedure proposal**. Scope: 19 operations and 57 actions. Requested procedure-design dispatch: `gpt-6-astra`, `xhigh`; actual executing model identity: **unavailable**.

[Structured actions](point-06-operations.json) contain all 15 required fields for each action, four execution modes, sources, alternatives, merge rules, migration and future cases. This document supplies the concrete steps, outputs, checks and helper contracts. [Original domain records](../workflows/domain-paths.json), [audit plan](plan.md), [sequence](sequence.json), [implementation plan](../implementation-plan.md), OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) and model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) remain the source contracts. Procedures, helpers and cases are proposals; acceptance labels use `MARK AS ACCEPTED`.

## 1. Terms and action responsibilities

1. **CAD** is computer-aided design. A **B-rep**, boundary representation, stores faces, edges and their connections; **topology** describes those connections. **Tessellation** approximates surfaces using triangle facets. A B-rep can itself have faceted surfaces.
2. A **component definition** identifies source geometry; an **occurrence** is a distinct placed instance. A **rigid link/body** groups parts with fixed relative motion. A **graph** contains named nodes and relations; a **tree** has one parent per non-root node and no cycle. A **closed loop** adds a relation that returns to an already connected body.
3. A **joint** defines permitted relative motion. **Degrees of freedom** are independent motion coordinates. **Forward kinematics** calculates body poses from joint coordinates. An **axis** needs direction and a named coordinate frame. A **datum** is a sourced reference point, axis or plane.
4. **URDF**, Unified Robot Description Format, represents robot links/joints and their geometry/physical data. **MJCF**, MuJoCo XML Format, is MuJoCo's native model description. A **compiler** converts source descriptions into the consumer's working representation; a saved editable source and a compiled model have separate identities.
5. **Visual geometry** serves appearance; **collision geometry** serves contact queries; **mass-distribution geometry** supports physical-property calculation under stated material assumptions. **Convex** geometry contains the straight segment between any two of its points. A **convex decomposition** approximates a concave object with separate convex pieces.
6. **COM**, centre of mass, locates the mass-weighted centre. An **inertia tensor** is a symmetric matrix describing rotational mass distribution about a stated point and axes. **Principal moments** are its diagonal values in principal axes. A **parallel-axis shift** translates the tensor's reference point; **density** is mass per volume.
7. **IFC**, Industry Foundation Classes, stores building objects, geometry, properties and relationships. **BIM**, building information modeling, uses such object/relationship information. **GlobalId** identifies an IFC entity; converted source identifiers retain their own namespace. A **schema** defines permitted entity/field structures. A **geometric context** defines representation coordinates/precision. **IDS**, Information Delivery Specification, states machine-checkable delivery requirements when supplied.
8. **Containment** associates an element with its spatial container; **aggregation** organizes spatial parts. A **void relationship** associates an opening with its host; a **filling relationship** associates a filling element with the opening. Geometric holes and those semantic relationships receive separate checks.
9. **CRS**, coordinate reference system, identifies geographic/projected coordinates. Model placements, project units, map conversion and vertical datum have separate records. **SI** is the international system of units; ROS uses metre, kilogram, second and radian conventions.
10. **GLB** is the binary glTF scene format. A **sidecar** is a companion mapping file. A **residual** is a measured difference under a named comparison. A **pinned revision** is an explicitly fixed revision or content hash.
11. A **VLM**, vision-language model, reads images and language together. It receives full source views and located crops, source fields and actual tool-query reports. It proposes source-supported associations, candidate selection or compatible combinations. A separate semantic reviewer execution examines the resulting source meanings; software supplies numerical and artifact checks.

OCS remains the native engineering baseline. Each alternate CAD, IFC, Blender or robot adapter has a named capability requirement and proposed scope. A native group, solid, scene object and parametric assembly constraint are recorded as their actual representations.

## 2. Shared evidence, source contracts and recovery

1. Reuse [point02 component/occurrence evidence](point-02-operations.json), [point03 native geometry/readback and interruption protocol](point-03-operations.json) and [point05 frame/uncertainty protocol](point-05-operations.json). Each transform names source/target revision, unit, axes, handedness, direction and application convention. Unit conversion, rigid placement, numerical-origin shift and map/CRS conversion remain separate.
2. Record engineering allowance, measurement/source uncertainty, geometry approximation, integration/solver criterion and numerical/readback threshold separately per feature or relationship. Layout, appearance, kinematic, contact, physical simulation, semantic building and fabrication branches each state their required coverage/detail and source-backed criteria.
3. A branch retains its source subset/digests, purpose, required features, frames and resource observations. Source-supported VLM selection can choose interpretation within the supplied task; a new design choice remains a user decision. Preserve conflicting values/meanings. A combined result has a new revision and repeats geometry, domain-relationship, physical and saved-consumer checks.
4. Preserve raw inputs, request IDs, native/spec/file revision, hashes, partial outputs and last checked boundary. Reconcile uncertain insertion/save completion before retry to avoid duplicate occurrences. Remote VLM recovery retains prompt/input/source hashes, request/response identity, raw/partial reply and retry lineage; malformed selection rows cannot change the published merge. Recheck source hashes and invalidate affected descendants only.
5. Numerical validation identifies actual saved artifact, reader/kernel and independent controls. Semantic review uses a separate execution instance and records its identity plus shared source/model/kernel dependencies. Parsing, schema validation, compilation, geometric agreement and physical evidence have individual results.

### Robot units, source serialization and effective geometry

[ROS REP-103](https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst) specifies SI and right-handed body coordinates. The inspected [URDF joint source](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/joint.hpp) and [inertial source](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/link.hpp) supply parent/child, origin, type-specific axis and symmetric tensor fields. A fixed or floating joint does not use an axis; continuous joints do not acquire invented finite travel limits.

[MuJoCo model editing](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html) and [XML reference](https://mujoco.readthedocs.io/en/stable/XMLreference.html) document editable specification parsing, compilation and separate XML serialization. `MjSpec.from_file/from_string` parses; the selected binding's compile route produces the compiled model; `mj_saveXML`, `mj_saveXMLString` or `mj_encode` supplies editable XML through the evidenced binding. `savecompiled=true` saves compilation-made canonical values; false saves authored/parsed values. Expanded includes/macros, discarded comments and attached compiler settings belong in the loss report. Original source text remains preserved.

MJCF's angle default is degrees; URDF uses radians. MuJoCo physical units must be chosen consistently. URDF importer defaults `discardvisual=true` and `fusestatic=true` can change geoms/body counts; retain actual settings and mappings. `inertiafromgeom=auto` infers properties when the inertial element is absent; true overrides explicit values. A body tree retains any extra loop edge through a supported constraint whose constrained freedoms match the mechanism. Connect/weld behavior receives explicit closure criteria.

MuJoCo compiler mesh centering/principal-axis processing retains raw asset coordinates, `mesh_scale`, `mesh_pos`, `mesh_quat` and referencing geom/body/world transforms. Compare effective placed vertices or surfaces through that complete chain. Visual, collision and inertial roles remain separate even when their source geometry coincides.

### Physical-property calculation contract

[OCCT 8.0.1 BRepGProp](https://occt3d.com/dev/doc/refman/html/class_b_rep_g_prop.html) supplies `VolumeProperties`; [GProp_GProps](https://dev.opencascade.org/doc/refman/html/class_g_prop___g_props.html) supplies `Mass`, `CentreOfMass`, `MatrixOfInertia` and `Add`. This optional backend is a proposed calculation adapter.

1. Validate finite closed, coherently oriented solids and applicable material distribution before integration; the integration API assumes these conditions. Record exact-surface versus triangulation mode and numerical integration settings.
2. Preserve no-density geometric integrals. Volume scales with length cubed; geometric volume inertia scales with length to the fifth power. Apply coherent material density exactly once. A unit-density geometric `Mass()` value can be volume until physical density is applied.
3. Decode every raw tensor's component order and matrix off-diagonal versus signed/unsigned product convention. Record its reference point, orientation and units. Convert it to a common symmetric matrix before frame operations.
4. GProp COM is expressed in absolute Cartesian coordinates; its tensor is central, with axes parallel to the absolute axes. Rotate a central tensor with **I_target = R I_centre Rᵀ**. Shift it to a named origin with **I_origin = I_centre + m((r·r)Identity − r rᵀ)** in a common frame. Sum component masses/origin tensors and subtract the corresponding shift to obtain the aggregate COM tensor. Preserve each calculation term and source membership.
5. MJCF `fullinertia` order is M11, M22, M33, M12, M13, M23; its compiler diagonalizes the matrix into inertial orientation and diagonal values. Record any compiler adjustment separately. Check source format/reference convention before writing URDF or MJCF.
6. Mass, COM and tensor completeness are independent. Symmetry, principal-moment positivity/triangle inequalities and integration error are numerical checks. Independent measurement and distribution evidence support physical accuracy. Scalar mass alone supplies a mass field.

### Collision, IFC and display contracts

[CoACD](https://github.com/SarahWeiii/CoACD) documents OBJ input, OBJ/WRL output and `-sp/--split` for separately written convex components. `-i/--input` and `-o/--output` are documented aliases. Its threshold is normalized unless real-metric mode is selected; real-metric uses metre-valued error with metre-scale input. Hull-count limiting with merge can exceed the threshold. Source defaults supply no project criterion. Required passages and contacts receive their own checks.

[IfcOpenShell geometry processing](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html) and [geometry API](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html) distinguish single-shape extraction from whole-element iterator output. Element-level opening subtraction is documented default. Python mesh vertices have no unit tag: preserve project scale/settings and verify actual dimensions. Triangle and non-triangulated OpenCASCADE/PythonOCC paths remain separate. Inspect actual face/shape type; faceted IFC can produce faceted B-rep.

[IfcConvert](https://docs.ifcopenshell.org/ifcconvert/usage.html) supports GLB, defaults geometric output to metres and offers explicit model-unit/world-coordinate options. Its documented `--use-element-guids` naming applies to OBJ/DAE/STEP/SVG, so the CLI GLB branch uses a separately checked identity sidecar. The Python GLB serializer example has its own optional GUID setting and explicit metre declaration. Preserve element→node/primitive and shared-mesh→occurrence mappings; node order or appearance cannot supply identity.

[Blender importer source](https://github.com/blender/blender/blob/main/scripts/addons_core/io_scene_gltf2/blender/imp/blender_gltf.py) maps glTF Y-up to Blender Z-up as (x, −z, y), with location conversion by 1/scene unit scale. This is mutable source evidence; pin the actual selected version. [IFC add_representation](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_representation/index.html) produces a representation from its supported Blender inputs; product class, placement and relationships have separate authoring actions.

The local IFC provenance example (`${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json`) records converted source-part IDs, millimetre-to-metre scale 0.001, preserved local orientation and geometric opening holes. Its semantic opening relationships are separately recorded. Those are fixture-specific findings, not generic project dimensions or geographic assignments.

### Original-contract findings

1. DOM-09 requires robot-assembly, joint-set and mass-properties **plus** visual-scene or collision-set. The target consumer determines additional required roles; a visual-only visualization package can satisfy its declared checks. Role clarification is a proposed refinement of the original contract.
2. DOM-14's measured-only branch retains only actually supplied mass/COM/tensor fields. DOM-16 emits mesh; DOM-27 owns B-rep extraction. DOM-24 accepts camera-solution alone for a camera-only scene.
3. DOM-32 modifies geometry in an existing MJCF while preserving its graph/actuator/sensor contract. An incompatible rebuilt model belongs to separately scoped DOM-11.
4. DOM-25 requires dimensions/materials plus solid or assembly and linked process/recipient criteria. Its optional [TechDraw SVG path](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/TechDraw_ExportPageSVG.md) uses `TechDrawGui.exportPageAsSvg(DrawPageObject,FilePath)` with active GUI and an existing populated page; hatch omission and text placement/size changes require readback. That source establishes SVG only.
5. DOM-35 needs actual target class/placement/relationship evidence and a supported representation adapter. DOM-37 needs an explicit parent/root and attachment evidence. Original typed inputs do not silently supply those values.

## 3. DOM-31 — Author assembly graph and joint set

**Inputs and dependencies.** CAD assembly, measurement-set and model-brief; occurrence IDs/placements and component revisions. Point02 component/assembly records; actual selected application's occurrence capability.

**Source entry points.** [FreeCAD Assembly documentation](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [ROS URDF tutorial](https://github.com/ros/urdf_tutorial), [urdf_model/joint.hpp — ros/urdfdom_headers rolling branch](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/joint.hpp), [REP-103: Standard Units of Measure and Coordinate Conventions — ros-infrastructure/rep master](https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-31-A01 — Bind assembly occurrences and motion evidence.** Read source assembly revision and placements. Associate each occurrence with measured interfaces and brief motion claims. Mark candidate rigid groups and unresolved moving connections. Output: Occurrence-to-rigid-group candidates and named motion/interface evidence. Check: Every occurrence is mapped or explicitly excluded; fixed relation needs evidence.
2. **DOM-31-A02 — Author named joint records and graph topology.** Record each relation in named parent and child frames. Set joint type and sourced position plus type-applicable axis/plane normal and limits/units; retain fixed/floating axis fields as inapplicable. Report connectivity, roots and every cycle or disconnected component. Output: Joint records with parent/child, type, joint-frame origin/axis, limits/units and tree/loop classification. Check: Required revolute/continuous/prismatic axes and planar normals are nonzero/unit-normalized in their stated frame; fixed/floating joints require no invented axis. Type-specific units and limit fields agree, and closed loops retain explicit edges. Continuous rotation keeps its sourced axis while omitting finite lower/upper travel bounds; consumer-specific effort/velocity rules remain explicit.
3. **DOM-31-A03 — Check reference and moved configurations.** Compare reference transforms to CAD placements. Evaluate specified motion directions/ranges and loop closure conditions. Publish graph/joints with supported configurations and exceptions. Output: Assembly-graph and joint-set with forward-transform and semantic review receipts. Check: A tree check cannot discharge loop closure; moving-part identity and source limits pass separately.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent interprets rigid groups and authors relations from evidence. |
| Software and agent | Software traverses/transforms; agent resolves motion interpretation. |
| Software handles ordinary cases | Checked joint families map automatically; cycles, missing axes or conflicting limits enter review. |
| Deterministic supported case | Explicit groups, relations, frames and checks produce deterministic graph records. |

**Alternatives and quality targets.** Use existing source application's joint mapping with versioned semantics. Author measured relation records beside OCS geometry. Retain a layout assembly with unresolved motion; working robot requires sourced joints/closure.

**Proposed helpers.** DOM-31-A01: graph intake maps occurrence IDs, source evidence and candidate rigid groups without editing source geometry. DOM-31-A02: joint author emits typed records and cycle edges, validates unique names, type-applicable axes/normals and limit fields; preserves inapplicable fields explicitly and never invents placeholder axes. DOM-31-A03: graph verifier emits per-joint pose residuals, unresolved closure conditions and downstream readiness.

**Selection and merge.** Independent grouping/joint candidates share occurrence revisions and reference configuration, while declaring layout versus motion targets. VLM compares source interfaces and motion evidence with numerical transform reports. Select consistent complete relations; preserve incompatible axes/types rather than averaging. New graph revision repeats connectivity, source-interface and configured-motion checks with separate semantic review.

**Migration and future cases.** Automate demonstrated occurrence/joint classes after direction, limit, duplicate ID, disconnected graph and loop cases. Swapped parent/child yields reference/motion disagreement. A closed four-link loop remains explicit and blocks a tree-only export until a scoped representation is supplied. Symmetric geometry permits two axis interpretations; source motion evidence selects or retains alternatives. Fixed/floating joints with inapplicable axis fields pass their supported consumer checks; a planar joint requires its sourced nonzero plane normal. Placeholder axes are never synthesized to satisfy schema. Continuous joint requires a sourced nonzero normalized rotation axis and omits finite lower/upper travel bounds; selected-consumer effort/velocity requirements are checked separately.

## 4. DOM-37 — Author robot assembly from CAD component

**Inputs and dependencies.** Cad-solid, measurement-set, model-brief and component-record; target parent/frame from brief or supplied assembly context. Point02 intake/placement and native OCS geometry; alternate assembly backend requires scoped capability.

**Source entry points.** [FreeCAD Assembly documentation](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [ROS URDF tutorial](https://github.com/ros/urdf_tutorial), [urdf_model/joint.hpp — ros/urdfdom_headers rolling branch](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/joint.hpp), [REP-103: Standard Units of Measure and Coordinate Conventions — ros-infrastructure/rep master](https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-37-A01 — Bind sourced component to target robot role.** Pin component bytes and solid revision. Resolve target parent and required interfaces. Bind source measurements and intended motion to attachment. Output: Component/target manifest and sourced attachment plan. Check: A standalone component cannot silently invent the remainder of a robot or its parent transform.
2. **DOM-37-A02 — Create separate occurrence and authored joint relation.** Create a distinct source-linked occurrence at the measured transform. Author fixed/movable relations through DOM-31. Record actual native representation and all three required output identities. Output: New native occurrence/assembly revision, occurrence-source map and joint candidates. Check: Source geometry stays pinned; new assembly occurrence IDs and measured interfaces correspond.
3. **DOM-37-A03 — Validate attachment and publish three outputs.** Read actual saved native assembly. Compare mount interfaces and graph/reference transforms. Publish all three outputs with required checks. Output: Three checked outputs with interface, frame and source receipts. Check: Geometry grouping alone cannot fulfill joint semantics; all output references match one revision.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent selects source-supported attachment and directs insertion. |
| Software and agent | Software places/checks; agent authors component role and motion. |
| Software handles ordinary cases | Repeated checked attachment families run with exceptions for unknown parent or interfaces. |
| Deterministic supported case | Complete component/parent/transform/joint records produce checked outputs. |

**Alternatives and quality targets.** Insert into an existing explicitly supplied assembly. Create a declared root/body when the brief defines one. Use layout occurrence without motion readiness for arrangement; working attachment requires joint/interface evidence.

**Proposed helpers.** DOM-37-A01: attachment intake emits source component, parent context and unresolved interface dependencies. DOM-37-A02: component inserter takes source/target revision and explicit transform and returns native handles plus graph relations. DOM-37-A03: attachment publisher checks cross-artifact IDs/transforms and emits per-output readiness.

**Selection and merge.** Attachment alternatives share component bytes, parent revision and sourced interfaces with target detail/criteria. VLM reviews source mount/role evidence; software compares transforms and dimensions. Select a coherent placement/relation pair; combine compatible evidence only. Repeat native readback, cross-output mapping and motion/interface checks.

**Migration and future cases.** Demonstrate parent resolution, repeated occurrence identity, source immutability and all-three-output cases before automation. Missing target parent retains intake but blocks dependent placement. Identical source geometry inserted twice preserves two occurrence IDs. Native assembly exists but joint-set is absent: three-output handoff remains partial.

## 5. DOM-08 — CAD assembly to articulated robot structure

**Inputs and dependencies.** Cad-assembly, joint-set and measurement-set; source transforms and rigid grouping evidence. DOM-31 authored graph and point02 assembly capability.

**Source entry points.** [FreeCAD Assembly documentation](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md), [CAD_TO_URDF repository](https://github.com/boelnasr/CAD_TO_URDF), [urdf_model/joint.hpp — ros/urdfdom_headers rolling branch](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/joint.hpp), [REP-103: Standard Units of Measure and Coordinate Conventions — ros-infrastructure/rep master](https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-08-A01 — Resolve rigid links from authored assembly relations.** Resolve all joint endpoints to occurrences. Group only explicitly rigidly connected parts. Record link local frames and geometry roles. Output: Occurrence-to-link map and expected graph/geometry coverage. Check: Every moving occurrence belongs to its declared link; repeated instances remain distinct.
2. **DOM-08-A02 — Build articulated link and joint representation.** Compose occurrence-to-link and joint transforms. Map each authored relation to its explicit robot type. Preserve loops and unsupported constraints in a named ledger. Output: Robot assembly with links, joints, geometry transforms and explicit loop edges. Check: Source joint type and degrees of freedom survive; arbitrary spanning-tree reduction cannot discard closure.
3. **DOM-08-A03 — Validate robot assembly against measured configurations.** Compare reference geometry and joint frames. Evaluate specified motion samples and closure evidence. Publish per-consumer readiness and retained limitations. Output: Checked robot-assembly with link/joint coverage and reference/moved-state reports. Check: A visually coincident reference pose cannot pass reversed motion axis or missing closure.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent interprets link grouping and directs explicit mapping. |
| Software and agent | Software maps frames and traverses graph; agent reviews mechanical meaning. |
| Software handles ordinary cases | Demonstrated source-app joint classes map automatically; loops/unknown semantics enter review. |
| Deterministic supported case | Complete grouping/joints/frames yield reproducible robot-assembly. |

**Alternatives and quality targets.** Preserve source app assembly and explicit external joint records. Inspect community CAD_TO_URDF inference as a candidate with independent checks. Layout link geometry can retain unresolved joints; working robot requires consumer-supported relations.

**Proposed helpers.** DOM-08-A01: link mapper accepts occurrences/joints/measurements and emits link memberships plus unmapped references. DOM-08-A02: articulation adapter emits joint/geometry frame maps and supported/unsupported relation ledger. DOM-08-A03: robot-assembly checker reports per-link/joint residuals and format-specific prerequisites.

**Selection and merge.** Alternative rigid grouping and source-app mappings retain common occurrence IDs and pose controls. VLM checks mechanical correspondence; software reports graph/frame/motion residuals. Select coherent grouping and relations; preserve competing motion interpretations. New robot revision repeats link coverage, measured pose and loop/semantic checks.

**Migration and future cases.** Automate only source-app constraint classes demonstrated against rigid grouping, reversed axes, duplicate occurrences and closed-loop fixtures. CAD hierarchy differs from physical link grouping; retain correct grouping evidence. Wrong axis sign matches zero pose but fails a sourced moved configuration. Closed-loop source retains closure edge and blocks unsupported tree consumer.

## 6. DOM-14 — Calculate or import physical mass properties

**Inputs and dependencies.** Physical-measurement-set OR material-set plus cad-solid/B-rep/mesh/cad-assembly; target body map. Each tensor field supplies raw component ordering, matrix off-diagonal versus signed/unsigned product convention, reference point and axes. DOM-08 rigid grouping; actual geometry integration capability.

**Source entry points.** [MuJoCo overview](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [MuJoCo modeling guide](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [GProp_GProps Class Reference — Open CASCADE Technology Reference Manual 8.0.1](https://dev.opencascade.org/doc/refman/html/class_g_prop___g_props.html), [BRepGProp Class Reference — Open CASCADE Technology Reference Manual 8.0.1](https://occt3d.com/dev/doc/refman/html/class_b_rep_g_prop.html), [XML Reference — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/XMLreference.html), [urdf_model/link.hpp — ros/urdfdom_headers rolling branch](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/link.hpp). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-14-A01 — Select physical-property evidence per rigid body.** Resolve each quantity to a rigid body. Select measured or geometry-density branch. Check distribution, geometry validity and field completeness. Output: Per-body mass/COM/tensor field status and calculation eligibility. Check: Scalar mass supports only mass; visual material labels alone supply no density. Geometry-integration branch first checks finite closed solid(s), coherent orientation and absence of free boundaries; the volume integration API assumes these conditions.
2. **DOM-14-A02 — Calculate and transform sourced mass properties.** Validate solid prerequisites or supplied measurement field conventions; decode tensor ordering/sign/reference into a common matrix and convert units. For geometry, integrate no-density properties under recorded surface/triangulation/error settings and apply material density exactly once; preserve central tensor and absolute COM conventions. Shift any noncentral source tensor to COM with stated direction, rotate each central tensor into target axes, aggregate via parallel-axis terms at a common origin and shift the aggregate to its weighted COM. Output: Mass, COM and symmetric tensor with raw source values, method and transform receipt. Check: Compare mass/COM and tensor independently; use I_about_point = I_COM + m((d·d)Identity − d dᵀ) in one frame and I_rotated = R I Rᵀ; inverse shift subtracts that term.
3. **DOM-14-A03 — Check admissibility and consumer-specific completeness.** Run units/reference and tensor admissibility checks. Compare independent supplied measurements and analytic fixture expectations. Publish complete or partial fields for the named consumer. Output: Per-field checked mass-properties with source, reference, uncertainty and readiness. Check: Admissible tensor values alone establish numerical consistency; supplied physical accuracy has its own evidence.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent selects source meaning/distribution and directs calculations. |
| Software and agent | Software integrates/transforms; agent reviews applicability and partial evidence. |
| Software handles ordinary cases | Checked material/body classes calculate with exceptions for cavities, mixed density or incomplete measurements. |
| Deterministic supported case | Explicit valid geometry/distribution or complete measured fields produce repeatable properties. |

**Alternatives and quality targets.** Use independently measured/manufacturer mass, COM and tensor fields. Calculate supported closed-solid/mesh volume with sourced density distribution. Context bodies can retain partial properties; working dynamics requires consumer-required fields.

**Proposed helpers.** DOM-14-A01: property intake emits per-field provenance, reference point/axes and required calculation inputs. DOM-14-A02: physical-property adapter accepts measured fields or validated shapes/density plus raw component/sign/reference/unit metadata. It emits no-density geometric integrals, density application count, physical mass/COM/central tensor and frame/aggregation ledger. Length scaling uses volume L³, geometric inertia L⁵ and physical inertia mass×L²; mass/length/density units convert coherently. Reject an unknown source off-diagonal/product convention rather than copy field names. DOM-14-A03: validator emits field-level admissibility, physical-evidence comparison and consumer readiness.

**Selection and merge.** Measured, manufacturer and calculated candidates retain body revision, reference frame and source uncertainty. VLM reviews body/distribution evidence; software compares physically equivalent COM-frame tensors and measurements. Select source-backed fields with consistent reference; preserve conflicting mass/distribution claims. Recheck aggregate membership, units, tensor admissibility and downstream compiled/readback properties.

**Migration and future cases.** Demonstrate analytic solids, offset/rotated tensors, composite bodies, hollow geometry and partial measured fields before routine computation. Scalar mass record preserves mass and leaves COM/tensor consumers unresolved. Off-centre rotated tensor catches wrong parallel-axis sign and squared-length conversion. Duplicate assembly occurrence or overlapping volume cannot be counted twice without distribution evidence. Negative principal moment or triangle violation fails admissibility; static world geom is classified separately. A source products-of-inertia convention with opposite off-diagonal signs is explicitly decoded; copying raw names fails a rotated-tensor reference fixture. Unit-density GProp Mass is volume until applicable density is applied exactly once; millimetre geometry plus SI density catches L³/L⁵ conversion and double-density errors. Open or incoherently oriented shape fails preflight before VolumeProperties; integration error estimate cannot stand in for physical uncertainty.

## 7. DOM-12 — Export mesh assets for MuJoCo

**Inputs and dependencies.** One cad-solid/B-rep/visual-scene/robot-assembly route; occurrence selection and intended visual/collision role. Point03 native geometry; supported exporter and selected MuJoCo format/version discovery.

**Source entry points.** [MuJoCo overview](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [MuJoCo extensions](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst), [XML Reference — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/XMLreference.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-12-A01 — Select geometry occurrence and mesh role.** Resolve source route and selected occurrences. Assign asset role and target frame. Set source-backed approximation and format requirements. Output: Per-asset source-to-target frame, unit and approximation plan. Check: Assembly/scene input resolves actual geometry; camera-only/no-geometry objects retain explicit state.
2. **DOM-12-A02 — Export source-linked mesh assets.** Tessellate selected occurrences at declared settings. Apply recorded unit/frame conversion exactly once. Write separate assets and source/transform manifests. Output: Meshes with hashes, per-piece source maps and export receipt. Check: Movable body assets preserve distinct frames; serialization records actual supported encoding.
3. **DOM-12-A03 — Compare meshes to source and reopen.** Read saved mesh independently. Measure required source/mesh features and transforms. Publish role-specific asset readiness. Output: Mesh set with loader/readback, deviation and role-readiness reports. Check: Bounds alone cannot verify a bore or passage; collision and mass suitability have separate downstream checks.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent selects source/role and directs exporter. |
| Software and agent | Software tessellates and compares; agent reviews omitted features. |
| Software handles ordinary cases | Checked source/export families run; unsupported geometry/encoding enters review. |
| Deterministic supported case | Explicit occurrences/settings/frames and target loader produce repeatable mesh assets. |

**Alternatives and quality targets.** Use native simulator primitives for simple supported geometry. Reuse an existing mesh with source/frame/error evidence. Context display mesh uses its own detail criterion; working collision/mass uses separately qualified geometry.

**Proposed helpers.** DOM-12-A01: mesh planner emits source occurrences, target body frames and role-specific export settings. DOM-12-A02: mesh exporter accepts occurrence/frame/role settings and returns meshes plus approximation/loss ledger. DOM-12-A03: asset checker emits source-to-mesh residuals, frame/unit checks and parser outcomes.

**Selection and merge.** Coarse/display and detailed/interface meshes share source IDs and frame with different declared error targets. VLM reviews labelled source/output views; software reports per-feature deviation and parser results. Select per-role assets; preserve separate body frames and incompatible approximation candidates. Reopen selected package and repeat source mapping, frame and required-feature checks.

**Migration and future cases.** Automate tested source types/formats after scale, mirrored axes, missing faces and separate-link fixtures. Millimetre geometry exported without scale fails independent dimension check. Two moving links retain separate asset transforms. Bounds match but a bore is filled; feature comparison fails. Compiler mesh centering/principal-axis alignment changes raw coordinates but full transformed world surfaces match; omitting mesh transform fails.

## 8. DOM-13 — Generate convex collision set

**Inputs and dependencies.** Mesh, source/body IDs, local frame/scale and intended contact/passages criteria. DOM-12 asset records; CoACD repository and selected-version prerequisite inspection.

**Source entry points.** [CoACD licence](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE), [V-HACD licence](https://github.com/kmammou/v-hacd/blob/master/LICENSE), [MuJoCo overview](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [SarahWeiii/CoACD README and repository page](https://github.com/SarahWeiii/CoACD), [XML Reference — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/XMLreference.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-13-A01 — Define collision scope and contact features.** Partition source by body or static obstacle. Mark contact regions and passages. Select primitive, convex hull or decomposition candidate method. Output: Per-body collision plan with source mesh and protected regions. Check: A moving assembly cannot become one rigid collider; source licence pages do not establish algorithm API.
2. **DOM-13-A02 — Generate independently framed convex pieces.** Generate pieces per rigid body with explicit settings. Retain piece-local to body/world transforms. Record approximation changes and candidate lineage. Output: Convex pieces with original body ID, transforms, settings and source hashes. Check: Piece transforms and convexity/finite geometry checked; decomposition does not assign mass properties.
3. **DOM-13-A03 — Validate passages and intended contact behavior.** Compare protected source features and hull coverage. Evaluate named contact/non-contact fixtures in selected consumer when execution is scoped. Publish passed use classes and retained approximation limits. Output: Approximation report and checked collision-set. Check: Volume/bounds alone cannot pass passage/contact criteria; compile and runtime contact checks have distinct results.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent identifies contact features and directs approximation. |
| Software and agent | Software decomposes/measures; agent reviews contact meaning. |
| Software handles ordinary cases | Demonstrated shape classes run with exceptions for passages, open meshes or excessive hull counts. |
| Deterministic supported case | Explicit body meshes/settings/contact criteria yield deterministic supported candidates and reports. |

**Alternatives and quality targets.** Primitives for measured simple contact shapes. Single convex hull for declared coarse envelope use. CoACD convex pieces for required concavity; detailed contact checks distinguish working robot from layout.

**Proposed helpers.** DOM-13-A01: collision intake partitions by rigid body and emits protected-feature/criteria records. DOM-13-A02: decomposition adapter accepts mesh/frame/settings and emits individually addressable pieces plus errors/loss map. DOM-13-A03: collision verifier reports per-feature envelope, penetration/clearance and contact outcomes.

**Selection and merge.** Primitive/single-hull/decomposed candidates share mesh/body/frame and protected-feature evidence. VLM compares contact-feature association; software reports directional geometry and named contact checks. Choose per-body collider set; combine compatible pieces without crossing rigid-body boundaries. New collision revision repeats body/frame, passage and consumer contact checks.

**Migration and future cases.** Automate only shape/contact classes demonstrated on concavity, units, independent links, openings and error-control cases. A convex hull fills a required passage and fails its clearance fixture. Two moving links decomposed together fail body ownership checks. Threshold changes yield similar volume but different contact; feature/contact criteria select the supported candidate. Normalized threshold mistaken for metre error fails settings validation; real-metric mode requires metre input and independent feature-error checks. Hull-count limit with merge can exceed requested threshold; measured passage/envelope criteria still govern.

## 9. DOM-09 — Robot assembly to URDF package

**Inputs and dependencies.** Robot-assembly, joint-set, mass-properties AND one visual-scene OR collision-set adjunct; assets and target consumer. DOM-08, DOM-12/13/14; selected urdfdom/consumer version.

**Source entry points.** [ROS URDF tutorial](https://github.com/ros/urdf_tutorial), [URDF consumer reference](https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html), [Assembly4 URDF exporter](https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF), [urdf_model/joint.hpp — ros/urdfdom_headers rolling branch](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/joint.hpp), [urdf_model/link.hpp — ros/urdfdom_headers rolling branch](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/link.hpp), [REP-103: Standard Units of Measure and Coordinate Conventions — ros-infrastructure/rep master](https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-09-A01 — Check literal package inputs and supported URDF tree.** Verify all common inputs plus stated adjunct. Map joint types and frames to supported tree representation. Check required geometry/physics roles and asset paths. Output: Link/joint/asset/inertia mapping and consumer-specific missing-role report. Check: Visual adjunct cannot silently become collision data; fixed/continuous joints receive type-specific range rules.
2. **DOM-09-A02 — Serialize links joints and distinct asset origins.** Write links/joints with source-derived frame/type/range data. Write visual, collision and inertial origins separately. Package referenced meshes and source/units/loss records. Output: URDF plus mesh files, link-to-source map and serialization/loss receipt. Check: Do not copy unsigned CAD products into tensor entries; tree export preserves all supported relation meaning.
3. **DOM-09-A03 — Parse reopen and compare robot poses and physics.** Parse saved URDF and resolve meshes. Compare named reference/moved states and properties. Load intended consumer and publish per-role results. Output: Parser/consumer receipt and source-to-target pose/physics/asset report. Check: Successful parsing cannot pass wrong axis, missing consumer-required visual/collision role or incorrect inertia. Absent roles remain explicit; a visualization consumer may accept its declared visual-only package.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent maps source roles and directs package authoring. |
| Software and agent | Software serializes/parses/checks; agent reviews motion and field meaning. |
| Software handles ordinary cases | Checked tree/asset classes export automatically; loops/unsupported types enter review. |
| Deterministic supported case | Complete supported graph, roles and properties yield reproducible package. |

**Alternatives and quality targets.** URDF for a specified ROS consumer. Direct MJCF for explicitly richer closures/contact scope. Layout visual URDF and working dynamics package have different required roles; literal adjunct input remains recorded.

**Proposed helpers.** DOM-09-A01: URDF preflight emits literal-input receipt, supported tree and per-role readiness. DOM-09-A02: package writer accepts checked graph/role/tensor records and emits URDF, meshes and mapped omission list. DOM-09-A03: package verifier emits type/asset/tree, kinematic and property equivalence results.

**Selection and merge.** Consumer-specific packages share graph/property/source hashes and declare detail/role requirements. VLM checks source/link correspondence; software compares saved poses, fields and assets. Select a consistent complete mapping; preserve incompatible loop/extension alternatives. Reparse and reload new package; repeat pose, property and role checks.

**Migration and future cases.** Demonstrate supported joint types, moved poses, asset units, tensor conventions and consumer load before routine export. Continuous joint receives no invented finite travel limits. Closed loop cannot silently lose closure in tree export. Visual/collision origins differ and remain separately placed. Mass in grams or inertia in kg·mm² fails SI conversion fixture. The same visual-only package passes a visualization consumer's declared role checks and fails a consumer requiring collision geometry; visual geometry is never promoted automatically.

## 10. DOM-10 — URDF import and MJCF conversion

**Inputs and dependencies.** URDF and mesh inputs, source mapping, selected MuJoCo version/compiler settings. DOM-09 package; documented MuJoCo decoder/compiler APIs for selected version.

**Source entry points.** [MuJoCo modeling guide](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [MuJoCo overview](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [MuJoCo model-editing source](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst), [XML Reference — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/XMLreference.html), [Model Editing — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html), [Python — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/python.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-10-A01 — Inventory URDF import policy and expected losses.** Read source graph/assets and extension fields. Record effective compiler flags including importer defaults. Define identity and property checks across any body fusion. Output: Import contract with expected body/geom/joint/property mappings and defaults. Check: Changed counts need explicit mapping; source unsupported fields remain visible.
2. **DOM-10-A02 — Parse compile and serialize editable MJCF.** Parse source into editable specification using recorded flags. Compile and retain errors/defaulted values. Serialize specification to editable MJCF and retain asset dependencies. Output: Editable MJCF XML and assets, compiled receipt and field/default/loss map. Check: Generated XML expands/applies defaults; source text identity and original hierarchy remain in source/mapping ledger. Save report identifies expanded/omitted include/replicate/attach/flexcomp/actuator shortcut constructs and comments, plus attached compiler-setting conflicts.
3. **DOM-10-A03 — Reopen MJCF and compare supported semantics.** Recompile actual saved MJCF. Compare mapped states/properties including fused bodies. Publish conversion outcomes and required authoring dependencies. Output: Recompile/readback report with joint, geometry, inertia and identity comparison. Check: Compile success cannot replace editable output, source equivalence or physical data.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent reviews import losses and directs conversion. |
| Software and agent | Software parses/compiles/saves; agent resolves unsupported semantics. |
| Software handles ordinary cases | Checked URDF subsets convert with explicit exception reports. |
| Deterministic supported case | Pinned supported subset/settings produces reproducible generated MJCF. |

**Alternatives and quality targets.** Direct DOM-11 MJCF authoring from full source records. Preserve URDF with versioned MJCF extension/derivative. Context visual conversion and working simulation require different retained role/physics checks.

**Proposed helpers.** DOM-10-A01: conversion preflight emits effective compiler options and field/default/loss expectations. DOM-10-A02: converter emits source/spec/compiled/saved stage receipts and generated flattened XML with mapping. DOM-10-A03: conversion verifier emits per-field equivalence, fusion mapping and consumer readiness.

**Selection and merge.** Importer-policy candidates share original package and intended consumer; fusion/visual choices declared. VLM reviews link/field identity with source views; software compares mapped configurations/properties. Select one coherent settings/representation branch; preserve unsupported source semantics in mapping. Reopen saved selected MJCF and repeat mapped pose/property/asset checks.

**Migration and future cases.** Demonstrate import defaults, fixed-body fusion, unsupported extensions, XML serialization and reopen fixtures before automation. Default discarded visual geometry appears explicitly in loss map. Fixed-body fusion changes count but mapped poses/mass remain checked. Compiled model with failed XML save leaves MJCF output incomplete. Unsupported actuator/contact intent enters authoring dependency rather than silent invention. savecompiled true versus false preserves distinct authored/canonical value receipts and successful reopened MJCF; original include/comment text remains in source.

## 11. DOM-11 — Author native MJCF simulation model

**Inputs and dependencies.** Robot-assembly, joint-set, collision-set, mass-properties, material-set and intended simulation scope. DOM-08/13/14 and pinned MJCF XML reference.

**Source entry points.** [MuJoCo modeling guide](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [MuJoCo overview](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [MuJoCo model-editing source](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst), [XML Reference — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/XMLreference.html), [Model Editing — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html), [Python — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/python.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-11-A01 — Bind native model roles and compiler policy.** Bind every source link and geom role. Record units, compiler angle/inertia options and closure requirements. Check sourced physics/contact/actuation fields. Output: Body/joint/geom/inertial mapping and explicit compiler/unit/closure policy. Check: Required physical fields have evidence; visual/collision replacements cannot silently alter inferred mass.
2. **DOM-11-A02 — Author body tree geoms and explicit closure constraints.** Create tree bodies and source-linked geometry roles. Assign joints and inertials with exact frame/tensor conventions. Add sourced closure/contact/actuation declarations and retain defaults. Output: Editable MJCF/spec source with source-to-body/joint/geom map. Check: Body tree alone does not close a loop; soft equality behavior and constrained freedoms require their own criterion.
3. **DOM-11-A03 — Compile read back and check model meaning.** Compile saved source and inspect effective values. Compare source frames, roles and physical records. Check specified closure/contact conditions and publish use readiness. Output: Compile/readback, pose/property and closure/contact reports. Check: Valid compile is distinct from matched physical model; equality residual/force behavior uses sourced criteria. Any compiler-adjusted inertia is a changed model value with explicit provenance; it cannot satisfy a source-property criterion merely by becoming numerically admissible.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent authors semantics and directs compiler/checks. |
| Software and agent | Software creates/checks XML; agent interprets contact/closure/physics choices. |
| Software handles ordinary cases | Demonstrated model families author with exceptions for new closures or physical roles. |
| Deterministic supported case | Complete supported mapping/settings/criteria generate and check native MJCF. |

**Alternatives and quality targets.** DOM-10 URDF conversion followed by explicit MJCF additions. Reuse a per-item licensed pinned model under DOM-32. Layout/kinematic model and working dynamic model retain different property/contact readiness.

**Proposed helpers.** DOM-11-A01: MJCF intake emits complete role/physical/source map and required model decisions. DOM-11-A02: MJCF author maps graph/roles/properties into editable source with explicit inferred/declared field ledger. DOM-11-A03: model verifier reports effective defaults, kinematics, inertials and named fixture outcomes.

**Selection and merge.** Native and imported/pinned candidates share source requirements and target tests but retain different defaults/losses. VLM compares source/body/role semantics; numerical checks inspect compiled poses, inertia and constraints. Select coherent source-linked fields and compatible assets; any combined source is a new model revision. Recompile/reopen and repeat pose, role, physical, closure and contact checks.

**Migration and future cases.** Automate only demonstrated graph/geom/physical/constraint classes after compiler-default, frame, inertia and closure fixtures. inertiafromgeom=true changes explicit inertial intent and is detected in compiled readback. A loop represented by a weld with wrong constrained freedoms fails its sourced motion fixture. Changing only visual geom cannot alter intended collision or mass behavior without an explicit recorded effect.

## 12. DOM-32 — Map CAD link geometry to MJCF body tree

**Inputs and dependencies.** MJCF, CAD assembly, joint-set, measurement-set and component-record; per-asset rights and body map. Pinned model/source terms; DOM-08/12/14 evidence and selected compiler.

**Source entry points.** [MuJoCo modeling guide](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [MuJoCo overview](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [XML Reference — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/XMLreference.html), [Model Editing — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-32-A01 — Pin seed model and map CAD occurrences to bodies.** Pin existing model and its complete assets. Map CAD occurrences to named bodies and required frames. Record preserved graph/actuator/sensor declarations and mass-inference dependencies. Output: Seed topology/actuator/sensor/physics snapshot and CAD-to-body mapping. Check: DOM-32 preserves existing topology; seed mismatch cannot silently route to a rebuilt model.
2. **DOM-32-A02 — Replace mapped role-specific geometry.** Write new geometry assets in mapped body frames. Patch only authorized geom/asset declarations. Record effective mass/contact consequences and source lineage. Output: New XML/assets with geom-to-source and transform map; explicit physics-effect report. Check: Automatic inertia recomputation cannot silently change preserved physical intent; collider replacement receives contact checks.
3. **DOM-32-A03 — Compare preserved semantics and effective geometry.** Recompile saved candidate. Compare seed invariants and effective placed geometry at named configurations. Publish mapping and independent semantic/metric findings. Output: Source-to-result graph/actuator/sensor/physics diff and effective placed-geometry report. Check: Raw mesh vertices or geom_pos alone cannot substitute full compiled mesh→geom→body transform comparison.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent interprets seed/CAD correspondence and directs replacement. |
| Software and agent | Software patches/compiles/diffs; agent reviews role and physics effects. |
| Software handles ordinary cases | Demonstrated seed/body/asset families update with exceptions for changed topology or inference. |
| Deterministic supported case | Complete compatible body map and explicit role/settings yield checked replacement. |

**Alternatives and quality targets.** Replace visual geometry while retaining sourced collisions/physics. Replace collision representation with separate approximation/contact checks. Rebuild incompatible robot through DOM-11 as a separately scoped alternative; layout versus working dynamics criteria remain explicit.

**Proposed helpers.** DOM-32-A01: seed mapper emits body/occurrence correspondence, invariants and affected physics dependencies. DOM-32-A02: geometry patcher accepts body/role/asset transforms and emits changed fields plus preservation diff. DOM-32-A03: replacement verifier emits preserved-field diff, world-geometry residuals and affected contact results.

**Selection and merge.** Replacement candidates share immutable seed and CAD revisions; roles/detail and permitted physical effects declared. VLM compares source body/configuration evidence; software reports invariants, placed geometry and properties. Select compatible body-specific replacements preserving whole seed invariants. Compile/reopen combined revision and recheck graph, actuators/sensors, inertials, frames and affected contacts.

**Migration and future cases.** Automate known seed/body mappings after geometry-centering, inference, topology-preservation and asset-revision fixtures. Visual replacement unexpectedly changes inferred body inertia; diff fails preservation. Compiler recentres mesh but effective world geometry matches; comparison uses full transform chain. Wrong CAD configuration matches bounds but fails critical mounting interface.

## 13. DOM-15 — Author semantic IFC building

**Inputs and dependencies.** Model-brief with source dimensions, element classes/properties, spatial hierarchy, frames and representation requirements. Point01 brief; IfcOpenShell/Bonsai capability for selected schema.

**Source entry points.** [Geometry creation — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html), [IFC profile representation API](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html), [IFC geometry authoring APIs](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html), [Geometry processing — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [ifcopenshell.api.geometry.add_representation — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_representation/index.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-15-A01 — Resolve building schema units hierarchy and element evidence.** Read target schema and brief element requirements. Record explicit units, contexts and local/site frames. Map spatial hierarchy, properties and representation choices. Output: IFC schema/context/unit/spatial plan and source-element mapping. Check: Shape appearance cannot supply semantic class or hidden dimensions; CRS values require source survey evidence.
2. **DOM-15-A02 — Author IFC elements placements and relationships.** Create project units, contexts and spatial hierarchy. Create source-linked elements and place their representations. Add required containment, properties, material and void/filling relationships. Output: IFC project/elements with GlobalId/source map, geometry and semantic relationships. Check: Geometric hole and semantic opening are separate records; avoid duplicate transform/unit application.
3. **DOM-15-A03 — Validate semantic graph and evaluated geometry.** Reopen saved IFC and validate entities/relationships. Evaluate geometry and compare dimensions, placements and openings. Publish use-specific semantic and geometric readiness. Output: Schema/IDS when supplied, semantic graph and geometry readback reports. Check: Valid schema and plausible rendering cannot substitute required property or opening-host evidence.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent interprets brief and authors semantics. |
| Software and agent | Software creates/validates entities; agent resolves class/property meaning. |
| Software handles ordinary cases | Checked building element families author with exceptions for unsupported schema or missing dimensions. |
| Deterministic supported case | Complete semantic/geometry records and supported schema produce reproducible IFC. |

**Alternatives and quality targets.** Bonsai UI authoring with explicit source maps. Scripted IfcOpenShell API authoring proposal. Context building geometry and working semantic delivery retain different property/detail requirements.

**Proposed helpers.** DOM-15-A01: semantic intake emits required element/property/relationship records and per-element readiness. DOM-15-A02: IFC author emits element/representation/relationship identities plus source/placement ledger. DOM-15-A03: IFC verifier emits per-element semantic, geometry and delivery-requirement results.

**Selection and merge.** Element/representation alternatives share brief/source IDs and target schema while declaring geometry/detail/delivery criteria. VLM checks plan/source-to-element meaning; software reports schema, placements, dimensions and relationships. Combine compatible elements with stable IDs; conflicts retain alternative semantic/geometry records. Validate new file's GlobalIds, hierarchy, relationships, geometry and source requirements independently.

**Migration and future cases.** Automate demonstrated schema/element/property classes after hierarchy, opening, units, IDs and incomplete-brief fixtures. Rotated wall/opening maintains host relationship and world-space void geometry. Duplicate GlobalId fails identity check. A geometric hole without required IfcOpeningElement/void relation fails semantic requirement. Missing height in brief blocks dependent solid without invented default.

## 14. DOM-35 — Place library component in semantic IFC

**Inputs and dependencies.** IFC, component-record and measurement-set; target class/type/storey/host and placement evidence. Point02 library intake; selected IFC representation adapter.

**Source entry points.** [Geometry creation — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html), [FreeCAD add-on catalogue](https://www.freecad.org/addons.php?lang=eng_EN), [ifcopenshell.api.geometry.add_representation — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_representation/index.html), [Geometry processing — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-35-A01 — Bind library asset and target IFC placement meaning.** Pin component and target IFC revisions. Resolve source-to-target measurement/frame mapping. Identify class/type/occurrence and supported geometry representation. Output: Asset-to-IFC representation/semantic plan with rights/source map. Check: Original inputs do not guarantee target semantics; record linked dependency rather than invent class.
2. **DOM-35-A02 — Create placed semantic occurrence with source mapping.** Create distinct semantic occurrence and representation. Apply source-to-project placement once. Assign required spatial/host/property relations and preserve source terms. Output: New occurrence/entity, source mapping, representation and spatial/host relations; existing identities retained. Check: Repeated instances have distinct occurrence identity; source definition and existing IFC IDs stay traceable.
3. **DOM-35-A03 — Check new occurrence and preserved IFC relationships.** Reopen/validate candidate IFC. Compare inserted interfaces and semantic relations. Publish source/occurrence map and preserved-context diff. Output: Validation/readback, placement/interface and identity/relationship diff. Check: Visual placement cannot pass wrong class/host; library geometry does not certify product specifications.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent interprets asset/target meaning and directs insertion. |
| Software and agent | Software imports/places/validates; agent reviews class/host correspondence. |
| Software handles ordinary cases | Checked library-format/class families insert with semantic/adapter exceptions. |
| Deterministic supported case | Complete asset/representation/class/frame inputs produce reproducible occurrence. |

**Alternatives and quality targets.** Native IFC library representation with explicit type/occurrence reuse. Supported Blender/geometry adapter for source asset with separate product/relationship authoring. Context furniture display and working building element require different semantic/interface evidence.

**Proposed helpers.** DOM-35-A01: component-to-IFC planner emits source/target identities, required semantics and representation capability. DOM-35-A02: library inserter emits new entity/representation/relation IDs and source/placement ledger. DOM-35-A03: insertion verifier emits source identity, occurrence geometry and preserved-context checks.

**Selection and merge.** Library/placement candidates share target IFC revision and source asset/configuration; detail/class targets explicit. VLM compares item/host evidence; software checks interfaces, IDs and relationships. Select compatible instances with distinct occurrence IDs and source mappings. Validate new IFC and repeat placement, classification, host and preserved-context checks.

**Migration and future cases.** Automate only demonstrated asset/class/representation types after duplicates, units, host, rights and source revision fixtures. Two placements of one asset preserve two IFC occurrence identities. add_representation returns geometry but missing product/containment keeps insertion partial. Library source configuration differs from required interface and fails measurement comparison.

## 15. DOM-16 — Extract IFC geometry as triangles

**Inputs and dependencies.** IFC source, selected elements, target use and geometry settings. IfcOpenShell selected build/settings; point05 coordinate chain.

**Source entry points.** [Geometry processing — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [ifcopenshell.geom — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html), [Usage — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcconvert/usage.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-16-A01 — Select IFC elements and triangle extraction policy.** Inventory selected representations and identities. Record opening evaluation and local/world output policy. Set triangle detail/error requirements. Output: Element/representation inventory, units/placement/opening policy and mesh criteria. Check: DOM-16 output is mesh; DOM-27 owns B-rep route despite original broad capability prose.
2. **DOM-16-A02 — Extract triangles with source and transform mapping.** Evaluate selected element geometry including chosen openings. Extract triangles and available identity/material mapping. Write derivative with explicit unit/frame and source manifest. Output: Vertices/faces and available material/item IDs, element map and placement/settings receipt. Check: Element geometry must not be double-transformed; generated IDs retain their namespace and source relation.
3. **DOM-16-A03 — Check element coverage placements and openings.** Compare required element coverage. Measure saved world geometry and protected openings. Publish mesh and mapping with source IFC retained. Output: Coverage/loss map, frame/bounds/interface/opening checks and readback report. Check: Triangle extraction does not carry complete IFC relationships; source/sidecar identity stays explicit.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent selects representations and reviews output meaning. |
| Software and agent | Software extracts/measures; agent reviews omissions and identity. |
| Software handles ordinary cases | Checked schema/representation classes extract with exceptions. |
| Deterministic supported case | Explicit selection/settings/frame policy produces deterministic mesh derivative. |

**Alternatives and quality targets.** Selected-element create_shape for bounded work. Iterator bulk extraction for required coverage. DOM-27 B-rep branch for kernel shape consumers; layout triangles and contact meshes keep different criteria.

**Proposed helpers.** DOM-16-A01: extraction planner emits element IDs, settings and expected output frame/unit contract. DOM-16-A02: triangle adapter emits per-element meshes, identity/material map and baked-versus-external transform flag. DOM-16-A03: extraction verifier reports element-level geometry/identity results and eligible downstream roles.

**Selection and merge.** Detail/kernel/settings candidates share IFC source and element IDs with named output frames. VLM compares full element context and opening identity; software compares dimensions/coverage. Select per-element supported output at common frame; preserve representation exceptions. Recheck identity coverage, transforms, dimensions and openings in new mesh package.

**Migration and future cases.** Demonstrate local/world placements, unit conversion, openings, absent geometry and element mapping before automation. World-coordinate output plus repeated placement fails double-transform fixture. Millimetre project and metre output retain one explicit conversion. Missing representation produces a named coverage exception. Opening subtraction setting change triggers protected-passage failure.

## 16. DOM-27 — Extract IFC geometry as OpenCASCADE B-rep

**Inputs and dependencies.** IFC source, element selection, required shape class and kernel/settings. IfcOpenShell geometry settings and selected OpenCASCADE/PythonOCC dependencies.

**Source entry points.** [Geometry processing — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [ifcopenshell.geom — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-27-A01 — Resolve IFC kernel shape extraction requirements.** Inspect representations and target use. Select supported non-triangulated kernel route. Record units, opening evaluation and placement policy. Output: Element-to-kernel plan with source schema/units/placements and dependencies. Check: B-rep may remain faceted; extraction cannot restore missing source analytic intent.
2. **DOM-27-A02 — Extract and retain native kernel shapes.** Evaluate selected shapes under recorded opening/settings policy. Record actual shape/face types and transforms. Retain serialized shape derivative and source manifest. Output: Kernel B-reps with per-element source/placement map and type/face metadata. Check: A triangle payload cannot be labelled B-rep; validity and analytic-face claims query actual output.
3. **DOM-27-A03 — Validate shape class and source feature agreement.** Reopen retained kernel shapes. Check class/validity and required interfaces/openings. Publish actual representation and source mapping. Output: Validity, topology/face-type, dimensional/placement and identity reports. Check: Valid shell differs from closed solid; equal bounds/volume cannot substitute interface checks.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent selects representation/backend and interprets exceptions. |
| Software and agent | Software extracts/queries shapes; agent reviews source meaning. |
| Software handles ordinary cases | Demonstrated IFC geometry classes run with explicit failures. |
| Deterministic supported case | Supported representation/settings/backend yields typed B-rep derivative. |

**Alternatives and quality targets.** DOM-16 triangles for display/collision consumers. Preserve source IFC for semantics while retaining B-rep for geometry queries. Faceted context B-rep versus analytic working shape has explicit per-face requirements.

**Proposed helpers.** DOM-27-A01: B-rep preflight emits supported shape classes and explicit backend/import dependencies. DOM-27-A02: B-rep adapter emits typed shapes, source maps and evaluation/healing settings. DOM-27-A03: shape verifier emits per-element class, metric, source and downstream-readiness records.

**Selection and merge.** Kernel/representation candidates share element/source/frame and required face/shape class. VLM reviews source/element associations; software checks actual face types, validity and dimensions. Select compatible per-element shapes without claiming restored source history. Reopen/check aggregate mappings, placements, openings and required shape classes.

**Migration and future cases.** Demonstrate faceted IFC, analytic surfaces, shells, unsupported entities and placement/opening cases. Faceted IFC becomes planar-face B-rep and retains that classification. Open shell cannot pass a required closed-solid handoff. PythonOCC dependency or return-type mismatch produces explicit adapter failure.

## 17. DOM-17 — IFC to GLB display scene

**Inputs and dependencies.** IFC, selected elements/materials, target display frame and identity requirements. IfcOpenShell/IfcConvert GLB source capability; optional Blender chain is separate adapter.

**Source entry points.** [IfcOpenShell introduction](https://docs.ifcopenshell.org/introduction.html), [Blender interchange formats](https://www.blender.org/features/pipeline/), [Geometry processing — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [Usage — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcconvert/usage.html), [blender_gltf.py — Blender glTF importer source, main branch](https://github.com/blender/blender/blob/main/scripts/addons_core/io_scene_gltf2/blender/imp/blender_gltf.py). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-17-A01 — Define IFC-to-display identity and unit policy.** Read source identities and target frame. Choose supported conversion chain/settings. Specify node/sidecar mapping and detail criteria. Output: Source-to-node/property mapping plan and unit/axis policy. Check: Generated fixture IDs are recorded as converted IDs; geometric holes do not imply opening relationships.
2. **DOM-17-A02 — Write GLB and semantic sidecar.** Convert through the selected CLI or Python serializer with branch-specific unit/frame settings. Obtain actual element-to-node/primitive/occurrence mapping through the serializer GUID policy or independently checked CLI sidecar; preserve one-to-many and shared-mesh occurrences. Write GLB and matching sidecar/loss record; required identity remains partial when mapping cannot be established. Output: GLB, asset/output hashes and element-node/property sidecar. Check: Geometry placement and identity map correspond to same source; IFC relationships remain source records.
3. **DOM-17-A03 — Reopen scene and compare identity coverage.** Open saved GLB and sidecar. Compare required nodes and world geometry to source. Publish display use with retained IFC reference. Output: Readback identity, orientation, dimensions and mapping report. Check: Plausible rendering cannot substitute correct node identity or source semantic preservation.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent chooses display semantics and directs conversion. |
| Software and agent | Software converts/reopens; agent reviews mapping/appearance. |
| Software handles ordinary cases | Checked IFC/GLB settings run with identity/geometry exceptions. |
| Deterministic supported case | Explicit selection, supported converter and mapping policy produce reproducible visual scene. |

**Alternatives and quality targets.** IFC-native viewer for semantic relationships. Direct IfcConvert GLB or separately evidenced Blender chain. Context display can simplify surfaces; working selection/measurement interface needs stable IDs and required geometry criteria.

**Proposed helpers.** DOM-17-A01: scene planner emits element selection, node identity policy and preserved/lost field map. DOM-17-A02: GLB writer emits scene plus ID/property/loss map; preserves original IFC independently. DOM-17-A03: scene verifier reports coverage, frame/units and visual/source correspondence.

**Selection and merge.** Display detail/material candidates share IFC revision and element mapping; branch goals differ explicitly. VLM checks source-to-node correspondence using labelled views; software checks transforms and coverage. Select compatible per-element display assets at one unit/frame policy. Reopen final GLB/sidecar and repeat identity, source geometry and viewer checks.

**Migration and future cases.** Demonstrate ID namespaces, absent geometry, local/world conversion, repeated instances and reader behavior before routine export. Converted source-part IDs are retained without relabelling as original GlobalIds. Rotated millimetre IFC exports/reopens with correct metre-scale orientation. GLB exists but sidecar points at older IFC revision: package readiness fails. Renamed, reordered or missing GLB nodes invalidate guessed index/name matching; required identity needs actual element→node/primitive/occurrence evidence, including shared meshes.

## 18. DOM-24 — Assemble and inspect Blender scene

**Inputs and dependencies.** One cad-solid/mesh/IFC/robot-assembly/camera-solution route, source assets and requested composition. Blender import/scene API; OCS remains engineering source; domain geometry adapters as needed.

**Source entry points.** [Blender interchange formats](https://www.blender.org/features/pipeline/), [Blender MCP source](https://projects.blender.org/lab/blender_mcp/src/branch/main), [Blender Python usage notes](https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst), [Registered Blender workflow article](https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0), [blender_gltf.py — Blender glTF importer source, main branch](https://github.com/blender/blender/blob/main/scripts/addons_core/io_scene_gltf2/blender/imp/blender_gltf.py). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-24-A01 — Resolve scene input branch and actual adapter.** Identify exact input route and source assets. Select supported adapter with recorded version. Define scene unit/axis, object and camera mappings. Output: Adapter/role/source map with unit, frame and camera conventions. Check: Camera-solution alone validly yields camera-only scene; geometry is required only for dependent checks.
2. **DOM-24-A02 — Compose source-linked scene objects and cameras.** Import or create only required objects/cameras. Apply explicit transforms/units and retain source association. Save candidate scene and resolved asset links. Output: Scene with object/source IDs, linked assets, transforms and domain-sidecar references. Check: Scene hierarchy does not replace IFC relationships or robot physical semantics; maps link to those sources.
3. **DOM-24-A03 — Reopen and inspect scene content numerically and visually.** Reopen saved artifact and resolve assets. Check applicable object/camera transforms and content. Review source-linked representative views and publish results. Output: Readback object/camera/asset, transform and representative-view report. Check: Camera-only branch can pass; absent geometry-dependent checks are inapplicable rather than failed.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent interprets source/composition and directs scene operations. |
| Software and agent | Software imports/queries; agent reviews appearance and source association. |
| Software handles ordinary cases | Checked import classes run with adapter/asset exceptions. |
| Deterministic supported case | Complete supported scene/camera inputs and transforms produce reproducible scene. |

**Alternatives and quality targets.** Direct Blender background/scripted adapter proposal. Version-compatible interactive bridge for iterative source inspection. Camera-only scene is valid; layout view and working geometry inspection use different content criteria.

**Proposed helpers.** DOM-24-A01: scene intake emits selected variant, object/camera map and importer prerequisites. DOM-24-A02: scene composer accepts typed imports/transforms/cameras and emits scene plus source/loss manifest. DOM-24-A03: scene verifier emits role-specific checks and source/derivative coverage.

**Selection and merge.** Scene/camera alternatives share source revisions and intended view while declaring detail/render targets. VLM compares labelled source/scene views with numerical transform receipts. Combine compatible scene objects/cameras retaining IDs and source roles. Reopen merged scene and repeat object/camera/asset, transform and source-view checks.

**Migration and future cases.** Automate supported import/camera classes after axis, scale, asset, camera-only and version mismatch fixtures. Camera-only input produces checked camera scene without fabricated geometry. glTF Y-up/metre import with non-unit scene scale preserves world dimensions. Scene references stale source ID despite matching appearance; coverage check fails.

## 19. DOM-34 — Author static MuJoCo environment from BIM mesh

**Inputs and dependencies.** Mesh and collision-set with IFC source/element mapping, units and frame lineage. DOM-16/17 source maps, DOM-13 colliders and point05 frame evidence.

**Source entry points.** [MuJoCo modeling guide](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [MuJoCo overview](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [XML Reference — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/XMLreference.html), [Geometry processing — IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-34-A01 — Bind BIM-derived mesh and collider identities.** Resolve both required inputs to same building source. Record exact element identifiers and transformation chain. Define static geometry and protected contact features. Output: Element-to-mesh-to-piece map and simulation-world placement/coverage plan. Check: BIM lineage is required for this operation's stated provenance; generic mesh can use a separately declared generic environment route.
2. **DOM-34-A02 — Author static world geoms and source sidecar.** Create explicit world/unit/compiler context. Attach static visual and collision assets. Write source/element mapping and retained semantic-source references. Output: MJCF world geoms plus IFC-element/asset sidecar and loss map. Check: Environment output creates no robot or invented inertial body requirements; IFC semantics stay source-linked.
3. **DOM-34-A03 — Validate static coverage and working passages.** Read compiled static scene. Compare building controls, IDs and required openings. Evaluate named fixtures and publish use-specific results. Output: Compile/readback, coverage/placement and contact approximation results. Check: A geometric passage check and IFC opening relationship check remain distinct; static scene carries only declared derivative semantics.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent maps building elements/world intent and directs authoring. |
| Software and agent | Software writes/checks static scene; agent reviews coverage/contact meaning. |
| Software handles ordinary cases | Checked BIM extraction/collider classes run with source/placement exceptions. |
| Deterministic supported case | Complete mesh/collider/map/frame contract produces reproducible static environment. |

**Alternatives and quality targets.** Analytic primitives for sourced building contact surfaces. Convex parts for complex source-derived obstacles. Layout building scene and working contact scene retain separate passage/geometry requirements.

**Proposed helpers.** DOM-34-A01: BIM-environment intake emits static role/coverage and source-frame contract. DOM-34-A02: static-world writer emits XML/assets with source-element and approximation mapping. DOM-34-A03: verifier emits per-element geometry/identity and per-contact readiness.

**Selection and merge.** Static representations share IFC revision, element IDs and world controls with different detail/contact targets. VLM checks element/source context; software measures coverage, placements and fixtures. Select per-element compatible geometry/colliders without merging semantic identities. New environment revision repeats source mapping, world geometry and contact checks.

**Migration and future cases.** Automate demonstrated building geometry classes after ID, openings, unit, local/world and contact fixtures. IFC metadata absent from mesh prevents BIM provenance claim while retaining geometry evidence. Storey placement applied twice fails source-to-world controls. Coarse hull fills doorway and fails working-passage criterion.

## 20. DOM-33 — Add environment collision geometry to MJCF

**Inputs and dependencies.** Existing MJCF, environment mesh and collision-set with registration/source map. Point05 registration; DOM-13 colliders and seed compiler.

**Source entry points.** [MuJoCo overview](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [MuJoCo modeling guide](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [XML Reference — MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/XMLreference.html). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-33-A01 — Bind environment to existing robot world frame.** Pin seed and environment sources. Resolve source-to-world transform once. Define static roles and required contact/passages. Output: Seed robot invariants and environment-to-world transform/contact plan. Check: Mesh and collider source frames must agree; scene appearance alone cannot establish registration.
2. **DOM-33-A02 — Add static geoms with separate visual and collision roles.** Insert source-linked static environment geoms. Assign visual/contact roles and explicit filtering. Save new scene with original robot declarations retained. Output: Revised MJCF with static geom/source map and seed-preservation diff. Check: Adding static obstacles does not invent dynamic-body mass or robot joints.
3. **DOM-33-A03 — Check robot preservation and obstacle contacts.** Compare seed robot after saved-scene compile. Measure obstacle placement/passages and effective collision geometry. Check declared fixtures and publish use readiness. Output: Compile/readback, seed invariant and environment/contact reports. Check: Compile and aggregate bounds cannot pass blocked required opening or wrong collision filter.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent identifies obstacle/source meaning and directs insertion. |
| Software and agent | Software composes/checks; agent interprets passage/contact intent. |
| Software handles ordinary cases | Checked registered environment classes run with frame/contact exceptions. |
| Deterministic supported case | Explicit static assets/transforms/filter policy produce repeatable scene addition. |

**Alternatives and quality targets.** Analytic primitives for measured simple obstacles. Convex pieces for required concave passages. Context visual environment versus working contact environment retains separate required checks.

**Proposed helpers.** DOM-33-A01: environment intake emits frame/contact dependencies and seed preservation snapshot. DOM-33-A02: static-geom composer emits new XML/assets and per-piece world placement/role ledger. DOM-33-A03: environment verifier reports seed invariants, frame/coverage and per-fixture outcomes.

**Selection and merge.** Environment collider/detail candidates share seed robot/world controls and contact feature IDs. VLM reviews source obstacle/passage association; software compares frames and fixtures. Select compatible static objects and preserve seed invariants. Recompile/reopen whole scene and repeat robot, geometry and contact checks.

**Migration and future cases.** Demonstrate static roles, transforms, passages, filters and seed preservation before routine insertion. Environment transform applied twice fails independent world control. Contact filter accidentally disables required obstacle and fails positive-contact fixture. Robot joint/actuator changed by environment composer fails preservation.

## 21. DOM-25 — Create fabrication package

**Inputs and dependencies.** Dimensions and material-set AND cad-solid OR cad-assembly; process/recipient requirements and sourced tolerances. Point03 native/readback; actual OCS exporter capability; optional CAD drawing adapter separately scoped.

**Source entry points.** [TechDraw ExportPageSVG — FreeCAD documentation main branch](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/TechDraw_ExportPageSVG.md). Exact APIs and output conditions are recorded in the actions and section 2.

1. **DOM-25-A01 — Bind model revision to fabrication requirements.** Pin authoritative model and part revisions. Bind sourced dimensions/materials/process requirements to features. Select supported drawing/exchange outputs and receiving checks. Output: Part/drawing/export plan with datum, feature, material and revision mapping. Check: Source geometry and materials alone cannot complete missing process/tolerance requirements.
2. **DOM-25-A02 — Produce linked drawings and exchange geometry.** Create required views/sections and sourced annotations. Export supported geometry/documents with explicit units/representation. Bundle files, materials, revisions and feature/source mapping. Output: Drawings and requested STEP/DXF/PDF or other supported files plus part/revision/source manifest. Check: Faceted mesh STEP cannot silently satisfy required analytic-solid exchange; exported geometry may need companion tolerance drawing.
3. **DOM-25-A03 — Reopen recipient artifacts and audit feature coverage.** Check all package revision/source identities. Reopen geometry/drawings and compare required features/annotations. Publish actual checks and process-specific package readiness. Output: Revision, dimension/material/tolerance coverage and recipient readback report. Check: Successful export does not establish manufacturability; required process evidence and recipient compatibility have their own results.

| Execution option | Procedure and condition |
| --- | --- |
| Agent directs work | Agent interprets fabrication requirements and directs drawings. |
| Software and agent | Software derives views/exports/checks; agent reviews annotations and process meaning. |
| Software handles ordinary cases | Demonstrated part/process/delivery classes package with missing-requirement/export exceptions. |
| Deterministic supported case | Complete sourced requirements and supported exporters/readers produce reproducible package. |

**Alternatives and quality targets.** Flat-part DXF plus sourced dimension/material drawing. Analytic STEP plus companion dimensional/process drawing. Layout documentation and fabrication package have distinct tolerance/material/process coverage.

**Proposed helpers.** DOM-25-A01: fabrication planner emits part/feature/datum/requirement coverage and supported output matrix. DOM-25-A02: package producer maps native feature IDs to views/dimensions and emits files plus lost-annotation/representation ledger. DOM-25-A03: fabrication verifier emits per-feature requirement coverage, format losses and readback results.

**Selection and merge.** Recipient/drawing/export alternatives share authoritative model and source requirements. VLM associates annotations with source features using complete views/crops; software checks actual geometry and values. Select compatible deliverables for one revision; preserve representation/annotation loss records. Reopen final package and repeat revision, feature/material/tolerance coverage and recipient checks.

**Migration and future cases.** Automate demonstrated process/part/export classes after revision, missing tolerance, unit, faceted/analytic and reader fixtures. Drawing dimension comes from older model revision and fails package coherence. Required analytic STEP receives mesh-faceted export and fails representation contract. Recipient reopens DXF at wrong scale and fails reference length. Material name exists but required grade/process evidence is absent: affected package item remains incomplete. Optional TechDraw SVG lacks hatch or shifts text: compare saved annotations/feature association and reject affected recipient requirement; inactive GUI is an explicit export failure.

## 22. Resource order and repeated validation

1. Begin with source identity, graph/units, required semantic fields and selected interfaces. Defer dense whole-building extraction, detailed meshes and broad contact evaluation until their input/role checks pass.
2. Local processor/memory/graphics estimates state body/element/face/hull counts, image/view size, tessellation density and selected algorithm settings. Numerical matrix/graph checks, mesh decomposition, building extraction and runtime contact fixtures have separate estimates. Performance measurements require actual hardware/version/settings/run evidence.
3. Remote inference calls, requested model/effort, actual exposed identity, tokens/latency/cost and manual interpretation/metrology/recipient effort are recorded independently. Higher reasoning effort is an option for ambiguous source semantics; checked explicit inputs support software paths.
4. Each operation's structured action resources specify its own scaling basis. Branches may use different geometry/detail targets while sharing source/identity/frame records and preserving target-specific readiness.
5. Future cases include interrupted remote selection, malformed rows, lost native-save acknowledgement, changed source digest and mixed-revision sidecars. Reconcile actual state before retry and invalidate only affected descendants. Physical-property inference and opening/placement changes identify their dependent simulation/display artifacts.
6. Software migration is per demonstrated action/input class after checked success, ambiguity, invalidity and interruption cases. The future test records describe expected outcomes; this audit executes documentation checks.

[Software review](reviews/point-06-software.md), [visual review](reviews/point-06-visual.md), [source review](reviews/point-06-sources.md) and [designer notes](reviews/point-06-designer.md) preserve source summaries, findings and review results.
