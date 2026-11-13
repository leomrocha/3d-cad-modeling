# Domain and component library architecture

Research status: web pages inspected on 12 November 2026. No web source file was downloaded; the links below are the inspected sources. The report records primary documentation, project repositories and vendor terms. It does not claim local software execution or validation. Research agent model identity: Luna, as assigned; exact model version is unavailable in the execution record.

## Recommended architecture

Use a neutral project record as the source of truth, with separate domain views and explicit adapters. Keep these layers distinct:

1. **Evidence and source assets**: original drawings, photographs, scans, vendor STEP files, IFC files, robot descriptions, license text, retrieval date and hashes. Preserve originals as immutable inputs.
2. **Canonical component record**: stable identity, semantic type, source/provenance, units and frames, parametric/CAD representation, visual geometry, collision geometry, physical properties, domain properties and license.
3. **Project assembly**: instances of library records with explicit transforms, joints/relationships, constraints, quantities and project-specific overrides. Reference library versions by immutable digest.
4. **Domain exports**: IFC for building information, STEP for boundary representation exchange, glTF/GLB for display, URDF for ROS-compatible robot kinematics, and MJCF for MuJoCo dynamics. Exports are derived, reproducible artifacts with adapter versions and validation reports.

The canonical record should not pretend one geometry representation serves every purpose. Preserve exact/parametric CAD where available; derive a simplified visual mesh and one or more collision representations. Record the conversion recipe and geometry hashes. Every adapter must declare supported fields and loss mappings.

## Software and formats

