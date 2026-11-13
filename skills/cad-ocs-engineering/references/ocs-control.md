# OCS control

Initial live evidence: OCS 2026.42, Linux, 2026-10-20. Native control works even without MCP tools exposed in this chat. Existing session descriptors under OCS configuration (normal or Snap) contain a session ID, local port and private token. Never print tokens. Do not launch another editor/headless process or change connection settings to evade a connection failure.

The bundled helper:

```bash
python "$SKILL_ROOT/scripts/ocs_control.py" discover
python "$SKILL_ROOT/scripts/ocs_control.py" read --session SESSION --request '{"op":"capabilities"}'
python "$SKILL_ROOT/scripts/ocs_control.py" read --session SESSION --request '{"op":"commands","name":"BOX"}'
```

Use `--descriptor DESCRIPTOR_JSON` for a known descriptor when discovery does not find it. Loopback can require sandbox escalation; that permission is separate from drawing-mutation authorization. A socket permission failure does not prove OCS is closed.

For an authorized write, inspect the installed schema first. A request file must contain exact `document_id`, `revision`, `request_id`. The helper checks current state and sends once; it does not infer authorization or create geometry:

```bash
python "$SKILL_ROOT/scripts/ocs_control.py" execute --session SESSION --request-file REQUEST_JSON --allow-write
```

It never starts OCS, removes stale descriptors, automatically retries or saves a drawing. The explicit request can still mutate the drawing: inspect it before sending.

## Protocol requirements

1. Read `state`, `capabilities`, document header/units and existing contents first. Bind edits to selected session/document/revision.
2. Read `commands`, `entity_schema`, `record_schema` for unfamiliar operations. Use observed response shapes, not guessed CAD methods.
3. Native control exchanges newline-delimited JSON. The helper adds `protocol:1`, session ID and token, keeping authentication out of output.
4. Timeout: inspect `operation` using the same request ID. Batches require checking completed steps. Unknown completion is not permission to repeat.
5. `running`/`waiting_input` require following operation/command state; do not feed guessed interactive answers or claim completion.
6. A definitive stale-state rejection permits refreshing and reconsidering the edit, not blind batch replay. Establish that a write did not commit before issuing a new identity.

## Evidence limits

- Registry includes Solid3D/ACIS, Mesh, layers, groups, blocks and appearance materials. No parametric feature tree, constrained mechanical assembly, physical-material model or general solid-clearance query was established.
- Manifest advertises `BOX`, `SPHERE`, `EXTRUDE`, `UNION`, `INTERFERE`, `MASSPROP` and other 3D commands. None were executed in initial research. Verify an authorized operation before depending on it.
- Material schema contains render properties; `MATERIAL` command search returned nothing. Creating/assigning render materials remains to be verified through installed schema. Appearance is not density/stiffness.
- Planar-curve intersection and XY filters are not 3D collision tests. An `INTERFERE` command name is not a verified numeric result.
- Audit and verified save are documented, but fidelity is target-specific. No conversion is implicit.

Original API/receipt evidence: `${ENERGY_ROOT}/heoliennes/research/cad-workflow/harness-findings.md`. Local source revision is not installed-binary revision.
