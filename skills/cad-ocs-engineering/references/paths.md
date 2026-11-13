# Installed skill and caller-owned paths

1. `SKILL_ROOT` is the installed cad-ocs-engineering directory containing `SKILL.md`. Resolve its bundled code from `SKILL_ROOT/scripts`; keep the package intact.
2. `PROJECT_ROOT`, `SOURCE_ROOT` and `JOB_ROOT` identify caller-owned project, source and job locations. Supply absolute runtime values when invoking helpers. Historical component examples use `FERME_ROOT` for their owning project.
3. Stored job locators use `${ROOT_NAME}/relative/path`. Pass every referenced root through repeated `--root ROOT_NAME=ABSOLUTE_PATH` arguments where supported. Python callers resolve those locators before passing source paths to readiness checks. A root map provides data locations.
4. Keep portable locators in saved documentation and metadata. Normalize runtime paths before retaining records. Preserve original source hashes when recording a normalized derivative.

5. `ENERGY_ROOT` identifies the external archive referenced by the original dated OCS capability records. These locators preserve source provenance. The installed skill carries its control code, modeling instructions and dependency declarations.
