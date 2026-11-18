# Tools

## Reusable native construction and recovery

1. [Stable record pagination](../scripts/cadtools/records.py) — bounded page-size recovery and native document/revision binding.
2. [Durable progress checkpoints](../scripts/cadtools/checkpoints.py) — ordered stage evidence and verified IN_PROGRESS native saves.
3. [Plate operations](../scripts/plate_reference.py) — supplied outlines, bulges, holes, transforms and actual sidewall checks.
4. [Planar profiles](../scripts/planar_profiles.py) — bounded native extrusion and analytic equal-radius opening clipping.
5. [Component insertion](../scripts/assembly_build.py) — source hashes, exact interactive prompts, native metadata and saved placements.
6. [Assembly occurrences](../scripts/assembly_occurrences.py) — nested part quantities, mirrored hands and original insertion-journal recovery.
7. [Native views](../scripts/native_views.py) — saved boundary samples, nested placements and hashed SVG/PNG orthographic/isometric views.
8. [Encoding-aware native geometry](../scripts/native_geometry.py) — stable SAT/SAB readback, OCS points and placed vertex extrema.
9. [Source vector paths](../scripts/source_vector_paths.py) — bounded SVG segment grammar, affine frames and explicit unit conversion.

The [reusable integration procedure](../skills/cad-ocs-engineering/references/generic-integration.md) defines inputs, outputs, units, representation limits and recovery conditions. Component data remains caller supplied.

## Software

1. **Python** runs the helper scripts. Dependencies are pinned in [requirements-native.txt](../requirements-native.txt).
2. **OpenCADStudio** provides the native CAD session via MCP server used by the construction and inspection skills.

## Skills

1. [cad-ocs-engineering](../skills/cad-ocs-engineering/SKILL.md) — combines the full OCS modeling contract, session control, component iteration, geometry checks, saved-model verification and computational handoff instructions.
2. [cad-drawing-inspection](../skills/cad-drawing-inspection/SKILL.md) — guides the agent through reading a DXF's units, layers, blocks and source shapes.
3. [cad-source-intake](../skills/cad-source-intake/SKILL.md) — records the request, source files, hashes and corrections as a new input revision.

4. [CAD MCP translator](../skills/cad-mcp-translator/SKILL.md) — maps and verifies native operations for the chosen bridge.

The [skill catalogue](../skills/README.md) separates these installed skills from proposed workflows. Component-specific procedures are indexed in [cad-ocs-engineering](../skills/cad-ocs-engineering/SKILL.md).

## Files, sources and component records

1. [part_index.py](../scripts/part_index.py) — reads and searches a supplied parts index.
2. [model_inventory.py](../scripts/model_inventory.py) — finds attributed models and filename candidates before a new build, retains exact path/hash-bound different-component reviews, supports exact configuration selection, and preserves known 2D drawing roles through retained-copy hashes. [Start-check procedure](../skills/cad-ocs-engineering/references/existing-model-start-check.md).
3. [source_intake.py](../scripts/source_intake.py) — saves source indexes, request scope and revision receipts.
4. [component_records.py](../scripts/component_records.py) — checks required source values and records individual modeling actions.
5. [source_metadata.py](../scripts/source_metadata.py) — compares expected source labels with the strings stored on a CAD entity.
6. [source_variant_table.py](../scripts/source_variant_table.py) — selects a value from a reviewed table for the specified product variant. The [source procedure](../skills/cad-ocs-engineering/references/source-variant-tables.md) also binds fastener dimensions to the exact standard edition, grade, row and drawing symbol.

7. [retained_artifacts.py](../scripts/retained_artifacts.py) — verifies retained-file hashes, JSON/JSONL syntax and manifest paths using caller-supplied roots. [Manifest procedure](../skills/cad-ocs-engineering/references/retained-artifact-checks.md).

## Drawings and construction

1. [dxf_inspect.py](../scripts/dxf_inspect.py) — lists DXF entities, units, layouts, layers and nested block transforms.
2. [calibrated_trace.py](../scripts/calibrated_trace.py) — converts image points to measured 2D coordinates using reference dimensions, scale and stated uncertainties.
3. [profile_reference.py](../scripts/profile_reference.py) — checks a supplied polygon, extrudes it as reference geometry and inspects the result.
4. [rounded_tube.py](../scripts/rounded_tube.py) — builds and checks a rounded hollow section from supplied dimensions.
5. [axial_motor.py](../scripts/axial_motor.py) — builds and checks the supported housing, shaft and mounting features of a source-bound motor job.
6. [envelope_reference.py](../scripts/envelope_reference.py) — builds and checks a rectangular reference volume from source dimensions.
7. [pixhawk.py](../scripts/pixhawk.py) — builds and checks the Pixhawk 6C mechanical envelope and nominal mounting-thread references.

