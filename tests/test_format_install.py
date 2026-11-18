import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAME = "cad-format-translator"


@unittest.skipUnless(
    os.environ.get("SKILLS_CLI_ROOT"), "Requires local cached skills CLI"
)
class FormatInstallation(unittest.TestCase):
    def test_local_install_and_execution(self):
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            source = workspace / "source"
            dest = workspace / "job"
            dest.mkdir()
            shutil.copytree(ROOT / "skills" / NAME, source / "skills" / NAME)
            env = dict(
                os.environ,
                HOME=str(workspace / "home"),
                XDG_CONFIG_HOME=str(workspace / "config"),
                DISABLE_TELEMETRY="1",
                DO_NOT_TRACK="1",
                CI="1",
            )
            cli = Path(env["SKILLS_CLI_ROOT"]) / "bin/cli.mjs"
            subprocess.run(
                [
                    "node",
                    cli,
                    "add",
                    source,
                    "--skill",
                    NAME,
                    "--agent",
                    "codex",
                    "--copy",
                    "--yes",
                ],
                cwd=dest,
                env=env,
                check=True,
                capture_output=True,
            )
            shutil.rmtree(source)
            (skill,) = list(dest.rglob("SKILL.md"))
            package = skill.parent

            def run(script, *args):
                # -S excludes third-party packages; relative imports come only from this installation.
                return subprocess.check_output(
                    [
                        sys.executable,
                        "-B",
                        "-E",
                        "-S",
                        package / "scripts" / script,
                        *args,
                    ],
                    cwd=dest,
                    env=env,
                    text=True,
                )

            self.assertEqual(json.loads(run("package_check.py"))["result"], "PASS")
            result = run(
                "routes.py",
                package / "fixtures/inventory.json",
                "--connection",
                "workshop-fixture",
                "--source",
                "step-solid",
                "--target",
                "stl-mesh",
                "--require",
                "mm",
            )
            self.assertEqual(json.loads(result)["status"], "CANDIDATE")
            run(
                "convert.py",
                "scad-python",
                package / "fixtures/plate.scad",
                dest / "plate.py",
            )
            self.assertIn("def build_model()", (dest / "plate.py").read_text())
