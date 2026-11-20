---
name: cad-source-intake
description: Register a CAD job's source revisions, scope and corrections. Select and run a supplied vision endpoint or local segmentation model when the job requires grounded image observations.
---

# Record source files, revisions and job scope

Use the [operation selection procedure](references/modeling-operation-selection.md) for component reuse, provider capability checks and job evidence. Apply it to the requested operation. Open the local operation catalogue on first use and after a request to refresh available skills.

Use for **Preserve the input revision and state the job boundary (INTAKE-A01)**. Read the existing job record first. Reuse a completed intake whose request, source observations and scope match the current task. A changed source or instruction creates a new revision referring to the completed prior index.

## Package setup

Set `SKILL_ROOT` to this installed skill directory, containing `SKILL.md`, `scripts/` and `requirements.txt`. Run with Python 3.12 on Linux or macOS; the source revision helpers use only the standard library. `SOURCE_ROOT` is your caller-owned input/output directory.

```sh
python3 "$SKILL_ROOT/scripts/package_check.py"
```

## Prepare the input

1. Read the request and source records. Supply a readable `job_name`, unique `revision_id` and actual agent `model` identity where available. `request.text` preserves the exact request; `request.location` identifies its message/document location.
2. Supply `scope.statement`, `scope.requested_output` and absolute `scope.authorized_paths`. The agent writes these from the actual authorization. Software preserves the statement; it does not decide the task's authorization.
3. Every `sources` entry has `id`, `title`, a concrete `summary`, `kind`, exact `locator` and ISO `observed_at`. Supported kinds: `file` with an absolute local path; `text` with an exact `text` field; `url` with the original HTTP(S) URL. File and text sources may supply `expected_sha256` to pin expected bytes.
4. Optional `parent_id` points to another source in this revision. Optional `corrections` entries contain `id`, `source_id`, exact `statement` and `location`. Optional `conflicts` contain at least two distinct `source_ids`, a `summary` and `affected_scope`. Retain the source's declared evidence fields; the tool records actual observation state separately.
5. Optional `prior_revision` is the absolute path to an earlier completed `source-index.json`. The tool verifies that prior index and scope against their receipt, checks job identity, and requires a new revision ID. Changed bytes and changed locators are recorded independently.

## Execute

```sh
python3 ${SKILL_ROOT}/scripts/source_intake.py \
  --input ${SOURCE_ROOT}/job-input.json \
  --output ${SOURCE_ROOT}/new-intake-directory
```

1. Reuses `part_index.parse_json` for duplicate-key/nonfinite-token rejection and `component_records.observe_file` for streaming hashes with change detection. Additional validation checks references, cycles, dates, required scope fields and overflowing numeric input.
2. Reserves the requested new output directory exclusively. Existing completed and incomplete attempts are preserved.
3. Writes a staged source index, scope Markdown and receipt. Validates the artifact hashes, then atomically publishes the `revision` subdirectory. Files are `revision/source-index.json`, `revision/scope.md`, and `revision/receipt.json`.
4. A source conflict or I/O/publication failure after reservation leaves `failure.json` and an `incomplete` directory under that attempt. Inspect the named failure. Corrected input uses a new output path; an existing attempt is preserved.
5. Exit codes: `0` completed; `1` source observation/hash conflict; `2` invalid input or other I/O/publication failure. A supplied URL is registered locally with `network_requests: 0`.

## Check and hand off

1. Call `source_intake.verify_revision(path_to_source_index)` to verify the completed index/scope hashes against the receipt.
2. The agent compares the recorded request, scope, corrections and affected source conflicts. Numerical capture checks establish source identity and output integrity. Source interpretation retains its own action.
3. Hand the completed revision to **Select the execution mode and define candidate branches (INTAKE-A02)**. Preserve the source/revision IDs in its inputs. Required source-priority decisions affect the named dependent feature.
4. Keep each supplied input, source index, receipt and execution result together in caller-owned persistent storage. Bind subsequent work to the exact retained revision.

## Verification

Run the bundled `scripts/package_check.py` to check package hashes and imports. After intake, call `source_intake.verify_revision()` on the completed source index to check the published index and scope against their receipt. Preserve source conflicts, corrections and interrupted publication as explicit results.

## Hand-drawn concepts

When the input is a freehand design sketch, record its kind as a file and identify it as a concept sketch in the summary. Preserve the sketch, page orientation, accompanying description and corrections as one input revision. Keep distinct design alternatives identifiable. Hand drawing inspection the original page and the decision needed, such as identifying hardware, interpreting motion or locating a mounting feature. Pin subsequent observations to this source hash and page.

## Image observations

Record image kind, stored pixel size, page, orientation, crop, resize and padding in the source revision. Keep the original file and any decoded response with their hashes. Select the required output (text, point, box, polygon or instance mask). Inspect a supplied endpoint's deployed schema and model, run a labeled case, and record the actual response, latency, cost and corrections. Keep service credentials outside the record.

For a decoded response, run the tested image interpreter with [image_observations.py](scripts/image_observations.py) SOURCE RECEIPT NEW_OUTPUT. Supply source_sha256, provider, provider_size_px, a 3 × 3 source_from_provider pixel-center matrix and instances. Each instance has an id and kind. A mask carries a 0/1 array in provider coordinates. A point, polygon, box or text region carries points (four ordered corners for a box or text). Text also carries its string. Convert normalized or box-relative coordinates according to the deployed schema first. Inspect the overlay and retain the instance ID, parent response hash and correction prompt across revisions. Return to catalogue lookup when a designation becomes legible. Use the catalogued interpreter that passed the image operation. If it fails, preserve the observation and use the next suitable route.

