# Modeling tool tests

1. Purpose: verify shared functions with synthetic fixtures and supported native geometry cases. Native case data is caller supplied.
2. Current suite command: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s ${MODELING_ROOT}/tests -p 'test_*.py'`. Use the existing Python environment containing the pinned native-reader dependencies.
3. Optional native cases use explicit `CAD_NATIVE_FIXTURE_ROOT`, `CAD_SCALED_ASSEMBLY_FIXTURE` and `CAD_TABBED_CASE_FIXTURE` directories. Source geometry and expected native results retain their pinned hashes. Ordinary synthetic checks use no sibling-project default.
4. The current smallBMS test also uses C054 files in execution and a temporary native-reader path. These tests and ongoing fixes retain their current locations during preparation.
5. Report executed tests, failures and skipped integration cases separately. Preserve recorded case results in their caller-owned location and generic regression evidence here.
6. `test_skill_package_build.py` always checks current package synchronisation and exercises helper creation, changes, deletion, transitive imports, unassigned files and completion failure propagation using temporary fixtures. Run `python3 scripts/build_skill_packages.py --finalize` after reusable tooling changes, and `--verify` for final validation with `SKILLS_CLI_ROOT` and `NATIVE_READER_ROOT` supplied. Completion requires the isolated installation suite; skipped prerequisite-dependent installation checks cannot produce a completion PASS.
7. Package registration checks cover helper and procedure catalogue entries.
