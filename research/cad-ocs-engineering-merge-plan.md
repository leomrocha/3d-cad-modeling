# Complete CAD OCS Engineering merge

Date: 13 November 2026. State: DONE. Execution authorized: merge the complete original OCS engineering skill and every component-cad addition into `skills/cad-ocs-engineering/`. Both workflows are merged directly into the main `SKILL.md`.

1. Inspect concurrent changes, record hashes and create the local checkpoint.
2. Inventory every original OCS file and every component package file; record each destination.
3. Include the original OCS instructions, all references, both helpers and agent metadata; normalize stored paths and retain provenance.
4. Preserve all repository additions: component iteration, source readiness, drawing interpretation, geometry helpers, assemblies, native readers, verification and cleanup.
5. Merge both sets of workflow instructions directly in the main entrypoint. Preserve detailed procedures and supported conditions inside the same skill directory.
6. Use the single package identity `cad-ocs-engineering`; retain `cad-drawing-inspection` and `cad-source-intake` as the other independently installable packages.
7. Keep canonical shared code in `scripts/`; generate package copies from authorized committed code and keep caller inputs explicit.
8. Update active documentation, links, metadata, generator and tests. Preserve historical identities with current locators.
9. Verify source-section coverage, retained files, references, isolated CLI installation, imports, fixtures, regression checks and read-only OCS access.
10. Review explicit staged paths and create the local result commit, preserving concurrent work and ignored private files.

[Source inventory](sources/cad-ocs-engineering-merge-2026-11-13.json). [Execution results](../execution/cad-ocs-engineering-merge-2026-11-13.md).
