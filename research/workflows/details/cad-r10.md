# CAD-R10 — OpenSCAD source to mesh and checked CAD handoff

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 1/5; setup 1/5; computing 2/5.**

Output: mesh + measurement-set

## Comparison conditions

One bounded input artifact set with the stated minimum quality; no unmeasured dimensions are promoted to fact. Ratings compare complete workflow under current contract scales.

## Registered starting artifact types

1. parametric-source

## Detailed source and preparation artifacts

1. Artifact: parametric-source; Format: OpenSCAD .scad and includes, parameters and unit convention; Requirement: OpenSCAD .scad source and declared unit convention; Quality: Readable/registered input with explicit units and known provenance.; Provenance: Keep original unchanged; record measurements and source page/frame.

## Reference points, datums and coordinate frames

1. **Datum:** Explicitly selected datum/control origin before reconstruction
2. **Axes:** Record coordinate frame, projection and handedness in the project units
3. **Controls:** OpenSCAD .scad source and declared unit convention
4. **Unit:** Explicit source units; normalize to mm only with documented scale

## Software, libraries and dependencies

1. Name: OpenSCAD; Role: OpenSCAD CLI; License: GPL-2.0-or-later with linking exception in upstream repository.; Apis: openscad -o output.stl source.scad; source units are numeric convention, STL carries no unit declaration; Dependencies: OpenSCAD executable; CGAL-backed render/export; no external runtime needed for ordinary CLI STL export.; Source urls: https://openscad.org/documentation.html; API-SPEC.md (`${OCS_ROOT}/docs/automation/API-SPEC.md`)
2. Name: mesh; Role: mesh inspection in OCS/CloudCompare; License: Selected viewer/license applies; OCS GPL-3.0 or CloudCompare GPL-2.0-or-later.; Apis: CloudCompare GUI: align/register; compute cloud/mesh statistics and bounding box; OCS --mcp: read mesh entities and bounds; Dependencies: OCS mesh support or CloudCompare; input PLY/STL mesh with recorded unit convention.; Source urls: https://openscad.org/documentation.html; API-SPEC.md (`${OCS_ROOT}/docs/automation/API-SPEC.md`)

## Procedure

1. Order: 1; Action: Run OpenSCAD CLI to export STL; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: documented_capability
2. Order: 2; Action: preserve source and unit declaration; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
3. Order: 3; Action: inspect mesh topology and dimensions; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
4. Order: 4; Action: if editable B-rep required, rebuild/import via explicit profile or FreeCAD workflow.; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-15; Name: Render source-defined CSG as a mesh; Inputs: ; Outputs: mesh; Tools: OpenSCAD; STL/3MF mesh export; Source urls: https://openscad.org/documentation; Prerequisites: Provide parametric-source in OpenSCAD syntax and resolve required parameters.; Choose a mesh export format and units; retain the source file as the editable parametric record.; Preserves: OpenSCAD source and its parameterized CSG construction; Changes or infers: Tessellates the evaluated CSG surface into mesh facets; the resulting mesh does not carry editable B-rep feature history.; Checks: Regenerate after changing one source parameter.; Check mesh watertightness, normals, bounds, units and dimensional deviation against the source parameters.; Alternatives: Use FreeCAD/build123d/CadQuery for a B-rep output requirement.; Automation: scripted; Evidence status: documented_capability; Summary: OpenSCAD documents source-defined constructive solid geometry and mesh export. This operation guarantees mesh output, not a CAD B-rep.; Input alternatives: parametric-source
2. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: README.md (`${OCS_ROOT}/docs/automation/README.md`); step.rs (`${OCS_ROOT}/src/io/step.rs`); SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Documented third-party tool and API entry points

1. Entrypoint: `openscad -o output.stl source.scad; inspect STL bounds/components; retain .scad and declared units`; Status: existing_tool_entrypoint; Source urls: https://openscad.org/documentation.html; API-SPEC.md (`${OCS_ROOT}/docs/automation/API-SPEC.md`); Notes: Documented application/API workflow. Human review steps remain manual; command/runtime not exercised in this research.

## Output artifacts

1. **Representations:** mesh; measurement-set
2. **Editable source:** Preserve input source and native CAD source where generated; neutral mesh/STEP does not retain upstream feature semantics.
3. **Preserves:** original inputs; declared units and datum; reviewed measurements/provenance
4. **Loss or inference:** occluded or hidden geometry requires explicit inference; representation conversion may discard feature history or unit metadata

## Checks

1. Object: OpenSCAD export; Quantity: mesh watertightness/components and source bounds; Unit: declared source units; Acceptance: mesh parses and dimensions match explicit source-derived checks; Method: OpenSCAD render/export; inspect mesh and compare bounds to source parameters.

## Failure recovery

1. Failure: Scale, topology or registration mismatch; Recovery: Stop downstream export; preserve source; recheck units/datums and rerun only the affected stage.
2. Failure: Ambiguous hidden feature or weak evidence; Recovery: Mark as unresolved candidate; request a new measurement/view or retain parameter range.

## Effort and computing classification

1. **Human:** 1
2. **Setup:** 1
3. **Compute:** 2
4. **Human reason:** Source describes constructive geometry, but mesh review and any B-rep conversion require checks.
5. **Setup reason:** OpenSCAD executable plus mesh reader.
6. **Compute reason:** Small model CPU; CGAL Boolean complexity and mesh resolution drive cost, no GPU.

## Resources and scaling

1. **Cpu:** Small model CPU; CGAL Boolean complexity and mesh resolution drive cost, no GPU.
2. **Gpu:** CPU geometry baseline; graphics display acceleration is separate.
3. **Ram:** Scales with CSG Boolean complexity, subdivision and triangles.
4. **Storage:** Preserve SCAD/includes, parameter set and mesh.
5. **Scaling drivers:** CSG Boolean complexity, subdivision and triangles
6. **Variants:** Small valid SCAD baseline; high tessellation and complex CSG increase CPU/RAM.

## Original sources

1. [https://openscad.org/documentation.html](https://openscad.org/documentation.html)
2. ${OCS_ROOT}/docs/automation/API-SPEC.md (`${OCS_ROOT}/docs/automation/API-SPEC.md`)

Full source summaries: [source register](../../sources/source-register.md).
