# MIX-R06 — IFC building + existing robot MJCF → building collision environment and semantic display

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 3/5; computing 3/5.**

Output: Robot scene with building colliders and a retained IFC/GLB identity map

## Comparison conditions

An existing semantic IFC building and an existing MJCF robot with stated frame mapping. Only selected building elements become colliders.

## Registered starting artifact types

1. ifc
2. mjcf
3. measurement-set

## Detailed source and preparation artifacts

1. Artifact: ifc; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.
2. Artifact: mjcf; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.
3. Artifact: measurement-set; Quality: Use the named source artifact with its original units, frame, revision and evidence status; roles are specified below.

## Reference points, datums and coordinate frames

1. IFC local/georeferenced origin and unit conversion
2. Robot world frame and building-to-world transform
3. IFC element identifiers for every extracted surface
4. Doorways, passages and relevant contact surfaces

## Software, libraries and dependencies

1. Name: IfcOpenShell geom.create_shape/iterator; IfcConvert; Role: Extract IFC geometry as triangles; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
2. Name: CoACD; V-HACD; primitive fitting; Role: Generate convex collision set; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
3. Name: documented adapter or explicit authoring step; Role: Add environment collision geometry to MJCF; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.
4. Name: IfcOpenShell IfcConvert; Blender; GLB export; Role: IFC to GLB display scene; Source urls: https://docs.ifcopenshell.org/introduction.html; https://www.blender.org/features/pipeline/; provenance.json (`${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json`); Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.

## Procedure

1. Operation id: DOM-16; Action: Extract IFC geometry as triangles; Inputs: ifc; Input alternatives: ; Input choice groups: ; Tools: IfcOpenShell geom.create_shape/iterator; IfcConvert; Outputs: mesh; Human interpretation: IFC schema and length units read; target representation chosen.; Preserves: IFC source, GlobalId/entity map, item/material IDs and object placement.; Changes or infers: Geometry API can emit tessellated triangles or OpenCASCADE B-rep; extraction is a derived geometry view.; Checks: Element ID mapping, bounds, face/solid count, volume and units against source; relationships remain in IFC.; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html
2. Operation id: DOM-13; Action: Generate convex collision set; Inputs: mesh; Input alternatives: ; Input choice groups: ; Tools: CoACD; V-HACD; primitive fitting; Outputs: collision-set; Human interpretation: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst
3. Operation id: DOM-33; Action: Add environment collision geometry to MJCF; Inputs: mjcf; mesh; collision-set; Input alternatives: ; Input choice groups: ; Tools: documented adapter or explicit authoring step; Outputs: mjcf; Human interpretation: Source MJCF/environment frames are named; collision-set approximation and transform are recorded.; Preserves: Robot body/joint graph and source scan/mesh.; Changes or infers: Adds static environment geoms and collision pieces.; Checks: Compile model; compare environment bounds and transforms; inspect passage openings and contact fixtures.; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst
4. Operation id: DOM-17; Action: IFC to GLB display scene; Inputs: ifc; Input alternatives: ; Input choice groups: ; Tools: IfcOpenShell IfcConvert; Blender; GLB export; Outputs: visual-scene; Human interpretation: Element-to-display mapping and length/orientation conversion are declared.; Preserves: IFC source/hash; stable element IDs; source properties in sidecar mapping where GLB cannot retain them.; Changes or infers: BIM objects become render nodes/meshes; semantic/relationship data may be reduced or remapped.; Checks: ID-to-node coverage, bounds, orientation, selected geometry hashes or residuals, output hashes.; Source urls: https://docs.ifcopenshell.org/introduction.html; https://www.blender.org/features/pipeline/; provenance.json (`${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json`)

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-16; Name: Extract IFC geometry as triangles; Inputs: ifc; Outputs: mesh; Tools: IfcOpenShell geom.create_shape/iterator; IfcConvert; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html; Prerequisites: IFC schema and length units read; target representation chosen.; Preserves: IFC source, GlobalId/entity map, item/material IDs and object placement.; Changes or infers: Geometry API can emit tessellated triangles or OpenCASCADE B-rep; extraction is a derived geometry view.; Checks: Element ID mapping, bounds, face/solid count, volume and units against source; relationships remain in IFC.; Alternatives: Triangulation for display/clash; B-rep where analytic editing/surface inspection is required.; Automation: scripted; Evidence status: documented_capability; Summary: Extract IFC geometry as tessellated triangles and retain its element mapping.; Source ids: DSRC-28; DSRC-29
2. Id: DOM-13; Name: Generate convex collision set; Inputs: mesh; Outputs: collision-set; Tools: CoACD; V-HACD; primitive fitting; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Prerequisites: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Alternatives: Primitive colliders; single convex hull for coarse bounding; use original mesh only where supported and semantics understood.; Automation: scripted; Evidence status: documented_capability; Summary: Derive a collision-specific approximation and review topology-sensitive errors.; Source ids: DSRC-23; DSRC-24; DSRC-20
3. Id: DOM-33; Name: Add environment collision geometry to MJCF; Tools: documented adapter or explicit authoring step; Prerequisites: Source MJCF/environment frames are named; collision-set approximation and transform are recorded.; Preserves: Robot body/joint graph and source scan/mesh.; Changes or infers: Adds static environment geoms and collision pieces.; Checks: Compile model; compare environment bounds and transforms; inspect passage openings and contact fixtures.; Alternatives: Use primitives, analytic shapes or simulator-native geoms when the environment does not need mesh colliders.; Automation: assisted; Evidence status: proposed_composition; Inputs: mjcf; mesh; collision-set; Outputs: mjcf; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; Summary: Add registered environment geometry and colliders to an existing MJCF scene, preserving scene frame and explicit collision approximation.; Source ids: DSRC-20; DSRC-19
4. Id: DOM-17; Name: IFC to GLB display scene; Inputs: ifc; Outputs: visual-scene; Tools: IfcOpenShell IfcConvert; Blender; GLB export; Source urls: https://docs.ifcopenshell.org/introduction.html; https://www.blender.org/features/pipeline/; provenance.json (`${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json`); Prerequisites: Element-to-display mapping and length/orientation conversion are declared.; Preserves: IFC source/hash; stable element IDs; source properties in sidecar mapping where GLB cannot retain them.; Changes or infers: BIM objects become render nodes/meshes; semantic/relationship data may be reduced or remapped.; Checks: ID-to-node coverage, bounds, orientation, selected geometry hashes or residuals, output hashes.; Alternatives: Use IFC-native viewer when BIM relationships/properties are the primary task.; Automation: scripted; Evidence status: documented_capability; Summary: Create a visual GLB derivative with provenance and object mapping, not a replacement IFC.; Source ids: DSRC-30; DSRC-31; DSRC-32

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Entrypoint: `MuJoCo MJCF body, joint, inertial, mesh and geom elements describe explicitly supplied frames, geometry and physical properties. MuJoCo MjModel.from_xml_path is the documented model compilation entry point.`; Source urls: https://mujoco.readthedocs.io/en/latest/XMLreference.html; https://github.com/google-deepmind/mujoco
2. Entrypoint: `Native application/API operations in the recorded recipe`; Status: existing_tool_entrypoint; Role: Complete the remaining source-backed CAD, reconstruction, IFC or robot steps with their explicit human interpretation points.; Source urls: provenance.json (`${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json`); https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html; https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://docs.ifcopenshell.org/introduction.html; https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://www.blender.org/features/pipeline/

