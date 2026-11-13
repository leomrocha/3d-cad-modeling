# Retained 2D drawing role in model inventory

Date: 2026-11-13. Implementation and verification: gpt-6.1-sol. Component observation: gpt-6-luna.

1. Retaining the existing Category 1 interface DWG in a component evidence packet moved its copy outside the `2d_schemas` directory. The previous inventory classified that copy as `3d_model_file` by its extension and directory.
2. `scripts/model_inventory.py` now groups the known `2d_schemas` references by SHA-256. A byte-identical copy inherits `2d_reference` and records its original reference paths and role basis. Distinct native model bytes retain their existing role. The helper reads files and changes no CAD artifact.
3. Twenty-nine model-inventory tests passed, including two new behavioral cases: a retained 2D copy remains a reference even when the component manifest links it; a distinct attributed component model still returns `SKIP_EXISTING_MODEL` beside a known 2D reference.
4. Live filesystem inspection found the retained C063 reference with SHA-256 `d87312c30cbc3a0eceb92542a08e544b14847487341609af7393cb9f362d506e`. Its role is now `2d_reference`, attributed to the unchanged original in `${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/iso730-category-1-interface-reference.dwg`. The original and retained copy were read without opening OCS.
