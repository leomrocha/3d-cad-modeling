# Portable path cleanup

Date: 13 November 2026. Executing model: gpt-6.1-sol.

1. Request: remove machine-specific absolute paths throughout repository content.
2. Converted repository-local Markdown links to page-relative links. Converted external source locations, tool locations and temporary paths to documented named-root locators.
3. Removed the native-reader test's fixed temporary path; it accepts NATIVE_READER_ROOT and derives its fallback with tempfile.
4. Preserved source IDs and original-source hashes. Example copies whose metadata changed have updated copy hashes and an explicit path-normalization status.
5. Preserved pre-existing prose and ongoing modeling edits. The commit contains only the cleanup changes and its documentation.
6. Checks: portable-path-cleanup-checks-2026-11-13.json.
