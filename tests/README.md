# Modeling tool tests

1. Purpose: verify shared functions with synthetic fixtures and supported native geometry cases. Generic test code belongs here; FERME owns real component integration fixtures and expectations.
2. Current suite command: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s /home/leo/projects/3dmodeling/tests -p 'test_*.py'`. Use the existing Python environment containing the pinned native-reader dependencies.
3. `test_native_acis.py`, `test_scaled_assembly.py` and `test_tabbed_battery.py` include FERME integration cases. They currently resolve FERME_ROOT with a sibling-project default. Read each test's dependency/fixture conditions when interpreting skips.
4. The current smallBMS test also uses C054 files in execution and a temporary native-reader path. These tests and ongoing fixes retain their current locations during preparation.
5. The [script-change plan](/home/leo/projects/3dmodeling/research/repository-split-preparation/script-changes.md) separates generic tests from component integration cases and makes fixture/runtime paths explicit in the later split.
6. Report executed tests, failures and skipped integration cases separately. Preserve recorded component results in FERME and generic regression evidence here.
