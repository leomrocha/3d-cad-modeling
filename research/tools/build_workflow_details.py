#!/usr/bin/env python3
"""Render complete workflow dossiers and independent effort/resource orderings."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DETAILS = ROOT / 'research/workflows/details'


def load(path):
    return json.loads(path.read_text())


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def label(key):
    return key.replace('_', ' ').capitalize()


def plain(value):
    if isinstance(value, str):
        if value.startswith('/') and Path(value).is_file():
            return f'[{Path(value).name}]({value})'
        return value
    if value is None:
        return 'See the selected tool/variant contract.'
    if isinstance(value, dict):
        return '; '.join(f'{label(k)}: ' + (f'`{v}`' if k in {'entrypoint', 'command'} and isinstance(v, str) else plain(v)) for k, v in value.items())
    if isinstance(value, list):
        return '; '.join(plain(item) for item in value)
    return str(value)


def section(title, value):
    lines = [f'## {title}', '']
    if isinstance(value, list):
        lines += [f'{i}. {plain(item)}' for i, item in enumerate(value, 1)]
    elif isinstance(value, dict):
        lines += [f'{i}. **{label(k)}:** {plain(v)}' for i, (k, v) in enumerate(value.items(), 1)]
    else:
        lines += [plain(value)]
    return lines + ['']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', required=True)
    args = parser.parse_args()
    contract = load(DETAILS / 'contract.json')
    recipes = {}
    operations = {}
    for name in ['cad', 'reconstruction', 'domain', 'combined']:
        domain = load(ROOT / f'research/workflows/{name}-paths.json')
        operations.update({o['id']: o for o in domain.get('operations', [])})
        for item in domain['recipes']:
            recipes[item['id']] = item
    records = []
    for path in [DETAILS / f'{name}-details.json' for name in ['cad', 'reconstruction', 'domain', 'combined']]:
        records += load(path)['workflows']
    errors = []
    ids = [r['id'] for r in records]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate workflow detail ID')
    if set(ids) != set(recipes):
        errors.append(f'Detail IDs differ from recipes: {sorted(set(ids) ^ set(recipes))}')
    source_records = load(ROOT / 'research/sources/source-register.json')['sources']
    source_ids = {(s['url'] or s['local_source_path']): s['id'] for s in source_records}
    code_statuses = set(contract['code_statuses'])
    for record in records:
        for key in contract['record_required_fields']:
            if key not in record or record[key] in [None, '', []]:
                errors.append(f'{record["id"]}: required detail {key}')
        effort = record.get('effort', {})
        for key in contract['effort_required_fields']:
            if key not in effort:
                errors.append(f'{record["id"]}: effort field {key}')
        for axis in ['human', 'setup', 'compute']:
            if type(effort.get(axis)) is not int or not 1 <= effort[axis] <= 5:
                errors.append(f'{record["id"]}: invalid {axis} rating')
        refs = set(record.get('source_urls', []))
        for software in record.get('software', []):
            if isinstance(software, dict):
                refs.update(software.get('source_urls', []))
        for code in record.get('code', []):
            if isinstance(code, dict):
                if code.get('status') and code['status'] not in code_statuses:
                    errors.append(f'{record["id"]}: code status {code["status"]}')
                refs.update(code.get('source_urls', []))
                path = code.get('path')
                if path and str(path).startswith('/') and not Path(path).is_file():
                    errors.append(f'{record["id"]}: code path unavailable: {path}')
        record['source_ids'] = []
        for ref in sorted(refs):
            if ref not in source_ids:
                errors.append(f'{record["id"]}: source not registered: {ref}')
            else:
                record['source_ids'].append(source_ids[ref])
        record['registered_recipe_inputs'] = recipes[record['id']]['inputs']
        record['registered_operation_sequence'] = [operations[i] for i in recipes[record['id']]['steps']]
        record['recorded_operations'] = len(recipes[record['id']]['steps'])
    if errors:
        dump(DETAILS / 'detail-checks.json', {'date': args.date, 'errors': errors})
        print(json.dumps({'errors': errors}, indent=2))
        raise SystemExit(1)
    records.sort(key=lambda r: r['id'])
    for record in records:
        score = record['effort']
        lines = [f'# {record["id"]} — {record["name"]}', '',
                 f'Date: {args.date}. Classification: analyst assessment under the stated conditions.', '',
                 f'**Manual effort {score["human"]}/5; setup {score["setup"]}/5; computing {score["compute"]}/5.**', '',
                 f'Output: {plain(record["output_scope"])}', '']
        lines += ['Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.', '']
        for title, key in [
            ('Comparison conditions', 'comparison_conditions'), ('Registered starting artifact types', 'registered_recipe_inputs'), ('Detailed source and preparation artifacts', 'inputs'),
            ('Reference points, datums and coordinate frames', 'reference_points'),
            ('Software, libraries and dependencies', 'software'), ('Procedure', 'steps'),
            ('Inputs, outputs and requirements at each registered operation', 'registered_operation_sequence'),
            ('Documented third-party tool and API entry points', 'code'), ('Output artifacts', 'outputs'),
            ('Checks', 'checks'), ('Failure recovery', 'failure_recovery'),
            ('Effort and computing classification', 'effort'), ('Resources and scaling', 'resources')]:
            lines += section(title, record[key])
        
        if record.get('branch_dossiers'):
            lines += section('Detailed branch procedures', record['branch_dossiers'])
            lines += [record['branch_software_selection'], '']
        lines += ['## Original sources', '']
        lines += [f'{i}. [{url}]({url})' for i, url in enumerate(record['source_urls'], 1)]
        lines += ['', 'Full source summaries: [source register](../../sources/source-register.md).', '']
        (DETAILS / f'{record["id"].lower()}.md').write_text('\n'.join(line.rstrip() for line in lines).rstrip() + '\n')
    dump(DETAILS / 'workflow-details.json', {'schema_version': 1, 'date': args.date,
         'classification_status': contract['rating_status'], 'workflows': records})
    names = {'human': 'manual effort', 'compute': 'computing demand'}
    sorted_records = {}
    for axis in ['human', 'compute']:
        order = sorted(records, key=lambda r: (r['effort'][axis], r['effort']['setup'],
                                               r['effort']['compute' if axis == 'human' else 'human'], r['id']))
        sorted_records[axis] = [r['id'] for r in order]
        lines = [f'# Workflows ordered by {names[axis]}', '',
                 'The ratings are ordinal comparisons under each dossier’s stated input and output conditions. '
                 'Ties remain in the same class. Setup and the other axis break display-order ties; the numbers are not durations or benchmark results.', '',
                 f'[Scales and assumptions]({DETAILS / "README.md"}); [structured details]({DETAILS / "workflow-details.json"}).', '',
                 '| Workflow | Manual | Setup | Computing | Recorded operations |', '| --- | ---: | ---: | ---: | ---: |']
        for r in order:
            e = r['effort']
            lines += [f'| [{r["id"]} — {r["name"]}]({DETAILS / (r["id"].lower()+".md")}) | {e["human"]} | {e["setup"]} | {e["compute"]} | {r["recorded_operations"]} |']
        (DETAILS / f'by-{axis}.md').write_text('\n'.join(line.rstrip() for line in lines).rstrip() + '\n')
    dump(DETAILS / 'detail-checks.json', {'date': args.date, 'workflow_count': len(records),
         'source_references': 'passed', 'required_detail_fields': 'passed',
         'complete_recipe_coverage': 'passed', 'documented_entrypoint_references': 'passed',
         'ordered_workflows': sorted_records,
         'errors': [], 'scope': 'Workflow documentation, classification and source-reference consistency.'})
    print(json.dumps({'workflows': len(records), 'errors': []}, indent=2))


if __name__ == '__main__':
    main()
