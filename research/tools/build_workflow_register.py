#!/usr/bin/env python3
"""Build research registers from retained reports and domain workflow records."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import os
import copy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / 'research'
GENERATED = {'source-register.md', 'README.md'}
LINK = re.compile(r'\[([^\]]+)\]\((https?://[^\s)]+)\)')
BARE = re.compile(r'https?://[^\s<>`]+')


def read_json(path):
    return json.loads(path.read_text())


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')


def sid(locator):
    return 'SRC-' + hashlib.sha256(locator.encode()).hexdigest()[:12]


def clean(text):
    text = LINK.sub(lambda m: m.group(1), text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', lambda m: m.group(1), text)
    return re.sub(r'\s+', ' ', text.replace('|', ';').replace('**', '')).strip(' ;')


def urls(text):
    found = {m.group(2) for m in LINK.finditer(text)}
    for match in BARE.finditer(LINK.sub("", text)):
        value = match.group().rstrip('.,;:')
        # Markdown link syntax closes outside the URL; supplied URLs contain no
        # literal parentheses in the retained reports.
        value = value.split(')', 1)[0]
        if value:
            found.add(value)
    return sorted(found)


def canonical_locator(locator):
    if locator.startswith(('scripts/', 'skills/', 'tests/', 'docs/', 'research/', 'execution/')):
        return '${MODELING_ROOT}/' + locator
    return locator


def merge_source_records(root, documents, date, check=False):
    """Merge attributed source records without rebuilding unrelated workflow outputs."""
    root = Path(root)
    directory = root / 'research/sources'
    json_path, markdown_path = directory / 'source-register.json', directory / 'source-register.md'
    original = read_json(json_path)
    result = copy.deepcopy(original)
    result['source_record_documents'] = sorted(set(result.get('source_record_documents', [])) | set(map(str, documents)))
    by_locator = {canonical_locator(item.get('url') or item['local_source_path']): item
                  for item in result['sources']}
    touched = set()
    for document in documents:
        document = str(document)
        value = read_json(root / document)
        entries = value if isinstance(value, list) else value.get('sources', value.get('records', []))
        if not isinstance(entries, list) or not entries:
            raise ValueError('Source record document has no records: ' + document)
        for entry in entries:
            locator = next((entry.get(key) for key in ('url', 'local_original', 'local_path', 'source_path')
                            if entry.get(key)), None)
            if not all((locator, entry.get('title'), entry.get('summary'), entry.get('evidence_status'))):
                raise ValueError('Incomplete attributed source record in ' + document)
            locator = canonical_locator(locator)
            item = by_locator.get(locator)
            if item is None:
                item = {'id': sid(locator), 'url': locator if locator.startswith(('https://', 'http://')) else None,
                        'local_source_path': None if locator.startswith(('https://', 'http://')) else locator,
                        'title': entry['title'], 'summary': entry['summary'], 'registered_at': date,
                        'evidence_statuses': [], 'observations': [], 'referring_documents': []}
                result['sources'].append(item)
                by_locator[locator] = item
            observation = dict(entry, source_record_document=document)
            if observation not in item['observations']:
                item['observations'].append(observation)
            if entry['evidence_status'] not in item['evidence_statuses']:
                item['evidence_statuses'].append(entry['evidence_status'])
            for referring in [document] + entry.get('referring_documents', []):
                if referring not in item['referring_documents']:
                    item['referring_documents'].append(referring)
            touched.add(item['id'])
    markdown = markdown_path.read_text()
    for item in result['sources']:
        if item['id'] not in touched:
            continue
        locator = item['url'] or item['local_source_path']
        if locator.startswith('${MODELING_ROOT}/'):
            target = os.path.relpath(root / locator.removeprefix('${MODELING_ROOT}/'), directory)
            source = f'[{locator}]({target})'
        elif locator.startswith(('https://', 'http://')):
            source = f'[{locator}]({locator})'
        else:
            source = f'`{locator}`'
        block = '\n'.join([f'<a id="{item["id"].lower()}"></a>', '',
                           f'## {item["id"]} — {item["title"]}', '',
                           f'Original source: {source}', '', f'Summary: {item["summary"]}', '',
                           'Evidence: ' + ', '.join(item['evidence_statuses']) + '.', '',
                           'Documents: ' + ', '.join(item['referring_documents']) + '.', '']) + '\n'
        pattern = (r'<a id="' + re.escape(item['id'].lower()) +
                   r'"></a>\n\n*#{2,3} [^\n]*\n.*?(?=<a id="|^#{2,3} |\Z)')
        if re.search(pattern, markdown, re.S | re.M):
            markdown = re.sub(pattern, lambda match: block, markdown, flags=re.S | re.M)
        else:
            markdown = markdown.rstrip() + '\n\n' + block
    markdown = markdown.rstrip() + '\n'
    if check:
        if result != original or markdown != markdown_path.read_text():
            raise ValueError('Combined source register is stale for: ' + ', '.join(map(str, documents)))
    else:
        write_json(json_path, result)
        markdown_path.write_text(markdown)
    return {'result': 'PASS', 'mode': 'check' if check else 'merge', 'source_records': len(touched)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', required=True, help='Explicit client date YYYY-MM-DD')
    parser.add_argument('--source-record', action='append', help='Merge only this attributed source-record document; repeat as needed')
    parser.add_argument('--check', action='store_true', help='Check the selected source-record merge without writing')
    args = parser.parse_args()
    date = args.date
    if args.source_record:
        print(merge_source_records(ROOT, args.source_record, date, check=args.check))
        return
    if args.check:
        parser.error('--check requires --source-record')
    existing_register = RESEARCH / 'sources/source-register.json'
    supplemental_documents = read_json(existing_register).get('source_record_documents', []) if existing_register.exists() else []
    records = {}

    def register(url, title, summary, evidence, document, **extra):
        key = url
        item = records.setdefault(key, {
            'id': sid(key), 'url': None if url.startswith('/') else url,
            'local_source_path': url if url.startswith('/') else None,
            'title': title or url, 'summary': clean(summary),
            'registered_at': date, 'evidence_statuses': [],
            'observations': [], 'referring_documents': [],
        })
        if evidence not in item['evidence_statuses']:
            item['evidence_statuses'].append(evidence)
        if document not in item['referring_documents']:
            item['referring_documents'].append(document)
        if extra:
            item['observations'].append({'evidence_status': evidence, **extra})
        if evidence in {'web_inspected', 'downloaded_original'}:
            item['title'], item['summary'] = title, clean(summary)
        return item

    # Register all URLs already written in project research, preserving their
    # report-level status instead of asserting a fresh source inspection.
    paths = [ROOT / 'README.md', ROOT / 'skills/README.md']
    paths += sorted(RESEARCH.glob('*.md'))
    paths += sorted((RESEARCH / 'workflows').glob('*-paths.md'))
    paths += sorted((RESEARCH / 'workflows/details').glob('*.md'))
    paths += sorted((RESEARCH / 'action-audit').rglob('*.md'))
    for path in paths:
        if path.name in {'source-register.md', 'workflow-map.md', 'ideas-register.md'}:
            continue
        document = str(path.relative_to(ROOT))
        for line in path.read_text().splitlines():
            labels = {url: label for label, url in LINK.findall(line)}
            for url in urls(line):
                summary = clean(line)
                if len(summary) > 1000:
                    summary = summary[:997] + '...'
                register(url, labels.get(url, url), summary,
                         'existing_report_registered', document)

    # Existing local originals are referenced in place with their actual hashes.
    for old in read_json(RESEARCH / 'sources/local-evidence.json'):
        locator = old['local_path']
        records[locator] = {
            'id': sid(locator), 'url': old.get('url'),
            'local_source_path': locator, 'title': old['title'],
            'summary': 'Existing local source inspected in the initial research; '
                       'its use is described in research/local-baseline.md.',
            'registered_at': date, 'evidence_statuses': ['local_source_inspected'],
            'observations': [old],
            'referring_documents': ['research/local-baseline.md',
                                    'research/sources/local-evidence.json'],
        }

    for path in sorted((RESEARCH / 'sources').glob('round-*/*-sources.json')):
        entries = read_json(path)
        if isinstance(entries, dict):
            entries = entries.get('sources', entries.get('records', []))
        for item in entries:
            locator = item.get('url') or item.get('local_original') or item.get('source_path')
            if not locator:
                raise ValueError(f'{path}: source has no original URL or local path: {item.get("title")}')
            register(locator, item['title'], item['summary'],
                     item['evidence_status'], str(path.relative_to(ROOT)),
                     **{k: v for k, v in item.items()
                        if k not in {'url', 'title', 'summary', 'evidence_status'}})

    domains = []
    for name in ['cad', 'reconstruction', 'domain']:
        path = RESEARCH / f'workflows/{name}-paths.json'
        if path.exists():
            domains.append(read_json(path))
    operations = [op for domain in domains for op in domain['operations']]
    recipes = [recipe for domain in domains for recipe in domain['recipes']]
    ideas = [idea for domain in domains for idea in domain['ideas']]
    combined_path = RESEARCH / 'workflows/combined-paths.json'
    if combined_path.exists():
        combined = read_json(combined_path)
        recipes += combined.get('recipes', [])
        ideas += combined.get('ideas', [])
    audit_ideas = RESEARCH / 'action-audit/ideas.json'
    if audit_ideas.exists():
        ideas += read_json(audit_ideas)['ideas']
    op_index = {op['id']: op for op in operations}
    errors = []
    if len(op_index) != len(operations):
        errors.append('Duplicate operation ID')
    for group, items in [('operation', operations), ('recipe', recipes), ('idea', ideas)]:
        for item in items:
            refs = []
            for url in item.get('source_urls', []):
                if url not in records:
                    errors.append(f'{group} {item["id"]}: source not registered: {url}')
                else:
                    refs.append(records[url]['id'])
            item['source_ids'] = refs
    for recipe in recipes:
        available = set(recipe['inputs'])
        for step in recipe['steps']:
            if step not in op_index:
                errors.append(f'{recipe["id"]}: unknown operation {step}')
                continue
            op = op_index[step]
            role_types = {role['type'] for role in op.get('input_roles', []) if role.get('type')}
            required = (set(op['inputs']) | role_types) - available
            if required:
                errors.append(f'{recipe["id"]}: {step} requires {sorted(required)}')
            choice_groups = list(op.get('input_choice_groups', []))
            if op.get('input_alternatives'):
                choice_groups.append(op['input_alternatives'])
            for alternatives in choice_groups:
                if not any(set(group) <= available for group in alternatives):
                    errors.append(f'{recipe["id"]}: {step} requires one input group {alternatives}')
            available.update(op['outputs'])
        recipe['available_representation_types_after_steps'] = sorted(available)
    # Register the earlier numbered proposals individually. Their original
    # document is the source of the proposal; external evidence lives in the
    # source-backed domain operations and retained tool assessments.
    plan = RESEARCH / 'implementation-plan.md'
    section = ''
    for line_number, line in enumerate(plan.read_text().splitlines(), 1):
        if line.startswith('#'):
            section = line.lstrip('# ').strip()
        if re.match(r'^\d+\. ', line):
            summary = re.sub(r'^\d+\. ', '', line)
            ideas.append({
                'id': 'PLAN-' + hashlib.sha256((section + summary).encode()).hexdigest()[:10],
                'name': clean(summary).split(':', 1)[0][:120].rstrip(),
                'summary': summary, 'status': 'proposal',
                'origin': 'retained_implementation_plan',
                'source_documents': [{'path': 'research/implementation-plan.md',
                                      'line': line_number, 'section': section}],
                'source_urls': urls(line),
                'source_ids': [records[url]['id'] for url in urls(line) if url in records],
                'next_check': 'Use the associated workflow operation and stage checks.',
            })
    # Edges represent possible data handoffs. They describe shared types only;
    # full execution also requires every input and the recorded prerequisites.
    handoffs = []
    for left in operations:
        for right in operations:
            alternatives = list(right.get('input_alternatives', []))
            alternatives += [group for choices in right.get('input_choice_groups', []) for group in choices]
            role_types = {role['type'] for role in right.get('input_roles', []) if role.get('type')}
            received = set(right['inputs']) | role_types | {kind for group in alternatives for kind in group}
            shared = sorted(set(left['outputs']) & received)
            if shared and left['id'] != right['id']:
                handoffs.append({'from': left['id'], 'to': right['id'],
                                 'representation_types': shared,
                                 'status': 'candidate_data_handoff',
                                 'requires_all_inputs_and_prerequisites': True})
    type_definitions = read_json(RESEARCH / 'workflows/representations.json')['types']
    for domain in domains:
        type_definitions.update(domain.get('type_definitions', {}))
    used_types = set()
    for op in operations:
        used_types.update(op['inputs'] + op['outputs'])
        used_types.update(role['type'] for role in op.get('input_roles', []) if role.get('type'))
        used_types.update(kind for group in op.get('input_alternatives', []) for kind in group)
        used_types.update(kind for choice in op.get('input_choice_groups', []) for group in choice for kind in group)
    undefined_types = sorted(used_types - set(type_definitions))
    if undefined_types:
        errors.append('Representation definitions required: ' + ', '.join(undefined_types))
    graph = {
        'schema_version': 1, 'research_date': date,
        'scope': 'Reusable operation families and explicitly documented composed recipes',
        'semantics': {
            'inputs': 'All inputs are required; input_alternatives requires one complete alternative set; input_choice_groups requires one complete alternative set from each independent choice group.',
            'edges': 'Candidate data flow only; prerequisites, units, frames, geometry and evidence status must also hold.',
            'recipes': 'Proposed compositions. Type availability checks validate the written sequence, not software execution.',
            'iterations': 'An edit or remeasurement produces a new revision; retain prior evidence and compare the changed revision.',
        },
        'type_definitions': type_definitions,
        'operations': operations, 'recipes': recipes, 'candidate_handoffs': handoffs,
    }
    for item in records.values():
        item['referring_documents'].sort()
    register_path = RESEARCH / 'sources/source-register.json'
    write_json(register_path, {'schema_version': 1, 'registered_at': date,
                              'sources': sorted(records.values(), key=lambda x: x['id'])})
    write_json(RESEARCH / 'workflows/workflow-map.json', graph)
    write_json(RESEARCH / 'ideas-register.json', {'schema_version': 1,
               'registered_at': date, 'ideas': ideas})
    lines = ['# Source register', '', f'Registered: {date}.', '',
             'Each entry preserves the original URL or local source path and records '
             'its summary, evidence status and referring documents. Detailed observations '
             f'are retained in [source-register.json]({RESEARCH / "sources/source-register.json"}).', '']
    for item in sorted(records.values(), key=lambda x: x['id']):
        locator = item['url'] or item['local_source_path']
        lines += [f'<a id="{item["id"].lower()}"></a>', '', f'## {item["id"]} — {item["title"]}', '',
                  f'Original source: [{locator}]({locator})', '',
                  f'Summary: {item["summary"]}', '',
                  'Evidence: ' + ', '.join(item['evidence_statuses']) + '.', '',
                  'Documents: ' + ', '.join(item['referring_documents']) + '.', '']
    (RESEARCH / 'sources/source-register.md').write_text('\n'.join(lines).rstrip() + '\n')
    if supplemental_documents:
        merge_source_records(ROOT, supplemental_documents, date)
    idea_lines = ['# Ideas and research questions', '', f'Registered: {date}.', '',
                  'The records retain project proposals, experiment questions and the earlier implementation-plan ideas. '
                  f'Each record identifies its origin and supporting sources. Detailed records: [ideas-register.json]({RESEARCH / "ideas-register.json"}).', '']
    for idea in ideas:
        idea_lines += [f'## {idea["id"]} — {idea["name"]}', '',
                       f'Status: {idea["status"]}.', '', idea['summary'], '']
        for url in idea.get('source_urls', []):
            idea_lines += [f'Original source: [{url}]({url})', '']
        for doc in idea.get('source_documents', []):
            path = doc['path']
            idea_lines += [f'Original proposal: [{path}]({ROOT / path}), line {doc["line"]}.', '']
        idea_lines += ['Next check: ' + idea.get('next_check', 'See the associated operation checks.'), '']
    (RESEARCH / 'ideas-register.md').write_text('\n'.join(idea_lines).rstrip() + '\n')
    catalog = ['# Operation catalogue', '', f'Registered: {date}.', '',
               'All `inputs` apply together. Alternative sets and independent choice groups are recorded explicitly. '
               f'Full prerequisites, changes, checks and evidence are in [workflow-map.json]({RESEARCH / "workflows/workflow-map.json"}) and the domain reports.', '',
               '| Operation | Required inputs and choices | Outputs | Summary and original sources |',
               '| --- | --- | --- | --- |']
    for op in operations:
        ins = ', '.join(op['inputs']) or 'see choices'
        if op.get('input_alternatives'):
            ins += '; choose ' + ' OR '.join(' + '.join(g) for g in op['input_alternatives'])
        for choices in op.get('input_choice_groups', []):
            ins += '; also choose ' + ' OR '.join(' + '.join(g) for g in choices)
        refs = ' '.join(f'[source {i+1}]({url})' for i, url in enumerate(op['source_urls']))
        summary = op.get('summary', op['name']).replace('|', ';').replace('\n', ' ')
        catalog += [f'| {op["id"]} — {op["name"]} | {ins} | {", ".join(op["outputs"])} | {summary} {refs} |']
    (RESEARCH / 'workflows/operation-catalogue.md').write_text('\n'.join(catalog).rstrip() + '\n')
    report = {'date': date, 'sources': len(records), 'operations': len(operations),
              'recipes': len(recipes), 'ideas': len(ideas),
              'candidate_handoffs': len(handoffs), 'errors': errors,
              'check_meaning': 'Registration and declared type consistency, not tool execution or geometric validation'}
    write_json(RESEARCH / 'workflows/register-checks.json', report)
    print(json.dumps(report, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