| Area | Evidence and capability | License/status | Proposed use |
|---|---|---|---|
| Bonsai / IfcOpenShell | Bonsai is a native IFC authoring and analysis platform integrated with Blender. IfcOpenShell provides C++/Python APIs, conversion, IDS validation, querying, clash and geometry tools. The documented conversion tool is IfcConvert. [Bonsai docs](https://docs.ifcopenshell.org/bonsai.html), [IfcOpenShell introduction](https://docs.ifcopenshell.org/introduction.html) | IfcOpenShell libraries/tooling: LGPL-3.0-or-later; Bonsai: GPL-3.0-or-later, per [project documentation](https://docs.ifcopenshell.org/introduction.html). IFC is an open building data schema; the authoring application remains separately licensed. | Building authoring and IFC import/export adapter. Use IFC entity relationships and property sets as semantic BIM data; do not flatten the only copy into meshes. Use IDS as machine-readable delivery checks. |
| Blender | Supports interchange including glTF, USD, OBJ, PLY, STL and Alembic; Blender artwork remains the creator's property. [Pipeline formats](https://www.blender.org/features/pipeline/), [license](https://www.blender.org/about/license/) | Upstream `COPYING` points to the GNU GPL text, which is GPL version 2. The installed Debian Blender 5.0.1 package copyright record labels the main Blender files GPL-2+. Components and add-ons may have separate terms. Blender's GPL-2+ later-version option permits choosing GPL-3 when distributing a covered combined work with GPL-3+-licensed Blender MCP code; preserve exact notices and assess each shipped component. [Upstream COPYING](https://github.com/blender/blender/blob/main/COPYING), [upstream GPL text](https://github.com/blender/blender/blob/main/doc/license/GPL-license.txt), [Blender MCP license](https://projects.blender.org/lab/blender_mcp/src/branch/main/LICENSE) | General scene inspection, image/mesh workflows, visualization and scripted conversions. OpenCADStudio remains the project's CAD baseline; Blender complements it for mesh/scene workflows, display and scripted conversions. |
| MuJoCo / MJCF | MJCF is MuJoCo's native XML model format; bodies form a kinematic tree, local spatial frames are relative to parents, and inertial frames are centered at center of mass and aligned to principal inertia axes. MuJoCo leaves base units to the user and requires internal consistency; its docs recommend MKS. Geoms combine appearance/collision concepts and nonconvex meshes are internally replaced by convex hulls, so nonconvex collision shapes should be decomposed into convex pieces. [Modeling](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [overview](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst) | MuJoCo repository declares Apache-2.0. Model files/assets retain their own terms. [Repository](https://github.com/google-deepmind/mujoco) | Target simulation adapter and simulation validation. Store source MJCF and package assets; treat compiled MJB as disposable/version-specific output because it cannot be decompiled to XML. |
| URDF / ROS tooling | Official `urdf_tutorial` teaches visual geometry, movable joints, collision and inertial properties, and Xacro; it is BSD-3-Clause. [Tutorial repository](https://github.com/ros/urdf_tutorial). URDF model guidance states metres/radians and kilograms for position/mass conventions. [URDF model reference](https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html) | URDF is a format; package and mesh licenses are independent. Tutorial: BSD-3-Clause. | Robot kinematic interchange and ROS visualization/control workflows. URDF does not express all closed-chain or advanced dynamics semantics; preserve source domain model and report unsupported fields. |
| STEP / Open CASCADE | STEP represents exchangeable CAD geometry; use AP242 where supported for product structure, geometry and PMI; test actual receiving application behavior. Manufacturer libraries frequently provide STEP, with separate download terms. | STEP files from a manufacturer are not automatically openly licensed. [CONTEC example terms](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280) restrict access/use to purchasers or prospective purchasers, bar adapting the data and disclaim warranty. | Preserve native STEP plus supplier identity and terms. Import only within stated terms; derive a display/collision mesh only where permitted. Open CASCADE tooling is a geometry kernel/translator candidate, not a semantic library. |

## Reusable component sources and license distinctions

| Source | Available content/capability | License and reuse boundary |
|---|---|---|
| FreeCAD Parts Library | Community library distributed in FCStd, STEP, STL and BREP, grouped across mechanical, electrical/electronic, architectural, medical, hydraulic, HVAC and piping families. [FreeCAD Addons](https://www.freecad.org/addons.php?lang=eng_EN) | FreeCAD's add-on listing identifies the library as CC-BY-3.0. Preserve attribution and license with each copied part; verify the individual component's attribution and source because the collection can contain third-party contributions. FreeCAD software's license does not license each model automatically. |
| KiCad 3D library | Board-footprint-linked 3D models for electronic components; the official package library is available through the [KiCad library repositories](https://github.com/KiCad/kicad-packages3D). | Library data is CC-BY-SA-4.0 with a specific exception: use in a design does not itself force licensing the design under CC-BY-SA; redistribution of the library or parts as a collection retains the library license and attribution. [Official terms](https://www.kicad.org/libraries/license/) |
| BOSL2 | Parametric OpenSCAD shapes, masks and manipulators; [OpenSCAD library catalog](https://openscad.org/libraries.html) identifies BSD-2-Clause. Repository describes it as beta. [BOSL2 repository](https://github.com/BelfrySCAD/BOSL2) | BSD-2-Clause per official catalog; check repository license/version when vendoring. Parametric code is useful for generated primitives and fixtures, not a catalog of measured commercial hardware. |
| ROS URDF tutorial robot assets | URDF and mesh examples cover robot links/joints and collision/inertial fields. [Repository](https://github.com/ros/urdf_tutorial) | Repository BSD-3-Clause; individual mesh files and upstream robot assets still need per-file review. Example structure is reusable; example geometry is not validated component data. |
| Manufacturer product CAD | Vendor sites commonly provide STEP/IGES for configured product models. For example, NORITAKE offers STEP/IGES for named product CU22042-Y100 and warns files may be incomplete, inaccurate, not to scale or outdated, under vendor terms. [Product CAD](https://www.noritake-elec.com/support/3d-cad-data?id=cu22042-y1a&part=CU22042-Y100). CONTEC terms expressly limit use and prohibit changing/adapting its CAD data. | Downloadability is not an open license. Store the exact terms and source URL with each asset. Default to private project use only as the terms allow; do not redistribute vendor files or converted derivatives absent permission. |
| 3D ContentCentral | Supplier-certified and user library models in multiple CAD formats. [SOLIDWORKS help](https://help.solidworks.com/2022/english/SolidWorks/sldworks/r_3d_contentcentral.htm?id=12.6.2.0) | Platform access requires agreement; contributor terms give the platform broad indexing/adaptation/distribution rights but do not establish a blanket open license for each downloaded model. Record per-item license/terms; do not treat the catalog as open data. [Contributor terms](https://www.3dcontentcentral.com/includes/Attachments/Terms_and_Conditions_for_Contributions.pdf) |
| FreeCAD add-on step.parts connector | FreeCAD listing describes searching an online open STEP parts catalog and inserting into the document. [Add-on listing](https://www.freecad.org/addons.php?lang=en_EN) | The connector's license is not sufficient evidence for every catalog asset's reuse rights. Capture item-level rights before caching or distributing. |
| MuJoCo Menagerie | Curated MuJoCo robot simulation assets include MJCF, scene XML, visual and collision meshes, README generation notes and per-model LICENSE files; examples include Unitree Go2 quadruped, Franka Emika Panda arm and Boston Dynamics Spot. [Repository and model table](https://github.com/google-deepmind/mujoco_menagerie), [model structure](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md) | Licensing is per model: the repository table lists Go2 and Spot BSD-3-Clause, Panda Apache-2.0; each model directory has its own license. The top-level project content is Apache-2.0. The README says model fidelity is ongoing and identifies intended quality grades from system-identified to conditionally stable. This is a strong simulation-description source, but the assets are simulation meshes/models, not verified manufacturing CAD for commercial hardware. |
| NopSCADlib | OpenSCAD library and project framework with a `vitamins` collection of modeled real-world hardware and a `tests` directory. [Repository](https://github.com/nophead/NopSCADlib), [usage](https://github.com/nophead/NopSCADlib/blob/master/docs/usage.md) | GPL-3.0. It is reusable parametric OpenSCAD code and geometry; check whether the intended use is to redistribute library code, generated part files or merely reference it, and retain notices. |
| Poly Haven | Library of 3D models, materials and HDRI environments useful for scene dressing, architectural visualization and lighting. [Asset catalog](https://polyhaven.com/) | Poly Haven states all site assets are CC0, including commercial use without attribution. This is useful for visual environments and render context; asset dimensions/geometry are not engineering component specifications. [License](https://polyhaven.com/license) |
| FreeCAD BIM Library | FreeCAD BIM can browse and insert FCStd, STEP and BREP entries from the FreeCAD Parts Library, either offline or through its experimental online library option. [BIM Library docs](https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html), [Parts Library repository](https://github.com/FreeCAD/FreeCAD-library) | The BIM insertion feature does not change the license of inserted assets. The Parts Library collection is listed as CC-BY-3.0 in FreeCAD Addons; verify individual item attribution and embedded files. Many entries are generic architecture/MEP objects, not certified building product specifications. |

## Mesh collision generation

MuJoCo collision is based on convex geoms; concave shape fidelity therefore requires a union of convex pieces or a simpler primitive approximation. Two open-source candidates for deriving convex partitions are:

- **CoACD**: approximate convex decomposition implementation [SarahWeiii/CoACD](https://github.com/SarahWeiii/CoACD). Its [LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE) is MIT, copyright Xinyue Wei and Minghua Liu (2022). Pin the reviewed revision and retain its notice when distributing the tool.
- **V-HACD**: convex decomposition implementation, with BSD-3-Clause at [kmammou/v-hacd LICENSE](https://github.com/kmammou/v-hacd/blob/master/LICENSE).

For each derived collider retain input mesh hash, tool/version, parameters, unit scale, output hull count, bounds, volume difference and a visual overlay. Acceptance should include watertightness or explicit explanation when the input is an open surface; no self-intersections where detectable; hulls inside or within a defined tolerance of the source; no missing required holes/contact channels; and scene-scale contact tests. Automatic decomposition is an aid, not an engineering verdict. Keep render mesh and collision mesh separate: display meshes prioritize surface detail; colliders prioritize stable contact computation and controlled approximation.

## Proposed component schema

Use versioned JSON/YAML metadata plus sidecar geometry and source files. A record should contain:

```yaml
schema_version: 1
id: "urn:3dmodeling:component:<stable-id>"
revision: 1
name: "Readable component name"
domain_types: [mechanical_component]
source:
  source_type: manufacturer | library | measured | authored | reconstructed
  title: ""
  url: ""
  retrieved_at: "YYYY-MM-DD"
  original_file: "source/original.step"
  sha256: ""
  source_claims: []
license:
  spdx_id: "LicenseRef-vendor-terms"
  terms_url: ""
  redistribution: allowed | restricted | prohibited | unknown
  attribution: ""
units:
  length: m
  mass: kg
  angle: rad
frames:
  component_origin: {definition: mounting_datum, axes: right_handed, up: z}
  named_frames: []
geometry:
  cad: []
  visual: []
  collision: []
physical:
  mass_kg: {value: null, status: unknown, source: null}
  center_of_mass_m: null
  inertia_kg_m2: {frame: component_origin, tensor: null, status: unknown, source: null}
interfaces: []
domain_properties: {}
conversion_lineage: []
checks: []
```

Extend rather than overload the schema for BIM and robotics. BIM fields include IFC schema/class, GlobalId, spatial containment, property-set provenance, material/layer assignments and IDS requirements. Robotics fields include link/joint identity, joint type/axis/limits, visual/collision/inertial origins and source of dynamics values. Preserve foreign keys and units as represented in incoming files, alongside normalized SI values and explicit transforms.

Each geometry entry should identify representation and role (`b-rep`, parametric source, point cloud, display mesh, collision primitive, convex hull set), file path/hash, units, local frame, tessellation/decomposition settings, and generation lineage. Geometry accuracy is a claim with status and evidence; never infer manufacturing accuracy from a low-poly STEP export or visualization mesh.

## Storage, provenance, revisions and reuse rules

1. Store human-maintained model sources and metadata in version control. Store large scans or vendor assets through content-addressed object storage or Git LFS only after repository policy and rights permit. Keep immutable originals under `sources/<source-id>/`; create normalized/imported assets in a separate derived directory.
2. Give every asset an immutable digest and every logical component a stable ID plus revision. A source file update creates a new asset digest and review event. Never overwrite a source binary silently. Project assemblies pin component revision and file hashes.
3. Keep facts with evidence: measured values, manufacturer claims, seller/library statements, assumptions and calculated results have distinct status labels, units, source identifiers and observation dates. Store uncertainty and unknowns at field level.
4. Carry a license record per asset and per derived file. Software licensing and model licensing are separate records. `unknown` or restrictive rights prevent publishing/copying into a public library; the user may still link to a source where allowed.
5. Import rules: preserve original; inspect units, axis conventions, scale and source identity; retain assembly hierarchy and named coordinate systems; detect empty geometry; report tessellation and topology changes; store a reversible transform from source frame to canonical frame.
6. Export rules: never silently overwrite source; emit a mapping report listing preserved, transformed, approximated and dropped fields; include adapter/tool versions and hashes; preserve semantics in native IFC/URDF/MJCF alongside neutral visual exports.
7. Geometry reuse: use vendor/model data only under its terms; use open libraries with attribution and license retention; authored assets receive explicit project license. Reconstructed geometry records input images/measurements and method; photo inference is not dimension evidence without calibration.

## Interoperability and validation gates

Each format adapter needs a fixture suite based on small, versioned source files. Minimum gates:

1. **Identity and provenance**: source and output hashes, stable part identity, preserved asset-license records, and exact import/export mapping.
2. **Units and frames**: round-trip known lengths, angles, mass, axis handedness, origin and named-frame transforms. Reject unitless/ambiguous inputs at the adapter boundary or require an explicit user-supplied interpretation.
3. **Geometry**: bounding boxes, solid/mesh count, volume where valid, surface area, watertightness, face orientation, degenerates and visual overlay against source. Set tolerances by workflow and source precision.
4. **BIM/IFC**: schema validation, entity and relationship counts, GlobalId uniqueness, placement checks, property-set mapping and IDS validation. Compare selected geometry bounds/volume and retain the source IFC. IfcOpenShell documents IfcTester/IDS for executable exchange requirements.
5. **Robot models**: parse URDF/MJCF; validate link/joint graph, axes, limits, transforms, positive mass and physically valid inertia tensor. Compare FK transforms at fixtures; ensure collision and visual geometries have intended origins and scales. MuJoCo compiler success is a syntax/model check, not a physical performance test.
6. **Collision assets**: ensure each collider has finite bounds and intended scale, cover source contact envelope within tolerance, inspect convex decomposition for lost passages/holes, test collision pairs with known outcomes, and compare simulation stability across representative contact scenes.
7. **Export mappings**: test known losses and round-trip semantics. URDF-to-MJCF should produce a declared mapping; compare against MuJoCo's documented URDF limitations/extensions. BIM-to-glTF validates display only and cannot stand in for IFC semantics.

The neighboring `${ENERGY_SIM_ROOT}/data/real-house-ifc/` provides a useful local pattern: immutable IFC and derived GLB are accompanied by provenance and display-map/validation JSON with source hashes, declared millimetre-to-metre conversion, stable converted part identities and geometry comparisons. The artifact records meaningful limitations such as absent IfcSpace/thermal-zone assignments and embedded opening geometry. Reuse the provenance structure and the practice of labeling identity derivation; do not treat its CASA-specific IFC content as a generic component library.

The neighboring `${ARCHITECTURE_ROOT}/` repository is an earlier architecture-oriented workflow exploration with ingestion/orchestration/frontend subsystems and planning/research notes. This review only established its on-disk presence and broad structure; it did not assess implementation capability or test status.

## Skills and integration interfaces

The local available `${CODEX_HOME}/skills/ocs-engineering/SKILL.md` describes an OpenCADStudio engineering workflow with explicit parts, units, frames, measured checks and simulation handoffs. OpenCADStudio remains the project's CAD baseline; Blender is a complementary scene/mesh and automation tool. No OCS MCP integration was found among the tools available to this research agent. Local installed skill inventory includes C4 architecture, OpenSpec, document, PDF, presentation, spreadsheet and image-generation skills; these do not provide CAD authoring or geometry validation. The project `skills/README.md` correctly describes software installation and CAD execution as later implementation actions.

### Blender MCP workflow source assigned for review

The assigned UX Planet article, [“3D Modeling with Claude Code: A Practical Blender Workflow”](https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0), was retrieved as a Medium HTML page on 12 November 2026. Its visible introduction says to use the language model as an agent controlling Blender through Blender MCP and shows a Claude Code → Blender MCP → Blender path. The article is member-only; the accessible page exposed the title, author, publication date, introductory claims and section headings, but not the detailed procedure, implementation code or full workflow. Retrieval outcome: partial page content accessible; full text inaccessible. The article is practitioner commentary, not a primary implementation source.

The Blender-hosted Blender Lab [MCP repository](https://projects.blender.org/lab/blender_mcp/src/branch/main) is the Blender project's own integration. Its README describes a two-process bridge: an MCP server launched by the client communicates over stdio and relays requests by TCP socket to a Blender add-on. The add-on executes requests inside Blender; the project exposes Blender Python execution and scene/file inspection tools. The repository license is GPL-3.0-or-later. Its [setup page](https://projects.blender.org/lab/blender_mcp/wiki/Setup) requires Blender 5.1 or newer. The installed workstation Blender is 5.0.1 (`/bin/blender --version`); this version is below the documented minimum, so the Blender Lab add-on has a version mismatch with the current installation. The [Blender Lab MCP page](https://www.blender.org/lab/mcp-server/) search result states that generated code runs without guards against deleting data or sending it remotely; direct page open returned HTTP 403. Blender's [scripting security guidance](https://docs.staging.blender.org/manual/en/latest/advanced/scripting/security.html) says Python scripts can perform unrestricted operations.

The separate community project [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) is explicitly not affiliated with Blender Foundation. Its package metadata declares MIT, and its current README supports Blender 3.0 or newer, so its stated Blender minimum includes the installed 5.0.1. It provides scene/object inspection and mutation, visual inspection, arbitrary Blender Python execution, and external asset integrations such as Poly Haven, Sketchfab and Poly Pizza. This broader feature set also increases the amount of connected code and network access. The repository documents an opt-in `BLENDER_MCP_SAFE_MODE=1`; that mode is a project feature, not an operating-system sandbox. [Package metadata](https://github.com/ahujasid/mcp-for-blender/blob/main/pyproject.toml), [setup/features/security sections](https://github.com/ahujasid/mcp-for-blender#limitations--security-considerations).

Both MCP projects execute Blender Python; neither is a constrained geometry API. For implementation, retain OpenCADStudio as the engineering/CAD baseline. Blender background scripts provide the deterministic conversion and geometry-check path; an MCP integration can add interactive inspection after version, process isolation and tool scope are addressed. This is a proposal, not a locally tested comparison.

Blender also supports scripted background work using `blender --background --python <script>` per the [official Python API guidance](https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst). For repeatable import/export and geometry checks, a pinned background script is easier to version and reproduce than a natural-language-only interaction. MCP may add interactive inspection and iterative scene edits; it should call versioned task scripts or typed operations for deterministic project outputs. This split is a proposal, not a tested comparison.

## Phased integration proposal

1. **Foundation**: define canonical schema, ID/digest rules, license vocabulary, immutable source/derived directory layout and one example authored mechanical component plus one IFC building component. No bulk library import.
2. **Read-only import and visual review**: implement parsers/adapters for STEP, IFC, URDF and common mesh formats; show source/normalized geometry in Blender or a project viewer; generate source and conversion reports. Tests use fixtures and record field loss.
3. **BIM path**: connect IfcOpenShell/Bonsai, preserve IFC graph and property sets, add IDS validation and GLB display export. Reuse existing IFC-to-GLB provenance pattern from energy-sim as evidence, with generic identities and tests.
4. **Robotics path**: import URDF/Xacro output, normalize SI and frames, maintain separate visual/collision/inertial data, export MJCF and compile with MuJoCo. Compare FK and frame placements; keep physical parameter claims sourced.
5. **Component library**: add curated collections only after per-asset rights review. Start with authored primitives, KiCad components under its stated exception, and selected permissively licensed examples such as BOSL2/V-HACD-derived assets. Vendor STEP data stays under the vendor's per-product conditions.
6. **Reconstruction and image/2D workflows**: attach calibration and measurement evidence to reconstructed geometry; retain raw images, camera/depth metadata, control points and uncertainty. Convert inferred geometry into CAD only through a reviewable, provenance-preserving operation.
7. **Automated release gates**: CI validates metadata schema, hashes, license presence, parser/export fixtures, unit/frame round trips, IFC IDS checks and robot simulation load. Release manifests include adapter versions and license inventory.

The first implementation milestone should deliver a schema plus import-report prototype and a pair of representative fixtures, rather than a broad asset download. That demonstrates identity, unit normalization, visual/collision separation and permission-aware provenance before collection size grows.

## Sources inspected

- [IfcOpenShell/Bonsai documentation](https://docs.ifcopenshell.org/bonsai.html)
- [IfcOpenShell introduction and license statement](https://docs.ifcopenshell.org/introduction.html)
- [MuJoCo modeling guide](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst)
- [MuJoCo overview, units, inertial and geom behavior](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst)
- [MuJoCo repository and Apache-2.0 license](https://github.com/google-deepmind/mujoco)
- [ROS URDF tutorial](https://github.com/ros/urdf_tutorial)
- [URDF unit and model reference](https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html)
- [Blender format support](https://www.blender.org/features/pipeline/)
- [Blender license and artwork terms](https://www.blender.org/about/license/)
- [FreeCAD Parts Library listing](https://www.freecad.org/addons.php?lang=eng_EN)
- [KiCad library terms](https://www.kicad.org/libraries/license/)
- [KiCad 3D package repository](https://github.com/KiCad/kicad-packages3D)
- [OpenSCAD library catalog and BOSL2 license](https://openscad.org/libraries.html)
- [BOSL2 repository](https://github.com/BelfrySCAD/BOSL2)
- [V-HACD BSD-3-Clause license](https://github.com/kmammou/v-hacd/blob/master/LICENSE)
- [CoACD MIT license](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE)
- [MuJoCo Menagerie repository and model license table](https://github.com/google-deepmind/mujoco_menagerie)
- [MuJoCo Menagerie model structure and quality notes](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md)
- [Unitree Go1 model BSD-3-Clause license](https://github.com/google-deepmind/mujoco_menagerie/blob/main/unitree_go1/LICENSE)
- [NopSCADlib repository and GPL-3.0 license](https://github.com/nophead/NopSCADlib)
- [Poly Haven asset license](https://polyhaven.com/license)
- [FreeCAD Parts Library repository](https://github.com/FreeCAD/FreeCAD-library)
- [FreeCAD BIM Library insertion documentation](https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html)
- [3D ContentCentral access description](https://help.solidworks.com/2022/english/SolidWorks/sldworks/r_3d_contentcentral.htm?id=12.6.2.0)
- [3D ContentCentral contributor terms](https://www.3dcontentcentral.com/includes/Attachments/Terms_and_Conditions_for_Contributions.pdf)
- [CONTEC STEP file terms](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280)
- [NORITAKE STEP/IGES download page](https://www.noritake-elec.com/support/3d-cad-data?id=cu22042-y1a&part=CU22042-Y100)
- [Assigned UX Planet article: 3D Modeling with Claude Code](https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0) (member-only; partial HTML retrieval)
- [Blender Foundation Blender MCP source repository](https://projects.blender.org/lab/blender_mcp/src/branch/main)
- [Blender MCP setup documentation](https://projects.blender.org/lab/blender_mcp/wiki/Setup)
- [Blender MCP official lab page](https://www.blender.org/lab/mcp-server/) (search result inspected; direct page open returned HTTP 403)
- [Blender Python scripting security guidance](https://docs.staging.blender.org/manual/en/latest/advanced/scripting/security.html)
- [Blender Python background scripting guidance](https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst)
- [Blender upstream COPYING](https://github.com/blender/blender/blob/main/COPYING)
- [Blender upstream GPL text](https://github.com/blender/blender/blob/main/doc/license/GPL-license.txt)
- Local Blender version and Debian copyright record: `/bin/blender` reports 5.0.1; `${SYSTEM_ROOT}/usr/share/doc/blender/copyright` labels the main Blender files GPL-2+.
- [Community MCP for Blender repository](https://github.com/ahujasid/mcp-for-blender)
- [Community MCP package metadata: MIT license](https://github.com/ahujasid/mcp-for-blender/blob/main/pyproject.toml)
- [Community MCP setup, capabilities and security documentation](https://github.com/ahujasid/mcp-for-blender#limitations--security-considerations)
