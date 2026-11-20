# Repository audit

Before committing, audit the staged files with `python3 maintenance/check_repository.py --index`.
Before merging, audit the proposed commit with `python3 maintenance/check_repository.py --commit REV`.
The **Repository audit** pull-request workflow checks the proposed merge commit and runs the audit tests.

The audit checks all tracked paths and reads text from the selected Git index or commit.
It resolves relative Markdown and HTML file links within that snapshot and runs the existing package synchronization check against the snapshot's package inputs.
Calendar dates, private references, historical instructions, missing local link targets and stale generated copies fail the audit.
Every recognized copyright year, protocol version date and standards edition is reported as `REVIEW`.
Review these entries against the source attribution or specification. They are excluded from the blocking calendar-date count.

Compare operating examples with the actual command arguments and run affected behavior tests separately.
Run the package verification procedure for skill and helper changes. [Package completion procedure](../skills/cad-ocs-engineering/references/package-completion.md).
