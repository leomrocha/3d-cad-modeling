# CAD-R04 — Clean DXF or SVG profile to editable extrusion

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 2/5; setup 2/5; computing 1/5.**

Output: cad-solid + parametric-source

## Comparison conditions

One bounded input artifact set with the stated minimum quality; no unmeasured dimensions are promoted to fact. Ratings compare complete workflow under current contract scales.

## Registered starting artifact types

1. vector-drawing
2. dimensions
3. model-brief

## Detailed source and preparation artifacts

1. Artifact: vector-drawing; Format: DXF or SVG with registered orthographic views where required; Requirement: selected closed profile, layer, scale, extrusion; Quality: Readable/registered input with explicit units and known provenance.; Provenance: Keep original unchanged; record measurements and source page/frame.

## Reference points, datums and coordinate frames

1. **Datum:** Explicitly selected datum/control origin before reconstruction
2. **Axes:** Record coordinate frame, projection and handedness in the project units
3. **Controls:** selected closed profile, layer, scale, extrusion
4. **Unit:** Explicit source units; normalize to mm only with documented scale

## Software, libraries and dependencies

1. Name: CadQuery; Role: CadQuery importexport; License: Apache-2.0.; Apis: cq.importers.importDXF(filename,tol=...,include=[layer]); imported.wires().vals(); Wire.Closed()/isValid(); cq.Matrix(scale); Wire.transformGeometry; Workplane.newObject([wire]).wires().toPending().extrude(height); Shape.isValid/BoundingBox/Volume; Workplane.solids().size(); export(unit="MM",outputUnit="MM"); importers.importStep; Dependencies: Python CadQuery, OCP Python bindings and OCCT; DXF unit/layer inspection additionally uses ezdxf.; Source urls: https://cadquery.readthedocs.io/en/stable/importexport.html; https://ezdxf.readthedocs.io/en/stable/concepts/units.html
2. Name: ezdxf; Role: ezdxf units; License: MIT.; Apis: ezdxf.readfile(path); doc.header["$INSUNITS"]; doc.modelspace().query("*") and entity.dxf.layer; Dependencies: Python 3 and ezdxf; importer reference combines it with CadQuery/OCP.; Source urls: https://ezdxf.readthedocs.io/en/stable/concepts/units.html; https://github.com/mozman/ezdxf
3. Name: FreeCAD; Role: FreeCAD Draft SVG importer; License: LGPL-2.1-or-later per project licensing page.; Apis: FreeCAD Python console/macros; App.newDocument; Sketcher::SketchObject.addGeometry/addConstraint; Part::Feature.Shape or PartDesign::Body/Feature for solids; ViewPart/TechDraw orthographic projection; import/export via Draft/Part; Dependencies: FreeCAD application with bundled Python, Sketcher, Part and (for assemblies) chosen Assembly workbench; system Python generally cannot import FreeCAD modules.; Source urls: https://cadquery.readthedocs.io/en/stable/importexport.html; https://ezdxf.readthedocs.io/en/stable/concepts/units.html

## Procedure

