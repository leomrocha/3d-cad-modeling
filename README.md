# 3D CAD Modeling

Reusable skills, Python tools and documented workflows for building 3D models from descriptions, dimensions, sketches, drawings, photographs and existing CAD files.

The project covers mechanical parts and assemblies, building models, surface reconstruction and geometry handoffs to simulation tools. Work connects each model to its source evidence, units, coordinate frames and checks.


## Documentation

The [documentation index](docs/README.md) links the Markdown pages:

1. [Modeling workflow](docs/modeling-workflow.md) — sources, geometry, assemblies and saved-model checks.
2. [Mechanical examples](docs/wind-generator.md) — wind-generator mast simulation captures.
3. [Building models](docs/building-models.md) — plans, building elements, IFC and display geometry.
4. [Photographs and scans](docs/reconstruction.md) — calibration, reconstruction and CAD remodeling.
5. [Tools and usage](docs/tools.md) — implemented helpers, dependencies and researched integrations.
6. [Sources and images](docs/sources.md) — evidence, image provenance and upstream documentation.
7. [Contributing](docs/contributing.md) — editing pages, recording evidence and testing changes.

## Repository

1. `docs/` — linked documentation and example images.
2. `skills/` — instructions for modeling and inspection tasks.
3. `scripts/` — Python helpers for sources, drawings, geometry and model checks.
4. `tests/` — helper regression tests and retained integration cases.
5. `research/` — tool assessments, workflow specifications and source registers.
6. `execution/` — recorded execution evidence.

## Development

Implemented helpers include source intake, DXF inspection, existing-model lookup, native solid checks, assembly-placement checks and calibrated image tracing. Broader building, reconstruction and simulation routes are documented workflow proposals. [Tool status and usage](docs/tools.md).

## License

Project code and documentation are released under the [MIT License](LICENSE). Third-party software and source assets retain their own license terms; [source records](docs/sources.md) identify their provenance.
