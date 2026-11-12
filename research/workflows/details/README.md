# Detailed input-to-3D workflows

Date: 12 November 2026. These are generic procedures for the 38 recorded routes. Each dossier states its input conditions and intended output.

1. [All workflows ordered by manual effort](/home/leo/projects/3dmodeling/research/workflows/details/by-human.md).
2. [All workflows ordered by computing demand](/home/leo/projects/3dmodeling/research/workflows/details/by-compute.md).
3. [Structured dossiers](/home/leo/projects/3dmodeling/research/workflows/details/workflow-details.json) and [classification contract](/home/leo/projects/3dmodeling/research/workflows/details/contract.json).
4. [Reference code and input contracts](/home/leo/projects/3dmodeling/examples/workflows/README.md).
5. [Reconstruction Mermaid graph](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.md) and [operation catalogue with source links](/home/leo/projects/3dmodeling/research/workflows/operation-catalogue.md).
6. [Original source register with summaries](/home/leo/projects/3dmodeling/research/sources/source-register.md).

## Reading the classifications

Ratings are analyst estimates from 1 to 5 under each dossier's conditions. Each axis is independent; equal numbers denote the same class. They describe relative work and resource demand, rather than measured durations.

| Class | Manual effort | Software setup | Computing demand |
| --- | --- | --- | --- |
| 1 | Direct import, parameter entry or reuse with explicit dimensions and identity | Existing application | Small CPU transforms, parsing or simple geometry |
| 2 | Limited tracing, cleanup or placement | A scripting library | CPU CAD operations or small mesh processing |
| 3 | Calibration, reconstruction review, moderate remodeling or semantic preparation | Several tools and adapters | Substantial CPU/RAM for clouds, decomposition or batches |
| 4 | Multiple sources, extensive feature interpretation or articulation | GPU, sensors or specialized stack | Dense image reconstruction, scene training or GPU inference |
| 5 | Ambiguous views, custom methods or research | Custom research integration | Large model memory or several heavy reconstruction branches |

Manual effort measures interpretation and intervention. Setup measures the dependencies to establish. Computing describes the stated baseline dataset and method. Resolution, image count, point count, batch size, GPU memory and representation can change the computing class; each dossier records those scaling factors. Operation counts describe the existing registered operations, whose internal procedures can contain many actions.

A known component or an explicitly dimensioned simple part starts with fewer interpretation steps. A raster drawing needs tracing and constraint decisions. Photogrammetry adds camera estimation, correspondence, dense reconstruction, scaling and cleanup. Converting a reconstructed mesh into editable CAD adds feature interpretation and fitting. IFC adds building entities and relationships; robotics adds link frames, joint definitions, collision geometry and sourced mass/inertia.

## Content of each dossier

Each page includes the original registered starting artifact types and full operation input/output requirements. Detailed artifact sections also describe prepared intermediates and optional existing data at the relevant stage. Every route records inputs, measured points and datums, coordinate frames, software and libraries, operation order, code/API entry points, outputs, checks, failure recovery, computing requirements and original evidence. Combined routes identify the reference-frame and evidence conditions for merging their branches. Their composition status remains a proposal.

## Reproduce the documentation checks

```sh
python3 research/tools/build_workflow_register.py --date 2026-11-12
python3 research/tools/build_workflow_details.py --date 2026-11-12
PYTHONDONTWRITEBYTECODE=1 python3 examples/workflows/common/test_control_distances.py
```

The builder checks coverage, required fields, ratings, source registration, local code paths and Python syntax. The distance-helper tests exercise synthetic coordinate and unit checks. Individual code examples record their integration status beside the code.