8. [envelope_job_runner.py](../scripts/envelope_job_runner.py) — runs read-only preflight by default; an authorized write run builds a source-bound rectangular envelope, checks saved geometry and metadata, and closes its completed owned document. [Runner procedure](../skills/cad-ocs-engineering/references/envelope-job-runner.md).

9. [annular_reference.py](../scripts/annular_reference.py) — constructs a plain ring from source-bound bore diameter, outside diameter and thickness in millimetres. Checks analytic cylinder surfaces, end-face loops, closed-body topology and stored source metadata. [Annular-reference procedure](../skills/cad-ocs-engineering/references/annular-reference.md).
   [annular_job_runner.py](../scripts/annular_job_runner.py) executes caller-supplied source-bound annular jobs through preflight, guarded construction, readback, save/reopen and owned-document cleanup. [Annular job procedure](../skills/cad-ocs-engineering/references/annular-job-runner.md).

10. [hexagonal_reference.py](../scripts/hexagonal_reference.py) — constructs a regular hexagonal prism from source-bound across-flats dimension, height and a placement frame, with an optional source-bound bore. Checks side and cap planes, bore surfaces, topology and metadata. [Hexagonal-reference procedure](../skills/cad-ocs-engineering/references/hexagonal-reference.md).

11. [spherical_seat_profile.py](../scripts/spherical_seat_profile.py) — calculates a closed spherical-seat, collar, shaft and tangent-blend profile from caller-supplied dimensions. [Profile procedure](../skills/cad-ocs-engineering/references/spherical-seat-profile.md).

12. [conical_washer_profile.py](../scripts/conical_washer_profile.py) — constructs and checks a free conical washer from source-bound normal material thickness and radial/axial dimensions. [Conical-washer procedure](../skills/cad-ocs-engineering/references/conical-washer-profile.md).

## Circular-section ring geometry

1. [toroidal_reference.py](../scripts/toroidal_reference.py) — constructs and checks a nominal circular-section ring from source-bound inside and section diameters. [Toroidal-reference procedure](../skills/cad-ocs-engineering/references/toroidal-reference.md).

## Geometry, assemblies and component checks

Some of these are specialized tools for particular geometries. I still have work to do on these things.

1. [native_acis.py](../scripts/native_acis.py) — reads supported native solids, analytic surfaces and optional [circular boundary curves and adjacent faces](../skills/cad-ocs-engineering/references/circular-boundary-checks.md).
2. [step_solid_inventory.py](../scripts/step_solid_inventory.py) — inventories STEP solid definitions without counting nested shells as additional solids.
3. [step_placements.py](../scripts/step_placements.py) — reads supported STEP/native placement matrices and compares component positions.
4. [assembly_units.py](../scripts/assembly_units.py) — prepares a unit-change plan for specified assembly root inserts, preserving internal geometry.
5. [assembly_repair.py](../scripts/assembly_repair.py) — applies a reviewed component-placement correction through the guarded CAD client.
6. [feature_checks.py](../scripts/feature_checks.py) — compares measured boundaries, cylinders and other native features with supplied expectations.
7. [small_bms.py](../scripts/small_bms.py) — compares supported solid points and assembly instances before and after saving.
8. [pillow_block.py](../scripts/pillow_block.py) — checks the supported bearing housing, rings, mounting slots and associated parts.
9. [battery_module.py](../scripts/battery_module.py) — checks the supported battery shells, terminals and tabbed-case patterns.
10. [driver_checks.py](../scripts/driver_checks.py) — checks the supported Sumitomo driver exterior and component features.

## CAD document cleanup

1. [ocs_document_cleanup.py](../scripts/ocs_document_cleanup.py) — closes the active owned document after matching its saved-file hash, persistence receipt and geometry revision; checks that unrelated documents retain their paths and dirty states. [Cleanup procedure](../skills/cad-ocs-engineering/references/document-cleanup.md).

