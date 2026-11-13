# Concurrent skill publishing and implementation

Instruction recorded 13 November 2026. Coordination: `gpt-6.1-sol`; implementation agents: `gpt-6-luna`.

1. **User instruction:** preserve the publishing agent's skill renames, moves, ordering and public-catalogue structure. Reload and recheck those changes periodically during continuing implementation.
2. **Applied coordination:** the three implementation agents received the instruction. The coordinator reloaded AGENTS.md, current skill entry points, docs/skill-packaging.md and the split preparation's script-change record.
3. **Reload points:** before each logical implementation batch, before adopting a native runtime at a component checkpoint, and before each scoped result commit, inspect current paths, imports, ownership instructions and pending Git changes. Re-read changed instruction or packaging files. Discover current skill folders from the filesystem rather than recreating old names.
4. **Current ownership contract:** reusable canonical code is under scripts/, including cadtools runtime and transport. Installed skills use their own scripts/ and explicit caller-owned inputs. Historical component-project callers keep their actual recorded runtime revisions until their checkpoint transition.
5. **Concurrent changes:** preserve the publishing owner's source/layout and generated package changes. Use commits limited to the current implementation's owned content; retain unrelated staged and working changes. Package generation follows the current build script and current packaging instructions after canonical changes are committed, without recreating superseded skill folders.
6. **Observation status:** renaming and package content are changeable. The source records below identify the versions inspected for this coordination update; later implementation batches reload the current files.
