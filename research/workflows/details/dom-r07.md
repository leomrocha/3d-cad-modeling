# DOM-R07 — BIM library component to IFC, Blender display or static MuJoCo obstacle

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 2/5; setup 2/5; computing 1/5.**

Output: Rights-cleared BIM family/IFC asset placed in semantic IFC, with optional Blender display mesh or static collision derivative.

## Comparison conditions

Asset has explicit license, units, object classification and local origin; intended use is building element or static obstacle, not articulated robot hardware.

## Registered starting artifact types

1. source-library
2. model-brief
3. measurement-set

## Detailed source and preparation artifacts

1. Type: source-library; Formats: IFC; FCStd; library family/object; Minimum quality: Asset-level terms allow intended reuse and storage.; Required evidence: URL; version/hash; license; attribution; Handling: Do not infer license from library application.
2. Type: ifc; Formats: IFC2x3/IFC4; Minimum quality: Valid source entity with units and object placement.; Required evidence: schema; GlobalId; units; class; Handling: Preserve source.
3. Type: model-brief; Formats: JSON/text; Minimum quality: Named storey and placement/orientation.; Required evidence: target storey; datum; rotation; Handling: Explicit target frame.

## Reference points, datums and coordinate frames

1. Kind: component origin; Fields: local origin/axes; dimensions; Frame: asset-local → building frame; Source status: library source
2. Kind: storey datum; Fields: elevation and placement; Frame: storey → project frame; Source status: IFC source
3. Kind: world origin; Fields: MuJoCo obstacle transform; Frame: building frame → simulation world; Source status: authored mapping

## Software, libraries and dependencies

1. Name: FreeCAD BIM Library; Role: catalogue of BIM objects; Software license: Library asset terms vary; check each file; Api or entrypoint: BIM library insertion and IFC export; Environment dependencies: FreeCAD/BIM workbench; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Community library download is not a blanket open license.; Source urls: https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html; https://github.com/FreeCAD/FreeCAD-library
2. Name: IfcOpenShell/Bonsai; Role: place, inspect and export semantic IFC; Software license: IfcOpenShell LGPL-3.0-or-later; Bonsai GPL-3.0-or-later; asset terms separate; Api or entrypoint: IFC API or Bonsai placement/classification UI; Environment dependencies: IFC version and matching Bonsai; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Mesh-only import may discard semantic object class.; Source urls: https://github.com/IfcOpenShell/IfcOpenShell
3. Name: Blender; Role: display IFC-derived geometry; Software license: GPL-3.0-or-later app; assets separate; Api or entrypoint: Bonsai or Blender import; bpy scene; Environment dependencies: Compatible add-on and Blender; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Display scene is not semantic IFC authority.; Source urls: https://docs.blender.org/manual/en/latest/advanced/command_line/
4. Name: MuJoCo; Role: static obstacle geometry only; Software license: Apache-2.0 engine; asset license separate; Api or entrypoint: MJCF `<geom>` or mesh asset; Environment dependencies: MuJoCo; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Static obstacle mapping discards IFC relationships/property sets.; Source urls: https://mujoco.readthedocs.io/en/latest/XMLreference.html

## Procedure

