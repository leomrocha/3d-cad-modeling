"""Offline feature checks and explicit live save/reopen checks."""

import hashlib
import math
from pathlib import Path

from .geometry import finite
from .runtime import CadError, Uncertain
from .records import identity


def close(a,b,tolerance):
    if finite(tolerance)<0:
        raise CadError("Negative comparison tolerance")
    return abs(finite(a)-finite(b))<=tolerance


def compare_observations(expected,observed,tolerance):
    """Expected values come from source inputs, observed values from a separate query."""
    if not expected:
        raise CadError("Nonempty expected feature set required")
    results = []
    for name,target in expected.items():
        actual = observed.get(name)
        result = "UNKNOWN" if actual is None else "PASS" if close(actual,target,tolerance) else "FAIL"
        results.append({"check":name,"expected":target,"observed":actual,
                        "numeric_tolerance":tolerance,"result":result})
    return results


def check_pattern(cylinders,diameter,pcd,angles,tolerance,angle_tolerance_deg):
    """Group coincident cylindrical patches by radius/axis/centre in the XY plane."""
    if not angles:
        raise CadError("Explicit expected angular coordinates required")
    if finite(tolerance)<0 or finite(angle_tolerance_deg)<0:
        raise CadError("Comparison tolerances must be nonnegative")
    # Ensure duplicate expected angles never silently pass.
    from .geometry import pattern
    pattern(pcd,angles)
    positions = []
    for c in cylinders:
        if not close(c["radius"],diameter/2,tolerance):
            continue
        x,y,_ = c["origin"]
        if not close(math.hypot(x,y),pcd/2,tolerance):
            continue
        axis = c["axis"]
        if not (close(axis[0],0,tolerance) and close(axis[1],0,tolerance)
                and close(abs(axis[2]),1,tolerance)):
            continue
        if not any(close(x,px,tolerance) and close(y,py,tolerance) for px,py in positions):
            positions.append((x,y))
    actual = sorted(math.degrees(math.atan2(y,x))%360 for x,y in positions)
    expected = sorted(a%360 for a in angles)
    # Match by circular distance rather than sorting across the 0/360 boundary.
    unmatched = actual.copy()
    matched = True
    for target in expected:
        options = [(min(abs(a-target),360-abs(a-target)),i) for i,a in enumerate(unmatched)]
        if not options:
            matched = False
            break
        distance,index = min(options)
        if distance>angle_tolerance_deg:
            matched = False
            break
        unmatched.pop(index)
    return {"check":"hole_pattern","result":"PASS" if matched and not unmatched else "FAIL",
            "expected_angles_deg":expected,"observed_angles_deg":actual,
            "diameter_mm":diameter,"pcd_mm":pcd,"length_tolerance_mm":tolerance,
            "angle_tolerance_deg":angle_tolerance_deg}




def compare_captures(first,second,camera_changed):
    hashes = [hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in [first,second]]
    return {"sha256":hashes,"result":"FAIL" if camera_changed and hashes[0]==hashes[1] else "UNKNOWN",
            "method":"image_hash_diagnostic","meaning":"Different bytes still require content/document inspection"}


def require_audit(audit):
    if audit.get("summary")!={"errors":0,"warnings":0}:
        raise CadError("Target audit has errors/warnings or lacks summary")
    return audit["manifest"]


def owned_audit(client, *, target_path=None, expected_path=None, expected_sha256=None):
    """Bind audit to a stable active document and optional persisted source pin."""
    before = identity(client.read("state"))
    if before[0] != client.document_id:
        raise CadError("Audit target document is inactive")
    options = {"target_format": "dwg", "target_version": "2018"}
    if target_path is not None:
        options["path"] = str(target_path)
    audit = client.read("audit", **options)
    if audit.get("document_id") != before[0] or identity(client.read("state")) != before:
        raise CadError("Audit document or revision identity differs")
    if expected_path is not None:
        source = audit.get("source", {})
        if source.get("path") != str(expected_path) or source.get("sha256") != expected_sha256:
            raise CadError("Reopened audit source path/hash differs")
    return audit


def save_reopen(client,path,expected_counts):
    """Explicit existing-document save; no overwrite, format conversion or cleanup."""
    target = Path(path)
    if not target.is_absolute() or target.suffix.lower()!=".dwg" or target.exists():
        raise CadError("A new absolute .dwg destination is required")
    before = owned_audit(client, target_path=target)
    manifest = require_audit(before)
    if manifest.get("by_type")!=expected_counts:
        raise CadError("Unexpected entity types/counts before save")
    save = client.mutate("verified-save","save_verified",path=str(target),
                         target_format="dwg",target_version="2018")
    result = save["result"]
    if result.get("dropped_on_save")!=0 or result.get("manifest")!=manifest or result.get("verified") is not True:
        raise CadError("Saved data differs; preserve output for diagnosis")
    if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest()!=result.get("sha256"):
        raise CadError("Saved output hash does not match file")
    previous=client.document_id
    try:opened=client.mutate("reopen","open",path=str(target))
    except Uncertain:opened=client.recover(client.namespace+':reopen')
    created=opened.get('state',{}).get('document_id')
    if type(created) is not int or created==previous:raise CadError('Exact OPEN response must identify reopened document')
    state = client.helper.request(client.descriptor,{"op":"state"},client.timeout)
    active = next((d for d in state.get("documents",[]) if d["id"]==state.get("document_id")),None)
    if not state.get("ok") or state.get('document_id')!=created or active is None or active.get("path")!=str(target):
        raise CadError("Reopened active document identity differs")
    client.document_id = state["document_id"]
    reopened = owned_audit(client, expected_path=target, expected_sha256=result["sha256"])
    if require_audit(reopened)!=manifest:
        raise CadError("Reopened manifest differs")
    if hashlib.sha256(target.read_bytes()).hexdigest()!=result["sha256"]:
        raise CadError("Saved output changed during reopen verification")
    return {"stage":"reopened","method":"audit_manifest_and_file_hash","sha256":result["sha256"],
            "saved_path":str(target),"reopened_document_id":created,
            "save":result,"reopened_audit":reopened,"result":"PASS"}
