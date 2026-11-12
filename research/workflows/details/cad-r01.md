# CAD-R01 — Text and explicit dimensions to an editable engineering part

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 2/5; setup 2/5; computing 1/5.**

Output: One parameterized mechanical solid, editable native source and verified STEP derivative.

## Comparison conditions

One simple engineering part with explicit dimensions and unambiguous feature intent; a small B-rep and recorded units/datums. OCS is the existing baseline; FreeCAD and CadQuery are documented alternatives.

## Registered starting artifact types

1. text
2. dimensions

## Detailed source and preparation artifacts

1. Artifact: text; Format: plain text/Markdown; Requirement: Part identity, feature intent and output scope.; Quality: Names features; no conflicting instructions.; Provenance: Retain exact source lines/page.
2. Artifact: dimensions; Format: table or JSON; Requirement: Length, width, thickness, hole centres/diameters with units.; Quality: Every value positive and explicit; no prose-derived dimensions.; Provenance: Each value points to measurement/drawing/declared design decision.

## Reference points, datums and coordinate frames

1. **Datum:** plate centre at bottom face
2. **Origin:** (0,0,0) mm
3. **Axes:** X length; Y width; +Z thickness
4. **Controls:** hole x/y from centre datum
5. **Unit:** mm

## Software, libraries and dependencies

1. Name: OpenCADStudio; Role: Project baseline: native drawing/solid geometry controlled through editor/MCP; installed skill supplies geometry contract, readback and save rules. Inspected sources establish Solid3D/ACIS and mesh schemas, not general parametric feature history.; License: GPL-3.0 (local LICENSE file).; Apis: OpenCADStudio --mcp; ocs_control.py discover/read; ocs_execute after inspecting command schema; ocs_read geometry/entity records; Dependencies: OpenCADStudio desktop build with MCP enabled; Python 3 helper plus local session credentials/config.; Source urls: [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); [API-SPEC.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md); [LICENSE](/home/leo/projects/3rdparty/OpenCADStudio/LICENSE)
2. Name: CadQuery; Role: Parameter-driven Python model using OCCT B-rep; STEP is geometry exchange, Python source is the parametric record.; License: Apache-2.0.; Apis: Workplane sketch operations, extrude and cut; Shape.isValid, BoundingBox and Volume; STEP export and importers.importStep; Dependencies: Python CadQuery, OCP Python bindings and OCCT; DXF unit/layer inspection additionally uses ezdxf.; Source urls: https://cadquery.readthedocs.io/en/stable/importexport.html; https://cadquery.readthedocs.io/en/stable/classreference.html; https://cadquery.readthedocs.io/en/stable/quickstart.html; https://github.com/CadQuery/cadquery/blob/master/LICENSE
3. Name: FreeCAD; Role: Complementary native feature-history and constrained-sketch backend.; License: LGPL-2.1-or-later per project licensing page.; Apis: FreeCAD Python console/macros; App.newDocument; Sketcher::SketchObject.addGeometry/addConstraint; Part::Feature.Shape or PartDesign::Body/Feature for solids; ViewPart/TechDraw orthographic projection; import/export via Draft/Part; Dependencies: FreeCAD application with bundled Python, Sketcher, Part and (for assemblies) chosen Assembly workbench; system Python generally cannot import FreeCAD modules.; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md; https://www.freecad.org/contributing.php?lang=eng

## Procedure

