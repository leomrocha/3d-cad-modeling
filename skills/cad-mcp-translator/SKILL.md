---
name: cad-mcp-translator
description: Adapt a CAD operation to an explicitly selected non-OCS application and MCP connection, or prepare an offline adaptation on request. Use for requests such as “use my FreeCAD to revise this plate.” Keep ordinary OCS, unspecified CAD, installation-only and export-only requests on their existing routes.
---

# CAD MCP translator

1. At the start tell the user: “I’ll keep the mappings, scripts and checks in your local project so you can reuse them. If an improvement works, you can review it later and decide whether to share it on GitHub.”
2. Identify the existing procedure, the requested operation, the chosen application, bridge and connection. Resolve an ambiguous destination before contacting a server. Use the configured client. Save working files in a caller-owned job folder. Treat installed files as read-only. Cloud saves require an identified destination and permission.
3. Follow the [operation procedure](references/operations.md) at bootstrap and whenever a new script, paragraph or procedure is needed. It covers document lookup, deciding what to reuse or write, mapping arguments, running an independent check, durable write intents and unknown outcomes. Use previous evidence only for the same binding and operation. Preserve behavior on every other endpoint.
4. For an offline start, select a documented candidate and run the bundled planner. SKILL_ROOT is the installed translator directory. The command reads the mapping and prints the plan. Python needs only its standard library.

```sh
python3 "$SKILL_ROOT/scripts/translator.py" --application freecad --bridge yonosoft/freecad-mcp --operation edit-bore-diameter
```

5. Report the evidence level: documented, schema observed, offline verified, or live verified for a named operation and binding. Offer [optional contribution](references/contributing.md) after a checked improvement. Completion of a translator operation has its own evidence receipt.
