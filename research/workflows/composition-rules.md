# Workflow composition rules

Status: proposed rules for composing the registered operations. Original project rationale: the user requested individual and combined workflows on 12 November 2026. The domain reports link each underlying software capability to its original documentation or paper.

## 1. Operation contract

An operation consumes named artifacts and produces new artifacts. Record both their representation and their evidence/geometry properties. A `point-cloud` label describes a representation; scale, frame, sampled region and measurement provenance determine the uses supported by that particular cloud.

Required contract fields:

1. Input artifacts and their roles: source/target clouds, source drawing, control measurements, camera calibration, native model or selected component.
2. Output artifacts and their roles: estimated camera poses, registered reference, candidate feature parameters, native CAD, visual mesh, collider, semantic building or robot description.
3. Tool/API and version; original source link and summary; evidence status.
4. Prerequisites: calibration, input rights, compatible file/version, selected datum, sufficient geometry or a required feature interpretation.
5. Information preserved, transformed, inferred or discarded, including identifiers, units, frames, topology, semantic relations and feature history.
6. Numerical, geometric and consumer checks tied to the produced revision.

`inputs` contains requirements that apply together. `input_alternatives`, where present, contains complete alternative sets; one complete set must also be available. `input_choice_groups` expresses several independent choices, each of which requires one complete alternative set. Named roles distinguish two inputs of the same representation. An output listed as optional requires its own conditions and downstream check.

## 2. Composition forms

1. **Sequence:** one operation's output becomes a later operation's input. Example: vector-drawing intake → constrained sketch → native CAD → a checked solid derivative.
2. **Branch:** one input feeds different analyses. Example: photographs feed camera-pose estimation and a visual reconstruction; both retain the original image references.
3. **Evidence merge:** different observations constrain the same feature. Example: a drawing supplies bore diameter while a scan supplies mounting-plane orientation. Record correspondence, source values, transforms and residuals at feature level.
4. **Geometry assembly:** identified components become occurrences in an assembly through named interface frames. The source component and occurrence transform have separate revisions.
5. **Component substitution:** replace an inferred or authored component with a specifically identified library component. Compare interfaces and revise dependent placements; retain the previous candidate and source evidence.
6. **Representation fork:** derive visual, collision, fabrication or semantic artifacts from one source revision. Each derivative has a role-specific tool, settings and checks.
7. **Edit and compare:** annotate an existing view/model, resolve the annotation to geometry and intent, create a changed native revision, and compare the changed features against retained source evidence.
8. **Refinement loop:** change one declared reconstruction/modeling parameter after a failed check, preserve the run, and compare results using the same controls. Iterate under a named objective and stop condition.
9. **Alternative routes:** retain multiple methods for the same target. Compare them using the same supplied dimensions, independent controls and output consumer.

## 3. Handoff conditions

1. **Units and frames:** store the source and target conventions, numerical conversion factor, transform direction, axes and origin. Camera-to-world and world-to-camera are explicit alternatives. Register georeferenced coordinates separately from local modeling coordinates.
2. **Geometry:** identify analytic faces, mesh triangles, point samples, Gaussian/radiance representations or semantic objects. Check the actual exported representation and the receiving tool's supported subset.
3. **Identity:** retain source component IDs and revision hashes; record any many-to-one fusion or one-to-many decomposition. An occurrence's transform belongs to the assembly.
4. **Dimensional evidence:** identify dimensions supplied by measurement, drawings, manufacturer data, reconstruction fitting or inference. Controls used to fit scale/pose and independent assessment controls have separate roles.
5. **Semantics:** retain native IFC relationships or robot joints/frames when a display representation is produced. Add or revise semantic interpretation through a recorded operation.
6. **Physical properties:** mass, centre of mass, inertia and material properties carry their own units, frames and sources. A geometric or visual derivative inherits only explicitly mapped physical data.
7. **Licences and provenance:** each source asset, tool, model weight and derivative references its actual terms and source record. A catalogue entry links to the component's original record.
8. **Version and checks:** a documented transition becomes an exercised transition only after the actual tool versions, input/output hashes and checks are recorded for that run.

## 4. Combination coverage

The operation graph represents reusable transitions; recipes describe named applications of those transitions. Branches and loops allow additional combinations without duplicating their component definitions. Record each newly proposed route with its own input roles, objective and handoff conditions, then link it to existing operations. When a requested step needs a new representation or tool capability, add a source-backed operation and its check instead of treating a matching file extension as a completed transition.

Research questions retained for later experiments:

1. Which shared transform/anchor record preserves image pixels, CAD datums, scan coordinates and component IDs across the named tools?
2. Which reconstruction features can be converted into editable CAD operations with a reproducible source-to-feature association?
3. Which exported fields survive each actual OCS, FreeCAD, Blender, IFC and robot importer/exporter version?
4. Which numerical checks detect a semantically incorrect but internally consistent model built from ambiguous views?
5. Which branch should be recomputed after one input measurement, component revision or interpretation changes?

These questions extend the source-linked CAD, reconstruction and domain idea records. The existing implementation plan retains its stage sequence; the research map supplies the route alternatives and experiment questions for those stages.
