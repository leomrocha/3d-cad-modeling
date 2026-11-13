# 3D modeling

Skills, scripts, software integrations and reusable components for turning descriptions, ideas, photographs, dimensions, sketches and 2D drawings into 3D models.

The project serves architecture, robotics and other engineering uses. Its scope includes CAD solids and assemblies, meshes, point clouds, reconstructed scenes, building information models and simulation models. Each workflow must preserve source evidence, dimensions, units, coordinate frames, component boundaries and the meaning of its output geometry.

## Inputs and workflows

1. Text and dimensions → constrained sketches, parametric parts and assemblies.
2. Photographs and measured reference points → calibrated reconstruction and CAD remodeling.
3. Multiple photographs, video and depth scans → point clouds, meshes and scene reconstruction.
4. Sketches, floor plans and 2D CAD → interpreted dimensions, 3D geometry and building components.
5. Existing CAD and component libraries → reusable assemblies and application exports.
6. Models and assemblies → architecture workflows and robotics simulation, including MuJoCo.

## Open source tool scope

Research includes OpenCADStudio, Blender, MuJoCo, FreeCAD, Open CASCADE tooling, photogrammetry, Gaussian splatting and related open source software. Candidate software and skills are assessed through primary sources, licence terms, automation interfaces, geometry outputs and practical validation requirements.

## Repository

1. [skills/](/home/leo/projects/3dmodeling/skills/README.md) — shared modeling procedures and skill catalogue; keep reusable instructions here.
2. [scripts/](/home/leo/projects/3dmodeling/scripts/README.md) — shared modeling and inspection code; component recipes belong in FERME.
3. [tests/](/home/leo/projects/3dmodeling/tests/README.md) — shared-code tests; FERME owns component integration data and component-specific cases.
4. [research/](/home/leo/projects/3dmodeling/research/README.md) — generic methods, workflow/action contracts and sources; FERME owns component research and originals.
5. [execution/](/home/leo/projects/3dmodeling/execution/README.md) — tooling development evidence; FERME owns component execution records. Historical mixed files are covered by the split preparation.
6. `.git/` — local repository history. `.agents/`, `.codex/` and `.aws/` were empty environment directories at inspection; keep environment data outside tracked project content.
7. [AGENTS.md](/home/leo/projects/3dmodeling/AGENTS.md) — scoped working rules. [Component development plan](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md) — existing iteration plan and repository ownership.
8. [Separation preparation](/home/leo/projects/3dmodeling/research/repository-split-preparation/README.md) — proposed migration manifest, script changes and instructions for the continuing modeling agent. This batch prepares documentation; existing artifact and code paths stay in place.

## Current stage

The repository contains tool assessments and 245 action definitions covering all 77 recorded operations. The [seven-point procedure index](/home/leo/projects/3dmodeling/research/action-audit/point-index.md), [38 routes linked to actions](/home/leo/projects/3dmodeling/research/action-audit/workflow-to-actions.md), [15 proposed skill groups](/home/leo/projects/3dmodeling/research/action-audit/skill-to-actions.md) and [source contract findings](/home/leo/projects/3dmodeling/research/action-audit/findings.md) connect the research to detailed implementation specifications. Each action states existing software/API dependencies, agent and software responsibilities, inputs/outputs, checks, recovery and resource conditions. Review records and receipts identify executed document/source checks. Source intake, DXF inspection, model inventory and native geometry/placement helpers have implementation and execution records. The broader workflow catalogue retains its individual proposal statuses; component model/check records belong to the consuming project.

## Research records and changes

All project ideas, sources and workflow combinations are registered with original links and summaries. The [workflow map](research/workflows/README.md), [source register](research/sources/source-register.md) and [ideas register](research/ideas-register.md) provide the current records. Each authorized change batch has a starting checkpoint commit and a result commit; see [documentation policy](research/documentation-policy.md).
