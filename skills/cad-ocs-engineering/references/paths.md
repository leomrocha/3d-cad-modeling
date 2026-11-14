# Installed package and caller paths

1. SKILL_ROOT identifies this installed skill folder. Load code from its scripts directory and keep the package intact.
2. PROJECT_ROOT, SOURCE_ROOT and JOB_ROOT are caller-supplied locations for job inputs, unchanged sources and persistent outputs. Supply absolute paths at runtime.
3. Stored locators use `${ROOT_NAME}/relative/path`. Resolve them with explicit `--root ROOT_NAME=ABSOLUTE_PATH` inputs where supported. Reject unresolved roots and path escapes before file access.
4. Keep stored job records portable. Record original hashes and a separate derivative hash when normalizing paths. Installed examples use synthetic values; real dimensions and source evidence come from the caller.
