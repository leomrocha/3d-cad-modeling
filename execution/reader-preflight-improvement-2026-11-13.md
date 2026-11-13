# Saved-body reader runtime preflight

Date: 13 November 2026. Procedure update: gpt-6-luna. Coordinator review/import check: gpt-6.1-sol.

The [envelope procedure](/home/leo/projects/3dmodeling/skills/component-cad/references/envelope-reference.md) now checks parser imports in the exact interpreter and environment selected for saved-body inspection before native writes. This addresses the recorded import failure after a successful component save/reopen. Recovery reused the saved artifact and performed a read-only check in the existing parser environment; [the executed component record](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/c055-build-01/execution-status.json) is in FERME commit `133dd29`.

Coordinator import check: `parse_sab` and `SabDataLoader` import successfully from the existing ezdxf 1.4.5 environment. Skill validation passes. [The source/check record](/home/leo/projects/3dmodeling/research/sources/reader-preflight-improvement-2026-11-13.json) contains the exact procedure hash and execution conditions.
