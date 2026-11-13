# Skills installation guide completion — 2026-11-13

Coordinator: gpt-6.1-sol. Official-source inspection: publishing_research agent; actual research model identity unavailable.

## Requirement and changes

1. Document the skills CLI prerequisite Node.js >=22.20 with npm/npx, and Python 3.12 with venv/pip on Linux or macOS.
2. Provide project, global and local-checkout installation examples with the exact skill name, Claude Code target, installation scope and SKILL_ROOT assignment. Use separate Python environments for the selected skills.
3. Continue directly from installation to dependency installation and package checking. Attribute DXF commands to packages containing the helper.
4. Keep the installation sections in README.md and docs/index.md consistent. docs/PAGES.md identifies docs/index.md as editable Jekyll source; both guides are edited directly. Preserve the site's layout, configuration and image references.

## Reused audit findings

The earlier local audit passed required metadata, package hashes, packaged Python syntax, local package links, copy/symlink installation and registration checks for cad-ocs-engineering, cad-drawing-inspection and cad-source-intake. It identified the Node.js prerequisite and concrete installed-path setup as guide gaps. The source record below registers all seven original audit sources, including format, discovery, commands, prerequisites, telemetry and directory-listing evidence.

## Installation workflow and evidence

1. Inputs: current skill directories, guide shell examples, cached official CLI 1.8.1 and pinned dependency wheels. Outputs: installed packages and checker JSON in temporary directories. Python dependencies are installed with pip into fresh Python 3.12 environments.
2. Tools: npx, official skills CLI, Python venv/pip and each installed package_check.py. Geometry representation, units and frames are unchanged by installation. Runtime source files, hashes, licences and dependency pins are preserved.
3. Check all three skills across project/global/local-checkout examples in copy and symlink modes. Target Claude Code for copy mode; target Claude Code and Codex together for symlink mode. The CLI selects copy for a single target even when --copy is omitted.
4. The test substitutes a local snapshot for the remote owner/repository argument and uses cached CLI/dependency software. HOME, configuration and installation locations are temporary; telemetry is disabled. The remote fetch and public directory listing retain their separate evidence.
5. Downstream operation: source intake, DXF inspection or component CAD using the installed package. CAD operations require the caller's existing OCS session; the installation gate runs without a live CAD mutation.
6. Portable runtime roots: SKILLS_CLI_ROOT identifies the caller-selected cached CLI installation; NATIVE_READER_ROOT identifies the existing pinned Python dependency directory; temporary artifacts use a caller-selected temporary root. Documentation stores repository-relative file paths.

## Sources and detailed results

[Attributed source records](../research/sources/skills-compliance-2026-11-13.json) retain original URLs, titles, summaries, observation dates, evidence status and referring documents. Both combined source indexes retain the merged observations.

[Executed checks](skills-installation-guide-2026-11-13.json) record exact outcomes and hashes for the checked guide commands.

## Executed result: DONE

1. All 18 installation cases pass: three skills × project/global/local-checkout scope × copy/symlink mode. Each case creates a fresh Python environment, installs packaged dependency pins with pip and runs the installed package checker.
2. The final guide sections match between README.md and docs/index.md; 16 shell examples pass syntax checks and 35 local links resolve. Seven source records pass merge consistency checking. Existing source IDs and observations are preserved.
3. Final batch-snapshot verification: PASS; 20 tests pass and one optional live OCS state check is skipped because it requires a caller-selected descriptor. Synchronisation, registrations and isolated fixture execution pass.
4. Current-worktree verification during this batch: FAILED because the concurrent untracked scripts/annular_job_runner.py and its CAD package manifest/copy were not synchronised. That implementation belongs to concurrent work. Batch verification used tracked HEAD plus the authorized guide/source-register files and preserved the concurrent runner unchanged.
5. The original audit's two guide gaps are resolved by these changes. Public remote acquisition retains the earlier Cache miss observation; tested installation inputs are the current local package snapshot.
