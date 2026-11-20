# Modeling tool tests

1. Purpose: verify shared functions with tracked fixtures.
2. Current suite command: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py'`. Use the existing Python environment containing the pinned native-reader dependencies.
3. Run the suite from the repository root. For native geometry tests, use the Python environment with the dependencies listed in [requirements-native.txt](../requirements-native.txt).
4. The bearing, CAD edit, sketch, two-view, orthographic, mesh-position and saved-body regression inputs are tracked under `tests/fixtures/`. Their tests resolve fixture paths from the test file. Some tests require optional CadQuery, SolveSpace, Open3D or native-reader dependencies.
5. Report executed tests, failures and skipped integration cases separately. Preserve recorded case results in their caller-owned location and generic regression evidence here.
6. `test_skill_package_build.py` always checks current package synchronisation and exercises helper creation, changes, deletion, transitive imports, unassigned files and completion failure propagation using temporary fixtures. Run `python3 scripts/build_skill_packages.py --finalize` after reusable tooling changes, and `--verify` for final validation with `SKILLS_CLI_ROOT` and `NATIVE_READER_ROOT` supplied. Completion requires the isolated installation suite; skipped prerequisite-dependent installation checks cannot produce a completion PASS.
7. Package registration checks cover helper and procedure catalogue entries.
