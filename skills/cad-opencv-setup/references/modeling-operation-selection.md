# Choose the route for one modeling operation

Start with the requested result, known part identity, required geometry or output type, and checks. Respect a caller-selected operation or provider. Use this order when there is a choice.

1. Reuse an existing suitable component unchanged. Check project models and each user-supplied parts source through the CAD Models indexing method. Confirm the actual asset, variant, representation and mating features. A matching alias can identify several sizes.
2. Reuse an editable member of the correct family. Identify the exposed parameter, supported range or configuration, units and affected interfaces. Save a derivative, change only the intended parameter, rebuild, then check the requested dimension and one independent datum or interface. Preserve the original.
3. Run an existing script, generator, algorithm or service that delivers the required output with repeatable checks.
4. Use an available sub-skill or skill when interpretation, correction or user judgment is needed. Give it the relevant source, the unresolved feature and a concrete output to return.
5. Carry out only the uncovered operation. Preserve useful scripts, prompts, procedures, outputs and checks in the job so a later skill improvement can reuse them.

Choose the first suitable level. Within that level consider total setup time, compute or service cost, correction effort and verification effort. Reuse an earlier verified lookup or intermediate result for the same inputs. After identifying a component from an image, return to component lookup for that component. A drawing-inspection, translation or repair request with a supplied file starts at its requested operation.

## Set up and refresh the local operation catalogue

During setup, or on first call after copying a skill, run `python3 "$SKILL_ROOT/scripts/operation_catalogue.py" show`. Ordinary jobs read this saved catalogue. It is shared across the modeling skills at `$XDG_CONFIG_HOME/cad-modeling/operations.json` (default `~/.config/cad-modeling/operations.json`). An explicit `--catalogue FILE` before the command selects another catalogue. The CAD Models parts index supplies reusable geometry.

Show the existing resources, the discovered interpreter and any tools, skills, environments, model files, servers and parts sources the user has already identified. Ask which resources may be used, including the permitted fixture input for each server. Discovery alone grants no permission. For **“Refresh the available skills”**, show the saved selections and ask what to add, remove or change, including keeping the same list. Use already installed dependencies and existing model files. Refresh installs and downloads nothing.

Supply the complete confirmed list to `refresh --resources FILE`, or run `refresh` to repeat the saved checks. Each resource has a unique `id`, a `kind` and the selected paths or endpoint. Store absolute paths to the selected interpreter, owned helper directory and existing fixture files. Include only credential references. For example, a confirmed OpenCV environment is a JSON list with one object:

```json
[{"id":"drawing-python","kind":"opencv","python":"/selected/environment/bin/python"}]
```

This selection runs separate contour, plane and thinning fixtures in that interpreter. Other resources declare `location`, `python`, optional `scripts` (the owning installed package's scripts directory) and a `methods` list. Each method has a readable `name`, `input`, exact `output` and a `probe`. Give each distinct operation its own fixture. Use a positive sample with the expected object or feature.

| Probe | Resource and fixture fields | Checked output |
| --- | --- | --- |
| `vision` | Approved endpoint or local YOLO checkpoint as `location`, `sample` image and `config` for the source-intake client. Identify image-only, text, box or point prompts in `input`. | Actual source-frame instance of the requested kind, such as `box`, `polygon` or `mask` |
| `sam`, `sam2` | Local model directory as `location`, `sample` image and `prompt` JSON | `mask` with foreground pixels |
| `cad-sequence` | Chat endpoint as `location`, `model`, `sample` prompt file, optional `images` and `key_env` | `editable sequence` with features |
| `intake` | Source-intake helper directory and `sample` source specification | `source revision` with a revision index |
| `dxf` | Drawing-inspection helper directory and `sample` DXF | `entity inventory` with selected geometry |
| `parts` | CAD Models data directory as `location`, trusted local `search_cli` and known `query` | `part candidates` with a local asset hash |
| `guided` | Selected tool or skill and a named operation, including tools with interactive interfaces | Run that operation on its fixture and inspect its output. Record a successful fresh check with `observed RESOURCE METHOD EVIDENCE_FILE "input, output and checked property"`. |

The catalogue binds a server fixture to the exact sample, views and configuration approved at setup. A changed file needs confirmation before transmission. For a tool such as OpenCADStudio, a translator or a navigation skill, name the selected installation in `location` and use a `guided` fixture for each intended operation. For example, inspect a known saved assembly and verify a named occurrence in the returned tree. During refresh, run each guided fixture again using the approved resource. The catalogue clears its previous qualification until the new output has been checked. Report the operations that became available or unavailable, including the final results of guided checks. A resource can remain listed with its exact failed requirement. Keep user selections and machine availability in this local catalogue.

For a job, use `routes OUTPUT` for the checked methods with the needed result. If one fails, use `failed RESOURCE METHOD "specific error"` and try the next suitable route in the reuse order. For an outline, reuse a saved trace, run a qualified contour or segmentation method, or trace the image with guidance. A detection box locates the region for a subsequent trace. Verify the contour, polygon or mask needed by the downstream operation. When every route falls short, report the exact missing output.

## Choose a provider by its actual capability

Ordinary skill execution, including helpers and subprocesses, uses existing packages and model files. A missing dependency skips that method. Skill installation and execution must never download models, weights, tokenizers or processors. Use a model only when its required files already exist locally or the user supplies a running inference service with that model already loaded. Use inference operations only. Skip unavailable models and services that fetch files on demand. Apply the same rule to tests and examples.

Identify the available local algorithms, scripts, models and user-supplied servers relevant to the operation. Inspect the selected deployment's tool schema, model/task metadata or API documentation. Match its inputs and actual outputs to the job. Use its declared API and configured client; do not assume a common endpoint format. Use a small job-relevant sample if capability or coordinate conventions need confirmation.

For an image operation, distinguish descriptions, class labels, boxes, point prompts, raster masks and polygons. A YOLO detection deployment can propose boxes. A segmentation deployment may return masks or polygons. A VLM may read markings, ground an object or emit a mask when its interface supports that output. Record original image dimensions, crop/resize/padding transforms, coordinate convention and instance IDs. Map the result back to source pixels and check the target boundary or feature. Forward a box to a compatible segmenter when a mask is required. Use an agent or user to correct the specific ambiguous instance or boundary when needed. Metric dimensions require separate scale evidence.

## Record the route in the existing job log

For direct reuse, record source/index revision, asset ID and hash and the match check. For a derivative, add the parent hash, parameter edit, output and readback. For a tool call, record the script or provider, model/version if exposed, inputs, settings, returned artifact and check. For guided or new work, also keep the useful prompt, correction and reusable script or procedure. Record why a higher-priority route was unsuitable when that affects the decision. Keep credentials outside logs. Retain evidence locally under the owning project's rules.
