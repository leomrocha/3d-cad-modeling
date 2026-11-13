---
name: source-intake
description: Record a new job's exact request, source identities, file hashes, corrections and scope as a protected revision using local files and supplied text or URLs.
---

# Record source files, revisions and job scope

Use for **Preserve the input revision and state the job boundary (INTAKE-A01)**. Read the existing job record first. Reuse a completed intake whose request, source observations and scope match the current task. A changed source or instruction creates a new revision referring to the completed prior index.

## Prepare the input

1. Read the request and source records. Supply a readable `job_name`, unique `revision_id` and actual agent `model` identity where available. `request.text` preserves the exact request; `request.location` identifies its message/document location.
2. Supply `scope.statement`, `scope.requested_output` and absolute `scope.authorized_paths`. The agent writes these from the actual authorization. Software preserves the statement; it does not decide the task's authorization.
3. Every `sources` entry has `id`, `title`, a concrete `summary`, `kind`, exact `locator` and ISO `observed_at`. Supported kinds: `file` with an absolute local path; `text` with an exact `text` field; `url` with the original HTTP(S) URL. File and text sources may supply `expected_sha256` to pin expected bytes.
4. Optional `parent_id` points to another source in this revision. Optional `corrections` entries contain `id`, `source_id`, exact `statement` and `location`. Optional `conflicts` contain at least two distinct `source_ids`, a `summary` and `affected_scope`. Retain the source's declared evidence fields; the tool records actual observation state separately.
5. Optional `prior_revision` is the absolute path to an earlier completed `source-index.json`. The tool verifies that prior index and scope against their receipt, checks job identity, and requires a new revision ID. Changed bytes and changed locators are recorded independently.

## Execute

```sh
python3 ${MODELING_ROOT}/scripts/source_intake.py \
  --input ${SOURCE_ROOT}/job-input.json \
  --output ${SOURCE_ROOT}/new-intake-directory
```

1. Reuses `part_index.parse_json` for duplicate-key/nonfinite-token rejection and `component_records.observe_file` for streaming hashes with change detection. Additional validation checks references, cycles, dates, required scope fields and overflowing numeric input.
2. Reserves the requested new output directory exclusively. Existing completed and incomplete attempts are preserved.
3. Writes a staged source index, scope Markdown and receipt. Validates the artifact hashes, then atomically publishes the `revision` subdirectory. Files are `revision/source-index.json`, `revision/scope.md`, and `revision/receipt.json`.
4. A source conflict or I/O/publication failure after reservation leaves `failure.json` and an `incomplete` directory under that attempt. Inspect the named failure. Corrected input uses a new output path; an existing attempt is preserved.
5. Exit codes: `0` completed; `1` source observation/hash conflict; `2` invalid input or other I/O/publication failure. A supplied URL is registered locally with `network_requests: 0`.

## Check and hand off

1. Call `source_intake.verify_revision(path_to_source_index)` to verify the completed index/scope hashes against the receipt.
2. The agent compares the recorded request, scope, corrections and affected source conflicts. Numerical capture checks establish source identity and output integrity. Source interpretation retains its own action.
3. Hand the completed revision to **Select the execution mode and define candidate branches (INTAKE-A02)**. Preserve the source/revision IDs in its inputs. Required source-priority decisions affect the named dependent feature.
4. The [actual executed input](../../execution/source-intake/job-input.json), [published index](../../execution/source-intake/live-01/revision/source-index.json) and [execution report](../../execution/source-intake.md) document the exercised interface.

## Verification

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s ${MODELING_ROOT}/tests -p test_source_intake.py
```

The cases cover actual file hashes and source preservation, exact Unicode/text/corrections, zero-network URL registration, new source revisions, equal bytes at distinct locators, invalid references/cycles, duplicate keys and overflowing numbers, pinned-source conflicts, changing files, interrupted publication and prior-artifact protection.
