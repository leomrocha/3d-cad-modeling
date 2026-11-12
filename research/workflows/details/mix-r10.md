# MIX-R10 — IFC + reusable library components → exact geometry branch and static MuJoCo environment

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 3/5; computing 3/5.**

Output: Semantic building revision with geometry derivatives and reusable source metadata

## Comparison conditions

An existing IFC project, identified library components and placement measurements. Outputs include an exact-geometry extraction where supported and a static simulation environment.

## Registered starting artifact types

1. ifc
2. source-library
3. measurement-set

## Detailed source and preparation artifacts

1. Artifact: ifc; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.
2. Artifact: source-library; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.
3. Artifact: measurement-set; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.

## Reference points, datums and coordinate frames

1. Component interfaces and IFC placements
2. Source IFC units and local/georeferenced frame
3. B-rep-to-mesh conversion settings and element mapping
4. Static-world collider transforms and passage checks

## Software, libraries and dependencies

1. Name: component registry/schema proposal; source license review; Role: Library asset intake and rights record; Source urls: https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://github.com/google-deepmind/mujoco_menagerie; https://polyhaven.com/license; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280; Dependency contract: Use the matching domain detail and code guide for the selected backend and version.
2. Name: documented adapter or explicit authoring step; Role: Place library component in semantic IFC; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html; https://www.freecad.org/addons.php?lang=eng_EN; Dependency contract: Use the matching domain detail and code guide for the selected backend and version.
3. Name: IfcOpenShell geom.create_shape/iterator using OpenCASCADE kernel; Role: Extract IFC geometry as OpenCASCADE B-rep; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html; Dependency contract: Use the matching domain detail and code guide for the selected backend and version.
4. Name: CAD mesh exporter; Blender; Open CASCADE tessellation; Role: Export mesh assets for MuJoCo; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst; [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); Dependency contract: Use the matching domain detail and code guide for the selected backend and version.
5. Name: CoACD; V-HACD; primitive fitting; Role: Generate convex collision set; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Dependency contract: Use the matching domain detail and code guide for the selected backend and version.
6. Name: content-addressed files; Git metadata; source/license registry; Role: Version and reuse component revision; Source urls: [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); Dependency contract: Use the matching domain detail and code guide for the selected backend and version.

## Procedure