## Output artifacts

1. Robot scene with building colliders and a retained IFC/GLB identity map
2. Native/source artifacts and role-specific derivatives linked by source revision and hash.

## Checks

1. Select the building surfaces used as simulation environment.
2. Preserve IFC-to-mesh element mapping and unit/frame conversion.
3. Inspect doorway/contact channels after convex decomposition.
4. The supplied MJCF and the environment-augmented derivative have distinct revision IDs.
5. Compare reference lengths with model coordinates in declared units; record residuals in mm separately for fit and check controls.
6. Inspect actual saved/imported geometry, component identities and source-to-output mapping.

## Failure recovery

1. Return to the operation whose calibration, identity, geometry or interpretation check failed; preserve its inputs and previous outputs.
2. Resolve the affected source correspondence or feature meaning explicitly before regenerating downstream derivatives.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 3
3. **Compute:** 3
4. **Human reason:** Select building surfaces, preserve element identity and align them with the existing robot scene.
5. **Setup reason:** Configure IFC extraction, collider generation and MJCF asset insertion.
6. **Compute reason:** Tessellation and decomposition scale with selected building geometry; no photogrammetry or model training is required.

## Resources and scaling

1. **Cpu:** CAD construction, parsing, transforms, semantic authoring and validation run in their selected application/library processes.
2. **Gpu:** Required by the selected dense-stereo/Gaussian/learned backend when included; otherwise optional for display.
3. **Ram:** Scales with images, points, triangles, CAD topology and retained representations. Record actual peak use during execution.
4. **Storage:** Preserve originals, native models, cameras/transforms, intermediate clouds/meshes and final derivatives separately.
5. **Scaling drivers:** Source artifact count and resolution; CAD feature/body count; Point/triangle count and collider count; Number of tool boundaries and evidence reconciliation steps
6. **Variants:** Already calibrated/registered inputs reduce preparation work.; Pre-existing components with explicit interfaces reduce geometry authoring.; Large scenes or high-resolution images increase computing demand independently of manual effort.

## Detailed branch procedures

1. [dom-r07.md](dom-r07.md)
2. [dom-r08.md](dom-r08.md)

The software lists include alternatives per operation. Select one compatible backend for each branch; follow the linked branch dossier for library/API dependencies and preserve the explicit operation handoff checks.

## Original sources

1. ${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json (`${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json`)
2. [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html)
3. [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html)
4. [https://docs.ifcopenshell.org/introduction.html](https://docs.ifcopenshell.org/introduction.html)
5. [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst)
6. [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst)
7. [https://github.com/kmammou/v-hacd/blob/master/LICENSE](https://github.com/kmammou/v-hacd/blob/master/LICENSE)
8. [https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE)
9. [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/)

Full source summaries: [source register](../../sources/source-register.md).