1. Order: 1; Action: Create a source-linked model brief and separate supplied/measured/inferred/assumed values.; Tool or command: Existing ocs-engineering skill and human review; Human review: Resolve contradictions before geometry.; Status: proposed_composition
2. Order: 2; Action: Inspect current OCS session, document units and schema before any authorized edit.; Tool or command: ocs_control.py discover/read; no write in this batch; Human review: Keep session tokens private.; Status: local_source_inspected
3. Order: 3; Action: Choose OCS baseline, FreeCAD for feature history, or CadQuery source for reproducible parameterized B-rep.; Tool or command: CAD backend; Human review: Backend choice follows required native artifact.; Status: proposed_composition
4. Order: 4; Action: Construct the confirmed sketch/features in OCS or FreeCAD, or use documented CadQuery Workplane operations; inspect geometry and STEP readback.; Tool or command: OCS/FreeCAD native features or CadQuery Workplane API; Human review: Check feature-to-parameter mapping.; Status: proposed_composition
5. Order: 5; Action: Reopen STEP independently and compare dimensions and solid count.; Tool or command: FreeCAD/OCS import; Human review: Check units and source ledger.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-01; Name: Extract a model brief from text and dimensions; Inputs: ; Outputs: model-brief; Tools: model brief schema; human review; OCS engineering skill; Source urls: [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); Prerequisites: Identify each value as supplied, measured, inferred, assumed, or calculated.; Declare units, origin, axes, component boundaries, intended output and source links.; Preserves: Original text; Value-to-source associations; Author's unresolved choices; Changes or infers: Groups explicit requirements into named parameters and geometry constraints.; Does not infer hidden geometry from prose alone.; Checks: Every numerical parameter has units and provenance.; Ambiguities affecting geometry are listed separately.; Alternatives: Direct interactive OCS modeling after brief readback; Code-CAD generation from a validated brief; Automation: assisted; Evidence status: proposed_composition; Summary: Create a source-linked brief before changing geometry; keep source claims separate from constraints and design choices.; Input alternatives: text; dimensions; text; dimensions
2. Id: CAD-10; Name: Create a kernel solid and native model document from confirmed parameters; Inputs: ; Outputs: cad-solid; native-model-document; Tools: OpenCADStudio kernel tools; FreeCAD PartDesign/Part; build123d; CadQuery; Source urls: https://build123d.readthedocs.io/en/latest/operations.html; https://cadquery.readthedocs.io/en/stable/; https://openscad.org/documentation; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md; [cadkernel-body-path.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md); Prerequisites: Declare units, feature parameters, direction/axis and part boundary.; Use exact B-rep backend if exact surfaces/export are required.; Preserve native feature document or code source.; Preserves: Input dimensions and feature parameters; Native feature tree or executable parametric source; Part names and component boundaries; Editable native model document; feature history depends on the selected CAD application; Changes or infers: Creates exact kernel geometry from the confirmed profile/feature instructions; unsupported features may require alternatives.; Checks: Kernel shape validity and solid count; Bounds, volume, hole/shaft dimensions and units; Recompute or regenerate after one parameter change; Save/reopen and independent import; Alternatives: FreeCAD feature-history model; build123d/CadQuery Python source; OCS native body; separate exact STEP exporter if needed; Automation: scripted; Evidence status: documented_capability; Summary: Build kernel CAD solids from a confirmed constrained sketch, parametric source, or explicit model brief plus dimensions. FreeCAD/build123d/CadQuery provide documented B-rep routes; OCS creates native geometry but its inspected STEP writer emits mesh-derived faceted STEP.; Input alternatives: constrained-sketch; parametric-source; model-brief; dimensions
3. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: [README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md); [step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs); [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Entrypoint: `CadQuery Workplane sketch operations, extrude and cut; inspect Shape.isValid, BoundingBox and Volume; use STEP export and importers.importStep for exchange readback. Preserve Python parameters or native CAD construction intent separately.`; Source urls: https://cadquery.readthedocs.io/en/stable/quickstart.html; https://cadquery.readthedocs.io/en/stable/classreference.html; https://cadquery.readthedocs.io/en/stable/importexport.html
2. Entrypoint: `python /home/leo/.codex/skills/ocs-engineering/scripts/ocs_control.py discover; read state/capabilities/commands using helper contract`; Status: existing_tool_entrypoint; Source urls: [ocs-control.md](/home/leo/.codex/skills/ocs-engineering/references/ocs-control.md); [API-SPEC.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md); Notes: Read-only command entrypoint observed in local skill sources; no OCS command run.; Path: [ocs_control.py](/home/leo/.codex/skills/ocs-engineering/scripts/ocs_control.py)

## Output artifacts

1. **Representations:** cad-solid; native-model-document; parametric-source; STEP
2. **Editable source:** CadQuery .py plus dimensions JSON, OCS native document, or FreeCAD feature-history document; STEP is neutral exchange geometry.
3. **Preserves:** source text and value provenance; units/datum; feature parameter names
4. **Loss or inference:** feature topology remains a modeling interpretation; STEP is exchange geometry; hidden dimensions stay unresolved variables

## Checks

1. Object: solid; Quantity: validity/solid count; Unit: boolean/count; Acceptance: isValid and exactly one solid for the single-part baseline; Method: CadQuery Shape.isValid/Workplane.solids; independent reader.
2. Object: envelope; Quantity: X/Y/Z bounds; Unit: mm; Acceptance: equals explicit dimensions within stated numeric tolerance; Method: Shape.BoundingBox plus source ledger.
3. Object: holes; Quantity: centre and diameter; Unit: mm; Acceptance: match each input, fit within boundary, do not intersect; Method: Compare parameter table to analytic faces.
4. Object: STEP; Quantity: readback unit/bounds/count; Unit: mm/count; Acceptance: valid one-solid output with expected bounds; Method: CadQuery importStep and independent CAD reader.

## Failure recovery

1. Failure: Conflicting dimension or missing unit; Recovery: Stop dependent features; retain both values and record the exact conflict in model brief.
2. Failure: Stale/unknown OCS schema; Recovery: Refresh read-only state/schema; do not replay mutation with unknown completion.
3. Failure: Invalid CadQuery boolean; Recovery: Inspect hole position/overlap and source inputs; export no replacement.
4. Failure: STEP readback differs; Recovery: Preserve source; compare another B-rep reader and classify exporter/importer mismatch.

## Effort and computing classification

1. **Human:** 2
2. **Setup:** 2
3. **Compute:** 1
4. **Human reason:** Parameter mapping and feature intent still require checking.
5. **Setup reason:** CadQuery needs Python/OCP; OCS branch uses existing application; FreeCAD branch uses app Python.
6. **Compute reason:** Small analytic part and STEP roundtrip are CPU-light; no GPU.

## Resources and scaling

1. **Cpu:** Low for one small B-rep.
2. **Gpu:** None.
3. **Ram:** Low; scales with Boolean and feature complexity.
4. **Storage:** Small JSON/Python/STEP.
5. **Scaling drivers:** feature count; Boolean complexity; configuration count
6. **Variants:** OCS interactive baseline; FreeCAD native feature tree; CadQuery Python source and B-rep STEP

## Original sources

1. [/home/leo/projects/3dmodeling/research/workflows/cad-paths.json](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json)
2. [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md)
3. [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)
4. [/home/leo/.codex/skills/ocs-engineering/references/ocs-control.md](/home/leo/.codex/skills/ocs-engineering/references/ocs-control.md)
5. [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md)
6. [/home/leo/projects/3rdparty/OpenCADStudio/LICENSE](/home/leo/projects/3rdparty/OpenCADStudio/LICENSE)
7. [https://cadquery.readthedocs.io/en/stable/importexport.html](https://cadquery.readthedocs.io/en/stable/importexport.html)
8. [https://cadquery.readthedocs.io/en/stable/classreference.html](https://cadquery.readthedocs.io/en/stable/classreference.html)
9. [https://cadquery.readthedocs.io/en/stable/quickstart.html](https://cadquery.readthedocs.io/en/stable/quickstart.html)
10. [https://github.com/CadQuery/cadquery/blob/master/LICENSE](https://github.com/CadQuery/cadquery/blob/master/LICENSE)
11. [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md)
12. [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md)
13. [https://www.freecad.org/contributing.php?lang=eng](https://www.freecad.org/contributing.php?lang=eng)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