1. Operation id: DOM-06; Action: Library asset intake and rights record; Inputs: source-library; Input alternatives: ; Input choice groups: ; Tools: component registry/schema proposal; source license review; Outputs: component-record; Human interpretation: Original source identity and item-level license/terms available or explicitly unknown.; Preserves: Original file, URL, retrieved date, hash, attribution, license text/terms and source claims.; Changes or infers: Normalize metadata; derived conversions become separate assets with lineage.; Checks: License status per file; duplicate hash; units/frame; source part number and revision when stated.; Source urls: https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://github.com/google-deepmind/mujoco_menagerie; https://polyhaven.com/license; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280
2. Operation id: DOM-35; Action: Place library component in semantic IFC; Inputs: ifc; component-record; measurement-set; Input alternatives: ; Input choice groups: ; Tools: documented adapter or explicit authoring step; Outputs: ifc; Human interpretation: Component record identifies exact geometry bytes, per-asset terms and placement interfaces; IFC project units and target frame known.; Preserves: Existing IFC entity identities, component source provenance and original component bytes.; Changes or infers: Adds a placed instance and semantic class/properties supported by the selected IFC authoring adapter.; Checks: IFC validation; placement and classification; source component mapping and stable identity; rights record attached.; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html; https://www.freecad.org/addons.php?lang=eng_EN
3. Operation id: DOM-27; Action: Extract IFC geometry as OpenCASCADE B-rep; Inputs: ifc; Input alternatives: ; Input choice groups: ; Tools: IfcOpenShell geom.create_shape/iterator using OpenCASCADE kernel; Outputs: b-rep; Human interpretation: IFC schema and length units read; target elements have geometry interpretable by selected kernel.; Preserves: IFC source, element GlobalIds, placements and mapping metadata.; Changes or infers: Extracts a kernel B-rep as a derived shape; IFC semantics remain in source IFC.; Checks: B-rep validity, face types, bounds, volume and entity-ID mapping.; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html
4. Operation id: DOM-12; Action: Export mesh assets for MuJoCo; Inputs: ; Input alternatives: cad-solid; b-rep; visual-scene; robot-assembly; Input choice groups: ; Tools: CAD mesh exporter; Blender; Open CASCADE tessellation; Outputs: mesh; Human interpretation: Tessellation settings and mesh local frame/units chosen.; Preserves: Source CAD/B-rep and conversion parameters.; Changes or infers: Surface geometry becomes triangles; MuJoCo supports OBJ and binary STL; material assignment is separate.; Checks: Bounds, scale, normals, topology, source/mesh overlay and referenced geom role.; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst; [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md)
5. Operation id: DOM-13; Action: Generate convex collision set; Inputs: mesh; Input alternatives: ; Input choice groups: ; Tools: CoACD; V-HACD; primitive fitting; Outputs: collision-set; Human interpretation: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst
6. Operation id: DOM-34; Action: Author static MuJoCo environment from BIM mesh; Inputs: mesh; collision-set; Input alternatives: ; Input choice groups: ; Tools: documented adapter or explicit authoring step; Outputs: mjcf; Human interpretation: Environment mesh and collision pieces share a known frame/scale; source IFC IDs are mapped.; Preserves: IFC source project and element IDs.; Changes or infers: Creates static MuJoCo geom assets from IFC-derived derivatives.; Checks: Compile model; compare element coverage, bounds, transforms and collision simplification.; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst
7. Operation id: DOM-26; Action: Version and reuse component revision; Inputs: component-record; Input alternatives: ; Input choice groups: ; Tools: content-addressed files; Git metadata; source/license registry; Outputs: component-record; Human interpretation: Stable component ID, exact source bytes, item terms and conversion lineage recorded.; Preserves: Existing revisions and assemblies pinning them; original files are immutable.; Changes or infers: New source content or license produces a new revision/digest; derived files link to input/tool versions.; Checks: Hash consistency, dependency/license closure, revision pinning and reproducible export manifests.; Source urls: [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md)

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-06; Name: Library asset intake and rights record; Inputs: source-library; Outputs: component-record; Tools: component registry/schema proposal; source license review; Source urls: https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://github.com/google-deepmind/mujoco_menagerie; https://polyhaven.com/license; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280; Prerequisites: Original source identity and item-level license/terms available or explicitly unknown.; Preserves: Original file, URL, retrieved date, hash, attribution, license text/terms and source claims.; Changes or infers: Normalize metadata; derived conversions become separate assets with lineage.; Checks: License status per file; duplicate hash; units/frame; source part number and revision when stated.; Alternatives: Keep external link only where local caching/redistribution terms are unclear.; Automation: mixed; Evidence status: proposed_composition; Summary: Create immutable, rights-aware component records instead of treating catalogs as a common license.; Source ids: DSRC-07; DSRC-08; DSRC-09; DSRC-10; DSRC-11
2. Id: DOM-35; Name: Place library component in semantic IFC; Tools: documented adapter or explicit authoring step; Prerequisites: Component record identifies exact geometry bytes, per-asset terms and placement interfaces; IFC project units and target frame known.; Preserves: Existing IFC entity identities, component source provenance and original component bytes.; Changes or infers: Adds a placed instance and semantic class/properties supported by the selected IFC authoring adapter.; Checks: IFC validation; placement and classification; source component mapping and stable identity; rights record attached.; Alternatives: Author the IFC component instance directly with IfcOpenShell API or another IFC-authoring application.; Automation: assisted; Evidence status: proposed_composition; Inputs: ifc; component-record; measurement-set; Outputs: ifc; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html; https://www.freecad.org/addons.php?lang=eng_EN; Summary: Place a licensed component instance in an IFC project with source identity, placement and semantic classification retained where representable.; Source ids: DSRC-25; DSRC-07
3. Id: DOM-27; Name: Extract IFC geometry as OpenCASCADE B-rep; Inputs: ifc; Outputs: b-rep; Tools: IfcOpenShell geom.create_shape/iterator using OpenCASCADE kernel; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html; Prerequisites: IFC schema and length units read; target elements have geometry interpretable by selected kernel.; Preserves: IFC source, element GlobalIds, placements and mapping metadata.; Changes or infers: Extracts a kernel B-rep as a derived shape; IFC semantics remain in source IFC.; Checks: B-rep validity, face types, bounds, volume and entity-ID mapping.; Alternatives: DOM-16 tessellated extraction for display or mesh consumers.; Automation: scripted; Evidence status: documented_capability; Summary: Extract analytic/spline boundary representations from IFC where the kernel supports them.; Source ids: DSRC-28; DSRC-29
4. Id: DOM-12; Name: Export mesh assets for MuJoCo; Inputs: ; Outputs: mesh; Tools: CAD mesh exporter; Blender; Open CASCADE tessellation; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst; [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); Prerequisites: Tessellation settings and mesh local frame/units chosen.; Preserves: Source CAD/B-rep and conversion parameters.; Changes or infers: Surface geometry becomes triangles; MuJoCo supports OBJ and binary STL; material assignment is separate.; Checks: Bounds, scale, normals, topology, source/mesh overlay and referenced geom role.; Alternatives: MuJoCo primitives for simple geometry; custom decoder plugin for other asset formats.; Automation: scripted; Evidence status: documented_capability; Summary: Create simulation mesh files and retain their source frame and approximation settings.; Input alternatives: cad-solid; b-rep; visual-scene; robot-assembly; Source ids: DSRC-20; DSRC-22; DSRC-13
5. Id: DOM-13; Name: Generate convex collision set; Inputs: mesh; Outputs: collision-set; Tools: CoACD; V-HACD; primitive fitting; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Prerequisites: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Alternatives: Primitive colliders; single convex hull for coarse bounding; use original mesh only where supported and semantics understood.; Automation: scripted; Evidence status: documented_capability; Summary: Derive a collision-specific approximation and review topology-sensitive errors.; Source ids: DSRC-23; DSRC-24; DSRC-20
6. Id: DOM-34; Name: Author static MuJoCo environment from BIM mesh; Tools: documented adapter or explicit authoring step; Prerequisites: Environment mesh and collision pieces share a known frame/scale; source IFC IDs are mapped.; Preserves: IFC source project and element IDs.; Changes or infers: Creates static MuJoCo geom assets from IFC-derived derivatives.; Checks: Compile model; compare element coverage, bounds, transforms and collision simplification.; Alternatives: Author a static MJCF environment directly from primitives or other verified mesh sources.; Automation: assisted; Evidence status: proposed_composition; Inputs: mesh; collision-set; Outputs: mjcf; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Summary: Create a static MuJoCo world from IFC-derived display mesh and collision representation; this operation does not author a robot.; Source ids: DSRC-19; DSRC-20
7. Id: DOM-26; Name: Version and reuse component revision; Inputs: component-record; Outputs: component-record; Tools: content-addressed files; Git metadata; source/license registry; Source urls: [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); Prerequisites: Stable component ID, exact source bytes, item terms and conversion lineage recorded.; Preserves: Existing revisions and assemblies pinning them; original files are immutable.; Changes or infers: New source content or license produces a new revision/digest; derived files link to input/tool versions.; Checks: Hash consistency, dependency/license closure, revision pinning and reproducible export manifests.; Alternatives: Git for small source assets; LFS/content-addressed storage for large licensed assets after policy check.; Automation: scripted; Evidence status: proposed_composition; Summary: Keep reusable assets immutable and project assemblies reproducible against pinned revisions.; Source ids: DSRC-13; DSRC-01

