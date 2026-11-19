"""Ordered reference closure for a single simple-instance STEP Part 21 DATA section."""
from collections import deque
import hashlib
import json
import re

from step_solid_inventory import _without_comments_and_strings


_TOKEN = re.compile(
    r"(?P<skip>\s+|/\*.*?\*/)|(?P<string>'(?:[^']|'')*')|(?P<ref>#[0-9]+)"
    r"|(?P<enum>\.[A-Z_][A-Z_0-9]*\.)|(?P<number>[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:E[+-]?[0-9]+)?)"
    r"|(?P<name>[A-Z][A-Z0-9_]*)|(?P<symbol>[=(),;*$])", re.DOTALL)
_DATA = re.compile(r'\bDATA\s*;', re.I)
_END = re.compile(r'\bENDSEC\s*;', re.I)


def _tokens(body):
    pos = 0
    while pos < len(body):
        match = _TOKEN.match(body, pos)
        if not match:
            raise ValueError(f'Unsupported Part 21 token at DATA offset {pos}')
        if match.lastgroup != 'skip':
            yield match.lastgroup, match.group()
        pos = match.end()


def _instances(source):
    text = source.decode('latin-1') if isinstance(source, bytes) else source
    if not isinstance(text, str):
        raise TypeError('STEP source must be bytes or text')
    masked = _without_comments_and_strings(text)
    if re.search(r'(?:^|;)\s*(?:ANCHOR|REFERENCE|SIGNATURE)\s*;', masked, re.I):
        raise ValueError('External sections are outside the supported dialect')
    sections = list(re.finditer(r'(?:(?<=;)|^)\s*(?P<tag>DATA)\s*(?=[;(])', masked, re.I))
    if len(sections) != 1 or not (start := _DATA.match(masked, sections[0].start('tag'))):
        raise ValueError('Require one unparameterized DATA section')
    end = _END.search(masked, start.end())
    if not end:
        raise ValueError('Unterminated DATA section')
    tokens = iter(_tokens(text[start.end():end.start()]))
    entities = {}
    for kind, identifier in tokens:
        if kind != 'ref' or next(tokens, None) != ('symbol', '='):
            raise ValueError('Expected numbered entity assignment')
        identifier = int(identifier[1:])
        if identifier == 0 or identifier in entities:
            raise ValueError(f'Invalid or duplicate entity #{identifier}')
        name = next(tokens, None)
        if not name or name[0] != 'name' or next(tokens, None) != ('symbol', '('):
            raise ValueError('Require simple uppercase entity TYPE(parameters)')
        payload = [name, ('symbol', '(')]
        # Each stack item is an aggregate or typed parameter list. Empty lists
        # are permitted. After a comma an actual parameter is mandatory.
        states = ['initial']
        for kind, value in tokens:
            payload.append((kind, value))
            state = states[-1]
            if value == ')' and state in ('initial', 'separator'):
                states.pop()
                if not states:
                    break
            elif value == ',' and state == 'separator':
                states[-1] = 'value'
            elif value == '(' and state in ('initial', 'value', 'typed'):
                states[-1] = 'separator'
                states.append('initial')
            elif state in ('initial', 'value') and kind == 'name':
                states[-1] = 'typed'
            elif state in ('initial', 'value') and (kind in ('string', 'ref', 'enum', 'number') or value in ('*', '$')):
                states[-1] = 'separator'
            else:
                raise ValueError(f'Unsupported parameter in #{identifier}')
        if states or next(tokens, None) != ('symbol', ';'):
            raise ValueError(f'Unterminated entity #{identifier}')
        entities[identifier] = payload
    return entities


def step_entity_graph(source, roots):
    """Fingerprint a directed, ordered subgraph and return its source IDs.

    Root order is significant. Canonical IDs are assigned on first encounter
    during ordered breadth-first traversal. Repeated references, cycles, string
    contents, numeric spelling and every scalar remain significant. Only
    whitespace, comments, declaration order and original entity IDs are ignored.
    This checks lexical structural identity; schema semantics, unit equivalence
    and translation-invariant geometric comparison require separate evidence.
    Complex entity instances, anchors, external references, multiple sections
    and binary literals are outside the supported DATA syntax.
    """
    entities = _instances(source)
    roots = list(roots)
    if not roots or any(type(root) is not int or root <= 0 for root in roots):
        raise ValueError('Provide positive integer root IDs')
    source_ids = []
    canonical = {}
    pending = deque()

    def discover(identifier):
        if identifier not in entities:
            raise ValueError(f'Missing referenced entity #{identifier}')
        if identifier not in canonical:
            canonical[identifier] = len(source_ids)
            source_ids.append(identifier)
            pending.append(identifier)
        return canonical[identifier]

    canonical_roots = [discover(root) for root in roots]
    digest = hashlib.sha256()

    def append(row):
        digest.update(json.dumps(row, separators=(',', ':'), ensure_ascii=True).encode('ascii'))
        digest.update(b'\n')

    append(['step-ordered-graph-v1', canonical_roots])
    while pending:
        identifier = pending.popleft()
        append([[kind, discover(int(value[1:])) if kind == 'ref' else value]
                for kind, value in entities[identifier]])
    return dict(roots=roots, entity_count=len(source_ids), source_ids=source_ids,
                ordered_graph_sha256=digest.hexdigest())
