# Portable paths

[Documentation](README.md) · [Tools](tools.md)

1. Markdown links within this repository are relative to the page containing the link.
2. Stored cross-project source locators use named roots, such as `${FERME_ROOT}/engineering/...`. Configure the root for the checkout being used.
3. Commands use shell variables for those roots. In JSON, `${ROOT_NAME}` is a locator placeholder; the consumer resolves it using its configured root map before opening the file.
4. Source IDs and hashes identify the originally registered revision. Normalized example copies record their own hash and the path-only transformation separately.

## Root names

1. **MODELING_ROOT:** this repository checkout.
2. **FERME_ROOT:** the consuming mechanical project checkout.
3. **EOLIENNES_ROOT / ENERGY_RAW_ROOT / ENERGY_ROOT:** wind research, original source archive and energy project checkouts.
4. **OCS_ROOT:** the OpenCADStudio source checkout.
5. **ARCHITECTURE_ROOT / ENERGY_SIM_ROOT / CASA_ROOT:** architecture and building-simulation checkouts.
6. **NIGHTLIGHT_ROOT / COCOLECOQ_ROOT:** other recorded project checkouts.
7. **PROJECTS_ROOT:** parent directory for other recorded sibling projects.
8. **CODEX_HOME / AGENT_SKILLS_ROOT:** local agent configuration and skill locations.
9. **NATIVE_READER_ROOT:** directory containing the existing native-reader dependencies.
10. **TEMP_ROOT / USER_HOME / SYSTEM_ROOT / SOURCE_ROOT:** temporary workspace, user directory, system-file root and caller-supplied source directory.

## Running a local reader test

Use the existing environment containing the dependencies, or set NATIVE_READER_ROOT to their directory. The test derives its temporary-directory fallback through Python's tempfile API.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_small_bms.py
```
