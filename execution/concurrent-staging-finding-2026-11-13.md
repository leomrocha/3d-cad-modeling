# Concurrent staging finding

1. Observed commit: `73d83e5`, catalogue row binding batch. Its file list also contains `docs/examples/mast.md` and `skills/component-cad/references/envelope-job-runner.md`, which were already staged concurrently. The coordinator committed the shared index instead of restricting the commit to its batch paths.
2. Scope finding: the mast documentation belonged to another ongoing documentation batch; the envelope procedure belonged to the separate runner batch. Commit contents and history are preserved. Subsequent coordinator result commits specify exact paths with `git commit --only`.
3. Evidence: local `git show --stat 73d83e5` and its recorded pre-commit staged-file output. Executing coordinator: gpt-6.1-sol. This finding records the executed commit and makes no historical rewrite.

## Current procedure links

1. `skills/component-cad/references/envelope-job-runner.md` → [envelope job runner](../skills/cad-ocs-engineering/references/envelope-job-runner.md)
