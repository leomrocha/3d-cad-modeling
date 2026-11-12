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

## Evidence and execution

Three research tasks were dispatched with model parameter `gpt-6-luna`: `cad_skills`, `reconstruction` and `domains_components`. Their reports contain source links and retrieval outcomes. Runtime model identifiers were not exposed to the agents; the dispatcher model parameter is recorded separately from actual runtime identity.

Primary-agent work includes local repository/source inspection, version and module-discovery probes, foundation creation, review of agent reports and synthesis of the proposed implementation plan. The existing OCS skill's partial runtime success is user-reported. Geometry experiments and installation steps in the plan describe proposed implementation work.

Web pages were inspected by the delegated research agents. Existing local originals are referenced in place with hashes. A web inspection records access to the source content; downloaded-original status applies only to files actually saved with a source manifest.

The workflow-research extension preserves the implementation plan and prior tool assessments. Its graphs and recipes record candidate routes and their specific handoff conditions. The source register distinguishes fresh inspection, earlier-report registration and preserved archived originals.

## Detailed procedures and effort classification

[Input requirements, documented software APIs and all 38 ranked workflows](/home/leo/projects/3dmodeling/research/workflows/details/README.md). The manual-effort and computing tables use independent ordinal scales and state each route’s comparison conditions.
