"""Job-local SQLite ledger for a selected CAD connection. No network or CAD calls.

Pass one stable, private, credential-free key per configured connection as
`endpoint`. Receipt values are supplied by the caller after independent
readback. The ledger verifies their binding; it cannot verify CAD geometry.
"""

from contextlib import closing, contextmanager
import hashlib
import json
from pathlib import Path
import re
import sqlite3


class StateConflict(RuntimeError):
    """The observed mapping changed or an operation requires reconciliation."""


def _json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def mapping_digest(mapping):
    """Hash the canonical JSON object containing the complete mapping."""
    if not isinstance(mapping, dict) or not mapping:
        raise ValueError("A nonempty JSON mapping is required")
    return hashlib.sha256(_json(mapping).encode("utf-8")).hexdigest()


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"A nonempty {label} is required")
    return value


_SCHEMA_VERSION = 1
# SQLite application_id distinguishes this ledger from unrelated databases.
_APPLICATION_ID = 0x43414454
_SCHEMA = (
    """CREATE TABLE revisions (
        revision_id INTEGER PRIMARY KEY,
        endpoint TEXT NOT NULL, operation TEXT NOT NULL,
        previous_revision INTEGER REFERENCES revisions(revision_id),
        mapping TEXT NOT NULL, verification TEXT NOT NULL
    )""",
    "CREATE INDEX revision_lookup ON revisions(endpoint, operation, revision_id)",
    """CREATE TABLE intents (
        endpoint TEXT NOT NULL, token TEXT NOT NULL,
        session TEXT NOT NULL, document TEXT NOT NULL, feature TEXT NOT NULL,
        input_revision TEXT NOT NULL, expected_effect TEXT NOT NULL,
        status TEXT NOT NULL CHECK (status IN ('PENDING','UNKNOWN','APPLIED','NOT_APPLIED')),
        PRIMARY KEY (endpoint, token)
    )""",
    """CREATE UNIQUE INDEX one_pending_per_endpoint ON intents(endpoint)
       WHERE status IN ('PENDING','UNKNOWN')""",
    """CREATE TABLE resolutions (
        event_id INTEGER PRIMARY KEY,
        endpoint TEXT NOT NULL, token TEXT NOT NULL,
        outcome TEXT NOT NULL, evidence TEXT NOT NULL,
        FOREIGN KEY(endpoint,token) REFERENCES intents(endpoint,token)
    )""",
)


