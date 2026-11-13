"""Guarded OCS adapter; extracted from the inspected ocs_control/NGV workflow.

The bundled control helper supplies the transport and authorisation guard.
Imports and offline planning never connect to OCS. Journals contain no descriptor.
"""

import importlib.util
import fcntl
import json
import math
import os
from pathlib import Path
import uuid


class CadError(RuntimeError):
    """A definitive request, geometry or verification failure."""


class Uncertain(CadError):
    """Completion is unknown; recover the original request, never replay it."""


def redact(value):
    if isinstance(value, dict):
        return {k: "[redacted]" if k.lower() in {
            "token", "authorization", "cookie", "password", "secret"
        } else redact(v) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    return value


def load_helper(path=None):
    """Load an explicitly selected existing helper, with no discovery on import."""
    if path is None:
        path = Path(__file__).resolve().parents[1] / "ocs_control.py"
    spec = importlib.util.spec_from_file_location("cadtools_ocs_control", path)
    if spec is None or spec.loader is None:
        raise CadError("Cannot load OCS helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Journal:
    """Append-only write-ahead intent; all request identities survive exceptions."""

    def __init__(self, path):
        self.path = Path(path)
        if not self.path.parent.is_dir():
            raise CadError("Journal parent directory must already exist")
        self.requests = {}
        if self.path.exists():
            try:
                for line in self.path.read_text().splitlines():
                    event = json.loads(line)
                    if event["event"] == "intent":
                        key = event["request"]["request_id"]
                        if key in self.requests:
                            raise CadError("Duplicate request identity in journal")
                        self.requests[key] = event
            except (KeyError, ValueError) as error:
                raise CadError("Invalid journal; preserve it for inspection") from error

    def append(self, event):
        line = json.dumps(redact(event), allow_nan=False, sort_keys=True) + "\n"
        with self.path.open("a", encoding="utf-8") as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            stream.write(line)
            stream.flush()
            os.fsync(stream.fileno())

    def intent(self, request, context):
        key = request["request_id"]
        if key in self.requests:
            raise CadError("Request already journalled; inspect/recover " + key)
        event = {"event": "intent", "request": request, "context": context}
        # Re-read under an OS lock: two clients cannot reserve the same identity.
        with self.path.open("a+", encoding="utf-8") as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            stream.seek(0)
            for line in stream:
                previous = json.loads(line)
                if previous.get("event") == "intent" and previous["request"]["request_id"] == key:
                    raise CadError("Request already journalled; inspect/recover " + key)
            stream.write(json.dumps(redact(event), allow_nan=False, sort_keys=True) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        self.requests[key] = event


class Client:
    """One selected existing document, one writer, bounded same-ID recovery.

    The caller must provide task authorisation, an existing helper and a journal.
    No automatic document creation, import, cancellation, deletion or retry occurs.
    """

    def __init__(self, helper, descriptor, document_id, namespace, journal,
                 allow_write=False, timeout=30, max_queries=8):
        if type(document_id) is not int or document_id < 1:
            raise CadError("A positive integer document ID is required")
        if not namespace or len(namespace.encode()) > 64:
            raise CadError("Request namespace must be 1..64 bytes")
        if not math.isfinite(timeout) or timeout <= 0 or max_queries < 1:
            raise CadError("Positive timeout and query bound are required")
        self.helper, self.descriptor = helper, descriptor
        self.document_id, self.namespace = document_id, namespace
        self.journal, self.allow_write = journal, allow_write
        self.timeout, self.max_queries = timeout, max_queries

    def read(self, op, **fields):
        if op not in self.helper.READ_OPS:
            raise CadError("Read operation is outside the helper allowlist: " + op)
        payload = dict(op=op, document_id=self.document_id, **fields)
        payload.setdefault("request_id", "read-" + uuid.uuid4().hex)
        response = self.helper.request(self.descriptor, payload, self.timeout)
        if not response.get("ok"):
            raise CadError(str(response.get("error", response.get("code"))))
        return response

    def mutate(self, label, op, allow_wait=False, **fields):
        if not self.allow_write:
            raise CadError("Mutation requires explicit --allow-write and task authorisation")
        key = self.namespace + ":" + label
        if len(key.encode()) > 128:
            raise CadError("Request ID exceeds 128 bytes")
        if key in self.journal.requests:
            raise CadError("Request already journalled; recover " + key)
        state = self.read("state")
        if state.get("document_id") != self.document_id:
            raise CadError("Active document changed; mutation not sent")
        payload = dict(op=op, document_id=self.document_id,
                       revision=state["revision"], request_id=key, **fields)
        json.dumps(payload, allow_nan=False)
        self.journal.intent(payload, {"session_id": self.descriptor["session_id"],
                                     "document_id": self.document_id})
        try:
            response = self.helper.execute_checked(
                self.descriptor, payload, allow_write=True, timeout=self.timeout)
        except Exception as error:
            # Helper can raise after send. Preserve identity even for preflight failures.
            self.journal.append({"event": "response_unavailable", "request_id": key,
                                 "exception_type": type(error).__name__})
            raise Uncertain("Inspect original operation: " + key) from error
        return self._finish(key, response, allow_wait)

    def recover(self, request_id, allow_wait=False):
        intent = self.journal.requests.get(request_id)
        if intent is None:
            raise CadError("Recovery requires an existing journal intent")
        context = intent["context"]
        if context != {"session_id": self.descriptor["session_id"],
                       "document_id": self.document_id}:
            raise CadError("Recovery session/document differs from journal")
        response = self.helper.request(self.descriptor,
                                       {"op": "operation", "request_id": request_id,
                                        "document_id": self.document_id}, self.timeout)
        return self._finish(request_id, response, allow_wait)

    def _finish(self, key, response, allow_wait):
        for query in range(self.max_queries + 1):
            self.journal.append({"event": "response", "request_id": key, "response": response})
            pending = response.get("status") in {"accepted", "running"}
            pending = pending or response.get("code") == "response_timeout"
            if not pending:
                break
            if query == self.max_queries:
                raise Uncertain("Operation query bound reached: " + key)
            try:
                response = self.helper.request(self.descriptor,
                    {"op": "operation", "request_id": key,
                     "document_id": self.document_id}, self.timeout)
            except Exception as error:
                raise Uncertain("Operation response unavailable: " + key) from error
        if not response.get("ok") or response.get("status") in {"failed", "rejected", "cancelled"}:
            raise CadError(str(response.get("error", response.get("status"))))
        status = response.get("status")
        if status == "waiting_input" and allow_wait:
            return response
        if status != "completed":
            raise CadError("Inspect entity effects and command state for " + key + ": " + str(status))
        return response

    def checkpoint(self, path, parts):
        state = self.read("state")
        if state.get("document_id") != self.document_id:
            raise CadError("Cannot checkpoint another active document")
        target = Path(path)
        # Exclusive creation protects an existing checkpoint from silent replacement.
        with target.open("x", encoding="utf-8") as stream:
            json.dump({"document_id": self.document_id, "revision": state["revision"],
                       "geometry_revision": state.get("geometry_revision"), "parts": parts,
                       "namespace": self.namespace}, stream, indent=2, allow_nan=False)


class PlanClient:
    """Offline command planning. Symbolic handles are never CAD observations."""

    def __init__(self):
        self.operations = []
        self.handles = []

    def mutate(self, label, op, allow_wait=False, **fields):
        self.operations.append(dict(label=label, op=op, allow_wait=allow_wait, **fields))
        creates = op == "entities_create" or (
            op == "run" and fields.get("cmd", "").split()[0] in {
                "CYLINDER", "SPHERE", "EXTRUDE", "REVOLVE", "UNION", "SWEEP"})
        count = len(fields.get("entities", [])) if op == "entities_create" else 1
        handles = []
        if creates:
            for _ in range(count):
                handle = "planned-" + str(len(self.handles) + 1)
                self.handles.append(handle)
                handles.append(handle)
        return {"ok": True, "status": "completed", "result": {"handles": handles},
                "changes": [{"handle": h, "kind": "Added"} for h in handles]}

    def read(self, op, **fields):
        if op == "query":
            return {"ok": True, "entities": [{"handle": h} for h in self.handles]}
        raise CadError("Offline planner cannot supply CAD measurements")
