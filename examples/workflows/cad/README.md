# CAD workflow reference scripts

The scripts are **reference code** for [CAD-R01](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json) and [CAD-R04](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json). They have not been run with CadQuery in this project. They preserve source files and refuse to overwrite an existing output unless `--overwrite` is supplied.

## CAD-R01 — explicit dimensions to one editable part

[`build_part.py`](/home/leo/projects/3dmodeling/examples/workflows/cad/build_part.py) reads a caller-supplied JSON file. It has no default part dimensions. The JSON contract requires `units: "mm"`, `part.name`, `part.length`, `part.width`, `part.thickness`, and `through_holes` (use `[]` to state that the plate has no holes). Hole `x` and `y` coordinates use the plate-centre datum in millimetres; the plate bottom lies at `z=0`.

Schema example only; replace each placeholder with a numeric value from a recorded source before use. Keep a sidecar provenance record mapping every JSON field (including each hole coordinate and diameter) to its source URL, drawing page or measurement record. The script reports the parameter JSON SHA256 so that record can identify the exact input revision.

```json
{
  "units": "mm",
  "part": {
    "name": "source-linked part name",
    "length": "<positive numeric value>",
    "width": "<positive numeric value>",
    "thickness": "<positive numeric value>"
  },
  "through_holes": []
}
```

Run in a Python environment that already provides CadQuery and its OCCT binding:

```sh
python /home/leo/projects/3dmodeling/examples/workflows/cad/build_part.py \
  --parameters /absolute/path/part-parameters.json \
  --step /absolute/path/output/part.step
```

The script creates a CadQuery source model from explicit parameters, checks one valid connected solid and its bounding dimensions, exports a STEP solid in millimetres, reopens the STEP file, and checks validity, solid count, bounds and volume. Keep the `.py` source and parameter JSON beside the STEP derivative. The script output is exact kernel geometry; it does not provide a GUI feature tree. CadQuery documents that its Python source is its parametric format and that imported STEP is interchange geometry.

## CAD-R04 — one DXF profile to an extruded solid

[`import_profile.py`](/home/leo/projects/3dmodeling/examples/workflows/cad/import_profile.py) reads one closed wire from one named DXF layer. The caller must provide source DXF path, selected layer, source-to-millimetre scale, extrusion length in millimetres, wire-merge tolerance in source units, and a new `.step` path. It reads `$INSUNITS` through ezdxf and stops on a conflicting scale unless `--allow-header-scale-mismatch` is explicitly supplied. A unitless DXF header leaves the caller-supplied scale as the controlling evidence.

```sh
python /home/leo/projects/3dmodeling/examples/workflows/cad/import_profile.py \
  --dxf /absolute/path/source/profile.dxf \
  --layer PROFILE \
  --scale-to-mm 1 \
  --extrusion-mm 0 \
  --merge-tolerance-source-units 0.000001 \
  --step /absolute/path/output/profile.step
```

Replace the numeric command values with the source unit conversion, confirmed extrusion length and justified importer tolerance. This reference accepts exactly one closed wire. It stops on multiple wires because holes, nested contours and separate regions need explicit profile topology. Uniform `transformGeometry` scaling can change analytic curve types; retain the DXF and inspect the exported STEP. The original DXF is never modified.

## API evidence and representation limits

- CadQuery's [`importers.importDXF`](https://cadquery.readthedocs.io/en/stable/importexport.html) accepts a layer include list and wire merge tolerance. Its documented profile route is `importDXF(...).wires().toPending().extrude(...)`.
- CadQuery's [`Shape.isValid`, `Shape.BoundingBox`, `Shape.Volume`, and `Shape.transformGeometry`](https://cadquery.readthedocs.io/en/stable/classreference.html) support the checks and coordinate scaling used in the reference scripts. CadQuery documents that `transformGeometry` may convert lines and circles to splines for general transforms.
- CadQuery's [STEP export documentation](https://cadquery.readthedocs.io/en/stable/importexport.html) documents millimetre defaults and explicit `unit` / `outputUnit` options. Its [import/export overview](https://cadquery.readthedocs.io/en/stable/importexport.html) says Python is its fully parametric source format and STEP is an interchange format.
- ezdxf's [`$INSUNITS` reference](https://ezdxf.readthedocs.io/en/stable/concepts/units.html) explains the DXF header's modelspace-unit convention and provides `conversion_factor`; DXF coordinates themselves are otherwise unitless.
- CadQuery is licensed Apache-2.0; ezdxf is MIT. Their dependencies, including OCCT/OCP and optional packages, have separate terms. See the source register for inspected links and evidence status.

## Manual and assisted workflow entries

CAD-R02 uses OpenCV image rectification and Tesseract dimension candidates, then a person confirms every glyph, feature association and constraint before CAD construction. CAD-R03 adds a reviewed wall/opening graph and explicit vertical dimensions. CAD-R05 and CAD-R09 require orthographic view matching; papers are research methods, not a bundled CAD reconstruction application. CAD-R06 reconstructs visible surfaces from overlapping photographs and measured controls before remodeling. CAD-R07 registers depth scans to an existing housing datum. CAD-R08 places identified library parts using recorded interface frames. CAD-R10 uses OpenSCAD source to create a mesh; STL coordinates have no inherent unit field, so keep a separate unit declaration and source.
