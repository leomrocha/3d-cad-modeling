# OCS control

Discover running OpenCADStudio sessions with the bundled helper. The helper reads existing session descriptors from the OpenCADStudio configuration directories, including Snap installations. Use the selected session ID to read the installed capabilities and the schema for the required command. Keep descriptor tokens out of output. Use the current editor and connection settings.

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


## Verify layer isolation and restoration

1. Read the live layer table and the matching layer records. Pin the drawing identity, layer handles and original visibility flags. Resolve effective layers through visible assembly occurrences, including nested block instances.
2. Use the installed writable property path. In deployments whose layer record stores visibility as `properties.flags.off`, pass `/flags/off` to `set_properties` and obtain the expected Boolean from that record. The summary returned by `layers` can expose `off` at the top level. Its summary shape does not define the write path.
3. On the owned drawing, isolate one requested group at a time. Toggle only the selected layer flags and verify the resulting enabled layer set and affected occurrence paths. Restore the original flags and verify the complete layer table before the final save and native preview.
4. Save the verified style checkpoint before isolation. If visibility verification fails, recover from that exact save and inspect the current schema before changing any flags. Reuse the saved geometry and compare solid payloads, occurrence transforms and definition membership with the original.


## Verify operation evidence

1. Use the selected session's capabilities, command registry and installed schemas to identify operations, geometry types and properties. Record the installed binary version and retain the corresponding responses.
2. Verify the authorized operation with readback. Use a three-dimensional intersection check for solid collision and record the measured result. Record appearance properties and physical material properties under their respective fields.
3. Audit the document and verify the saved geometry using the requested output format and fidelity checks.
