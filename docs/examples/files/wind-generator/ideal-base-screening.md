# Ideal-base tower screening

Author authorization: 28 October 2026, apply simplification to check the tower; pins and cable hardware evaluated separately later.

1. Revise the existing selected square-reach400-steel-structure simulation. CAD and saved upper shell/beam mesh are unchanged.
2. Replace detailed MOVING, GROUND, pin and optional pad meshes with an ideal rigid assembled base at the existing upper mesh BASE/BBASE cut plane. Fix translations and rotations of the existing member-end nodes at that plane. The local assembled foot is treated as rigid; this is not the raising configuration with a released fixation pin.
3. Retain upper mast chords, lattice, crossed welded reinforcement plates, horizontal diaphragms and tip perimeter members with source sections and materials.
4. Retain tension-only cable spans, source attachment coordinates, axial compliance, mass and installed-tension calibration. Individual clamps, tensioners and pins are excluded from local capacity predictions.
5. Retain gravity, head mass/application points, aerodynamic loads and selected wind input from the current register. Wind input is 15 m/s (54 km/h), incoming direction 0 degrees. Load and resistance factors remain 1; no new safety factor is applied.
6. Absolute equilibrium residual input remains 0.1 N for translational equations or 0.1 N m for rotational equations. The relative criterion is disabled. No base-contact seating stage is needed.
7. Reuse native input/weld checks and run the full existing sequence sequentially: gravity equilibrium, cable pretension calibration, wind equilibrium, saved-field extraction. One computational job at a time. Memory EVAL remains waived by author; Docker 16 GiB, Code_Aster memory_limit 15000, CPU time_limit 36000 seconds unchanged.
8. Extract mast stresses/displacements, cable forces and reactions at IDEAL_BASE and the guy anchors. Base reactions are loads for subsequent connection calculations. This run does not calculate foot, pin, bore or foundation capacity, foot compliance, clearance or raising behavior.
9. Preserve all previous detailed-base attempts. Never relabel their validation or results as belonging to this idealization. The revised native input check is saved under the existing check directory in ideal-base/.

Sources: screening_job.py, screening-15ms/input-register.json and the existing selected upper mesh metadata. Actual assistant model identifier unavailable.

## Execution outcome

The selected ideal-base sequence completed: native input construction, gravity equilibrium, installed cable-tension calibration, wind equilibrium and saved-result extraction. The successful wind attempt is `screening-15ms/cases/square-reach400-steel-structure-15ms-from0deg-retry02/`; `metrics.json` contains the calculated member stress comparisons, displacement, cable tensions and support reactions. Native computed fields are in `fields.med`, `plates.med`, `members.med` and `cables.med`. Earlier export failures remain preserved separately.

The chord and lattice-brace stress comparisons do not exceed their assigned yield inputs in this case. This does not establish complete tower capacity: physical-panel buckling, weld resistance and plate surface stresses remain uncomputed. DKTG exports plate force/moment resultants; the eccentric reference-plane correction must be verified before recovering physical surface stresses. See `../../research/code-aster-convergence-tolerances/dktg-stress-extraction.md`. No plate yield input or new load/resistance factor was invented. Cable/pin/ground hardware capacity remains outside this idealized calculation.

Work performed by Code_Aster 17.4.0. Primary assistant model identifier unavailable; documentation research performed by gpt-6-luna.

## Incoming 45-degree wind and ParaView

The subsequently authorized incoming 45-degree case completed using the same geometry, ideal base, materials and installed cable calibration. Native construction and the memory EVAL passed before this wind run. Results are in `screening-15ms/cases/square-reach400-steel-structure-15ms-from45deg/metrics.json`. Its calculated chord and lattice-brace stresses exceed their assigned yield inputs. This is a failed yield screening comparison using an elastic model, not a prediction of post-yield behavior or observed breakage.

Run `bash simulations/code-aster-mast/open_results.sh` from the project directory to open the saved native comparison. This loads the installed MEDReader plugin and `screening-15ms/mast-assembly-comparison.pvsm`, showing the final computed step for both wind directions. Its three layout tabs show actual deformation at scale one, a separate deformation display magnified by ten, and member yield coefficients on the actual deformed geometry. Displacement colours use metres and the same range in both directions. The display magnification is not a load factor. Native member-force arrows and cable/plate force samples are retained as hidden pipeline items that can be shown using their eye icons. Plate samples are resultants, not physical surface stresses. No result-data format conversion is performed.

Recreate the state with the installed ParaView `pvpython` running `prepare_comparison_view.py --native`; run this alone under the existing computational-job lock. Simulation fields and viewing states remain local generated outputs excluded from Git by default.

The restored yield-coefficient view reuses `saved_stress_records` in `export_stress_limits.py` and the existing member-stress equations. Each dimensionless coefficient is assigned yield strength divided by calculated equivalent stress, aggregated by maximum saved stress per original solver cell. The native MED cell identifiers are checked against saved solver connectivity and coordinates before attaching these arrays inside ParaView. Colours use the previous yield-coefficient bands; the exact `Yield_over_stress` scalar remains available for selection and inspection. Each panel also states its minimum assigned coefficient. Members without a yield input and components outside this check remain unevaluated. Plate stress recovery is deferred under the author's instruction; no plate coefficient is inferred. No simulation or result-file format conversion is required.
