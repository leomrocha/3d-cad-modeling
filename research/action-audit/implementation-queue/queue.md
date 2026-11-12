# Ordered implementation queue

Date: 12 November 2026. Status: proposed implementation order. Coordinator: gpt-6.1-sol.

Coverage: 245 distinct action definitions, all 77 operations and 38 original routes. Each entry retains the original action and operation input contracts in [structured queue](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.json).

Reuse evidence and code entry points: [inspected assets](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/assets.md). First task: [Record source files, revisions and job scope](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/first-action-plan.md).

## Ordering and boundaries

1. Satisfy each preceding action dependency, then sort by proposed resource band, proposed implementation effort, descending original-route reuse count and original audited order. The estimates use each action's software/resources text; original route scores/conditions are copied separately into the structured queue. These are qualitative comparisons.
2. An operation can receive existing artifacts satisfying its original inputs. Conditional route predecessors describe those particular routes; the 879 candidate type handoffs are preserved as candidate edges.
3. Bands 0–7 mean source bookkeeping; metadata/reasoning; vector/CAD; raster/video; building/robot/scene; cloud/calibration; dense reconstruction; learned inference/training. Effort bands 1–4 mean bounded bookkeeping; interpretation/configuration; format/geometry/image adapters; multi-system reconstruction/physics.
4. Branch options and merge/selection actions retain their original records. CAD-01 and DOM-01 share ten readable intake actions; INTAKE-A01–A10 are local queue references to those existing headings.
5. A documented capability, inspected code subset, recorded component check and new runtime test are separate evidence categories. Asset links state the covered subset and applicability.

## Queue

| Order | Human-readable action and reference | Resource / effort band | Previous action | Original routes | Reuse evidence |
| ---: | --- | --- | --- | ---: | --- |
| 1 | [Preserve the input revision and state the job boundary (INTAKE-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 0 / 1 | operation inputs | 8 | existing_code_subset |
| 2 | [Bind checks to actual artifacts and source criteria (CAD-13-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 15 | existing_code_subset |
| 3 | [Identify the exact library item and retained files (DOM-06-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 1 / 2 | operation inputs | 11 | existing_code_subset |
| 4 | [Define collision scope and contact features (DOM-13-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 11 | source_supported_action_specification |
| 5 | [Define feature evidence and all required editable outputs (REC-14-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 9 | source_supported_action_specification |
| 6 | [Select the execution mode and define candidate branches (INTAKE-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 1 / 2 | Preserve the input revision and state the job boundary (INTAKE-A01) | 8 | source_supported_action_specification |
| 7 | [Extract source claims and associate each value with its subject (INTAKE-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 1 / 2 | Select the execution mode and define candidate branches (INTAKE-A02) | 8 | documented_procedure_or_case |
| 8 | [Identify components, features and geometric relationships (INTAKE-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 1 / 2 | Extract source claims and associate each value with its subject (INTAKE-A03) | 8 | documented_procedure_or_case |
| 9 | [Normalize explicit quantities, units, datums and frames (INTAKE-A05)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 1 / 2 | Identify components, features and geometric relationships (INTAKE-A04) | 8 | documented_procedure_or_case |
| 10 | [Record per-feature tolerance and evidence requirements (INTAKE-A06)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 1 / 2 | Normalize explicit quantities, units, datums and frames (INTAKE-A05) | 8 | documented_procedure_or_case |
| 11 | [Evaluate candidate briefs against their source evidence (INTAKE-A07)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 1 / 2 | Record per-feature tolerance and evidence requirements (INTAKE-A06) | 8 | documented_procedure_or_case |
| 12 | [Select supported records and merge compatible contributions (INTAKE-A08)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 1 / 2 | Evaluate candidate briefs against their source evidence (INTAKE-A07) | 8 | documented_procedure_or_case |
| 13 | [Validate the merged brief independently (INTAKE-A09)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 1 / 2 | Select supported records and merge compatible contributions (INTAKE-A08) | 8 | documented_procedure_or_case |
| 14 | [Deliver the brief and specify the downstream handoff (INTAKE-A10)](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md) | 1 / 2 | Validate the merged brief independently (INTAKE-A09) | 8 | documented_procedure_or_case |
| 15 | [Bind image identities calibration groups and sparse-solve settings (REC-03-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 8 | source_supported_action_specification |
| 16 | [Freeze comparison baseline and bounded edit scope (REC-16-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 7 | source_supported_action_specification |
| 17 | [Select geometry occurrence and mesh role (DOM-12-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 7 | source_supported_action_specification |
| 18 | [Pin source definitions and assembly roles (CAD-12-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 1 / 2 | operation inputs | 5 | documented_procedure_or_case |
| 19 | [Resolve rigid links from authored assembly relations (DOM-08-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 5 | source_supported_action_specification |
| 20 | [Validate sparse-to-dense image and camera handoff (REC-17-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 5 | source_supported_action_specification |
| 21 | [Classify the component change and identify new bytes (DOM-26-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 1 / 2 | operation inputs | 4 | existing_code_subset |
| 22 | [Select a supported solid feature route (CAD-10-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 4 | documented_procedure_or_case |
| 23 | [Identify plane evidence and independent metric controls (CAD-02-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 1 / 2 | operation inputs | 4 | source_supported_action_specification |
| 24 | [Separate stroke classes and inspect source regions (CAD-04-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 1 / 2 | operation inputs | 4 | source_supported_action_specification |
| 25 | [Select calibrated target observations and hold-out views (REC-01-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 4 | source_supported_action_specification |
| 26 | [Select physical-property evidence per rigid body (DOM-14-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 4 | source_supported_action_specification |
| 27 | [Define IFC-to-display identity and unit policy (DOM-17-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 4 | source_supported_action_specification |
| 28 | [Bind environment to existing robot world frame (DOM-33-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 4 | source_supported_action_specification |
| 29 | [Bind sensor calibration timing and depth encoding (REC-05-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 4 | source_supported_action_specification |
| 30 | [Resolve fusion grid and pose convention (REC-06-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 4 | source_supported_action_specification |
| 31 | [Prepare a Gaussian training dataset with verified camera mapping (REC-19-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 4 | source_supported_action_specification |
| 32 | [Inspect source entities, units and drawing contexts (CAD-08-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 33 | [Map curves and sourced constraints to a sketch plan (CAD-09-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 34 | [Locate annotations and retain crop mappings (CAD-03-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 35 | [Identify views and declare their projection frames (CAD-06-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 36 | [Enumerate source-constrained 3D feature candidates (CAD-07-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 37 | [Select observed regions and preserve point membership (REC-09-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 38 | [Bind exact CAD and observation-route evidence (REC-12-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 39 | [Check literal package inputs and supported URDF tree (DOM-09-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 40 | [Select IFC elements and triangle extraction policy (DOM-16-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 41 | [Resolve scene input branch and actual adapter (DOM-24-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 42 | [Bind library asset and target IFC placement meaning (DOM-35-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 43 | [Resolve literal photo input and cloud detail target (DOM-20-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 3 | source_supported_action_specification |
| 44 | [Declare plan conventions and wall/opening candidates (CAD-05-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 45 | [Bind all five inputs and element-level building requirements (DOM-18-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 46 | [Freeze initialization and comparison objective (REC-08-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 47 | [Verify metric evidence and select functional features (CAD-11-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 48 | [Bind sketch view, camera and hit surface (REC-13-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 49 | [Bind source revisions, datums and discrepancy purpose (REC-15-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 50 | [Resolve scan, building and survey frame definitions (DOM-19-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 51 | [Bind assembly occurrences and motion evidence (DOM-31-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 52 | [Bind sourced component to target robot role (DOM-37-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 53 | [Bind native model roles and compiler policy (DOM-11-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 54 | [Pin seed model and map CAD occurrences to bodies (DOM-32-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 55 | [Bind BIM-derived mesh and collider identities (DOM-34-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 56 | [Bind mandatory depth and measurement evidence (DOM-21-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 57 | [Bind supplied cameras and required surface outputs (DOM-28-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 58 | [Inspect point evidence normals and meshing assumptions (DOM-29-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 2 | source_supported_action_specification |
| 59 | [Resolve source and target interface identities (DOM-07-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 60 | [Inspect STEP identity, structure and unit evidence (DOM-38-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 61 | [Inspect CSG source, parameters and mesh criteria (CAD-15-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 62 | [Choose the profile target and source entity mapping (DOM-03-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 63 | [Define native artifact and solid prerequisites (DOM-04-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 1 | documented_procedure_or_case |
| 64 | [Bind the solid export to representation and consumer criteria (DOM-05-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 65 | [Define sourced parameters and the executable model contract (DOM-40-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 1 | documented_procedure_or_case |
| 66 | [Bind graph elements to sourced vertical parameters (CAD-17-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 67 | [Specify raster-backed sketch requirements (DOM-02-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 68 | [Bind both clouds and declare transform freedoms (REC-07-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 69 | [Audit literal input contract and target remodeling meaning (DOM-23-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 70 | [Inventory URDF import policy and expected losses (DOM-10-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 71 | [Resolve building schema units hierarchy and element evidence (DOM-15-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 72 | [Resolve IFC kernel shape extraction requirements (DOM-27-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 73 | [Bind model revision to fabrication requirements (DOM-25-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 74 | [Inventory video timing camera state and coverage (REC-04-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 75 | [Bind complete photo and metric-control contract (CAD-16-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 76 | [Bind learned reconstruction variant, images and camera roles (REC-10-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 77 | [Select one source image and a mesh-producing model contract (REC-18-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 1 | source_supported_action_specification |
| 78 | [Freeze the native assembly and export contract (DOM-39-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 1 / 2 | operation inputs | 0 | documented_procedure_or_case |
| 79 | [Reconcile the failed operation and preserve its evidence (CAD-14-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 1 / 2 | operation inputs | 0 | existing_component_code_subset |
| 80 | [Bind photographs, target evidence and camera state (CAD-02B-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 0 | source_supported_action_specification |
| 81 | [Bind 3D landmarks to calibrated image coordinates (REC-02-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 1 / 2 | operation inputs | 0 | source_supported_action_specification |
| 82 | [Bind NeRF method, supplied cameras and training-space transforms (REC-20-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 0 | source_supported_action_specification |
| 83 | [Choose the actual renderable scene subtype and consumer (REC-11-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 0 | source_supported_action_specification |
| 84 | [Bind the domain Gaussian scene contract (DOM-22-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 0 | source_supported_action_specification |
| 85 | [Bind domain features and cameras to the NeRF route (DOM-30-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 1 / 2 | operation inputs | 0 | source_supported_action_specification |
| 86 | [Read actual geometry and compare required features (CAD-13-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Bind checks to actual artifacts and source criteria (CAD-13-A01) | 15 | existing_component_code_subset |
| 87 | [Reopen saved artifacts and issue the verification report (CAD-13-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Read actual geometry and compare required features (CAD-13-A02) | 15 | existing_component_code_subset |
| 88 | [Attach item-level terms and permitted operations (DOM-06-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Identify the exact library item and retained files (DOM-06-A01) | 11 | source_supported_action_specification |
| 89 | [Classify component representations and interface evidence (DOM-06-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Attach item-level terms and permitted operations (DOM-06-A02) | 11 | documented_procedure_or_case |
| 90 | [Register the component record and handoff conditions (DOM-06-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Classify component representations and interface evidence (DOM-06-A03) | 11 | documented_procedure_or_case |
| 91 | [Define interface frames and placement relations (CAD-12-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Pin source definitions and assembly roles (CAD-12-A01) | 5 | existing_code_subset |
| 92 | [Create bounded native occurrences (CAD-12-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Define interface frames and placement relations (CAD-12-A02) | 5 | source_supported_action_specification |
| 93 | [Validate and preserve assembly structure (CAD-12-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Create bounded native occurrences (CAD-12-A03) | 5 | documented_procedure_or_case |
| 94 | [Resolve the complete dependency and rights set (DOM-26-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Classify the component change and identify new bytes (DOM-26-A01) | 4 | documented_procedure_or_case |
| 95 | [Publish a new immutable revision and explicit reuse pins (DOM-26-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Resolve the complete dependency and rights set (DOM-26-A02) | 4 | documented_procedure_or_case |
| 96 | [Reopen pinned artifacts and check reuse reproducibility (DOM-26-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Publish a new immutable revision and explicit reuse pins (DOM-26-A03) | 4 | documented_procedure_or_case |
| 97 | [Construct features with revision-bound readback (CAD-10-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Select a supported solid feature route (CAD-10-A01) | 4 | existing_component_code_subset |
| 98 | [Verify native solid and saved construction record (CAD-10-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Construct features with revision-bound readback (CAD-10-A02) | 4 | existing_component_code_subset |
| 99 | [Create a mapped and explicitly cleaned derivative (CAD-08-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Inspect source entities, units and drawing contexts (CAD-08-A01) | 3 | existing_component_code_subset |
| 100 | [Validate curve fidelity and publish the vector handoff (CAD-08-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Create a mapped and explicitly cleaned derivative (CAD-08-A02) | 3 | existing_component_code_subset |
| 101 | [Create the sketch and solve bounded constraint groups (CAD-09-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Map curves and sourced constraints to a sketch plan (CAD-09-A01) | 3 | source_supported_action_specification |
| 102 | [Measure and reopen the constrained sketch (CAD-09-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Create the sketch and solve bounded constraint groups (CAD-09-A02) | 3 | source_supported_action_specification |
| 103 | [Compute the occurrence transform (DOM-07-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Resolve source and target interface identities (DOM-07-A01) | 1 | existing_code_subset |
| 104 | [Insert the component occurrence and connection edge (DOM-07-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Compute the occurrence transform (DOM-07-A02) | 1 | source_supported_action_specification |
| 105 | [Measure placed interfaces and preserve the result (DOM-07-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Insert the component occurrence and connection edge (DOM-07-A03) | 1 | existing_code_subset |
| 106 | [Choose and configure an isolated importer (DOM-38-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Inspect STEP identity, structure and unit evidence (DOM-38-A01) | 1 | documented_procedure_or_case |
| 107 | [Transfer geometry and classify actual output (DOM-38-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Choose and configure an isolated importer (DOM-38-A02) | 1 | documented_procedure_or_case |
| 108 | [Measure and independently reopen imported geometry (DOM-38-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Transfer geometry and classify actual output (DOM-38-A03) | 1 | documented_procedure_or_case |
| 109 | [Evaluate final CSG and export the mesh derivative (CAD-15-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Inspect CSG source, parameters and mesh criteria (CAD-15-A01) | 1 | source_supported_action_specification |
| 110 | [Measure the mesh and check declared parametric behavior (CAD-15-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Evaluate final CSG and export the mesh derivative (CAD-15-A02) | 1 | source_supported_action_specification |
| 111 | [Normalize curves and construct the constrained profile (DOM-03-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Choose the profile target and source entity mapping (DOM-03-A01) | 1 | source_supported_action_specification |
| 112 | [Verify profile semantics and constrained editability (DOM-03-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Normalize curves and construct the constrained profile (DOM-03-A02) | 1 | source_supported_action_specification |
| 113 | [Construct or reuse the checked native body (DOM-04-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Define native artifact and solid prerequisites (DOM-04-A01) | 1 | existing_component_code_subset |
| 114 | [Save and validate the native model contract (DOM-04-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Construct or reuse the checked native body (DOM-04-A02) | 1 | existing_component_code_subset |
| 115 | [Write a separate STEP derivative with actual settings (DOM-05-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Bind the solid export to representation and consumer criteria (DOM-05-A01) | 1 | source_supported_action_specification |
| 116 | [Reopen STEP and compare critical geometry (DOM-05-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Write a separate STEP derivative with actual settings (DOM-05-A02) | 1 | source_supported_action_specification |
| 117 | [Author readable parametric source with stable feature references (DOM-40-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Define sourced parameters and the executable model contract (DOM-40-A01) | 1 | existing_component_code_subset |
| 118 | [Generate geometry in the declared environment (DOM-40-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Author readable parametric source with stable feature references (DOM-40-A02) | 1 | existing_component_code_subset |
| 119 | [Validate generated geometry and a supplied parameter variant (DOM-40-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Generate geometry in the declared environment (DOM-40-A03) | 1 | existing_component_code_subset |
| 120 | [Select the assembly-aware exporter and settings (DOM-39-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Freeze the native assembly and export contract (DOM-39-A01) | 0 | source_supported_action_specification |
| 121 | [Write the STEP derivative and preservation mapping (DOM-39-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Select the assembly-aware exporter and settings (DOM-39-A02) | 0 | source_supported_action_specification |
| 122 | [Reopen and compare the exported assembly (DOM-39-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json) | 2 / 3 | Write the STEP derivative and preservation mapping (DOM-39-A03) | 0 | source_supported_action_specification |
| 123 | [Diagnose the earliest invalid source-to-geometry transition (CAD-14-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Reconcile the failed operation and preserve its evidence (CAD-14-A01) | 0 | documented_procedure_or_case |
| 124 | [Revise the brief and issue a bounded retry plan (CAD-14-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) | 2 / 3 | Diagnose the earliest invalid source-to-geometry transition (CAD-14-A02) | 0 | documented_procedure_or_case |
| 125 | [Estimate plane mapping and rectified derivative (CAD-02-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Identify plane evidence and independent metric controls (CAD-02-A01) | 4 | source_supported_action_specification |
| 126 | [Check independent controls and publish measurements (CAD-02-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Estimate plane mapping and rectified derivative (CAD-02-A02) | 4 | source_supported_action_specification |
| 127 | [Fit source-supported vector candidates (CAD-04-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Separate stroke classes and inspect source regions (CAD-04-A01) | 4 | source_supported_action_specification |
| 128 | [Check geometry and publish vector evidence (CAD-04-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Fit source-supported vector candidates (CAD-04-A02) | 4 | source_supported_action_specification |
| 129 | [Recognize glyphs and parse engineering notation (CAD-03-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Locate annotations and retain crop mappings (CAD-03-A01) | 3 | source_supported_action_specification |
| 130 | [Associate text with geometric features (CAD-03-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Recognize glyphs and parse engineering notation (CAD-03-A02) | 3 | source_supported_action_specification |
| 131 | [Publish reviewed text and association evidence (CAD-03-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Associate text with geometric features (CAD-03-A03) | 3 | source_supported_action_specification |
| 132 | [Match source features and solve registration candidates (CAD-06-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Identify views and declare their projection frames (CAD-06-A01) | 3 | source_supported_action_specification |
| 133 | [Verify registration and publish reconstruction brief (CAD-06-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Match source features and solve registration candidates (CAD-06-A02) | 3 | source_supported_action_specification |
| 134 | [Construct candidate edges and bounded surfaces (CAD-07-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Enumerate source-constrained 3D feature candidates (CAD-07-A01) | 3 | source_supported_action_specification |
| 135 | [Form and inspect the required solid (CAD-07-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Construct candidate edges and bounded surfaces (CAD-07-A02) | 3 | source_supported_action_specification |
| 136 | [Project back to every view and publish checked geometry (CAD-07-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Form and inspect the required solid (CAD-07-A03) | 3 | source_supported_action_specification |
| 137 | [Construct dimensioned wall and opening relationships (CAD-05-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Declare plan conventions and wall/opening candidates (CAD-05-A01) | 2 | source_supported_action_specification |
| 138 | [Verify plan graph and publish vector handoff (CAD-05-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Construct dimensioned wall and opening relationships (CAD-05-A02) | 2 | source_supported_action_specification |
| 139 | [Create explicit IFC identity, units and spatial structure (DOM-18-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Bind all five inputs and element-level building requirements (DOM-18-A01) | 2 | source_supported_action_specification |
| 140 | [Author placed wall/opening geometry and host relations (DOM-18-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Create explicit IFC identity, units and spatial structure (DOM-18-A02) | 2 | source_supported_action_specification |
| 141 | [Validate saved IFC geometry and semantics (DOM-18-A04)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Author placed wall/opening geometry and host relations (DOM-18-A03) | 2 | source_supported_action_specification |
| 142 | [Construct walls and opening voids with retained identities (CAD-17-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Bind graph elements to sourced vertical parameters (CAD-17-A01) | 1 | source_supported_action_specification |
| 143 | [Validate plan, elevation and saved assembly (CAD-17-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Construct walls and opening voids with retained identities (CAD-17-A02) | 1 | source_supported_action_specification |
| 144 | [Compose calibrated vectors and source-linked constraints (DOM-02-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Specify raster-backed sketch requirements (DOM-02-A01) | 1 | source_supported_action_specification |
| 145 | [Verify solved geometry and saved editability (DOM-02-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) | 3 / 3 | Compose calibrated vectors and source-linked constraints (DOM-02-A02) | 1 | source_supported_action_specification |
| 146 | [Extract selected frames with reversible timeline mapping (REC-04-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 3 / 4 | Inventory video timing camera state and coverage (REC-04-A01) | 1 | source_supported_action_specification |
| 147 | [Check dataset quality and camera compatibility (REC-04-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 3 / 4 | Extract selected frames with reversible timeline mapping (REC-04-A02) | 1 | source_supported_action_specification |
| 148 | [Generate independently framed convex pieces (DOM-13-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Define collision scope and contact features (DOM-13-A01) | 11 | source_supported_action_specification |
| 149 | [Validate passages and intended contact behavior (DOM-13-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Generate independently framed convex pieces (DOM-13-A02) | 11 | source_supported_action_specification |
| 150 | [Export source-linked mesh assets (DOM-12-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Select geometry occurrence and mesh role (DOM-12-A01) | 7 | source_supported_action_specification |
| 151 | [Compare meshes to source and reopen (DOM-12-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Export source-linked mesh assets (DOM-12-A02) | 7 | source_supported_action_specification |
| 152 | [Build articulated link and joint representation (DOM-08-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Resolve rigid links from authored assembly relations (DOM-08-A01) | 5 | source_supported_action_specification |
| 153 | [Validate robot assembly against measured configurations (DOM-08-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Build articulated link and joint representation (DOM-08-A02) | 5 | source_supported_action_specification |
| 154 | [Calculate and transform sourced mass properties (DOM-14-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Select physical-property evidence per rigid body (DOM-14-A01) | 4 | source_supported_action_specification |
| 155 | [Check admissibility and consumer-specific completeness (DOM-14-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Calculate and transform sourced mass properties (DOM-14-A02) | 4 | source_supported_action_specification |
| 156 | [Write GLB and semantic sidecar (DOM-17-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Define IFC-to-display identity and unit policy (DOM-17-A01) | 4 | source_supported_action_specification |
| 157 | [Reopen scene and compare identity coverage (DOM-17-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Write GLB and semantic sidecar (DOM-17-A02) | 4 | source_supported_action_specification |
| 158 | [Add static geoms with separate visual and collision roles (DOM-33-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Bind environment to existing robot world frame (DOM-33-A01) | 4 | source_supported_action_specification |
| 159 | [Check robot preservation and obstacle contacts (DOM-33-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Add static geoms with separate visual and collision roles (DOM-33-A02) | 4 | source_supported_action_specification |
| 160 | [Serialize links joints and distinct asset origins (DOM-09-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Check literal package inputs and supported URDF tree (DOM-09-A01) | 3 | source_supported_action_specification |
| 161 | [Parse reopen and compare robot poses and physics (DOM-09-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Serialize links joints and distinct asset origins (DOM-09-A02) | 3 | source_supported_action_specification |
| 162 | [Extract triangles with source and transform mapping (DOM-16-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Select IFC elements and triangle extraction policy (DOM-16-A01) | 3 | source_supported_action_specification |
| 163 | [Check element coverage placements and openings (DOM-16-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Extract triangles with source and transform mapping (DOM-16-A02) | 3 | source_supported_action_specification |
| 164 | [Compose source-linked scene objects and cameras (DOM-24-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Resolve scene input branch and actual adapter (DOM-24-A01) | 3 | source_supported_action_specification |
| 165 | [Reopen and inspect scene content numerically and visually (DOM-24-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Compose source-linked scene objects and cameras (DOM-24-A02) | 3 | source_supported_action_specification |
| 166 | [Create placed semantic occurrence with source mapping (DOM-35-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Bind library asset and target IFC placement meaning (DOM-35-A01) | 3 | source_supported_action_specification |
| 167 | [Check new occurrence and preserved IFC relationships (DOM-35-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Create placed semantic occurrence with source mapping (DOM-35-A02) | 3 | source_supported_action_specification |
| 168 | [Author named joint records and graph topology (DOM-31-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Bind assembly occurrences and motion evidence (DOM-31-A01) | 2 | source_supported_action_specification |
| 169 | [Check reference and moved configurations (DOM-31-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Author named joint records and graph topology (DOM-31-A02) | 2 | source_supported_action_specification |
| 170 | [Create separate occurrence and authored joint relation (DOM-37-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Bind sourced component to target robot role (DOM-37-A01) | 2 | source_supported_action_specification |
| 171 | [Validate attachment and publish three outputs (DOM-37-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Create separate occurrence and authored joint relation (DOM-37-A02) | 2 | source_supported_action_specification |
| 172 | [Author body tree geoms and explicit closure constraints (DOM-11-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Bind native model roles and compiler policy (DOM-11-A01) | 2 | source_supported_action_specification |
| 173 | [Compile read back and check model meaning (DOM-11-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Author body tree geoms and explicit closure constraints (DOM-11-A02) | 2 | source_supported_action_specification |
| 174 | [Replace mapped role-specific geometry (DOM-32-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Pin seed model and map CAD occurrences to bodies (DOM-32-A01) | 2 | source_supported_action_specification |
| 175 | [Compare preserved semantics and effective geometry (DOM-32-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Replace mapped role-specific geometry (DOM-32-A02) | 2 | source_supported_action_specification |
| 176 | [Author static world geoms and source sidecar (DOM-34-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Bind BIM-derived mesh and collider identities (DOM-34-A01) | 2 | source_supported_action_specification |
| 177 | [Validate static coverage and working passages (DOM-34-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Author static world geoms and source sidecar (DOM-34-A02) | 2 | source_supported_action_specification |
| 178 | [Parse compile and serialize editable MJCF (DOM-10-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Inventory URDF import policy and expected losses (DOM-10-A01) | 1 | source_supported_action_specification |
| 179 | [Reopen MJCF and compare supported semantics (DOM-10-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Parse compile and serialize editable MJCF (DOM-10-A02) | 1 | source_supported_action_specification |
| 180 | [Author IFC elements placements and relationships (DOM-15-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Resolve building schema units hierarchy and element evidence (DOM-15-A01) | 1 | source_supported_action_specification |
| 181 | [Validate semantic graph and evaluated geometry (DOM-15-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Author IFC elements placements and relationships (DOM-15-A02) | 1 | source_supported_action_specification |
| 182 | [Extract and retain native kernel shapes (DOM-27-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Resolve IFC kernel shape extraction requirements (DOM-27-A01) | 1 | source_supported_action_specification |
| 183 | [Validate shape class and source feature agreement (DOM-27-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Extract and retain native kernel shapes (DOM-27-A02) | 1 | source_supported_action_specification |
| 184 | [Produce linked drawings and exchange geometry (DOM-25-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Bind model revision to fabrication requirements (DOM-25-A01) | 1 | source_supported_action_specification |
| 185 | [Reopen recipient artifacts and audit feature coverage (DOM-25-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json) | 4 / 4 | Produce linked drawings and exchange geometry (DOM-25-A02) | 1 | source_supported_action_specification |
| 186 | [Author constrained source and materialize geometry (REC-14-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Define feature evidence and all required editable outputs (REC-14-A01) | 9 | source_supported_action_specification |
| 187 | [Verify editability, interfaces and fixed scan comparisons (REC-14-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Author constrained source and materialize geometry (REC-14-A02) | 9 | source_supported_action_specification |
| 188 | [Estimate sparse cameras and points with retained hypotheses (REC-03-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Bind image identities calibration groups and sparse-solve settings (REC-03-A01) | 8 | source_supported_action_specification |
| 189 | [Validate camera coverage and scale evidence (REC-03-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Estimate sparse cameras and points with retained hypotheses (REC-03-A02) | 8 | source_supported_action_specification |
| 190 | [Apply scoped edit and read actual resulting geometry (REC-16-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Freeze comparison baseline and bounded edit scope (REC-16-A01) | 7 | source_supported_action_specification |
| 191 | [Compare fixed evidence and publish revision deltas (REC-16-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Apply scoped edit and read actual resulting geometry (REC-16-A02) | 7 | source_supported_action_specification |
| 192 | [Estimate intrinsic and distortion parameters (REC-01-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Select calibrated target observations and hold-out views (REC-01-A01) | 4 | source_supported_action_specification |
| 193 | [Check held-out distortion behavior and publish intrinsics (REC-01-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Estimate intrinsic and distortion parameters (REC-01-A02) | 4 | source_supported_action_specification |
| 194 | [Estimate or import sequence poses and projected samples (REC-05-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Bind sensor calibration timing and depth encoding (REC-05-A01) | 4 | source_supported_action_specification |
| 195 | [Validate trajectory and metric depth independently (REC-05-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Estimate or import sequence poses and projected samples (REC-05-A02) | 4 | source_supported_action_specification |
| 196 | [Integrate observations and extract explicit geometry (REC-06-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Resolve fusion grid and pose convention (REC-06-A01) | 4 | source_supported_action_specification |
| 197 | [Compare fusion candidates and independent controls (REC-06-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Integrate observations and extract explicit geometry (REC-06-A02) | 4 | source_supported_action_specification |
| 198 | [Generate plane, cluster and cylinder candidates (REC-09-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Select observed regions and preserve point membership (REC-09-A01) | 3 | source_supported_action_specification |
| 199 | [Check sampling bias and publish primitive evidence (REC-09-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Generate plane, cluster and cylinder candidates (REC-09-A02) | 3 | source_supported_action_specification |
| 200 | [Estimate route-specific CAD alignment candidates (REC-12-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Bind exact CAD and observation-route evidence (REC-12-A01) | 3 | source_supported_action_specification |
| 201 | [Validate alignment and publish conditional outputs (REC-12-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Estimate route-specific CAD alignment candidates (REC-12-A02) | 3 | source_supported_action_specification |
| 202 | [Refine transform and retain correspondence evidence (REC-08-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Freeze initialization and comparison objective (REC-08-A01) | 2 | source_supported_action_specification |
| 203 | [Measure independent and directional surface differences (REC-08-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Refine transform and retain correspondence evidence (REC-08-A02) | 2 | source_supported_action_specification |
| 204 | [Estimate analytic parameters and uncertainty (CAD-11-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Verify metric evidence and select functional features (CAD-11-A01) | 2 | source_supported_action_specification |
| 205 | [Construct and validate supported CAD feature geometry (CAD-11-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Estimate analytic parameters and uncertainty (CAD-11-A02) | 2 | source_supported_action_specification |
| 206 | [Cast rays and record hit alternatives (REC-13-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Bind sketch view, camera and hit surface (REC-13-A01) | 2 | source_supported_action_specification |
| 207 | [Reproject anchors and publish measurement evidence (REC-13-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Cast rays and record hit alternatives (REC-13-A02) | 2 | source_supported_action_specification |
| 208 | [Align evidence under fixed datum choices and measure differences (REC-15-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Bind source revisions, datums and discrepancy purpose (REC-15-A01) | 2 | source_supported_action_specification |
| 209 | [Publish reconciliation choices and preserved conflicts (REC-15-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Align evidence under fixed datum choices and measure differences (REC-15-A02) | 2 | source_supported_action_specification |
| 210 | [Estimate supported scan-to-building transform (DOM-19-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Resolve scan, building and survey frame definitions (DOM-19-A01) | 2 | source_supported_action_specification |
| 211 | [Validate controls and publish aligned derivative (DOM-19-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Estimate supported scan-to-building transform (DOM-19-A02) | 2 | source_supported_action_specification |
| 212 | [Project register and publish source-linked cloud candidate (DOM-21-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Bind mandatory depth and measurement evidence (DOM-21-A01) | 2 | source_supported_action_specification |
| 213 | [Check registered cloud controls and source coverage (DOM-21-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Project register and publish source-linked cloud candidate (DOM-21-A02) | 2 | source_supported_action_specification |
| 214 | [Reconstruct surface and retain every cleanup derivative (DOM-29-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Inspect point evidence normals and meshing assumptions (DOM-29-A01) | 2 | source_supported_action_specification |
| 215 | [Compare surface and protected features to source (DOM-29-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 5 / 4 | Reconstruct surface and retain every cleanup derivative (DOM-29-A02) | 2 | source_supported_action_specification |
| 216 | [Generate coarse alignment hypotheses (REC-07-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Bind both clouds and declare transform freedoms (REC-07-A01) | 1 | source_supported_action_specification |
| 217 | [Test withheld controls and publish initialization (REC-07-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Generate coarse alignment hypotheses (REC-07-A02) | 1 | source_supported_action_specification |
| 218 | [Author parametric source and actual feature geometry (DOM-23-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Audit literal input contract and target remodeling meaning (DOM-23-A01) | 1 | source_supported_action_specification |
| 219 | [Validate functional interfaces and saved parametric output (DOM-23-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Author parametric source and actual feature geometry (DOM-23-A02) | 1 | source_supported_action_specification |
| 220 | [Compose intrinsic calibration and per-image pose solutions (CAD-02B-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Bind photographs, target evidence and camera state (CAD-02B-A01) | 0 | source_supported_action_specification |
| 221 | [Validate and publish camera solution (CAD-02B-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Compose intrinsic calibration and per-image pose solutions (CAD-02B-A02) | 0 | source_supported_action_specification |
| 222 | [Estimate object-to-camera pose candidates (REC-02-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Bind 3D landmarks to calibrated image coordinates (REC-02-A01) | 0 | source_supported_action_specification |
| 223 | [Validate independent reprojection and publish pose (REC-02-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json) | 5 / 4 | Estimate object-to-camera pose candidates (REC-02-A02) | 0 | source_supported_action_specification |
| 224 | [Estimate dense depth and fuse visible samples (REC-17-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 6 / 4 | Validate sparse-to-dense image and camera handoff (REC-17-A01) | 5 | source_supported_action_specification |
| 225 | [Mesh dense cloud and validate both outputs (REC-17-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 6 / 4 | Estimate dense depth and fuse visible samples (REC-17-A02) | 5 | source_supported_action_specification |
| 226 | [Recover cameras and the declared cloud representation (DOM-20-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 6 / 4 | Resolve literal photo input and cloud detail target (DOM-20-A01) | 3 | source_supported_action_specification |
| 227 | [Validate saved domain outputs and downstream conditions (DOM-20-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 6 / 4 | Recover cameras and the declared cloud representation (DOM-20-A02) | 3 | source_supported_action_specification |
| 228 | [Compose dense estimation fusion and meshing (DOM-28-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 6 / 4 | Bind supplied cameras and required surface outputs (DOM-28-A01) | 2 | source_supported_action_specification |
| 229 | [Check source geometry and independent controls (DOM-28-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 6 / 4 | Compose dense estimation fusion and meshing (DOM-28-A02) | 2 | source_supported_action_specification |
| 230 | [Compose sparse and dense visible-surface reconstruction (CAD-16-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 6 / 4 | Bind complete photo and metric-control contract (CAD-16-A01) | 1 | source_supported_action_specification |
| 231 | [Validate metric reference and saved three-output package (CAD-16-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 6 / 4 | Compose sparse and dense visible-surface reconstruction (CAD-16-A02) | 1 | source_supported_action_specification |
| 232 | [Train and export the actual Gaussian scene representation (REC-19-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Prepare a Gaussian training dataset with verified camera mapping (REC-19-A01) | 4 | source_supported_action_specification |
| 233 | [Evaluate captured-view appearance and geometry handoff boundaries (REC-19-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Train and export the actual Gaussian scene representation (REC-19-A02) | 4 | source_supported_action_specification |
| 234 | [Estimate depth and cameras and materialize the declared cloud (REC-10-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Bind learned reconstruction variant, images and camera roles (REC-10-A01) | 1 | source_supported_action_specification |
| 235 | [Compare predictions with independent controls and conventional candidates (REC-10-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Estimate depth and cameras and materialize the declared cloud (REC-10-A02) | 1 | source_supported_action_specification |
| 236 | [Generate and preserve the proxy mesh and its coordinate frame (REC-18-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Select one source image and a mesh-producing model contract (REC-18-A01) | 1 | source_supported_action_specification |
| 237 | [Evaluate visible fit and gate geometric reuse by independent evidence (REC-18-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Generate and preserve the proxy mesh and its coordinate frame (REC-18-A02) | 1 | source_supported_action_specification |
| 238 | [Train and save a renderable NeRF state (REC-20-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Bind NeRF method, supplied cameras and training-space transforms (REC-20-A01) | 0 | source_supported_action_specification |
| 239 | [Validate scene appearance and any separately extracted geometry (REC-20-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Train and save a renderable NeRF state (REC-20-A02) | 0 | source_supported_action_specification |
| 240 | [Execute the selected typed training route and package its scene (REC-11-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Choose the actual renderable scene subtype and consumer (REC-11-A01) | 0 | source_supported_action_specification |
| 241 | [Validate scene use and proposed appearance/mesh/CAD composition (REC-11-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Execute the selected typed training route and package its scene (REC-11-A02) | 0 | source_supported_action_specification |
| 242 | [Build the Gaussian scene and preserve domain mappings (DOM-22-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Bind the domain Gaussian scene contract (DOM-22-A01) | 0 | source_supported_action_specification |
| 243 | [Check domain appearance and explicit geometric overlays (DOM-22-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Build the Gaussian scene and preserve domain mappings (DOM-22-A02) | 0 | source_supported_action_specification |
| 244 | [Train and package the domain NeRF state (DOM-30-A02)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Bind domain features and cameras to the NeRF route (DOM-30-A01) | 0 | source_supported_action_specification |
| 245 | [Evaluate domain viewing results and optional surface reuse (DOM-30-A03)](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json) | 7 / 4 | Train and package the domain NeRF state (DOM-30-A02) | 0 | source_supported_action_specification |

## Action-specific implementation work

### 1. Preserve the input revision and state the job boundary (INTAKE-A01)

Original action: [Preserve the input revision and state the job boundary](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Add a per-job source-index and scope-record adapter using standard-library hashing and the existing provenance fields; retain original bytes and correction references.

Software: retain original files unchanged; record existing local paths or exact supplied URLs, source identity, date and content hash for retained files. Preserve prior revisions and the correction sequence. For a supplied URL, record the actual retrieval/inspection state beside it.

Agent: identify the supplied scope, intended use, source authority and dependencies. Separate instructions, observations, assumptions and candidate ideas using the wording and provenance of each item.

Inputs: read the current request, supplied descriptions and explicit values; identify the requested model and the exact next output.

Output/check: source index plus a scope statement; every retained source has an identity and every explicit correction points to the statement it changes. The original can be reopened from its recorded location.

Dependencies: [project instructions](/home/leo/projects/3dmodeling/AGENTS.md), research registration rules 1–7; [OCS skill](/home/leo/.codex/skills/ocs-engineering/SKILL.md), modeling contract steps 1–2.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Reuse: [build_workflow_register.py](/home/leo/projects/3dmodeling/research/tools/build_workflow_register.py). Source identity/hash and report registration conventions; per-job interface is proposed.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Source/feature association, unit/frame, checking and provenance instructions for the corresponding action; retain the original action-specific procedure.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 2. Bind checks to actual artifacts and source criteria (CAD-13-A01)

Original action: [Bind checks to actual artifacts and source criteria](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-13 — Verify model geometry and saved output.

Implementation proposal: Add feature/source criteria binding around the existing supplied-measurement checker; group only compatible numerical criteria and retain each feature identity.

Software: Inventory artifact type and available measurements; map each check to source feature and supported query.

Agent: Select checks appropriate to curves/solids/mesh/native history and identify independent control evidence.

Inputs: Artifact/revision/hash; model brief/source controls; intended use; per-feature criteria and representation.

Output/check: Check plan and evidence prerequisites for CAD-13-A02. Validation: Every planned numeric result has units, frame, criterion source and actual measurement route; reviewer checks feature identity.

Dependencies: Native measurement APIs and actual independent consumer; OCS numerical helper checks supplied point/axis/plane values only.

Resources: Metadata planning first; local CPU small relative to geometry queries for the same artifact. Remote/manual review concerns source associations and criteria.

Reuse: [check_contract.py](/home/leo/.codex/skills/ocs-engineering/scripts/check_contract.py). Supplied point/axis/plane numerical checks only; caller supplies independently sourced observations and criteria.

Source-supported tools: OCS read/measure/audit/save_verified, FreeCAD B-rep readback, build123d/CadQuery shape checks, independent importer, mesh validation. Original evidence: [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md), [https://build123d.readthedocs.io/en/stable/](https://build123d.readthedocs.io/en/stable/).

### 3. Identify the exact library item and retained files (DOM-06-A01)

Original action: [Identify the exact library item and retained files](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-06 — Library asset intake and rights record.

Implementation proposal: Proposal: item intake helper with separate item, file, source and occurrence identities.

Software: Read retained metadata, file types and SHA-256; detect identical bytes across different names.

Agent: Match the item/configuration to the brief using original labels; use VLM views only to resolve visible identifying details with source corroboration.

Inputs: Supplied source-library item; exact URL/local original; configuration/part number; retrieved files and dates where already acquired.

Output/check: Item/file inventory and source identity, consumed by DOM-06-A02. Validation: Check every inventoried file against its recorded digest/type; semantic review checks part/configuration names and supplied corrections.

Dependencies: Existing library/source records and standard file/hash tools; catalogue entries link to item sources.

Resources: Local metadata/hash work first; source inspection/manual identity effort recorded separately. Remote model work uses item labels/views; external retrieval remains its authorized research action.

Reuse: [build_workflow_register.py](/home/leo/projects/3dmodeling/research/tools/build_workflow_register.py). Source identity/hash and report registration conventions; per-job interface is proposed.

Source-supported tools: component registry/schema proposal; source license review. Original evidence: [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN), [https://www.kicad.org/libraries/license/](https://www.kicad.org/libraries/license/), [https://github.com/google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie), [https://polyhaven.com/license](https://polyhaven.com/license), [https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280).

### 4. Define collision scope and contact features (DOM-13-A01)

Original action: [Define collision scope and contact features](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-13 — Generate convex collision set.

Implementation proposal: Proposal: collision intake partitions by rigid body and emits protected-feature/criteria records.

Software: Check finite geometry, connected pieces, source scale and algorithm prerequisites.

Agent: Identify contact-relevant passages and independent moving bodies.

Inputs: Mesh, source/body IDs, local frame/scale and intended contact/passages criteria.

Output/check: Per-body collision plan with source mesh and protected regions. Validation: A moving assembly cannot become one rigid collider; source licence pages do not establish algorithm API.

Dependencies: DOM-12 asset records; CoACD repository and selected-version prerequisite inspection.

Resources: Local bounds/topology checks first; detailed source inspection and remote/manual interpretation separate.

Source-supported tools: CoACD; V-HACD; primitive fitting. Original evidence: [https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE), [https://github.com/kmammou/v-hacd/blob/master/LICENSE](https://github.com/kmammou/v-hacd/blob/master/LICENSE), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst).

### 5. Define feature evidence and all required editable outputs (REC-14-A01)

Original action: [Define feature evidence and all required editable outputs](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-14 — Remodel segmented scan evidence as parametric CAD.

Implementation proposal: Proposal: remodeling planner emits feature dependencies and required artifact/output capability matrix.

Software: Check complete dimensions/closure and actual backend persistence for sketch constraints, source and solid.

Agent: Select source-supported features and identify hidden geometry/idealizations.

Inputs: Measurement-set plus selected point-cloud/mesh; registration/datum; segmented fits; component/use criteria.

Output/check: Feature/parameter provenance plan and backend combination capable of all three outputs. Validation: Source evidence and output capability are explicit; unsupported editable artifact blocks full operation readiness.

Dependencies: Point03 CAD-09/CAD-10/DOM-40; OCS native bodies alone do not establish all three outputs.

Resources: Local metadata/fit reuse first; remote higher reasoning for feature intent; manual missing measurements separate.

Source-supported tools: Open3D feature fits, OpenCADStudio OCS skill, parametric CAD backend. Original evidence: [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html).

### 6. Select the execution mode and define candidate branches (INTAKE-A02)

Original action: [Select the execution mode and define candidate branches](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Encode the existing execution-mode/branch instructions as a reusable agent task with branch input/output ownership and recorded reasons.

Software: identify actual source formats, available machine-readable values and stable identifiers. Record the supported adapter/version for a software-first branch when exercised capability exists.

Agent: choose a proposed execution mode from section 5 and explain the choice by the source's concrete properties. For difficult inputs, define independent candidate branches: a source-literal interpretation, an independent feature/relationship interpretation and a software extraction branch wherever the source format supports it. Name each branch's intended use, required feature coverage/detail and per-feature accuracy criteria from the task. A branch may cover controlling dimensions while another adds sourced feature relationships; record the target difference and the source subset each uses.

Inputs: use the preserved source set to identify which records are explicit and which require interpretation.

Output/check: a branch plan naming the source corpus revision, branch source subset, assigned actions, intended use, required coverage/detail, feature accuracy criteria, component rationale, output ownership, resource-record requirements and evaluation conditions. Verify that every branch receives the same controlling source revisions and that its proposed detail/accuracy target follows the requested use.

Dependencies: [implementation plan](/home/leo/projects/3dmodeling/research/implementation-plan.md), source intake and proposed skills; [project instructions](/home/leo/projects/3dmodeling/AGENTS.md), bounded parallel contribution and evidence separation. Branch composition is a proposal.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 7. Extract source claims and associate each value with its subject (INTAKE-A03)

Original action: [Extract source claims and associate each value with its subject](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Add extraction adapters retaining original tokens and locations; validate JSON duplicate keys/nonfinite values and CSV dialect; keep semantic association in the agent step.

Software: copy machine-readable text and tabular cells with their locations and original formatting. Preserve the original numeric token, signs, decimal separator, unit label, inequality and tolerance notation. For JSON, detect duplicate object names through `object_pairs_hook` before creating a dictionary; reject `NaN`, `Infinity` and `-Infinity` through `parse_constant` and check parsed numerical finiteness. Preserve numeric token strings using the appropriate parsing callbacks. For CSV, record encoding/dialect and retain field strings through extraction. A parser reports rejected or ambiguous tokens as exceptions. These behaviors follow the official-library findings in the [source lookup](/home/leo/projects/3dmodeling/research/action-audit/reviews/source-check.md).

Agent: name the component, feature and property to which each claim refers. Link a pronoun, repeated name or shorthand only when the cited context supports that association. For visual annotations, a VLM cites the source image/page and relevant region and distinguishes the label from the feature it labels.

Inputs: read each supplied statement and value in the preserved sources.

Output/check: a claim record for every relevant statement or value: source location, original text, subject, proposed meaning, evidence status and branch identity. Compare the extracted claims against the original source; count and name omitted or duplicated source items.

Dependencies: [CAD-01](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json), preservation/check requirements; [DOM-01](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json), original wording and evidence status; [OCS skill](/home/leo/.codex/skills/ocs-engineering/SKILL.md), source-view inspection; original [JSON](https://docs.python.org/3/library/json.html) and [CSV](https://docs.python.org/3/library/csv.html) documentation inspected by the source-lookup role.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Source/feature association, unit/frame, checking and provenance instructions for the corresponding action; retain the original action-specific procedure.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 8. Identify components, features and geometric relationships (INTAKE-A04)

Original action: [Identify components, features and geometric relationships](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Add reference/name consistency checks around the existing component/feature association procedure.

Software: check name uniqueness, reference resolution and repeated identifiers. Preserve original names beside normalized readable names. Report two claims using one name for different subjects.

Agent: identify separate components, occurrences, feature boundaries, contact/clearance relationships and any described relative motion. Record the source for each relationship. Keep an interpretation alternative as a named candidate with its consequence for later geometry.

Inputs: organize the source claims into the component and feature structure needed by the intended model.

Output/check: a component/feature list and a relationship list, each with source pointers and dependencies. Check that a component named in a dimension exists and that a relation points to the intended features on both sides.

Dependencies: [OCS model contract](/home/leo/.codex/skills/ocs-engineering/references/model-contract.md), named separate parts, connections/motion and measurable invariants; [CAD-01](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json), component boundaries and geometry intent.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Source/feature association, unit/frame, checking and provenance instructions for the corresponding action; retain the original action-specific procedure.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 9. Normalize explicit quantities, units, datums and frames (INTAKE-A05)

Original action: [Normalize explicit quantities, units, datums and frames](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Add explicit quantity/unit conversion and frame records around the existing normalization procedure; keep semantic datum selection with the agent.

Software: parse explicit numbers and units; check quantity type; retain source values beside normalized values and the conversion rule. Construct decimal values from their retained source strings; record arithmetic precision/rounding and preserve the original precision. Use a unit mapping that has a documented source and checked conversions. Apply domain constraints to the named quantity: signed offsets retain their signs. Record source/target frames and an explicitly supplied transform where a coordinate conversion is required.

Agent: determine which datum and frame a source actually names; associate each dimension with its endpoints, axis, surface or reference plane. Keep size, position and orientation as distinct properties. Trace source-relative terms such as “above” to the source's stated frame.

Inputs: convert source-linked claims into quantities a later model can consume without changing their meaning.

Output/check: per-feature quantity records with original/normalized values, units, source location, datum, frame and value status. Recompute each permitted unit conversion; verify that source/target quantity types match and that each positional value names its reference.

Dependencies: [DOM-01](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json), unit normalization and preserved source frames; [OCS skill](/home/leo/.codex/skills/ocs-engineering/SKILL.md), units/origin/axes/datums; [implementation plan](/home/leo/projects/3dmodeling/research/implementation-plan.md), interchange and reproducibility checks.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Source/feature association, unit/frame, checking and provenance instructions for the corresponding action; retain the original action-specific procedure.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 10. Record per-feature tolerance and evidence requirements (INTAKE-A06)

Original action: [Record per-feature tolerance and evidence requirements](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Add per-feature criteria records distinguishing engineering allowance, source uncertainty and numerical checks.

Software: preserve the exact tolerance notation and its unit. Associate a general source tolerance with only the features covered by that source's applicability conditions. Check that lower/upper bounds and minimum/maximum conditions remain attached to the same feature after conversion.

Agent: distinguish the nominal geometry requirement, allowed geometric departure, source measurement uncertainty and numerical comparison rule. Keep a later solver stopping criterion and export/readback comparison threshold as separately sourced requirements when those operations apply. Name the intended measurement or geometric relation and its operating/measurement conditions. A categorical relationship such as separate components receives an exact identity/relationship check; a dimensional relationship receives its sourced quantitative rule.

Inputs: connect each geometry check to the acceptance rule and evidence that apply to that feature.

Output/check: for every controlling feature, record component/feature name, quantity or relation, nominal value if applicable, units/frame, tolerance form/value, tolerance source and scope, evidence uncertainty, intended check and responsible decision record. Verify each tolerance against the cited requirement. Preserve features whose pending question blocks a particular numerical check, with the exact question and affected downstream action.

Dependencies: [OCS model contract](/home/leo/.codex/skills/ocs-engineering/references/model-contract.md), selected dimensions/tolerances and check interface; [implementation plan](/home/leo/projects/3dmodeling/research/implementation-plan.md), component geometry and verification specification; [project instructions](/home/leo/projects/3dmodeling/AGENTS.md), sourced engineering values.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Source/feature association, unit/frame, checking and provenance instructions for the corresponding action; retain the original action-specific procedure.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 11. Evaluate candidate briefs against their source evidence (INTAKE-A07)

Original action: [Evaluate candidate briefs against their source evidence](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Package candidate-to-source review as an action-specific agent instruction with software coverage comparisons.

Software: align records by source item and feature identity; compare explicit values, signs, units, datum references, tolerance bounds, required relationships and source coverage. Evaluate each branch against its declared use, coverage/detail and per-feature accuracy criteria, then compare common required records across branches. Produce record-level disagreements and exception causes. Classify each difference as transcription, unit conversion, frame conversion, feature association, relationship interpretation, source conflict or added detail.

Agent: evaluate each candidate's interpretation using its cited source. For visual evidence, give a VLM the original full view/page, label region, associated endpoints/features, relevant text and competing records. Require an evidence-based assessment for each disputed feature or label association. For text-only evidence, use a reasoning review of source passages and competing meanings. Select the supported interpretation when the sources and existing task requirements determine it; record the concrete reason.

Inputs: compare the isolated candidate records against the frozen source revision and requested output.

Output/check: an evidence assessment for each differing record, the source region/passage, numerical checks, branch identity, evaluator identity and proposed selection. Verify that every selected claim points to an input source or a separately recorded user decision.

Dependencies: [OCS skill](/home/leo/.codex/skills/ocs-engineering/SKILL.md), source inspection and distinction between visual inspection and measured checks; [CAD-01](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json), source/value preservation. Candidate evaluation by a VLM is a proposed composition of these requirements.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Source/feature association, unit/frame, checking and provenance instructions for the corresponding action; retain the original action-specific procedure.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 12. Select supported records and merge compatible contributions (INTAKE-A08)

Original action: [Select supported records and merge compatible contributions](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Add a contribution merge adapter preserving compatible records and conflicting alternatives with their sources.

Software: carry selected records and their source links into the merged document; record the originating branch and comparison finding. Detect duplicate identities, conflicting values and dangling feature/frame references.

Agent: select a whole candidate when its evidence and completeness support the requested brief, or merge complementary records from several candidates. The reasoning agent or VLM can perform this evidence-supported selection within the task's existing requirements. Before merging, check common source revision, component identity, units, frames, datum meaning, tolerance applicability and interpretation dependencies. Record the reason for every disputed selection.

Inputs: produce one coherent brief from evaluated candidates and recorded user decisions.

Output/check: merged brief plus a selection record containing retained candidate contributions, discarded candidate interpretations with reasons, preserved conflicts and sources. Recheck every cross-feature relationship affected by the merge.

Dependencies: [CAD-01](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json), source associations and unresolved choices; [DOM-01](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json), preserved units/frames/status; [project instructions](/home/leo/projects/3dmodeling/AGENTS.md), proposal and decision separation. Record selection/merge is a proposal.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Source/feature association, unit/frame, checking and provenance instructions for the corresponding action; retain the original action-specific procedure.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 13. Validate the merged brief independently (INTAKE-A09)

Original action: [Validate the merged brief independently](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Package independent merged-brief reread plus structural/reference checks; retain reviewer identity and observations.

Software: validate source references, identifiers, unit compatibility, conversion reversibility to the documented precision, duplicate/conflicting requirements, tolerance coverage and relationships. Compare required source claims to the brief in both directions: each requirement has a brief record; each controlling record has source/decision evidence.

Agent: a review agent instance or source-reading reviewer separate from the producing/merging interpretation rereads the original source against the merged brief for initial interpretation, changed semantic mappings and candidate merges. Record producer, merger and reviewer identities, actual exposed model identities and shared source/model dependencies. Check feature identity, geometric intent, scope, datum interpretation, source priority and preservation of corrections. For image evidence, review the original view and merged feature associations using a VLM; cite concrete source regions in each finding. A deterministic replay uses the independently checked expected case and its supported rules; a new semantic exception returns to independent source review.

Inputs: inspect the exact merged revision for numerical, referential and semantic errors introduced during extraction or merging.

Output/check: per-feature/action status with the exact test, source and result. Use `READY — source extraction` for recorded literal value/source correspondence and `READY — named geometry operation` when the feature supplies that operation's required evidence and decisions. Use `BLOCKED — named prerequisite` with the source conflict/question and exact dependent operation. Carry a controlling feature's blocked prerequisite to the placements/relations that depend on it. The brief also records the current artifact revision and source revisions.

Dependencies: [implementation plan](/home/leo/projects/3dmodeling/research/implementation-plan.md), verification/reproducibility requirements; [OCS skill](/home/leo/.codex/skills/ocs-engineering/SKILL.md), measured checks and corresponding visual inspection; [CAD-01](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json), provenance and ambiguity checks.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Source/feature association, unit/frame, checking and provenance instructions for the corresponding action; retain the original action-specific procedure.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 14. Deliver the brief and specify the downstream handoff (INTAKE-A10)

Original action: [Deliver the brief and specify the downstream handoff](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md). Operations: CAD-01 — Extract a model brief from text and dimensions, DOM-01 — Normalize model brief.

Implementation proposal: Add consumer-input and artifact-revision checks for the existing brief handoff procedure.

Software: preserve the readable brief, original evidence links, source/brief hashes, candidate comparison, merge record and actual validation findings. Record completed action, input revision, output revision, software/model identity and resumption dependency.

Agent: name the target representation and its required fields. A constrained sketch consumes feature/profile intent, units, geometric and dimensional constraints. CAD solid construction consumes named parts/features, their sourced dimensions and frames. A domain operation additionally consumes the domain relationships its own operation contract requires.

Inputs: save the checked brief revision and state which subsequent actions can consume its records.

Output/check: one documented brief revision and a named next action or exact input request for each feature branch. A subsequent source change starts from Action 01's revision step and invalidates only the affected downstream records. Handoff checks: link each next action to the feature records it needs, its applicable tolerances and its later geometry measurement plan. Retain original source wording and proposal/decision statuses. Check that the consumer receives a single identified brief revision.

Dependencies: [CAD-09/CAD-10 — Constrained sketch/kernel solid operations](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json); [DOM-04/DOM-40 — Native CAD/script-parametric authoring](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json); [implementation plan](/home/leo/projects/3dmodeling/research/implementation-plan.md), source ownership and verification.

Resources: Local file I/O, hashing/text records and optional remote reasoning; per-action requirements remain in the first-point table.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Source/feature association, unit/frame, checking and provenance instructions for the corresponding action; retain the original action-specific procedure.

Source-supported tools: model brief schema, human review, OCS engineering skill. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

Source-supported tools: existing OCS engineering skill; structured project schema proposal. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 15. Bind image identities calibration groups and sparse-solve settings (REC-03-A01)

Original action: [Bind image identities calibration groups and sparse-solve settings](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-03 — Estimate camera poses and sparse structure from overlapping photos.

Implementation proposal: Proposal: SfM intake emits per-image camera/model/mask records and explicit scale status.

Software: Inspect images and camera models; map calibration through verified adapter; group shared intrinsics only for documented shared state. COLMAP +0.5 principal-point correction is conditional on actual source/destination pixel conventions; read back saved camera model/parameters.

Agent: Identify feature-bearing static regions, symmetry and repeated texture.

Inputs: Photo-set with original/derived lineage, camera state/masks and optional calibration/control receipts.

Output/check: Dataset/camera-group manifest, fit/check split and sparse configuration. Validation: Photo-only input permits arbitrary-scale reconstruction; original scale-control checks apply only when linked metric evidence exists.

Dependencies: COLMAP/pycolmap or separate Meshroom/OpenMVG branch; point05 calibration contract.

Resources: Local metadata and bounded image review precede feature extraction; model calls/manual control capture separate.

Source-supported tools: COLMAP/pycolmap, AliceVision/Meshroom, OpenMVG. Original evidence: [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst), [https://alicevision.org/](https://alicevision.org/), [https://github.com/openMVG/openMVG](https://github.com/openMVG/openMVG).

### 16. Freeze comparison baseline and bounded edit scope (REC-16-A01)

Original action: [Freeze comparison baseline and bounded edit scope](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-16 — Iterate CAD edits against registered evidence.

Implementation proposal: Proposal: edit-baseline binder emits immutable comparison inputs and bounded feature plan.

Software: Read actual geometry and baseline measurements; verify target revision and authorized feature edit.

Agent: Identify intended source-backed change and unaffected interfaces.

Inputs: Measurement-set; cad-solid or materialized parametric-source; cloud/mesh; immutable transform; edit plan/regions/criteria.

Output/check: Baseline CAD/scan/configuration receipt and exact edit/check dependencies. Validation: No changed registration/mask/threshold can silently enter the before/after comparison.

Dependencies: OCS revision-bound operations; point03 CAD-14 recovery; actual parametric generation route.

Resources: Local baseline regions first; remote/manual edit interpretation separate.

Source-supported tools: OCS revision-bound edit/readback, Open3D distance queries, CloudCompare distance command. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode).

### 17. Select geometry occurrence and mesh role (DOM-12-A01)

Original action: [Select geometry occurrence and mesh role](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-12 — Export mesh assets for MuJoCo.

Implementation proposal: Proposal: mesh planner emits source occurrences, target body frames and role-specific export settings.

Software: Query supported shape/scene geometry; inventory existing mesh data and required tessellation.

Agent: Select relevant source surfaces and role without merging movable links.

Inputs: One cad-solid/B-rep/visual-scene/robot-assembly route; occurrence selection and intended visual/collision role.

Output/check: Per-asset source-to-target frame, unit and approximation plan. Validation: Assembly/scene input resolves actual geometry; camera-only/no-geometry objects retain explicit state.

Dependencies: Point03 native geometry; supported exporter and selected MuJoCo format/version discovery.

Resources: Metadata/selected regions precede full tessellation; remote/manual role review separate.

Source-supported tools: CAD mesh exporter; Blender; Open CASCADE tessellation. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 18. Pin source definitions and assembly roles (CAD-12-A01)

Original action: [Pin source definitions and assembly roles](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: CAD-12 — Assemble existing CAD or source-library components.

Implementation proposal: Proposal: definition intake helper preserving identity, unit/frame and representation with a source/occurrence distinction.

Software: Read files/metadata and hashes; count definitions and occurrences separately; inspect geometry representation with the selected reader.

Agent: Resolve component names and choose existing assets within the brief; distinguish sourced parts and proposed placeholders.

Inputs: Base cad-solid; distinct additional cad-solid or source-library item; brief; original files, hashes, units and rights records.

Output/check: Component-definition manifest with base/additional roles, consumed by CAD-12-A02. Validation: Recompute source hashes; check a distinct additional input exists; independent semantic review compares configuration/part identity to the brief.

Dependencies: Existing source records, native CAD reader and OCS skill; operation sources document reuse and assembly alternatives.

Resources: Local metadata/hash CPU and file I/O first; geometry inspection scales with file size. Remote reasoning only for ambiguous identity; log model calls and active source review.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Documented exact part/revision, representation, source dependency and reproduction-package records; serialization/automation follows each action.

Source-supported tools: OCS blocks/groups, FreeCAD App::Link/Assembly, build123d/CadQuery Assembly, unit and frame mapping. Original evidence: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [https://cadquery.readthedocs.io/en/stable/](https://cadquery.readthedocs.io/en/stable/).

### 19. Resolve rigid links from authored assembly relations (DOM-08-A01)

Original action: [Resolve rigid links from authored assembly relations](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-08 — CAD assembly to articulated robot structure.

Implementation proposal: Proposal: link mapper accepts occurrences/joints/measurements and emits link memberships plus unmapped references.

Software: Read occurrence hierarchy; expand instances and compare joint references; preserve definition and occurrence IDs.

Agent: Interpret supported rigid grouping and distinguish CAD hierarchy from motion graph.

Inputs: Cad-assembly, joint-set and measurement-set; source transforms and rigid grouping evidence.

Output/check: Occurrence-to-link map and expected graph/geometry coverage. Validation: Every moving occurrence belongs to its declared link; repeated instances remain distinct.

Dependencies: DOM-31 authored graph and point02 assembly capability.

Resources: Local metadata work scales with parts/joints; remote interpretation handles ambiguous grouping.

Source-supported tools: FreeCAD Assembly Workbench; explicit robot-description authoring; CAD-to-URDF scripts as candidates. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md), [https://github.com/boelnasr/CAD_TO_URDF](https://github.com/boelnasr/CAD_TO_URDF).

### 20. Validate sparse-to-dense image and camera handoff (REC-17-A01)

Original action: [Validate sparse-to-dense image and camera handoff](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-17 — Build dense point cloud and mesh from SfM camera solution.

Implementation proposal: Proposal: dense intake emits source-to-undistorted image/camera map and compatible workspace receipt.

Software: Read sparse model and verify image/model pairing; use image_undistorter with documented output convention; inspect selected dense backend/build.

Agent: Review visible coverage, weak baseline and material regions.

Inputs: Photo-set AND camera-solution, source sparse model, masks and desired geometry criteria.

Output/check: Undistorted image/camera workspace and dense-backend/settings plan. Validation: Undistorted intrinsics and pixels must agree; a sparse camera model carries its own arbitrary/metric scale status.

Dependencies: COLMAP/OpenMVS interface and actual hardware/build capability.

Resources: Local metadata/sparse checks before dense work; cost plan names resolution/neighbors/depth range and memory.

Source-supported tools: OpenMVS DensifyPointCloud, OpenMVS ReconstructMesh, COLMAP dense workspace. Original evidence: [https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/](https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/), [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst).

### 21. Classify the component change and identify new bytes (DOM-26-A01)

Original action: [Classify the component change and identify new bytes](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-26 — Version and reuse component revision.

Implementation proposal: Proposal: revision-diff helper separating source bytes, rights evidence, metadata and geometry derivatives.

Software: Hash source/derivative bytes; compare normalized metadata without rewriting originals; list changed dependency references.

Agent: Classify identity-preserving revision versus a different component/configuration and identify affected feature evidence.

Inputs: Component-record whose required intake/representation references exist; prior revisions; changed source/terms/metadata; original and derivative byte hashes. Preliminary file digests remain intake evidence until component publication prerequisites pass.

Output/check: Change classification and candidate revision identity, consumed by DOM-26-A02. Validation: Recompute digests and confirm earlier revisions resolve unchanged; independent reviewer checks revision-versus-new-component classification.

Dependencies: Existing content hashes and completed required intake references; proposed registry/version organization in implementation plan. Partial intake records retain their draft/action-readiness status.

Resources: Local hashing/I/O first; cost scales with asset bytes. Remote/manual work is limited to identity and semantic change classification.

Reuse: [build_workflow_register.py](/home/leo/projects/3dmodeling/research/tools/build_workflow_register.py). Source identity/hash and report registration conventions; per-job interface is proposed.

Source-supported tools: content-addressed files; Git metadata; source/license registry. Original evidence: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 22. Select a supported solid feature route (CAD-10-A01)

Original action: [Select a supported solid feature route](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-10 — Create a kernel solid and native model document from confirmed parameters.

Implementation proposal: Proposal: feature capability planner with explicit profile, operand and representation prerequisites.

Software: Inspect backend version/API and actual curve/solid support; verify closed profile, finite inputs, extrusion direction or revolution axis/sweep.

Agent: Choose primitive/extrude/revolve/Boolean sequence preserving separate parts and required surfaces.

Inputs: Constrained-sketch, compatible parametric-source, or model-brief plus dimensions; units, axes, part boundaries and feature criteria.

Output/check: Feature/backend plan for CAD-10-A02. Validation: Plan uses actual available operations and sourced dimensions. OCS plugin Extrude accepts one curve-profile handle and rejects Region; closed profile yields Solid3D and open profile yields Surface. A required solid from an open profile blocks construction until sourced closure or an evidenced alternate route exists. Outer/inner hole loops require an expressly supported operation sequence/backend.

Dependencies: OCS SolidOperation enum/source implements create, rigid transform, region/surface, extrude and Boolean; REVOLVE uses its command path. FreeCAD/CadQuery/build123d are documented alternatives.

Resources: Metadata/profile checks first; local CPU/RAM scales with feature/operand complexity. High-reasoning agent handles ambiguous topology/sequence; record manual decisions.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md), [ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md). Source-defined feature route and component representation decisions.

Source-supported tools: OpenCADStudio kernel tools, FreeCAD PartDesign/Part, build123d, CadQuery. Original evidence: [https://build123d.readthedocs.io/en/latest/operations.html](https://build123d.readthedocs.io/en/latest/operations.html), [https://cadquery.readthedocs.io/en/stable/](https://cadquery.readthedocs.io/en/stable/), [https://openscad.org/documentation](https://openscad.org/documentation), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md), [/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md).

### 23. Identify plane evidence and independent metric controls (CAD-02-A01)

Original action: [Identify plane evidence and independent metric controls](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-02 — Rectify a raster drawing plane from known dimensions.

Implementation proposal: Proposal: plane preflight consumes image/control evidence and emits model sufficiency, control roles and check IDs.

Software: Read image orientation/size; inventory control pairs; detect repeated, collinear or clustered configurations.

Agent: Distinguish lens distortion, page perspective/deformation, drawing-to-object scale and freehand proportions.

Inputs: Original raster/page hash; known coplanar coordinates/lengths; unit/frame; intended plane; independent controls.

Output/check: Plane/control manifest and selected scale/projective model for CAD-02-A02. Validation: One length supports uniform scale only with justified front-parallel/isotropic conditions; projective correction requires sufficient nondegenerate correspondences.

Dependencies: OpenCV perspective APIs; CAD-R02 conditions; point01 source/unit intake.

Resources: Local metadata/few-point work first; remote high reasoning for plane ambiguity; manual point selection and uncertainty recorded.

Source-supported tools: OpenCV point correspondences, planar homography. Original evidence: [https://docs.opencv.org/5.0/main_modules/calib.html](https://docs.opencv.org/5.0/main_modules/calib.html).

### 24. Separate stroke classes and inspect source regions (CAD-04-A01)

Original action: [Separate stroke classes and inspect source regions](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-04 — Extract raster edges, lines and contours.

Implementation proposal: Proposal: stroke preflight emits source-mapped class masks and ambiguous regions.

Software: Threshold/detect edges with recorded settings; preserve crossing and overlapping class candidates.

Agent: Interpret boundary versus centreline and hidden-line convention; retain uncertain class alternatives.

Inputs: Original/rectified raster; mapping; text/view masks; intended geometry and drawing convention.

Output/check: Candidate masks for object, annotation, extension, centre and hidden strokes. Validation: Overlay masks and confirm required features survive preprocessing.

Dependencies: OpenCV image primitives; OCR masks are optional evidence.

Resources: Local work scales with pixels; coarse inspection precedes original-resolution feature work; remote/manual classification tracked.

Source-supported tools: OpenCV thresholding, HoughLinesP, findContours, approxPolyDP. Original evidence: [https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html](https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html), [https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html](https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html), [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html).

### 25. Select calibrated target observations and hold-out views (REC-01-A01)

Original action: [Select calibrated target observations and hold-out views](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-01 — Calibrate camera intrinsics and distortion.

Implementation proposal: Proposal: target-observation collector returns point identities, coverage and exclusions.

Software: Detect supported chessboard/target features; inspect ordering, image-field and orientation coverage.

Agent: Review target identity, blur/deformation and whether camera states require separate groups.

Inputs: Photo-set; measurement-set target geometry/units; focus/zoom/sensor state; image mappings.

Output/check: Target/image-point sets with fit/hold-out roles and coverage report. Validation: Poor spatial/orientation coverage or wrong target order is diagnosed before parameter fitting.

Dependencies: OpenCV target detector and calibrateCamera; selected target family API discovered.

Resources: Local detection follows image pixels; manual target review and remote ambiguity reasoning separate.

Source-supported tools: OpenCV calibrateCamera, checkerboard or Charuco target. Original evidence: [https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html).

### 26. Select physical-property evidence per rigid body (DOM-14-A01)

Original action: [Select physical-property evidence per rigid body](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-14 — Calculate or import physical mass properties.

Implementation proposal: Proposal: property intake emits per-field provenance, reference point/axes and required calculation inputs.

Software: Read supplied fields; inventory solids, cavities, overlapping occurrences and mesh closure/orientation.

Agent: Distinguish measured scalar mass, supplied COM/tensor and geometry-density assumptions.

Inputs: Physical-measurement-set OR material-set plus cad-solid/B-rep/mesh/cad-assembly; target body map. Each tensor field supplies raw component ordering, matrix off-diagonal versus signed/unsigned product convention, reference point and axes.

Output/check: Per-body mass/COM/tensor field status and calculation eligibility. Validation: Scalar mass supports only mass; visual material labels alone supply no density. Geometry-integration branch first checks finite closed solid(s), coherent orientation and absence of free boundaries; the volume integration API assumes these conditions.

Dependencies: DOM-08 rigid grouping; actual geometry integration capability.

Resources: Metadata checks first; mesh validity cost follows triangles; manual metrology separate.

Source-supported tools: CAD kernel mass properties; MuJoCo compiler geom inference; measured scale. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 27. Define IFC-to-display identity and unit policy (DOM-17-A01)

Original action: [Define IFC-to-display identity and unit policy](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-17 — IFC to GLB display scene.

Implementation proposal: Proposal: scene planner emits element selection, node identity policy and preserved/lost field map.

Software: Inspect selected IfcConvert CLI or Python GLB serializer separately. CLI supports GLB and GlobalId filtering, but its documented use-element-guids naming flag covers OBJ/DAE/STEP/SVG. Serializer example has explicit optional GUID configuration. Define a checked many-to-many source-element/node/primitive/occurrence map.

Agent: Select meaningful display coverage and sidecar properties.

Inputs: IFC, selected elements/materials, target display frame and identity requirements.

Output/check: Source-to-node/property mapping plan and unit/axis policy. Validation: Generated fixture IDs are recorded as converted IDs; geometric holes do not imply opening relationships.

Dependencies: IfcOpenShell/IfcConvert GLB source capability; optional Blender chain is separate adapter.

Resources: Local mapping preflight first; remote/manual display semantics separate.

Source-supported tools: IfcOpenShell IfcConvert; Blender; GLB export. Original evidence: [https://docs.ifcopenshell.org/introduction.html](https://docs.ifcopenshell.org/introduction.html), [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/), [/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json](/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json).

### 28. Bind environment to existing robot world frame (DOM-33-A01)

Original action: [Bind environment to existing robot world frame](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-33 — Add environment collision geometry to MJCF.

Implementation proposal: Proposal: environment intake emits frame/contact dependencies and seed preservation snapshot.

Software: Read seed graph/settings; validate per-piece transforms and common scale; inventory contact filters/pairs.

Agent: Associate obstacles and required passage/contact regions.

Inputs: Existing MJCF, environment mesh and collision-set with registration/source map.

Output/check: Seed robot invariants and environment-to-world transform/contact plan. Validation: Mesh and collider source frames must agree; scene appearance alone cannot establish registration.

Dependencies: Point05 registration; DOM-13 colliders and seed compiler.

Resources: Local transforms/bounds first; detailed passage queries selected; remote/manual evidence review separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst).

### 29. Bind sensor calibration timing and depth encoding (REC-05-A01)

Original action: [Bind sensor calibration timing and depth encoding](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-05 — Register RGB and depth frames and estimate sequence poses.

Implementation proposal: Proposal: RGB-D intake emits calibrated frame pairs, depth units/validity and source-to-target camera mapping.

Software: Decode stated depth representation; inspect synchronization/image sizes; preserve invalid masks and calibrated registration parameters. Open3D v0.20.0 RGBDImage.h declares defaults; Image.cpp divides raw depth by depth_scale and zeros >= depth_trunc. Use sensor-specific settings, invalid mask and axial-versus-ray-range convention.

Agent: Identify dynamic regions, depth discontinuities and unsupported sensor assumptions.

Inputs: Depth-frames with raw RGB/depth, timestamps, intrinsics, RGB-depth extrinsics, depth scale/invalid/range rules and pose source.

Output/check: Per-frame sensor/calibration/time manifest and alignment/validity plan. Validation: Depth numeric values require declared divisor/units; different clocks/extrinsics cannot be treated as aligned frames.

Dependencies: Sensor SDK/calibration and pinned Open3D RGBDImage/odometry contracts.

Resources: Local metadata/range samples first; full reprojection cost follows pixels/frames; manual calibration separate.

Source-supported tools: Open3D RGB-D odometry, sensor SDK calibration, Open3D camera intrinsics/trajectory. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html).

### 30. Resolve fusion grid and pose convention (REC-06-A01)

Original action: [Resolve fusion grid and pose convention](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-06 — Integrate calibrated RGB-D frames into point cloud or TSDF mesh.

Implementation proposal: Proposal: fusion preflight emits per-frame integration transform and units/settings receipt.

Software: Use explicit world→camera integration extrinsics. The tutorial uses inverse(camera_pose) for its camera-to-world input; invert only the actual opposite-direction input. Check matching image/intrinsic/pose revisions, depth units and bounded region.

Agent: Review observed coverage and effect of dynamic/invalid regions.

Inputs: Depth-frames AND matching camera-solution; depth encoding/calibration, voxel length, signed-distance truncation and range policy.

Output/check: Integration manifest with frame order, world frame, validity masks and grid settings. Validation: Depth truncation and signed-distance truncation are separate quantities; no implicit unit/default conversion.

Dependencies: REC-05 checked poses and pinned Open3D TSDF/RGBDImage API.

Resources: Local metadata/bounded subset first; volume memory depends on occupied region and voxel length.

Source-supported tools: Open3D ScalableTSDFVolume, Open3D RGBDImage, Open3D marching-cubes extraction. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html).

### 31. Prepare a Gaussian training dataset with verified camera mapping (REC-19-A01)

Original action: [Prepare a Gaussian training dataset with verified camera mapping](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-19 — Train and export a Gaussian splat scene.

Implementation proposal: PROPOSAL Gaussian dataset adapter: photos + supplied cameras + selected parser/config → training dataset, camera/world normalization receipt, readback differences and participation table.

Software: Use an evidenced supplied-camera parser or prepared transforms.json pathway with version discovery; read actual parsed cameras, auto-orientation/centering/scale settings and output transform. Do not rerun default pose estimation unintentionally. Preserve actual dataparser_transform and dataparser_scale, applied metadata and orientation override; scene_scale is box extent. Use the recorded inverse composition for round trip, as specified in common_protocol.parser_contract.

Agent: Associate source regions/masks and camera groups, identify view gaps and choose supported training/evaluation partitions.

Inputs: Photo-set AND camera-solution, image/camera IDs, intrinsics/distortion/preprocessing, masks, train/evaluation roles, selected Splatfacto version/config and rights records.

Output/check: Dataset/parser receipt with original-to-training camera/world transforms, scale, image assignments, camera-optimization policy and feature evaluation plan. Validation: Check camera projection against source before training; reject duplicate axis flip/scale normalization; evaluation images used in SfM retain their shared pose dependence.

Dependencies: REC-03/05/10 camera source and preprocess mappings; common camera convention/partition protocol; actual parser capabilities.

Resources: CPU metadata/projection preview first; record dataset images/resolution and anticipated Gaussian/training settings before GPU allocation; remote VLM and manual masks separate.

Source-supported tools: Nerfstudio Splatfacto / gsplat, Gaussian PLY export. Original evidence: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html).

### 32. Inspect source entities, units and drawing contexts (CAD-08-A01)

Original action: [Inspect source entities, units and drawing contexts](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-08 — Read and clean vector drawing geometry.

Implementation proposal: Proposal: drawing preflight retaining entity IDs, nested transforms, unit evidence and importer option receipt.

Software: Use ezdxf.readfile/modelspace queries or inspected native reader; inventory nested INSERT transforms, entity coordinate systems and unsupported types.

Agent: Identify profile versus annotation/construction geometry and whether SVG path centreline or styled outline supplies the intended shape.

Inputs: Original DXF/SVG; file hash; intended layers/entities; model/paper-space choice; physical dimensions and target plane.

Output/check: Entity/context inventory and source-to-target map prerequisites for CAD-08-A02. Validation: Compare source controls and entity inventory; independent semantic reviewer checks selected profile/context and unit meaning.

Dependencies: Documented FreeCAD DXF/SVG import and ezdxf APIs; OCS read/schema interfaces for the actual session.

Resources: Metadata/stream reading first; local CPU/RAM grows with entities/nesting. Remote VLM uses original views for selection; record manual source-review effort.

Source-supported tools: OpenCADStudio DWG/DXF/MCP, FreeCAD Draft DXF/SVG import, ezdxf, geometry audit. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md), [https://ezdxf.readthedocs.io/en/stable/](https://ezdxf.readthedocs.io/en/stable/), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md).

### 33. Map curves and sourced constraints to a sketch plan (CAD-09-A01)

Original action: [Map curves and sourced constraints to a sketch plan](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-09 — Build and constrain an editable planar sketch.

Implementation proposal: Proposal: source-to-sketch constraint mapper with stable geometry IDs and intended freedom records.

Software: Resolve element IDs and plane coordinates; check curve support, loop closure and duplicate constraint candidates.

Agent: Distinguish driving dimensions, reference dimensions, construction geometry and intended free motion.

Inputs: Vector-drawing plus model-brief, dimensions or measurement-set; support plane, datum and source-to-entity map.

Output/check: Sketch element/constraint plan for CAD-09-A02. Validation: Check every constraint references correct elements and units; independent reviewer verifies diameter/radius, centre/edge and hole-loop meaning.

Dependencies: FreeCAD Sketcher addGeometry/addConstraint documentation; OCS sketch/constraint use requires discovered actual support.

Resources: Local mapping checks depend on entity/constraint count. High-reasoning/VLM review addresses ambiguous relation meaning; record manual decisions.

Source-supported tools: FreeCAD Sketcher scripting, FreeCAD Draft-to-Sketch, OpenCADStudio sketch/constraint capability as discovered in session. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 34. Locate annotations and retain crop mappings (CAD-03-A01)

Original action: [Locate annotations and retain crop mappings](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-03 — Recognize dimension text with OCR.

Implementation proposal: Proposal: annotation-region helper emits mapped crops and contextual source locations.

Software: Create bounded reading derivatives; preserve original image and valid coordinate mappings.

Agent: Identify dimensions, leaders, notes and legends; include adjacent arrow/extension endpoints.

Inputs: Original raster/hash; view regions; orientation; optional plane transform; language hints.

Output/check: Text-region crops with full-view references, pixel boxes and crop/deskew/resize mapping. Validation: Crop/rotation coordinates map to original pixels; masks preserve inspectable glyph evidence.

Dependencies: Documented OCR preparation and image-transform interfaces.

Resources: Local work scales with crop pixels; remote VLM receives full view plus selected crops; manual region selection recorded.

Source-supported tools: Tesseract OCR TSV output, image crop/deskew, human transcription review. Original evidence: [https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html).

### 35. Identify views and declare their projection frames (CAD-06-A01)

Original action: [Identify views and declare their projection frames](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-06 — Register orthographic drawing views in a shared coordinate frame.

Implementation proposal: Proposal: view manifest accepts vector bundle/metadata and outputs explicit view-to-model projection definitions.

Software: Inventory view regions and declared transforms; reject accidental mixing of detail/section/perspective views.

Agent: Determine source-supported front/top/side and projection convention; retain view alternatives where ambiguous.

Inputs: Vector-drawing bundle containing at least two identified orthographic views; original source mappings; labels/dimensions and control metadata.

Output/check: View inventory with plane axes, viewing direction, scale, datum and convention evidence. Validation: At least two identified views are available; auxiliary/section views have their own projection definition.

Dependencies: Original CAD-06 vector bundle contract; documented orthographic methods; manual OCS/FreeCAD alignment.

Resources: Local manifest/control checks first; remote high reasoning for labels/conventions; manual view association recorded.

Source-supported tools: view segmentation, projection-axis declaration, line/vertex matching, dimension reconciliation. Original evidence: [https://xnjdxb.swjtu.edu.cn/en/article/id/9616](https://xnjdxb.swjtu.edu.cn/en/article/id/9616), [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html).

### 36. Enumerate source-constrained 3D feature candidates (CAD-07-A01)

Original action: [Enumerate source-constrained 3D feature candidates](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-07 — Reconstruct a candidate 3D wireframe and surface from orthographic views.

Implementation proposal: Proposal: reconstruction hypothesis builder emits source-linked candidate edges/features and unresolved dependencies.

Software: Solve compatible projection-coordinate constraints; enumerate distinct solutions where data underdetermine geometry.

Agent: Interpret feature meaning and supported hidden surfaces; compare candidates with dimensions and task purpose.

Inputs: Vector view bundle; measurement-set; CAD-06 model-brief; feature criteria and component boundaries.

Output/check: Candidate vertex/edge/feature hypotheses with source-view links and unresolved degrees of freedom. Validation: Every required coordinate/feature has source or explicit inference status; equal projections preserve alternatives.

Dependencies: Registered view transforms; proposed geometric reconstruction; supported kernel route from point03.

Resources: Local constraint/candidate search depends on repetition/ambiguity; high-reasoning remote review targets hidden-feature interpretation.

Source-supported tools: multi-view edge correspondence, wireframe/face reconstruction, OpenCASCADE or FreeCAD surface/solid creation. Original evidence: [https://www.sciencedirect.com/science/article/pii/S0097849323000766](https://www.sciencedirect.com/science/article/pii/S0097849323000766), [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html).

### 37. Select observed regions and preserve point membership (REC-09-A01)

Original action: [Select observed regions and preserve point membership](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-09 — Segment point clouds and fit candidate primitive evidence.

Implementation proposal: Proposal: region selector emits immutable point-membership and coverage manifests.

Software: Inventory density/normals/outliers; create explicit region/sampling derivatives retaining original membership.

Agent: Distinguish mixed surfaces, dynamic points and unsampled interfaces.

Inputs: Metric framed point-cloud; registration/source receipt; target regions; scale/noise evidence.

Output/check: Region masks and original-point index mapping with sampling/coverage description. Validation: Region includes stated surface evidence without silently removing inconvenient samples.

Dependencies: Open3D point-cloud operations; source geometry/capture metadata.

Resources: Local region/index checks precede full fitting; remote/manual surface classification separate.

Source-supported tools: Open3D segment_plane, Open3D DBSCAN, CloudCompare scalar-field and primitive tools. Original evidence: [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html), [https://github.com/CloudCompare/CloudCompare](https://github.com/CloudCompare/CloudCompare).

### 38. Bind exact CAD and observation-route evidence (REC-12-A01)

Original action: [Bind exact CAD and observation-route evidence](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-12 — Register existing CAD to calibrated photographs or scan points.

Implementation proposal: Proposal: CAD observation binder emits route-specific geometry/control manifests.

Software: Materialize parametric source through an authorized supported generator or consume its checked geometry receipt; query actual landmarks/surfaces.

Agent: Identify source correspondence and whether assembly configuration matches observed object.

Inputs: Measurement-set; one parametric-source/cad-solid; one photo-set/point-cloud/mesh; photo calibration when selected.

Output/check: Route manifest with materialized CAD revision, observation identities, units/frame and fit/check landmarks. Validation: Source text alone cannot provide queried CAD landmarks; photo intrinsics match actual preprocessing.

Dependencies: Point02 CAD identity, point03 generation, REC-02/07/08 appropriate branch.

Resources: Local metadata/required landmarks before tessellation/full cloud; remote/manual association separate.

Source-supported tools: CAD tessellation with named 3D landmarks, OpenCV solvePnPRansac, Open3D global registration and ICP. Original evidence: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html).

### 39. Check literal package inputs and supported URDF tree (DOM-09-A01)

Original action: [Check literal package inputs and supported URDF tree](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-09 — Robot assembly to URDF package.

Implementation proposal: Proposal: URDF preflight emits literal-input receipt, supported tree and per-role readiness.

Software: Validate unique rooted tree, joint types and applicable limits; detect loops; resolve visual/collision/inertial frames independently.

Agent: Interpret adjunct geometry role and source mapping; preserve source literal contract.

Inputs: Robot-assembly, joint-set, mass-properties AND one visual-scene OR collision-set adjunct; assets and target consumer.

Output/check: Link/joint/asset/inertia mapping and consumer-specific missing-role report. Validation: Visual adjunct cannot silently become collision data; fixed/continuous joints receive type-specific range rules.

Dependencies: DOM-08, DOM-12/13/14; selected urdfdom/consumer version.

Resources: Local tree/path/units checks precede mesh reads; remote/manual semantic review separate.

Source-supported tools: URDF XML/Xacro authoring; ROS urdf_tutorial; CAD-to-URDF adapter proposal. Original evidence: [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial), [https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html](https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html), [https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF](https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF).

### 40. Select IFC elements and triangle extraction policy (DOM-16-A01)

Original action: [Select IFC elements and triangle extraction policy](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-16 — Extract IFC geometry as triangles.

Implementation proposal: Proposal: extraction planner emits element IDs, settings and expected output frame/unit contract.

Software: Read IFC units/placements; choose create_shape or iterator and explicit geometry settings.

Agent: Review selection, absent representations and intended opening evaluation.

Inputs: IFC source, selected elements, target use and geometry settings.

Output/check: Element/representation inventory, units/placement/opening policy and mesh criteria. Validation: DOM-16 output is mesh; DOM-27 owns B-rep route despite original broad capability prose.

Dependencies: IfcOpenShell selected build/settings; point05 coordinate chain.

Resources: Local metadata first; selected-element extraction precedes full building; remote review separate.

Source-supported tools: IfcOpenShell geom.create_shape/iterator; IfcConvert. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html).

### 41. Resolve scene input branch and actual adapter (DOM-24-A01)

Original action: [Resolve scene input branch and actual adapter](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-24 — Assemble and inspect Blender scene.

Implementation proposal: Proposal: scene intake emits selected variant, object/camera map and importer prerequisites.

Software: Inspect actual Blender/add-on versions and supported input adapters; pin scene units and transform policy.

Agent: Identify required scene content and source object/element/link associations.

Inputs: One cad-solid/mesh/IFC/robot-assembly/camera-solution route, source assets and requested composition.

Output/check: Adapter/role/source map with unit, frame and camera conventions. Validation: Camera-solution alone validly yields camera-only scene; geometry is required only for dependent checks.

Dependencies: Blender import/scene API; OCS remains engineering source; domain geometry adapters as needed.

Resources: Local metadata/adapter check first; remote/manual composition interpretation separate.

Source-supported tools: Blender Python API; Blender MCP; background Blender scripts. Original evidence: [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/), [https://projects.blender.org/lab/blender_mcp/src/branch/main](https://projects.blender.org/lab/blender_mcp/src/branch/main), [https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst](https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst), [https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0](https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0).

### 42. Bind library asset and target IFC placement meaning (DOM-35-A01)

Original action: [Bind library asset and target IFC placement meaning](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-35 — Place library component in semantic IFC.

Implementation proposal: Proposal: component-to-IFC planner emits source/target identities, required semantics and representation capability.

Software: Inspect asset format and applicable geometry adapter; read target project units/context/placement hierarchy.

Agent: Associate source component role with evidence-supported class and target relationships.

Inputs: IFC, component-record and measurement-set; target class/type/storey/host and placement evidence.

Output/check: Asset-to-IFC representation/semantic plan with rights/source map. Validation: Original inputs do not guarantee target semantics; record linked dependency rather than invent class.

Dependencies: Point02 library intake; selected IFC representation adapter.

Resources: Local source/metadata checks first; remote/manual role interpretation separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html), [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN).

### 43. Resolve literal photo input and cloud detail target (DOM-20-A01)

Original action: [Resolve literal photo input and cloud detail target](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-20 — Photos/video to camera solution, point cloud and mesh.

Implementation proposal: Proposal: domain photo intake distinguishes typed photo input from video upstream and mesh downstream dependencies.

Software: Validate images/camera model through REC-03; require prior video extraction if original source is video.

Agent: Interpret target scene/features and required cloud coverage.

Inputs: Photo-set with provenance/camera state; optional explicitly linked controls and intended sparse/dense use.

Output/check: Input/quality/frame plan and camera/cloud output specification. Validation: Title's video/mesh wording does not alter photo-set→camera-solution+point-cloud contract.

Dependencies: REC-03 and optional REC-17 dense stages.

Resources: Local metadata/source review first; remote/manual coverage choices separate.

Source-supported tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG/OpenMVS. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 44. Declare plan conventions and wall/opening candidates (CAD-05-A01)

Original action: [Declare plan conventions and wall/opening candidates](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-05 — Convert raster floor-plan candidates into a wall and opening graph.

Implementation proposal: Proposal: plan candidate ledger accepts traced vectors/measurements and returns wall/opening roles and convention alternatives.

Software: Inventory candidate wall traces, junctions, opening spans and labels with persistent IDs.

Agent: Interpret wall boundaries, centreline, door/window symbols and curved/nonorthogonal geometry.

Inputs: Raster-plan; CAD-02 measurement-set; CAD-04 candidates or manual traces; plan legend/conventions.

Output/check: Wall edge/centreline convention, candidate walls/openings and source locations. Validation: Semantic review checks each role against full plan/legend; orthogonality is conditional on source constraints.

Dependencies: Research floor-plan methods provide proposals; manual OCS/FreeCAD trace is a documented alternative.

Resources: Local indexed vectors first; remote VLM/manual interpretation for symbols; learned segmentation adds separately recorded weights/runtime/compute.

Source-supported tools: floor-plan segmentation/vectorization model or manual trace, graph consistency checks, OCS or FreeCAD Draft. Original evidence: [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html), [https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf), [https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf).

### 45. Bind all five inputs and element-level building requirements (DOM-18-A01)

Original action: [Bind all five inputs and element-level building requirements](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: DOM-18 — Raster floor plan to IFC building.

Implementation proposal: Proposal: building intake binder emits linked source/control/asset/element manifest and feature prerequisites.

Software: Check input presence/revisions, unit/frame conversions, controls and referenced source-library items.

Agent: Interpret wall/opening/spatial roles against source and intended building use; identify usable CAD-05/CAD-17 receipts.

Inputs: Raster-plan, dimensions, measurement-set, source-library and model-brief; plan orientation, floor datum and interpretation rules.

Output/check: Building intake manifest with all five input revisions, element requirements and source-asset terms. Validation: Each required element has source-backed geometry/semantic prerequisites; library terms attach to actual reused items.

Dependencies: Point01 brief, point02 source-library checks, CAD-02/05 evidence; original five-input contract.

Resources: Local manifests first; remote semantic interpretation and manual evidence acquisition recorded separately.

Source-supported tools: Image calibration; OCS/FreeCAD sketching; Bonsai/IfcOpenShell. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html).

### 46. Freeze initialization and comparison objective (REC-08-A01)

Original action: [Freeze initialization and comparison objective](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-08 — Refine registration and compare point-cloud surfaces.

Implementation proposal: Proposal: refinement preflight emits supported objective, overlap and observability diagnostics.

Software: Validate initialization/overlap and normals; define point-to-point or supported point-to-plane objective and sampling.

Agent: Assess partial overlap, density imbalance, symmetry and unobservable motions.

Inputs: Source/target clouds; measurement-set coarse transform; units; normals/masks; source-backed thresholds.

Output/check: Refinement specification with source-to-target initialization, objective and check configuration. Validation: ICP initialization lies within supported convergence conditions; missing normals or degeneracy creates a named exception.

Dependencies: Open3D ICP/evaluate_registration; CloudCompare distance route.

Resources: Coarse/local checks first; RAM follows sampled points/normals; remote region review separate.

Source-supported tools: Open3D point-to-plane ICP, Open3D evaluate_registration, CloudCompare cloud-to-cloud distance. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode).

### 47. Verify metric evidence and select functional features (CAD-11-A01)

Original action: [Verify metric evidence and select functional features](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: CAD-11 — Fit analytic features to scans or image-derived point clouds.

Implementation proposal: Proposal: analytic-fit intake emits feature/support/criteria manifest and unresolved prerequisites.

Software: Check metric registration; derive source-linked metric samples from supported depth/mesh route; reuse REC-09 regions when matching.

Agent: Identify functional plane/cylinder/axis and distinguish observations from nominal/hidden geometry.

Inputs: One declared depth-frame/point-cloud/mesh route plus measurement-set; source scale/frame; registration and independent controls.

Output/check: Feature fit plan with sample membership, observation coverage and dimension provenance. Validation: Unregistered or scale-ambiguous data cannot support metric feature dimensions.

Dependencies: REC-09 evidence; supported calibrated-depth/mesh sampling adapter; point03 construction contract.

Resources: Local source/control preflight precedes fitting; remote/manual feature identification recorded.

Source-supported tools: point-cloud registration and segmentation, least-squares plane/cylinder/axis fits, FreeCAD/build123d. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [/home/leo/projects/architecture/research/README.md](/home/leo/projects/architecture/research/README.md).

### 48. Bind sketch view, camera and hit surface (REC-13-A01)

Original action: [Bind sketch view, camera and hit surface](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-13 — Anchor a screen sketch to a 3D surface.

Implementation proposal: Proposal: anchor intake emits camera/ray conventions, surface selection and feature prerequisites.

Software: Validate image/camera compatibility; materialize evaluated geometry and record transform/face-index mapping.

Agent: Interpret intended target surface versus visible occluder and whether projection is perspective or orthographic.

Inputs: Raster-sketch; camera-solution; selected mesh/cad-solid; view/image mapping and units.

Output/check: Anchor manifest with camera/view/geometry revision, target components and stroke meaning. Validation: View or geometry mismatch invalidates anchor prerequisites; a screenshot alone cannot establish intended depth.

Dependencies: Fresh official Blender RNA source documents Scene.ray_cast in world space and Object.ray_cast in object space on evaluated geometry; pin actual installed release/signature before use.

Resources: Local metadata/selected geometry first; remote/manual target interpretation recorded.

Source-supported tools: Blender Scene.ray_cast, screen-to-camera ray projection, OpenCV projectPoints, OCS constrained sketch. Original evidence: [https://docs.blender.org/api/current/bpy.types.Scene.html](https://docs.blender.org/api/current/bpy.types.Scene.html), [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html).

### 49. Bind source revisions, datums and discrepancy purpose (REC-15-A01)

Original action: [Bind source revisions, datums and discrepancy purpose](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-15 — Reconcile scan surfaces with dimensioned drawings.

Implementation proposal: Proposal: reconciliation intake emits paired feature sources, datum choices and separate fit/check roles.

Software: Check units/revisions, materialize drawing feature records and identify matching scan regions.

Agent: Interpret nominal, tolerance, manufactured condition and fit meaning; avoid matching unrelated revisions.

Inputs: Measurement-set; selected cloud/mesh; selected vector/raster drawing; known revisions/units; common datum evidence.

Output/check: Feature correspondence and datum/control manifest with nominal/observed evidence classes. Validation: Revision/configuration mismatch is explicit; raster pixel estimates do not replace printed dimension values.

Dependencies: Point04 drawing interpretation; REC-07/08 registration; source measurement ledger.

Resources: Local source/feature inventory first; remote/manual meaning review separate.

Source-supported tools: CAD drawing datums, Open3D/CloudCompare registration and distance map, OCS constrained sketch. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode).

### 50. Resolve scan, building and survey frame definitions (DOM-19-A01)

Original action: [Resolve scan, building and survey frame definitions](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: DOM-19 — Register scan to building frame.

Implementation proposal: Proposal: building-frame resolver emits explicit unit/placement/map chains and control sufficiency.

Software: Read actual IFC placements/units; compose hierarchy and supplied map conversion; inspect control geometry/observable freedoms.

Agent: Identify intended building datum and matching physical features; distinguish local frame from geographic reference.

Inputs: IFC; measurement-set distributed controls; point-cloud; sensor/scale evidence; project units, local placements and any supplied CRS/map conversion.

Output/check: Frame manifest naming scan, IFC local/building and survey/map frames with transform dependencies. Validation: Blank georeference entities supply no coordinates; one datum plus insufficient control geometry cannot determine all pose freedoms.

Dependencies: IfcOpenShell read/placement/georeference APIs; actual sensor calibration and REC-07 prerequisites.

Resources: Local IFC/control parsing first; remote/manual datum/source review separate.

Source-supported tools: COLMAP/AliceVision; Open3D/CloudCompare; IFC geometry as reference. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 51. Bind assembly occurrences and motion evidence (DOM-31-A01)

Original action: [Bind assembly occurrences and motion evidence](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-31 — Author assembly graph and joint set.

Implementation proposal: Proposal: graph intake maps occurrence IDs, source evidence and candidate rigid groups without editing source geometry.

Software: Read OCS native occurrence/placement data where supported; use the point02 assembly adapter contract for richer assembly records.

Agent: Associate actual rigid parts and intended movable relations; preserve alternatives when geometry admits several meanings.

Inputs: CAD assembly, measurement-set and model-brief; occurrence IDs/placements and component revisions.

Output/check: Occurrence-to-rigid-group candidates and named motion/interface evidence. Validation: Every occurrence is mapped or explicitly excluded; fixed relation needs evidence.

Dependencies: Point02 component/assembly records; actual selected application's occurrence capability.

Resources: Local metadata/transform reads scale with occurrences; remote interpretation and manual joint identification recorded separately.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial).

### 52. Bind sourced component to target robot role (DOM-37-A01)

Original action: [Bind sourced component to target robot role](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-37 — Author robot assembly from CAD component.

Implementation proposal: Proposal: attachment intake emits source component, parent context and unresolved interface dependencies.

Software: Read solid geometry and component metadata; check target frame/parent references exist.

Agent: Match named mount faces/axes to required component role.

Inputs: Cad-solid, measurement-set, model-brief and component-record; target parent/frame from brief or supplied assembly context.

Output/check: Component/target manifest and sourced attachment plan. Validation: A standalone component cannot silently invent the remainder of a robot or its parent transform.

Dependencies: Point02 intake/placement and native OCS geometry; alternate assembly backend requires scoped capability.

Resources: Local identity/bounds queries precede modeling; remote/manual interface interpretation recorded.

Source-supported tools: FreeCAD Assembly Workbench or explicit CAD assembly authoring. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial).

### 53. Bind native model roles and compiler policy (DOM-11-A01)

Original action: [Bind native model roles and compiler policy](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-11 — Author native MJCF simulation model.

Implementation proposal: Proposal: MJCF intake emits complete role/physical/source map and required model decisions.

Software: Validate body tree and role maps; inventory closure edges and effective inertiafromgeom/default settings. Record MJCF compiler/angle default degrees versus URDF radians and selected consistent physical units.

Agent: Interpret physical versus visual material and requested dynamics semantics.

Inputs: Robot-assembly, joint-set, collision-set, mass-properties, material-set and intended simulation scope.

Output/check: Body/joint/geom/inertial mapping and explicit compiler/unit/closure policy. Validation: Required physical fields have evidence; visual/collision replacements cannot silently alter inferred mass.

Dependencies: DOM-08/13/14 and pinned MJCF XML reference.

Resources: Local graph/property checks first; remote/manual modeling choices separately recorded.

Source-supported tools: MuJoCo MJCF XML and mjSpec API. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst).

### 54. Pin seed model and map CAD occurrences to bodies (DOM-32-A01)

Original action: [Pin seed model and map CAD occurrences to bodies](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-32 — Map CAD link geometry to MJCF body tree.

Implementation proposal: Proposal: seed mapper emits body/occurrence correspondence, invariants and affected physics dependencies.

Software: Parse seed and inspect effective compiled mappings; record inertia inference, fusion and mesh transforms.

Agent: Match exact robot configuration and source occurrence to body; identify visual/collision replacement role.

Inputs: MJCF, CAD assembly, joint-set, measurement-set and component-record; per-asset rights and body map.

Output/check: Seed topology/actuator/sensor/physics snapshot and CAD-to-body mapping. Validation: DOM-32 preserves existing topology; seed mismatch cannot silently route to a rebuilt model.

Dependencies: Pinned model/source terms; DOM-08/12/14 evidence and selected compiler.

Resources: Local parse/frame checks first; source geometry queries by mapped bodies; remote/manual association separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst).

### 55. Bind BIM-derived mesh and collider identities (DOM-34-A01)

Original action: [Bind BIM-derived mesh and collider identities](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-34 — Author static MuJoCo environment from BIM mesh.

Implementation proposal: Proposal: BIM-environment intake emits static role/coverage and source-frame contract.

Software: Check mesh/collider lineage and element coverage; resolve local/project/map-to-world chain.

Agent: Associate building elements, geometric holes and required passage/contact regions.

Inputs: Mesh and collision-set with IFC source/element mapping, units and frame lineage.

Output/check: Element-to-mesh-to-piece map and simulation-world placement/coverage plan. Validation: BIM lineage is required for this operation's stated provenance; generic mesh can use a separately declared generic environment route.

Dependencies: DOM-16/17 source maps, DOM-13 colliders and point05 frame evidence.

Resources: Local metadata/frame checks first; remote/manual element interpretation separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst).

### 56. Bind mandatory depth and measurement evidence (DOM-21-A01)

Original action: [Bind mandatory depth and measurement evidence](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-21 — Depth frames to registered point cloud or mesh.

Implementation proposal: Proposal: depth-domain intake emits mandatory-input receipt and point-cloud prerequisites.

Software: Validate sensor data through REC-05 intake; resolve metric frame controls and required coverage.

Agent: Associate measurement targets with observed depth surfaces.

Inputs: Depth-frames AND measurement-set, sensor calibration/timing and available pose source.

Output/check: Control/calibration/frame plan for registered point-cloud. Validation: Original output is point-cloud; mesh title wording is recorded as a separate downstream branch.

Dependencies: REC-05 and point05 control/frame procedures.

Resources: Local metadata/control checks first; manual sensor/target acquisition separate.

Source-supported tools: Open3D; CloudCompare. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 57. Bind supplied cameras and required surface outputs (DOM-28-A01)

Original action: [Bind supplied cameras and required surface outputs](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-28 — Dense multi-view stereo to point cloud and mesh.

Implementation proposal: Proposal: domain dense planner emits image/camera/settings and cloud/mesh dependency graph.

Software: Reuse REC-17 workspace preflight; inspect backend output types and required coverage.

Agent: Associate requested surfaces with captured evidence.

Inputs: Photo-set AND camera-solution, intended surface use and linked scale/control evidence.

Output/check: Camera/image/frame validation receipt and both-output requirements. Validation: Calibrated intrinsics alone do not establish unrelated scene scale.

Dependencies: REC-17 documented dense/meshing routes.

Resources: Local manifest/control review before dense processing; remote/manual capture decisions separate.

Source-supported tools: COLMAP dense reconstruction; AliceVision/Meshroom; OpenMVS. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 58. Inspect point evidence normals and meshing assumptions (DOM-29-A01)

Original action: [Inspect point evidence normals and meshing assumptions](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-29 — Point cloud to surface mesh.

Implementation proposal: Proposal: meshing intake emits validated geometric point set, normal lineage and method prerequisites.

Software: Inspect PLY/other fields; reject Gaussian rendering parameters as measured surface cloud; estimate/orient normals where method requires and retain neighborhood settings. Open3D orient_normals_consistent_tangent_plane(k) propagates neighbour consistency; check outward/side orientation against capture evidence separately.

Agent: Review open boundaries, thin surfaces, gaps and physical feature association.

Inputs: Point-cloud with actual field schema, source/frame/scale, density/noise and observed-region evidence.

Output/check: Method/normal/filter plan and source-point membership map. Validation: Gaussian PLY centers/covariances/opacity require separately defined surface extraction before this geometry route.

Dependencies: Pinned Open3D surface/normal APIs; source-typed geometry adapter.

Resources: Local schema/density checks and bounded regions before full meshing; normal search scales with samples/neighborhood.

Source-supported tools: Open3D surface reconstruction; CloudCompare mesh reconstruction; Blender mesh cleanup. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 59. Resolve source and target interface identities (DOM-07-A01)

Original action: [Resolve source and target interface identities](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-07 — Place reusable component in assembly.

Implementation proposal: Proposal: datum resolver requiring explicit source/target frame direction and occurrence identity.

Software: Read pinned component and assembly revisions; resolve graph nodes and measurement references; check units.

Agent: Interpret feature correspondence using source views; VLM selects the source-supported mapping while preserving alternative interpretations.

Inputs: Component-record; required assembly-graph; measurement-set; source/target datum IDs, geometry revisions and stated mating relation.

Output/check: Interface correspondence and placement prerequisites, consumed by DOM-07-A02. Validation: Verify all measurement references belong to pinned revisions; separate semantic reviewer checks centre/edge, axis sign and component occurrence.

Dependencies: Native measurement/frame APIs; OCS contract; existing assembly-graph records.

Resources: Local identity/measurement queries first; CPU/RAM depends on queried geometry. Remote VLM uses bounded cited views; record manual datum decisions.

Source-supported tools: OCS; FreeCAD Assembly Workbench; native CAD assembly API. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 60. Inspect STEP identity, structure and unit evidence (DOM-38-A01)

Original action: [Inspect STEP identity, structure and unit evidence](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-38 — Import STEP solid into CAD representation.

Implementation proposal: Proposal: STEP preflight inspector reporting referenced unit contexts, topology/entity families and product structure.

Software: Read header/schema and entity references using a supported STEP parser; inventory product/occurrence structure and referenced unit contexts.

Agent: Interpret whether the task needs analytic faces, faceted geometry, individual solids or product hierarchy.

Inputs: Original STEP bytes plus DOM-06-A01/A02 identity/rights receipt or equivalent retained source record; schema/header, declared units/product structure and known interface dimensions. A completed component-record is not an import prerequisite.

Output/check: STEP intake manifest and expected invariants, consumed by DOM-38-A02. Validation: Validate header/entity references and control dimensions; classify analytic, faceted and mixed data from actual entities, retaining uncertainty on unsupported entities.

Dependencies: Existing original STEP and partial identity/rights receipt; selected parser/reader with known schema support; OCS step.rs is exporter source evidence.

Resources: Local file/header inspection first; full entity parsing scales with file size. Remote review handles schema/use or source ambiguity; record manual interpretation.

Source-supported tools: FreeCAD/Open CASCADE STEP adapter. Original evidence: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md).

### 61. Inspect CSG source, parameters and mesh criteria (CAD-15-A01)

Original action: [Inspect CSG source, parameters and mesh criteria](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-15 — Render source-defined CSG as a mesh.

Implementation proposal: Proposal: source/render manifest and parameter/dependency validator.

Software: Inspect source/dependency references, supported syntax/backend and resolution controls; record render versus preview route and export settings.

Agent: Confirm CSG operation meaning, separate parts and required holes/features before rendering.

Inputs: OpenSCAD parametric-source; dependencies/licences; parameters; units; target mesh format; feature and approximation criteria.

Output/check: Render/export configuration and pinned source package for CAD-15-A02. Validation: Check parameter/dependency completeness and exact intended CSG interpretation; reviewer verifies source feature correspondence.

Dependencies: Documented OpenSCAD language/render/export interfaces; actual installed version/backend discovered in future execution.

Resources: Local source inspection precedes rendering; complexity follows CSG tree and dependencies. Remote reasoning reviews ambiguous source intent; manual parameter decisions recorded.

Source-supported tools: OpenSCAD, STL/3MF mesh export. Original evidence: [https://openscad.org/documentation](https://openscad.org/documentation).

### 62. Choose the profile target and source entity mapping (DOM-03-A01)

Original action: [Choose the profile target and source entity mapping](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-03 — DXF/SVG drawing to constrained profile.

Implementation proposal: Proposal: profile route selector exposing actual output type and required source/constraint inputs.

Software: Inspect source and importer coverage; map entity-to-loop IDs and explicit target constraint representation.

Agent: Select supported sketch route; identify profile-only import and CSG extrusion as alternatives with their actual output type.

Inputs: Original vector-drawing; units/spaces/layers/blocks; target plane; model-brief or explicit source dimensions/relations.

Output/check: Profile/constraint contract and CAD-08/CAD-09 prerequisites for DOM-03-A02. Validation: Confirm all promised constrained-sketch fields have an actual implementation path; CadQuery import/OpenSCAD extrusion alone is classified as profile/CSG.

Dependencies: CAD-08 vector preparation and CAD-09 constrained sketch; FreeCAD Sketcher documented route.

Resources: Local entity/metadata checks first; remote VLM handles loop/label meaning and manual output choices.

Source-supported tools: OpenCADStudio; FreeCAD Sketcher; CadQuery DXF import; OpenSCAD DXF linear_extrude. Original evidence: [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 63. Define native artifact and solid prerequisites (DOM-04-A01)

Original action: [Define native artifact and solid prerequisites](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-04 — Brief/profile to native CAD solid.

Implementation proposal: Proposal: native-artifact contract mapper separating native document, parametric source, B-rep and mesh.

Software: Inspect required feature support and native document capability; identify whether code source alone or a native document is requested.

Agent: Choose supported interactive or procedural construction while preserving source history and component boundaries.

Inputs: Model-brief, constrained-sketch or compatible parametric-source; explicit dimensions/datums/parts; native editability requirement.

Output/check: Native/solid delivery contract and construction prerequisites for DOM-04-A02. Validation: An OpenSCAD source/mesh route is explicitly CAD-15; it supplies no automatic cad-solid/native feature-history claim.

Dependencies: OCS native body/document; FreeCAD feature document; CAD-10 and DOM-40 routes with their actual outputs.

Resources: Local contract/capability reading precedes modeling. Remote agent/manual effort resolves intent and representation choices.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md), [ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md). Source-defined feature route and component representation decisions.

Source-supported tools: OpenCADStudio baseline; FreeCAD; CadQuery; build123d; OpenSCAD. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs).

### 64. Bind the solid export to representation and consumer criteria (DOM-05-A01)

Original action: [Bind the solid export to representation and consumer criteria](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-05 — Export STEP solid.

Implementation proposal: Proposal: solid-export capability/criteria planner with source-to-output field mapping.

Software: Inspect source body/surface types and exporter options; record actual unit/precision and tessellation behavior.

Agent: Choose analytic-preserving or explicitly faceted route matching the task; identify native history and source identity preservation requirements.

Inputs: Cad-solid or B-rep; native source revision/hash; units/frame; required surfaces/features; target consumer/schema and output path.

Output/check: Solid-export contract for DOM-05-A02. Validation: Exporter can satisfy required representation or reports the precise alternative; no source STEP bytes are invented for native-only input.

Dependencies: Selected FreeCAD/OCCT/CadQuery export capability; OCS mesh writer is a distinct inspected faceted route.

Resources: Local metadata/shape inspection first; export cost follows surfaces/triangles. Remote/manual review addresses consumer and representation requirements.

Source-supported tools: OCS STEP exporter; FreeCAD/Open CASCADE STEP import/export. Original evidence: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs).

### 65. Define sourced parameters and the executable model contract (DOM-40-A01)

Original action: [Define sourced parameters and the executable model contract](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-40 — Script-parametric CAD authoring.

Implementation proposal: Proposal: parametric model-brief skill and contract validator with actual output-type gate.

Software: Check parameter names/types/units and declared ranges where sourced; inspect chosen library/version capabilities.

Agent: Choose stable datums and source-supported feature sequence; distinguish B-rep backend from OpenSCAD CSG/mesh output.

Inputs: Model-brief; sourced dimensions/units/datums; separate parts; output contract; dependency/licence requirements.

Output/check: Parameter/feature program specification for DOM-40-A02. Validation: Parameter coverage and output type match the brief; source code alone is not a generated cad-solid result.

Dependencies: CadQuery/build123d/FreeCAD documented APIs; OpenSCAD source route enters CAD-15 for mesh output.

Resources: Local metadata/API inspection first; high-reasoning model can interpret complex intent. Record remote calls and manual parameter decisions separately.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md), [ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md). Source-defined feature route and component representation decisions.

Source-supported tools: CadQuery; build123d; OpenSCAD; FreeCAD Python. Original evidence: [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 66. Bind graph elements to sourced vertical parameters (CAD-17-A01)

Original action: [Bind graph elements to sourced vertical parameters](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-17 — Build wall and opening solids from a confirmed floor-plan graph.

Implementation proposal: Proposal: wall feature planner emits explicit wall/cutter construction records and feature-level blocking dependencies.

Software: Check mandatory values, host IDs, unit conversions, wall-local frames and supported curve types.

Agent: Interpret edge/centreline offsets and opening meaning; distinguish void/cutter representation from a physical component.

Inputs: Reviewed CAD-05 vector graph; measurement-set; model-brief with floor datum, wall height/thickness convention and opening widths/heights/sills.

Output/check: Per-wall/opening feature plan with units/frame, host IDs and complete or blocked parameter states. Validation: Required heights/thicknesses/opening parameters come from sources or explicit decisions; no values are filled from plan appearance.

Dependencies: CAD-05 graph and point01 brief; CAD-10 supported native features and point02 assembly identity rules.

Resources: Local graph/parameter checks first; remote interpretation for junctions/offsets; manual missing-parameter acquisition separate.

Source-supported tools: FreeCAD Part/Sketcher or OCS native geometry, wall/opening graph interpretation, human confirmation. Original evidence: [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html), [https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf), [https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md).

### 67. Specify raster-backed sketch requirements (DOM-02-A01)

Original action: [Specify raster-backed sketch requirements](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: DOM-02 — Raster sketch to constrained sketch.

Implementation proposal: Proposal: raster-sketch intake emits feature/constraint requirements and source-evidence prerequisites.

Software: Check raster presence and whether scale model/control geometry suffice; inspect selected sketch backend capabilities.

Agent: Determine which source features need constraints and which strokes are schematic.

Inputs: Raster-sketch plus dimension/measurement prerequisites; source plane/orientation; intended profiles/features and criteria.

Output/check: Sketch intake record with source hash, controls, required constraints and route selection. Validation: Dimension-only material routes to point01/point03; this raster procedure retains actual raster evidence.

Dependencies: CAD-02/03/04 and CAD-09 contracts; original DOM-02 raster input plus stated control prerequisite.

Resources: Local metadata first; higher reasoning for freehand intent; manual controls and remote effort recorded.

Source-supported tools: OpenCADStudio; FreeCAD Sketcher; manual image tracing. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 68. Bind both clouds and declare transform freedoms (REC-07-A01)

Original action: [Bind both clouds and declare transform freedoms](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-07 — Estimate coarse transform between point clouds.

Implementation proposal: Proposal: cloud preflight emits role/frame/model manifest, masks and observability prerequisites.

Software: Check unit/frame compatibility, sample coverage and geometric degeneracy; make bounded coarse derivatives with original-index mapping.

Agent: Identify static overlap, symmetries and observable translations/rotations/scale.

Inputs: Distinct source and target cloud revisions; units/frames; overlap/static-region masks; independent controls.

Output/check: Registration manifest with source-to-target direction, rigid or justified similarity model and fit/check regions. Validation: A planar/repetitive region cannot silently constrain all pose freedoms; source and target remain distinct.

Dependencies: Open3D global registration; original two input_roles preserved.

Resources: Local coarse sampling first; point count controls RAM; remote/manual overlap interpretation separate.

Source-supported tools: Open3D FPFH, Open3D RANSAC global registration, CloudCompare alignment. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html).

### 69. Audit literal input contract and target remodeling meaning (DOM-23-A01)

Original action: [Audit literal input contract and target remodeling meaning](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: DOM-23 — Scan or mesh to parametric CAD remodeling.

Implementation proposal: Proposal: remodeling intake distinguishes literal four-input route from separately proposed true alternative or explicit sampled-cloud route.

Software: Verify literal inputs; if explicit mesh-sampling conversion is scoped, produce source-indexed cloud derivative before satisfying cloud role; do not silently treat name as schema.

Agent: Interpret observed geometry, intended function and whether nominal/idealized feature source exists.

Inputs: Literal existing record requires point-cloud, measurement-set and model-brief plus its mesh alternative entry: preserve all four supplied inputs for that contract.

Output/check: Input/lineage manifest, target use/interface criteria and explicit route status; proposed true cloud-or-mesh interpretation recorded separately. Validation: Title 'scan or mesh' does not erase mandatory fields; each conversion retains original source and explicit information changes.

Dependencies: Original DOM23 record, point02 identity, CAD11/REC14 evidence and source conversion scope.

Resources: Local manifests first; sampling if later authorized has explicit size/compute; remote/manual intent review separate.

Source-supported tools: Open3D/CloudCompare measurement; OCS baseline; FreeCAD/OCCT solid modeling. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 70. Inventory URDF import policy and expected losses (DOM-10-A01)

Original action: [Inventory URDF import policy and expected losses](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-10 — URDF import and MJCF conversion.

Implementation proposal: Proposal: conversion preflight emits effective compiler options and field/default/loss expectations.

Software: Resolve assets and inspect URDF/extensions; record discardvisual/fusestatic and inertia inference policy.

Agent: Review source semantics and whether fixed-body fusion preserves required identity mapping.

Inputs: URDF and mesh inputs, source mapping, selected MuJoCo version/compiler settings.

Output/check: Import contract with expected body/geom/joint/property mappings and defaults. Validation: Changed counts need explicit mapping; source unsupported fields remain visible.

Dependencies: DOM-09 package; documented MuJoCo decoder/compiler APIs for selected version.

Resources: Local XML/assets inventory precedes compile; semantic review separate.

Source-supported tools: MuJoCo URDF parser/compiler; mjSpec API. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst).

### 71. Resolve building schema units hierarchy and element evidence (DOM-15-A01)

Original action: [Resolve building schema units hierarchy and element evidence](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-15 — Author semantic IFC building.

Implementation proposal: Proposal: semantic intake emits required element/property/relationship records and per-element readiness.

Software: Validate required brief fields; plan project/site/building/storey aggregation, containment and geometric contexts.

Agent: Associate source geometry with supported IFC classes and relationships.

Inputs: Model-brief with source dimensions, element classes/properties, spatial hierarchy, frames and representation requirements.

Output/check: IFC schema/context/unit/spatial plan and source-element mapping. Validation: Shape appearance cannot supply semantic class or hidden dimensions; CRS values require source survey evidence.

Dependencies: Point01 brief; IfcOpenShell/Bonsai capability for selected schema.

Resources: Local metadata/schema checks first; remote/manual semantic interpretation separate.

Source-supported tools: Bonsai; IfcOpenShell API. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html).

### 72. Resolve IFC kernel shape extraction requirements (DOM-27-A01)

Original action: [Resolve IFC kernel shape extraction requirements](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-27 — Extract IFC geometry as OpenCASCADE B-rep.

Implementation proposal: Proposal: B-rep preflight emits supported shape classes and explicit backend/import dependencies.

Software: Inspect selected geometry library and non-triangulated/PythonOCC return capability for actual build.

Agent: Review whether faceted source can satisfy requested shape meaning.

Inputs: IFC source, element selection, required shape class and kernel/settings.

Output/check: Element-to-kernel plan with source schema/units/placements and dependencies. Validation: B-rep may remain faceted; extraction cannot restore missing source analytic intent.

Dependencies: IfcOpenShell geometry settings and selected OpenCASCADE/PythonOCC dependencies.

Resources: Local capability/metadata checks precede shape evaluation; manual interpretation separate.

Source-supported tools: IfcOpenShell geom.create_shape/iterator using OpenCASCADE kernel. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html).

### 73. Bind model revision to fabrication requirements (DOM-25-A01)

Original action: [Bind model revision to fabrication requirements](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-25 — Create fabrication package.

Implementation proposal: Proposal: fabrication planner emits part/feature/datum/requirement coverage and supported output matrix.

Software: Inspect actual native geometry and OCS drawing/export capabilities; inventory recipient formats and annotation support.

Agent: Associate dimension/tolerance/material notation with actual manufacturing feature and process.

Inputs: Dimensions and material-set AND cad-solid OR cad-assembly; process/recipient requirements and sourced tolerances.

Output/check: Part/drawing/export plan with datum, feature, material and revision mapping. Validation: Source geometry and materials alone cannot complete missing process/tolerance requirements.

Dependencies: Point03 native/readback; actual OCS exporter capability; optional CAD drawing adapter separately scoped.

Resources: Local feature/requirement inventory first; manual engineering decisions separate.

Source-supported tools: Native CAD drawing/workbench; STEP/DXF/PDF exporters. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 74. Inventory video timing camera state and coverage (REC-04-A01)

Original action: [Inventory video timing camera state and coverage](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-04 — Convert video into an image reconstruction dataset.

Implementation proposal: Proposal: video intake emits stream/timebase/camera/rights records and selection plan.

Software: Use supported ffprobe/decoder metadata inspection; inventory resolution/rate/rotation and variable timing.

Agent: Identify static scene, viewpoint changes, occlusion and moving content.

Inputs: Original video, stream/timebase metadata, camera state, rights and intended scene/use.

Output/check: Source hash/stream manifest, scene intervals and frame-selection criteria. Validation: Frame rate alone cannot reconstruct variable presentation timestamps; physical capture and synthetic frames remain labelled.

Dependencies: Pinned video metadata/decoder API; exact source inspection needed before adapter execution.

Resources: Local metadata then low-resolution review before full decode; remote/manual scene review separately recorded.

Source-supported tools: ffmpeg frame extraction, blur/duplicate-frame filtering, COLMAP or Meshroom downstream. Original evidence: [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md), [https://github.com/nerfstudio-project/nerfstudio](https://github.com/nerfstudio-project/nerfstudio).

### 75. Bind complete photo and metric-control contract (CAD-16-A01)

Original action: [Bind complete photo and metric-control contract](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: CAD-16 — Reconstruct camera poses and dense visible geometry from overlapping photos.

Implementation proposal: Proposal: reconstruction planner emits source/control plan and prerequisites for all three outputs.

Software: Validate capture/calibration through REC-03 intake and measurements through point01/05 contracts.

Agent: Associate controls with visible physical features and requested CAD-reference scope.

Inputs: Photo-set AND measurement-set; intended feature use, camera state and capture/control lineage.

Output/check: Dataset/control/frame plan selecting sparse and dense stages. Validation: Original contract requires all three outputs; inferred hidden geometry retains its evidence label.

Dependencies: REC-03, REC-17/DOM-28 and source-backed backend capabilities.

Resources: Local input/control review first; expensive dense work waits for sparse/control checks.

Source-supported tools: COLMAP or AliceVision/Meshroom, scale/control-point alignment. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [https://github.com/colmap/colmap](https://github.com/colmap/colmap), [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst).

### 76. Bind learned reconstruction variant, images and camera roles (REC-10-A01)

Original action: [Bind learned reconstruction variant, images and camera roles](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-10 — Estimate multi-view depth, camera poses and Gaussian outputs.

Implementation proposal: PROPOSAL learned-input planner: image/video manifest + selected model card/config → exact input/output manifest, camera policy, expected coordinate/scale record and blocked conditions.

Software: Inspect selected DA3 entrypoint/version, export settings and checkpoint support; streaming configuration must actually emit intrinsics/poses plus cloud to fulfill this operation.

Agent: Reason about coverage, moving regions, candidate model variant and semantic feature/control associations using full views and mapped crops.

Inputs: Photo-set OR video as the literal alternative; video first supplies REC-04 frame manifest; checkpoint/config, model card, image rights, masks and available calibration/control records.

Output/check: Inference manifest with source/generated origin, variant/checkpoint hash, processed image mapping, supplied-versus-estimated camera policy, output names and scale status. Validation: Check literal one-of input, all files/revisions, rights references and actual model export contract; a GLB-only example cannot complete camera-solution plus point-cloud.

Dependencies: REC-04 for video; REC-01/02 camera checks and point-01 brief where supplied; model/code/checkpoint/input rights records.

Resources: Metadata and a minimal representative subset first; record image count/resolution/chunk overlap and actual backend/GPU/VRAM conditions before full inference; remote VLM calls and manual masks separately.

Source-supported tools: Depth Anything 3, DA3-Streaming, DA3 Blender add-on. Original evidence: [https://github.com/ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3), [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md), [https://github.com/xy-gao/DA3-blender](https://github.com/xy-gao/DA3-blender).

### 77. Select one source image and a mesh-producing model contract (REC-18-A01)

Original action: [Select one source image and a mesh-producing model contract](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-18 — Generate a single-image mesh proxy.

Implementation proposal: PROPOSAL proxy-input planner: chosen image/mask + model specification + intended use → generation request, output type and visible/inferred region map.

Software: Inspect exact model interface/checkpoint/output and preprocessing; TRELLIS.2 pipeline returns mesh and optional GLB; keep SAM Gaussian route outside a direct mesh completion claim.

Agent: VLM selects source-supported foreground/mask and explains occlusion/shape ambiguities; inspect full image beside crops.

Inputs: Photo-set containing the explicitly selected image, object/mask identity, image source/rights, chosen model/checkpoint and intended-use brief.

Output/check: Single-image generation manifest with mask/preprocessing, generated-region policy, model/output contract and resource conditions. Validation: Input selection remains explicit; actual source image rather than a rendered substitute is identified; unsupported Gaussian-only output cannot satisfy mesh.

Dependencies: Photo-set source identity; mask lineage; code/checkpoint/dependency/input rights; actual GPU support.

Resources: Start with source/mask inspection; source claims TripoSR default about 6 GB VRAM, TRELLIS.2 Linux/NVIDIA>=24 GB and SAM Objects>=32 GB apply to exact setups, not local capacity results.

Source-supported tools: TripoSR, TRELLIS.2, SAM 3D Objects. Original evidence: [https://github.com/VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR), [https://github.com/microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2), [https://github.com/facebookresearch/sam-3d-objects](https://github.com/facebookresearch/sam-3d-objects).

### 78. Freeze the native assembly and export contract (DOM-39-A01)

Original action: [Freeze the native assembly and export contract](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-39 — Export STEP assembly.

Implementation proposal: Proposal: export contract builder with exact definition/occurrence and per-feature invariant sets.

Software: Read component/occurrence tree, transforms, units, shape types and rights dependencies; freeze source revision/hashes.

Agent: Map required native fields to STEP product/geometry fields and identify representation-specific changes.

Inputs: Native assembly revision; component pins; output schema/consumer; item terms; required names, occurrence hierarchy, units and geometry properties.

Output/check: Export manifest and per-field preservation requirements, consumed by DOM-39-A02. Validation: Check manifest matches the native assembly and every required component has rights/provenance; independent reviewer checks occurrence versus definition meaning.

Dependencies: Native assembly reader; component/version records; selected consumer's supported STEP route.

Resources: Local tree/hash inspection first; no geometry conversion. Remote/manual review addresses consumer meaning and export scope.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Documented exact part/revision, representation, source dependency and reproduction-package records; serialization/automation follows each action.

Source-supported tools: FreeCAD/Open CASCADE STEP adapter. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 79. Reconcile the failed operation and preserve its evidence (CAD-14-A01)

Original action: [Reconcile the failed operation and preserve its evidence](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-14 — Recover from failed interpretation or geometry construction.

Implementation proposal: Reuse execute_checked and same-request-ID operation lookup; add a durable per-operation reconciliation record, bounded polling and partial-effect/command-state tests.

Software: Query the same operation identity after timeout; read document revision/handles and partial output without replaying mutations.

Agent: Compare actual state with intended transition and locate which steps committed.

Inputs: Model-brief; verification-report naming failed transition/artifact; request/document/revision IDs; logs and partial outputs.

Output/check: Reconciled failure receipt and unchanged evidence set for CAD-14-A02. Validation: Verify reported failure refers to the observed artifact/revision; independent reviewer checks the diagnostic source boundary.

Dependencies: OCS operation-status and revision protocol; backend logs; saved artifact/hash records.

Resources: Local logs/state/hash work precedes new geometry. Remote reasoning examines evidence; manual effort resolves only source/scope ambiguity.

Reuse: [ocs_control.py](/home/leo/.codex/skills/ocs-engineering/scripts/ocs_control.py), [ngv064_ocs.py](/tmp/opencode/ngv064_ocs.py), [cad-workflow-findings.md](/home/leo/projects/ferme/skills/cad-workflow-findings.md). One-send transport/WriteUncertain and request-ID lookup; reconcile entity effects separately from command state.

Source-supported tools: source overlay, operation logs, constraint residuals, OCS operation status/revision readback, CAD kernel validity reports. Original evidence: [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md), [/home/leo/projects/energy/eoliennes/research/cad-workflow/harness-findings.md](/home/leo/projects/energy/eoliennes/research/cad-workflow/harness-findings.md), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md).

### 80. Bind photographs, target evidence and camera state (CAD-02B-A01)

Original action: [Bind photographs, target evidence and camera state](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: CAD-02B — Calibrate camera poses from photographs and known controls.

Implementation proposal: Proposal: calibration intake emits camera groups, target roles and per-image prerequisites.

Software: Check dimensions, target coordinates, image resolution and control-role completeness.

Agent: Identify camera grouping and whether existing calibration matches the actual images.

Inputs: Photo-set; measurement-set; camera/lens/focus state; original pixel grid and preprocessing.

Output/check: Camera/image/control manifest selecting REC-01 and REC-02 prerequisites. Validation: Calibration covers the actual image/lens state; transformed images retain compatible intrinsics/distortion mapping.

Dependencies: OpenCV calibration/PnP documented inputs; point04 image mapping records.

Resources: Local manifests first; remote/manual point identification recorded separately.

Source-supported tools: OpenCV findChessboardCorners, OpenCV calibrateCamera, OpenCV solvePnP. Original evidence: [https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html), [https://docs.opencv.org/5.0/main_modules/calib.html](https://docs.opencv.org/5.0/main_modules/calib.html).

### 81. Bind 3D landmarks to calibrated image coordinates (REC-02-A01)

Original action: [Bind 3D landmarks to calibrated image coordinates](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-02 — Solve camera pose from known 3D-to-2D correspondences.

Implementation proposal: Proposal: PnP preflight returns compatible correspondences and ambiguous/unobservable components.

Software: Validate point count/configuration for selected PnP method, units, image transform and calibration compatibility.

Agent: Identify repeated/symmetric landmarks and planar/degenerate configurations with alternative poses.

Inputs: Measurement-set with 3D points and image locations; camera-solution intrinsics/distortion; image/CAD revisions.

Output/check: Pose input record with point IDs, units, image model, fit/check roles and geometric sufficiency. Validation: Point configuration meets actual method rules; correspondences derive from exact CAD/image revisions.

Dependencies: OpenCV solvePnP method-specific prerequisites; source camera model.

Resources: Local point checks first; remote VLM/manual identity review for repeated landmarks.

Source-supported tools: OpenCV solvePnP / solvePnPRansac, projectPoints. Original evidence: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html).

### 82. Bind NeRF method, supplied cameras and training-space transforms (REC-20-A01)

Original action: [Bind NeRF method, supplied cameras and training-space transforms](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-20 — Train and export a NeRF scene.

Implementation proposal: PROPOSAL NeRF input adapter: photos/cameras/config → parsed dataset, reversible world transform, camera comparison and partition manifest.

Software: Read selected parser inputs/settings and actual camera values; convert source camera basis only when required; preserve inverse world normalization and any camera-optimization changes. Preserve actual dataparser_transform and dataparser_scale, applied metadata and orientation override; scene_scale is box extent. Use the recorded inverse composition for round trip, as specified in common_protocol.parser_contract.

Agent: Reason about view coverage, dynamic regions and source feature associations; choose supported masked/excluded regions.

Inputs: Photo-set AND camera-solution, original/preprocessed images, calibration/pose mapping, masks, exact NeRF method/parser/config and evaluation roles.

Output/check: NeRF dataset receipt with camera basis/world orientation/centering/scale transforms, parser readback and source participation table. Validation: Projection agreement is checked before training; a generic processing route that re-estimates supplied poses must be explicitly requested and produce a new camera revision.

Dependencies: Existing camera-solution and calibration; exact selected method/parser entrypoint and source rights.

Resources: Low-cost CPU camera/projection audit first; image count/resolution/ray sampling/model architecture determine planned training demand; remote reasoning separate.

Source-supported tools: Nerfstudio nerfacto, Nerfstudio checkpoint and viewer export. Original evidence: [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md), [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md).

### 83. Choose the actual renderable scene subtype and consumer (REC-11-A01)

Original action: [Choose the actual renderable scene subtype and consumer](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-11 — Train NeRF or Gaussian scene for view synthesis.

Implementation proposal: PROPOSAL scene dispatcher: photos/cameras + consumer requirements + capability evidence → typed method route and explicit visual-scene payload manifest.

Software: Inspect chosen method and consumer interface; resolve whether visual-scene contains training state/renderer assets or a supported exported scene subtype.

Agent: Compare method capability, input coverage and required viewing behavior; interpret masks/features and document source-supported choice.

Inputs: Photo-set AND camera-solution, intended viewing purpose, camera/preprocess receipt, target consumer and available method/version evidence.

Output/check: Scene dispatch record naming Gaussian or NeRF subtype, renderer, config/checkpoint/assets, camera route and optional separate geometry branch. Validation: Consumer supports the actual subtype and required assets; a generic visual-scene type cannot conceal missing renderer/checkpoint dependencies.

Dependencies: REC-19/20 input contracts; source/camera dataset; actual selected renderer; no generic GLB assumption.

Resources: Metadata and source projection preview first; method training costs are estimated from exact images/settings, separately from VLM selection/manual evidence review.

Source-supported tools: Nerfstudio ns-process-data, ns-train nerfacto/splatfacto, ns-export gaussian-splat/tsdf/poisson/pointcloud. Original evidence: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html), [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md), [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md).

### 84. Bind the domain Gaussian scene contract (DOM-22-A01)

Original action: [Bind the domain Gaussian scene contract](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-22 — Photographs to Gaussian/NeRF visual scene.

Implementation proposal: PROPOSAL domain Gaussian planner: photos/cameras + domain feature/use map → REC-19 request, typed gaussian-scene consumer and coverage criteria.

Software: Typed dispatcher verifies input camera coverage and exact Gaussian renderer/export support; preserves element/component IDs as a sidecar mapping.

Agent: Interpret building/part region identities and required view coverage with full source images and camera map.

Inputs: Photo-set AND camera-solution, source/mask/camera lineage, domain feature IDs, intended visual consumer and optional measured-frame controls.

Output/check: Gaussian domain route receipt with feature-to-source mapping, camera policy and explicit link to REC-19; NeRF requests route separately to DOM-30. Validation: NeRF or mesh request is explicitly dispatched to its own operation; every required region has source/evaluation roles and consumer support.

Dependencies: REC-19 input conditions; domain source identity and optional registration controls.

Resources: Local manifest/projection checks first; record image count/resolution and required viewing extent before training; manual identity and remote VLM costs separate.

Source-supported tools: Nerfstudio/gsplat; COLMAP camera input; Blender viewer/export. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 85. Bind domain features and cameras to the NeRF route (DOM-30-A01)

Original action: [Bind domain features and cameras to the NeRF route](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-30 — Photos to NeRF visual scene.

Implementation proposal: PROPOSAL domain NeRF planner: source photos/cameras + domain/view goals → REC-20 request, parser/renderer contract and required region checks.

Software: Inspect selected supplied-camera parser and renderer; validate feature/image links and actual normalization receipt requirements.

Agent: Interpret source-region/domain identities and view gaps; choose evidenced route within current purpose.

Inputs: Photo-set AND camera-solution, source identity/rights, domain feature map, actual NeRF renderer/method and evaluation plan.

Output/check: Domain NeRF request referencing REC-20, input camera/parser mapping and required source/view coverage. Validation: Both inputs and camera coverage are present; actual renderer supports NeRF payload; parser coordinate/scale discovery is assigned before training.

Dependencies: REC-20 input contract; source camera/calibration and domain feature evidence.

Resources: Metadata/camera preview first; training demand based on exact image count/resolution/method rather than a universal GPU score; remote inference/manual separate.

Source-supported tools: Nerfstudio; COLMAP camera input. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 86. Read actual geometry and compare required features (CAD-13-A02)

Original action: [Read actual geometry and compare required features](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-13 — Verify model geometry and saved output.

Implementation proposal: Reuse sat_features and check_contract.run for their supported observations; detach pure readers from session-binding imports and dispatch by actual SAT/SAB representation with per-feature supported-check results.

Software: Measure critical dimensions/axes, shape counts/topology, validity and applicable volume; inspect mesh degeneracy/normals/closedness when relevant.

Agent: Independent reviewer checks that each numeric query addresses the intended feature; VLM compares same-revision views and source references.

Inputs: Check plan; fixed document/artifact revision; geometry query route; source references.

Output/check: Measurement-set and check findings for CAD-13-A03. Validation: Cross-check critical features using independent controls/readers where appropriate; equal bounds/volume do not replace local interface checks.

Dependencies: Native kernel/mesh query APIs; point/axis/plane helper only after actual measurement extraction.

Resources: Required-feature queries precede broad topology/mesh scans; local CPU/RAM scales with geometry size. Remote VLM and manual measurement review tracked separately.

Reuse: [check_ngv064_wheel.py](/tmp/opencode/check_ngv064_wheel.py), [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [neugart-ngv064-wheel-160-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/neugart-ngv064-wheel-160-native.json), [item-angle-bracket-set-41115-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-angle-bracket-set-41115-native.json), [item-profile-02633-segment-100mm-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm-native.json), [nissan-leaf-gen2-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/nissan-leaf-gen2-native.json), [bmw-i3-94ah-native-checks.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/bmw-i3-94ah-native-checks.json). Restricted native surface checks and retained pre-save component results; choose reader for actual representation.

Reuse: [check_contract.py](/home/leo/.codex/skills/ocs-engineering/scripts/check_contract.py). Supplied point/axis/plane numerical checks only; caller supplies independently sourced observations and criteria.

Source-supported tools: OCS read/measure/audit/save_verified, FreeCAD B-rep readback, build123d/CadQuery shape checks, independent importer, mesh validation. Original evidence: [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md), [https://build123d.readthedocs.io/en/stable/](https://build123d.readthedocs.io/en/stable/).

### 87. Reopen saved artifacts and issue the verification report (CAD-13-A03)

Original action: [Reopen saved artifacts and issue the verification report](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-13 — Verify model geometry and saved output.

Implementation proposal: Reuse existing save_verified/open/audit sequences; add separately recorded reopened feature checks and verified document/view identity.

Software: Open saved artifact read-only; compare identities/units/frames/geometry; use OCS audit/save_verified only for its supported targets and authorized save.

Agent: Separate reviewer compares source-to-output semantic mapping and native editability/history versus actual exchange content.

Inputs: Saved output and hash; check findings; native source revision; chosen reader; any authorized save scope.

Output/check: Verification-report with preserved failures, output identities and named downstream readiness. Validation: Report passes apply only to checked revisions; a fabrication package remains an inspected input and verification creates its report.

Dependencies: Native reader and supported independent consumer; OCS verified DWG/DXF save scope; STEP checked through its actual importer.

Resources: Local reopen/query costs follow file/geometry size; record reader CPU/RAM and I/O. Remote/manual review checks mappings, failures and intended use.

Reuse: [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [item-profile-02633-segment-100mm.md](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm.md), [neugart-ngv064-wheel-160.md](/home/leo/projects/ferme/engineering/module-development/cad/checks/neugart-ngv064-wheel-160.md). save_verified/open and reopened audits in existing component procedures; detailed surface and visual checks retain stage-specific evidence.

Source-supported tools: OCS read/measure/audit/save_verified, FreeCAD B-rep readback, build123d/CadQuery shape checks, independent importer, mesh validation. Original evidence: [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md), [https://build123d.readthedocs.io/en/stable/](https://build123d.readthedocs.io/en/stable/).

### 88. Attach item-level terms and permitted operations (DOM-06-A02)

Original action: [Attach item-level terms and permitted operations](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-06 — Library asset intake and rights record.

Implementation proposal: Proposal: rights evidence attachment and operation-permission checklist driven by actual terms, with manual ambiguity review.

Software: Preserve terms file/hash and link each asset to its applicable notice; compare changes in terms and attribution.

Agent: Read scope/conditions and distinguish collection, software and individual-model terms; identify the exact clause requiring a decision.

Inputs: Item inventory; actual asset LICENSE/terms text and URL/revision; attribution; requested usage operations.

Output/check: Per-file identity/terms receipt with intake-draft status, consumed directly by DOM-38-A01 when STEP inspection is required, then by DOM-06-A03. Validation: Independent source-reading reviewer checks clause/file applicability and notices; verify each proposed derivative has a recorded terms basis.

Dependencies: Existing original terms or registered source documents; source-specific rights review.

Resources: Local text comparison/hash CPU is small relative to geometry work. Manual terms interpretation dominates; remote reasoning calls use source passages and are recorded.

Source-supported tools: component registry/schema proposal; source license review. Original evidence: [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN), [https://www.kicad.org/libraries/license/](https://www.kicad.org/libraries/license/), [https://github.com/google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie), [https://polyhaven.com/license](https://polyhaven.com/license), [https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280).

### 89. Classify component representations and interface evidence (DOM-06-A03)

Original action: [Classify component representations and interface evidence](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-06 — Library asset intake and rights record.

Implementation proposal: Proposal: representation inspector linking source claims and measured feature records without promoting visual proxies to dimensional evidence.

Software: Read file signatures and actual geometry entity types using a selected reader; inventory units, hierarchy, bounds and named interfaces.

Agent: Associate source documents with feature identities; choose the representation matching the requested use and identify an evidence-supported alternative.

Inputs: DOM-06-A01/A02 identity/rights receipt; actual assets and source evidence; DOM-38 checked representation receipt when STEP transfer is required for the requested use.

Output/check: Representation and feature-evidence records, consumed by DOM-06-A04 and DOM-38/DOM-07. Preserve source IFC element or MJCF body identities and frame links when supplied; later domain operations own their semantic transformations. Validation: Check representation labels against actual reader findings; independent reviewer verifies the feature/source mapping and intended-use fit.

Dependencies: Native CAD/mesh readers; DOM-38 accepts the partial identity/rights receipt before a completed component record and returns checked representation evidence; OCS model contract for parts/interfaces.

Resources: Start with file metadata; load geometry only for required features. CPU/RAM scales with entities/triangles; GPU only for view inspection. Record VLM inputs and manual associations.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Documented exact part/revision, representation, source dependency and reproduction-package records; serialization/automation follows each action.

Source-supported tools: component registry/schema proposal; source license review. Original evidence: [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN), [https://www.kicad.org/libraries/license/](https://www.kicad.org/libraries/license/), [https://github.com/google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie), [https://polyhaven.com/license](https://polyhaven.com/license), [https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280).

### 90. Register the component record and handoff conditions (DOM-06-A04)

Original action: [Register the component record and handoff conditions](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-06 — Library asset intake and rights record.

Implementation proposal: Proposal: component registration validator with per-operation prerequisite status and immutable original references.

Software: Validate references/digests, duplicate identities, required terms and recorded frame mappings; emit the readable record.

Agent: Independent reviewer checks that intended-use claims follow the retained evidence and source terms.

Inputs: Identity/rights receipt plus required representation/feature evidence, including DOM-38 verification when the target use requires imported STEP geometry.

Output/check: Component-record with source/terms/geometry references, consumed by DOM-26, DOM-38 and DOM-07. Validation: Reopen the record and resolve every retained file/terms reference; independent semantic check compares it with the original selected item. Keep intake-draft/readiness per target action until its required representation evidence exists.

Dependencies: Existing source registry and proposed component-record organization in implementation-plan; actual storage policy remains task-specific.

Resources: Local metadata/reference checks first; storage scales with retained originals. Remote/manual review addresses source meaning and decisions, with actual effort recorded.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Documented exact part/revision, representation, source dependency and reproduction-package records; serialization/automation follows each action.

Source-supported tools: component registry/schema proposal; source license review. Original evidence: [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN), [https://www.kicad.org/libraries/license/](https://www.kicad.org/libraries/license/), [https://github.com/google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie), [https://polyhaven.com/license](https://polyhaven.com/license), [https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280).

### 91. Define interface frames and placement relations (CAD-12-A02)

Original action: [Define interface frames and placement relations](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: CAD-12 — Assemble existing CAD or source-library components.

Implementation proposal: Reuse check_contract.run for supported axis/plane predicates; add interface identity, frame composition and per-feature criteria mapping.

Software: Normalize explicit units; calculate frame composition and constraint consistency with a checked matrix/assembly backend.

Agent: Associate measured planes/axes with intended interfaces; use a VLM to compare source views and candidate correspondences.

Inputs: Pinned definitions; sourced component frames; target assembly frame; interface measurements; allowed placements and motion.

Output/check: Named interface correspondence and placement plan, consumed by CAD-12-A03 or DOM-07. Validation: Check frame direction, units, right-handed rigid rotation after explicit convention mapping, and graph parent identities; reviewer rereads semantic correspondences.

Dependencies: OCS model contract; FreeCAD Assembly documented joints; existing measurement API only where installed support is discovered.

Resources: Small matrix/graph checks use local CPU/RAM. CAD measurements depend on shape size. VLM calls use cited views; record manual relation decisions and latency.

Reuse: [check_contract.py](/home/leo/.codex/skills/ocs-engineering/scripts/check_contract.py). Supplied point/axis/plane numerical checks only; caller supplies independently sourced observations and criteria.

Source-supported tools: OCS blocks/groups, FreeCAD App::Link/Assembly, build123d/CadQuery Assembly, unit and frame mapping. Original evidence: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [https://cadquery.readthedocs.io/en/stable/](https://cadquery.readthedocs.io/en/stable/).

### 92. Create bounded native occurrences (CAD-12-A03)

Original action: [Create bounded native occurrences](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: CAD-12 — Assemble existing CAD or source-library components.

Implementation proposal: Proposal: occurrence adapter with immutable definition references, explicit IDs and revision-aware restart.

Software: Use the inspected native assembly API; OCS block_define/group_create only for their declared drawing semantics; FreeCAD/CadQuery assembly alternatives require checked adapter support.

Agent: Choose the matching native representation, orchestrate bounded creation and examine partial results.

Inputs: Checked placement plan; source definitions; chosen native representation; authorized document/revision and save scope.

Output/check: Native occurrence tree with definition references and transforms, consumed by CAD-12-A04. Validation: Verify source component hashes remain unchanged; read occurrence IDs/counts/transforms; inspect same-revision views and connection relations.

Dependencies: OCS API-SPEC revision/request protocol; FreeCAD Assembly or CadQuery assembly route per recorded tool/version.

Resources: Local CPU/RAM scales with occurrence count and geometry; graphics only for native display. Remote agent directs exceptions; record manual constraint edits.

Source-supported tools: OCS blocks/groups, FreeCAD App::Link/Assembly, build123d/CadQuery Assembly, unit and frame mapping. Original evidence: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [https://cadquery.readthedocs.io/en/stable/](https://cadquery.readthedocs.io/en/stable/).

### 93. Validate and preserve assembly structure (CAD-12-A04)

Original action: [Validate and preserve assembly structure](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: CAD-12 — Assemble existing CAD or source-library components.

Implementation proposal: Reuse the recorded assembly count/save checks; add explicit definition/occurrence/transform and interface preservation comparisons.

Software: Check definition/occurrence counts, transforms and native save/reopen; use bounding boxes only to select candidate interference pairs, then a supported exact query for actual clearance.

Agent: Independent reviewer examines component meaning, datum association and permitted contact against source views; diagnose failed numerical checks.

Inputs: Created assembly; placement plan; source definitions; per-feature criteria; supported geometry measurement API.

Output/check: Revision-bound assembly validation and native artifact, consumed by DOM-26/DOM-39 or a named downstream operation. Validation: Numerical checks and independent semantic review both reference the saved revision; report actual solid/shell/mesh status and shared-kernel dependencies of the second reader.

Dependencies: Native CAD measurement/save facilities; OCS save audit applies only to supported targets; independent reader where available.

Resources: Local shape checks may dominate CPU/RAM for large assemblies; begin with hashes/counts/transforms. Remote review uses bounded views; record review time and corrections.

Reuse: [cad-workflow-findings.md](/home/leo/projects/ferme/skills/cad-workflow-findings.md), [ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md). Reported native IMPORT and assembly/save preservation for Victron and RoboteQ; retained counts apply to those examples.

Source-supported tools: OCS blocks/groups, FreeCAD App::Link/Assembly, build123d/CadQuery Assembly, unit and frame mapping. Original evidence: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [https://cadquery.readthedocs.io/en/stable/](https://cadquery.readthedocs.io/en/stable/).

### 94. Resolve the complete dependency and rights set (DOM-26-A02)

Original action: [Resolve the complete dependency and rights set](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-26 — Version and reuse component revision.

Implementation proposal: Proposal: dependency-closure and invalidation helper with explicit asset/tool/configuration edges.

Software: Traverse dependency references, detect missing pins/cycles according to allowed graph semantics, recompute hashes and compare rights applicability.

Agent: Interpret derivative lineage and identify which downstream checks require repetition after a change.

Inputs: Candidate revision; referenced source assets, child components, terms, adapter versions, parameters and derivative manifests.

Output/check: Closed dependency manifest and impacted-consumer list, consumed by DOM-26-A03. Validation: Every referenced artifact resolves to the recorded bytes; independent reviewer checks semantic dependency completeness and terms scope.

Dependencies: Existing source/terms registry, file hashing and reference graph; storage choice follows measured size and rights.

Resources: Local graph/hash work scales with dependency count/bytes; no geometry regeneration. Remote review handles lineage/terms ambiguities; record manual effort.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Documented exact part/revision, representation, source dependency and reproduction-package records; serialization/automation follows each action.

Source-supported tools: content-addressed files; Git metadata; source/license registry. Original evidence: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 95. Publish a new immutable revision and explicit reuse pins (DOM-26-A03)

Original action: [Publish a new immutable revision and explicit reuse pins](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-26 — Version and reuse component revision.

Implementation proposal: Proposal: revision publisher with collision detection, atomic metadata replacement and recoverable consumer pin updates.

Software: Write new immutable artifact/metadata locations using checked storage facilities; update only named consumer references; retain old pins elsewhere.

Agent: Review the exact change set and choose bounded update order with recovery points.

Inputs: Closed candidate manifest; storage policy; existing revision namespace; explicitly requested consumer updates.

Output/check: New component revision and separately updated consumer pins, consumed by DOM-26-A04. Validation: Old pins still resolve unchanged; new pins resolve the new digest; compare the intended and actual consumer change set.

Dependencies: Existing repository/content-addressed storage policy; Git/LFS are candidate storage choices requiring their actual authorization and setup.

Resources: Local storage and hash I/O dominate; record bytes written and checks. Remote/manual work reviews consumer selection and exceptions.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Documented exact part/revision, representation, source dependency and reproduction-package records; serialization/automation follows each action.

Source-supported tools: content-addressed files; Git metadata; source/license registry. Original evidence: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 96. Reopen pinned artifacts and check reuse reproducibility (DOM-26-A04)

Original action: [Reopen pinned artifacts and check reuse reproducibility](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-26 — Version and reuse component revision.

Implementation proposal: Proposal: revision-resolution report and affected-check scheduler scoped to changed dependencies.

Software: Resolve every pin; validate source/derivative hashes; compare a future controlled regeneration only when that execution is authorized.

Agent: Independent reviewer checks that a passing old report is not assigned to changed geometry and that required downstream checks are named.

Inputs: Published revision, dependency manifest, consumers and existing validation reports.

Output/check: Revision resolution report and downstream test obligations, consumed by DOM-07/DOM-39. Validation: All pins resolve correctly; source/terms closure holds; changed geometry has explicit pending validation for its named use.

Dependencies: Existing readers and manifest records; supported exporter/adapter needed for any future reproducibility execution.

Resources: Local hash/read cost scales with selected dependency closure. Remote/manual review examines semantic invalidation and migration scope.

Reuse: [SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md). Documented exact part/revision, representation, source dependency and reproduction-package records; serialization/automation follows each action.

Source-supported tools: content-addressed files; Git metadata; source/license registry. Original evidence: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 97. Construct features with revision-bound readback (CAD-10-A02)

Original action: [Construct features with revision-bound readback](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-10 — Create a kernel solid and native model document from confirmed parameters.

Implementation proposal: Adapt execute_checked and the existing write/step geometry wrappers to explicit session/document configuration and bounded completion polling; preserve the existing one-send guard and separate entity effects from interactive command state.

Software: Execute bounded primitive/extrude/revolve/Boolean operations and query each actual result. For OCS Python methods explicitly record and pass delete_source=False for region/surface/extrude when preserving the profile, and keep_operands=True for union/subtract/intersect when preserving operands. An explicitly selected deletion policy uses its recorded flags; the inspected Boolean default keep_operands=False consumes operands.

Agent: Diagnose profile, coincidence, Boolean refusal and changed history from actual returned errors.

Inputs: Feature plan; source profiles/operands; target document/revision; supported command/plugin interface.

Output/check: Body candidate, feature lineage and operation receipts for CAD-10-A03. Validation: Check finite bounds, resulting component count and required feature after each stage; detect open-profile surface result, invalid Boolean and unwanted fusion. Compare actual retained/deleted handles with the flag receipt; default Boolean behavior cannot stand in for an operand-preserving policy.

Dependencies: Installed OCS command/plugin path; FreeCAD Part/PartDesign or CadQuery/build123d selected API; native syntax discovered before use. OCS plugin single-profile extrusion, Region rejection and Boolean operand/profile deletion flags are checked explicitly; REVOLVE is a command path, not an inspected plugin enum variant.

Resources: Local Boolean/kernel work can dominate simple profile checks; record actual face/feature counts and build mode. Remote agent diagnoses exceptions; GPU is display-only unless actual backend uses it.

Reuse: [ocs_control.py](/home/leo/.codex/skills/ocs-engineering/scripts/ocs_control.py), [ngv064_ocs.py](/tmp/opencode/ngv064_ocs.py), [item_ocs_parts.py](/tmp/opencode/item_ocs_parts.py), [battery_ocs_parts.py](/tmp/opencode/battery_ocs_parts.py), [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [build_leaf_gen2.py](/tmp/opencode/build_leaf_gen2.py), [build_bmw_i3_94ah.py](/tmp/opencode/build_bmw_i3_94ah.py). Guarded writes and native geometry creation; component recipes require explicit input/session adapters.

Source-supported tools: OpenCADStudio kernel tools, FreeCAD PartDesign/Part, build123d, CadQuery. Original evidence: [https://build123d.readthedocs.io/en/latest/operations.html](https://build123d.readthedocs.io/en/latest/operations.html), [https://cadquery.readthedocs.io/en/stable/](https://cadquery.readthedocs.io/en/stable/), [https://openscad.org/documentation](https://openscad.org/documentation), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md), [/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md).

### 98. Verify native solid and saved construction record (CAD-10-A03)

Original action: [Verify native solid and saved construction record](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-10 — Create a kernel solid and native model document from confirmed parameters.

Implementation proposal: Reuse recorded feature checks; add explicit native representation selection and stage-bound saved-artifact evidence to their result adapter.

Software: Check validity, solids/shells/face types, critical dimensions and valid volume; save/reopen native result; retain parametric source or feature tree according to the chosen backend.

Agent: Independent reviewer checks cut direction, axes, component separation and source correspondence using same-revision views.

Inputs: Constructed bodies; feature plan; source controls; native representation contract; supplied variant if requested.

Output/check: Native model, actual solid classification and verification receipt consumed by CAD-13/DOM-04/DOM-05. Validation: Validate topology and critical interfaces beyond bounds/volume; report actual native history/source retention and independent-reader dependencies.

Dependencies: Native CAD readback/save; CAD-13 validation contract; exact source exporter route checked separately.

Resources: Local shape/reopen costs depend on faces and feature history; start with counts and required features. Remote/VLM semantic review uses bounded views; manual corrections logged.

Reuse: [check_ngv064_wheel.py](/tmp/opencode/check_ngv064_wheel.py), [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [neugart-ngv064-wheel-160-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/neugart-ngv064-wheel-160-native.json), [item-angle-bracket-set-41115-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-angle-bracket-set-41115-native.json), [item-profile-02633-segment-100mm-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm-native.json), [nissan-leaf-gen2-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/nissan-leaf-gen2-native.json), [bmw-i3-94ah-native-checks.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/bmw-i3-94ah-native-checks.json). Restricted native surface checks and retained pre-save component results; choose reader for actual representation.

Source-supported tools: OpenCADStudio kernel tools, FreeCAD PartDesign/Part, build123d, CadQuery. Original evidence: [https://build123d.readthedocs.io/en/latest/operations.html](https://build123d.readthedocs.io/en/latest/operations.html), [https://cadquery.readthedocs.io/en/stable/](https://cadquery.readthedocs.io/en/stable/), [https://openscad.org/documentation](https://openscad.org/documentation), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md), [/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md).

### 99. Create a mapped and explicitly cleaned derivative (CAD-08-A02)

Original action: [Create a mapped and explicitly cleaned derivative](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-08 — Read and clean vector drawing geometry.

Implementation proposal: Reuse contours sampling/normalization only for the retained text-contour branch; parameterize its source transform and approximation criteria. Implement DXF/SVG adapters as their separately identified format branches.

Software: Compose nested block transforms; apply object/world coordinates; preserve analytic curves where supported; detect duplicates/gaps/intersections before bounded joins or conversions.

Agent: Compare repair candidates using source curves and dimensions; VLM selects supported loop/feature interpretation.

Inputs: Source inventory; selected entities; explicit unit/frame mapping; approved repair/approximation criteria.

Output/check: Clean vector derivative and per-entity preservation/change map for CAD-08-A03. Validation: Nonuniform transforms preserve their actual curve result, such as circle-to-ellipse; compare repaired endpoints and source controls within their individual criteria.

Dependencies: Native OCS/Draft edits or ezdxf derivative writer; actual supported entity behavior must be checked.

Resources: Local transform/detection work scales with curve count and intersection candidates; expensive comparisons follow bounding filters. Remote review/manual edits address only ambiguous repairs.

Reuse: [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [item-profile-02633-segment-100mm.md](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm.md). Existing extracted-contour sampling, duplicate removal and XY normalization branch; DXF/SVG generic parsing remains a separate adapter.

Source-supported tools: OpenCADStudio DWG/DXF/MCP, FreeCAD Draft DXF/SVG import, ezdxf, geometry audit. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md), [https://ezdxf.readthedocs.io/en/stable/](https://ezdxf.readthedocs.io/en/stable/), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md).

### 100. Validate curve fidelity and publish the vector handoff (CAD-08-A03)

Original action: [Validate curve fidelity and publish the vector handoff](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-08 — Read and clean vector drawing geometry.

Implementation proposal: Reuse the profile contour-count/area and dimension checks as a case fixture; add source-to-curve maps and actual curve-fidelity/closure checks for the chosen vector format.

Software: Count by type/layer; check open endpoints, self-intersections, loop nesting, bounds and area; reopen the derivative.

Agent: Independent reviewer checks outer/hole loops and excluded annotation against original source views.

Inputs: Original and derivative; change ledger; source controls; loop/hole intent; target plane.

Output/check: Checked vector-drawing revision and curve comparison receipt for CAD-09/DOM-03. Validation: Require numerical source correspondence and independent loop/feature review; unsupported entity losses remain explicit failures for required geometry.

Dependencies: Selected geometry reader/curve checker; independent reader when its coverage supports the entity set.

Resources: Local topology checks scale with curves/intersections; views add display cost. Record remote review calls, source image size and manual correspondence corrections.

Reuse: [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [item-profile-02633-segment-100mm-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm-native.json). Source contour counts/area and checked dimensions on the profile example; per-curve fidelity check still follows the audited action.

Source-supported tools: OpenCADStudio DWG/DXF/MCP, FreeCAD Draft DXF/SVG import, ezdxf, geometry audit. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md), [https://ezdxf.readthedocs.io/en/stable/](https://ezdxf.readthedocs.io/en/stable/), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md).

### 101. Create the sketch and solve bounded constraint groups (CAD-09-A02)

Original action: [Create the sketch and solve bounded constraint groups](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-09 — Build and constrain an editable planar sketch.

Implementation proposal: Proposal: incremental constraint adapter and conflict reporter preserving source-to-constraint relationships.

Software: Create geometry; add constraints in diagnosable groups; solve/recompute and collect remaining degrees of freedom, redundancy and conflict reports. Record each diagnostic's actual API, value and supported status; an unavailable required diagnostic yields an unresolved check and blocks its dependent readiness claim.

Agent: Interpret whether remaining freedom is intended and diagnose the smallest conflicting constraint group.

Inputs: Checked sketch plan; target document/revision; chosen Sketcher or supported equivalent; solver configuration.

Output/check: Constrained-sketch candidate and solve history for CAD-09-A03. Validation: Inspect solver state/residuals and movement from source geometry; a solved sketch must also satisfy source-to-constraint correspondence.

Dependencies: FreeCAD Sketcher APIs/version; OCS equivalent only after installed capability inspection. The archived FreeCAD Sketcher example establishes addGeometry/addConstraint/recompute; the selected version's actual diagnostic API must be discovered for solver state, remaining degrees of freedom, conflicts and residuals.

Resources: Local solver CPU/RAM scales with constraints and connectivity. Remote reasoning diagnoses semantics; manual work concerns exact conflict decisions.

Source-supported tools: FreeCAD Sketcher scripting, FreeCAD Draft-to-Sketch, OpenCADStudio sketch/constraint capability as discovered in session. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 102. Measure and reopen the constrained sketch (CAD-09-A03)

Original action: [Measure and reopen the constrained sketch](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-09 — Build and constrain an editable planar sketch.

Implementation proposal: Proposal: sketch evidence validator linking solver, geometry and native parameter behavior.

Software: Measure critical dimensions, closure/nesting/intersections; save/reopen and, when authorized, recompute one declared parameter variant.

Agent: Independent reviewer compares source feature associations and intended free variables with the saved sketch.

Inputs: Solved sketch; source curves/constraints; feature criteria; intended degrees of freedom; native save path.

Output/check: Native sketch revision and validation receipt for CAD-10/DOM-04. Validation: Solver consistency, source correctness and saved editability are separate findings; detect a fully constrained wrong loop.

Dependencies: Native Sketcher measurements/recompute and save/reopen; separate reader for supported geometry checks.

Resources: Local readback precedes variant recompute; effort scales with sketch dependencies. Remote/manual source review and local graphics are recorded separately.

Source-supported tools: FreeCAD Sketcher scripting, FreeCAD Draft-to-Sketch, OpenCADStudio sketch/constraint capability as discovered in session. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 103. Compute the occurrence transform (DOM-07-A02)

Original action: [Compute the occurrence transform](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-07 — Place reusable component in assembly.

Implementation proposal: Reuse the existing numerical observation checker; add explicit source-to-target frame composition and instance transform output.

Software: Use column-vector convention: T_A_C = T_A_I × T_I_J × inverse(T_C_J), with A assembly, C component, I target interface and J component interface; apply declared unit/convention mapping separately.

Agent: Check transform direction, mating offset meaning and source conventions; compare candidate mappings with intended geometry.

Inputs: Checked source and target interface frames; declared mating offset; source-unit conversion; per-interface criteria.

Output/check: Component-to-assembly transform with derivation and residual checks, consumed by DOM-07-A03. Validation: Verify inverse/round-trip consistency, orthonormal rigid rotation and determinant +1 after explicit convention conversion; test independent control points and named axes within their sourced criteria.

Dependencies: Checked matrix arithmetic and native placement API; representation conventions from composition rules.

Resources: Small local matrix computations need CPU/RAM; no GPU requirement. Remote reasoning only for semantic exceptions; record human frame corrections.

Reuse: [check_contract.py](/home/leo/.codex/skills/ocs-engineering/scripts/check_contract.py). Supplied point/axis/plane numerical checks only; caller supplies independently sourced observations and criteria.

Source-supported tools: OCS; FreeCAD Assembly Workbench; native CAD assembly API. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 104. Insert the component occurrence and connection edge (DOM-07-A03)

Original action: [Insert the component occurrence and connection edge](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-07 — Place reusable component in assembly.

Implementation proposal: Proposal: placement adapter with stable occurrence IDs and recoverable native-document/graph update ordering. Preserve target assembly revision, required graph and graph revision explicitly.

Software: Use supported native placement/assembly API; read current schema/state; write occurrence and relationship within a bounded operation sequence.

Agent: Choose the supported placement representation and reconcile partial native/graph results.

Inputs: Pinned component definition; checked transform; target document/revision; assembly-graph; native API capabilities.

Output/check: Occurrence plus graph edge and actual transform readback, consumed by DOM-07-A04. Validation: Check exactly one intended occurrence was added, graph endpoints resolve and source hash is unchanged; compare actual and intended transforms.

Dependencies: OCS block/group semantics only where appropriate; FreeCAD Assembly/other native APIs require inspected capabilities.

Resources: Local insertion cost scales with source shape/display complexity; rendering GPU use recorded if observed. Agent/manual work diagnoses interface or state exceptions.

Source-supported tools: OCS; FreeCAD Assembly Workbench; native CAD assembly API. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 105. Measure placed interfaces and preserve the result (DOM-07-A04)

Original action: [Measure placed interfaces and preserve the result](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-07 — Place reusable component in assembly.

Implementation proposal: Reuse supported supplied-measurement predicates; add placed-interface observation acquisition and saved occurrence/revision binding.

Software: Measure named interfaces; validate graph transform composition; perform supported exact interference query where required; save/reopen within scope.

Agent: Independent reviewer checks that the measured feature is the intended interface and that allowed contact matches the supplied relationship.

Inputs: Placed occurrence, graph edge, source measurements, saved revision and feature-specific validation criteria.

Output/check: Placement verification and pinned assembly update, consumed by CAD-12/DOM-26/DOM-39. Validation: Require both revision-bound numerical checks and separate semantic review; bounding-box intersection remains a candidate pair classification.

Dependencies: Native measurement and save/reopen interface; OCS contract checker only for its supplied point/axis/plane subset.

Resources: Local bounded measurements precede expensive pair checks; record CPU/RAM and candidate-pair count. Remote review and manual corrections receive separate effort records.

Reuse: [check_contract.py](/home/leo/.codex/skills/ocs-engineering/scripts/check_contract.py). Supplied point/axis/plane numerical checks only; caller supplies independently sourced observations and criteria.

Source-supported tools: OCS; FreeCAD Assembly Workbench; native CAD assembly API. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 106. Choose and configure an isolated importer (DOM-38-A02)

Original action: [Choose and configure an isolated importer](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-38 — Import STEP solid into CAD representation.

Implementation proposal: Reuse the recorded native IMPORT workflow; add installed-schema and exact target/session/import-setting configuration around that route.

Software: Inspect native importer and documented OCCT STEPCAFControl_Reader: assembly-shape, name/color modes and root transfer into a DECAF document. A pinned local adapter must establish its actual calls and output; record FreeCAD import-structure preferences and importer settings.

Agent: Select the supported route for the intended use, explaining expected names/hierarchy/colour/topology treatment.

Inputs: STEP preflight manifest; target native representation; importer capabilities/settings; authorized destination.

Output/check: Import plan and isolated target context, consumed by DOM-38-A03. Validation: Check the plan accounts for every required identity/shape/frame field; preserve existing document state and explicit source-to-target unit rule.

Dependencies: OCCT 8.0.1 STEPCAFControl_Reader documentation inspected by Luna; archived FreeCAD preference documentation; an installed runtime/adapter still requires discovery and tests. OCS README documents OBJ import and mesh-derived STEP export.

Resources: Local capability/settings inspection precedes full import. Import CPU/RAM estimates follow file/entity size; remote/manual effort concerns route choice.

Reuse: [cad-workflow-findings.md](/home/leo/projects/ferme/skills/cad-workflow-findings.md), [ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md). Reported native IMPORT and assembly/save preservation for Victron and RoboteQ; retained counts apply to those examples.

Source-supported tools: FreeCAD/Open CASCADE STEP adapter. Original evidence: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md).

### 107. Transfer geometry and classify actual output (DOM-38-A03)

Original action: [Transfer geometry and classify actual output](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-38 — Import STEP solid into CAD representation.

Implementation proposal: Reuse the evidenced IMPORT route; record actual imported geometry classes, nested instances and source-to-result mapping.

Software: Run the selected import; inventory solids, shells, face types, occurrences, names and placements; retain transfer warnings and healing reports.

Agent: Compare expected and actual representation; identify semantic losses and whether a faceted source remains suitable for the requested use.

Inputs: Isolated import context; original STEP; configured importer; expected invariants.

Output/check: Imported native geometry and transfer mapping/diagnostics, consumed by DOM-38-A04. Validation: Detect empty result, invalid/open topology and dropped products; validate finite bounds and actual scale; compare expected occurrence identities.

Dependencies: Selected native/OCCT STEP reader; shape inspection APIs; source-faceted STEP remains source-faceted geometry after ordinary import.

Resources: Local import/healing CPU and RAM scale with entity/face count; begin without optional costly healing. Display GPU only if used. Agent reviews transfer exceptions.

Reuse: [cad-workflow-findings.md](/home/leo/projects/ferme/skills/cad-workflow-findings.md), [ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md). Reported native IMPORT and assembly/save preservation for Victron and RoboteQ; retained counts apply to those examples.

Source-supported tools: FreeCAD/Open CASCADE STEP adapter. Original evidence: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md).

### 108. Measure and independently reopen imported geometry (DOM-38-A04)

Original action: [Measure and independently reopen imported geometry](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-38 — Import STEP solid into CAD representation.

Implementation proposal: Reuse recorded imported-assembly audit/save checks; add required interface measurements and stage-specific reopen comparisons.

Software: Measure required features; check solid/shell/face counts; reopen saved derivative and read original with a second supported consumer.

Agent: Separate semantic reviewer checks feature/product association and analytic/faceted claims against source evidence and same-revision views.

Inputs: Imported revision; original STEP; known source/control dimensions; feature tolerances; independent reader route.

Output/check: Import verification and native artifact identity, returned to DOM-06-A03/A04 for component-record completion and then consumed by CAD-12/DOM-07/DOM-26. Validation: Report identity/scale/feature residuals, topology and face types; valid-solid volume comparisons use comparable closed shapes; same-kernel agreement records that dependency. Match product definitions and occurrences by stable mapping/parent path, including local and world placements; equal bounds/volume still require critical-interface checks.

Dependencies: Native shape validity/measurement APIs and second reader; OCS check_contract supplies only its point/axis/plane numerical subset.

Resources: Metadata/count checks precede detailed face/feature measurements; CPU/RAM scales with shape complexity. Remote VLM views support identity review; manual discrepancy work is logged.

Reuse: [cad-workflow-findings.md](/home/leo/projects/ferme/skills/cad-workflow-findings.md), [ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md). Reported native IMPORT and assembly/save preservation for Victron and RoboteQ; retained counts apply to those examples.

Source-supported tools: FreeCAD/Open CASCADE STEP adapter. Original evidence: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md).

### 109. Evaluate final CSG and export the mesh derivative (CAD-15-A02)

Original action: [Evaluate final CSG and export the mesh derivative](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-15 — Render source-defined CSG as a mesh.

Implementation proposal: Proposal: resumable render wrapper with source/settings digest and explicit mesh result type.

Software: Use final geometry evaluation and mesh export; preserve source and record empty/invalid/nonmanifold warnings.

Agent: Interpret Boolean/contact warnings and whether required openings and separate components survive.

Inputs: Pinned source/render configuration; isolated output path; actual OpenSCAD version/backend.

Output/check: Mesh bytes, source-to-output lineage and render log for CAD-15-A03. Validation: Detect empty output or failed render; verify source unchanged and saved mesh can be parsed; preview appearance is a separate observation.

Dependencies: Supported OpenSCAD final-render backend and chosen mesh exporter; no B-rep preservation is inferred.

Resources: Local render/Boolean CPU/RAM scales with CSG/triangle complexity; resolution may dominate. GPU use depends on actual backend; remote/manual effort addresses failures.

Source-supported tools: OpenSCAD, STL/3MF mesh export. Original evidence: [https://openscad.org/documentation](https://openscad.org/documentation).

### 110. Measure the mesh and check declared parametric behavior (CAD-15-A03)

Original action: [Measure the mesh and check declared parametric behavior](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-15 — Render source-defined CSG as a mesh.

Implementation proposal: Proposal: source-to-mesh feature validator and variant comparison report.

Software: Check connected components, manifold/closedness where required, normals, degeneracy, finite bounds and critical feature dimensions; verify unit treatment.

Agent: Independent reviewer compares source-defined holes, cuts, part boundaries and orientation with measured mesh features.

Inputs: Mesh/hash; source/parameters; mesh criteria; reader; supplied variant value when editability testing is requested.

Output/check: Mesh verification plus source/render receipt for CAD-13 or the named mesh consumer. Validation: Check geometry and semantic source correspondence independently; mesh output remains mesh through this operation.

Dependencies: Mesh parser/validator and OpenSCAD regeneration route; STL unit convention is recorded externally when format lacks a unit declaration.

Resources: Local mesh checks scale with vertices/faces; begin with parsing/counts then critical features. Remote VLM/manual review uses bounded same-output views.

Source-supported tools: OpenSCAD, STL/3MF mesh export. Original evidence: [https://openscad.org/documentation](https://openscad.org/documentation).

### 111. Normalize curves and construct the constrained profile (DOM-03-A02)

Original action: [Normalize curves and construct the constrained profile](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-03 — DXF/SVG drawing to constrained profile.

Implementation proposal: Proposal: composed profile adapter joining existing curve and sketch receipts by stable feature IDs.

Software: Reuse CAD-08 derivative; execute CAD-09 with sourced constraints; retain importer/entity changes and solver state.

Agent: Review loop/hole assignment, unsupported curves and constraint exceptions using original source evidence.

Inputs: Profile contract; original drawing; completed CAD-08 receipt if available; CAD-09 constraint plan/backend.

Output/check: Constrained-sketch candidate with source-to-curve-to-constraint mapping for DOM-03-A03. Validation: Check no required entity/loop is lost, source units are correct and actual constraint objects exist; independent semantic reviewer checks associations.

Dependencies: Selected DXF/SVG reader plus actual constraint-bearing backend; direct extrusion tools produce a separately labeled alternative.

Resources: Local parsing/curve/solver workload depends on entities/constraints; remote/manual review concentrates on exceptions.

Source-supported tools: OpenCADStudio; FreeCAD Sketcher; CadQuery DXF import; OpenSCAD DXF linear_extrude. Original evidence: [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 112. Verify profile semantics and constrained editability (DOM-03-A03)

Original action: [Verify profile semantics and constrained editability](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-03 — DXF/SVG drawing to constrained profile.

Implementation proposal: Proposal: profile handoff validator that distinguishes constrained-sketch from clean-wire or mesh outputs.

Software: Check closure, self-intersections, hole nesting, dimensions and actual constraints; save/reopen supported native sketch.

Agent: Independent reviewer compares source-selected loops and dimensional associations rather than relying on solver success.

Inputs: Native sketch; source/curve/constraint maps; feature criteria; intended free variables.

Output/check: Profile verification and native sketch identity for CAD-10/DOM-04. Validation: Constrained output requires its actual constraint graph; a clean profile can pass curve checks while retaining its separate representation label.

Dependencies: Native sketch reader and geometric validators; CAD-09 check receipt reused at its exact revision.

Resources: Local sketch/readback work precedes solid construction; remote VLM review and manual corrections are separate records.

Source-supported tools: OpenCADStudio; FreeCAD Sketcher; CadQuery DXF import; OpenSCAD DXF linear_extrude. Original evidence: [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 113. Construct or reuse the checked native body (DOM-04-A02)

Original action: [Construct or reuse the checked native body](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-04 — Brief/profile to native CAD solid.

Implementation proposal: Reuse the checked native body or existing component construction functions; add an explicit brief-to-existing-function parameter map and exact artifact/revision handoff.

Software: Reuse an exact checked construction receipt or execute CAD-10; attach generated geometry to the supported native artifact where required.

Agent: Review whether actual result supports the requested native editing and feature semantics.

Inputs: Delivery contract; checked inputs; CAD-10 result or DOM-40 generated geometry when already available; target document/revision.

Output/check: Native body/document candidate with source lineage for DOM-04-A03. Validation: Check required solids and separate parts exist and actual native source content matches the contract.

Dependencies: Chosen native CAD API and CAD-10/DOM-40 contracts; no duplicate creation when a receipt already matches inputs.

Resources: Local kernel/attachment work scales with features and shape size. Remote/manual effort examines editing/history exceptions.

Reuse: [ocs_control.py](/home/leo/.codex/skills/ocs-engineering/scripts/ocs_control.py), [ngv064_ocs.py](/tmp/opencode/ngv064_ocs.py), [item_ocs_parts.py](/tmp/opencode/item_ocs_parts.py), [battery_ocs_parts.py](/tmp/opencode/battery_ocs_parts.py), [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [build_leaf_gen2.py](/tmp/opencode/build_leaf_gen2.py), [build_bmw_i3_94ah.py](/tmp/opencode/build_bmw_i3_94ah.py). Guarded writes and native geometry creation; component recipes require explicit input/session adapters.

Source-supported tools: OpenCADStudio baseline; FreeCAD; CadQuery; build123d; OpenSCAD. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs).

### 114. Save and validate the native model contract (DOM-04-A03)

Original action: [Save and validate the native model contract](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-04 — Brief/profile to native CAD solid.

Implementation proposal: Reuse component save/open code; add a manifest linking the saved revision, representation and actual per-stage checks to the native model contract.

Software: Save/reopen native artifact; run CAD-13 shape/feature checks; inspect actual constraints/history/source references.

Agent: Independent reviewer compares editing capability and feature meaning with the supplied task.

Inputs: Native candidate; source/feature map; save target; feature criteria; CAD-13 check plan.

Output/check: Native-model-document, cad-solid and validation receipt for DOM-05 or later operations. Validation: Both native artifact and actual solid are present; script-only source and mesh derivatives retain their own labels.

Dependencies: Supported native save/readback and CAD-13; OCS save audit limited to its demonstrated target.

Resources: Local save/reopen and required-feature queries first; record CPU/RAM/I/O. Remote review and manual editing decisions separately.

Reuse: [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [item-profile-02633-segment-100mm.md](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm.md), [neugart-ngv064-wheel-160.md](/home/leo/projects/ferme/engineering/module-development/cad/checks/neugart-ngv064-wheel-160.md). save_verified/open and reopened audits in existing component procedures; detailed surface and visual checks retain stage-specific evidence.

Source-supported tools: OpenCADStudio baseline; FreeCAD; CadQuery; build123d; OpenSCAD. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs).

### 115. Write a separate STEP derivative with actual settings (DOM-05-A02)

Original action: [Write a separate STEP derivative with actual settings](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-05 — Export STEP solid.

Implementation proposal: Proposal: solid export wrapper retaining actual representation and source/output lineage.

Software: Export to a new path; inspect file/schema/unit references and actual face representation; retain changed/dropped-field findings.

Agent: Assess warnings, shape flattening and whether required curved/interface geometry survives.

Inputs: Export contract; pinned body/native source; selected tool/version/settings; authorized output path.

Output/check: STEP artifact/hash, export diagnostics and mapping for DOM-05-A03. Validation: Check nonempty parseable output and unchanged native source; STEP entity names alone do not establish valid closed analytic geometry.

Dependencies: Selected STEP writer; OCS source body collects triangles into one faceted shell with unreferenced millimetre entity and six-decimal coordinates.

Resources: Local export CPU/RAM/I/O scales with faces/triangles; remote reasoning only examines warnings or loss decisions.

Source-supported tools: OCS STEP exporter; FreeCAD/Open CASCADE STEP import/export. Original evidence: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs).

### 116. Reopen STEP and compare critical geometry (DOM-05-A03)

Original action: [Reopen STEP and compare critical geometry](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-05 — Export STEP solid.

Implementation proposal: Proposal: solid exchange comparator with named-feature, unit and representation checks.

Software: Reimport in isolated consumer; inspect solids/shells/face types, units/frame and critical interfaces; compare with source.

Agent: Independent reviewer checks feature correspondence and same-output views, recording any shared kernel between readers.

Inputs: STEP hash; source solid/native revision; consumer/version; per-feature criteria and actual source measurements.

Output/check: STEP verification receipt and artifact for named consumer/CAD-13. Validation: Source curved faces versus faceted output are explicit; wrong holes/axes fail even when aggregate bounds/volume agree.

Dependencies: Actual consumer STEP reader; native shape/feature queries; CAD-13 reporting.

Resources: Local reader/shape work scales with topology; required features precede broad checks. Remote/manual semantic review remains separate.

Source-supported tools: OCS STEP exporter; FreeCAD/Open CASCADE STEP import/export. Original evidence: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md), [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs).

### 117. Author readable parametric source with stable feature references (DOM-40-A02)

Original action: [Author readable parametric source with stable feature references](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-40 — Script-parametric CAD authoring.

Implementation proposal: Extract explicit source-backed parameters and feature references from the existing component programs while retaining their working geometry functions and provenance metadata.

Software: Author bounded source modules/operations; perform syntax/static checks; prefer named datums/semantic selections over unqualified generated face indices.

Agent: Review feature ordering, selector stability, component identity and unintended defaults.

Inputs: Program contract; reviewed reusable code/licences; chosen library APIs; explicit output paths and parameters.

Output/check: Parametric-source candidate and dependency manifest for DOM-40-A03. Validation: Independent source review verifies operation meaning, units and part boundaries; syntax success is separate from generated geometry validity.

Dependencies: Actual supported CadQuery/build123d/FreeCAD/OpenSCAD APIs; existing implementation patterns before replacement.

Resources: Local syntax/static analysis scales with source/dependencies; remote reasoning authors/reviews semantic construction; manual choices remain recorded.

Reuse: [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [item_ocs_parts.py](/tmp/opencode/item_ocs_parts.py), [build_leaf_gen2.py](/tmp/opencode/build_leaf_gen2.py), [build_bmw_i3_94ah.py](/tmp/opencode/build_bmw_i3_94ah.py). Existing readable component parameter/construction code; constants, import side effects and file locations require scoped extraction.

Source-supported tools: CadQuery; build123d; OpenSCAD; FreeCAD Python. Original evidence: [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 118. Generate geometry in the declared environment (DOM-40-A03)

Original action: [Generate geometry in the declared environment](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-40 — Script-parametric CAD authoring.

Implementation proposal: Add configured source/parameter/output paths and complete helper dependency resolution around the existing component build entry point.

Software: Run source in the selected supported environment; capture errors and actual geometry/part counts; preserve previous outputs.

Agent: Diagnose topology, Boolean, selector and output-type errors against source/brief.

Inputs: Checked source/hash; dependency/runtime versions; parameters; output contract; bounded execution scope.

Output/check: Generated geometry, run receipt and parametric-source identity for DOM-40-A04. Validation: Successful process exit must accompany expected geometry; B-rep contract requires actual supported solid output; OpenSCAD mesh remains typed mesh.

Dependencies: Pinned library/runtime/kernel; CAD-10 supported construction or CAD-15 OpenSCAD mesh route; installation remains separate scope.

Resources: Local kernel/render CPU/RAM scales with feature/Boolean/mesh complexity; remote model time is separate. Record manual exception handling and actual build mode.

Reuse: [ocs_control.py](/home/leo/.codex/skills/ocs-engineering/scripts/ocs_control.py), [ngv064_ocs.py](/tmp/opencode/ngv064_ocs.py), [item_ocs_parts.py](/tmp/opencode/item_ocs_parts.py), [battery_ocs_parts.py](/tmp/opencode/battery_ocs_parts.py), [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [build_leaf_gen2.py](/tmp/opencode/build_leaf_gen2.py), [build_bmw_i3_94ah.py](/tmp/opencode/build_bmw_i3_94ah.py). Guarded writes and native geometry creation; component recipes require explicit input/session adapters.

Source-supported tools: CadQuery; build123d; OpenSCAD; FreeCAD Python. Original evidence: [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 119. Validate generated geometry and a supplied parameter variant (DOM-40-A04)

Original action: [Validate generated geometry and a supplied parameter variant](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: DOM-40 — Script-parametric CAD authoring.

Implementation proposal: Reuse component verification functions and recorded fixtures; parameterize their expected values from independent inputs and test one explicit supported parameter change.

Software: Check validity, part/feature counts, controlling dimensions and saved readback; regenerate the declared variant and compare expected dependency changes.

Agent: Independent reviewer checks source feature meaning and selector behavior across variants, using same-revision views.

Inputs: Generated artifacts; source/brief mapping; per-feature criteria; supplied variant and expected response when requested.

Output/check: Validated parametric source, cad-solid for compatible B-rep route, and verification receipt for CAD-13/DOM-04/DOM-05. Validation: Both source and actual geometry satisfy their contracts; a wrong face selection after parameter change fails even when the solid is valid.

Dependencies: Native/independent shape queries, CAD-13 and selected backend regenerate/save APIs.

Resources: Local regeneration may dominate readback; compare actual feature/face count and runtime. Remote/VLM review targets semantic variant changes; manual corrections recorded.

Reuse: [check_ngv064_wheel.py](/tmp/opencode/check_ngv064_wheel.py), [build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py), [neugart-ngv064-wheel-160-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/neugart-ngv064-wheel-160-native.json), [item-angle-bracket-set-41115-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-angle-bracket-set-41115-native.json), [item-profile-02633-segment-100mm-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm-native.json), [nissan-leaf-gen2-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/nissan-leaf-gen2-native.json), [bmw-i3-94ah-native-checks.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/bmw-i3-94ah-native-checks.json). Restricted native surface checks and retained pre-save component results; choose reader for actual representation.

Source-supported tools: CadQuery; build123d; OpenSCAD; FreeCAD Python. Original evidence: [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 120. Select the assembly-aware exporter and settings (DOM-39-A02)

Original action: [Select the assembly-aware exporter and settings](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-39 — Export STEP assembly.

Implementation proposal: Proposal: exporter capability adapter that declares preserved product structure and blocks mismatched route selection.

Software: Inspect OCCT STEPCAFControl_Writer document/label/root-assembly transfer and name/color options; record root-label length unit or Cascade fallback and actual schema settings. Use the selected tested assembly-aware adapter; compare actual consumer readback.

Agent: Choose a route matching hierarchy and analytic/faceted requirements; compare alternatives using actual consumer checks.

Inputs: Frozen export contract; actual exporter/version capabilities; target schema; unit/healing/tessellation settings.

Output/check: Exporter configuration and capability mapping, consumed by DOM-39-A03. Validation: Trace every required invariant to an actual exporter capability or future fixture check; unit declaration must be referenced and verified by consumer readback.

Dependencies: OCCT 8.0.1 STEPCAFControl_Writer source documentation and archived FreeCAD preferences. The inspected OCS writer emits one faceted shell and an SI millimetre entity unreferenced by its geometric context; consumer unit interpretation requires an exercised fixture.

Resources: Local capability inspection precedes export; CPU/RAM estimate follows component/face count. Remote/manual work compares consumer and representation constraints.

Source-supported tools: FreeCAD/Open CASCADE STEP adapter. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 121. Write the STEP derivative and preservation mapping (DOM-39-A03)

Original action: [Write the STEP derivative and preservation mapping](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-39 — Export STEP assembly.

Implementation proposal: Proposal: export transaction/report wrapper with stable operation identity and source/output lineage.

Software: Export to a new path; capture product/occurrence labels and placement mapping where provided; retain dropped/changed-field report.

Agent: Inspect warnings and determine whether a loss affects the named consumer use.

Inputs: Frozen source; selected exporter/configuration; authorized derivative path; preservation contract.

Output/check: STEP bytes/hash, export log and native-to-STEP mapping, consumed by DOM-39-A04. Validation: Verify nonempty readable STEP, unchanged native source and completed output bytes; inspect schema/unit/product entities before consumer import.

Dependencies: Selected STEP exporter and native assembly API; destination writing follows existing project scope.

Resources: Local export CPU/RAM/storage depends on faces/products; no reconstruction inference. Agent reviews warnings; record manual intervention and any remote review.

Source-supported tools: FreeCAD/Open CASCADE STEP adapter. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 122. Reopen and compare the exported assembly (DOM-39-A04)

Original action: [Reopen and compare the exported assembly](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json). Operations: DOM-39 — Export STEP assembly.

Implementation proposal: Proposal: assembly exchange comparator using stable source-object mappings plus explicit failure localization.

Software: Import into an isolated consumer; compare definition/occurrence counts, parent relationships, names, transforms, surface types and required interfaces.

Agent: Independent reviewer checks semantic part/occurrence mapping and same-geometry views; assess whether required details survive.

Inputs: Exported STEP/hash; frozen native manifest; feature criteria; actual consumer and optional second reader.

Output/check: Export verification, checked derivative and field-loss report, consumed by the intended receiver/DOM-26. Validation: Numerical invariants and independent semantic mapping must both pass for the named use; compare per-part closed-shape volume only where applicable and distinguish union from occurrence totals. Compare parent paths and both local and composed world transforms; identical geometry hashes and aggregate counts cannot identify repeated occurrences alone.

Dependencies: Actual receiving importer and shape/assembly inspection APIs; second reader's shared kernel dependencies recorded.

Resources: Begin with structure/units/transforms; detailed topology/features scale with entity count. Remote VLM review is supplementary evidence; log latency and manual mapping effort.

Source-supported tools: FreeCAD/Open CASCADE STEP adapter. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 123. Diagnose the earliest invalid source-to-geometry transition (CAD-14-A02)

Original action: [Diagnose the earliest invalid source-to-geometry transition](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-14 — Recover from failed interpretation or geometry construction.

Implementation proposal: Proposal: causal transition map linking failed predicates to source/constraint/feature/export actions.

Software: Compare source entities, constraints and feature parameters; isolate minimal failing inputs and shape/query errors without changing source.

Agent: VLM reviews source-to-feature correspondence; reasoning agent distinguishes source ambiguity, wrong mapping, unsupported backend and invalid geometry.

Inputs: Reconciled failure receipt; original source views/values; constraint residuals; kernel errors; importer/exporter findings.

Output/check: Diagnosis with candidate corrections and dependencies for CAD-14-A03. Validation: Independent reviewer tests the diagnosis against preserved observations; a suggested tolerance increase must address the actual sourced requirement.

Dependencies: Native diagnostics, source overlays and kernel validity reports; actual tool capability records.

Resources: Local comparison uses retained records first; geometry isolation is a separate authorized computation. Remote/VLM calls and manual diagnosis are measured separately.

Reuse: [ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md), [cad-workflow-findings.md](/home/leo/projects/ferme/skills/cad-workflow-findings.md). Recorded topology, command-state, bounds and capture failures; component-specific recovery decisions.

Source-supported tools: source overlay, operation logs, constraint residuals, OCS operation status/revision readback, CAD kernel validity reports. Original evidence: [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md), [/home/leo/projects/energy/eoliennes/research/cad-workflow/harness-findings.md](/home/leo/projects/energy/eoliennes/research/cad-workflow/harness-findings.md), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md).

### 124. Revise the brief and issue a bounded retry plan (CAD-14-A03)

Original action: [Revise the brief and issue a bounded retry plan](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). Operations: CAD-14 — Recover from failed interpretation or geometry construction.

Implementation proposal: Proposal: recovery-plan emitter with per-action prerequisites, restart boundary and required rechecks.

Software: Update source/feature mappings and dependency invalidation; preserve original models and failed artifacts.

Agent: Select evidence-supported correction within existing requirements; prepare new geometry execution through its owning operation.

Inputs: Diagnosis; explicit correction/required user decision; previous brief; original evidence and source revisions.

Output/check: New model-brief revision with retry plan, consumed by the named CAD-08/09/10/15 or DOM operation. Validation: Check the plan repairs the diagnosed transition and preserves unrelated features; later owning-operation execution must read back actual geometry.

Dependencies: Existing brief/version records and owning-operation contracts; geometry mutation belongs to that operation's authorized action.

Resources: Local metadata/dependency work is bounded by affected records. Remote/manual effort records correction choices; actual rerun cost belongs to the owning operation.

Reuse: [ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md), [cad-workflow-findings.md](/home/leo/projects/ferme/skills/cad-workflow-findings.md). Recorded topology, command-state, bounds and capture failures; component-specific recovery decisions.

Source-supported tools: source overlay, operation logs, constraint residuals, OCS operation status/revision readback, CAD kernel validity reports. Original evidence: [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md), [/home/leo/projects/energy/eoliennes/research/cad-workflow/harness-findings.md](/home/leo/projects/energy/eoliennes/research/cad-workflow/harness-findings.md), [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md).

### 125. Estimate plane mapping and rectified derivative (CAD-02-A02)

Original action: [Estimate plane mapping and rectified derivative](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-02 — Rectify a raster drawing plane from known dimensions.

Implementation proposal: Proposal: rectification adapter emits matrix/inverse, valid domain, fit diagnostics and sampling receipt.

Software: Use getPerspectiveTransform for four suitable point pairs or documented estimator; warpPerspective samples derivative.

Agent: Inspect control order, spatial coverage, stretching and unsupported plane assumptions.

Inputs: Plane/control manifest; selected model; output sampling/interpolation; target units/frame.

Output/check: Transform, coordinate inverse where defined, ancillary rectified derivative and fit report. Validation: Check finite/invertible mapping and residual distribution across feature regions; inverse maps coordinates, while source pixels remain preserved separately.

Dependencies: Selected OpenCV signatures; image/crop pixel-center and coordinate conventions.

Resources: Small matrix fit precedes pixel-scale warping; CPU/RAM follows output resolution; remote review uses source+derivative.

Source-supported tools: OpenCV point correspondences, planar homography. Original evidence: [https://docs.opencv.org/5.0/main_modules/calib.html](https://docs.opencv.org/5.0/main_modules/calib.html).

### 126. Check independent controls and publish measurements (CAD-02-A03)

Original action: [Check independent controls and publish measurements](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-02 — Rectify a raster drawing plane from known dimensions.

Implementation proposal: Proposal: planar checker consumes mapping/checks/criteria and emits residual rows and named downstream readiness.

Software: Transform withheld endpoints and compare dimensions; verify regional scale and frame signs.

Agent: Independent reviewer checks feature/control correspondence and residual page/lens distortion.

Inputs: Mapping; withheld checks; source uncertainty and per-feature criteria.

Output/check: Measurement-set with original/transformed coordinates, units/frame, method, uncertainty and readiness; derivative is ancillary. Validation: Fitted-control agreement and independent-check agreement remain separate; failures block only affected metric uses.

Dependencies: Actual mapping implementation, independent controls, model-contract fields.

Resources: Few-point checks precede dense sampling; local numerical work and remote/manual review recorded separately.

Source-supported tools: OpenCV point correspondences, planar homography. Original evidence: [https://docs.opencv.org/5.0/main_modules/calib.html](https://docs.opencv.org/5.0/main_modules/calib.html).

### 127. Fit source-supported vector candidates (CAD-04-A02)

Original action: [Fit source-supported vector candidates](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-04 — Extract raster edges, lines and contours.

Implementation proposal: Proposal: curve fitter consumes support pixels/class/criteria and emits typed alternatives, support sets and residuals.

Software: Use HoughLinesP/findContours/approxPolyDP; arc fitting is a separately selected documented or proposed method.

Agent: Choose stroke centreline/boundary and line/arc hypothesis; interpret gaps using source context.

Inputs: Masks; pixel mapping; plane measurement receipt; curve classes and per-feature approximation limits.

Output/check: Segments/contours and separately typed arc candidates with support pixels and fit residuals. Validation: Review local residual distribution and overlays; short/noisy arcs can retain multiple centres/radii.

Dependencies: Pinned OpenCV primitives; arc estimator and class interpretation have separate capability records.

Resources: Local extraction follows pixels/support; curve fitting limited to relevant regions; remote/manual choice recorded.

Source-supported tools: OpenCV thresholding, HoughLinesP, findContours, approxPolyDP. Original evidence: [https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html](https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html), [https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html](https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html), [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html).

### 128. Check geometry and publish vector evidence (CAD-04-A03)

Original action: [Check geometry and publish vector evidence](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-04 — Extract raster edges, lines and contours.

Implementation proposal: Proposal: raster-vector audit outputs typed geometry, source map, change ledger and named check results.

Software: Check duplicates, crossings, endpoints, loop containment and independent controls; serialize supported curves.

Agent: Independent semantic review checks holes, feature presence and annotation separation.

Inputs: Candidates/support pixels; control measurements; selected roles and feature criteria.

Output/check: Vector-drawing with IDs, pixel mapping, topology findings and operation-specific readiness. Validation: Check required holes/openings individually; silhouette agreement accompanies feature checks.

Dependencies: CAD-08/CAD-09 downstream contract; actual vector writer curve support.

Resources: Local checks follow curve/intersection count; remote semantic review and manual repair recorded separately.

Source-supported tools: OpenCV thresholding, HoughLinesP, findContours, approxPolyDP. Original evidence: [https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html](https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html), [https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html](https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html), [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html).

### 129. Recognize glyphs and parse engineering notation (CAD-03-A02)

Original action: [Recognize glyphs and parse engineering notation](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-03 — Recognize dimension text with OCR.

Implementation proposal: Proposal: annotation parser consumes raw TSV/source context and emits typed candidates with unsupported/ambiguous flags.

Software: Run documented TSV recognition; parse signs, decimal separators, fractions, radius/diameter and plus-minus symbols conservatively.

Agent: Compare 0/O, 1/I, punctuation, diameter and tolerance symbols with source pixels.

Inputs: Mapped crops; traineddata/language/version; OCR settings; notation/unit evidence.

Output/check: Raw TSV and parsed candidates retaining literal strings, boxes, hierarchy, confidence and alternatives. Validation: Every interpreted field traces to literal source tokens; uncertainty remains explicit.

Dependencies: Pinned Tesseract/traineddata; engineering parser is proposed.

Resources: Local OCR follows pixels/languages; remote/manual review targets ambiguous glyphs.

Source-supported tools: Tesseract OCR TSV output, image crop/deskew, human transcription review. Original evidence: [https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html).

### 130. Associate text with geometric features (CAD-03-A03)

Original action: [Associate text with geometric features](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-03 — Recognize dimension text with OCR.

Implementation proposal: Proposal: association helper returns candidate links, source locators and selected/ambiguous states.

Software: Test incidence, direction and endpoint consistency; enumerate compatible links instead of nearest-text selection.

Agent: VLM selects supported feature associations using source context and candidate geometry.

Inputs: Text candidates; full view; object/dimension/extension/leader candidates or manual anchors; frame.

Output/check: Association records with label region, feature IDs, endpoints/axis, quantity kind and alternatives. Validation: Independent reviewer checks meaning; software checks endpoint/axis and quantity consistency.

Dependencies: CAD-04 candidates are optional enrichment; manually located anchors permit association before vectorization.

Resources: Local spatial comparisons follow labels/segments; higher reasoning for chains; remote/manual effort recorded separately.

Source-supported tools: Tesseract OCR TSV output, image crop/deskew, human transcription review. Original evidence: [https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html).

### 131. Publish reviewed text and association evidence (CAD-03-A04)

Original action: [Publish reviewed text and association evidence](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-03 — Recognize dimension text with OCR.

Implementation proposal: Proposal: evidence exporter emits reviewed text plus structured companion records.

Software: Check field completeness, units, duplicate IDs and conflicting repeated values.

Agent: Independent reviewer verifies literal text and feature associations against source.

Inputs: Raw/parsed candidates; associations; source views; review and feature requirements.

Output/check: Reviewed text with source/crop IDs, units/tolerances, associations and unresolved alternatives. Validation: Each usable controlling dimension has source-linked literal and association checks.

Dependencies: Point01 brief intake and original text output contract.

Resources: Record validation is small local work; remote review/manual correction tracked per annotation set.

Source-supported tools: Tesseract OCR TSV output, image crop/deskew, human transcription review. Original evidence: [https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html).

### 132. Match source features and solve registration candidates (CAD-06-A02)

Original action: [Match source features and solve registration candidates](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-06 — Register orthographic drawing views in a shared coordinate frame.

Implementation proposal: Proposal: correspondence solver emits candidate links, transform receipts and contradictions from view manifests/vectors.

Software: Project common-axis coordinates, compare compatible vertices/edges and solve declared scale/offset transforms; retain multiple matches.

Agent: VLM uses complete labelled views to interpret repeated/symmetric features and hidden/visible line roles.

Inputs: View manifest; vector entities; dimension associations; common datum and comparison criteria.

Output/check: Per-view transforms and feature-correspondence alternatives with residuals. Validation: Independent controls and shared-axis residuals check registration; equal projections can retain several 3D interpretations.

Dependencies: Proposed line/vertex matcher plus numeric transform checks; research methods are evidence for algorithms, not an exercised project adapter.

Resources: Local candidate matching scales with features/repetition; prune by source class before comparison; remote/manual interpretation cost separate.

Source-supported tools: view segmentation, projection-axis declaration, line/vertex matching, dimension reconciliation. Original evidence: [https://xnjdxb.swjtu.edu.cn/en/article/id/9616](https://xnjdxb.swjtu.edu.cn/en/article/id/9616), [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html).

### 133. Verify registration and publish reconstruction brief (CAD-06-A03)

Original action: [Verify registration and publish reconstruction brief](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-06 — Register orthographic drawing views in a shared coordinate frame.

Implementation proposal: Proposal: registered-view brief exporter preserves frames, alternate matches and exact downstream prerequisites.

Software: Compare projected control coordinates across views and validate transform chains and feature IDs.

Agent: Independent reviewer checks convention, visible/hidden/section roles and source meaning.

Inputs: View transforms/correspondences; independent controls; source dimensional evidence and intended part features.

Output/check: Model-brief containing projection frames, correspondences, known dimensions, inferred/ambiguous fields and readiness. Validation: Reconstruction readiness names features and source constraints; successful registration alone cannot choose among equal-projection shapes.

Dependencies: Point01 brief evidence contract; CAD-07 explicit vector/measurement/brief inputs.

Resources: Local projection checks are bounded by feature count; remote review uses full views plus located regions; manual missing-source work recorded.

Source-supported tools: view segmentation, projection-axis declaration, line/vertex matching, dimension reconciliation. Original evidence: [https://xnjdxb.swjtu.edu.cn/en/article/id/9616](https://xnjdxb.swjtu.edu.cn/en/article/id/9616), [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html).

### 134. Construct candidate edges and bounded surfaces (CAD-07-A02)

Original action: [Construct candidate edges and bounded surfaces](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-07 — Reconstruct a candidate 3D wireframe and surface from orthographic views.

Implementation proposal: Proposal: reconstruction adapter consumes hypothesis/sequence and emits typed edges/faces plus lineage.

Software: Use supported sketch/edge/face operations or source-backed feature construction; retain each intermediate representation.

Agent: Diagnose inconsistent edges, face orientation and hidden-surface assumptions.

Inputs: Selected hypothesis; explicit geometry/feature sequence; kernel capabilities; per-feature criteria.

Output/check: Candidate wireframe/faces with feature IDs, source links and construction receipt. Validation: Check projected edges and dimensions before sealing; open surface remains an intermediate artifact.

Dependencies: CAD-09/CAD-10 supported backend subset; research method output may require a proposed adapter.

Resources: Local kernel cost follows curves/faces and intersections; remote agent diagnoses semantic or kernel exceptions.

Source-supported tools: multi-view edge correspondence, wireframe/face reconstruction, OpenCASCADE or FreeCAD surface/solid creation. Original evidence: [https://www.sciencedirect.com/science/article/pii/S0097849323000766](https://www.sciencedirect.com/science/article/pii/S0097849323000766), [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html).

### 135. Form and inspect the required solid (CAD-07-A03)

Original action: [Form and inspect the required solid](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-07 — Reconstruct a candidate 3D wireframe and surface from orthographic views.

Implementation proposal: Proposal: solid readiness checker accepts candidate boundary/criteria and reports actual class and blocking boundaries.

Software: Use supported sewing/solid/feature operations; query closedness, validity, volumes where meaningful and required part boundaries.

Agent: Review whether a repair changes hidden geometry or merges intended parts.

Inputs: Candidate faces/features; body/component intent; kernel closure/validity capabilities.

Output/check: Actual solid candidate or retained incomplete surface state, with structure/geometry check report. Validation: CAD-07 cad-solid readiness requires a closed valid supported shape; a surface/mesh alone retains its actual class.

Dependencies: Selected FreeCAD/Open CASCADE or OCS supported construction; CAD-10 capability gates.

Resources: Local validity/solid operations scale with topology and surfaces; remote/manual repair effort recorded separately.

Source-supported tools: multi-view edge correspondence, wireframe/face reconstruction, OpenCASCADE or FreeCAD surface/solid creation. Original evidence: [https://www.sciencedirect.com/science/article/pii/S0097849323000766](https://www.sciencedirect.com/science/article/pii/S0097849323000766), [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html).

### 136. Project back to every view and publish checked geometry (CAD-07-A04)

Original action: [Project back to every view and publish checked geometry](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-07 — Reconstruct a candidate 3D wireframe and surface from orthographic views.

Implementation proposal: Proposal: multiview verifier emits located edge/dimension residuals, feature coverage and unresolved alternatives.

Software: Project geometry into each view, compare corresponding visible/hidden edges and controls; save/reopen only within construction scope via CAD-13.

Agent: Independent semantic reviewer checks missing/extra features, visibility and source associations.

Inputs: Actual candidate solid; all view projections; source dimensions; withheld checks and native artifact scope.

Output/check: Checked cad-solid and measured feature set; source projections and saved-readback receipt accompany them. Validation: A kernel-valid body with wrong hole/depth fails source checks; equal projections alone cannot resolve unseen geometry.

Dependencies: Supported projection and CAD-13 read-only verification interfaces; independent query/reader records.

Resources: Local projection scales with edges/faces; high-detail checks focus required features; remote semantic review uses source+projected overlays.

Source-supported tools: multi-view edge correspondence, wireframe/face reconstruction, OpenCASCADE or FreeCAD surface/solid creation. Original evidence: [https://www.sciencedirect.com/science/article/pii/S0097849323000766](https://www.sciencedirect.com/science/article/pii/S0097849323000766), [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html).

### 137. Construct dimensioned wall and opening relationships (CAD-05-A02)

Original action: [Construct dimensioned wall and opening relationships](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-05 — Convert raster floor-plan candidates into a wall and opening graph.

Implementation proposal: Proposal: graph builder consumes candidates/conventions/criteria and emits nodes, wall paths, opening host/intervals and residuals.

Software: Build adjacency and containment; attach opening intervals to host wall paths; apply explicit dimensions with recorded residuals.

Agent: Resolve T/cross junctions, breaks, duplicate strokes and wall boundary/centreline offsets.

Inputs: Wall/opening candidates; measurement-set; dimension associations; selected convention and criteria.

Output/check: Graph nodes/wall edges/opening-host records encoded with vector-drawing metadata. Validation: Check host existence and interval containment, coincident endpoints within criteria, room boundaries where meaningful and sourced angular relations.

Dependencies: Proposed graph builder over actual supported line/arc geometry; point03 curve/unit checks.

Resources: Local graph operations follow vertices/edges; intersection cost follows candidates; remote/manual work resolves topology exceptions.

Source-supported tools: floor-plan segmentation/vectorization model or manual trace, graph consistency checks, OCS or FreeCAD Draft. Original evidence: [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html), [https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf), [https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf).

### 138. Verify plan graph and publish vector handoff (CAD-05-A03)

Original action: [Verify plan graph and publish vector handoff](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-05 — Convert raster floor-plan candidates into a wall and opening graph.

Implementation proposal: Proposal: plan-graph verifier emits geometric/semantic findings and downstream element readiness.

Software: Measure wall lengths/thicknesses, opening stations/spans; test graph integrity, IDs and selected room connectivity.

Agent: Independent reviewer checks real openings, host selection, symbol interpretation and required coverage.

Inputs: Graph; original plan; independent controls; selected convention and required feature coverage.

Output/check: Checked vector-drawing plus graph/source metadata, measurements and per-element readiness. Validation: Curved/nonorthogonal walls retain actual geometry; unsupported downstream curves are explicit route exceptions.

Dependencies: Versioned graph serializer and dimensional checks; original CAD-05 output remains vector-drawing.

Resources: Local graph checks first; full-resolution source regions for critical openings; remote/manual review cost tracked separately.

Source-supported tools: floor-plan segmentation/vectorization model or manual trace, graph consistency checks, OCS or FreeCAD Draft. Original evidence: [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html), [https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf), [https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf).

### 139. Create explicit IFC identity, units and spatial structure (DOM-18-A02)

Original action: [Create explicit IFC identity, units and spatial structure](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: DOM-18 — Raster floor plan to IFC building.

Implementation proposal: Proposal: IFC context builder consumes semantic/placement records and emits identity/units/context hierarchy receipts.

Software: Use documented project/root/unit/context APIs and aggregate/spatial relationships; read created IDs and placements.

Agent: Review semantic classes and hierarchy against source use; avoid inferring geographic registration from plan appearance.

Inputs: Building manifest; explicit schema/unit choice; project/site/building/storey records and placements.

Output/check: IFC document with unique identities, units, representation contexts and spatial hierarchy. Validation: Schema/unit and unique-ID checks pass; source storey elevations and local/world transforms match declared frames.

Dependencies: Selected IfcOpenShell/Bonsai schema/API version; DOM-R01 documented entrypoints.

Resources: Local metadata/relationship creation scales with elements; remote review covers semantic decisions; manual hierarchy corrections recorded.

Source-supported tools: Image calibration; OCS/FreeCAD sketching; Bonsai/IfcOpenShell. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html).

### 140. Author placed wall/opening geometry and host relations (DOM-18-A03)

Original action: [Author placed wall/opening geometry and host relations](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: DOM-18 — Raster floor plan to IFC building.

Implementation proposal: Proposal: building element adapter accepts wall/opening/placement records and emits geometry, identity and host-relation receipts.

Software: Create element identities, assign supported geometry and local placement; then call feature.add_feature with existing opening and host to obtain IfcRelVoidsElement. Use source-backed create_2pt_wall only within its supported geometry class. Record whether placement translations use SI units or project units, including the actual is_si setting; geometry evaluation timing is recorded from the selected implementation.

Agent: Interpret host, wall-local +X direction and thickness-side +Y; choose separate supported route for curved/nonconforming walls.

Inputs: Reviewed wall/opening graph; dimensions/elevations; IFC context; source-library items; compatible CAD-17 geometry where used.

Output/check: Placed IfcWall/IfcOpeningElement records, representations and explicit host void relationships with source mapping. Validation: Element creation, representation/placement and host relation are separately checked; relation API consumes an existing opening. Actual opening geometry is evaluated/queried using the selected supported implementation.

Dependencies: IfcOpenShell geometry/placement/feature APIs; existing CAD geometry transfer needs an evidenced adapter and preservation checks.

Resources: Local geometry cost follows walls/openings and Boolean evaluation; semantic record work separate; remote/manual host review recorded.

Source-supported tools: Image calibration; OCS/FreeCAD sketching; Bonsai/IfcOpenShell. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html).

### 141. Validate saved IFC geometry and semantics (DOM-18-A04)

Original action: [Validate saved IFC geometry and semantics](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: DOM-18 — Raster floor plan to IFC building.

Implementation proposal: Proposal: IFC source verifier emits separate schema, relationship, dimensional, projection and source-correspondence reports.

Software: Write within scoped authoring output; reopen read-only; validate schema/IDs/units/placements, hierarchy, host void relations and actual wall/opening geometry.

Agent: Independent reviewer checks source-to-element classification, host meaning and feature coverage using plan/elevation views.

Inputs: Authored IFC revision; all source manifests; per-feature criteria; intended schema/consumer.

Output/check: Saved IFC hash, reopened geometry/relationship findings, source/ID map and downstream readiness. Validation: Valid schema alone cannot pass wrong host/units/height; required void is checked in evaluated geometry and relation graph.

Dependencies: Selected IfcOpenShell validator/geometry API and independent consumer where available; CAD-13 measurement pattern.

Resources: Local parse/relationship checks precede geometry evaluation; resource evidence names element/face counts; remote reviewer/manual work separate.

Source-supported tools: Image calibration; OCS/FreeCAD sketching; Bonsai/IfcOpenShell. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html).

### 142. Construct walls and opening voids with retained identities (CAD-17-A02)

Original action: [Construct walls and opening voids with retained identities](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-17 — Build wall and opening solids from a confirmed floor-plan graph.

Implementation proposal: Proposal: wall assembly executor accepts feature records and emits wall/cutter handles, Boolean receipts and source mappings.

Software: Construct supported wall profiles/solids; create separately identified opening cutters; subtract with explicit preservation flags and query result type.

Agent: Diagnose junction overlaps, reversed offset/sill direction and unsupported curve/Boolean cases.

Inputs: Complete feature plan; target document/revision; supported native kernel and explicit operand-retention policy.

Output/check: Wall solids, retained opening cutter/void records and assembly mapping with operation receipts. Validation: Each opening affects only intended host geometry; assembly/group representation records actual available identity semantics.

Dependencies: CAD-10 native capability gates; OCS explicit delete_source/keep_operands flags; FreeCAD alternative when selected.

Resources: Local cost follows walls/faces/cuts; curved Booleans may dominate; remote/manual diagnosis and display GPU role separate.

Source-supported tools: FreeCAD Part/Sketcher or OCS native geometry, wall/opening graph interpretation, human confirmation. Original evidence: [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html), [https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf), [https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md).

### 143. Validate plan, elevation and saved assembly (CAD-17-A03)

Original action: [Validate plan, elevation and saved assembly](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: CAD-17 — Build wall and opening solids from a confirmed floor-plan graph.

Implementation proposal: Proposal: wall assembly verifier emits plan/elevation/host comparisons and saved-revision mapping.

Software: Measure wall lengths/thickness/heights and opening station/sill/clear size; check part identity and save/reopen via point03 rules.

Agent: Independent reviewer checks host identity, junction meaning and required opening coverage.

Inputs: Actual assembly revision; wall/opening mapping; source plan and elevations; per-feature criteria.

Output/check: Checked CAD assembly with geometry/source manifest and readiness for named downstream use. Validation: Plan projection alone cannot pass height/sill checks; separate wall/opening identity persists after save.

Dependencies: CAD-13 dimensional/readback checks; CAD assembly representation supports only documented identities.

Resources: Local required-feature checks precede whole-model comparisons; remote full/section review and manual work tracked.

Source-supported tools: FreeCAD Part/Sketcher or OCS native geometry, wall/opening graph interpretation, human confirmation. Original evidence: [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html), [https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf), [https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf), [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md).

### 144. Compose calibrated vectors and source-linked constraints (DOM-02-A02)

Original action: [Compose calibrated vectors and source-linked constraints](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: DOM-02 — Raster sketch to constrained sketch.

Implementation proposal: Proposal: raster-sketch composer maps source feature records into native geometry/constraints and retains all upstream receipts.

Software: Reuse valid calibration/OCR/vector results; invoke CAD-09 supported geometry/constraint operations and read actual diagnostics.

Agent: Select source-supported line/arc/profile meaning and intended remaining degrees of freedom.

Inputs: Intake; valid CAD-02 measurements when required; CAD-03 annotations; CAD-04 vectors or manual trace; sketch parameters.

Output/check: Native sketch revision with pixel-to-curve-to-constraint map and reused action receipts. Validation: Actual constraint data and source map are present; unavailable required diagnostics remain unresolved.

Dependencies: FreeCAD Sketcher documented construction and discovered diagnostics; OCS route only with evidenced native constraint output.

Resources: Local tracing/solver cost follows curves/relations; remote/manual work resolves semantic association.

Source-supported tools: OpenCADStudio; FreeCAD Sketcher; manual image tracing. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 145. Verify solved geometry and saved editability (DOM-02-A03)

Original action: [Verify solved geometry and saved editability](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json). Operations: DOM-02 — Raster sketch to constrained sketch.

Implementation proposal: Proposal: raster-sketch verifier outputs source, solver and saved-editability results separately.

Software: Check dimensions, closure/intersections, intended degrees of freedom and retained constraints on reopen.

Agent: Independent reviewer checks annotation-to-feature meaning and solved movements against source.

Inputs: Solved sketch; original raster; independent controls; source requirements and saved artifact scope.

Output/check: Checked native constrained-sketch, source map and solver/dimensional/semantic report. Validation: Correct solver state with wrong association fails semantic/dimensional source check; native constraints survive save.

Dependencies: CAD-09/CAD-13; actual native save/readback interfaces.

Resources: Local required-feature checks first; remote reviewer sees source/full sketch and located discrepancies; manual corrections recorded.

Source-supported tools: OpenCADStudio; FreeCAD Sketcher; manual image tracing. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 146. Extract selected frames with reversible timeline mapping (REC-04-A02)

Original action: [Extract selected frames with reversible timeline mapping](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-04 — Convert video into an image reconstruction dataset.

Implementation proposal: Proposal: frame extractor accepts timeline selections and outputs images plus frame/time/pixel manifest.

Software: Decode selected source frames with supported FFmpeg selection; retain exact timestamps and avoid synthesizing intermediate views.

Agent: Review selected viewpoints and omissions against complete interval.

Inputs: Video/selection plan, decoder version and resize/rotation/colour policy.

Output/check: Frame images with original index/timestamp/source hash and pixel-processing map. Validation: Derived frame label must identify original event; duplicates and interpolation retain explicit status.

Dependencies: Exact selected FFmpeg build/options; build-dependent software licence separate from media rights.

Resources: Local decode cost follows duration/resolution/codec and chosen frames; no dense reconstruction yet.

Source-supported tools: ffmpeg frame extraction, blur/duplicate-frame filtering, COLMAP or Meshroom downstream. Original evidence: [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md), [https://github.com/nerfstudio-project/nerfstudio](https://github.com/nerfstudio-project/nerfstudio).

### 147. Check dataset quality and camera compatibility (REC-04-A03)

Original action: [Check dataset quality and camera compatibility](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-04 — Convert video into an image reconstruction dataset.

Implementation proposal: Proposal: frame-set verifier emits per-image quality/camera/timeline readiness.

Software: Check hashes, monotonic timestamps per stream, duplicate rates and compatible image/calibration dimensions.

Agent: Separate reviewer checks missed viewpoint bridges, dynamics and source/generated classification.

Inputs: Extracted frames, source interval and camera/calibration state.

Output/check: Checked photo-set with coverage, quality and timing exceptions. Validation: Many adjacent images do not substitute geometric baseline; moving/blurred regions remain explicit.

Dependencies: Proposed dataset checker and point05 camera/preprocessing contract.

Resources: Local quality summaries before remote image review; manual capture effort separate.

Source-supported tools: ffmpeg frame extraction, blur/duplicate-frame filtering, COLMAP or Meshroom downstream. Original evidence: [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md), [https://github.com/nerfstudio-project/nerfstudio](https://github.com/nerfstudio-project/nerfstudio).

### 148. Generate independently framed convex pieces (DOM-13-A02)

Original action: [Generate independently framed convex pieces](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-13 — Generate convex collision set.

Implementation proposal: Proposal: decomposition adapter accepts mesh/frame/settings and emits individually addressable pieces plus errors/loss map.

Software: Use source-backed CoACD CLI adapter with split individual components, or supported primitive fitting. Record -t/--threshold normalized concavity versus -rm/--real-metric metre error mode (input must be metre scale), and merge/max-convex-hull interaction; hull-count limiting may exceed threshold. The source default 0.05 is an example/default, never a project criterion.

Agent: Review candidate decomposition meaning and protect narrow gaps.

Inputs: Per-body mesh/plan, selected algorithm/version and sourced approximation settings.

Output/check: Convex pieces with original body ID, transforms, settings and source hashes. Validation: Piece transforms and convexity/finite geometry checked; decomposition does not assign mass properties.

Dependencies: Inspected current CoACD README: -i/--input OBJ, -o/--output OBJ or WRL; -sp/--split writes individual components under output_parts. Pin selected version before execution. Older short/long dossier spellings are aliases in this inspected source.

Resources: Local cost follows triangles, hull count and search settings; coarse/protected-region option first; remote review separate.

Source-supported tools: CoACD; V-HACD; primitive fitting. Original evidence: [https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE), [https://github.com/kmammou/v-hacd/blob/master/LICENSE](https://github.com/kmammou/v-hacd/blob/master/LICENSE), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst).

### 149. Validate passages and intended contact behavior (DOM-13-A03)

Original action: [Validate passages and intended contact behavior](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-13 — Generate convex collision set.

Implementation proposal: Proposal: collision verifier reports per-feature envelope, penetration/clearance and contact outcomes.

Software: Measure piece/source deviations and passage dimensions; future target fixture checks expected contact/non-contact at named poses.

Agent: Separate reviewer checks body association and retained contact meaning.

Inputs: Candidate pieces, source mesh, protected features and future target-contact fixtures.

Output/check: Approximation report and checked collision-set. Validation: Volume/bounds alone cannot pass passage/contact criteria; compile and runtime contact checks have distinct results.

Dependencies: Geometric comparator and selected simulator fixture adapter proposals.

Resources: Local geometry checks before consumer fixtures; fixture cost follows piece/pair counts, remote/manual assessment separate.

Source-supported tools: CoACD; V-HACD; primitive fitting. Original evidence: [https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE), [https://github.com/kmammou/v-hacd/blob/master/LICENSE](https://github.com/kmammou/v-hacd/blob/master/LICENSE), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst).

### 150. Export source-linked mesh assets (DOM-12-A02)

Original action: [Export source-linked mesh assets](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-12 — Export mesh assets for MuJoCo.

Implementation proposal: Proposal: mesh exporter accepts occurrence/frame/role settings and returns meshes plus approximation/loss ledger.

Software: Use supported OCS mesh export/native triangulation where adequate; capability-gated CAD/Blender adapter for required formats; retain local coordinates and explicit transforms.

Agent: Review any material/normal/surface interpretation changes.

Inputs: Selected geometry, unit/frame transforms, tessellation settings and format.

Output/check: Meshes with hashes, per-piece source maps and export receipt. Validation: Movable body assets preserve distinct frames; serialization records actual supported encoding.

Dependencies: Selected actual exporter and target mesh loader; no unsupported API assumed. Inspected MuJoCo accepts STL, OBJ and MSH; verify selected version/encoding. Keep raw asset coordinates, mesh scale and effective compiler mesh_pos/mesh_quat transforms.

Resources: Local cost follows faces, tessellation density and asset count; GPU only if actual exporter uses it.

Source-supported tools: CAD mesh exporter; Blender; Open CASCADE tessellation. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 151. Compare meshes to source and reopen (DOM-12-A03)

Original action: [Compare meshes to source and reopen](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-12 — Export mesh assets for MuJoCo.

Implementation proposal: Proposal: asset checker emits source-to-mesh residuals, frame/unit checks and parser outcomes.

Software: Load target-supported mesh format; compare bounds, selected interfaces, orientation and surface deviations. For MuJoCo load, compare effective placed surfaces using recorded mesh_scale, mesh_pos/mesh_quat and geom/body/world transforms; validate composition against the selected version's reader.

Agent: Independent reviewer checks part identity, omissions and intended role.

Inputs: Exported meshes, source geometry and independent interface controls.

Output/check: Mesh set with loader/readback, deviation and role-readiness reports. Validation: Bounds alone cannot verify a bore or passage; collision and mass suitability have separate downstream checks.

Dependencies: Proposed mesh comparator and target loader fixture.

Resources: Local selected-feature checks before dense distances; remote view review/manual controls separate.

Source-supported tools: CAD mesh exporter; Blender; Open CASCADE tessellation. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 152. Build articulated link and joint representation (DOM-08-A02)

Original action: [Build articulated link and joint representation](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-08 — CAD assembly to articulated robot structure.

Implementation proposal: Proposal: articulation adapter emits joint/geometry frame maps and supported/unsupported relation ledger.

Software: Compose local transforms; validate tree/loop structure and preserve source geometry links.

Agent: Map application constraints only where physical joint meaning is evidenced.

Inputs: Link map; authored joint types/axes/limits; reference pose.

Output/check: Robot assembly with links, joints, geometry transforms and explicit loop edges. Validation: Source joint type and degrees of freedom survive; arbitrary spanning-tree reduction cannot discard closure.

Dependencies: Documented source assembly adapter or proposed explicit mapper; consumer capability discovery.

Resources: Local matrices/graph checks low relative to mesh processing; model calls only for semantics.

Source-supported tools: FreeCAD Assembly Workbench; explicit robot-description authoring; CAD-to-URDF scripts as candidates. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md), [https://github.com/boelnasr/CAD_TO_URDF](https://github.com/boelnasr/CAD_TO_URDF).

### 153. Validate robot assembly against measured configurations (DOM-08-A03)

Original action: [Validate robot assembly against measured configurations](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-08 — CAD assembly to articulated robot structure.

Implementation proposal: Proposal: robot-assembly checker reports per-link/joint residuals and format-specific prerequisites.

Software: Compare reference and supplied test poses via forward transforms; check axes/limits and geometry placement.

Agent: Review source part/link identity, motion sign and loop treatment independently.

Inputs: Candidate robot assembly, CAD measurements and specified configuration controls.

Output/check: Checked robot-assembly with link/joint coverage and reference/moved-state reports. Validation: A visually coincident reference pose cannot pass reversed motion axis or missing closure.

Dependencies: DOM-31 verifier and actual selected CAD readback.

Resources: Local transform/control tests first; collision queries only for requested interfaces; review effort separate.

Source-supported tools: FreeCAD Assembly Workbench; explicit robot-description authoring; CAD-to-URDF scripts as candidates. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md), [https://github.com/boelnasr/CAD_TO_URDF](https://github.com/boelnasr/CAD_TO_URDF).

### 154. Calculate and transform sourced mass properties (DOM-14-A02)

Original action: [Calculate and transform sourced mass properties](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-14 — Calculate or import physical mass properties.

Implementation proposal: Proposal: physical-property adapter accepts measured fields or validated shapes/density plus raw component/sign/reference/unit metadata. It emits no-density geometric integrals, density application count, physical mass/COM/central tensor and frame/aggregation ledger. Length scaling uses volume L³, geometric inertia L⁵ and physical inertia mass×L²; mass/length/density units convert coherently. Reject an unknown source off-diagonal/product convention rather than copy field names.

Software: Source-backed candidate: OCCT 8.0.1 BRepGProp::VolumeProperties fills GProp_GProps with no-density volume integrals. Validate finite closed coherently oriented solids first. Record exact-surface versus UseTriangulation setting and integration-error method. Apply coherent material density once; GProp Mass may initially mean volume, CentreOfMass is absolute and MatrixOfInertia is central with axes parallel to absolute axes. Decode raw tensor order/sign/reference into a common symmetric matrix before shifts/rotations; GProp Add(component,density) can aggregate with parallel-axis shifts when frames/reference conventions match.

Agent: Review hollow/heterogeneous distribution and source assumptions; prevent counting repeated geometry twice.

Inputs: Eligible geometry/density or supplied mass/COM/tensor, reference point/frame, unit conversion and rigid-group membership.

Output/check: Mass, COM and symmetric tensor with raw source values, method and transform receipt. Validation: Compare mass/COM and tensor independently; use I_about_point = I_COM + m((d·d)Identity − d dᵀ) in one frame and I_rotated = R I Rᵀ; inverse shift subtracts that term.

Dependencies: Documented kernel mass-property API and selected format inertia convention; exact API discovery required.

Resources: Local analytic/solid integration before dense mesh integration; cost follows bodies/faces; remote review/manual density data separate.

Source-supported tools: CAD kernel mass properties; MuJoCo compiler geom inference; measured scale. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 155. Check admissibility and consumer-specific completeness (DOM-14-A03)

Original action: [Check admissibility and consumer-specific completeness](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-14 — Calculate or import physical mass properties.

Implementation proposal: Proposal: validator emits field-level admissibility, physical-evidence comparison and consumer readiness.

Software: Check applicable positive mass, tensor symmetry, principal moments and triangle inequalities; compare known analytic fixtures and converted output.

Agent: Separate reviewer confirms body membership, mass distribution meaning and uncertainty labels.

Inputs: Candidate properties, independent measurements and target format requirements.

Output/check: Per-field checked mass-properties with source, reference, uncertainty and readiness. Validation: Admissible tensor values alone establish numerical consistency; supplied physical accuracy has its own evidence.

Dependencies: Proposed numerical property checker; downstream URDF/MJCF readback.

Resources: Small matrix checks low compute; independent physical measurement/manual review separately costed.

Source-supported tools: CAD kernel mass properties; MuJoCo compiler geom inference; measured scale. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md).

### 156. Write GLB and semantic sidecar (DOM-17-A02)

Original action: [Write GLB and semantic sidecar](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-17 — IFC to GLB display scene.

Implementation proposal: Proposal: GLB writer emits scene plus ID/property/loss map; preserves original IFC independently.

Software: Choose one evidenced branch: IfcConvert .glb with explicit metre/default or convert-back-units and use-world-coords settings plus separately checked element-to-node sidecar; OR Python GLB serializer with explicit GUID policy, dimensionality/material settings and setUnitNameAndMagnitude('METER',1.0). Do not claim CLI use-element-guids naming for GLB. Optional Blender chain records its own coordinate/unit conversion.

Agent: Review representation/material simplification and identifier coverage.

Inputs: Checked IFC selection, triangle/settings policy and unit/axis transform.

Output/check: GLB, asset/output hashes and element-node/property sidecar. Validation: Geometry placement and identity map correspond to same source; IFC relationships remain source records.

Dependencies: Pinned converter/serializer and DOM-16 geometry semantics.

Resources: Local tessellation/serialization scales with triangles/materials; display GPU optional and recorded.

Source-supported tools: IfcOpenShell IfcConvert; Blender; GLB export. Original evidence: [https://docs.ifcopenshell.org/introduction.html](https://docs.ifcopenshell.org/introduction.html), [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/), [/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json](/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json).

### 157. Reopen scene and compare identity coverage (DOM-17-A03)

Original action: [Reopen scene and compare identity coverage](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-17 — IFC to GLB display scene.

Implementation proposal: Proposal: scene verifier reports coverage, frame/units and visual/source correspondence.

Software: Reopen GLB independently; inspect node IDs, transforms, bounds, selected openings/materials and sidecar references.

Agent: Separate reviewer compares labelled source/full-context views to display nodes.

Inputs: Saved GLB/sidecar, IFC controls and target viewer.

Output/check: Readback identity, orientation, dimensions and mapping report. Validation: Plausible rendering cannot substitute correct node identity or source semantic preservation.

Dependencies: Target GLB reader and proposed IFC-display comparator.

Resources: Local coverage/transform checks before render review; remote/manual image review separate.

Source-supported tools: IfcOpenShell IfcConvert; Blender; GLB export. Original evidence: [https://docs.ifcopenshell.org/introduction.html](https://docs.ifcopenshell.org/introduction.html), [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/), [/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json](/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json).

### 158. Add static geoms with separate visual and collision roles (DOM-33-A02)

Original action: [Add static geoms with separate visual and collision roles](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-33 — Add environment collision geometry to MJCF.

Implementation proposal: Proposal: static-geom composer emits new XML/assets and per-piece world placement/role ledger.

Software: Add supported worldbody/fixed static geoms; retain original robot graph; keep visual roles distinct from active colliders.

Agent: Review intended obstacle coverage and contact filters.

Inputs: Checked environment plan and per-piece assets/settings.

Output/check: Revised MJCF with static geom/source map and seed-preservation diff. Validation: Adding static obstacles does not invent dynamic-body mass or robot joints.

Dependencies: Pinned MJCF API and DOM-13 piece records.

Resources: Local XML/asset work follows geom count; graphics and contact compute separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst).

### 159. Check robot preservation and obstacle contacts (DOM-33-A03)

Original action: [Check robot preservation and obstacle contacts](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-33 — Add environment collision geometry to MJCF.

Implementation proposal: Proposal: environment verifier reports seed invariants, frame/coverage and per-fixture outcomes.

Software: Reopen/compile; compare robot graph/poses, effective obstacle geometry and source mapping; evaluate named contact/no-contact fixtures when scoped.

Agent: Separate reviewer checks environment identity and required passage meaning.

Inputs: Saved candidate, source seed, frame controls and passage/contact fixtures.

Output/check: Compile/readback, seed invariant and environment/contact reports. Validation: Compile and aggregate bounds cannot pass blocked required opening or wrong collision filter.

Dependencies: Proposed scene diff and selected consumer fixture adapter.

Resources: Local graph/geometry checks precede contact fixtures; effort scales with relevant geom pairs, remote review separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst).

### 160. Serialize links joints and distinct asset origins (DOM-09-A02)

Original action: [Serialize links joints and distinct asset origins](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-09 — Robot assembly to URDF package.

Implementation proposal: Proposal: package writer accepts checked graph/role/tensor records and emits URDF, meshes and mapped omission list.

Software: Proposed exporter writes link/joint/geometry/inertial fields; Xacro source if used retains expansion receipt and resulting URDF.

Agent: Review mapping of names, motion sign and physical-field conventions.

Inputs: Checked tree, sourced inertial records, visual/collision assets and relative paths.

Output/check: URDF plus mesh files, link-to-source map and serialization/loss receipt. Validation: Do not copy unsigned CAD products into tensor entries; tree export preserves all supported relation meaning.

Dependencies: URDF format documentation; actual XML/Xacro/asset adapter capability.

Resources: Local XML work low compute; mesh conversion cost separately inherited from DOM-12.

Source-supported tools: URDF XML/Xacro authoring; ROS urdf_tutorial; CAD-to-URDF adapter proposal. Original evidence: [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial), [https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html](https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html), [https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF](https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF).

### 161. Parse reopen and compare robot poses and physics (DOM-09-A03)

Original action: [Parse reopen and compare robot poses and physics](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-09 — Robot assembly to URDF package.

Implementation proposal: Proposal: package verifier emits type/asset/tree, kinematic and property equivalence results.

Software: Use check_urdf when installed and target consumer load; compare forward transforms at named states, axes/ranges and inertial data.

Agent: Separate reviewer verifies link identity, asset roles and documented losses.

Inputs: Saved package, source graph/properties and independent pose/interface controls.

Output/check: Parser/consumer receipt and source-to-target pose/physics/asset report. Validation: Successful parsing cannot pass wrong axis, missing consumer-required visual/collision role or incorrect inertia. Absent roles remain explicit; a visualization consumer may accept its declared visual-only package.

Dependencies: Target parser/consumer and proposed semantic/diff checker.

Resources: Local parsing/FK before display; consumer graphics and manual review separately recorded.

Source-supported tools: URDF XML/Xacro authoring; ROS urdf_tutorial; CAD-to-URDF adapter proposal. Original evidence: [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial), [https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html](https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html), [https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF](https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF).

### 162. Extract triangles with source and transform mapping (DOM-16-A02)

Original action: [Extract triangles with source and transform mapping](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-16 — Extract IFC geometry as triangles.

Implementation proposal: Proposal: triangle adapter emits per-element meshes, identity/material map and baked-versus-external transform flag.

Software: Use geom.create_shape or iterator; record actual vertices/faces, shape.id and transformation; apply declared local/world placement exactly once and preserve opening settings. create_shape supports selected elements/representations/items/profiles; iterator processes whole elements. Preserve available local vertex/material/item arrays and actual result matrix; Python vertices have no unit tag, so verify settings/project scale through controls. Element-level opening subtraction is documented default.

Agent: Inspect unsupported or missing geometry responses.

Inputs: Selected IFC/settings, source IDs and target-frame policy.

Output/check: Vertices/faces and available material/item IDs, element map and placement/settings receipt. Validation: Element geometry must not be double-transformed; generated IDs retain their namespace and source relation.

Dependencies: Pinned IfcOpenShell 0.9.0post1-documented API; runtime version inspected before execution.

Resources: Local cost follows element geometry and tessellation density; iterator parallelism only when authorized, remote interpretation separate.

Source-supported tools: IfcOpenShell geom.create_shape/iterator; IfcConvert. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html).

### 163. Check element coverage placements and openings (DOM-16-A03)

Original action: [Check element coverage placements and openings](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-16 — Extract IFC geometry as triangles.

Implementation proposal: Proposal: extraction verifier reports element-level geometry/identity results and eligible downstream roles.

Software: Reopen mesh; compare selected dimensions/world placements and opening passages; record elements without output and unsupported metadata.

Agent: Separate reviewer checks visual/source identity and intentional omissions.

Inputs: Saved triangles, source IFC and independent selected geometry controls.

Output/check: Coverage/loss map, frame/bounds/interface/opening checks and readback report. Validation: Triangle extraction does not carry complete IFC relationships; source/sidecar identity stays explicit.

Dependencies: Proposed mesh/IFC comparator; independent source controls.

Resources: Local selected-feature tests first; dense comparison scales with triangles, manual/remote review separate.

Source-supported tools: IfcOpenShell geom.create_shape/iterator; IfcConvert. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html).

### 164. Compose source-linked scene objects and cameras (DOM-24-A02)

Original action: [Compose source-linked scene objects and cameras](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-24 — Assemble and inspect Blender scene.

Implementation proposal: Proposal: scene composer accepts typed imports/transforms/cameras and emits scene plus source/loss manifest.

Software: Use supported bpy import/scene operators or version-compatible bridge; glTF import records Y-up to Z-up and scene scale; preserve evaluated versus source geometry identity.

Agent: Review framing, visibility and appearance decisions using source context.

Inputs: Checked import map, assets, frame transforms and camera/render intent.

Output/check: Scene with object/source IDs, linked assets, transforms and domain-sidecar references. Validation: Scene hierarchy does not replace IFC relationships or robot physical semantics; maps link to those sources.

Dependencies: Actual Blender operator/add-on API; bridge version compatibility checked independently.

Resources: Local mesh/memory scales with geometry; GPU display/render only when needed; model calls separately logged.

Source-supported tools: Blender Python API; Blender MCP; background Blender scripts. Original evidence: [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/), [https://projects.blender.org/lab/blender_mcp/src/branch/main](https://projects.blender.org/lab/blender_mcp/src/branch/main), [https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst](https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst), [https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0](https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0).

### 165. Reopen and inspect scene content numerically and visually (DOM-24-A03)

Original action: [Reopen and inspect scene content numerically and visually](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-24 — Assemble and inspect Blender scene.

Implementation proposal: Proposal: scene verifier emits role-specific checks and source/derivative coverage.

Software: Reopen actual output; query object/world transforms, bounds where geometry exists, camera projection and linked paths.

Agent: Separate reviewer compares full context and source-labelled views; camera-only branch checks camera data without invented geometry.

Inputs: Saved scene/optional requested GLB, source map and feature/camera criteria.

Output/check: Readback object/camera/asset, transform and representative-view report. Validation: Camera-only branch can pass; absent geometry-dependent checks are inapplicable rather than failed.

Dependencies: Selected scene/GLB reader and proposed source-map checker.

Resources: Local numerical checks precede renders; render size/samples and remote image review effort recorded.

Source-supported tools: Blender Python API; Blender MCP; background Blender scripts. Original evidence: [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/), [https://projects.blender.org/lab/blender_mcp/src/branch/main](https://projects.blender.org/lab/blender_mcp/src/branch/main), [https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst](https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst), [https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0](https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0).

### 166. Create placed semantic occurrence with source mapping (DOM-35-A02)

Original action: [Create placed semantic occurrence with source mapping](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-35 — Place library component in semantic IFC.

Implementation proposal: Proposal: library inserter emits new entity/representation/relation IDs and source/placement ledger.

Software: Create product/type as required, create or import supported representation, assign placement and containment; openings/fillings use separate supported relations. add_representation alone supplies only representation.

Agent: Review actual source-to-class/type meaning and instance overrides.

Inputs: Checked representation/class/placement plan and target context.

Output/check: New occurrence/entity, source mapping, representation and spatial/host relations; existing identities retained. Validation: Repeated instances have distinct occurrence identity; source definition and existing IFC IDs stay traceable.

Dependencies: Selected IfcOpenShell/Bonsai capability; Blender-dependent add_representation applies only to its supported input.

Resources: Local entity writes low compute; geometry import complexity varies by asset; remote semantics separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html), [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN).

### 167. Check new occurrence and preserved IFC relationships (DOM-35-A03)

Original action: [Check new occurrence and preserved IFC relationships](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-35 — Place library component in semantic IFC.

Implementation proposal: Proposal: insertion verifier emits source identity, occurrence geometry and preserved-context checks.

Software: Reopen/validate; compare new geometry/placement, class/type/containment and required opening/fill relations; diff existing IDs/relationships.

Agent: Separate reviewer checks source configuration and intended component meaning.

Inputs: Saved candidate, original IFC, component measurements and semantic requirements.

Output/check: Validation/readback, placement/interface and identity/relationship diff. Validation: Visual placement cannot pass wrong class/host; library geometry does not certify product specifications.

Dependencies: DOM-15 verifier and proposed library-source comparator.

Resources: Local graph/selected geometry checks before whole-building derivatives; manual/remote review separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html), [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN).

### 168. Author named joint records and graph topology (DOM-31-A02)

Original action: [Author named joint records and graph topology](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-31 — Author assembly graph and joint set.

Implementation proposal: Proposal: joint author emits typed records and cycle edges, validates unique names, type-applicable axes/normals and limit fields; preserves inapplicable fields explicitly and never invents placeholder axes.

Software: Build adjacency/connected-component/cycle reports; compose frame transforms. Validate fields by actual joint type: revolute/continuous/prismatic motion axis and planar plane normal are nonzero and normalized; fixed/floating axis fields are inapplicable. Apply range/effort/velocity rules required by the selected type/consumer.

Agent: Choose evidence-supported relation mapping; distinguish fixed group, tree joint and loop closure.

Inputs: Checked rigid groups; joint source points/axes, ranges and reference configuration.

Output/check: Joint records with parent/child, type, joint-frame origin/axis, limits/units and tree/loop classification. Validation: Required revolute/continuous/prismatic axes and planar normals are nonzero/unit-normalized in their stated frame; fixed/floating joints require no invented axis. Type-specific units and limit fields agree, and closed loops retain explicit edges. Continuous rotation keeps its sourced axis while omitting finite lower/upper travel bounds; consumer-specific effort/velocity rules remain explicit.

Dependencies: Graph authoring proposal; FreeCAD Assembly source capability when alternate app is explicitly scoped.

Resources: Local graph traversal and matrix checks are low compute by link count; manual motion decisions dominate ambiguous cases.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial).

### 169. Check reference and moved configurations (DOM-31-A03)

Original action: [Check reference and moved configurations](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-31 — Author assembly graph and joint set.

Implementation proposal: Proposal: graph verifier emits per-joint pose residuals, unresolved closure conditions and downstream readiness.

Software: Compose forward kinematics at reference and specified range samples; compare joint centres/axes and loop residuals.

Agent: Separate reviewer checks parent/child meaning, positive motion and preserved fixed groups.

Inputs: Authored graph; reference configuration; sourced test configurations and interface controls.

Output/check: Assembly-graph and joint-set with forward-transform and semantic review receipts. Validation: A tree check cannot discharge loop closure; moving-part identity and source limits pass separately.

Dependencies: Proposed kinematic checker; loop solver separately capability-gated.

Resources: Local transform checks precede any collision/loop solve; remote semantic review and manual fixtures separately recorded.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial).

### 170. Create separate occurrence and authored joint relation (DOM-37-A02)

Original action: [Create separate occurrence and authored joint relation](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-37 — Author robot assembly from CAD component.

Implementation proposal: Proposal: component inserter takes source/target revision and explicit transform and returns native handles plus graph relations.

Software: Use supported OCS placement/native grouping path; capability-gated assembly adapter preserves richer occurrences/constraints.

Agent: Direct explicit placement and relation authoring; distinguish a rigid group from parametric assembly constraints.

Inputs: Attachment plan; target assembly context or explicit new root; measured placement transform.

Output/check: New native occurrence/assembly revision, occurrence-source map and joint candidates. Validation: Source geometry stays pinned; new assembly occurrence IDs and measured interfaces correspond.

Dependencies: Point02 DOM-07 and DOM-31 graph procedure.

Resources: Local one-component placement is bounded; large target assembly query cost depends on occurrences; remote decisions separate.

Source-supported tools: FreeCAD Assembly Workbench or explicit CAD assembly authoring. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial).

### 171. Validate attachment and publish three outputs (DOM-37-A03)

Original action: [Validate attachment and publish three outputs](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-37 — Author robot assembly from CAD component.

Implementation proposal: Proposal: attachment publisher checks cross-artifact IDs/transforms and emits per-output readiness.

Software: Query saved occurrence placement and required geometry; compare graph forward transforms and specified motion configurations.

Agent: Separate reviewer confirms component role and evidence-supported joint semantics.

Inputs: New assembly and graph/joints; independent mount controls and actual saved native revision.

Output/check: Three checked outputs with interface, frame and source receipts. Validation: Geometry grouping alone cannot fulfill joint semantics; all output references match one revision.

Dependencies: Point02 readback and DOM-31 verifier.

Resources: Local focused measurements before broad collision work; remote semantic review and manual controls recorded.

Source-supported tools: FreeCAD Assembly Workbench or explicit CAD assembly authoring. Original evidence: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial).

### 172. Author body tree geoms and explicit closure constraints (DOM-11-A02)

Original action: [Author body tree geoms and explicit closure constraints](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-11 — Author native MJCF simulation model.

Implementation proposal: Proposal: MJCF author maps graph/roles/properties into editable source with explicit inferred/declared field ledger.

Software: Use supported MJCF body/joint/inertial/geom elements or mjSpec API; encode supported equality connect/weld closure only when its constrained freedoms match the source mechanism. For MJCF fullinertia decode order M11,M22,M33,M12,M13,M23 and inertial frame convention; compiler diagonalization/diaginertia and any boundinertia adjustment are read back. inertiafromgeom auto uses geom inference only without inertial element; true overrides explicit fields.

Agent: Choose evidence-supported parameter/constraint mappings; retain physics assumptions explicitly.

Inputs: Checked mapping, geometry transforms, physical properties and requested contact/actuator settings.

Output/check: Editable MJCF/spec source with source-to-body/joint/geom map. Validation: Body tree alone does not close a loop; soft equality behavior and constrained freedoms require their own criterion.

Dependencies: Selected XML/spec API; fullinertia/diaginertia and compiler settings checked against actual version.

Resources: Local XML generation low compute; compilation/mesh cost tracked separately; reasoning effort rises for closures.

Source-supported tools: MuJoCo MJCF XML and mjSpec API. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst).

### 173. Compile read back and check model meaning (DOM-11-A03)

Original action: [Compile read back and check model meaning](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-11 — Author native MJCF simulation model.

Implementation proposal: Proposal: model verifier reports effective defaults, kinematics, inertials and named fixture outcomes.

Software: Compile with MjModel.from_xml_path or supported spec route; compare effective body/joint/inertial/geom data; run bounded closure/contact fixtures only when authorized.

Agent: Separate reviewer checks role mapping and physical assumptions against source.

Inputs: Saved source/assets, expected body/joint/physical records and named future fixtures.

Output/check: Compile/readback, pose/property and closure/contact reports. Validation: Valid compile is distinct from matched physical model; equality residual/force behavior uses sourced criteria. Any compiler-adjusted inertia is a changed model value with explicit provenance; it cannot satisfy a source-property criterion merely by becoming numerically admissible.

Dependencies: Pinned compiler and proposed source-to-compiled checker.

Resources: Local compile/FK before dynamic fixtures; runtime cost depends on geoms/contacts/constraints; remote/manual review separate.

Source-supported tools: MuJoCo MJCF XML and mjSpec API. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst).

### 174. Replace mapped role-specific geometry (DOM-32-A02)

Original action: [Replace mapped role-specific geometry](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-32 — Map CAD link geometry to MJCF body tree.

Implementation proposal: Proposal: geometry patcher accepts body/role/asset transforms and emits changed fields plus preservation diff.

Software: Replace/add only mapped geoms; preserve body/joint/actuator/sensor definitions; control inertia inference and contact roles explicitly.

Agent: Review intended replacement and any geometry-driven physical effects.

Inputs: Checked body map, source-linked mesh/primitive assets, role settings and preservation policy.

Output/check: New XML/assets with geom-to-source and transform map; explicit physics-effect report. Validation: Automatic inertia recomputation cannot silently change preserved physical intent; collider replacement receives contact checks.

Dependencies: DOM-12/13 assets; selected MJCF API and immutable seed snapshot.

Resources: Local asset generation cost follows selected geometry; remote semantics/manual mass data separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst).

### 175. Compare preserved semantics and effective geometry (DOM-32-A03)

Original action: [Compare preserved semantics and effective geometry](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-32 — Map CAD link geometry to MJCF body tree.

Implementation proposal: Proposal: replacement verifier emits preserved-field diff, world-geometry residuals and affected contact results.

Software: Reopen/compile; compare preserved declarations and mapped kinematics, inertials, collision roles and effective surfaces including compiler mesh offsets/rotation.

Agent: Separate reviewer checks body/part correspondence and intended role.

Inputs: Saved candidate, seed snapshot, independent interface/pose controls.

Output/check: Source-to-result graph/actuator/sensor/physics diff and effective placed-geometry report. Validation: Raw mesh vertices or geom_pos alone cannot substitute full compiled mesh→geom→body transform comparison.

Dependencies: DOM-10/11 readback and proposed seed-diff checker.

Resources: Local compiled/FK checks before selected contact fixtures; large mesh comparisons bounded by required regions.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst).

### 176. Author static world geoms and source sidecar (DOM-34-A02)

Original action: [Author static world geoms and source sidecar](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-34 — Author static MuJoCo environment from BIM mesh.

Implementation proposal: Proposal: static-world writer emits XML/assets with source-element and approximation mapping.

Software: Create static worldbody geometry with separate visual/collision roles; retain per-piece transforms and selected material appearance/contact meaning.

Agent: Review source coverage and static designation.

Inputs: Checked mesh/collider map, world frame, role/contact settings and assets.

Output/check: MJCF world geoms plus IFC-element/asset sidecar and loss map. Validation: Environment output creates no robot or invented inertial body requirements; IFC semantics stay source-linked.

Dependencies: Pinned MJCF XML/spec API; DOM-13/16 geometry contracts.

Resources: Local creation low compute relative to building mesh size; memory/assets scale with elements/hulls.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst).

### 177. Validate static coverage and working passages (DOM-34-A03)

Original action: [Validate static coverage and working passages](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-34 — Author static MuJoCo environment from BIM mesh.

Implementation proposal: Proposal: verifier emits per-element geometry/identity and per-contact readiness.

Software: Compile/reopen; compare element coverage, effective world geometry and static roles; test protected contact/no-contact configurations.

Agent: Separate reviewer verifies source element identity and preserved required openings.

Inputs: Saved environment, IFC-derived controls and named contact/passage fixtures.

Output/check: Compile/readback, coverage/placement and contact approximation results. Validation: A geometric passage check and IFC opening relationship check remain distinct; static scene carries only declared derivative semantics.

Dependencies: Proposed BIM-to-world verifier and target fixture runner.

Resources: Local selected controls before detailed world contacts; remote review and manual survey evidence separate.

Source-supported tools: documented adapter or explicit authoring step. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst).

### 178. Parse compile and serialize editable MJCF (DOM-10-A02)

Original action: [Parse compile and serialize editable MJCF](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-10 — URDF import and MJCF conversion.

Implementation proposal: Proposal: converter emits source/spec/compiled/saved stage receipts and generated flattened XML with mapping.

Software: Use the selected binding's documented MjSpec.from_file/from_string parse into mjSpec; compile via supported spec.compile/mj_compile route; serialize with evidenced mj_saveXML/mj_saveXMLString or mj_encode XML route. Record compiler/savecompiled: true saves compilation-made canonical values; false saves parsed/authored spec values. Passing compiled model to mj_encode copies model modifications into spec. Pin exact callable/language/version before execution.

Agent: Review dropped/defaulted fields and explicit new simulator parameters.

Inputs: Source package and checked import settings; output path and asset policy.

Output/check: Editable MJCF XML and assets, compiled receipt and field/default/loss map. Validation: Generated XML expands/applies defaults; source text identity and original hierarchy remain in source/mapping ledger. Save report identifies expanded/omitted include/replicate/attach/flexcomp/actuator shortcut constructs and comments, plus attached compiler-setting conflicts.

Dependencies: Pinned MuJoCo spec/compile/XML-save capability; compiled MJB alone cannot satisfy MJCF output.

Resources: Local compile cost follows bodies/geoms/meshes; no dynamics run implied; remote exception interpretation separate.

Source-supported tools: MuJoCo URDF parser/compiler; mjSpec API. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst).

### 179. Reopen MJCF and compare supported semantics (DOM-10-A03)

Original action: [Reopen MJCF and compare supported semantics](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-10 — URDF import and MJCF conversion.

Implementation proposal: Proposal: conversion verifier emits per-field equivalence, fusion mapping and consumer readiness.

Software: Reopen/compile saved XML; compare mapped body/joint poses, ranges, assets and inertials; inspect effective actuators/contact fields.

Agent: Separate reviewer evaluates source-supported identity and any extra modeling choices.

Inputs: Saved MJCF/assets, source URDF and mapped reference/moved states.

Output/check: Recompile/readback report with joint, geometry, inertia and identity comparison. Validation: Compile success cannot replace editable output, source equivalence or physical data.

Dependencies: Source-target checker and selected MuJoCo reader.

Resources: Local FK/field comparisons precede any requested contact fixture; manual semantics separate.

Source-supported tools: MuJoCo URDF parser/compiler; mjSpec API. Original evidence: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst), [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst).

### 180. Author IFC elements placements and relationships (DOM-15-A02)

Original action: [Author IFC elements placements and relationships](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-15 — Author semantic IFC building.

Implementation proposal: Proposal: IFC author emits element/representation/relationship identities plus source/placement ledger.

Software: Use supported project.create_file, root.create_entity, unit.assign_unit, context and aggregate/spatial APIs; create/assign geometry and placements. Create/represent/place opening first, then feature.add_feature to host; filling uses its own supported relation.

Agent: Review source-supported classes, containment, materials and opening/filling meaning.

Inputs: Checked brief plan, sourced geometry/material/property values and placement chains.

Output/check: IFC project/elements with GlobalId/source map, geometry and semantic relationships. Validation: Geometric hole and semantic opening are separate records; avoid duplicate transform/unit application.

Dependencies: Selected IfcOpenShell schema/API version; point04 opening sequence and point05 unit/CRS contract.

Resources: Local entity work scales with elements/relations; geometry evaluation dominates complex solids; remote semantics separate.

Source-supported tools: Bonsai; IfcOpenShell API. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html).

### 181. Validate semantic graph and evaluated geometry (DOM-15-A03)

Original action: [Validate semantic graph and evaluated geometry](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-15 — Author semantic IFC building.

Implementation proposal: Proposal: IFC verifier emits per-element semantic, geometry and delivery-requirement results.

Software: Reopen IFC; run supported validation and requested IDS checks; inspect uniqueness, hierarchy/containment, placements, void/fill and properties; measure geometry.

Agent: Separate reviewer checks element meaning, source trace and relationship interpretation.

Inputs: Saved IFC, source requirements and independent geometry/property controls.

Output/check: Schema/IDS when supplied, semantic graph and geometry readback reports. Validation: Valid schema and plausible rendering cannot substitute required property or opening-host evidence.

Dependencies: Pinned validator/geometry engine and proposed semantic checker.

Resources: Local schema checks precede selected-element geometry; whole-building processing follows required coverage, review effort separate.

Source-supported tools: Bonsai; IfcOpenShell API. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html).

### 182. Extract and retain native kernel shapes (DOM-27-A02)

Original action: [Extract and retain native kernel shapes](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-27 — Extract IFC geometry as OpenCASCADE B-rep.

Implementation proposal: Proposal: B-rep adapter emits typed shapes, source maps and evaluation/healing settings.

Software: Use supported create_shape/iterator non-triangulated/OpenCASCADE route; preserve returned shape ownership/lifetime and serialize using evidenced backend path. Source API documents use-python-opencascade and non-triangulated settings; inspect actual build's PythonOCC availability and return type. Iterator whole-element scope differs from single representation/item/profile create_shape.

Agent: Review exceptions, healing or altered representation report.

Inputs: Checked extraction settings and selected IFC representations.

Output/check: Kernel B-reps with per-element source/placement map and type/face metadata. Validation: A triangle payload cannot be labelled B-rep; validity and analytic-face claims query actual output.

Dependencies: Exact selected IfcOpenShell/build/shape binding and serializer.

Resources: Local kernel memory/time follows representation complexity; bulk work after selected fixtures.

Source-supported tools: IfcOpenShell geom.create_shape/iterator using OpenCASCADE kernel. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html).

### 183. Validate shape class and source feature agreement (DOM-27-A03)

Original action: [Validate shape class and source feature agreement](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-27 — Extract IFC geometry as OpenCASCADE B-rep.

Implementation proposal: Proposal: shape verifier emits per-element class, metric, source and downstream-readiness records.

Software: Query shape validity, solid/shell status, face types, bounds and applicable volume; compare openings and transforms.

Agent: Separate reviewer checks source-element meaning and faceted/analytic classification.

Inputs: Saved/reopened shapes, source IFC and independent feature checks.

Output/check: Validity, topology/face-type, dimensional/placement and identity reports. Validation: Valid shell differs from closed solid; equal bounds/volume cannot substitute interface checks.

Dependencies: Selected kernel checker and proposed IFC shape comparator.

Resources: Local kernel checks first; detailed comparisons follow selected features, remote review separate.

Source-supported tools: IfcOpenShell geom.create_shape/iterator using OpenCASCADE kernel. Original evidence: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html).

### 184. Produce linked drawings and exchange geometry (DOM-25-A02)

Original action: [Produce linked drawings and exchange geometry](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-25 — Create fabrication package.

Implementation proposal: Proposal: package producer maps native feature IDs to views/dimensions and emits files plus lost-annotation/representation ledger.

Software: OCS supported native drawing/export remains baseline with exact runtime capability discovery. Optional separately scoped FreeCAD candidate: TechDrawGui.exportPageAsSvg(DrawPageObject,FilePath) requires active GUI and an existing populated DrawPage; source says hatch patterns omitted and text placement/size may be inaccurate. This source proves SVG export only; PDF/DXF/STEP paths retain their own capability requirements and point03 representation checks.

Agent: Review view/section selection, datum references and source dimension interpretation.

Inputs: Checked plan, native parts, source annotations/materials and selected exporters.

Output/check: Drawings and requested STEP/DXF/PDF or other supported files plus part/revision/source manifest. Validation: Faceted mesh STEP cannot silently satisfy required analytic-solid exchange; exported geometry may need companion tolerance drawing.

Dependencies: Actual OCS exporter evidence; optional inspected TechDraw SVG API with active GUI/DrawPage prerequisites; page construction/dimension association is separate supported UI/API work.

Resources: Local drawing/solid export cost follows parts/views/faces; PDF rendering and manual annotation review separately recorded.

Source-supported tools: Native CAD drawing/workbench; STEP/DXF/PDF exporters. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 185. Reopen recipient artifacts and audit feature coverage (DOM-25-A03)

Original action: [Reopen recipient artifacts and audit feature coverage](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json). Operations: DOM-25 — Create fabrication package.

Implementation proposal: Proposal: fabrication verifier emits per-feature requirement coverage, format losses and readback results.

Software: Reopen using designated reader; query scale/holes/profiles/shape class and inspect drawing dimensions/datums/materials against model revision.

Agent: Separate reviewer verifies annotation-feature meaning and required process coverage.

Inputs: Saved files/manifest, source model/requirements and chosen receiving reader.

Output/check: Revision, dimension/material/tolerance coverage and recipient readback report. Validation: Successful export does not establish manufacturability; required process evidence and recipient compatibility have their own results.

Dependencies: Selected recipient/reader and proposed coverage checker.

Resources: Local file/feature checks first; graphics/document review and recipient manual effort separate.

Source-supported tools: Native CAD drawing/workbench; STEP/DXF/PDF exporters. Original evidence: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md), [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md).

### 186. Author constrained source and materialize geometry (REC-14-A02)

Original action: [Author constrained source and materialize geometry](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-14 — Remodel segmented scan evidence as parametric CAD.

Implementation proposal: Proposal: editable remodel composer emits three artifacts plus dependency and source mapping.

Software: Use evidenced native sketch/feature backend and retained source program; generate actual shape and query output types.

Agent: Review stable feature references and scan-to-feature correspondence; diagnose missing backend output.

Inputs: Feature plan; supported backend; source parameter values; target revision/output scope.

Output/check: Constrained-sketch, parametric-source and actual cad-solid candidates with linked feature IDs. Validation: CadQuery/source+solid without native constrained sketch remains partial; OCS native body without feature/source outputs remains partial.

Dependencies: FreeCAD documented sketch/Part and source route, or separately evidenced compatible adapters; OCS route typed by actual capability.

Resources: Local solver/kernel cost follows feature graph; remote/manual modeling interpretation separate.

Source-supported tools: Open3D feature fits, OpenCADStudio OCS skill, parametric CAD backend. Original evidence: [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html).

### 187. Verify editability, interfaces and fixed scan comparisons (REC-14-A03)

Original action: [Verify editability, interfaces and fixed scan comparisons](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-14 — Remodel segmented scan evidence as parametric CAD.

Implementation proposal: Proposal: editable-output verifier emits each representation's checks and cross-artifact lineage.

Software: Check constraints/source persistence, actual solid validity and dimensions; compare fixed scan regions; test supplied variant when in scope.

Agent: Independent reviewer checks feature meaning, hidden assumptions and parameter dependency behavior.

Inputs: Three candidate artifacts; immutable registered scan/controls; required interface criteria; supplied variant if requested.

Output/check: Validated constrained-sketch, parametric-source and cad-solid with regional residual and saved-readback reports. Validation: All required outputs exist and retain intended editability; low scan error cannot replace interface/source checks.

Dependencies: CAD-13 and REC-08/16 comparison contracts; actual independent reader where available.

Resources: Local regeneration/readback/region distances follow features/samples; remote semantics and manual corrections separate.

Source-supported tools: Open3D feature fits, OpenCADStudio OCS skill, parametric CAD backend. Original evidence: [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html).

### 188. Estimate sparse cameras and points with retained hypotheses (REC-03-A02)

Original action: [Estimate sparse cameras and points with retained hypotheses](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-03 — Estimate camera poses and sparse structure from overlapping photos.

Implementation proposal: Proposal: sparse runner emits database/model/settings plus registered/unregistered-image and component reports.

Software: Use documented feature_extractor, chosen matcher and mapper or selected equivalent; preserve raw components and bundle-adjustment calibration policy.

Agent: Review correspondence ambiguity, disconnected components and implausible camera paths.

Inputs: Checked dataset/configuration and any sourced calibration priors.

Output/check: Feature/match database, camera poses/intrinsics, sparse points and reconstruction components. Store COLMAP image poses as world→camera Hamilton (qw,qx,qy,qz) plus translation and preserve source image/camera IDs. Validation: Camera database/model readback matches image dimensions/model parameters; disconnected components keep independent frames.

Dependencies: Pinned sparse backend/build; exact CPU/GPU feature/matching options inspected.

Resources: Local CPU-capable sparse route where supported; cost follows images/resolution/features/pairs; GPU backend conditional.

Source-supported tools: COLMAP/pycolmap, AliceVision/Meshroom, OpenMVG. Original evidence: [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst), [https://alicevision.org/](https://alicevision.org/), [https://github.com/openMVG/openMVG](https://github.com/openMVG/openMVG).

### 189. Validate camera coverage and scale evidence (REC-03-A03)

Original action: [Validate camera coverage and scale evidence](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-03 — Estimate camera poses and sparse structure from overlapping photos.

Implementation proposal: Proposal: sparse verifier emits per-camera/component readiness, control residuals and explicit arbitrary/metric scale state.

Software: Inspect registered-view/component coverage, residual distribution and poses; apply sourced similarity/scale only with sufficient controls and reserve independent checks.

Agent: Separate reviewer checks physical feature correspondence and repeated/symmetric alternatives.

Inputs: Sparse candidates, reserved views/controls and optional scale/datum evidence.

Output/check: Checked sparse model, normalized pose convention, control/coverage report and scale transform if supported. Validation: Calibration target units alone do not scale an unrelated photo object; two scale lengths do not automatically determine full spatial datum.

Dependencies: Point05 pose/registration validation and sparse output reader.

Resources: Local residual/control checks before dense work; remote semantic review/manual measurement separate.

Source-supported tools: COLMAP/pycolmap, AliceVision/Meshroom, OpenMVG. Original evidence: [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst), [https://alicevision.org/](https://alicevision.org/), [https://github.com/openMVG/openMVG](https://github.com/openMVG/openMVG).

### 190. Apply scoped edit and read actual resulting geometry (REC-16-A02)

Original action: [Apply scoped edit and read actual resulting geometry](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-16 — Iterate CAD edits against registered evidence.

Implementation proposal: Proposal: revision edit executor emits actual changed geometry and dependency receipt.

Software: Execute bounded supported edit; regenerate if source-driven; query actual shape and changed handles.

Agent: Diagnose feature dependency or selector failures from actual state.

Inputs: Baseline receipt; explicit edit parameters; target revision; supported editor.

Output/check: New CAD/source revision and readback/operation receipt; prior revision preserved. Validation: Successful command requires expected valid geometry and preserved intended interfaces.

Dependencies: OCS actual operation schema or selected source backend; output capability checks from point03.

Resources: Local regeneration cost follows feature graph; remote/manual diagnosis separate.

Source-supported tools: OCS revision-bound edit/readback, Open3D distance queries, CloudCompare distance command. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode).

### 191. Compare fixed evidence and publish revision deltas (REC-16-A03)

Original action: [Compare fixed evidence and publish revision deltas](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-16 — Iterate CAD edits against registered evidence.

Implementation proposal: Proposal: revision comparator emits comparable deltas, invariants and failed dependencies.

Software: Measure both models against same evidence; verify functional dimensions and actual saved output; classify changed/unchanged features.

Agent: Independent reviewer checks source meaning and whether fit improvement conceals wrong nominal/functional change.

Inputs: Both actual revisions; same scan/transform/regions; independent dimensions; fixed statistic rules.

Output/check: Per-region/feature delta report, affected invariants, saved-readback evidence and next bounded action. Validation: Geometry fit reduction cannot pass an interface violation; refitting alignment creates a separately labelled branch.

Dependencies: REC-08 comparison, CAD-13 read-only verification and source control ledger.

Resources: Local two-revision queries use fixed relevant samples; remote semantic review/manual follow-up separate.

Source-supported tools: OCS revision-bound edit/readback, Open3D distance queries, CloudCompare distance command. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode).

### 192. Estimate intrinsic and distortion parameters (REC-01-A02)

Original action: [Estimate intrinsic and distortion parameters](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-01 — Calibrate camera intrinsics and distortion.

Implementation proposal: Proposal: intrinsic fitter emits candidates, residual distribution and declared observability findings.

Software: Run supported calibrateCamera; retain per-image/per-region residuals and available uncertainty diagnostics.

Agent: Compare model adequacy and outlier causes without excluding points solely to improve aggregate score.

Inputs: Fit observations; model/options; actual image size; target units.

Output/check: Intrinsic matrix, distortion model/coefficients, fit poses and residual diagnostics. Validation: Finite parameters and fit consistency accompany coverage/conditioning checks; unavailable diagnostics remain unresolved.

Dependencies: Version-pinned OpenCV calibration interface; extra diagnostics only when actually available.

Resources: Local nonlinear fit follows image/point/model size; no inferred GPU requirement; remote model interpretation separate.

Source-supported tools: OpenCV calibrateCamera, checkerboard or Charuco target. Original evidence: [https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html).

### 193. Check held-out distortion behavior and publish intrinsics (REC-01-A03)

Original action: [Check held-out distortion behavior and publish intrinsics](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-01 — Calibrate camera intrinsics and distortion.

Implementation proposal: Proposal: calibration validator emits region/state validity and derivative metadata.

Software: Freeze intrinsics/distortion. Use externally known held-out target pose, or estimate that pose from designated target points and evaluate a separate reserved point set. Project reserved controls and inspect regional residuals/straight edges; retain new camera matrix and valid domain for derivatives.

Agent: Independent reviewer checks systematic distortion and target association.

Inputs: Calibration candidates; held-out target images/controls; image-state record. Each held-out target view also needs an externally known pose or a designated pose-fitting point subset disjoint from evaluated points.

Output/check: Checked calibration with scope, residual maps and optional undistorted derivative/mapping. Validation: Intrinsics remain tied to camera state and actual pixel grid; undistorted images use their recorded new matrix/distortion convention. Record shared target/calibration uncertainty and pose-fitting dependence; pose-fit points cannot count as independent validation points.

Dependencies: OpenCV project/undistort APIs and point04 derivative mapping.

Resources: Local projection/remap cost follows checks/pixels; remote review/manual recapture effort distinct.

Source-supported tools: OpenCV calibrateCamera, checkerboard or Charuco target. Original evidence: [https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html).

### 194. Estimate or import sequence poses and projected samples (REC-05-A02)

Original action: [Estimate or import sequence poses and projected samples](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-05 — Register RGB and depth frames and estimate sequence poses.

Implementation proposal: Proposal: pose adapter emits pairwise/source-to-world transforms, sample IDs and failed intervals.

Software: Use supported RGB-D odometry or imported sensor/survey poses; project valid depth using matching intrinsics and preserve transform direction at each boundary. compute_rgbd_odometry returns success, pairwise 4x4 motion and 6x6 information; verify selected adapter direction before composing trajectory.

Agent: Review motion/overlap failures and physical correspondence.

Inputs: Calibrated frame pairs, pose initialization/trajectory and odometry settings.

Output/check: Per-frame poses, relative transforms, projected samples and success/overlap diagnostics. Validation: A successful local fit does not remove global drift; missing intervals remain explicit.

Dependencies: Pinned Open3D odometry direction and sensor pose convention; exact API checked before execution.

Resources: Local bounded frame pairs first; compute follows resolution/overlap/pyramid settings; GPU only actual selected backend.

Source-supported tools: Open3D RGB-D odometry, sensor SDK calibration, Open3D camera intrinsics/trajectory. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html).

### 195. Validate trajectory and metric depth independently (REC-05-A03)

Original action: [Validate trajectory and metric depth independently](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-05 — Register RGB and depth frames and estimate sequence poses.

Implementation proposal: Proposal: trajectory verifier emits per-segment control/drift and output-readiness records.

Software: Read back trajectory/points; test transform inverses, range bias, loop closure and distributed controls.

Agent: Separate reviewer checks physical sample identity, dynamic exclusions and plausible path alternatives.

Inputs: Saved poses/samples, withheld depth/length/position controls and loop evidence.

Output/check: Checked outputs with scale/frame, drift, coverage and control results. Validation: Sensor metric scale does not guarantee dimensional accuracy or drift-free trajectory.

Dependencies: Point05 frame/registration checker and proposed RGB-D verifier.

Resources: Local control tests precede fusion; remote review/manual target measurement separately recorded.

Source-supported tools: Open3D RGB-D odometry, sensor SDK calibration, Open3D camera intrinsics/trajectory. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html).

### 196. Integrate observations and extract explicit geometry (REC-06-A02)

Original action: [Integrate observations and extract explicit geometry](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-06 — Integrate calibrated RGB-D frames into point cloud or TSDF mesh.

Implementation proposal: Proposal: fusion runner emits both geometry types and frame-to-surface/support evidence or documented mapping limits.

Software: Use ScalableTSDFVolume integration and supported cloud/triangle extraction; retain exact grid/range/pose settings and filled/unobserved-region classification.

Agent: Review fusion artifacts at discontinuities and moving surfaces.

Inputs: Checked integration manifest and selected Open3D volume/backend.

Output/check: TSDF state or replay receipt, extracted cloud and mesh, observation/support metadata. Validation: Empty volume or cloud-only extraction leaves required outputs partial; interpolated closure remains inferred.

Dependencies: Actual pinned integration/extraction methods and storage/checkpoint behavior.

Resources: Local CPU-supported path where evidenced; cost follows pixels, frames, occupied voxels and extraction; GPU-specific path separate.

Source-supported tools: Open3D ScalableTSDFVolume, Open3D RGBDImage, Open3D marching-cubes extraction. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html).

### 197. Compare fusion candidates and independent controls (REC-06-A03)

Original action: [Compare fusion candidates and independent controls](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-06 — Integrate calibrated RGB-D frames into point cloud or TSDF mesh.

Implementation proposal: Proposal: verifier reports per-feature/control error, coverage and approximation changes across settings.

Software: Reopen outputs; compare independent controls and directed sample/surface residuals; inspect holes, double walls and protected features.

Agent: Separate reviewer checks observed/inferred regions and feature identity.

Inputs: Saved geometry, raw-frame projections, control set and bounded alternative voxel/settings results.

Output/check: Cloud/mesh metric, drift, coverage and source/readback report. Validation: Smaller voxel or lower fit residual does not automatically improve measured accuracy.

Dependencies: Point05 comparison and proposed fusion verifier.

Resources: Local regional checks before full dense comparisons; manual controls and remote review separate.

Source-supported tools: Open3D ScalableTSDFVolume, Open3D RGBDImage, Open3D marching-cubes extraction. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html).

### 198. Generate plane, cluster and cylinder candidates (REC-09-A02)

Original action: [Generate plane, cluster and cylinder candidates](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-09 — Segment point clouds and fit candidate primitive evidence.

Implementation proposal: Proposal: primitive-candidate adapter accepts immutable cloud/normal IDs, original-index mapping, model and typed settings; emits inlier IDs, raw coefficient vector, named parameter fields, source unit/frame, setting receipt, coverage and geometric residuals. Reject length/index mismatches, nonfinite/zero normals, empty support, invalid coefficient vectors and nonpositive radius before downstream use.

Software: Open3D segment_plane and cluster_dbscan supply plane/cluster candidates. Proposed PCL adapter configures SACSegmentationFromNormals<PointXYZ, Normal>, SACMODEL_CYLINDER, selected consensus method (tutorial uses RANSAC), optimization flag, normal-distance weight, iterations/probability, distance threshold, radius limits and any evidenced axis/angle constraint; segment(inliers, coefficients) supplies sampled cylinder candidates.

Agent: Assess whether cluster/plane corresponds to intended feature and whether coverage constrains parameters.

Inputs: Region manifest with original point IDs; plane/cluster settings or PCL cylinder model; point cloud plus corresponding normal cloud and normal-estimation neighborhood/index mapping; explicit cloud unit/frame, consensus controls and source-backed radius/axis constraints.

Output/check: Segmented point-cloud with original indices; plane/cluster candidates or cylinder inlier indices and seven coefficients: axis point x,y,z [0–2], axis direction x,y,z [3–5], radius [6]; fit residuals and coverage records. Validation: Check point-normal alignment, finite seven-value cylinder output, nonzero axis direction, positive radius and configured bounds. Independently measure sample-to-cylinder geometric residuals and axial/angular coverage; a threshold/bound-clipped candidate retains that state, and low residual alone cannot resolve radius or axis uncertainty.

Dependencies: Open3D APIs; PCL 1.15.1-dev API documentation and mutable master cylinder header supply source contracts. Pin and inspect the selected installed release/binding before executing the proposed adapter; preserve point-normal order after every mask/downsample.

Resources: Local point/normal inventory precedes fitting; normal-neighborhood search and consensus cost depend on selected point count, neighborhood size and bounded iteration/hypothesis counts. Start with source-linked region samples for candidate search, then check retained full/reserved samples. Record local memory/time separately from remote interpretation and manual surface labeling.

Source-supported tools: Open3D segment_plane, Open3D DBSCAN, CloudCompare scalar-field and primitive tools. Original evidence: [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html), [https://github.com/CloudCompare/CloudCompare](https://github.com/CloudCompare/CloudCompare).

### 199. Check sampling bias and publish primitive evidence (REC-09-A03)

Original action: [Check sampling bias and publish primitive evidence](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-09 — Segment point clouds and fit candidate primitive evidence.

Implementation proposal: Proposal: fit evidence checker emits parameter confidence basis and source-dependent limitations.

Software: Evaluate withheld distances and sensitivity to region/threshold/sampling; report unsupported parameter observability.

Agent: Independent reviewer checks primitive/feature identity and excluded regions.

Inputs: Candidates; held-out regions/controls; alternative sample/threshold reports.

Output/check: Point labels and measurement records with parameter source, support, residual distribution and readiness. Validation: Low residual on a narrow patch does not resolve unconstrained radius/axis/extent; required parameter checks remain unresolved.

Dependencies: Numerical sensitivity checker proposed; supported cloud distance queries.

Resources: Local limited sensitivity checks follow selected points; remote/manual feature review separate.

Source-supported tools: Open3D segment_plane, Open3D DBSCAN, CloudCompare scalar-field and primitive tools. Original evidence: [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html), [https://github.com/CloudCompare/CloudCompare](https://github.com/CloudCompare/CloudCompare).

### 200. Estimate route-specific CAD alignment candidates (REC-12-A02)

Original action: [Estimate route-specific CAD alignment candidates](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-12 — Register existing CAD to calibrated photographs or scan points.

Implementation proposal: Proposal: route registrar preserves native CAD and emits conditional pose/spatial records.

Software: Photo route uses REC-02; scan/mesh route uses REC-07/08 with documented sampling and transform direction.

Agent: Review alternate symmetry poses, occlusion, partial overlap and wrong physical revision.

Inputs: Route manifest; named photo correspondences or source/target sampled surfaces; controls.

Output/check: Photo CAD-to-camera pose candidates or scan-to-CAD spatial transform candidates with receipts. Validation: Rigid CAD alignment preserves geometry; scan route creates no camera parameters from absent observations.

Dependencies: OpenCV PnP or Open3D registration actual supported interface.

Resources: Local pose or surface work follows chosen route; remote/manual evidence selection recorded.

Source-supported tools: CAD tessellation with named 3D landmarks, OpenCV solvePnPRansac, Open3D global registration and ICP. Original evidence: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html).

### 201. Validate alignment and publish conditional outputs (REC-12-A03)

Original action: [Validate alignment and publish conditional outputs](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-12 — Register existing CAD to calibrated photographs or scan points.

Implementation proposal: Proposal: conditional registration exporter emits supported branch artifacts and unmet original output labels.

Software: Reproject photo checks or compare fixed scan regions; inspect source/target transforms and required interfaces.

Agent: Independent reviewer checks matched component/configuration and visible/occluded evidence.

Inputs: Alignment hypotheses; withheld landmarks/interfaces; fixed source revisions and criteria.

Output/check: Measurement-set with spatial registration/controls; photo branch also emits camera-solution. Scan-only branch records original camera-output mismatch explicitly. Validation: Original REC-12 output list is preserved as a finding; scan-only spatial records cannot satisfy a camera-consuming handoff.

Dependencies: REC-02/08 check reports; CAD-13 actual geometry queries.

Resources: Local selected-feature checks first; remote semantic review/manual metrology separate.

Source-supported tools: CAD tessellation with named 3D landmarks, OpenCV solvePnPRansac, Open3D global registration and ICP. Original evidence: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html), [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html).

### 202. Refine transform and retain correspondence evidence (REC-08-A02)

Original action: [Refine transform and retain correspondence evidence](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-08 — Refine registration and compare point-cloud surfaces.

Implementation proposal: Proposal: refinement adapter emits transform lineage, convergence and correspondence receipt.

Software: Run registration_icp or evidenced equivalent; record whether returned transform includes initialization; evaluate declared objective.

Agent: Diagnose local minima, unexpected scale/motion and concentration on one surface.

Inputs: Refinement specification and immutable cloud derivatives.

Output/check: Final source-to-target transform, iterations/status, correspondences and objective diagnostics. Validation: Check rigid/similarity properties and original-to-final mapping; reject silent double-application of initialization.

Dependencies: Selected Open3D/CloudCompare version and actual result semantics.

Resources: Local nearest-neighbor/iteration cost follows points and overlap; remote diagnosis and manual intervention distinct.

Source-supported tools: Open3D point-to-plane ICP, Open3D evaluate_registration, CloudCompare cloud-to-cloud distance. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode).

### 203. Measure independent and directional surface differences (REC-08-A03)

Original action: [Measure independent and directional surface differences](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-08 — Refine registration and compare point-cloud surfaces.

Implementation proposal: Proposal: comparison reporter emits direction-specific residual/coverage and control checks.

Software: Evaluate controls and declared source-to-target distances; compute reverse direction where needed; report regional maxima/quantiles/RMS and excluded counts.

Agent: Independent reviewer checks region correspondence and whether observed difference is sampling/occlusion or geometry.

Inputs: Final transform; original clouds; independent controls; fixed regions and distance/sampling rules.

Output/check: Regional distance maps, control residuals, non-overlap masks and transform readiness. Validation: Empty/low-overlap regions cannot pass through summary statistics; dense patches cannot conceal failing interfaces.

Dependencies: Open3D evaluation; documented CloudCompare distance commands; statistic helper proposed.

Resources: Local distance queries may dominate full-resolution work; bounded critical regions first; remote/manual interpretation separate.

Source-supported tools: Open3D point-to-plane ICP, Open3D evaluate_registration, CloudCompare cloud-to-cloud distance. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode).

### 204. Estimate analytic parameters and uncertainty (CAD-11-A02)

Original action: [Estimate analytic parameters and uncertainty](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: CAD-11 — Fit analytic features to scans or image-derived point clouds.

Implementation proposal: Proposal: analytic estimator accepts feature/model/support/normal/settings/criteria records and emits named parameters plus raw coefficients, inlier IDs, coverage, diagnostics and observable components. Cylinder-axis comparison uses a common sourced datum and explicit direction convention; extent/closure comes from separate feature evidence. Validate settings and decoded output before CAD consumption.

Software: Fit planes through evidenced Open3D support or cylinders through proposed PCL SACSegmentationFromNormals with SACMODEL_CYLINDER and matched points/normals. Preserve consensus method, optimization, normal weight, threshold, iteration/probability, radius limits and optional sourced axis/angle constraints. Independently evaluate geometric residuals, coverage, sensitivity and retained checks.

Agent: Compare primitive meanings and distinguish geometric fit from functional nominal dimension.

Inputs: Feature regions; Open3D plane or proposed PCL normal-assisted cylinder estimator; cloud/normal identities and membership mapping; source uncertainty and radius/axis constraints; held-out controls.

Output/check: Parameters, units/frame, support indices, residual distribution and sensitivity/uncertainty records. PCL cylinder output retains raw seven coefficients plus named axis point [0–2], direction [3–5] and radius [6]; finite extent and feature identity have separate evidence. Validation: Verify finite supported coefficients and axis/radius conventions, then compare independent feature distances and axial/angular coverage. Narrow arcs, short spans, normal errors, radius-bound clipping or biased samples leave affected parameters unresolved despite low residual; an infinite fitted cylinder supplies no finite end locations.

Dependencies: REC-09 cylinder adapter contract; PCL 1.15.1-dev API and mutable master header remain separate from selected installed-release evidence. Normal estimation and point-index mapping must be recorded. Additional primitive types require their own evidenced estimator contract.

Resources: Local point/normal checks and source-linked region sampling precede bounded optimization/consensus and sensitivity studies; cost depends on samples, normal neighborhoods and hypothesis limits. Precision checks use required retained samples/controls. Record remote interpretation and manual metrology separately.

Source-supported tools: point-cloud registration and segmentation, least-squares plane/cylinder/axis fits, FreeCAD/build123d. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [/home/leo/projects/architecture/research/README.md](/home/leo/projects/architecture/research/README.md).

### 205. Construct and validate supported CAD feature geometry (CAD-11-A03)

Original action: [Construct and validate supported CAD feature geometry](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: CAD-11 — Fit analytic features to scans or image-derived point clouds.

Implementation proposal: Proposal: fitted-feature builder emits native solid and feature-measurement/uncertainty ledger.

Software: Construct through supported CAD-10 operations; query shape class, required dimensions, held-out distances and saved output.

Agent: Independent reviewer checks observed/fitted/authored distinctions and hidden-feature meaning.

Inputs: Checked fitted parameters; explicit component/closure/hidden-feature decisions; CAD backend and criteria.

Output/check: Measurement-set plus actual valid cad-solid, source/fit mapping and native readback; incomplete surfaces retain typed intermediate state. Validation: A plane or open surface alone does not fulfill cad-solid; every solid-defining assumption is explicit and required features checked.

Dependencies: Point03 native construction/readback; actual backend capability and source/feature persistence.

Resources: Local CAD/kernel and regional distances follow surfaces/samples; remote semantics and manual missing data separate.

Source-supported tools: point-cloud registration and segmentation, least-squares plane/cylinder/axis fits, FreeCAD/build123d. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [/home/leo/projects/architecture/research/README.md](/home/leo/projects/architecture/research/README.md).

### 206. Cast rays and record hit alternatives (REC-13-A02)

Original action: [Cast rays and record hit alternatives](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-13 — Anchor a screen sketch to a 3D surface.

Implementation proposal: Proposal: ray-anchor adapter emits full ray/hit provenance, candidate ordering and validity states.

Software: Construct camera-consistent rays, including distortion treatment; query actual supported target geometry; retain misses and competing surfaces. Scene rays use world coordinates; Object rays use object coordinates with explicit transforms. Preserve evaluated geometry identity; face index -1 is an unavailable primitive reference, not a valid face.

Agent: Review occlusion and whether frontmost hit is the intended feature; preserve disconnected stroke segments.

Inputs: Anchor manifest; supported ray query; mapped stroke samples.

Output/check: Hit/miss/ambiguous records with world/local position, object/primitive ID, depth and source pixel. Validation: A hit is calculated from selected geometry; no-hit intervals are not bridged as measured surfaces.

Dependencies: Selected Blender ray adapter or evidenced CAD intersection interface; mesh derivative error explicit.

Resources: Local ray cost follows samples/scene acceleration; remote ambiguity review and manual selection separate.

Source-supported tools: Blender Scene.ray_cast, screen-to-camera ray projection, OpenCV projectPoints, OCS constrained sketch. Original evidence: [https://docs.blender.org/api/current/bpy.types.Scene.html](https://docs.blender.org/api/current/bpy.types.Scene.html), [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html).

### 207. Reproject anchors and publish measurement evidence (REC-13-A03)

Original action: [Reproject anchors and publish measurement evidence](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-13 — Anchor a screen sketch to a 3D surface.

Implementation proposal: Proposal: anchor verifier emits view residuals and explicit planar/nonplanar feature states.

Software: Reproject world anchors; inspect residuals, target membership and discontinuities; test required plane conditions separately.

Agent: Independent reviewer checks chosen surface, occlusion and trace meaning.

Inputs: Hit candidates; original stroke; selected interpretation; source criteria.

Output/check: Anchor measurement-set with pixel/object/primitive lineage, residuals and downstream sketch prerequisites. Validation: Anchors do not themselves become independent physical measurements or constrained sketch; remeshing invalidates unstable primitive references.

Dependencies: projectPoints or compatible selected-camera projection; point03 CAD-09 handoff when requested.

Resources: Local projection/plane checks bounded by anchors; separate remote semantic review/manual decisions.

Source-supported tools: Blender Scene.ray_cast, screen-to-camera ray projection, OpenCV projectPoints, OCS constrained sketch. Original evidence: [https://docs.blender.org/api/current/bpy.types.Scene.html](https://docs.blender.org/api/current/bpy.types.Scene.html), [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html).

### 208. Align evidence under fixed datum choices and measure differences (REC-15-A02)

Original action: [Align evidence under fixed datum choices and measure differences](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-15 — Reconcile scan surfaces with dimensioned drawings.

Implementation proposal: Proposal: paired-feature comparator emits direction/method/uncertainty-specific discrepancies.

Software: Apply supported registration; measure selected quantities and surfaces; reserve evaluation dimensions from alignment.

Agent: Review whether discrepancy stems from datum, interpretation, sampling, physical variation or drawing revision.

Inputs: Paired features; declared datum registration; fit/check regions; immutable source data.

Output/check: Transform receipt and per-feature nominal-versus-observed differences with coverage. Validation: Optimizer adjustment cannot silently remove a required nominal-versus-observed deviation.

Dependencies: REC-08 directional distance and independent control rules; source-linked measurement methods.

Resources: Local targeted measurements first; remote reasoning interprets source/context; manual metrology separate.

Source-supported tools: CAD drawing datums, Open3D/CloudCompare registration and distance map, OCS constrained sketch. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode).

### 209. Publish reconciliation choices and preserved conflicts (REC-15-A03)

Original action: [Publish reconciliation choices and preserved conflicts](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-15 — Reconcile scan surfaces with dimensioned drawings.

Implementation proposal: Proposal: reconciliation exporter emits source-separated values, reasons and downstream readiness.

Software: Validate units/feature links and publish complete discrepancy/choice records without mutating source CAD.

Agent: VLM selects evidence-supported association within current intent; independent reviewer checks nominal/observed meaning.

Inputs: Feature discrepancies; drawing/scan sources; stated target purpose; reviewer findings.

Output/check: Reconciled measurement-set with nominal, measured, fit and authored candidates, selected-use reason and open conflicts. Validation: Unresolved controlling choice blocks only dependent feature; source revision discrepancies remain visible.

Dependencies: Point01 evidence records and REC-14 downstream parameter map.

Resources: Local record checks small; remote/manual decision review recorded.

Source-supported tools: CAD drawing datums, Open3D/CloudCompare registration and distance map, OCS constrained sketch. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode).

### 210. Estimate supported scan-to-building transform (DOM-19-A02)

Original action: [Estimate supported scan-to-building transform](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: DOM-19 — Register scan to building frame.

Implementation proposal: Proposal: building registrar returns transform candidates and source/target sampling/normalization receipts.

Software: Use control alignment or REC-07/08; preserve actual IFC geometry and record any numerical local-origin shift.

Agent: Review symmetry, partial façade coverage, moving objects and source revision discrepancies.

Inputs: Frame manifest; source cloud and IFC reference geometry/controls; static overlap; fit/check roles.

Output/check: Source-scan-to-building transform candidates with control/surface receipts. Validation: Local numerical shift has recorded inverse; no CRS, floor elevation or camera pose is inferred from fit.

Dependencies: Open3D/CloudCompare supported registration; IFC geometry extraction adapter and its approximation limits.

Resources: Local coarse regions first; large-cloud memory/target tessellation explicit; remote/manual correspondence separate.

Source-supported tools: COLMAP/AliceVision; Open3D/CloudCompare; IFC geometry as reference. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 211. Validate controls and publish aligned derivative (DOM-19-A03)

Original action: [Validate controls and publish aligned derivative](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: DOM-19 — Register scan to building frame.

Implementation proposal: Proposal: building-registration publisher emits aligned cloud, transform chain and source/readback checks.

Software: Apply transform once to derivative; check held-out points/lengths, regions, units/vertical datum and inverse mapping.

Agent: Independent reviewer checks building/feature correspondence and observed-versus-design differences.

Inputs: Chosen transform; immutable source cloud; withheld controls/regions; IFC frame manifest.

Output/check: Registration-transform plus transformed point-cloud derivative with original-index/source mapping and check report. Validation: Outputs are exactly registration-transform and point-cloud; IFC semantics and raw scan remain preserved.

Dependencies: REC-08 metric protocol and actual cloud serializer; camera operations are separate scope.

Resources: Local transformed cloud cost follows points; required regions first; remote semantic/manual checks separate.

Source-supported tools: COLMAP/AliceVision; Open3D/CloudCompare; IFC geometry as reference. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md).

### 212. Project register and publish source-linked cloud candidate (DOM-21-A02)

Original action: [Project register and publish source-linked cloud candidate](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-21 — Depth frames to registered point cloud or mesh.

Implementation proposal: Proposal: depth-cloud composer emits actual cloud, source membership and removed/inferred-region ledger.

Software: Compose REC-05 projection/poses and supported cloud accumulation/fusion; optional REC-06 route retains its separate mesh output.

Agent: Review dynamic regions and filters affecting required features.

Inputs: Checked depth/control plan and compatible poses/settings.

Output/check: Registered point-cloud and point/frame/filter/transform lineage. Validation: Filtered points remain traceable; mesh generation is not required to fulfill this typed output.

Dependencies: Open3D or independently evidenced CloudCompare adapter; exact transform conventions.

Resources: Local bounded cloud first; memory follows retained samples/frames; remote region review separate.

Source-supported tools: Open3D; CloudCompare. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 213. Check registered cloud controls and source coverage (DOM-21-A03)

Original action: [Check registered cloud controls and source coverage](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-21 — Depth frames to registered point cloud or mesh.

Implementation proposal: Proposal: registered-cloud checker emits per-feature metric/coverage and lineage results.

Software: Compare known lengths/targets, local residuals, loop/drift and excluded regions; verify units/transform application.

Agent: Separate reviewer checks physical correspondence and coverage for target use.

Inputs: Saved cloud, independent measurements and source frame/pose receipts.

Output/check: Control/drift/coverage report and registered point-cloud. Validation: Sensor units or plausible bounds cannot replace independent dimensional checks.

Dependencies: Point05 cloud comparator and proposed domain verifier.

Resources: Local control queries before dense analysis; remote/manual evidence review separate.

Source-supported tools: Open3D; CloudCompare. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 214. Reconstruct surface and retain every cleanup derivative (DOM-29-A02)

Original action: [Reconstruct surface and retain every cleanup derivative](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-29 — Point cloud to surface mesh.

Implementation proposal: Proposal: surface adapter emits raw mesh plus independent cleanup derivatives and change/support ledger.

Software: Open3D create_from_point_cloud_poisson takes an oriented point cloud and returns mesh plus density; create_from_point_cloud_ball_pivoting takes oriented cloud and length-unit radii. simplify_quadric_decimation targets triangle count with stated maximum_error/boundary_weight; retain original mesh and measure actual feature deviation.

Agent: Review extrapolated/filled regions and required small-feature loss.

Inputs: Checked point/normal plan and selected method/settings.

Output/check: Raw reconstructed mesh, optional cleaned/decimated variants and point/region source map. Validation: Closed-looking Poisson surface can include inferred empty-space closure; triangle target is not error guarantee.

Dependencies: Actual Open3D method/version and prerequisites; decimation capability discovery.

Resources: Cost follows points, octree/grid/resolution or pivot neighborhoods and triangles; bounded detail first.

Source-supported tools: Open3D surface reconstruction; CloudCompare mesh reconstruction; Blender mesh cleanup. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 215. Compare surface and protected features to source (DOM-29-A03)

Original action: [Compare surface and protected features to source](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-29 — Point cloud to surface mesh.

Implementation proposal: Proposal: mesh checker emits per-feature before/after deviation, topology/coverage and downstream-readiness results.

Software: Compare cloud→mesh and mesh→cloud with sampling/direction reported; query holes/components/normals and required passages; reproject to original captures when available.

Agent: Separate reviewer checks source feature meaning and inferred-region status.

Inputs: Saved raw/final mesh, source cloud/captures and independent controls.

Output/check: Directed residual, coverage, topology and feature-readback reports. Validation: Bounds/volume and low one-way residual cannot pass overfilled gaps or lost thin features.

Dependencies: Point05 geometry comparator and proposed mesh verifier.

Resources: Local selected-feature checks precede whole-surface distances; remote image review and manual metrology separate.

Source-supported tools: Open3D surface reconstruction; CloudCompare mesh reconstruction; Blender mesh cleanup. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 216. Generate coarse alignment hypotheses (REC-07-A02)

Original action: [Generate coarse alignment hypotheses](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-07 — Estimate coarse transform between point clouds.

Implementation proposal: Proposal: coarse registrar outputs hypotheses and exact source/target correspondences.

Software: Compute documented FPFH and RANSAC candidates or explicit target alignment; rigid default and similarity adapter distinguished.

Agent: Review symmetric/repeated matches and coverage; keep plausible alternatives.

Inputs: Manifest; coarse samples/normals; feature or landmark settings.

Output/check: Transform candidates, correspondence/inlier records and coarse fit diagnostics. Validation: Check transform rotation/scale/handedness and spatial distribution of supporting matches.

Dependencies: Open3D global registration/CloudCompare selected interface; similarity estimator requires evidenced capability.

Resources: Local feature/matching cost follows coarse points and candidate pairs; remote selection review separate.

Source-supported tools: Open3D FPFH, Open3D RANSAC global registration, CloudCompare alignment. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html).

### 217. Test withheld controls and publish initialization (REC-07-A03)

Original action: [Test withheld controls and publish initialization](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-07 — Estimate coarse transform between point clouds.

Implementation proposal: Proposal: coarse-check report emits control residuals and permitted downstream refinement state.

Software: Transform controls, assess regional alignment/non-overlap and test transform inverse.

Agent: Independent reviewer checks landmark/region identity and symmetry choice.

Inputs: Hypotheses; independent controls; intended overlap and feature criteria.

Output/check: Source-to-target transform/check records and alternatives with REC-08 readiness. Validation: Low matching error cannot pass a wrong symmetry pose that fails controls.

Dependencies: Open3D evaluation and source-independent metrology where supplied.

Resources: Local control checks precede full clouds; remote/full-context review and manual controls separate.

Source-supported tools: Open3D FPFH, Open3D RANSAC global registration, CloudCompare alignment. Original evidence: [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html).

### 218. Author parametric source and actual feature geometry (DOM-23-A02)

Original action: [Author parametric source and actual feature geometry](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: DOM-23 — Scan or mesh to parametric CAD remodeling.

Implementation proposal: Proposal: remodeling composer emits parameter/source dependency graph and actual CAD output.

Software: Reuse CAD11/REC14 checked evidence; construct through supported source/feature backend and query actual solid.

Agent: Choose feature sequence and stable parameter references; inspect hidden-feature assumptions against intent.

Inputs: Complete route manifest; target brief; fit/measurement evidence; supported parametric backend.

Output/check: Parametric source and actual solid candidates with feature/source mapping and generation receipt. Validation: Both required output representations exist; arbitrary mesh wrapper is not a parametric feature family.

Dependencies: Point03 DOM40/CAD10 supported source and geometry; OCS native body alone does not fulfill parametric-source.

Resources: Local fitting/kernel work follows selected features; remote/manual feature interpretation separate.

Source-supported tools: Open3D/CloudCompare measurement; OCS baseline; FreeCAD/OCCT solid modeling. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 219. Validate functional interfaces and saved parametric output (DOM-23-A03)

Original action: [Validate functional interfaces and saved parametric output](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: DOM-23 — Scan or mesh to parametric CAD remodeling.

Implementation proposal: Proposal: remodel verifier emits output-specific editability/geometry/source reports.

Software: Check solid validity and required interfaces; compare fixed held-out samples; reopen/rebuild from retained source and test supplied variant if requested.

Agent: Independent reviewer checks nominal/observed interpretation and hidden geometry assumptions.

Inputs: Generated source/solid; original observations/controls; target interface criteria; fixed comparison setup.

Output/check: Checked source/solid with held-out regional distances, interface measurements and saved/rebuild receipts. Validation: Appearance agreement or aggregate fit cannot pass a failing functional interface; source reproduces intended geometry.

Dependencies: CAD13 and REC16 fixed-evidence checks; actual backend persistence demonstrated in future cases.

Resources: Local required-feature checks first; large distance comparisons bounded; remote semantic/manual metrology separate.

Source-supported tools: Open3D/CloudCompare measurement; OCS baseline; FreeCAD/OCCT solid modeling. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md).

### 220. Compose intrinsic calibration and per-image pose solutions (CAD-02B-A02)

Original action: [Compose intrinsic calibration and per-image pose solutions](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: CAD-02B — Calibrate camera poses from photographs and known controls.

Implementation proposal: Proposal: camera-solution composer links versioned calibration and pose receipts without rerunning valid stages.

Software: Execute or reuse REC-01 then REC-02; retain object-to-camera transforms and explicit inverses for consumers.

Agent: Review alternate poses and control association; reject silent calibration changes.

Inputs: Manifest; REC-01 calibration or compatible source receipt; known 3D/image correspondences.

Output/check: Per-camera intrinsic/distortion and per-image pose candidates with subaction receipts. Validation: Each pose uses matching image coordinates/intrinsics; source length units determine translation scale.

Dependencies: REC-01 and REC-02 supported OpenCV paths; actual version/options recorded.

Resources: Local fit cost follows images/points; remote reasoning reserved for ambiguous hypotheses.

Source-supported tools: OpenCV findChessboardCorners, OpenCV calibrateCamera, OpenCV solvePnP. Original evidence: [https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html), [https://docs.opencv.org/5.0/main_modules/calib.html](https://docs.opencv.org/5.0/main_modules/calib.html).

### 221. Validate and publish camera solution (CAD-02B-A03)

Original action: [Validate and publish camera solution](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: CAD-02B — Calibrate camera poses from photographs and known controls.

Implementation proposal: Proposal: camera package checker emits per-image/control readiness for named consumers.

Software: Project check points, verify positive depth where required and transform/inverse consistency.

Agent: Separate reviewer checks point identity, camera convention and plausible alternate poses.

Inputs: Pose/calibration candidates; withheld controls; target feature criteria.

Output/check: Camera-solution including camera model, image mapping, pose direction and check results. Validation: Camera model/resolution and independent evidence match intended alignment use.

Dependencies: REC-01/REC-02 check contracts and project source ledger.

Resources: Local projections are bounded by checks; remote/full-view review and manual acquisition separate.

Source-supported tools: OpenCV findChessboardCorners, OpenCV calibrateCamera, OpenCV solvePnP. Original evidence: [https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html), [https://docs.opencv.org/5.0/main_modules/calib.html](https://docs.opencv.org/5.0/main_modules/calib.html).

### 222. Estimate object-to-camera pose candidates (REC-02-A02)

Original action: [Estimate object-to-camera pose candidates](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-02 — Solve camera pose from known 3D-to-2D correspondences.

Implementation proposal: Proposal: pose solver emits transform candidates, objective diagnostics and source-to-camera convention receipt.

Software: Use solvePnP/solvePnPRansac as supported; retain multiple solutions where exposed and compute explicit inverse.

Agent: Review outliers, symmetry, planar alternatives and positive-depth consistency.

Inputs: Validated correspondence set; solver options; initial guess if required.

Output/check: Candidate object-to-camera rotation/translation, inlier mask and residuals. Validation: Check rotation/handedness, finite translation and required positive depths; solver success is a candidate result.

Dependencies: OpenCV PnP/projectPoints; camera axes x-right, y-down, z-forward recorded with conversion.

Resources: Local fit follows points/hypotheses; robust sampling cost depends outliers; remote interpretation separate.

Source-supported tools: OpenCV solvePnP / solvePnPRansac, projectPoints. Original evidence: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html).

### 223. Validate independent reprojection and publish pose (REC-02-A03)

Original action: [Validate independent reprojection and publish pose](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json). Operations: REC-02 — Solve camera pose from known 3D-to-2D correspondences.

Implementation proposal: Proposal: pose verifier returns per-landmark residual and feature-level readiness.

Software: Project withheld 3D points, compare regional residuals and roundtrip transform direction; evaluate alternate hypotheses.

Agent: Independent semantic reviewer checks landmark identities and occlusion visibility.

Inputs: Pose hypotheses; withheld image landmarks/control quantities; source criteria.

Output/check: Camera-solution pose/check records with supported features and ambiguity status. Validation: Wrong but low-fit-residual pose fails independent controls; output supplies pose, not reconstructed surfaces.

Dependencies: projectPoints and independent source measurements; image preprocessing receipt.

Resources: Local projections bounded by points; remote/full-image review and manual extra controls separate.

Source-supported tools: OpenCV solvePnP / solvePnPRansac, projectPoints. Original evidence: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html).

### 224. Estimate dense depth and fuse visible samples (REC-17-A02)

Original action: [Estimate dense depth and fuse visible samples](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-17 — Build dense point cloud and mesh from SfM camera solution.

Implementation proposal: Proposal: dense runner emits depth/fusion artifacts and source support/coverage manifest.

Software: COLMAP patch_match_stereo then stereo_fusion, or InterfaceCOLMAP→DensifyPointCloud under documented image/camera bridge; preserve selected backend differences.

Agent: Review depth consistency and excluded reflective/dynamic/low-texture regions.

Inputs: Checked workspace, masks and depth/fusion settings.

Output/check: Per-view dense depth/confidence and fused cloud with camera/settings lineage. Validation: Empty or sparse-only cloud cannot satisfy declared dense coverage; fusion creates no mesh output.

Dependencies: Actual selected dense API/CLI/build; source CPU/GPU support conditional.

Resources: Cost follows image pixels, depth range, neighbors and stored maps; bounded subset/CPU-supported alternative first where suitable.

Source-supported tools: OpenMVS DensifyPointCloud, OpenMVS ReconstructMesh, COLMAP dense workspace. Original evidence: [https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/](https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/), [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst).

### 225. Mesh dense cloud and validate both outputs (REC-17-A03)

Original action: [Mesh dense cloud and validate both outputs](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-17 — Build dense point cloud and mesh from SfM camera solution.

Implementation proposal: Proposal: dense-output publisher emits both typed artifacts with per-feature observed/inferred status.

Software: Use supported COLMAP poisson_mesher/delaunay_mesher or OpenMVS ReconstructMesh with actual cloud input; inspect normals/holes/components and compare mesh/cloud/controls.

Agent: Separate reviewer checks source feature association and filled/unsampled surfaces.

Inputs: Fused cloud, selected mesher/normal settings, original photos and withheld controls.

Output/check: Actual cloud and triangle mesh plus source/approximation/readback report. Validation: Successful fusion alone cannot satisfy mesh contract; same captures produce dependent evidence, not independent truth.

Dependencies: Pinned meshing backend and DOM-29 comparison/cleanup conditions.

Resources: Meshing cost follows points/normals/grid and triangles; local selected controls precede full comparisons, remote review separate.

Source-supported tools: OpenMVS DensifyPointCloud, OpenMVS ReconstructMesh, COLMAP dense workspace. Original evidence: [https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/](https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/), [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst).

### 226. Recover cameras and the declared cloud representation (DOM-20-A02)

Original action: [Recover cameras and the declared cloud representation](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-20 — Photos/video to camera solution, point cloud and mesh.

Implementation proposal: Proposal: photo-domain composer emits camera/cloud and typed optional-stage ledger.

Software: Compose REC-03; add supported dense sampling only when declared, preserving actual cloud type; mesh remains explicit REC-17/DOM-28 branch.

Agent: Review disconnected/low-confidence regions and source correspondence.

Inputs: Checked photo plan, selected sparse/dense backend and settings.

Output/check: Camera-solution plus explicitly sparse/dense point-cloud with stage/source receipts. Validation: Mesh is not required output; absent camera or cloud remains partial.

Dependencies: Actual backend capability and point05 camera/frame checks.

Resources: Sparse CPU-compatible work first; dense GPU/RAM requirements conditional on actual chosen branch.

Source-supported tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG/OpenMVS. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 227. Validate saved domain outputs and downstream conditions (DOM-20-A03)

Original action: [Validate saved domain outputs and downstream conditions](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-20 — Photos/video to camera solution, point cloud and mesh.

Implementation proposal: Proposal: photo-domain verifier emits exact-output and downstream mesh/metric prerequisites.

Software: Verify image/pose mapping, component coverage, cloud detail and scale/frame; apply independent controls as required.

Agent: Separate reviewer checks scene/feature identity and visible versus inferred evidence.

Inputs: Saved outputs, source views and reserved controls where metric use is required.

Output/check: Camera/coverage/source/frame report and use-specific outputs. Validation: Cloud/file format cannot be substituted by Gaussian parameters or scene checkpoint.

Dependencies: REC-03/17 validation and proposed domain output checker.

Resources: Local output/control checks before display review; remote/manual assessment separate.

Source-supported tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG/OpenMVS. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 228. Compose dense estimation fusion and meshing (DOM-28-A02)

Original action: [Compose dense estimation fusion and meshing](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-28 — Dense multi-view stereo to point cloud and mesh.

Implementation proposal: Proposal: domain composer links dense/cloud/mesh stages without treating one output as another.

Software: Execute REC-17 supported stages; preserve exact mesher and nonempty/output-type checks.

Agent: Review coverage and method-dependent missing/filled regions.

Inputs: Checked dense plan and supported runtime/configuration.

Output/check: Both artifacts plus per-stage depth/fusion/mesh/settings receipts. Validation: Names/format suffixes cannot substitute actual dense samples and triangle faces.

Dependencies: Pinned COLMAP/OpenMVS or separately evidenced Meshroom graph.

Resources: Local CPU-compatible stage choices first; dense GPU/RAM conditions and storage recorded per backend.

Source-supported tools: COLMAP dense reconstruction; AliceVision/Meshroom; OpenMVS. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 229. Check source geometry and independent controls (DOM-28-A03)

Original action: [Check source geometry and independent controls](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-28 — Dense multi-view stereo to point cloud and mesh.

Implementation proposal: Proposal: dense-domain verifier emits output-completeness and source/metric findings.

Software: Reopen and compare required interfaces, holes/components, source projection and cloud/mesh residuals.

Agent: Separate reviewer checks inferred/observed partition and feature identity.

Inputs: Saved outputs, source images/cameras and reserved measurements/views.

Output/check: Coverage, frame, geometric residual and per-feature readiness report. Validation: Rendered surface plausibility cannot pass metric or occluded-feature requirement.

Dependencies: REC-17/DOM-29 verifiers and point05 registration checks.

Resources: Local selected controls before dense full-surface comparisons; remote review/manual metrology separate.

Source-supported tools: COLMAP dense reconstruction; AliceVision/Meshroom; OpenMVS. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 230. Compose sparse and dense visible-surface reconstruction (CAD-16-A02)

Original action: [Compose sparse and dense visible-surface reconstruction](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: CAD-16 — Reconstruct camera poses and dense visible geometry from overlapping photos.

Implementation proposal: Proposal: stage composer links immutable sparse/dense/mesh receipts and common metric transform.

Software: Run REC-03 sparse checks, then REC-17/DOM-28 dense cloud and mesh stages only when prerequisites pass.

Agent: Review coverage exceptions and select supported visible-surface branch.

Inputs: Checked photo/control plan; supported sparse/dense backend and settings.

Output/check: Stage receipts and all three actual output artifacts with common source/scale/frame lineage. Validation: Sparse cloud alone cannot satisfy dense/mesh target; meshing/filling cannot promote hidden regions to observations.

Dependencies: Actual dense backend/import bridge; CPU/GPU configuration and output support recorded.

Resources: Sparse CPU-compatible subset first; dense GPU/RAM cost follows images/resolution/depth range/neighbors; remote review separate.

Source-supported tools: COLMAP or AliceVision/Meshroom, scale/control-point alignment. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [https://github.com/colmap/colmap](https://github.com/colmap/colmap), [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst).

### 231. Validate metric reference and saved three-output package (CAD-16-A03)

Original action: [Validate metric reference and saved three-output package](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: CAD-16 — Reconstruct camera poses and dense visible geometry from overlapping photos.

Implementation proposal: Proposal: package verifier emits each output's actual type/source/frame and feature-readiness report.

Software: Reopen outputs; compare camera/image consistency, controls, cloud/mesh distances, holes/outliers and frame propagation.

Agent: Separate reviewer checks observed versus inferred feature correspondence.

Inputs: Saved cameras/cloud/mesh, physical withheld controls and source image regions.

Output/check: Camera-solution, point-cloud and mesh with per-feature metric/coverage/readback results. Validation: Appearance agreement alone cannot qualify working interfaces or hidden dimensions.

Dependencies: Point05 geometry comparison and proposed reconstruction-package checker.

Resources: Local targeted controls before dense comparison/render review; manual measurements and remote VLM separate.

Source-supported tools: COLMAP or AliceVision/Meshroom, scale/control-point alignment. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md), [https://github.com/colmap/colmap](https://github.com/colmap/colmap), [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst).

### 232. Train and export the actual Gaussian scene representation (REC-19-A02)

Original action: [Train and export the actual Gaussian scene representation](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-19 — Train and export a Gaussian splat scene.

Implementation proposal: PROPOSAL Gaussian package adapter: trained state + parser transform + supported Gaussian export → typed gaussian-scene with renderer assets, attribute manifest and resume receipt.

Software: Use selected Splatfacto training and Gaussian export; preserve checkpoint/config and inspect exported attributes expected by the chosen renderer. Record actual GPU/backend requirements and resumable state.

Agent: Inspect training-view/coverage artifacts and compare recorded candidate settings without interpreting rendered completion as observed surface evidence.

Inputs: A01 dataset/receipt, exact model/config/checkpoint schedule, selected backend and documented Gaussian export capability.

Output/check: Gaussian scene package with training config/checkpoint, renderer/version, exported Gaussian PLY when supported, bounds/frame mapping and artifact hashes. Validation: Load with the named Gaussian renderer; verify image/camera/frame associations and required attributes. Ordinary point-cloud readers cannot establish Gaussian-scene completeness.

Dependencies: A01 parsed cameras; actual renderer/export schema and compatible consumer; source rights/checkpoint terms.

Resources: Local GPU memory depends on method, image size/count, iterations and Gaussian count; source Splatfacto examples about 6/12 GB are setup-specific. Record actual duration/VRAM when tested, separate from remote VLM.

Source-supported tools: Nerfstudio Splatfacto / gsplat, Gaussian PLY export. Original evidence: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html).

### 233. Evaluate captured-view appearance and geometry handoff boundaries (REC-19-A03)

Original action: [Evaluate captured-view appearance and geometry handoff boundaries](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-19 — Train and export a Gaussian splat scene.

Implementation proposal: PROPOSAL Gaussian evaluation/composition ledger: scene + captured checks + optional geometry transforms → region results, compatible scene layers and fresh composite validation.

Software: Render evaluation cameras using pinned renderer; compare captured regions under stated exposure/mask policy; verify scene transform by known source projections; typed-check any additional mesh.

Agent: VLM compares original capture/full-view/crops and numerical appearance report; independent reviewer checks object/region meanings and source/generated/evaluation roles.

Inputs: A02 scene, exact evaluation cameras and real images, participation table, feature/region criteria and optional independently reconstructed mesh/CAD.

Output/check: Appearance evaluation with shared dependencies, selected Gaussian revision, renderer receipt and explicit geometry/composite proposal. Validation: Generated novel views retain checkpoint lineage; training-heldout/SfM-used views are labelled accordingly; Splatfacto geometry export remains capability-gated despite generic TSDF wording.

Dependencies: A02 complete renderable package; heldout policy and camera provenance; separate geometry branch if a mesh/CAD composite is requested.

Resources: Small fixed evaluation set first, then required viewing coverage; renderer GPU cost and VLM image/token/manual review costs separately recorded.

Source-supported tools: Nerfstudio Splatfacto / gsplat, Gaussian PLY export. Original evidence: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html).

### 234. Estimate depth and cameras and materialize the declared cloud (REC-10-A02)

Original action: [Estimate depth and cameras and materialize the declared cloud](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-10 — Estimate multi-view depth, camera poses and Gaussian outputs.

Implementation proposal: PROPOSAL DA3 result adapter: raw depth/camera/confidence exports + image/config manifest → named camera records, typed geometric cloud, frame/scale receipt and partial-output status.

Software: Use documented DA3 photo/video or streaming route; read raw camera arrays/conventions and cloud attributes, apply a recorded transform only once. Discover release-specific output schema before interpreting it. DA3Metric-Large card fields are depth/confidence [N,H,W], W2C extrinsics [N,3,4] and K [N,3,3]; actual selected API metric/focal conversion must be established without inventing a card-missing divisor or converting twice.

Agent: Review alternative pose/scale or foreground/background assignments; retain competing outputs when source/control evidence does not select one.

Inputs: A01 manifest, selected input subset/checkpoint, actual invocation configuration, optional supplied pose policy and masks.

Output/check: Camera-solution, point-cloud, per-frame depth/confidence where enabled, raw model output and export receipt; optional Gaussian output stays a separate typed derivative. Validation: Read back every camera/image match, matrix direction and finite valid sample; detect missing camera export, arbitrary scale and Gaussian attributes before classifying a PLY as geometric samples.

Dependencies: A01 output contract; per-image preprocessing/calibration mapping; actual selected backend export discovery.

Resources: Local inference cost depends on variant, image resolution/count and chunk size/overlap; record peak RAM/VRAM and inference duration when tested; streaming chunks need overlap/seam checks.

Source-supported tools: Depth Anything 3, DA3-Streaming, DA3 Blender add-on. Original evidence: [https://github.com/ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3), [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md), [https://github.com/xy-gao/DA3-blender](https://github.com/xy-gao/DA3-blender).

### 235. Compare predictions with independent controls and conventional candidates (REC-10-A03)

Original action: [Compare predictions with independent controls and conventional candidates](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-10 — Estimate multi-view depth, camera poses and Gaussian outputs.

Implementation proposal: PROPOSAL prediction comparison ledger: predicted and conventional candidates + fit/check partition → regional errors, selection reasons, common dependencies and per-feature readiness.

Software: Project/reproject sampled geometry through actual cameras; align only using designated fit controls; calculate withheld distances and source-region differences with typed cloud readers.

Agent: VLM compares feature associations and masks using full views, crops and numerical reports; a separate reviewer checks the selected interpretation and shared model/source dependencies.

Inputs: A02 artifacts, independent control measurements/views with fit roles, optional REC-03/17 conventional candidate and same-revision comparison package.

Output/check: Per-feature comparison report, selected candidate or unresolved alternatives, camera/cloud handoff and independent semantic review. Validation: Both typed outputs exist; independent checks use reserved controls; inferred hidden regions retain inferred status; same-source predictions do not count as independent acquisitions. Card-only focal conversion ambiguity blocks a metric claim until the actual adapter's units/recipe are checked.

Dependencies: A02 complete outputs; comparison candidates bound to same feature IDs/frame or explicit measured transform; withheld controls.

Resources: Numerical subset comparison before full-cloud distances; local projection/nearest-neighbour cost scales with samples, while VLM image/crop tokens and manual correspondence work are separate.

Source-supported tools: Depth Anything 3, DA3-Streaming, DA3 Blender add-on. Original evidence: [https://github.com/ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3), [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md), [https://github.com/xy-gao/DA3-blender](https://github.com/xy-gao/DA3-blender).

### 236. Generate and preserve the proxy mesh and its coordinate frame (REC-18-A02)

Original action: [Generate and preserve the proxy mesh and its coordinate frame](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-18 — Generate a single-image mesh proxy.

Implementation proposal: PROPOSAL proxy exporter: raw model result + input/config receipt → mesh/material package, frame/normalization map and per-region generated lineage.

Software: Future adapter invokes selected documented model, records raw mesh and texture outputs, reads vertices/faces/material references and export axes; save derivative before optional cleanup.

Agent: Inspect visible silhouette and hidden geometry across labelled rendered views while keeping their common generated origin.

Inputs: A01 request, selected model/config/checkpoint/seed, original image/mask and optional explicit alignment controls.

Output/check: Generated triangle mesh, optional texture/materials, raw model output, bounds/frame/unit-status and generation receipt. Validation: Read back face indices, finite coordinates, normals, bounds/material references and actual mesh payload; a preview image or Gaussian file is a partial output.

Dependencies: A01 mesh contract; new output path/revision; renderer can consume actual mesh format.

Resources: Local inference depends on exact model resolution, variant and GPU memory; export/mesh checks depend on vertex/face count; remote model services and VLM reasoning have distinct request/cost records.

Source-supported tools: TripoSR, TRELLIS.2, SAM 3D Objects. Original evidence: [https://github.com/VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR), [https://github.com/microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2), [https://github.com/facebookresearch/sam-3d-objects](https://github.com/facebookresearch/sam-3d-objects).

### 237. Evaluate visible fit and gate geometric reuse by independent evidence (REC-18-A03)

Original action: [Evaluate visible fit and gate geometric reuse by independent evidence](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-18 — Generate a single-image mesh proxy.

Implementation proposal: PROPOSAL proxy qualification ledger: mesh + actual capture/control evidence → feature readiness by intended use, candidate selection and remodeling requirements.

Software: Render under the matched camera, compare original-pixel masks and measured controls; run mesh validity/local topology checks before reuse.

Agent: VLM compares competing generated candidates using actual visible evidence and required interfaces; separate semantic reviewer checks visible/inferred labels and source correspondence.

Inputs: A02 mesh, source image/camera information, independent additional captured views/measurements if supplied, and intended-use criteria.

Output/check: Proxy evaluation, visible/inferred feature map, selected candidate and scoped handoff to point-05 remodeling or visual context. Validation: Generated back views of the candidate count as internal visualization; independent capture/control IDs are preserved; mesh validity alone cannot pass dimensional requirements.

Dependencies: A02 artifact hash; source pixel mapping; proposed CAD handoff preserves exact dimensional evidence and generated mesh.

Resources: Low-resolution renders and selected feature queries first; full mesh queries only for required regions; record manual interpretation and remote VLM evidence package separately.

Source-supported tools: TripoSR, TRELLIS.2, SAM 3D Objects. Original evidence: [https://github.com/VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR), [https://github.com/microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2), [https://github.com/facebookresearch/sam-3d-objects](https://github.com/facebookresearch/sam-3d-objects).

### 238. Train and save a renderable NeRF state (REC-20-A02)

Original action: [Train and save a renderable NeRF state](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-20 — Train and export a NeRF scene.

Implementation proposal: PROPOSAL NeRF package adapter: training state/config + transform receipt → renderable nerf-scene and separately typed optional export with support/loss map.

Software: Use supported NeRF trainer/save/load route; preserve config/checkpoint and renderer dependencies. Before optional export, verify method supplies depth/normals/field needed by that exporter.

Agent: Inspect training progress/coverage evidence and compare actual region outputs, retaining source-dependent artifacts.

Inputs: A01 parsed dataset and transforms, selected NeRF configuration/backend, training schedule, checkpoint/resume settings.

Output/check: NeRF scene package: config, weights/checkpoint, renderer/code version, bounds, camera/world map and hashes; conditional mesh export is a separate derivative. Validation: Reopen checkpoint with selected renderer and render a recorded camera; an exported preview GLB alone is insufficient for a resumable NeRF-state claim.

Dependencies: A01 dataset; locally supported GPU/backend and checkpoint format; actual consumer renderer contract.

Resources: Local training depends on ray batch/image resolution/iterations/model and hardware; renderer/extraction grids can add substantial memory; record actual observations separately from remote VLM/manual effort.

Source-supported tools: Nerfstudio nerfacto, Nerfstudio checkpoint and viewer export. Original evidence: [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md), [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md).

### 239. Validate scene appearance and any separately extracted geometry (REC-20-A03)

Original action: [Validate scene appearance and any separately extracted geometry](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-20 — Train and export a NeRF scene.

Implementation proposal: PROPOSAL NeRF qualification adapter: trained scene + actual captures + optional extracted geometry/control evidence → appearance and geometry reports with independent readiness.

Software: Render fixed captured evaluation cameras; compare named regions; if extraction is supported, read mesh topology/frame, reproject to sources and check withheld dimensions without replacing the trained state.

Agent: VLM chooses scene/extraction candidates from original images and numerical reports; separate semantic reviewer checks surface interpretation and generated regions.

Inputs: A02 scene and optional extracted mesh, real evaluation images/cameras/role table, feature criteria and independent measurements when geometry is requested.

Output/check: Region-based appearance report, actual scene consumer receipt, optional geometry validation and selected revision. Validation: Field-derived meshes retain inference/extraction provenance; generated evaluation views are internal tests; Gaussian exports cannot substitute for nerf-scene state.

Dependencies: A02 complete state, evaluation partition and actual optional exporter capability; point-05 registration for CAD composition.

Resources: Render small fixed comparison set first; extraction resolution/bounds determines local grid cost; full mesh checks only required regions, with VLM/manual review logged independently.

Source-supported tools: Nerfstudio nerfacto, Nerfstudio checkpoint and viewer export. Original evidence: [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md), [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md).

### 240. Execute the selected typed training route and package its scene (REC-11-A02)

Original action: [Execute the selected typed training route and package its scene](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-11 — Train NeRF or Gaussian scene for view synthesis.

Implementation proposal: PROPOSAL visual-scene manifest builder: checked Gaussian/NeRF package + consumer contract → generic visual-scene with exact subtype, dependency closure and load receipt.

Software: Invoke the selected typed procedure in future execution; verify saved state and supported export; package actual renderer dependencies and raw source revisions.

Agent: Review typed route exceptions and incompatible output formats; retain evidence-supported alternatives rather than relabel one representation as another.

Inputs: A01 dispatch record and complete REC-19 or REC-20 dataset/training inputs.

Output/check: Visual-scene manifest referencing actual Gaussian or NeRF package, renderer/version, config/checkpoint/assets, world transform and export loss map. Validation: All referenced assets exist and hashes match; named consumer actually loads the scene; mesh/GLB expectations require their separate supported export branch.

Dependencies: A01 dispatch; REC-19/20 complete package and source rights; target renderer adapter.

Resources: Reuse the selected route's training cost record; manifest/asset validation is local I/O proportional to checkpoint size; renderer load and remote reasoning separately logged.

Source-supported tools: Nerfstudio ns-process-data, ns-train nerfacto/splatfacto, ns-export gaussian-splat/tsdf/poisson/pointcloud. Original evidence: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html), [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md), [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md).

### 241. Validate scene use and proposed appearance/mesh/CAD composition (REC-11-A03)

Original action: [Validate scene use and proposed appearance/mesh/CAD composition](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: REC-11 — Train NeRF or Gaussian scene for view synthesis.

Implementation proposal: PROPOSAL scene composition ledger: typed appearance package + optional mesh/CAD + measured transforms → layered scene manifest, affected checks and source-per-feature report.

Software: Render fixed captured views; if composition is in scope, calculate/read actual source→target transforms and compare projection and critical geometric controls for each layer.

Agent: VLM selects compatible layer associations using full captured views and numerical reports; independent semantic reviewer checks feature identity and generated/observed labels.

Inputs: A02 visual-scene, real evaluation captures/cameras/role table, optional independently reconstructed mesh and measured parametric CAD with their frames.

Output/check: Visual-scene evaluation and selected revision; optional composition manifest with typed layers, transforms, source mappings and independent checks. Validation: Each layer preserves its representation and source role; shared camera/model dependencies are stated; a visual alignment cannot replace critical interface measurements.

Dependencies: A02 loadable scene; real evaluation sources; separate mesh/CAD artifact identities and supported renderer/composition adapter.

Resources: Small source-aligned preview before full rendering; geometry queries scale with required features; local rendering/geometry work, remote VLM and manual corrections remain separate.

Source-supported tools: Nerfstudio ns-process-data, ns-train nerfacto/splatfacto, ns-export gaussian-splat/tsdf/poisson/pointcloud. Original evidence: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html), [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md), [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md).

### 242. Build the Gaussian scene and preserve domain mappings (DOM-22-A02)

Original action: [Build the Gaussian scene and preserve domain mappings](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-22 — Photographs to Gaussian/NeRF visual scene.

Implementation proposal: PROPOSAL domain scene packager: Gaussian state + source/domain map → gaussian-scene with stable source feature references and actual renderer receipt.

Software: Use REC-19 A01/A02; preserve domain IDs through source region mapping and scene transform, rather than assuming each learned primitive has a physical component identity.

Agent: Review changed masks/coverage and feature association after training/export.

Inputs: A01 request plus complete REC-19 training inputs and domain feature/source sidecar.

Output/check: Gaussian scene package and domain mapping sidecar with checkpoint, renderer, parsed-camera/world transform and export attributes. Validation: Typed Gaussian attributes and renderer state match; source feature identity is retained through mappings; node/primitive order does not create semantic IDs.

Dependencies: A01 mapping; REC-19 complete scene and renderer dependency manifest.

Resources: Reuse recorded training demand; sidecar checks are local metadata work; rendering cost follows scene size/viewpoints and remote reasoning separate.

Source-supported tools: Nerfstudio/gsplat; COLMAP camera input; Blender viewer/export. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 243. Check domain appearance and explicit geometric overlays (DOM-22-A03)

Original action: [Check domain appearance and explicit geometric overlays](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-22 — Photographs to Gaussian/NeRF visual scene.

Implementation proposal: PROPOSAL domain appearance report: Gaussian scene + captured checks + optional measured geometry → region readiness and compatible overlay receipt.

Software: Render actual evaluation cameras; check source-region coverage; if geometry overlay is scoped, apply checked transforms and query required measured interfaces/placements.

Agent: VLM associates domain features using source images and numerical overlay evidence; separate reviewer checks physical identity and representation roles.

Inputs: A02 Gaussian scene/mapping, real evaluation captures and role table, optional domain geometry with controls and frame chain.

Output/check: Domain region report, selected Gaussian revision and optional checked composition manifest. Validation: Gaussian coverage cannot satisfy missing physical geometry; optional overlay requires actual feature/frame checks; generated views retain shared checkpoint lineage.

Dependencies: A02 renderable output; independent source/control evidence; separate geometry identity for composition.

Resources: Use selected region views and control queries before full scene traversal; log local render/query costs and remote VLM/manual associations separately.

Source-supported tools: Nerfstudio/gsplat; COLMAP camera input; Blender viewer/export. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 244. Train and package the domain NeRF state (DOM-30-A02)

Original action: [Train and package the domain NeRF state](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-30 — Photos to NeRF visual scene.

Implementation proposal: PROPOSAL domain NeRF packager: trained NeRF + domain/source map → loadable nerf-scene manifest with renderer, frame chain and artifact dependencies.

Software: Run REC-20 A01/A02 in future execution; attach domain/source references and actual parsed-camera/world mapping; preserve checkpoint/assets.

Agent: Review domain coverage/mask changes or invalid camera interpretations; select evidence-supported configuration alternatives.

Inputs: A01 request, REC-20 dataset/config/training inputs and source-to-domain mapping.

Output/check: NeRF config/checkpoint/renderer package, domain source sidecar, parser transform/scale and complete/partial receipt. Validation: Checkpoint/config/renderer dependencies load; domain/source mappings remain revision-bound; an optional extracted mesh cannot replace NeRF state.

Dependencies: A01 request and REC-20 complete renderable-state requirements.

Resources: Reuse actual NeRF training measurements when available; package hash/readback scales with checkpoint bytes; remote VLM/manual review is recorded separately.

Source-supported tools: Nerfstudio; COLMAP camera input. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).

### 245. Evaluate domain viewing results and optional surface reuse (DOM-30-A03)

Original action: [Evaluate domain viewing results and optional surface reuse](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json). Operations: DOM-30 — Photos to NeRF visual scene.

Implementation proposal: PROPOSAL domain NeRF qualification: scene + source/check roles + optional geometry → per-region appearance/geometry readiness and affected dependency checks.

Software: Render named captured evaluation views; compare domain regions; inspect supported optional extraction's geometry and frame against controls before geometric reuse.

Agent: VLM evaluates source-supported domain associations and alternative outputs; a separate semantic reviewer verifies feature meaning, observed/inferred status and evaluation dependencies.

Inputs: A02 scene, real evaluation captures/cameras/roles, domain criteria and optional surface/control evidence.

Output/check: Domain appearance report, selected NeRF revision and optional separate geometry/composition validation receipt. Validation: Generated novel views retain derived status; NeRF geometry cannot inherit IFC/component semantics from appearance; new geometric layers preserve original identity evidence.

Dependencies: A02 complete renderer state; exact optional exporter capability; domain measured controls for geometry use.

Resources: Fixed region/view sample first; extraction grid and mesh checks have separate local memory/compute costs; VLM evidence and manual correction effort separate.

Source-supported tools: Nerfstudio; COLMAP camera input. Original evidence: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md).
