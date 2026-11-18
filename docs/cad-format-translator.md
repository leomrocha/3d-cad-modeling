---
layout: default
title: Translate CAD files and editable programs
---

# Translate CAD files and editable programs

Use `cad-format-translator` when the deliverable is a different file or an editable generator. Tell the agent the source, target, units and properties you want to retain.

```sh
npx skills add . --skill cad-format-translator
```

Run that command from a checkout containing the skill. Select the skill in the normal repository installer when installing a published revision that contains it.

1. **Convert an existing file.** Example: “Convert this STEP solid to a closed STL in millimetres. Report the change in volume.” The supplied CadQuery route checks the STEP solid, writes triangles, and reads the STL back.
2. **Generate a model.** Example: “Run this reviewed Python generator using its project environment and export a STEP assembly. Keep names and placements.” The supplied helper understands a CadQuery shape, workplane or assembly named model. For another Python project, the agent first identifies its own entry point, libraries and project data.
3. **Translate editable code.** Example: “Translate this OpenSCAD plate to Python and keep bore diameter editable.” The supplied translator handles a bounded set of primitives, extrusion, translation and subtraction. Unsupported syntax gets a source location. Fixed-facet cylinders stay polygonal by default; replacing them with analytic circular cylinders is an explicit option.
4. **Use an unfamiliar MCP server.** Select the connection and show the agent its tool inventory. The agent maps actual tools and argument schemas to directional operations, including a single conversion call or an import followed by export from an owned scratch document. It checks required properties, dependencies, path access and known losses before proposing a route. A synthetic inventory ships with the skill so the planner works offline.

The local conversions use whichever optional runtime the route requires. The planner and SCAD-to-Python translator use the Python standard library. A successful local CLI or library check applies to that route. Each live MCP endpoint needs its own readback evidence.
