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



### Preflight an ancestor layer change

Record the full occurrence paths for every requested role group before changing any layers. In memory, substitute only the proposed ancestor INSERT layers and rebuild the occurrence tree. For each new control layer, retain the actual colour and flag profile of its corresponding source layer. Use `verify_ancestor_appearance` in [layer_isolation.py](../scripts/layer_isolation.py) to check all uses of edited definition handles against the authorized scope. Compare effective RGB, layer and visibility blockers across the full tree, including hidden references and descendants on raw layer 0. Pass only explicitly approved effective layer changes. Compare native records, block membership, world placement and normal visible membership separately.

Use `plan_exact_isolation_masks` on the proposed full dependency sets and the original named groups. Include every raw and effective ancestor layer and each leaf layer in its dependencies. For each group the helper keeps only the enabled layers required by its paths. It reports missing and extra paths across the named groups. Check the whole assembly role and each named subgroup separately before applying the existing transition procedure.

### Transition between isolated groups

1. Verify and save the styled checkpoint in normal visibility before isolation. Pin the session, owned document, native layer identities and complete original flags. For each requested group, derive the required layer set from every ancestor and leaf in the full occurrence paths. Reject a candidate state that would hide a requested leaf or reveal another physical or protected reference path.
2. For several groups in one exclusive ownership interval, carry the last verified isolation state forward. [The transition planner](../scripts/layer_isolation.py) takes the original flag table, the observed full table, the preceding hidden layer identities and the next hidden layer identities. Both sets contain only layers whose original flags were on and thawed. It fails on any unexpected flag or missing layer and emits only the differing off-flag writes, with their expected values. Apply them under the verified owned session, document and revision. Hiding changes precede enabling changes.
3. Give each write a stable journal label for its transition and native layer. Resolve an uncertain request under its original ID and verify the resulting live flag before planning or writing another transition. On a terminal failure, stop and reconcile the exact live table and journal with the last verification and the saved styled checkpoint. Do not treat a partial transition as verified or save it as the final appearance.
4. Verify the complete expected flag table, exact visible occurrence paths and effective appearance after each transition. Only then use it as the preceding state. After the last group, pass an empty target to restore the original flags once. Verify the complete restored flag table, original visible paths, effective appearance and retained geometry before the final save. Isolating one group at a time and restoring between groups remains valid.
5. Multiple updates in a single record edit do not establish a multi-record batch capability. Use a provider batch only after qualifying its exact transport, schema, per-step commit evidence and same-request recovery. Do not use a bulk visibility command that changes unrelated flags or silently skips unresolved layer identities.

### Preserve hidden references during a style revision

1. Inventory physical solids and reference solids separately. When reference geometry has no leaf role metadata, use its exact source definition and full occurrence path to identify it. Preserve its recorded purpose and keep its leaves on a reference layer separate from the working parts.
2. Calculate visibility along the entire occurrence path. A visible leaf layer cannot display a solid beneath a hidden or frozen parent insert. Record the controlling parent layer and its initial flags. Retain this hidden state in the delivered model unless the job calls for displaying the reference.
3. Verify physical group isolation against the visible occurrence paths. Record a hidden reference as preserved when its parent flags, leaf assignments, geometry and transform match the requested state. To inspect that reference on demand, enable its controlling parent and leaf in an owned viewing session and restore the original flags afterward.

### Recover missing part labels during a style revision

1. Use a construction receipt that binds the role to the exact source drawing and handle, or a recorded lineage from that drawing to the current occurrence. Verify the full occurrence path, owning definition and placement. Equal handle strings in separate drawings do not establish identity.
2. When the current solid lacks a source label, copy the recorded role into its source metadata on the owned revision. Retain existing source labels. Native layer membership supplies isolation, while the source metadata preserves the part identity and its receipt link.
3. Read the label back before saving. Compare solid payloads, occurrence transforms and block membership before and after the display and metadata edits. Verify the live layers and exact saved file independently. Preserve the source role and model hash in the repair receipt.

## Verify operation evidence

1. Use the selected session's capabilities, command registry and installed schemas to identify operations, geometry types and properties. Record the installed binary version and retain the corresponding responses.
2. Verify the authorized operation with readback. Use a three-dimensional intersection check for solid collision and record the measured result. Record appearance properties and physical material properties under their respective fields.
3. Audit the document and verify the saved geometry using the requested output format and fidelity checks.