For a local prompted segmentation model, run [sam_mask.py](scripts/sam_mask.py) SOURCE LOCAL_SAM_DIRECTORY PROMPT_JSON NEW_RECEIPT in an interpreter with Transformers, Torch and Pillow. The tested CPU checkpoint is SlimSAM-uniform-77. Supply a single instance, for example `{"id":"plate","box":[16,16,264,184]}`. Coordinates refer to the stored image pixels. For a correction, retain the id and full intended prompt, add points such as `"points":[[88,88,0]]` (0 for background, 1 for foreground), and pass `--parent PREVIOUS_RECEIPT`. Run the receipt through image_observations.py. Inspect each required opening against the source before passing the mask to drawing inspection. The model score ranks mask candidates. Evaluate geometric accuracy against independent evidence.

### Select and run a deployed image provider

For each placement, outline or identification task name the missing feature. First check whether the matching indexed model or existing trace already resolves it. Choose a view that exposes that feature. Record the observed side or region in the source frame. When the selected model derives from the same photo, cite that single observation for both.

Run the selected image interpreter with [vision_provider.py](scripts/vision_provider.py) SOURCE CONFIG NEW_DIRECTORY. It sends one JSON POST directly to the user-supplied inference endpoint for an already loaded model. Skill installation and execution must never download model files. Select the endpoint and permitted image before transmission. A config declares the deployed model, wire format, payload and response location. The request builder substitutes complete string values `$model`, `$prompt`, `$image_base64` and `$image_data_url`. A `response_path` is a list of object keys and array indices. For an offline response use `--response FILE` and include the matching original image `source_sha256` in CONFIG.

1. **Qwen localization.** For an OpenAI-compatible deployment use format `qwen`, the deployed model ID, endpoint URL and `response_path: ["choices",0,"message","content"]`. Supply the deployment's message body with a user text prompt and image data URL. Request a JSON list of objects with `label` and `bbox_2d`. Set `coordinate_units` to `pixels`, `normalized` (0–1), or `normalized1000` for the deployed output convention. If pixel units refer to a transformed model image, give its `provider_size_px` and `source_from_provider` matrix. For an automated handoff, pass the resulting observations.json to vision_provider_sam2.py with `--grounding OBSERVATIONS` and a prompt such as `{"id":"plate","box_observation_id":"plate-1"}`. The segmenter checks the source hash and frame, bounds the detected corners in stored pixels and retains the observation ID and receipt hash.
2. **Moondream segmentation.** With optional CairoSVG in the image interpreter, format `moondream` accepts a normalized `bbox` and a box-relative SVG `path`. Example payload: `{"model":"$model","image_url":"$image_data_url","object":"$prompt"}`. Set `instance_id` for the requested object. The decoder scales the path within the returned box, rasterizes at the declared resolution using SVG fill semantics and returns a binary mask. Check holes, thin regions and the overlay.
3. **YOLO and other servers.** A YOLO server finds instances from the image alone. A detection deployment returns boxes. A segmentation deployment can additionally return polygons. The server client uses Pillow and NumPy for source-frame normalization. For local inference only, select an existing Ultralytics and Torch environment and replace the endpoint and payload with an absolute `local_checkpoint` path to an existing trusted detection or segmentation `.pt` file. Set `format` to `yolo`, `coordinate_units` to `pixels` and supply the `model` identity. Both routes use the same result reader. Format `yolo` accepts Ultralytics JSON rows with `name`, `box` and optional `segments.x/y`. Set coordinate units from the actual endpoint. Each detection gets a stable ID within that response. Format `instances` accepts a response field carrying already decoded box, mask, polygon, point or text instances in the existing intake contract. These formats use the caller's JSON payload and response selector.
4. **LISA language masks.** For a deployment returning the restored per-image segmentation logits choose format `lisa` and select the N×H×W array with `response_path`. Each positive logit is foreground. Preserve multiple referenced masks and an empty detection. In an existing LISA Python deployment the supplied `evaluate_lisa` bridge invokes its loaded model with prepared input tensors, tokenizer, resize and original H×W. Its `pred_masks` field can feed this decoder.
5. **Request and readback.** For a credential use an environment reference such as `"auth":{"header":"Authorization","prefix":"Bearer ","env":"VISION_TOKEN"}`. Version or task selectors may appear in the endpoint query. For a query credential use `"query_from_env":{"api_key":"VISION_TOKEN"}`. Select the transport appropriate for the deployed service. Use Moondream's deployed header for that service. The output retains the raw JSON response, provider-frame receipt, source-frame observations and overlay. Retain the caller's config without its environment secrets. Compare results with known features before treating the deployment as qualified.

### Local SAM 2 correction with previous logits

Run [vision_provider_sam2.py](scripts/vision_provider_sam2.py) SOURCE LOCAL_SAM2_DIRECTORY PROMPT_JSON NEW_RECEIPT using Transformers with Sam2Model, Torch and Pillow. Prompt boxes and signed points use the same format as the local SAM route. The SAM 2 receipt includes the selected low-resolution logits, their shape and hash. For refinement, supply the full intended box and points with `--parent PREVIOUS_RECEIPT`. It checks checkpoint, image and instance identity and passes the restored logits to the mask decoder. Use image_observations.py for overlay and original-frame conversion. Check foreground polarity and the count of required openings when a grounded box covers most of the image. A high model score can select background. Choose the revision that preserves the features needed downstream.
