# Local baseline

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Observed: 2026-11-12. Executing primary model identity is unavailable. Probe receipt: [local-inventory.json](local-inventory.json). Existing-source hashes: [local-evidence.json](sources/local-evidence.json).

## Existing assets to reuse

1. **OCS engineering skill:** `${CODEX_HOME}/skills/ocs-engineering/`. Inspected `SKILL.md` and `references/sources-and-capabilities.md`. The skill covers explicit model inputs, units, axes, component boundaries, live-session discovery, revision-bound changes, operation tracking, readback, geometry checks and verified save. It includes `scripts/ocs_control.py` and `scripts/check_contract.py`; their existence is observed, their execution is outside this research. The user reports partial success using this skill locally. Reuse this baseline when implementing the OCS integration.
2. **CAD skill research:** `${EOLIENNES_ROOT}/research/cad-workflow/skills-findings.md`. The 2026-10-20 report inspected six repositories: `earthtojake/text-to-cad`, `glotoff/freecad-skills`, `github/awesome-copilot`, `reyk/freecad-ai-skill`, `Foster1202/cad-modeling-fusion-skill` and `mitsuhiko/agent-stuff`. Original files and metadata remain under `${ENERGY_RAW_ROOT}/wind-prototypes/`. Historical popularity counts remain observations from that research date.
3. **OCS harness research:** `${EOLIENNES_ROOT}/research/cad-workflow/harness-findings.md`. It records a historical read-only observation of OCS 2026.42 and provides source and receipt locations. The new research reuses its workflow findings and separately inspects the current source checkout.
4. **Architecture research:** `${ARCHITECTURE_ROOT}/research/README.md` and local third-party source folders for Meshgen, AliceVision and Gaussian Splatting. These provide leads for the agents' current source assessment. Prior conversational suggestions in `discussion.md` are historical proposals.
5. **Building simulation project:** `${ENERGY_SIM_ROOT}/README.md` describes an IFC input route. This is a prospective consumer of architecture output. Its code and repository remain separate.

## Tool observations

1. `blender --version` returned **Blender 5.0.1**.
2. `openscad --version` returned **OpenSCAD 2021.01**.
3. Active Python is **3.12.9**. Module discovery found NumPy, SciPy, OpenCV and PyTorch. The receipt records each queried module and command. A Python module lookup describes this interpreter only; Blender embeds its own Python environment.
4. OCS source checkout: `${OCS_ROOT}`, revision `abad1b904577f4ea9d6d826c7143cad1eb5560bd`, clean at inspection. Its README describes native DWG/DXF workflows, kernel-backed solid commands and MCP/JSON automation. An installed executable's revision must be recorded by the future runtime experiment.
5. Host CPU: **Intel Core i7-1270P**, **16 logical CPUs**. `free -h` reported **30 GiB RAM total**, **13 GiB available** at the probe. This environment inventory supports a CPU-first benchmark proposal; future accelerator experiments should record the actual selected GPU and backend.
6. Git reports an unborn `master` branch. The foundation consists of new files; this task performs no staging or commit.

## OCS STEP export finding

The inspected `src/io/step.rs` declares `build_step(meshes: &[&MeshModel])`, extracts triangles and writes plane-based faces into a closed-shell/solid representation. The README calls STEP AP203 an export of 3D mesh data. This establishes the representation used by this source exporter. The proposed analytic-solid interchange test must inspect cylinders, topology, volume and dimensions after import, as well as the output extension.

Sources inspected in place:

1. `${OCS_ROOT}/README.md`, file-workflows table.
2. `${OCS_ROOT}/src/io/step.rs`, `build_step`, triangle collection and closed-shell writer.
3. `${CODEX_HOME}/skills/ocs-engineering/SKILL.md`, geometry readback and save requirements.

## Foundation files

At the initial foundation step, `AGENTS.md` was a byte-for-byte copy of `${FERME_ROOT}/AGENTS.md`. Its farm-robot and used-vehicle sourcing sections explicitly scope themselves to those tasks. The current request authorizes research spanning multiple open source applications; README records that project scope.

The later workflow-research batch adds the user’s standing documentation and before/after commit instructions to the copied rules; see [documentation-policy.md](documentation-policy.md).