## Installed packages and maintenance

1. [build_skill_packages.py](../scripts/build_skill_packages.py) — generates per-skill copies and source/hash manifests; `--finalize` regenerates and requires registration and isolated-installation checks, `--verify` performs final validation, and `--check` checks package synchronisation. [Completion procedure](../skills/cad-ocs-engineering/references/package-completion.md).
2. [package_check.py](../scripts/package_check.py) — verifies installed package hashes, imports and pinned dependency versions; component CAD also accepts a selected OCS session for a read-only state check.
3. [ocs_control.py](../scripts/ocs_control.py) — reads an existing authenticated native session and guards explicitly authorized mutation requests.
4. [check_contract.py](../scripts/check_contract.py) — checks caller-supplied point, axis and plane measurements against an explicit coordinate contract.
5. [cadtools runtime](../scripts/cadtools/runtime.py), [geometry](../scripts/cadtools/geometry.py) and [save/reopen verification](../scripts/cadtools/verification.py) — shared OCS adapters included in the component package. [Package contents and maintenance](skill-packaging.md).

## Running the tools

The file, index and DXF command-line helpers can be run from a terminal. Construction and check modules are imported by component jobs with their source values, model records and CAD client. [Setup and command examples](../README.md#installing).

## Source-bound screw reference

1. [hex_screw_reference.py](../scripts/hex_screw_reference.py) — constructs and inspects a caller-defined regular-hex head joined to a nominal cylindrical shaft. [Procedure](../skills/cad-ocs-engineering/references/hex-screw-reference.md).

## Exact source and partial-work checks

1. [exact_profiles.py](../scripts/exact_profiles.py) — complete ordered Line/Arc/clamped-NURBS loop matching and signed source extrusion direction.
2. [source_solid_checks.py](../scripts/source_solid_checks.py) — ACIS face sense, retained halfspaces, convex planar cell boundary volume and planar bilinear corner correspondence.
3. [Capture checks](../scripts/cadtools/captures.py) — document, revision, rendered frame, PNG integrity and stale-image diagnostics.
4. [Component records](../scripts/component_records.py) — completion gate binding final model evidence to an applied verified reusable change.

## Reversible source workflows

1. [profile_conditioning.py](../scripts/profile_conditioning.py) — caller-specified positive uniform profile/seed/depth conditioning and input roundtrip checks.
2. [solid_transfer.py](../scripts/solid_transfer.py) — complete unchanged native payload and original metadata verification with explicit bijective mappings.
3. [exact_profiles.py](../scripts/exact_profiles.py) — exact-fraction straight cubic certificates and explicitly allowed Line equivalence while preserving strict results.

## Insertion recovery, resume and assembly verification

1. [insert_recovery.py](../scripts/insert_recovery.py) — exact native INSERT default contracts, durable same-request continuation and completion checkpoints.
2. [assembly_verification.py](../scripts/assembly_verification.py) — geometry-bound nested occurrence matching, repeated source-world vertex matching and caller-defined envelope checks.
3. [assembly_build.py](../scripts/assembly_build.py) — guarded insertion-point compare-and-set correction with complete placement readback.
4. [cadtools/checkpoints.py](../scripts/cadtools/checkpoints.py) — source-pinned incremental saves and verified live-document resume gates.

## Rational surfaces and open mesh derivatives

1. [rational_surface.py](../scripts/rational_surface.py) — caller-bound rational B-spline evaluation at two precisions with transform before final rounding.
2. [mesh_checks.py](../scripts/mesh_checks.py) — triangle/UV numerical area, duplicate and oriented edge-incidence checks.
3. [mesh_dxf.py](../scripts/mesh_dxf.py) — source-pinned MESH-only DXF layer declarations with exact entity-tag readback.
4. [insert_recovery.py](../scripts/insert_recovery.py) — offline verification of a recorded cancellation and unchanged caller snapshots.

## Translator-only helpers

1. [Operation planner](../translator/translator.py) validates a documented mapping against a captured tool inventory and selected connection.
2. [Local state ledger](../translator/state.py) stores verified revisions and unresolved native write intents.
3. [Bore fixture checker](../translator/bore_check.py) checks the fixture’s bore rims and wall against ASCII STL triangles.
4. [Installed package checker](../translator/package_check.py) checks the translator’s complete file inventory and hashes.
