# Validate an installed skill package

1. Keep this package's scripts, references, requirements, license and package-manifest.json together. The manifest records bundled script hashes.
2. Use an isolated Python 3.12 environment with the pinned requirements.txt dependencies. Run `python "$SKILL_ROOT/scripts/package_check.py"` to verify manifest hashes, imports, dependency versions and native-reader availability.
3. Import reusable modules from this package's scripts directory. Supply source data, output paths, session and job namespace as runtime arguments. Offline imports make no native connection.
4. With an explicitly selected running native session, add --session SESSION or --descriptor DESCRIPTOR_JSON for a read-only connection check. Keep descriptor credentials private.
5. Check local Markdown links resolve inside the installed package and that a copied installation works from an unrelated working directory. Run focused synthetic geometry/recovery cases independently of any real component job. Report actual checks and native execution separately.
