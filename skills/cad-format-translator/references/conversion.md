# Discover, execute and verify a conversion

## Choose the representation

1. Inspect source headers and project metadata. For a Python project, inspect the entry point, modeling library, imports, external assets and project-defined parameters. Record the generator runtime and hashes of all dependencies that influence geometry. Executing an arbitrary script can read files or launch processes. Run only reviewed, authorized code in the owning project's environment.
2. Specify receiving units, origin, axes and required information. An assembly may require individual occurrences, names, transforms and analytic faces. A drawing projection needs a view plane, scale and layer policy. IFC needs class, spatial containment, unit, placement and property requirements. A tessellated surface carries different information from an analytic cylinder. Identify permitted losses before choosing an exporter.
3. Probe optional runtimes without installing them. The planner and source translator require only Python. Source rendering needs OpenSCAD on PATH. CadQuery operations need the caller-selected Python environment with CadQuery. Use an existing project exporter for other Python dialects. Preserve input dependencies, use an owned working directory, stage to a new artifact and keep its check receipt with the job.

## Use any configured MCP server

1. Bind to the connection selected by the user. Collect all pages of the current tools/list inventory, relevant schemas, host version and units. Use local workspace labels; keep credentials private. Inspect publisher docs and actual tool contracts to map reader, writer, generator or direct conversion semantics. Never infer support from a brand or from suggestive tool names. The [MCP tool specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) defines discovery.
2. Use the [example inventory](../fixtures/inventory.json) as a schema example. Populate operations with actual representation identifiers, input argument bindings, format direction, supported properties, documented losses, explicit handoff representation, path visibility and evidence. Use a distinct intermediate identifier for each compatible handle contract. Include document/workspace scope, units, version and settings in the inventory. Set complete only after uninterrupted discovery. An ambiguous capability remains a gap until clarified or tested.
3. Run the [planner](../scripts/routes.py) with the job's chosen representations:

```sh
python3 "$SKILL_ROOT/scripts/routes.py" "$SKILL_ROOT/fixtures/inventory.json" --connection workshop-fixture --source step-solid --target stl-mesh --require mm
```

4. Compare all candidate routes and expected losses. For direct conversion, bind source and output to exact schema fields. For import/export, use an owned scratch document, take the actual handle from import, pass it to the selected writer, and verify each tool result. Require an accessible output and independent readback. For generator tools, record text/asset delivery, runtime and parameters. Any cloud upload requires explicit permission. After an uncertain write inspect actual state before taking another action; preserve user documents during cleanup.
5. Store the inventory, plan binding, chosen steps, resolved arguments, artifact hashes and verification receipt together in the caller's job. Repeat the planner with --previous and the stored binding before reuse. A matching binding permits reusing the candidate mapping. Only the matching directional fixture results establish verified behavior.

## Bundled conversions

Use the [conversion command](../scripts/convert.py) in a runtime with the required optional dependency. Every command requires a new output filename. Its JSON result contains primary input and output hashes. Redirect the result to a new receipt path. Pass --dependency PATH for each reviewed include, sibling module or data file to pin its bytes before and after conversion. Supplement that receipt with the project dependency map, host settings and feature checks specific to the job.

```sh
python3 "$SKILL_ROOT/scripts/convert.py" scad-stl "$SKILL_ROOT/fixtures/plate.scad" plate.stl --trusted-source
python3 "$SKILL_ROOT/scripts/convert.py" scad-python "$SKILL_ROOT/fixtures/plate.scad" editable.py
python3 "$SKILL_ROOT/scripts/convert.py" python-step editable.py plate.step --trusted-source
python3 "$SKILL_ROOT/scripts/convert.py" step-stl plate.step exchange.stl
```

