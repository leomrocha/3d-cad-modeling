# Existing implementations and evidence

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 12 November 2026. Inspection model: gpt-6.1-sol. Local source reading and retained check-file inspection.

## cad-workflow-findings.md — ferme-findings

Original: cad-workflow-findings.md (`${FERME_ROOT}/skills/cad-workflow-findings.md`). Evidence: `recorded_execution_summary`. SHA-256: `fbd89002aa02beb1ead8d537dcb650047c357b90eea40d2281350ff28212811e`.

OCS 2026.42 component constructions, import/save results, failed requests and component-specific recoveries.

Claims are attributed to the retained reports/session identifiers; raw session replay is a separate result.

## SKILL.md — ferme-skill

Original: SKILL.md (`${FERME_ROOT}/skills/cad-construction/SKILL.md`). Evidence: `documented_skill`. SHA-256: `bc45db50ee1ee9ddbc1a39e10cc9de3dedd372698d5309f9f5bacfacb76bf3db`.

Reusable source, component/frame, construction, feature-check and saved-file procedure.

Repository skill instructions and reproduction-package specification.

## ocs-skill-improvements.md — ferme-ocs

Original: ocs-skill-improvements.md (`${FERME_ROOT}/skills/ocs-skill-improvements.md`). Evidence: `proposed_skill_extension`. SHA-256: `cf8ded1155c0984063a2c634eb4b741e9d22b2baadd4c218ba15814e5f4c5e10`.

Proposed OCS additions derived from recorded commands, topology recovery and representation/display observations.

Held in ferme; installation is a separate action.

## README.md — ferme-readme

Original: README.md (`${FERME_ROOT}/skills/README.md`). Evidence: `evidence_index`. SHA-256: `852b9f2ee0efe7689d85d8e182693aa9e895c33202c3907f991c4b80d4da857e`.

Scope, source session/review boundary, OCS build and document use order.



## SKILL.md — ocs-skill

