# Preserve raw CAD history by job and revision

Place the raw request and response JSON, JSONL journal, checkpoints, failed attempts, debug logs and related evidence for each job revision in its own history directory. Keep relative subdirectory names so repeated receipt names remain distinct. Finish writing that revision before archiving. Give each new or resumed revision its own identity and output filename.

Run the [history archive helper](../scripts/job_history_archive.py) with the source directory and a new output path outside it. Use persistent caller-owned storage.

```sh
python3 "$SKILL_ROOT/scripts/job_history_archive.py" create "$HISTORY_DIR" "$ARCHIVE_DIR/$REVISION.tar.bz2" --job "$JOB" --revision "$REVISION"
python3 "$SKILL_ROOT/scripts/job_history_archive.py" inventory "$ARCHIVE_DIR/$REVISION.tar.bz2"
```

Creation preserves the input files, verifies the compressed stream, reads every payload and compares file paths, byte counts and SHA-256 digests with the embedded manifest. It publishes the verified archive exclusively. Inventory repeats the readback and returns the embedded job, revision and member manifest without extracting files. Pin the archive path, its SHA-256 and revision identity in the handoff. When a revision already has an archive, inventory that archive and compare its manifest with the intended revision. Retain earlier archives and create a separately named revision for changed evidence.
