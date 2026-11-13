# Existing-model reconciliation and mandatory start check

1. Checked all 103 component entries against 43 model/reference files. Thirteen entries have matching existing 3D files and are DONE.
2. Corrected four stale statuses: ME0907 motor (C005), Sumitomo PRO-M (C010), Sumitomo PRO-L (C011), BMW module (C022). The existing CAD and recorded checks are reused.
3. FERME list and file links (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/README.md`). Complete before/after evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/audit.json`).
4. [Reusable start check](../scripts/model_inventory.py) reads all observed model path fields, input-sheet links and actual files. Ten tests cover stale status, file discovery, dependencies, 2D references and completed-record preservation.
5. The [component skill](../skills/cad-ocs-engineering/SKILL.md) and project instructions require this check before each start. C001 — Trelleborg T539 tyre is the next manifest entry whose actual-file lookup returns NEW_MODEL_REQUIRED.
6. Executing model: gpt-6.1-sol. Checkpoints: 3dmodeling `51ac0cf`, FERME `e3cac14`.