1. Order: 1; Action: Inspect DXF units/layers; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: documented_capability
2. Order: 2; Action: select one closed profile; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
3. Order: 3; Action: apply confirmed scale; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
4. Order: 4; Action: extrude in CadQuery; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
5. Order: 5; Action: check validity and STEP readback.; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-08; Name: Read and clean vector drawing geometry; Inputs: vector-drawing; Outputs: vector-drawing; Tools: OpenCADStudio DWG/DXF/MCP; FreeCAD Draft DXF/SVG import; ezdxf; geometry audit; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md; https://ezdxf.readthedocs.io/en/stable/; README.md (`${OCS_ROOT}/docs/automation/README.md`); README.md (`${OCS_ROOT}/README.md`); Prerequisites: Preserve source file and hash.; Determine drawing units, model/paper space, layer selection, block transforms, origin and target sketch plane.; Read DXF/SVG import option and unsupported entity behavior.; Preserves: Original file; Entity types, layers, blocks, annotations and source coordinates where supported; Changes or infers: Selects profile entities, normalizes transforms and may join, discretize, or repair curves.; Checks: Count input/output entities by type and layer.; Find duplicate/open/self-intersecting edges.; Compare profile bounds, area and source dimensions.; For SVG, verify viewBox and physical scale; FreeCAD importer flattens Z.; Alternatives: Use the source DXF unchanged in OCS; Use FreeCAD native DXF or legacy importer; Parse DXF with ezdxf and build clean geometry separately; Automation: mixed; Evidence status: documented_capability; Summary: FreeCAD documents DXF/SVG entity coverage and import modes; ezdxf reads and writes DXF. Entity preservation and scale depend on the specific importer/settings.
2. Id: CAD-09; Name: Build and constrain an editable planar sketch; Inputs: vector-drawing; Outputs: constrained-sketch; Tools: FreeCAD Sketcher scripting; FreeCAD Draft-to-Sketch; OpenCADStudio sketch/constraint capability as discovered in session; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md; SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`); Prerequisites: Specify units, support plane and datum.; Resolve profile closure/repair and record which source curves changed.; Associate each dimensional constraint with measured/source/inferred status.; Preserves: 2D profile geometry; Named dimensions and geometric constraints; Constraint provenance in the project evidence ledger; Changes or infers: Adds constraints and may alter underconstrained geometry to satisfy them.; Checks: Solver state/degrees of freedom; Residuals and overconstraints; Source-to-constraint numeric comparison; Profile closedness and intersections; Alternatives: Keep vector geometry as non-parametric Draft/OCS drawing entities; Generate sketch geometry from code-CAD source; Automation: mixed; Evidence status: documented_capability; Summary: FreeCAD documents Python creation of Sketcher geometry and constraints. Solver success tests consistency, not the truth of supplied or inferred measurements.; Input alternatives: model-brief; dimensions; measurement-set
3. Id: CAD-10; Name: Create a kernel solid and native model document from confirmed parameters; Inputs: ; Outputs: cad-solid; native-model-document; Tools: OpenCADStudio kernel tools; FreeCAD PartDesign/Part; build123d; CadQuery; Source urls: https://build123d.readthedocs.io/en/latest/operations.html; https://cadquery.readthedocs.io/en/stable/; https://openscad.org/documentation; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md; cadkernel-body-path.md (`${OCS_ROOT}/docs/cadkernel-body-path.md`); Prerequisites: Declare units, feature parameters, direction/axis and part boundary.; Use exact B-rep backend if exact surfaces/export are required.; Preserve native feature document or code source.; Preserves: Input dimensions and feature parameters; Native feature tree or executable parametric source; Part names and component boundaries; Editable native model document; feature history depends on the selected CAD application; Changes or infers: Creates exact kernel geometry from the confirmed profile/feature instructions; unsupported features may require alternatives.; Checks: Kernel shape validity and solid count; Bounds, volume, hole/shaft dimensions and units; Recompute or regenerate after one parameter change; Save/reopen and independent import; Alternatives: FreeCAD feature-history model; build123d/CadQuery Python source; OCS native body; separate exact STEP exporter if needed; Automation: scripted; Evidence status: documented_capability; Summary: Build kernel CAD solids from a confirmed constrained sketch, parametric source, or explicit model brief plus dimensions. FreeCAD/build123d/CadQuery provide documented B-rep routes; OCS creates native geometry but its inspected STEP writer emits mesh-derived faceted STEP.; Input alternatives: constrained-sketch; parametric-source; model-brief; dimensions
4. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: README.md (`${OCS_ROOT}/docs/automation/README.md`); step.rs (`${OCS_ROOT}/src/io/step.rs`); SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Entrypoint: `Read DXF units/layers with ezdxf; use CadQuery importers.importDXF with explicit include layers and merge tolerance; select closed wires with wires().toPending(), apply confirmed scale and extrude with the required length. Inspect resulting topology and STEP readback. SVG uses the separately documented FreeCAD import route.`; Source urls: https://cadquery.readthedocs.io/en/stable/importexport.html; https://ezdxf.readthedocs.io/en/stable/concepts/units.html

## Output artifacts

1. **Representations:** cad-solid; parametric-source
2. **Editable source:** Preserve input source and native CAD source where generated; neutral mesh/STEP does not retain upstream feature semantics.
3. **Preserves:** original inputs; declared units and datum; reviewed measurements/provenance
4. **Loss or inference:** occluded or hidden geometry requires explicit inference; representation conversion may discard feature history or unit metadata

## Checks

1. Object: DXF extrusion; Quantity: closed loops, XY bounds and Z height; Unit: mm; Acceptance: one selected closed wire; solid valid; Z equals supplied height; Method: CadQuery isValid/Closed/solids/BBox and STEP reread.

## Failure recovery

1. Failure: Scale, topology or registration mismatch; Recovery: Stop downstream export; preserve source; recheck units/datums and rerun only the affected stage.
2. Failure: Ambiguous hidden feature or weak evidence; Recovery: Mark as unresolved candidate; request a new measurement/view or retain parameter range.

## Effort and computing classification

1. **Human:** 2
2. **Setup:** 2
3. **Compute:** 1
4. **Human reason:** Clean contours need little interpretation; choosing loops and extrusion still needs explicit values.
5. **Setup reason:** One CAD library plus importer dependency.
6. **Compute reason:** Small CPU topology and extrusion; nested loops increase review.

## Resources and scaling

1. **Cpu:** Small CPU topology and extrusion; nested loops increase review.
2. **Gpu:** CPU geometry baseline; graphics display acceleration is separate.
3. **Ram:** Scales with profile edges, nested contours and Boolean topology.
4. **Storage:** Preserve DXF/SVG, parameters, generator and STEP.
5. **Scaling drivers:** profile edges, nested contours and Boolean topology
6. **Variants:** Single closed wire in the single-profile baseline; assign holes/multiple regions explicitly for richer profiles.

## Original sources

1. [https://cadquery.readthedocs.io/en/stable/importexport.html](https://cadquery.readthedocs.io/en/stable/importexport.html)
2. [https://ezdxf.readthedocs.io/en/stable/concepts/units.html](https://ezdxf.readthedocs.io/en/stable/concepts/units.html)
3. [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md)

Full source summaries: [source register](../../sources/source-register.md).
