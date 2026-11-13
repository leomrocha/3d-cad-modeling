# Complete a reusable skill or script change

This development operation runs from the 3D CAD Modeling source repository root after an authorized reusable tooling change. The source repository owns `scripts/build_skill_packages.py` and its tests. The installed skill carries its runtime code.

1. Keep component recipes, dimensions and model artifacts in the component project. Put generic Python helpers under the source repository's `scripts/` directory. New helpers there are automatically assigned to the full CAD package; source-intake and drawing-inspection also receive the transitive local imports of their entry points. Package manifests record source paths and hashes. Build-only code is explicitly excluded by the builder's `HOST_ONLY` declaration.
2. Supply `SKILLS_CLI_ROOT` for an existing skills CLI package and `NATIVE_READER_ROOT` for the existing pinned Python dependency directory. These runtime paths are caller inputs. Use the repository's Python test environment.
   Register each reusable helper in `docs/tools.md` and each procedure referenced by the main skill in `skills/README.md`. Add attributed source observations under `research/sources/` and merge them into the combined source indexes with `python3 research/tools/build_workflow_register.py --date YYYY-MM-DD --source-record research/sources/RECORD.json` from the source repository root. Supply the actual client date. The merge retains source IDs and original observations. Completion checks fail when catalogue entries or source observations are missing.
3. After creating, modifying or deleting helpers or changing package dependencies/instructions, run:

   ```sh
   python3 scripts/build_skill_packages.py --finalize
   ```

   This regenerates the packages, checks their generated indexes and runs lifecycle and isolated installation checks. It uses temporary installations with telemetry disabled. It fails when required test inputs are absent or a check fails. Existing `--cli-root` and `--reader-root` arguments can supply those paths explicitly. A caller-selected `OCS_DESCRIPTOR` enables the additional read-only OCS state test.
4. Before reporting completion, run the read-only final validation:

   ```sh
   python3 scripts/build_skill_packages.py --verify
   ```

   This rejects skipped synchronisation and repeats the required checks. Ordinary unittest discovery also checks current package/source synchronisation. Source changes arriving during validation cause the final synchronisation check to fail.
5. Record the operation's actual result. Include the canonical changes, generated files and manifests in the same authorized result batch. Preserve concurrent changes and coordinate another writer's unfinished helper before regenerating its distribution. Apply the source repository's checkpoint and staging rules.

Development command reference: [package builder](https://github.com/leomrocha/3d-cad-modeling/blob/master/scripts/build_skill_packages.py).
