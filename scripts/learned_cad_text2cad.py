"""Invoke the pinned external Text2CAD implementation offline or rebuild a saved token sequence."""

import argparse
import hashlib
import json
from local_model_runtime import offline_model_libraries
from pathlib import Path
import subprocess
import sys

REVISION = "669a81472ede2269837c22a4d00070eaac360c82"


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def checkout(root):
    root = root.resolve()
    head = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
    ).strip()
    if (
        head != REVISION
        or subprocess.run(
            ["git", "-C", str(root), "diff", "--quiet", "HEAD", "--"]
        ).returncode
    ):
        raise ValueError(f"Select the clean Text2CAD source revision {REVISION}")
    sys.path.insert(0, str(root))
    return root


def infer(args, root):
    supplied_hash = digest(args.checkpoint)
    if supplied_hash != args.sha256:
        raise ValueError("Checkpoint hash differs from the supplied SHA-256")
    if not args.encoder.is_dir():
        raise ValueError(
            "Supply the local google-bert/bert-large-uncased tokenizer and model directory"
        )
    import torch
    import yaml

    if not torch.cuda.is_available():
        raise ValueError(
            "The pinned Text2CAD text embedder requires CUDA for token embedding"
        )
    from CadSeqProc.utility.macro import MAX_CAD_SEQUENCE_LENGTH
    from Cad_VLM.models.layers.text_embed import MODEL_NAME_DICT
    from Cad_VLM.models.text2cad import Text2CAD

    config = yaml.safe_load(
        (root / "Cad_VLM/config/inference_user_input.yaml").read_text()
    )
    MODEL_NAME_DICT["bert_large_uncased"] = str(args.encoder.resolve())
    config["text_encoder"]["text_embedder"]["cache_dir"] = str(args.encoder.resolve())
    decoder = dict(config["cad_decoder"], cad_seq_len=MAX_CAD_SEQUENCE_LENGTH)
    model = Text2CAD(text_config=config["text_encoder"], cad_config=decoder).to("cuda")
    weights = torch.load(args.checkpoint, map_location="cpu", weights_only=True)[
        "model_state_dict"
    ]
    state = {key.removeprefix("module."): val for key, val in weights.items()}
    missing, unused = model.load_state_dict(state, strict=False)
    if any(not key.startswith("base_text_embedder.model.") for key in missing):
        raise ValueError(f"Checkpoint lacks trained inference parameters: {missing}")
    prompt = args.prompt.read_text().strip()
    if not prompt:
        raise ValueError("Prompt is empty")
    model.eval()
    with torch.inference_mode():
        result = model.test_decode(
            texts=[prompt],
            maxlen=MAX_CAD_SEQUENCE_LENGTH,
            nucleus_prob=0,
            topk_index=1,
            device="cuda",
        )
    return dict(
        tokens=result["cad_vec"][0].cpu().tolist(),
        prompt=prompt,
        checkpoint_sha256=supplied_hash,
        source_revision=REVISION,
        unused_checkpoint_keys=unused,
        encoder_files={
            p.name: digest(p) for p in sorted(args.encoder.iterdir()) if p.is_file()
        },
    )


def run(args):
    offline_model_libraries()
    root = checkout(args.checkout)
    if args.mode == "infer":
        record = infer(args, root)
    else:
        record = json.loads(args.sequence.read_text())
        if record["source_revision"] != REVISION:
            raise ValueError(
                "Sequence was recorded against a different vocabulary revision"
            )
    import numpy as np
    from CadSeqProc.cad_sequence import CADSequence
    from CadSeqProc.utility.macro import N_BIT, MAX_CAD_SEQUENCE_LENGTH

    tokens = np.array(record["tokens"])
    if (
        tokens.ndim != 2
        or tokens.shape[1] != 2
        or not 0 < len(tokens) <= MAX_CAD_SEQUENCE_LENGTH
        or not np.issubdtype(tokens.dtype, np.integer)
        or tokens.min() < 0
    ):
        raise ValueError("Expected integer pairs in the Text2CAD CAD vocabulary")
    job = args.new_directory
    job.mkdir()
    (job / "sequence.json").write_text(json.dumps(record, indent=2) + "\n")
    cad = CADSequence.from_vec(tokens, bit=N_BIT, post_processing=True)
    cad.save_stp("solid", str(job))
    from OCC.Core.STEPControl import STEPControl_Reader
    from OCC.Core.IFSelect import IFSelect_RetDone
    from OCC.Core.BRepCheck import BRepCheck_Analyzer
    from OCC.Core.TopAbs import TopAbs_SOLID
    from OCC.Core.TopExp import TopExp_Explorer

    reader = STEPControl_Reader()
    path = job / "solid.step"
    if reader.ReadFile(str(path)) != IFSelect_RetDone or not reader.TransferRoots():
        raise ValueError("Reopening decoded STEP failed")
    shape = reader.OneShape()
    solids = TopExp_Explorer(shape, TopAbs_SOLID)
    if not solids.More() or not BRepCheck_Analyzer(shape).IsValid():
        raise ValueError("STEP result has no solid or is kernel-invalid")
    (job / "receipt.json").write_text(
        json.dumps(
            dict(
                step_sha256=digest(path),
                sequence_sha256=digest(job / "sequence.json"),
                valid=True,
                has_solid=True,
                scale_evidence="normalized model coordinates; explicit dimension checks required",
            ),
            indent=2,
        )
        + "\n"
    )


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    parsers = p.add_subparsers(dest="mode", required=True)
    for mode in ("infer", "rebuild"):
        sub = parsers.add_parser(mode)
        sub.add_argument("checkout", type=Path)
        if mode == "infer":
            sub.add_argument("checkpoint", type=Path)
            sub.add_argument("sha256")
            sub.add_argument("encoder", type=Path)
            sub.add_argument("prompt", type=Path)
        else:
            sub.add_argument("sequence", type=Path)
        sub.add_argument("new_directory", type=Path)
    try:
        run(p.parse_args())
    except (ImportError, ValueError, OSError, subprocess.SubprocessError) as exc:
        p.exit(2, str(exc) + "\n")