1. Action: Inspect asset file and per-file terms.; Tool: Library intake; Command or api: Record file hash, URL/revision, license, attribution and units.; Preserves: Asset original; Changes or infers: Rights-bearing manifest.; Check: Check license beside actual file.; Code status: manual
2. Action: Import and place component on named storey.; Tool: FreeCAD/Bonsai/IfcOpenShell; Command or api: Set object class and storey containment; use explicit transform.; Preserves: IFC graph and storey datum; Changes or infers: Semantic IFC instance.; Check: GlobalId uniqueness, containment and dimensions.; Code status: assisted
3. Action: Make Blender visualization derivative.; Tool: Bonsai/Blender; Command or api: Import IFC or derive meshes retaining GlobalId mapping.; Preserves: IFC source; Changes or infers: Display mesh/scene.; Check: Compare placements and element IDs.; Code status: existing_tool_entrypoint
4. Action: Optional static collision object.; Tool: MuJoCo; Command or api: Export simplified collision mesh and set fixed/world geom transform.; Preserves: IFC geometry; Changes or infers: MJCF static geom.; Check: Frame, units and collision bounds.; Code status: assisted

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-06; Name: Library asset intake and rights record; Inputs: source-library; Outputs: component-record; Tools: component registry/schema proposal; source license review; Source urls: https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://github.com/google-deepmind/mujoco_menagerie; https://polyhaven.com/license; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280; Prerequisites: Original source identity and item-level license/terms available or explicitly unknown.; Preserves: Original file, URL, retrieved date, hash, attribution, license text/terms and source claims.; Changes or infers: Normalize metadata; derived conversions become separate assets with lineage.; Checks: License status per file; duplicate hash; units/frame; source part number and revision when stated.; Alternatives: Keep external link only where local caching/redistribution terms are unclear.; Automation: mixed; Evidence status: proposed_composition; Summary: Create immutable, rights-aware component records instead of treating catalogs as a common license.; Source ids: DSRC-07; DSRC-08; DSRC-09; DSRC-10; DSRC-11
2. Id: DOM-15; Name: Author semantic IFC building; Inputs: model-brief; Outputs: ifc; Tools: Bonsai; IfcOpenShell API; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html; Prerequisites: Storey/frame, element classes, openings, spatial relations and property requirements declared.; Preserves: Element IDs, semantic relationships, object placements, source dimensions, property values and geometry representation type.; Changes or infers: Creates IfcProduct relationships and representations; parametric profiles or mesh representations are distinct IFC options.; Checks: Schema validation, unique GlobalIds, placement, property-set and relationship checks, IDS requirements.; Alternatives: Bonsai authoring UI; scripted IfcOpenShell creation; IFC import followed by semantic enrichment.; Automation: mixed; Evidence status: documented_capability; Summary: Create building elements and semantics with explicit parametric or mesh geometry representation.; Source ids: DSRC-25; DSRC-26; DSRC-27
3. Id: DOM-35; Name: Place library component in semantic IFC; Tools: documented adapter or explicit authoring step; Prerequisites: Component record identifies exact geometry bytes, per-asset terms and placement interfaces; IFC project units and target frame known.; Preserves: Existing IFC entity identities, component source provenance and original component bytes.; Changes or infers: Adds a placed instance and semantic class/properties supported by the selected IFC authoring adapter.; Checks: IFC validation; placement and classification; source component mapping and stable identity; rights record attached.; Alternatives: Author the IFC component instance directly with IfcOpenShell API or another IFC-authoring application.; Automation: assisted; Evidence status: proposed_composition; Inputs: ifc; component-record; measurement-set; Outputs: ifc; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html; https://www.freecad.org/addons.php?lang=eng_EN; Summary: Place a licensed component instance in an IFC project with source identity, placement and semantic classification retained where representable.; Source ids: DSRC-25; DSRC-07
4. Id: DOM-16; Name: Extract IFC geometry as triangles; Inputs: ifc; Outputs: mesh; Tools: IfcOpenShell geom.create_shape/iterator; IfcConvert; Source urls: https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html; https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html; Prerequisites: IFC schema and length units read; target representation chosen.; Preserves: IFC source, GlobalId/entity map, item/material IDs and object placement.; Changes or infers: Geometry API can emit tessellated triangles or OpenCASCADE B-rep; extraction is a derived geometry view.; Checks: Element ID mapping, bounds, face/solid count, volume and units against source; relationships remain in IFC.; Alternatives: Triangulation for display/clash; B-rep where analytic editing/surface inspection is required.; Automation: scripted; Evidence status: documented_capability; Summary: Extract IFC geometry as tessellated triangles and retain its element mapping.; Source ids: DSRC-28; DSRC-29
5. Id: DOM-17; Name: IFC to GLB display scene; Inputs: ifc; Outputs: visual-scene; Tools: IfcOpenShell IfcConvert; Blender; GLB export; Source urls: https://docs.ifcopenshell.org/introduction.html; https://www.blender.org/features/pipeline/; [provenance.json](/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json); Prerequisites: Element-to-display mapping and length/orientation conversion are declared.; Preserves: IFC source/hash; stable element IDs; source properties in sidecar mapping where GLB cannot retain them.; Changes or infers: BIM objects become render nodes/meshes; semantic/relationship data may be reduced or remapped.; Checks: ID-to-node coverage, bounds, orientation, selected geometry hashes or residuals, output hashes.; Alternatives: Use IFC-native viewer when BIM relationships/properties are the primary task.; Automation: scripted; Evidence status: documented_capability; Summary: Create a visual GLB derivative with provenance and object mapping, not a replacement IFC.; Source ids: DSRC-30; DSRC-31; DSRC-32
6. Id: DOM-13; Name: Generate convex collision set; Inputs: mesh; Outputs: collision-set; Tools: CoACD; V-HACD; primitive fitting; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Prerequisites: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Alternatives: Primitive colliders; single convex hull for coarse bounding; use original mesh only where supported and semantics understood.; Automation: scripted; Evidence status: documented_capability; Summary: Derive a collision-specific approximation and review topology-sensitive errors.; Source ids: DSRC-23; DSRC-24; DSRC-20
7. Id: DOM-34; Name: Author static MuJoCo environment from BIM mesh; Tools: documented adapter or explicit authoring step; Prerequisites: Environment mesh and collision pieces share a known frame/scale; source IFC IDs are mapped.; Preserves: IFC source project and element IDs.; Changes or infers: Creates static MuJoCo geom assets from IFC-derived derivatives.; Checks: Compile model; compare element coverage, bounds, transforms and collision simplification.; Alternatives: Author a static MJCF environment directly from primitives or other verified mesh sources.; Automation: assisted; Evidence status: proposed_composition; Inputs: mesh; collision-set; Outputs: mjcf; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Summary: Create a static MuJoCo world from IFC-derived display mesh and collision representation; this operation does not author a robot.; Source ids: DSRC-19; DSRC-20