class StateStore:
    """Open or create a job-specific ledger in an existing local directory."""

    def __init__(self, db_path):
        self.path = Path(db_path).resolve()
        with self._transaction() as db:
            app_id = db.execute("PRAGMA application_id").fetchone()[0]
            version = db.execute("PRAGMA user_version").fetchone()[0]
            if app_id == _APPLICATION_ID and version == _SCHEMA_VERSION:
                return
            existing = db.execute("SELECT 1 FROM sqlite_master LIMIT 1").fetchone()
            if app_id or version or existing:
                raise ValueError("Unrecognized ledger or unsupported ledger version")
            for statement in _SCHEMA:
                db.execute(statement)
            db.execute(f"PRAGMA application_id = {_APPLICATION_ID}")
            db.execute(f"PRAGMA user_version = {_SCHEMA_VERSION}")

    @contextmanager
    def _connection(self):
        with closing(sqlite3.connect(self.path, isolation_level=None, timeout=10)) as db:
            db.row_factory = sqlite3.Row
            db.execute("PRAGMA foreign_keys = ON")
            db.execute("PRAGMA synchronous = FULL")
            yield db

    @contextmanager
    def _transaction(self):
        with self._connection() as db:
            db.execute("BEGIN IMMEDIATE")
            with db:
                yield db

    @staticmethod
    def _revision(db, endpoint, operation):
        row = db.execute(
            """SELECT * FROM revisions WHERE endpoint=? AND operation=?
               ORDER BY revision_id DESC LIMIT 1""", (endpoint, operation)
        ).fetchone()
        if row is None:
            return None
        return dict(row, mapping=json.loads(row["mapping"]),
                    verification=json.loads(row["verification"]))

    def active(self, endpoint, operation):
        """Return the last committed revision of this endpoint's operation."""
        with self._connection() as db:
            return self._revision(db, endpoint, operation)

    def promote(self, endpoint, operation, *, expected_revision, mapping, verification):
        """Append an immutable verified mapping if expected_revision is current.

        Supply None on first promotion. The evidence_sha256 in verification
        identifies the caller's verified evidence artifact.
        """
        _text(endpoint, "endpoint")
        _text(operation, "operation")
        if expected_revision is not None and (type(expected_revision) is not int or expected_revision < 1):
            raise ValueError("expected_revision must be None or a positive revision_id")
        expected = dict(endpoint=endpoint, operation=operation, mapping_sha256=mapping_digest(mapping),
                        level="live_verified", result="PASS")
        if not isinstance(verification, dict) or any(verification.get(k) != v for k, v in expected.items()):
            raise ValueError("Receipt must verify this exact endpoint, operation and mapping")
        evidence_hash = verification.get("evidence_sha256")
        if not isinstance(evidence_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", evidence_hash):
            raise ValueError("Receipt must identify the evidence artifact by SHA-256")
        with self._transaction() as db:
            current = self._revision(db, endpoint, operation)
            current_id = current["revision_id"] if current else None
            if current_id != expected_revision:
                raise StateConflict("Mapping changed since the caller's read")
            db.execute(
                """INSERT INTO revisions(endpoint,operation,previous_revision,mapping,verification)
                   VALUES(?,?,?,?,?)""",
                (endpoint, operation, current_id, _json(mapping), _json(verification)),
            )
            return self._revision(db, endpoint, operation)

    def begin_intent(self, endpoint, token, *, session, document, feature, input_revision, expected_effect):
        """Commit the write intent before sending a native mutation.

        The return marks a durable local intent. It is not authority to resend
        a CAD mutation after a lost response. Session and artifact identifiers
        are caller-supplied local labels, not credentials.
        """
        values = (endpoint, token, session, document, feature, input_revision, expected_effect)
        for value, field in zip(values, ("endpoint", "token", "session", "document", "feature",
                                         "input revision", "expected effect")):
            _text(value, field)
        with self._transaction() as db:
            try:
                db.execute(
                    """INSERT INTO intents(endpoint,token,session,document,feature,input_revision,
                                           expected_effect,status) VALUES(?,?,?,?,?,?,?,'PENDING')""",
                    values,
                )
            except sqlite3.IntegrityError as error:
                raise StateConflict("Token already used or endpoint has an unresolved intent") from error

    def pending_intents(self, endpoint):
        """List all uncertain or unfinished writes for this connection on startup."""
        with self._connection() as db:
            return [dict(r) for r in db.execute(
                "SELECT * FROM intents WHERE endpoint=? AND status IN ('PENDING','UNKNOWN')",
                (endpoint,),
            )]

    def resolve_intent(self, endpoint, token, *, outcome, evidence):
        """Record independent observations; UNKNOWN continues to block writes."""
        if outcome not in ("APPLIED", "NOT_APPLIED", "UNKNOWN"):
            raise ValueError("Expected APPLIED, NOT_APPLIED or UNKNOWN")
        _text(evidence, "reconciliation evidence")
        with self._transaction() as db:
            row = db.execute("SELECT status FROM intents WHERE endpoint=? AND token=?",
                             (endpoint, token)).fetchone()
            if row is None or row["status"] not in ("PENDING", "UNKNOWN"):
                raise StateConflict("Expected an unresolved intent on this endpoint")
            db.execute("INSERT INTO resolutions(endpoint,token,outcome,evidence) VALUES(?,?,?,?)",
                       (endpoint, token, outcome, evidence))
            db.execute("UPDATE intents SET status=? WHERE endpoint=? AND token=?",
                       (outcome, endpoint, token))
