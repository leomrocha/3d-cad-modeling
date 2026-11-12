# Source-first component preparation and rounded hollow-section construction

Observed case: main frame longitudinal rail (P01), 12 November 2026. Executing model: gpt-6.1-sol. [Execution evidence](/home/leo/projects/3dmodeling/execution/p01-rail-build.md).

## Source actions before construction

1. Read the component sheet and existing stock/catalogue records. Search existing project sources for the exact part and dimensions before commissioning external research. Preserve item identity, original source and proposal labels. P01's input is proposed 40 × 40 × 3 mm tube, 600 mm cut length.
2. For a standard-defined feature such as tube corner geometry, identify the standard and manufacturing-route branches through existing sources or authorized research. Record the search itself as an action. Apply the project's delegated-research rules to external searches.
3. Check how each source was accessed: readable document, indexed excerpt, metadata or failed request. Associate each clause/formula with its actual observation. Preserve access failures and corrections.
4. Calculate the required values with their input units, formula and edition. EN 10219-2:2019 Annex A.3 gives nominal calculation radii of 6/3 mm at T=3 mm; Table 3 supplies the separate external profile interval4.8–7.2 mm. [Source observations](/home/leo/projects/3dmodeling/research/sources/round-10/tube-corner-sources.json).
5. Bind the intended representation and source revision. This run uses the EN 10219 nominal section-property reference geometry. Retain the EN 10210 hot-finished calculation branch and actual-stock measurement branch as alternatives. An input revision stores the nominal model basis and source hashes.
6. Run source readiness. Append the action results in the component project's registry and link the reusable definitions [here](/home/leo/projects/3dmodeling/research/action-audit/component-source-actions.json). The original operation graph keeps its identifiers and boundaries.

## Supported construction and verification procedure

1. Read the installed OCS state/capabilities and `record_schema` for the actual entity types. In this installed build, `entity_schema` and `guide` returned `unknown_operation`; `record_schema` returned the profile/solid definitions. Preserve the observed response with the component evidence.
2. Use an isolated new document, millimetres and world coordinates. For this recipe, origin is front-end centre; X/Y span the section, +Z follows cut length. Assembly placement is a separate action.
3. Create two exact closed lightweight polylines, each with eight vertices. Four straight segments alternate with four quarter-circle arcs. Bulge is tan(pi/8), the native arc encoding. Inner section dimensions are width−2T and height−2T. This helper supports concentric corners with outer radius−inner radius=T and positive straight wall lengths.
4. Use explicit selection readback. **OCS 2026.42 treats select(clear=True) as clear-only even when handles are present.** `SelectionCheckedClient` sends clear=False for a nonempty explicit handles list and checks the actual selected handles. It preserves clear-only calls and uses the existing guarded runtime/journal.
5. For this source-defined section, the exercised construction route is bounded-area extrusion: clear selection, run `PRESSPULL 18.5,0,0 600`, then finish the owned PRESSPULL command if it remains active. The pick point is derived from width/2−wall/2 and lies in a straight wall. Inspect the resulting entities for exactly one native solid; remove only the temporary profiles created by this call. Add source metadata.
6. Read the solid's native SAT text and verify vertex extents, four X wall planes, four Y wall planes, end planes and the four outer/four inner cylindrical corner surfaces. P01 passed all five check groups. Numerical comparison threshold is1e−7 mm, adopted from the existing FERME native-surface reader; manufacturing limits keep their own source values.
7. Audit and save a new DWG 2018 target. Inspect save hash, dropped data and entity manifest, then reopen the exact saved file. The existing `save_reopen` function checks file identity and audit manifests.
8. Read the reopened entity record before checking its features. P01 reopens with SAB binary data. The current Python feature reader returns `UNKNOWN` for that encoding and preserves the raw record. The repeated feature check is a distinct step from the successful save/hash/manifest checks.
9. Capture the reopened end view and isometric view; inspect their contents. P01's images show its hollow rounded section and longitudinal edges. The same reopened document's measure/audit bounds report zero while its mesh has volume 252167.41146658108 mm³. Preserve both observations; view identity and mesh metrics have their own evidence.

## Executable helper and dependencies

1. [rounded_tube.py](/home/leo/projects/3dmodeling/scripts/rounded_tube.py) is a live-run helper, using Python3.10+ standard library, this project's source-record reader, externally supplied FERME `cadtools` modules and the installed OCS control helper. Imports perform no discovery. `--allow-write` enables the separately authorized live run.
2. Supply the input job, actual helper/module paths, session, new request namespace, new journal, existing work directory and new absolute DWG output. The helper derives dimensions from the source-pinned job. It creates an isolated document. Existing journals require explicit stage inspection.

```sh
python3 /home/leo/projects/3dmodeling/scripts/rounded_tube.py JOB_JSON \
  --cad-modules /home/leo/projects/ferme/skills/cad-construction/scripts \
  --control /home/leo/.codex/skills/ocs-engineering/scripts/ocs_control.py \
  --session SESSION_ID --namespace NEW_NAMESPACE --journal NEW_JOURNAL \
  --work-dir EXISTING_WORK_DIRECTORY --output NEW_ABSOLUTE_DWG \
  --route bounded-area --allow-write
```

3. Exit0 requires native pre-save and reopened feature checks to pass. Exit1 with an `UNKNOWN` result retains the saved model and the unsupported reopened feature result. The first live run raised on this encoding; the helper now writes the raw record and explicit result.
4. [Tests](/home/leo/projects/3dmodeling/tests/test_rounded_tube.py) cover selection semantics, selection mismatch, incorrect dimensions/walls/radii, native reader boundaries and binary-record status. Run `python3 -m unittest discover -s tests -v` from this repository.

## Failed routes and recovery

1. Initial extrusion had an empty selection because of the clear-only semantics. Its definitive completed response had no changes; the sole surviving profile was read back before a new, corrected extrusion request. `--resume-profile HANDLE --route solid-subtract` supports this specific inspected state and refuses extra entities or changed profile data.
2. The solid-base/cutter route produced the intended outer and inner solids, then SUBTRACT returned `the selected topology could not be cut safely`. A separate planar-region subtraction attempt returned the same error. Both attempts retain their journals and document IDs; the helper exposes their route names for diagnosis. The default bounded-area route is the one that produced the native hollow rail.
3. Isometric capture initially exceeded the runtime's operation-query count. Same-ID recovery returned its completed result. Use the existing journal's request identity after uncertain completion; inspect the returned command and geometry state before any dependent mutation.
4. Next required checker work for P01 is reading or querying the reopened SAB feature geometry and resolving the zero-bounds API discrepancy. Reuse a supported existing decoder/query method before introducing a reader. Repeat the source-linked dimensional checks against that saved revision.
