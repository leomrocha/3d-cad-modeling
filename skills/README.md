# Project skill catalogue

## Skills supplied by this repository

1. [cad-ocs-engineering](cad-ocs-engineering/SKILL.md) — OCS modeling contracts, guarded session control, component iteration, geometry checks, saved results and computational handoffs.
2. [cad-drawing-inspection](cad-drawing-inspection/SKILL.md) — inventories DXF entities, units, layers, spaces and nested transforms.
3. [cad-source-intake](cad-source-intake/SKILL.md) — preserves source files, hashes, request scope and corrected input revisions.

4. [CAD MCP translator](cad-mcp-translator/SKILL.md) — adapt an operation to a selected endpoint and qualify it independently.

5. [CAD format translator](cad-format-translator/SKILL.md) — convert model files, generate geometry or translate editable source. [Blender exchange, conversion routes and verification](cad-format-translator/references/conversion.md).

Install these skills using the [README instructions](../README.md#installing). The [tools page](../docs/tools.md) lists the Python helpers. Each skill directory includes its runtime files and dependencies. OCS engineering (`cad-ocs-engineering`) includes its OCS control and geometry adapters. [Package maintenance](../docs/skill-packaging.md).

## Component CAD procedure index

1. **Job contract:** [component requirements and action records](cad-ocs-engineering/references/component-procedure.md).
2. **Model reuse:** [existing-model checks and configuration selection](cad-ocs-engineering/references/existing-model-start-check.md).
3. **Source interpretation:** [drawing features](cad-ocs-engineering/references/drawing-feature-checks.md), [limits, datums, drawing scale and dual units](cad-ocs-engineering/references/dimension-limits-and-datums.md), [source-image inspection and retrieval routes](cad-ocs-engineering/references/source-view-evidence.md), [variant tables and fastener standard editions](cad-ocs-engineering/references/source-variant-tables.md).
4. **Traced geometry:** [calibrated coordinates](cad-ocs-engineering/references/calibrated-trace.md), [source-vector perimeter chains](cad-ocs-engineering/references/source-perimeter-chains.md), [profile extrusion](cad-ocs-engineering/references/profile-reference.md).
5. **Construction:** [rounded hollow sections](cad-ocs-engineering/references/source-first-and-tube.md), [axial motors](cad-ocs-engineering/references/axial-motor.md), [rectangular envelopes](cad-ocs-engineering/references/envelope-reference.md), [guarded envelope runner](cad-ocs-engineering/references/envelope-job-runner.md), [Pixhawk clearance geometry](cad-ocs-engineering/references/pixhawk.md), [annular references](cad-ocs-engineering/references/annular-reference.md), [guarded annular job runner](cad-ocs-engineering/references/annular-job-runner.md), [hexagonal references](cad-ocs-engineering/references/hexagonal-reference.md), [toroidal references](cad-ocs-engineering/references/toroidal-reference.md), [spherical-seat profiles](cad-ocs-engineering/references/spherical-seat-profile.md), [conical-washer profiles](cad-ocs-engineering/references/conical-washer-profile.md).
6. **Component checks:** [bearing geometry](cad-ocs-engineering/references/existing-bearing.md), [battery shells and terminals](cad-ocs-engineering/references/existing-battery.md), [tabbed battery cases](cad-ocs-engineering/references/tabbed-battery.md), [smallBMS saved geometry](cad-ocs-engineering/references/small-bms.md), [shared feature comparisons](cad-ocs-engineering/references/shared-feature-checks.md).
7. **Assemblies:** [manufacturer placements](cad-ocs-engineering/references/manufacturer-assembly.md), [scaled imports](cad-ocs-engineering/references/scaled-assemblies.md), [root unit-change plans](cad-ocs-engineering/references/assembly-units.md), [STEP solid inventories](cad-ocs-engineering/references/step-solid-inventory.md).
8. **Completion:** [saved source metadata](cad-ocs-engineering/references/source-metadata.md), [retained-file manifests](cad-ocs-engineering/references/retained-artifact-checks.md), [owned-document cleanup](cad-ocs-engineering/references/document-cleanup.md), [required package completion and registration](cad-ocs-engineering/references/package-completion.md).

The [tools page](../docs/tools.md) lists the packaged helper implementations and their source-bound geometry roles.

## OCS engineering procedures

[Reusable geometry, recovery and artifact methods](cad-ocs-engineering/references/generic-integration.md) covers stable records, incremental checkpoints, plates, bounded profiles, sidewall cuts, insertion, quantities and native solid and straight polyline boundary views with caller-supplied inputs.

1. [OCS control](cad-ocs-engineering/references/ocs-control.md) — session discovery, installed schemas and guarded requests.
   [Incremental saving](cad-ocs-engineering/SKILL.md#save-work-in-progress) preserves IN_PROGRESS native models and supporting files at verified checkpoints throughout long jobs. The pre-save audit uses the checkpoint destination.
2. [Computational engineering](cad-ocs-engineering/references/computational-engineering.md) — equations, geometry/material/solver contracts and representation handoffs.
3. [Capability evidence](cad-ocs-engineering/references/sources-and-capabilities.md) — original dated OCS and tool findings with source locators.
4. [Non-geometric requirements](cad-ocs-engineering/references/non-geometric-requirements.md) — explicit source-pinned tasks whose scope requires no CAD geometry.
5. [Prepare a batch of CAD operations](cad-ocs-engineering/SKILL.md#prepare-a-batch-of-cad-operations) covers grouping targets by action, input entity and output, reviewing unit-normalized rows, and qualifying the selected catalogue operation with readback before applying those rows.
6. [Resolve batch targets against measured geometry](cad-ocs-engineering/SKILL.md#resolve-batch-targets-against-measured-geometry) covers occurrence paths, named selections, distance conditions from measured references, DXF inventories, and target and reference checks after reopening.
7. [Generate positions on a planar reference](cad-ocs-engineering/references/planar-positions.md) covers ordered coordinates, tangent directions, and transferring position IDs, units and frames to a batch action.
8. [Position and orient occurrences in 3D](cad-ocs-engineering/references/spatial-positions.md) covers prism, cylinder and sphere positions, mounting directions, parent and world transforms, and distance and placement checks.
9. [Resolve row spacing and measure surface gaps](cad-ocs-engineering/references/row-spacing.md) covers centre pitches, face gaps, border margins, residual spacing and clearance measurements between placed shapes.
10. [Place existing occurrences at reviewed destinations](cad-ocs-engineering/references/existing-batch-placement.md) covers matching DXF INSERT entities to position IDs, moving them in their parent frames, resuming individual requests and checking saved placements.

11. [Create a group of elements](cad-ocs-engineering/references/batch-creation.md) covers drawing circles, holes in a selected solid and shared part occurrences.
12. [Modify selected dimensions and properties](cad-ocs-engineering/references/batch-modification.md) covers driving sketch dimensions, STEP bore enlargement and changes to selected XCAF bar lengths and occurrence names.

## Installed package references

1. [Bundled OCS runtime](cad-ocs-engineering/references/ocs-runtime.md), [model and coordinate-check contract](cad-ocs-engineering/references/model-contract.md) and [caller-owned paths](cad-ocs-engineering/references/paths.md) explain cad-ocs-engineering execution from its installed directory.
2. [Package maintenance](../docs/skill-packaging.md) records canonical code ownership, distribution generation and isolated checks.

Choose a modeling operation using the [operation selection procedure](../docs/modeling-operation-selection.md).

## Component-driven implementation

[Component CAD iterations](cad-ocs-engineering/SKILL.md) checks source readiness, records individual action occurrences and requires an applied verified skill or script improvement per completed CAD design. Use the [parts catalogue configured at setup or refresh](cad-ocs-engineering/references/modeling-operation-selection.md#set-up-and-refresh-the-local-operation-catalogue) to find existing components. Save component models, recipes and inspection results in the modeling job's configured output directory. [Part-index access](../scripts/part_index.py) and [component source and action records](../scripts/component_records.py) operate on explicit data paths.

## Source intake

1. [Record source files, revisions and job scope](cad-source-intake/SKILL.md) implements source capture, corrections and protected revisions for the shared intake action.

## DXF inspection

1. [Inspect a DXF drawing before selecting a profile](cad-drawing-inspection/SKILL.md) records source entities, units, spaces, layers and nested block transforms.

## Circular opening inspection

1. [Saved circular boundaries](cad-ocs-engineering/references/circular-boundary-checks.md) — associates full circular cap loops, analytic curve parameters and reciprocal cylindrical face boundaries.

## Source-bound screw construction

1. [Hex-head and cylindrical-shaft reference](cad-ocs-engineering/references/hex-screw-reference.md) — source pins, explicit frame, joined solid and native feature checks.

## Exact source and partial-work procedures

1. [Exact source checks](cad-ocs-engineering/references/exact-source-checks.md) — complete curves, material-domain proofs, outward face orientation, ruled patches, persistence and capture identities.
2. [Component completion](cad-ocs-engineering/references/component-completion.md) — incremental saves and final source/metadata/persistence/cleanup evidence plus an applied verified reusable improvement.

## Reversible source workflows

1. [Conditioning, exact equivalence and solid transfer](cad-ocs-engineering/references/reversible-source-workflows.md) — bounded input transforms, preserved strict failures, unchanged native evidence and checkpoint identity.

## Insertion recovery and verified resume

1. [Insertion, resume and assembly verification](cad-ocs-engineering/references/insertion-resume-verification.md) — verified defaults, point-only correction, pinned checkpoints, repeated-instance matching and preserved source anomalies.
2. [Recover a batch of DXF block insertions](cad-ocs-engineering/references/insertion-resume-verification.md#recover-a-batch-of-dxf-block-insertions) covers request journals, saved DXF readback and dependent writes after interruption.

## Surface and mesh recovery

1. [Numerical surface and mesh recovery](cad-ocs-engineering/references/surface-mesh-recovery.md) — bounded rational evaluation, triangle checks, DXF layer derivatives, cancellation effects and caller-selected persistence operations.

## Optional contributions

1. [Contribute a verified modeling improvement](cad-ocs-engineering/references/contributing.md) covers the local preview, checked branch and separate choice to publish.

## CAD MCP translator procedures

1. [Bootstrap, adapt and verify one operation](cad-mcp-translator/references/operations.md).
2. [Contribute a translator improvement](cad-mcp-translator/references/contributing.md).

## Navigation and repair

1. [Model navigation](cad-model-navigation/SKILL.md) covers occurrence identities, nested placement, materials, visible layers and catalogue lookup. [Saved assembly checks](cad-model-navigation/references/assembly-validation.md).
2. [Model repair](cad-model-repair/SKILL.md) checks the original geometry and native history, the repaired assignments, and repeat application.

## Service clearance

1. [Service clearance](cad-ocs-engineering/references/service-clearance.md) covers straight translation, seated lifts, nested bore guards, source-attributed endpoints and interference witnesses.

- [Source assembly evidence](cad-ocs-engineering/references/assembly-evidence.md) covers occurrence frames, fit and contact witnesses, source trims, source-preserving STEP wrappers and shell orientation.
- [Job history archives](cad-ocs-engineering/references/job-history-archive.md) preserve and verify raw receipts and debug histories for each revision.

[Photo and multi-view blueprint handoff](cad-ocs-engineering/references/source-view-evidence.md#ruler-photographs-and-multi-view-blueprints) covers independent photo controls and orthographic landmark agreement. [Mating-interface evaluation](cad-ocs-engineering/references/assembly-evidence.md#judge-a-mating-interface) applies the job’s stated fit to measured geometry.

[Modeling operation selection](cad-ocs-engineering/references/modeling-operation-selection.md) specifies component reuse, family edits, scripted and guided providers and job evidence. Each skill includes the procedure, local operation catalogue and OpenCV operation probes. Setup and refresh record user-confirmed resources and operation dependencies.

[Optional OpenCV setup](cad-opencv-setup/SKILL.md) qualifies a selected interpreter for the image operations in drawing inspection and source intake.

[Source intake](cad-source-intake/SKILL.md) can run a supplied local SAM checkpoint with box or point prompts and preserve the earlier mask when correcting an instance.

[Two-photo measurement and learned-mesh readback](cad-ocs-engineering/references/source-view-evidence.md#two-product-photos-and-a-learned-mesh) covers camera sensitivity, independent dimensions and geometric checks after an edit.

[Hand-drawn concept sketches](cad-drawing-inspection/SKILL.md#hand-drawn-concept-sketch) links each part, relationship and dimension to its mark on the page. The [CAD handoff](cad-ocs-engineering/references/source-view-evidence.md#use-a-hand-drawn-concept-for-cad) uses those observations for catalogue lookup, approximate layout and dimensioned features.

[Standard fastener variants](cad-ocs-engineering/references/source-variant-tables.md) covers generator checks and the represented diameter of cosmetic threads.

Model workflows require existing local files or a user-supplied service with the model already loaded. Skill installation and execution must never fetch models.

[Installed modeling operations](cad-ocs-engineering/references/modeling-input-operations.md) gives runtime inputs and outputs for family generation, geometry retrieval, feature recovery, editable sequences and metric reconstruction.
