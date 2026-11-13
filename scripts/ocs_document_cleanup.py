"""Safely close one active OCS document owned by a completed CAD job.

The caller supplies explicit ownership and saved-persistence evidence. This
module never selects, activates, saves, or edits a document.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import re


class CleanupError(ValueError):
    """Invalid cleanup evidence or malformed OCS session state."""


def _document_id(value, field):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise CleanupError(f"{field} must be a nonnegative integer")
    return value


def _revision(value, field):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise CleanupError(f"{field} must be a nonnegative integer")
    return value


def _required_text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise CleanupError(f"{field} must be a nonempty string")
    return value


def _absolute_path(value, field):
    value = _required_text(value, field)
    if not Path(value).is_absolute():
        raise CleanupError(f"{field} must be an absolute runtime path")
    return value


def _owned_documents(rows):
    if not isinstance(rows, (list, tuple)) or not rows:
        raise CleanupError("owned_documents must be a nonempty list")
    result = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise CleanupError(f"owned_documents[{index}] must be an object")
        identity = _document_id(row.get("document_id"),
                                f"owned_documents[{index}].document_id")
        if identity in result:
            raise CleanupError(f"duplicate owned document ID {identity}")
        expected_path = row.get("expected_path")
        if expected_path is not None and (not isinstance(expected_path, str)
                                          or not expected_path.strip()
                                          or not Path(expected_path).is_absolute()):
            raise CleanupError(
                f"owned_documents[{index}].expected_path must be an absolute path or null")
        _revision(row.get("expected_geometry_revision"),
                  f"owned_documents[{index}].expected_geometry_revision")
        if type(row.get("dirty_discard_allowed")) is not bool:
            raise CleanupError(
                f"owned_documents[{index}].dirty_discard_allowed must be boolean")
        if type(row.get("construction_copy")) is not bool:
            raise CleanupError(
                f"owned_documents[{index}].construction_copy must be boolean")
        if row["dirty_discard_allowed"] and not row["construction_copy"]:
            raise CleanupError(
                "dirty discard is allowed only for an owned construction copy")
        saved_path = _absolute_path(row.get("saved_model_path"),
                                    f"owned_documents[{index}].saved_model_path")
        saved_hash = row.get("saved_model_sha256")
        if not isinstance(saved_hash, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", saved_hash):
            raise CleanupError(
                f"owned_documents[{index}].saved_model_sha256 must be a SHA-256 digest")
        receipt = row.get("persistence_receipt")
        if not isinstance(receipt, dict):
            raise CleanupError(
                f"owned_documents[{index}].persistence_receipt must be an object")
        result[identity] = {**row, "saved_model_path": saved_path,
                            "saved_model_sha256": saved_hash.lower()}
    return result


def _session_snapshot(state):
    if not isinstance(state, dict) or state.get("ok") is not True:
        raise CleanupError("OCS state read did not return ok=true")
    if state.get("command") not in (None, "") or state.get("modal") not in (None, ""):
        raise CleanupError("OCS command or modal state is active")
    active = _document_id(state.get("document_id"), "active document_id")
    rows = state.get("documents")
    if not isinstance(rows, list):
        raise CleanupError("OCS state documents must be a list")
    docs = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise CleanupError(f"documents[{index}] must be an object")
        identity = _document_id(row.get("id"), f"documents[{index}].id")
        if identity in docs:
            raise CleanupError(f"duplicate OCS document ID {identity}")
        if type(row.get("dirty")) is not bool:
            raise CleanupError(f"documents[{index}].dirty must be boolean")
        path = row.get("path")
        if path is not None and not isinstance(path, str):
            raise CleanupError(f"documents[{index}].path must be a string or null")
        title = row.get("title")
        if title is not None and not isinstance(title, str):
            raise CleanupError(f"documents[{index}].title must be a string or null")
        docs[identity] = {"path": path, "dirty": row["dirty"], "title": title}
    if active not in docs:
        raise CleanupError("active document_id is absent from OCS document list")
    geometry_revision = _revision(state.get("geometry_revision"),
                                  "active geometry_revision")
    return active, geometry_revision, docs


def _persistence_binding(receipt):
    """Read the caller-normalized passing receipt required by this helper."""
    if receipt.get("result") != "PASS":
        return None
    path = receipt.get("saved_path")
    digest = receipt.get("sha256")
    if not isinstance(path, str) or not path.strip() or not Path(path).is_absolute():
        return None
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
        return None
    return path, digest.lower()


def _file_sha256_once(path):
    """Hash a saved model once and reject a file changed during the read."""
    path = Path(path)
    before = path.stat()
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    after = path.stat()
    stable_fields = ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")
    if any(getattr(before, field) != getattr(after, field) for field in stable_fields):
        raise OSError("saved model changed while its hash was being checked")
    return digest.hexdigest()


def _blocked(status, reason, active, docs, owned, *, closed_document_id=None,
             request_id=None):
    return {
        "cleanup_status": status,
        "result": status,
        "reason": reason,
        "active_document_id": active,
        "remaining_owned_document_ids": sorted(set(docs) & set(owned)),
        "closed_document_id": closed_document_id,
        "close_confirmed": closed_document_id is not None,
        "request_id": request_id,
    }


def cleanup_active_owned_document(*, state_reader, client_factory,
                                  owned_documents, namespace,
                                  uncertain_type=None):
    """Close the active document only when its complete ownership proof passes.

    Args:
        state_reader: Callable returning the native OCS ``state`` response.
        client_factory: Callable ``(document_id, namespace) -> Client`` bound to
            that exact active document. The returned client must expose
            ``mutate(label, 'close', discard=...)`` and ``recover(request_id)``.
        owned_documents: Explicit evidence rows. Each row has ``document_id``,
            ``expected_path``, ``expected_geometry_revision``,
            ``construction_copy``, ``dirty_discard_allowed``,
            ``saved_model_path``, ``saved_model_sha256`` and a normalized
            ``persistence_receipt`` with ``result='PASS'``, ``saved_path`` and
            ``sha256``.
        namespace: Nonempty caller-owned stable request namespace.
        uncertain_type: Runtime ``Uncertain`` exception type. When omitted, it
            is imported lazily from ``cadtools.runtime``.

    Returns a cleanup-only status. It never changes a component's saved-model
    completion state and never activates another document.
    """
    if not callable(state_reader) or not callable(client_factory):
        raise CleanupError("state_reader and client_factory must be callable")
    _required_text(namespace, "namespace")
    owned = _owned_documents(owned_documents)
    state = state_reader()
    active, geometry_revision, docs = _session_snapshot(state)
    if active not in owned:
        return _blocked("ACTIVE_DOCUMENT_OUTSIDE_OWNED_SET",
                        "Active document is not in the caller's owned-document evidence.",
                        active, docs, owned)

    evidence = owned[active]
    observed = docs[active]
    if observed["path"] != evidence["expected_path"]:
        return _blocked("OWNERSHIP_PATH_MISMATCH",
                        "Active document path differs from the recorded owned path.",
                        active, docs, owned)
    if geometry_revision != evidence["expected_geometry_revision"]:
        return _blocked("GEOMETRY_REVISION_MISMATCH",
                        "Active geometry revision differs from the recorded owned epoch.",
                        active, docs, owned)
    if observed["dirty"] and not evidence["dirty_discard_allowed"]:
        return _blocked("DIRTY_DISCARD_NOT_AUTHORIZED",
                        "Dirty document is not an authorized construction copy.",
                        active, docs, owned)

    receipt = _persistence_binding(evidence["persistence_receipt"])
    if receipt is None:
        return _blocked("PERSISTENCE_RECEIPT_FAILED",
                        "Persistence receipt must pass and bind a saved path and SHA-256.",
                        active, docs, owned)
    receipt_path, receipt_hash = receipt
    allowed_receipt_paths = {evidence["saved_model_path"]}
    if evidence["expected_path"] is not None:
        allowed_receipt_paths.add(evidence["expected_path"])
    if receipt_path not in allowed_receipt_paths \
            or receipt_hash != evidence["saved_model_sha256"]:
        return _blocked("PERSISTENCE_RECEIPT_MISMATCH",
                        "Persistence receipt path or hash differs from saved-model evidence.",
                        active, docs, owned)
    try:
        actual_hash = _file_sha256_once(evidence["saved_model_path"])
    except OSError as error:
        return _blocked("SAVED_MODEL_UNAVAILABLE",
                        "Saved-model hash check failed: " + str(error),
                        active, docs, owned)
    if actual_hash != evidence["saved_model_sha256"]:
        return _blocked("SAVED_MODEL_HASH_MISMATCH",
                        "Saved model SHA-256 differs from caller evidence.",
                        active, docs, owned)

    if uncertain_type is None:
        try:
            from cadtools.runtime import Uncertain
        except ImportError as error:
            raise CleanupError("uncertain_type is required when cadtools.runtime is unavailable") from error
        uncertain_type = Uncertain
    if not isinstance(uncertain_type, type) or not issubclass(uncertain_type, BaseException):
        raise CleanupError("uncertain_type must be an exception class")

    client = client_factory(active, namespace)
    label = f"close-owned-document-{active}"
    request_id = namespace + ":" + label
    try:
        response = client.mutate(label, "close", discard=observed["dirty"],
                                 geometry_revision=geometry_revision)
    except uncertain_type:
        # Query the same stable request identity. Never replay the mutation.
        response = client.recover(request_id)
    except Exception as error:
        # The close request may be rejected by the runtime's fresh-state CAS.
        # Read state once to report the guard outcome; never retry the mutation.
        try:
            rejected_state = state_reader()
            rejected_active, rejected_revision, rejected_docs = _session_snapshot(rejected_state)
        except Exception:
            return _blocked("CLOSE_REJECTED_STATE_UNKNOWN",
                            "Close failed and its post-failure state could not be read.",
                            active, docs, owned, request_id=request_id)
        if active in rejected_docs and rejected_revision != geometry_revision:
            return _blocked("GEOMETRY_REVISION_CHANGED_BEFORE_CLOSE",
                            "The runtime rejected close after the geometry epoch changed.",
                            rejected_active, rejected_docs, owned, request_id=request_id)
        if active in rejected_docs:
            return _blocked("CLOSE_REJECTED", str(error), rejected_active,
                            rejected_docs, owned, request_id=request_id)
        return _blocked("CLOSE_OUTCOME_UNCERTAIN",
                        "Close raised an error and the owned document is absent; inspect its journal.",
                        rejected_active, rejected_docs, owned, closed_document_id=active,
                        request_id=request_id)
    response_result = response.get("result") if isinstance(response, dict) else None
    if not isinstance(response_result, dict) or response_result.get("closed") is not True:
        return _blocked("CLOSE_NOT_CONFIRMED",
                        "OCS did not confirm closure for the stable close request.",
                        active, docs, owned, request_id=request_id)

    after_state = state_reader()
    try:
        active_after, _, after_docs = _session_snapshot(after_state)
    except CleanupError as error:
        return _blocked("POSTCHECK_STATE_INVALID", str(error), active, docs, owned,
                        closed_document_id=active, request_id=request_id)
    if active in after_docs:
        return _blocked("POSTCHECK_DOCUMENT_REMAINS",
                        "Closed document ID remains in OCS state.",
                        active_after, after_docs, owned, closed_document_id=active,
                        request_id=request_id)
    expected_ids = set(docs) - {active}
    replacement_id = None
    if not expected_ids and len(after_docs) == 1:
        candidate_id, candidate = next(iter(after_docs.items()))
        if (candidate_id not in docs and candidate["path"] is None
                and candidate["dirty"] is False):
            replacement_id = candidate_id
    if set(after_docs) != expected_ids and replacement_id is None:
        return _blocked("POSTCHECK_DOCUMENT_SET_CHANGED",
                        "OCS document set changed beyond removal of the owned active document.",
                        active_after, after_docs, owned, closed_document_id=active,
                        request_id=request_id)
    changed = [identity for identity in expected_ids
               if any(after_docs[identity][key] != docs[identity][key]
                      for key in ("path", "dirty"))]
    if changed:
        return _blocked("POSTCHECK_OTHER_DOCUMENT_CHANGED",
                        "Other document path or dirty state changed: " +
                        ", ".join(map(str, sorted(changed))), active_after, after_docs,
                        owned, closed_document_id=active, request_id=request_id)

    return {
        "cleanup_status": "CLOSED",
        "result": "PASS",
        "document_id": active,
        "document_path": observed["path"],
        "geometry_revision": geometry_revision,
        "dirty_construction_copy_discarded": observed["dirty"],
        "saved_model_sha256": actual_hash,
        "persistence_receipt": {"result": "PASS", "saved_path": receipt_path,
                                "sha256": receipt_hash},
        "request_id": request_id,
        "replacement_document_id": replacement_id,
        "replacement_document_status": (
            "NEW_CLEAN_UNTITLED_REPLACEMENT" if replacement_id is not None else None),
        "remaining_owned_document_ids": sorted(set(after_docs) & set(owned)),
        "active_document_after": active_after,
        "other_documents_unchanged": True,
    }
