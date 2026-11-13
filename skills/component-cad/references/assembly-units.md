# Plan assembly root unit changes

Use `scripts/assembly_units.py::plan_root_unit_change` to prepare a read-only plan when an assembly root insertion converts coordinates between drawing units. Supply the complete root insert records and explicit source and destination unit mappings from the caller's job. Each mapping contains a readable `label`, an integer `code`, and `millimetres_per_drawing_unit`; codes are descriptive inputs and do not determine scale.

The planner computes `source millimetres per drawing unit / destination millimetres per drawing unit`. For each root it applies that factor to the root insertion point's x/y/z coordinates and to x/y/z scale values. It preserves the normal, rotation, array metadata, block name and block-internal geometry. It returns the before and after properties and corresponding matrices. The planner performs no CAD mutation.

The helper validates every supplied root before returning any plan. It rejects empty or duplicate root sets, non-Insert records, missing or empty handles, nonpositive or nonfinite unit factors, unsupported array inserts, nonpositive/nonfinite scale values, reflections, nonuniform scales, and nonfinite entries in the before, planned, or expected transform matrices. It relies on `scripts/step_placements.py::native_matrix(..., allow_uniform_scale=True)` for the supported insert transform contract. Root records must represent the actual top-level inserts; a nested insert or a block with an unsupported base point needs a separate reviewed method.

Read the source unit declaration and native drawing unit setting first. Compare the plan matrices and feature dimensions against the actual native drawing after an authorized edit. A successful plan and synthetic test establish planner behavior; they do not establish source association, physical fit, or saved CAD persistence.

`tests/test_assembly_units.py` uses synthetic root records only. It covers translation and scale together, orientation preservation, zero-origin roots, invalid units, arrays, nonuniform or invalid scales, empty and duplicate handles, a NaN rotation that produces a nonfinite transform, and all-roots validation.