1. **SCAD → STL.** The OpenSCAD CLI renders the saved source, including its normal local dependencies. Use a millimetre source convention. The reader checks finite triangles, reciprocal closed edges, positive volume and extents. Supply a separate feature check for the part. [OpenSCAD CLI](https://files.openscad.org/documentation/manual/Using_OpenSCAD_in_a_command_line_environment.html).
2. **SCAD → editable CadQuery Python.** The [source translator](../scripts/scad_source.py) supports top-level scalar assignments and references, signed numeric literals, origin-based cubes, fixed-facet cylinders with named h/d, translation, difference and linear extrusion of an origin-based square. Use positive dimensions and a single resulting shape. Modules, loops, arbitrary expressions and unsupported statements produce a source-line diagnostic. The default emits a polygonal cylinder at the explicit facet count. Opt in to --analytic-cylinders to replace that polygon by a circular surface with the same nominal diameter. Record this geometry change. Change a named parameter in both programs and compare independently reopened results.
3. **Trusted Python → STEP.** The example generator exposes a CadQuery Shape, Workplane or Assembly named model. Run it with its required modules and inputs available to the selected interpreter. The helper writes a shape and compares solid count, cylinder radii, bounds and volume after STEP import. For an Assembly, the helper uses the assembly writer and compares the reopened tree, labels, local transforms and geometry at each path. Colors, materials and constraints require separate checks. [CadQuery exchange](https://cadquery.readthedocs.io/en/latest/importexport.html).
4. **STEP solid → STL.** CadQuery imports and triangulates the input. Read back ASCII STL as closed triangles and compare signed volume to the input using a 1% screening threshold. STL units follow the documented millimetre convention. Assemblies with touching surfaces and non-closed outputs need a different qualified route. Functional tolerances must come from the job.
5. **IFC and other formats.** Use capability discovery. IFC authoring requires semantic inputs even when an existing solid supplies shape. Inspect project, classification, placement and geometry after reopening. [IfcOpenShell geometry creation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html).

## Blender native files (.blend)

1. **Determine scale before writing.** Inspect the active scene, selected mesh, world transform, scene unit system and Unit Scale. For a metric or imperial scene, Unit Scale gives metres per Blender unit (BU). The displayed length label alone does not determine scale. STL coordinates have no embedded unit. If the job and file leave a scale unknown or disagree, pause and ask: “Which physical length does one source unit represent, and which unit should the destination use? Alternatively, which feature should match which dimension on your reference model?” For a new Blender scene, also obtain its intended metric or imperial system and physical length per BU.
2. **Calibrate from another model.** Identify the same two points on both models, measure their separation in world coordinates and record the reference model, feature and physical unit. Divide the known length in metres by the measured source distance. For example, 4 BU matching 6 inches gives 0.0381 m per BU. Use a second known dimension to check the result when available. If dimensions imply different factors along different axes, ask which geometry or measurement to use before converting.
3. **Write a new derivative.** The [Blender exchange script](../scripts/blend_exchange.py) uses Blender's native scene reader/writer and STL operators. It keeps Y forward and Z up in both directions and applies the unit factor once. Run from the local job using a Blender executable with these operators. Examples assume the shown units and object name have already been established.

```sh
blender -b --factory-startup --disable-autoexec --python-exit-code 1 --python "$SKILL_ROOT/scripts/blend_exchange.py" -- part.stl part.blend --stl-unit mm --scene-system METRIC --metres-per-bu 0.01
blender -b --factory-startup --disable-autoexec --python-exit-code 1 --python "$SKILL_ROOT/scripts/blend_exchange.py" -- design.blend part-inches.stl --object Bracket --stl-unit in
```

4. **Apply a reference measurement.** On Blender export, pass `--reference 4 6 in` when a 4 BU distance represents 6 inches. On STL import, replace `--stl-unit mm` with `--stl-reference 4 6 in` for the equivalent measurement in STL coordinates. An explicit Blender scale overrides scene metadata. Record the user's choice when they conflict.
5. **Check the handoff.** Reopen the derivative, compare the reference feature and world-space bounds in the same physical unit, and record the tolerance and result. A new .blend holds the imported triangle mesh and scene units. STL export writes the selected mesh's evaluated triangles in world placement. Materials, scene hierarchy and editable modifiers stay in the original .blend. For another format or an assembly that needs these properties, qualify the specific reader, writer and receiving software through the capability procedure above.
