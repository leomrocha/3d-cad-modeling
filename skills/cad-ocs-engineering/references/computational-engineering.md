# Computational engineering

Read for actual equations, procedural geometry or solver preparation. This reference installs nothing and selects no model fidelity.

## Tool boundaries

1. OCS remains interactive CAD. An automation API does not prove parametric history or solver functionality.
2. PicoGK and ShapeKernel are public code-driven geometry projects; they can supplement a requested procedural/implicit geometry task. Geometry generation supplies no tested turbine physics model or material law.
3. Noyron is proprietary in LEAP 71's archived description. Company claims do not establish public reproducible software or current-project accuracy.
4. Retrieved PicoGK project declares .NET9 and package2.3.0. Native paths list macOS ARM64 and Windows x64; this is not the full support matrix or proof of Linux compatibility. No installation or OCS interchange was tested.

## Separate linked artifacts

- **Inputs:** parameters, units, domain/ranges, uncertainty, source class and author choices; coordinate frames/interfaces.
- **Geometry:** native document/part mapping, representation (solid/B-rep, mesh, voxel field, shell), placement, topology checks, resolution.
- **Calculations:** equations/units, assumptions, independent reference and limiting cases, numeric tolerance. Correct algebra does not prove applicability.
- **Physical materials:** property/value/unit/source, condition/temperature/orientation, measured/manufacturer/literature/assumed status. Render appearance is not density, modulus or laminate data.
- **Simulation:** solver/version, geometry and mesh hashes, elements/resolution and named-face mapping, materials/loads/constraints/contact/boundary conditions, convergence settings.
- **Run evidence:** input/output hashes, logs, residuals/conservation where applicable, convergence/sensitivity and explicit failure/unknown. Prediction remains distinct from experiment.

Check dimensions/signs before solver launch. Use independent analytical reference cases, geometry checks, mesh/solver convergence and measured comparisons appropriate to scope. Do not invent load cases, material properties or safety factors.

## Interfaces

For each CAD/mesher/solver/code boundary, specify source/target representation, units/transform, exporter/importer version, part/face mapping and data losses. Follow exact format-conversion approval rules. Test a known geometry only with authorization; compare body counts, bounds and volumes where supported. A display tessellation is not a volumetric FE mesh; an STL that opens does not preserve solid or assembly semantics.

A runnable solver setup requires software/dependencies, valid inputs and accepted assumptions. This skill alone is not that setup. Initial inventory found Python, Blender and OpenSCAD on PATH; several solvers were not found there. That does not prove machine-wide absence. Do not install or execute because a tool is mentioned here.

Evidence: `${ENERGY_ROOT}/heoliennes/research/cad-workflow/computational-engineering-findings.md` and `${ENERGY_ROOT}/raw/wind-prototypes/manifests/cad-computational-engineering.jsonl`.