## Code and tool entry points

1. Path: [check_control_distances.py](/home/leo/projects/3dmodeling/examples/workflows/common/check_control_distances.py); Entrypoint: `python /home/leo/projects/3dmodeling/examples/workflows/common/check_control_distances.py --references <lengths.json> --model-points <points.json> --out <report.json> --require-check-controls`; Status: reference_code; Role: Check supplied reference lengths against exported model points; six local numerical tests cover the helper.; Source urls: [check_control_distances.py](/home/leo/projects/3dmodeling/examples/workflows/common/check_control_distances.py)
2. Path: [ifc_model.py](/home/leo/projects/3dmodeling/examples/workflows/domains/ifc_model.py); Status: reference_code; Role: Bounded shared operation; use its documented supported subset and required arguments.; Entrypoint: `python /home/leo/projects/3dmodeling/examples/workflows/domains/ifc_model.py <explicit-building.json> <new-building.ifc>`; Source urls: [ifc_model.py](/home/leo/projects/3dmodeling/examples/workflows/domains/ifc_model.py)
3. Path: [robot_model.py](/home/leo/projects/3dmodeling/examples/workflows/domains/robot_model.py); Status: reference_code; Role: Bounded shared operation; use its documented supported subset and required arguments.; Entrypoint: `python /home/leo/projects/3dmodeling/examples/workflows/domains/robot_model.py <explicit-robot.json> <new-model.xml>`; Source urls: [robot_model.py](/home/leo/projects/3dmodeling/examples/workflows/domains/robot_model.py)
4. Entrypoint: `Native application/API operations in the recorded recipe`; Status: existing_tool_entrypoint; Role: Complete the remaining source-backed CAD, reconstruction, IFC or robot steps with their explicit human interpretation points.; Source urls: [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html; https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html; https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst; https://github.com/google-deepmind/mujoco_menagerie; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://polyhaven.com/license; https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280; https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/

## Output artifacts

1. Semantic building revision with geometry derivatives and reusable source metadata
2. Native/source artifacts and role-specific derivatives linked by source revision and hash.

## Checks

1. Geometry extraction keeps the source IFC graph and object identity mapping.
2. B-rep extraction and tessellation are separately recorded representation changes.
3. Static environment MJCF uses colliders derived from the selected mesh and stated frame.
4. Component versioning records the native source and intended derivative roles.
5. Compare reference lengths with model coordinates in declared units; record residuals in mm separately for fit and check controls.
6. Inspect actual saved/imported geometry, component identities and source-to-output mapping.

## Failure recovery

1. Return to the operation whose calibration, identity, geometry or interpretation check failed; preserve its inputs and previous outputs.
2. Resolve the affected source correspondence or feature meaning explicitly before regenerating downstream derivatives.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 3
3. **Compute:** 3
4. **Human reason:** Place identified components semantically and review selected simulation geometry and frame mapping.
5. **Setup reason:** Connect source intake, IFC placement, B-rep extraction/tessellation and static MJCF authoring.
6. **Compute reason:** Geometry extraction and convex decomposition are the main CPU/RAM stages; no image training is included.

## Resources and scaling

1. **Cpu:** CAD construction, parsing, transforms, semantic authoring and validation run in their selected application/library processes.
2. **Gpu:** Required by the selected dense-stereo/Gaussian/learned backend when included; otherwise optional for display.
3. **Ram:** Scales with images, points, triangles, CAD topology and retained representations. Record actual peak use during execution.
4. **Storage:** Preserve originals, native models, cameras/transforms, intermediate clouds/meshes and final derivatives separately.
5. **Scaling drivers:** Source artifact count and resolution; CAD feature/body count; Point/triangle count and collider count; Number of tool boundaries and evidence reconciliation steps
6. **Variants:** Already calibrated/registered inputs reduce preparation work.; Pre-existing components with explicit interfaces reduce geometry authoring.; Large scenes or high-resolution images increase computing demand independently of manual effort.

## Detailed branch procedures

1. [dom-r07.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r07.md)
2. [dom-r02.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r02.md)

The software lists include alternatives per operation. Select one compatible backend for each branch; follow the linked branch dossier for library/API dependencies and preserve the explicit operation handoff checks.

## Original sources

1. [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md)
2. [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md)
3. [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html)
4. [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html)
5. [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html)
6. [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst)
7. [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst)
8. [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst)
9. [https://github.com/google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie)
10. [https://github.com/kmammou/v-hacd/blob/master/LICENSE](https://github.com/kmammou/v-hacd/blob/master/LICENSE)
11. [https://polyhaven.com/license](https://polyhaven.com/license)
12. [https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE)
13. [https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280)
14. [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN)
15. [https://www.kicad.org/libraries/license/](https://www.kicad.org/libraries/license/)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