## Code and tool entry points

1. Status: existing_tool_entrypoint; Path: See the selected tool/variant contract.; Summary: Use the software/API entry points below in the recorded procedure; manual CAD, joint and semantic authoring steps use the explicit frames and source data recorded for that step.; Related entrypoints: ; Source urls: https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html; https://github.com/FreeCAD/FreeCAD-library; https://github.com/IfcOpenShell/IfcOpenShell; https://docs.blender.org/manual/en/latest/advanced/command_line/; https://mujoco.readthedocs.io/en/latest/XMLreference.html; Entrypoints: BIM library insertion and IFC export; IFC API or Bonsai placement/classification UI; Bonsai or Blender import; bpy scene; MJCF `<geom>` or mesh asset

## Output artifacts

1. Type: ifc; Format: IFC instance; Retained: Semantic class, storey relationship and properties when preserved.; Loss or inference: Neutral mesh export drops semantic graph.
2. Type: visual-scene; Format: Blend/GLB; Retained: Display geometry/material and transforms.; Loss or inference: BIM properties may be lost.
3. Type: collision-set; Format: MJCF mesh/primitive; Retained: Static collision proxy.; Loss or inference: IFC semantics and detail lost.

## Checks

1. Per-asset source and rights record.
2. IFC class, GlobalId, storey and unit validation.
3. Blender transforms agree with IFC.
4. MJCF static transform and bounds agree with IFC.

## Failure recovery

1. No reuse license: restrict to local reference or use a permissively licensed alternative.
2. Bad origin/units: inspect source coordinates and re-place using measured dimensions.
3. IFC class lost: return to semantic source, not mesh.
4. Collision proxy inaccurate: produce a separately reviewed simplified mesh.

## Effort and computing classification

1. **Human:** 2
2. **Setup:** 2
3. **Compute:** 1
4. **Human reason:** Identified library item with explicit placement is low interpretation.
5. **Setup reason:** One IFC/BIM tool; display or simulator adapter optional.
6. **Compute reason:** Single asset transformation is light.

## Resources and scaling

1. **Cpu:** CPU import/placement.
2. **Gpu:** No GPU.
3. **Ram:** Asset mesh size and IFC graph size.
4. **Storage:** Original library asset, IFC and display/collision derivatives.
5. **Scaling drivers:** mesh triangles; IFC property graph; asset count
6. **Variants:** Already semantic IFC easiest.; Generic mesh requires authored classification.

## Detailed branch procedures

1. [dom-r01.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r01.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. [https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html](https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html)
2. [https://github.com/FreeCAD/FreeCAD-library](https://github.com/FreeCAD/FreeCAD-library)
3. [https://github.com/IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)
4. [https://docs.blender.org/manual/en/latest/advanced/command_line/](https://docs.blender.org/manual/en/latest/advanced/command_line/)
5. [https://mujoco.readthedocs.io/en/latest/XMLreference.html](https://mujoco.readthedocs.io/en/latest/XMLreference.html)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