Original: SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`). Evidence: `installed_skill_source`. SHA-256: `d910a4f545aa1575bed507f7b27c9e5476404cfe6a9ce21db5259d1248df8058`.

Existing OCS contract, guarded control, revision-bound readback, preservation and handoff instructions.



## ocs_control.py — ocs-control

Original: ocs_control.py (`${CODEX_HOME}/skills/ocs-engineering/scripts/ocs_control.py`). Evidence: `existing_code`. SHA-256: `ceae138056ec8d0522181706fd686bf19936814fe13337cb89dd0dd197949f8e`.

request, execute_checked and redact implement authenticated transport, preflight revision checks, one-send writes and uncertain-result identity.

Inspected source only this batch; session descriptors are excluded from inspection/output. READ_OPS includes guide although the recorded OCS build rejects it.

Entry points: `ControlError` (line 19), `WriteUncertain` (line 23), `redact` (line 29), `load_descriptor` (line 38), `candidate_paths` (line 49), `request` (line 60), `descriptors` (line 81), `execute_checked` (line 95), `main` (line 127).

Dependencies: `import argparse`; `import json`; `import os`; `import socket`; `import sys`; `from pathlib import Path`.

## check_contract.py — measurement-checker

Original: check_contract.py (`${CODEX_HOME}/skills/ocs-engineering/scripts/check_contract.py`). Evidence: `existing_code`. SHA-256: `e64e24976352c5c9ecb74a6729b6e67a1847d608c78a84e2bd27d7535f7603a8`.

run checks supplied point/axis/plane observations, finite numbers, units, evidence identities and numerical criteria.

Consumes supplied observations; acquisition and solid/topology verification belong to other code.

Entry points: `number` (line 9), `vector` (line 17), `dot` (line 23), `sub` (line 27), `cross` (line 31), `norm` (line 35), `normalized` (line 39), `run` (line 46), `main` (line 140).

Dependencies: `import argparse`; `import json`; `import math`; `import sys`.

## ngv064_ocs.py — native-wrapper

Original: ngv064_ocs.py (`${TEMP_ROOT}/opencode/ngv064_ocs.py`). Evidence: `existing_component_code`. SHA-256: `68a0204cc78b8d46210fbf1498e015a0666f94cb5287427219c0188a23f53b71`.

read/write/step, checkpoint, revolve_z, cylinder and subtract wrap native requests and stepped command state.

Fixed session, temporary paths/prefix allowlist; module import selects a descriptor; accepted/running polling is unbounded; write treats waiting_input as failure, while step permits it.

Entry points: `configure` (line 22), `read` (line 32), `write` (line 37), `checkpoint` (line 51), `added` (line 54), `run` (line 57), `select` (line 59), `new` (line 61), `revolve_z` (line 72), `cylinder` (line 85), `subtract` (line 88), `step` (line 105), `tag` (line 116).

Dependencies: `import importlib.util`; `import json`; `from pathlib import Path`.

## item_ocs_parts.py — item-geometry

Original: item_ocs_parts.py (`${TEMP_ROOT}/opencode/item_ocs_parts.py`). Evidence: `existing_component_code`. SHA-256: `500d72af1767b433d521737a7aa2db2c268db9caa34aad357d5bc84fcd774bd4`.

extrude, rotate, move, combine and tag provide explicit source-labelled native constructions.

Imports native-wrapper; dimensions and several recipes are ITEM-specific.

Entry points: `tag` (line 5), `move` (line 13), `rotate` (line 15), `extrude` (line 19), `combine` (line 25), `nut` (line 32), `washer` (line 47), `screw` (line 53).

Dependencies: `import math`; `import ngv064_ocs as n`.

## check_ngv064_wheel.py — sat-reader

Original: check_ngv064_wheel.py (`${TEMP_ROOT}/opencode/check_ngv064_wheel.py`). Evidence: `existing_component_code`. SHA-256: `1d8f89b4b2b5701b694d194e980112897425137390f09593b44cd64c328c60c4`.

sat_features extracts selected SAT cylinders, planes, tori and points; verify checks the wheel.

Top-level import loads native-wrapper. Restricted SAT fields; one body transform, unit scale; SAB requires a separate supported reader.

Entry points: `sat_features` (line 9), `verify` (line 37).

Dependencies: `import json`; `import math`; `from pathlib import Path`; `import ngv064_ocs as n`.

## build_item_profile_segment.py — profile-build

Original: build_item_profile_segment.py (`${TEMP_ROOT}/opencode/build_item_profile_segment.py`). Evidence: `existing_component_code`. SHA-256: `80d3fe7fd2308a26dda4133748c54d478a085ca381a423a60362dbf966324521`.

contours samples retained text curves and normalizes the section; build/complete/verify construct and check the profile.

Uses extracted contour text rather than a DXF parser; fixed 40 mm normalization, 100 mm length, output paths, session wrapper and component checks.

Entry points: `contours` (line 16), `area` (line 46), `build` (line 48), `complete` (line 58), `verify` (line 76).

Dependencies: `import json`; `import math`; `import re`; `from pathlib import Path`; `import ngv064_ocs as n`; `from item_ocs_parts import extrude,tag`; `from check_ngv064_wheel import sat_features`.

## battery_ocs_parts.py — battery-geometry

Original: battery_ocs_parts.py (`${TEMP_ROOT}/opencode/battery_ocs_parts.py`). Evidence: `existing_component_code`. SHA-256: `ccf4bccc801c1315c0289c509e7f91681754c72fd65b89b5827f18de7b7c5159`.

rr, axial_x, face_x and tag reuse rounded sections, transforms and metadata.

Imports item and session wrappers; caller must supply source-backed geometry.

Entry points: `rr` (line 6), `tag` (line 19), `axial_x` (line 26), `face_x` (line 29).

Dependencies: `import math`; `import ngv064_ocs as n`; `from item_ocs_parts import extrude,rotate,move,combine`.

## build_leaf_gen2.py — leaf-build

Original: build_leaf_gen2.py (`${TEMP_ROOT}/opencode/build_leaf_gen2.py`). Evidence: `existing_component_code`. SHA-256: `4d6f8eb52addd7a4c5b3ee687cd3118364360a7a162713e6185101b369bb9ef7`.

top and staged recovery functions reconstruct shell/terminal features; finish checks and saves the component.

Component-specific dimensions and staged resumption; imports shared battery/item/wrapper/SAT modules.

Entry points: `top` (line 17), `after_cavity` (line 26), `after_hollow` (line 31), `after_pan` (line 37), `rest` (line 52), `finish` (line 68).

Dependencies: `import json`; `from pathlib import Path`; `import ngv064_ocs as n`; `from battery_ocs_parts import rr,tag,axial_x,face_x`; `from item_ocs_parts import rotate,move,combine`; `from check_ngv064_wheel import sat_features`.

## build_bmw_i3_94ah.py — bmw-build

Original: build_bmw_i3_94ah.py (`${TEMP_ROOT}/opencode/build_bmw_i3_94ah.py`). Evidence: `existing_component_code`. SHA-256: `4bacd498f12f1dab482e6cb5f050e8a7dc2c5efc61473ee2127d2e8be5fa5c16`.

build/accessories/cable_done/finish reconstruct exterior parts and swept cable with checks.

Component-specific dimensions, paths and cable pose; imports shared battery/item/wrapper/SAT modules.

Entry points: `box` (line 18), `label` (line 21), `build` (line 25), `accessories` (line 60), `cable_done` (line 87), `finish` (line 98).

Dependencies: `import json,math`; `from pathlib import Path`; `import ngv064_ocs as n`; `from battery_ocs_parts import rr,tag,face_x`; `from item_ocs_parts import extrude,move,rotate,combine`; `from check_ngv064_wheel import sat_features`.

## build_workflow_register.py — register-builder

Original: [build_workflow_register.py](../../tools/build_workflow_register.py). Evidence: `existing_documentation_code`. SHA-256: `e7bc20940a4b1e3594ad29316c928aa7e4167edb37ce378495bcb8cae9a9195e`.

Existing read_json, write_json and sid conventions plus local-evidence/register handling provide source-record precedents.

Uses project-global paths and report scanning; a per-job source intake adapter needs its own interface and tests.

Entry points: `read_json` (line 17), `write_json` (line 21), `sid` (line 25), `clean` (line 29), `urls` (line 35), `main` (line 47).

Dependencies: `from __future__ import annotations`; `import argparse`; `import hashlib`; `import json`; `import re`; `from pathlib import Path`.

## neugart-ngv064-wheel-160.md — wheel-report

Original: neugart-ngv064-wheel-160.md (`${FERME_ROOT}/engineering/module-development/cad/checks/neugart-ngv064-wheel-160.md`). Evidence: `recorded_execution_report`. SHA-256: `9ef13208ea35beabc65104ee0e807ee65915446f3a449b6bf8419525eca7bef2`.

Component-specific native checks, save/reopen observations and source paths for OCS 2026.42.



## item-profile-02633-segment-100mm.md — profile-report

Original: item-profile-02633-segment-100mm.md (`${FERME_ROOT}/engineering/module-development/cad/checks/item-profile-02633-segment-100mm.md`). Evidence: `recorded_execution_report`. SHA-256: `d9f68c3ed038b1e39649437594fade9db78f1412ace69a832436fa3f4aca8f8d`.

Component-specific native checks, save/reopen observations and source paths for OCS 2026.42.



## neugart-ngv064-wheel-160-native.json — wheel-checks

Original: neugart-ngv064-wheel-160-native.json (`${FERME_ROOT}/engineering/module-development/cad/checks/neugart-ngv064-wheel-160-native.json`). Evidence: `recorded_check_results`. SHA-256: `ba3fd46f29645a8434aed14f217ab5320836c5f13404885287c8359133964b98`.

Retained feature/audit observations for the named component.

Pre-save stage; transfer conditions are retained in the matching report.

Retained check observations: {"count": 14, "statuses": {"PASS": 14}, "document_id": 51, "revision": 137, "geometry_revision": 5508}.

## item-angle-bracket-set-41115-native.json — bracket-checks

Original: item-angle-bracket-set-41115-native.json (`${FERME_ROOT}/engineering/module-development/cad/checks/item-angle-bracket-set-41115-native.json`). Evidence: `recorded_check_results`. SHA-256: `df42709bbd7bc2a10102c5e7c7559667baa1aa0bba44eab57dce407ba5b7318f`.

Retained feature/audit observations for the named component.

Pre-save stage; transfer conditions are retained in the matching report.

Retained check observations: {"count": 21, "statuses": {"PASS": 21}, "document_id": 59, "revision": 186, "geometry_revision": 7634}.

## item-profile-02633-segment-100mm-native.json — profile-checks

Original: item-profile-02633-segment-100mm-native.json (`${FERME_ROOT}/engineering/module-development/cad/checks/item-profile-02633-segment-100mm-native.json`). Evidence: `recorded_check_results`. SHA-256: `7bae7ea075ac2a41d001518863889e6a593f24d25cbaa0c5a3556cadf3cdab58`.

Retained feature/audit observations for the named component.

Pre-save stage; transfer conditions are retained in the matching report.

Retained check observations: {"count": 11, "statuses": {"PASS": 11}, "document_id": 61, "revision": 22, "geometry_revision": 7756}.

## nissan-leaf-gen2-native.json — leaf-checks

Original: nissan-leaf-gen2-native.json (`${FERME_ROOT}/engineering/module-development/cad/checks/nissan-leaf-gen2-native.json`). Evidence: `recorded_check_results`. SHA-256: `d91733280a6fc484e9f769e3af1746145401331d8148a5ef0bbbd4ae827cafc8`.

Retained feature/audit observations for the named component.

Pre-save stage; transfer conditions are retained in the matching report.

Retained check observations: {"count": 14, "statuses": {"PASS": 14}, "document_id": 63, "revision": 192, "geometry_revision": 8590}.

## bmw-i3-94ah-native-checks.json — bmw-checks

Original: bmw-i3-94ah-native-checks.json (`${FERME_ROOT}/engineering/module-development/cad/checks/bmw-i3-94ah-native-checks.json`). Evidence: `recorded_check_results`. SHA-256: `18c6149a67d9397172579eab59855e397d035866225bef1fae7b79e22682d619`.

Retained feature/audit observations for the named component.

Pre-save stage; transfer conditions are retained in the matching report.

Retained check observations: {"count": 13, "statuses": {"PASS": 13}, "document_id": 65, "revision": 287, "geometry_revision": 9882}.
