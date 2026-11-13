# C034 family-reference variant-scope method proposal

Date: 2026-11-13. Executing model: `gpt-6-luna`.

## Observed case

C034 is the Albright SW200-281 contactor candidate. The exact seller offer names SW200-281 and 24 V intermittent coil, while the retained manufacturer dimensional drawings identify SW200 family revisions rather than the -281 suffix. The 2020 v2-05-20 drawing supports the 153 × 61 × 72 mm family envelope. The 2018 catalogue separately labels 152 mm overall length and different feature values. An optional SW200C inset is a separate configuration.

The case packet therefore gives each value its source revision and configuration scope, ties the proposed envelope to one chosen revision, and keeps the exact input candidate mapping as a separate gate. This prevents a model label from making family dimensions appear suffix-specific.

## Proposed addition to `source-variant-tables.md`

> When a component candidate uses dimensions from a family drawing or a different source revision, record source revision, page/view, configuration or option scope for every dimension used. Label the geometry with the drawing's family/configuration identity. Keep the exact candidate-to-family mapping as a separate evidence gate. Do not merge dimensions across revisions or optional configurations into one geometry unless a source explicitly establishes that combination.

This text is a proposal for the shared skill reference. The shared reference was not edited in this case. The component-specific evidence and source-pinned job remain in FERME.

## Real-case validation

The existing `scripts/envelope_job_runner.py` and `scripts/envelope_reference.py` were reused without modification. A read-only runtime resolution with caller root `PROJECT_ROOT=${FERME_ROOT}` returned `SOURCE_READY`, verified the retained PDF SHA-256 `80c65140cc1d87bbd602c9061536b63e70b42852f9102c1c29a0f33611be1cf6`, and parsed X=153 mm, Y=61 mm, Z=72 mm with origin `[0,-30.5,0]`. The job names the 2020 v2-05-20 family source per dimension, records the separate 2018 revision values, and excludes the optional SW200C inset. No native CAD operation has been performed.

Component job: `${PROJECT_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c034-build-01/envelope-reference-job.json`.
