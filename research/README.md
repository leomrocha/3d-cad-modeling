# Research and proposed implementation

Research date: 12 November 2026.

1. [Implementation plan](implementation-plan.md) — input routes, model representations, software layers, 15 proposed workflow skills, component schema, six implementation stages and verification criteria.
2. [CAD tools and available skills](cad-and-skills.md) — OCS, FreeCAD, CadQuery, build123d, OpenSCAD, Blender, SolveSpace, OCCT, drawing intake and existing skills.
3. [Image, video and scan reconstruction](reconstruction.md) — photogrammetry, control points, point clouds, Gaussian scenes, learned reconstruction and CAD remodeling.
4. [Architecture, robotics and components](domains-and-components.md) — IFC/Bonsai, MuJoCo/MJCF, URDF, collisions, source libraries, licences and metadata.
5. [Local baseline](local-baseline.md) — existing OCS skill, prior research, tool versions and OCS exporter source inspection.
6. [Local inventory receipt](local-inventory.json) and [existing-source hashes](sources/local-evidence.json).
7. [User-supplied links](user-supplied-links.md) — all nine supplied URLs mapped to their assessment.
8. [Skill catalogue](../skills/README.md) — reuse candidates and proposed project workflows.
9. [Verification receipt](verification.json) — copied instructions, local source hashes, link coverage and document checks.

## Evidence and execution

Three research tasks were dispatched with model parameter `gpt-6-luna`: `cad_skills`, `reconstruction` and `domains_components`. Their reports contain source links and retrieval outcomes. Runtime model identifiers were not exposed to the agents; the dispatcher model parameter is recorded separately from actual runtime identity.

Primary-agent work includes local repository/source inspection, version and module-discovery probes, foundation creation, review of agent reports and synthesis of the proposed implementation plan. The existing OCS skill's partial runtime success is user-reported. Geometry experiments and installation steps in the plan describe proposed implementation work.

Web pages were inspected by the delegated research agents. Existing local originals are referenced in place with hashes. A web inspection records access to the source content; downloaded-original status applies only to files actually saved with a source manifest.
