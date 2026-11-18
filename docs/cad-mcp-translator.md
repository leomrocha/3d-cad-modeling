---
layout: default
title: Adapt a CAD operation to your MCP server
---

# Adapt a CAD operation to your MCP server

Use the CAD MCP translator when you have a procedure for one CAD application and want your agent to perform it in another. It works one operation at a time. Existing OCS modeling jobs continue to use the OCS engineering skill.

## Install

```sh
npx skills add leomrocha/3d-cad-modeling --skill cad-mcp-translator
```

To install this checkout, run the following from the repository root:

```sh
npx skills add . --skill cad-mcp-translator
```

## Ask your agent

> Use the CAD MCP translator to adapt the bore-diameter change to my FreeCAD project. Start offline. Show the mapping, how you would check the saved result, and which calls need confirmation on my bridge.

The translator reads its packaged mapping and the source procedure. With a configured connection, the agent compares advertised tools and schemas with the mapping for the selected bridge. It can reuse existing code, adapt the instructions or write a helper specific to that endpoint. Changes and checks stay in the local job directory.

## What has been checked?

1. **OpenSCAD.** A documented source-edit procedure and a checked local plate fixture. The fixture checker measures the through-bore and its rims from a temporary ASCII STL.
2. **FreeCAD.** A documented edit of a named sketch constraint through the Yonosoft bridge. Offline tests cover tool selection, missing tools and changed schemas. Native save, reopen and measured readback require evidence from the selected session.
3. **Fusion.** A discovery procedure for Autodesk's desktop MCP server. The tool mapping is filled from the running installation.
4. **Other bridges.** The agent can create an operation mapping locally from an installed procedure, publisher documentation and the selected server's tool inventory. A successful test applies to that operation and binding.

For an offline example after installation, set SKILL_ROOT to the translator's installed directory:

```sh
python3 "$SKILL_ROOT/scripts/translator.py" --application openscad --bridge Nilusche/OpenscadMCP --operation edit-bore-diameter
```

The output identifies the documented operations and required readback. It makes no CAD calls. The installed skill includes instructions for using a captured inventory, verifying the intended change and contributing it through a separately approved pull request. [Contributor guide](https://leomrocha.github.io/3d-cad-modeling/contributing.html).
