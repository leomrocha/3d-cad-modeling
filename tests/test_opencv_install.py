"""Exercise independent skill discovery and the probe with a bare interpreter."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import venv

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(os.getenv("SKILLS_CLI_ROOT"), "Local skills CLI required")
class OpenCVInstall(unittest.TestCase):
    def test_isolated_probe(self):
        with tempfile.TemporaryDirectory() as temporary:
            job = Path(temporary)
            env = dict(
                os.environ,
                HOME=temporary,
                XDG_CONFIG_HOME=str(job / "config"),
                CI="1",
                DISABLE_TELEMETRY="1",
                DO_NOT_TRACK="1",
            )
            name = "cad-opencv-setup"
            subprocess.run(
                [
                    "node",
                    Path(env["SKILLS_CLI_ROOT"]) / "bin/cli.mjs",
                    "add",
                    str(ROOT / "skills" / name),
                    "--skill",
                    name,
                    "--agent",
                    "codex",
                    "--copy",
                    "--yes",
                ],
                check=True,
                env=env,
                cwd=job,
                capture_output=True,
            )
            (script,) = job.rglob("opencv_env.py")
            venv.EnvBuilder(with_pip=False).create(job / "bare")
            proc = subprocess.run(
                [job / "bare/bin/python", "-I", script, "probe", "contours"],
                cwd=job,
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 1)
            self.assertEqual(json.loads(proc.stdout)["status"], "absent")
