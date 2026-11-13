import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from source_metadata import compare_source_metadata


class SourceMetadataTests(unittest.TestCase):
    def setUp(self):
        self.lines = ['Synthetic identity', 'Frame: ' + 'x' * 110,
                      'Scope: source-defined reference']
        self.chunks = [line[i:i + 100] for line in self.lines
                       for i in range(0, len(line), 100)]
        self.record = {'handle': 'A7', 'properties': {'common': {'extended_data': {
            'records': [{'application_name': 'TEST_SOURCE',
                         'values': [{'String': x} for x in self.chunks]}]}}}}

    def check(self, record=None, lines=None, **kwargs):
        return compare_source_metadata(self.record if record is None else record,
                                       'A7', 'TEST_SOURCE',
                                       self.lines if lines is None else lines, **kwargs)

    def test_complete_identity_frame_and_scope_pass_with_long_line_chunks(self):
        before = copy.deepcopy(self.record)
        result = self.check()
        self.assertEqual('PASS', result['result'])
        self.assertEqual(self.chunks, result['observed'])
        self.assertEqual(before, self.record)

    def test_scope_overwrite_loses_identity_and_fails(self):
        entry = self.record['properties']['common']['extended_data']['records'][0]
        entry['values'] = [{'String': self.lines[-1]}]
        self.assertEqual('FAIL', self.check()['result'])

    def test_changed_scope_or_order_fails(self):
        self.assertEqual('FAIL', self.check(lines=self.lines[:-1] + ['Scope: changed'])['result'])
        self.assertEqual('FAIL', self.check(lines=list(reversed(self.lines)))['result'])

    def test_missing_application_fails_and_other_application_is_preserved(self):
        self.record['properties']['common']['extended_data']['records'][0]['application_name'] = 'OTHER'
        result = self.check()
        self.assertEqual('FAIL', result['result'])
        self.assertFalse(result['application_present'])

    def test_absent_extended_data_fails(self):
        self.record['properties']['common'].pop('extended_data')
        self.assertEqual('FAIL', self.check()['result'])

    def test_wrong_handle_is_rejected(self):
        self.record['handle'] = 'B8'
        with self.assertRaisesRegex(ValueError, 'handle'):
            self.check()

    def test_duplicate_applications_are_rejected(self):
        entries = self.record['properties']['common']['extended_data']['records']
        entries.append(copy.deepcopy(entries[0]))
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            self.check()

    def test_malformed_or_nonstring_native_payload_is_rejected(self):
        entry = self.record['properties']['common']['extended_data']['records'][0]
        for value in [{'Integer': 3}, {'String': 3}, {'String': 'a', 'Integer': 3}]:
            entry['values'] = [value]
            with self.assertRaises(ValueError):
                self.check()

    def test_invalid_expected_lines_and_chunk_size_are_rejected(self):
        for lines in [[], [''], 'text', [3]]:
            with self.assertRaises(ValueError):
                self.check(lines=lines)
        for size in [0, -1, True, 1.5]:
            with self.assertRaises(ValueError):
                self.check(chunk_size=size)


if __name__ == '__main__':
    unittest.main()
