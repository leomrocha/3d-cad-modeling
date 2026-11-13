# Research and proposed implementation

Research date: 12 November 2026.

1. [Proposed next stages](next-step-proposal.md) — seven work packages derived from the retained workflow research.
2. [Workflow map](workflows/README.md) — individual operations, combined routes, representation handoffs and composition rules.
3. [Original source register](sources/source-register.md) and [structured records](sources/source-register.json) — original links, summaries and evidence status, including referenced archived originals.
4. [Ideas register](ideas-register.md) and [structured records](ideas-register.json) — retained plan proposals and new workflow research questions.
5. [Documentation and checkpoint rules](documentation-policy.md) and [research record](research-log.md).
6. [Implementation plan](implementation-plan.md) — input routes, model representations, software layers, 15 proposed workflow skills, component schema, six implementation stages and verification criteria.
7. [CAD tools and available skills](cad-and-skills.md) — OCS, FreeCAD, CadQuery, build123d, OpenSCAD, Blender, SolveSpace, OCCT, drawing intake and existing skills.
8. [Image, video and scan reconstruction](reconstruction.md) — photogrammetry, control points, point clouds, Gaussian scenes, learned reconstruction and CAD remodeling.
9. [Architecture, robotics and components](domains-and-components.md) — IFC/Bonsai, MuJoCo/MJCF, URDF, collisions, source libraries, licences and metadata.
10. [Local baseline](local-baseline.md) — existing OCS skill, prior research, tool versions and OCS exporter source inspection.
11. [Local inventory receipt](local-inventory.json) and [existing-source hashes](sources/local-evidence.json).
12. [User-supplied links](user-supplied-links.md) — all nine supplied URLs mapped to their assessment.
13. [Skill catalogue](../skills/README.md) — reuse candidates and proposed project workflows.
14. [Initial verification receipt](verification.json) — observations from the repository foundation.
15. [Workflow registration checks](workflows/register-checks.json) and [document checks](workflows/document-checks.json) — current documentation consistency checks.
16. [Square-tube corner standards for the main-frame rails and crossmembers](tube-corner-research.md) — EN 10219-2 and EN 10210-2 nominal calculation radii, external manufacturing limits, supplier evidence and proposed CAD representations; [individual source observations](sources/round-10/tube-corner-sources.json).
17. [Main-frame rail execution and applied tooling improvements](../execution/p01-rail-build.md) — source-first action records, actual OCS construction attempts, checked native rail geometry, saved model, reopened views and the SAB feature-reader issue; [four source-action definitions](action-audit/component-source-actions.json).
18. [Saved rail verification completed](../execution/p01-saved-verification.md) — existing binary parser reused, six native check groups passed, reader/skill improvement applied, 32 tests passed and crossmember dependency satisfied.
19. [Main frame crossmember completed](../execution/p02-crossmember.md) — native and saved geometry, nominal rail-gap and local midpoint checks, inspected model views and the shared interface-check improvement; 35 tests passed.

## Evidence and execution

Three research tasks were dispatched with model parameter `gpt-6-luna`: `cad_skills`, `reconstruction` and `domains_components`. Their reports contain source links and retrieval outcomes. Runtime model identifiers were not exposed to the agents; the dispatcher model parameter is recorded separately from actual runtime identity.

Primary-agent work includes local repository/source inspection, version and module-discovery probes, foundation creation, review of agent reports and synthesis of the proposed implementation plan. The existing OCS skill's partial runtime success is user-reported. Geometry experiments and installation steps in the plan describe proposed implementation work.

Web pages were inspected by the delegated research agents. Existing local originals are referenced in place with hashes. A web inspection records access to the source content; downloaded-original status applies only to files actually saved with a source manifest.

The workflow-research extension preserves the implementation plan and prior tool assessments. Its graphs and recipes record candidate routes and their specific handoff conditions. The source register distinguishes fresh inspection, earlier-report registration and preserved archived originals.

## Detailed procedures and effort classification

[Input requirements, documented software APIs and all 38 ranked workflows](workflows/details/README.md). The manual-effort and computing tables use independent ordinal scales and state each route’s comparison conditions.

## Action-by-action software and AI audit

[Detailed procedures, operation inventory and reviews](action-audit/README.md) cover all 77 original operations through 245 action definitions. The [38-route index](action-audit/workflow-to-actions.md) maps 220 original steps to their action contracts and explicitly lists eight additional audited operations. The [skill packaging map](action-audit/skill-to-actions.md) groups all 77 operations under the existing fifteen proposed skill names. [Source contract findings](action-audit/findings.md) preserve original contradictions and the detailed procedures' conditional clarifications. Per-point review records and check receipts state the observed evidence.

## Generic research and component research

1. This repository owns modeling methods, software/API findings, workflow contracts and generic tool evidence. FERME owns component specifications, originals, geometry inputs and component execution evidence.
2. Preserve exact URLs, dates, source labels and hashes. Link a general finding here to its component evidence in FERME when both subjects occur in one investigation.
3. [Separation preparation](repository-split-preparation/README.md) contains the dated file manifest, proposed extraction/move operations and script changes. Current modeling continues with its existing active paths.
4. [Preparation source register](sources/repository-separation-2026-11-13.json) and [proposal register](repository-split-preparation/ideas.json) record this batch independently of source-register generation used by ongoing work.
