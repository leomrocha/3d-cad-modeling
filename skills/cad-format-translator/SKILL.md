---
name: cad-format-translator
description: Convert CAD files, generate a model from trusted CAD source, or translate editable CAD code. Select an available library, CLI or user-selected MCP server by its demonstrated reader and writer capabilities. Use for format changes and generator translation; native modeling in place uses the existing modeling skills.
---

# Translate CAD files and editable programs

1. Tell the user that source files, derivatives, verification evidence and any new conversion scripts stay in the local job. Ask before contributing improvements.
2. Identify the source representation and requested deliverable: file conversion, generation from trusted code, or editable source translation. Record units, coordinate frame, source/dependency hashes, destination and properties the user requires. Inspect scripts as text before execution. Preserve originals.
3. Discover available software locally, including the user's selected MCP connection. Follow the [route and conversion procedure](references/conversion.md). Direct library and CLI commands handle the listed formats. For other capabilities, map the actual tools on that connection without restricting the product name. A format name alone does not establish fidelity.
   For a Blender file (`.blend`) in either direction, follow the [Blender unit and reference procedure](references/conversion.md#blender-native-files-blend). Ask for the intended units and physical scale or a reference-model dimension whenever scale is ambiguous.
4. Run the selected route only within the authorized workspace. Reopen the staged derivative and compare the specified features. Capture tool versions, arguments, hashes, units, information changes and results. Retain qualified routes locally with their binding and invalidate them when the bridge, documentation, schemas or settings change.
5. After qualifying a reusable script or route, ask if the user wants a local contribution preview. Include only shareable code, mappings and fixtures. Show the final diff, commit, destination and branch. Push and open the PR only after separate explicit approval of that exact revision and destination.
