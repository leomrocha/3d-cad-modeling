# Contributing and editing documentation

[Documentation](README.md) · [Project](../README.md)

## Editing pages

1. Edit the Markdown page for the subject. Keep the project README as the introduction and docs/README.md as the documentation index.
2. Link related pages using repository-relative paths so the links work in a GitHub checkout.
3. Give images readable captions and alt text. Record each copied image's original source, date and hash in the asset manifest.
4. Preserve factual status: executed results, source claims, measured values and workflow proposals retain those labels.
5. Describe the component, action, inputs and resulting geometry directly. Keep dimensional values beside their units and source.

## Code and evidence

1. Shared tools receive project-specific values and paths as inputs. Application geometry and component job evidence stay with the consuming project.
2. Reuse existing code and models before constructing replacements. Preserve source originals and record derivatives separately.
3. Run checks for the changed behavior. Separate generic regression tests from integration checks requiring an external model or fixture.
4. Record the exact model/tool revision behind an execution claim and retain failed attempts with their job evidence.

## Documentation checks

1. Resolve every local page and image link.
2. Check that image copies match the registered hashes.
3. Check that proposal pages and executed examples have their stated evidence.
4. Preserve third-party attribution and the [MIT license notice](../LICENSE).

[Modeling workflow](modeling-workflow.md) · [Source records](sources.md)
