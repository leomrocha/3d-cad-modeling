# Execution plan: define one workflow point at a time

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 12 November 2026. Status: authorized documentation work; procedure and component designs are proposals. The current point is descriptions and explicit dimensions → model brief.

## 1. Required action record

Each action records the following information:

1. Purpose: the specific change or decision and the reason the workflow needs it.
2. Intended use: sketch, layout, appearance model, dimensioned geometry, simulation, manufacturing or assembly.
3. Inputs: files, values, units, source references, reference points, origins and axis directions, with required quality.
4. Outputs: artifact or decision, plus the action that consumes it.
5. Accuracy requirements: tolerances for particular features or relationships, their sources and intended use.
6. Evidence: measured dimensions, manufacturer geometry, drawing values, calculations, fitted geometry and inferred shape, with their source quality.
7. Software responsibility: parsing, calculations, geometry construction and defined checks.
8. Agent responsibility: interpretation, comparison, parameter selection, tool orchestration and exception diagnosis.
9. User decisions: the choices that determine the intended design or resolve conflicting requirements.
10. Existing dependencies: skills, applications, libraries, interfaces and supported conditions.
11. Proposed development: specific skill instructions, functions or helpers, each justified by an action and its input/output requirements.
12. Procedure: ordered operations and intermediate results.
13. Validation: software measurements, source correspondence and interpretation review, with expected outcomes and evidence.
14. Failure and resumption: detection, retained evidence, next bounded action and invalidated dependent results.
15. Resources: local processor, memory and graphics-processor use; remote model calls, latency/cost and manual intervention. Estimates carry their conditions; measurements carry their run evidence.

A broad operation can require several action records. For example, dimension recognition contains text detection, symbol interpretation, feature association and source verification.

## 2. Alternative execution options

A vision-language model (VLM) processes images and language together. A text-only reasoning model is an alternative for descriptions and structured values. The action defines the evidence given to the model and the decision or artifact it must return.

| Option | Software responsibility | Agent responsibility | Selection condition |
| --- | --- | --- | --- |
| Agent directs work | Read inputs/state; execute explicit operations and checks | Interpret evidence, choose operations and examine results | A supported reasoning procedure covers the input; interpretation remains variable |
| Software and agent work together | Perform defined calculations or construction stages | Choose input values, resolve ambiguity and direct corrections | Algorithms exist; semantic association or parameters vary |
| Software handles ordinary cases | Process supported input classes and report defined exceptions | Diagnose exceptions and choose another bounded action | Representative input and failure cases support the ordinary-case procedure |
| Software handles the complete action | Process explicit inputs and check outputs | Optional review or coordination | Rules, input conditions and required validation are established for that action |

One workflow can use several options. Model reasoning effort can increase for ambiguous evidence or competing interpretations and decrease for routine supported work. Record the requested model/effort and actual exposed runtime identity separately.

## 3. Parallel branches, comparison and merging

1. Define branches with their purpose and evidence: VLM interpretation, existing component retrieval, drawing/measurement processing, and simplified arrangement modeling are available patterns.
2. Permit different detail and accuracy targets where the requested use justifies them. Each branch retains its target and evidence labels.
3. Put branch results into common units, origins and axis directions. Identify matching parts/features before comparing them.
4. Calculate differences and record contradictions.
5. A reasoning VLM examines the source evidence, checks and intended use, then proposes feature selection, a complete candidate, retained alternatives or another iteration.
6. Record each retained feature's source branch and selection reason. Combine compatible selected features while retaining their origin and uncertainty.
7. Validate the resulting artifact and its relationships again. A successful branch check belongs to that branch's revision; the merge produces its own revision and checks.

## 4. Goal-specific accuracy and completeness

1. Define permitted dimensional differences per relevant feature or relationship and cite their source.
2. Separate dimensional accuracy, geometric detail, appearance, function, simulation properties and manufacturing requirements.
3. The user's examples distinguish a robot joint with sub-millimetre requirements from building features that can permit larger differences. These describe goal-dependent requirements; each actual feature receives its own requirement.
4. Preserve parallel representations where useful: arrangement geometry, detailed geometry, contact-calculation shapes, semantic building records and robot link/joint records each have a declared purpose.
5. A branch can pass checks for one purpose while another purpose requires further evidence or detail. Record the purpose in every result.

## 5. Replacing particular agent actions with software

1. Describe how the agent performs the action with existing tools.
2. Identify the repeatable rules and calculations in that work.
3. Specify the proposed software function for those parts and its supported input class.
4. Define representative checked examples and ambiguous/failure cases with expected results before implementation.
5. Test an authorized implementation against those cases and record actual results.
6. Use the software path for the demonstrated input class; preserve agent-assisted paths for other supported situations.
7. Record the selection rule and the condition that switches processing to another path. Migration applies per action and input class.

## 6. Model roles and validation responsibilities

| Role | Requested model and reasoning effort | Responsibility |
| --- | --- | --- |
| Procedure design | gpt-6-astra, xhigh | Examine source-backed tools; define actions, alternatives, interfaces, checks and failures |
| Visual interpretation/comparison | gpt-6.1-sol, xhigh | Examine visual-evidence procedures, feature association and evidence-based merging |
| Independent procedure review | Separate gpt-6.1-sol agent, xhigh | Challenge assumptions, contradictions, coverage and validation cases |
| Software/library/API review | gpt-6.1-terra, xhigh | Check proposed software responsibilities against existing interfaces and capabilities |
| External source lookup | gpt-6-luna, high | Inspect original documentation and register links, summaries and retrieval status |

1. Dispatch configurations and exposed runtime identities have separate execution records.
2. Designer and reviewers use original sources and actual artifacts where supplied. This audit's first point is a generic procedure definition.
3. Model agreement, source correspondence and numerical checks are recorded separately. Numerical differences are measured against named reference values; shape checks identify how edges and surfaces connect.
4. Schedule the roles within the available agent slots. The independent reviewer receives the drafted point and the original sources before its review. External browsing belongs to the Luna source task.

## 7. Local-compute-first definition order

1. Descriptions and explicit dimensions → model brief.
2. Existing components and computer-aided design (CAD) files → inspected reusable inputs.
3. Confirmed dimensions or clean vector drawings → small CAD models.
4. Pixel-based drawings → interpreted outlines and dimensions.
5. Existing CAD with photographs or scans → alignment and comparison.
6. Building and robot models → domain-specific structure and properties.
7. Overlapping photographs, large scans and learned scene reconstruction → reconstructed geometry or appearance scenes.

Photogrammetry reconstructs geometry from overlapping photographs. Dense reconstruction produces closely sampled surfaces. Gaussian splatting represents scenes using many small coloured 3D blobs. Neural radiance fields (NeRF) are trained models used to render views from different positions. These branches receive their own processing assessment.

For every option, compare local processing/memory/graphics requirements, remote model processing, latency/cost, manual intervention, output quality/evidence and further refinement work. Model calls on a remote host and processing on the local machine have separate resource records.

## Original project sources

1. [Existing CAD operations](../workflows/cad-paths.json): CAD-01 defines the source-linked brief and its evidence categories.
2. [Existing domain operations](../workflows/domain-paths.json): DOM-01 defines brief normalization.
3. [Composition rules](../workflows/composition-rules.md): branches, evidence merges and revision loops.
4. Existing OCS engineering contract (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) and model-contract reference (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`): source identity, units, frames, part boundaries and supplied-measurement checks.
5. [Retained implementation plan](../implementation-plan.md): original proposed skills, software layers and verification requirements.
