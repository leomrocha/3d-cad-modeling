import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from step_placements import eye, inverse, native_fields, native_matrix, near
from assembly_repair import apply_source_placements


class Client:
    def __init__(self, rows):
        self.rows = {r['handle']: copy.deepcopy(r) for r in rows}
        self.writes = []
        self.corrupt_readback = False
    def read(self, op, **kw):
        return {'records': [copy.deepcopy(self.rows[h]) for h in kw['handles']]}
    def mutate(self, label, op, **kw):
        self.writes.append(label)
        p = self.rows[kw['handle']]['properties']
        for u in kw['updates']:
            key = u['path'][1:]
            if p[key] != u['expected']:
                raise ValueError('compare-and-set conflict')
            p[key] = copy.deepcopy(u['value'])
        if self.corrupt_readback:
            p['insert_point']['x'] += 1


def fixture():
    rows = []; plan = []
    for h, x in [('A', 12), ('B', 27)]:
        expected = eye(); expected[0][3] = x; before = inverse(expected)
        p = dict(native_fields(before), x_scale=1, y_scale=1, z_scale=1)
        rows.append({'handle': h, 'type': 'Insert', 'properties': p})
        plan.append(dict(handle=h, before=before, expected=expected,
                         fields=native_fields(expected), source_id=100+x))
    rows.append({'handle': 'C', 'type': 'Solid3D', 'properties': {'acis_data': {'sat_data': 'original'}}})
    return rows, plan


class RepairTests(unittest.TestCase):
    def test_repeated_placements_preserve_definition(self):
        rows, plan = fixture(); c = Client(rows)
        result = apply_source_placements(c, plan, rows)
        self.assertEqual(len(result['placements']), 2)
        self.assertEqual(result['solid_definitions_preserved'], 1)
        self.assertEqual(c.rows['A']['properties']['insert_point']['x'], 12)
    def test_stale_second_record_rejects_before_first_write(self):
        rows, plan = fixture(); c = Client(rows)
        c.rows['B']['properties']['insert_point']['x'] += 1
        with self.assertRaisesRegex(ValueError, 'changed since'): apply_source_placements(c, plan, rows)
        self.assertEqual(c.writes, [])
    def test_inconsistent_target_fields_rejected(self):
        rows, plan = fixture(); c = Client(rows)
        plan[0]['fields']['insert_point']['y'] = 1
        with self.assertRaisesRegex(ValueError, 'fields differ'): apply_source_placements(c, plan, rows)
        self.assertEqual(c.writes, [])
    def test_duplicate_target_rejected(self):
        rows, plan = fixture(); c = Client(rows)
        with self.assertRaisesRegex(ValueError, 'Duplicate planned'): apply_source_placements(c, plan + plan[:1], rows)
        self.assertEqual(c.writes, [])
    def test_native_readback_failure_preserves_partial_state(self):
        rows, plan = fixture(); c = Client(rows); c.corrupt_readback = True
        with self.assertRaisesRegex(ValueError, 'readback differs'): apply_source_placements(c, plan, rows)
        self.assertEqual(c.writes, ['source-placement-A'])
    def test_rotated_y_reflection_keeps_signed_scale(self):
        rows, plan = fixture()
        original = rows[0]['properties']
        original['y_scale'] = -1
        target = [[1,0,0,14],[0,0,1,-12],[0,1,0,28],[0,0,0,1]]
        plan[0].update(before=native_matrix(original,allow_unit_reflection=True),
                       expected=target,fields=native_fields(target))
        c = Client(rows)
        with self.assertRaisesRegex(ValueError,'Positive finite'):
            apply_source_placements(c, plan, rows)
        self.assertEqual(c.writes, [])
        result = apply_source_placements(c, plan, rows, allow_unit_reflection=True)
        placed = c.rows['A']['properties']
        self.assertEqual(result['result'], 'PASS')
        self.assertEqual(placed['y_scale'], -1)
        self.assertTrue(near(native_matrix(placed,allow_unit_reflection=True),target))

    def test_reflection_mode_rejects_changed_handedness_before_write(self):
        rows, plan = fixture()
        original = rows[0]['properties']
        original['y_scale'] = -1
        plan[0]['before'] = native_matrix(original,allow_unit_reflection=True)
        c = Client(rows)
        with self.assertRaisesRegex(ValueError,'fields differ'):
            apply_source_placements(c, plan, rows, allow_unit_reflection=True)
        self.assertEqual(c.writes, [])

    def test_changed_solid_definition_detected(self):
        rows, plan = fixture(); c = Client(rows)
        c.rows['C']['properties']['acis_data']['sat_data'] = 'changed'
        with self.assertRaisesRegex(ValueError, 'solid definition changed'): apply_source_placements(c, plan, rows)


if __name__ == '__main__': unittest.main()
