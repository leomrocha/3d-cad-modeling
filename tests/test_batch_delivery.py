"""Check reviewed request pinning, target identity and command exit status."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import batch_delivery as delivery


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.request = self.root / "request.json"
        self.catalogue = self.root / "catalogue.json"
        self.job = self.root / "job"
        operation = "occurrence name"
        self.spec = dict(
            operation=operation,
            targets=[{"id": "selected"}],
            value={"name": "reviewed"},
        )
        self.request.write_text(json.dumps(self.spec))
        action, entity, out = delivery.CONTRACTS[operation]
        method = dict(name="name", sample_request=str(self.request))
        resource = dict(id="native", methods=[method])
        row = dict(
            resource="native",
            name="name",
            action=action,
            input=entity,
            output=out,
            usable=True,
            readback_verified=True,
            evidence_sha256="digest",
            readback_file="sample",
        )
        self.catalogue.write_text(
            json.dumps(dict(version=2, resources=[resource], operations=[row]))
        )

    def test_pinned_payload_and_wrong_output_id(self):
        original = self.request.read_bytes()

        def change(*args, **kwargs):
            self.spec["value"]["name"] = "unreviewed"
            self.request.write_text(json.dumps(self.spec))
            return "digest"

        def execute(path, directory, *, reviewed_bytes):
            self.assertEqual(reviewed_bytes, original)
            self.assertNotEqual(path.read_bytes(), reviewed_bytes)
            return {"elements": [{"id": "unselected"}]}

        with (
            patch.object(delivery, "verify_job_sample", side_effect=change),
            patch.object(delivery, "writer", return_value=execute),
        ):
            result = delivery.deliver(
                self.request,
                self.catalogue,
                self.job,
                request_sha256=hashlib.sha256(original).hexdigest(),
            )
        self.assertIn("blocker", result)
        self.assertEqual(result["remaining"], ["selected"])

    def test_empty_or_duplicate_target_fails_command(self):
        for targets in ([], [{"id": "A"}, {"id": "A"}], [{"id": ""}]):
            self.spec["targets"] = targets
            self.request.write_text(json.dumps(self.spec))
            cmd = [
                sys.executable,
                delivery.__file__,
                str(self.request),
                str(self.job),
                "--catalogue",
                str(self.catalogue),
                "--request-sha256",
                delivery.file_digest(self.request),
            ]
            p = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("nonempty reviewed target IDs", p.stderr)
            self.assertFalse(self.job.exists())

    def test_worker_response_requires_job_and_target_evidence(self):
        data = json.loads(self.catalogue.read_bytes())
        pattern = dict(
            kind="explicit",
            unit="mm",
            reference="plate",
            tolerance=0.001,
            frame=dict(origin=[0, 0, 0], x=[1, 0, 0], y=[0, 1, 0]),
            positions=[dict(id="A", xy=[0, 0])],
        )
        self.spec = dict(
            operation="circle",
            relationship="individual",
            pattern=pattern,
            model="source.dxf",
            revision="original",
        )
        self.request.write_text(json.dumps(self.spec))
        action, entity, out = delivery.CONTRACTS["circle"]
        data["operations"][0].update(action=action, input=entity, output=out)
        self.catalogue.write_text(json.dumps(data))
        for completed, record in (
            (["A"], "garbage"),
            (["wrong"], {"elements": [{"id": "wrong"}]}),
            (["A"], {"elements": [{"id": "A"}]}),
        ):
            response = dict(completed=completed, remaining=[], readback=record)
            with (
                patch.object(
                    delivery, "provider_python", return_value=Path("/other/python")
                ),
                patch.object(delivery, "provider_call", return_value=response),
            ):
                result = delivery.deliver(self.request, self.catalogue, self.job)
            self.assertIn("blocker", result)
            self.assertEqual(result["completed"], [])
            self.assertEqual(result["remaining"], ["A"])
            self.assertFalse(self.job.exists())

    def test_no_provider_retains_pending_pattern_and_diagnostic(self):
        data = json.loads(self.catalogue.read_bytes())
        data["resources"][0]["methods"][0].update(name="circle")
        action, entity, out = delivery.CONTRACTS["circle"]
        data["operations"][0].update(
            name="circle",
            action=action,
            input=entity,
            output=out,
            usable=False,
            reason="configured writer missing",
        )
        self.catalogue.write_text(json.dumps(data))
        pattern = dict(
            kind="interior",
            unit="mm",
            reference="plate",
            tolerance=0.001,
            frame=dict(origin=[0, 0, 0], x=[1, 0, 0], y=[0, 1, 0]),
        )
        for unit, diagnostic in (("mm", "Shapely"), ("bad", "Unsupported length unit")):
            pattern["unit"] = unit
            self.request.write_text(
                json.dumps(dict(operation="circle", pattern=pattern))
            )
            cmd = [
                sys.executable,
                "-E",
                "-S",
                delivery.__file__,
                str(self.request),
                str(self.job),
                "--catalogue",
                str(self.catalogue),
                "--request-sha256",
                delivery.file_digest(self.request),
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 2, proc.stderr)
            result = json.loads(proc.stdout)
            self.assertEqual(
                result["attempts"][0]["outcome"], "configured writer missing"
            )
            self.assertEqual(result["unresolved_pattern"], pattern)
            self.assertIn(diagnostic, result["target_error"])
            self.assertIn("configured writer missing", result["blocker"])

    def test_package_catalogue_excludes_engineering_adapter(self):
        import build_skill_packages as pkg

        for skill in pkg.SKILLS:
            if skill != "cad-ocs-engineering":
                self.assertNotIn("scripts/batch_delivery.py", pkg.inputs(skill), skill)
