import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from source_variant_table import select_cell


class SourceVariantTableTests(unittest.TestCase):
    def setUp(self):
        self.table = {
            'table_id': 'synthetic-table',
            'source_location': 'synthetic page 1, table 1',
            'headers': ['Variant Alpha (assembly)', 'Variant Beta (bare)', 'Variant Gamma (assembly)'],
            'rows': [
                {'label': 'Envelope', 'values': ['31 mm x 9 mm x 4 mm',
                                                 '27 mm x 9 mm x 2 mm',
                                                 '31 mm x 9 mm x 4 mm']},
                {'label': 'Mass', 'values': ['8 g', '5 g', '7 g']},
            ],
        }

    def test_exact_header_selects_only_its_column(self):
        beta = select_cell(self.table, 'Variant Beta (bare)', 'Envelope')
        alpha = select_cell(self.table, 'Variant Alpha (assembly)', 'Envelope')
        gamma = select_cell(self.table, 'Variant Gamma (assembly)', 'Envelope')
        self.assertEqual('27 mm x 9 mm x 2 mm', beta['value'])
        self.assertEqual('31 mm x 9 mm x 4 mm', alpha['value'])
        self.assertEqual('31 mm x 9 mm x 4 mm', gamma['value'])
        self.assertEqual(1, beta['header_index'])
        self.assertEqual('synthetic page 1, table 1', beta['source_location'])

    def test_neighboring_or_case_changed_header_does_not_match(self):
        for header in ('Variant Beta', 'variant beta (bare)', 'Variant Beta (bare) '):
            with self.subTest(header=header), self.assertRaisesRegex(ValueError, 'exactly one header'):
                select_cell(self.table, header, 'Envelope')

    def test_duplicate_headers_are_rejected_even_when_unselected(self):
        self.table['headers'][2] = ' variant beta (BARE) '
        with self.assertRaisesRegex(ValueError, 'duplicate variant/header'):
            select_cell(self.table, 'Variant Alpha (assembly)', 'Envelope')

    def test_duplicate_row_labels_are_rejected_even_when_unselected(self):
        self.table['rows'].append({'label': ' envelope ',
                                   'values': ['aa', 'bb', 'cc']})
        with self.assertRaisesRegex(ValueError, 'duplicate table row labels'):
            select_cell(self.table, 'Variant Beta (bare)', 'Mass')

    def test_requested_row_label_must_match_exactly(self):
        with self.assertRaisesRegex(ValueError, 'exactly one row'):
            select_cell(self.table, 'Variant Beta (bare)', 'envelope')

    def test_malformed_row_width_is_rejected(self):
        self.table['rows'][0]['values'].pop()
        with self.assertRaisesRegex(ValueError, 'exactly one cell per header'):
            select_cell(self.table, 'Variant Beta (bare)', 'Mass')

    def test_malformed_empty_cell_is_rejected(self):
        self.table['rows'][0]['values'][1] = ' '
        with self.assertRaisesRegex(ValueError, 'nonempty string'):
            select_cell(self.table, 'Variant Beta (bare)', 'Mass')

    def test_malformed_row_record_is_rejected(self):
        self.table['rows'].append(['Dimension', '1', '2', '3'])
        with self.assertRaisesRegex(ValueError, 'each row must be an object'):
            select_cell(self.table, 'Variant Beta (bare)', 'Mass')

    def test_missing_table_location_is_rejected(self):
        del self.table['source_location']
        with self.assertRaisesRegex(ValueError, 'source_location'):
            select_cell(self.table, 'Variant Beta (bare)', 'Envelope')


if __name__ == '__main__':
    unittest.main()
