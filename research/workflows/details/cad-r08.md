# CAD-R08 — Known library parts to placed assembly

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 2/5; setup 3/5; computing 2/5.**

Output: cad-assembly + native-model-document

## Comparison conditions

One bounded input artifact set with the stated minimum quality; no unmeasured dimensions are promoted to fact. Ratings compare complete workflow under current contract scales.

## Registered starting artifact types

1. cad-solid
2. source-library

## Detailed source and preparation artifacts

1. Artifact: source-library; Format: Native CAD/STEP/IFC/mesh assets with per-file manifest and interfaces; Requirement: identified parts with interface datums and placement constraints; Quality: Readable/registered input with explicit units and known provenance.; Provenance: Keep original unchanged; record measurements and source page/frame.

## Reference points, datums and coordinate frames

1. **Datum:** Explicitly selected datum/control origin before reconstruction
2. **Axes:** Record coordinate frame, projection and handedness in the project units
3. **Controls:** identified parts with interface datums and placement constraints
4. **Unit:** Explicit source units; normalize to mm only with documented scale

## Software, libraries and dependencies

1. Name: FreeCAD; Role: FreeCAD assembly/workbench or OCS assembly entities; License: LGPL-2.1-or-later per project licensing page.; Apis: App.newDocument; import STEP/library document; Placement(Base=Vector(x,y,z),Rotation=Rotation(axis,angle)); Part::Feature.Shape; Assembly workbench constraints if selected and version-matched; Dependencies: FreeCAD application with bundled Python, Sketcher, Part and (for assemblies) chosen Assembly workbench; system Python generally cannot import FreeCAD modules.; Source urls: [API-SPEC.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md)

## Procedure

1. Order: 1; Action: Resolve exact source-library part/revision; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: documented_capability
2. Order: 2; Action: import native or STEP; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
3. Order: 3; Action: place by interface frames; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
4. Order: 4; Action: constrain clearances/motion; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
5. Order: 5; Action: verify envelope and interference.; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-12; Name: Assemble existing CAD or source-library components; Inputs: cad-solid; Outputs: cad-assembly; Tools: OCS blocks/groups; FreeCAD App::Link/Assembly; build123d/CadQuery Assembly; unit and frame mapping; Source urls: [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); [README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md); https://cadquery.readthedocs.io/en/stable/; Prerequisites: Record component source/license/hash and representation.; Establish local units, origin, axis directions and interface frames for each part.; Separate source components from placeholders.; Provide a distinct base cad-solid plus either a source-library component or one or more additional cad-solid component files; identify each occurrence separately.; Preserves: Component identities and source files; Occurrence transforms and assembly hierarchy; Native component boundaries; Changes or infers: Places parts using declared mating frames; inferred contact or fastener geometry is proposal unless sourced.; Checks: Frame/transform consistency; Interface dimension agreement; Component counts and source hashes; Collision/clearance only with supported exact geometry and query; Alternatives: Visual-only assembly in Blender; OCS block/group drawing arrangement; Full parametric assembly in FreeCAD or Python code-CAD; Automation: mixed; Evidence status: proposed_composition; Summary: Build an assembly from identified components and explicit transforms; preserve the difference between imported component geometry and inferred placeholders.; Input alternatives: source-library; cad-solid
2. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: [README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md); [step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs); [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Documented third-party tool and API entry points

1. Entrypoint: `FreeCAD import STEP; set Placement(Base=Vector(...),Rotation=Rotation(...)); apply selected assembly workbench constraints; run solve and interference review`; Status: existing_tool_entrypoint; Source urls: [API-SPEC.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md); Notes: Documented application/API workflow. Human review steps remain manual; command/runtime not exercised in this research.

## Output artifacts

1. **Representations:** cad-assembly; native-model-document
2. **Editable source:** Preserve input source and native CAD source where generated; neutral mesh/STEP does not retain upstream feature semantics.
3. **Preserves:** original inputs; declared units and datum; reviewed measurements/provenance
4. **Loss or inference:** occluded or hidden geometry requires explicit inference; representation conversion may discard feature history or unit metadata

## Checks

1. Object: assembly; Quantity: interface transforms, clearances and interference; Unit: mm/degrees; Acceptance: mating datums coincide and required clearance holds; Method: Assembly constraint solve plus bounding-box/interference review.

## Failure recovery

1. Failure: Scale, topology or registration mismatch; Recovery: Stop downstream export; preserve source; recheck units/datums and rerun only the affected stage.
2. Failure: Ambiguous hidden feature or weak evidence; Recovery: Mark as unresolved candidate; request a new measurement/view or retain parameter range.

## Effort and computing classification

1. **Human:** 2
2. **Setup:** 3
3. **Compute:** 2
4. **Human reason:** Identified interfaces reduce reconstruction; joints and clearances still need explicit placement review.
5. **Setup reason:** Assembly support and library formats/metadata.
6. **Compute reason:** Small assembly CPU; part count and tessellation/detail drive RAM/storage.

## Resources and scaling

1. **Cpu:** Small assembly CPU; part count and tessellation/detail drive RAM/storage.
2. **Gpu:** CPU geometry baseline; graphics display acceleration is separate.
3. **Ram:** Scales with part count, source B-rep detail and assembly constraints.
4. **Storage:** Preserve component originals, manifests, placements and assembly.
5. **Scaling drivers:** part count, source B-rep detail and assembly constraints
6. **Variants:** Simplified envelopes reduce working memory; retain detailed originals.

## Original sources

1. [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
