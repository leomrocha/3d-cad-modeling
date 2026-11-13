#!/usr/bin/env python3
"""Existing-session OCS native control. Discovery/read default; explicit guarded writes."""
import argparse
import json
import os
import socket
import sys
from pathlib import Path

READ_OPS = frozenset({
    'hello', 'state', 'capabilities', 'commands', 'entity_schema', 'record_schema',
    'records', 'entities', 'query', 'layers', 'header', 'properties', 'measure',
    'snap', 'grips', 'history', 'events', 'operation', 'batch_result', 'guide',
    'validate', 'xdata_get', 'audit', 'text_search', 'text_audit', 'get_selection',
})
MAX_RESPONSE = 16 * 1024 * 1024


class ControlError(Exception):
    pass


class WriteUncertain(ControlError):
    def __init__(self, request_id):
        self.request_id = request_id
        super().__init__('Write completion unknown; inspect the existing operation before any retry')


def redact(value):
    if isinstance(value, dict):
        return {k: '[redacted]' if k.lower() in {'token', 'authorization', 'cookie'}
                else redact(v) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    return value


def load_descriptor(path):
    d = json.loads(Path(path).read_text())
    if not isinstance(d, dict) or not isinstance(d.get('session_id'), str):
        raise ControlError('Invalid OCS session descriptor identity')
    if not d['session_id'] or not isinstance(d.get('token'), str) or not d['token']:
        raise ControlError('Invalid OCS session descriptor authentication')
    if type(d.get('port')) is not int or not 1 <= d['port'] <= 65535:
        raise ControlError('Invalid OCS loopback port')
    return d


def candidate_paths(explicit=None):
    if explicit:
        return [Path(explicit)]
    home = Path.home()
    config = Path(os.environ.get('XDG_CONFIG_HOME', str(home / '.config')))
    paths = list((config / 'OpenCADStudio' / 'automation').glob('*.json'))
    paths += list((home / 'snap' / 'open-cad-studio').glob(
        '*/.config/OpenCADStudio/automation/*.json'))
    return sorted(set(p.resolve() for p in paths))


def request(d, payload, timeout=15):
    if any(k in payload for k in ('token', 'protocol', 'session_id')):
        raise ControlError('Authentication/envelope fields are supplied by the helper')
    wire = dict(payload, protocol=1, session_id=d['session_id'], token=d['token'])
    encoded = json.dumps(wire, allow_nan=False).encode() + b'\n'
    with socket.create_connection(('127.0.0.1', d['port']), timeout=timeout) as sock:
        sock.settimeout(timeout)
        sock.sendall(encoded)
        result = bytearray()
        while b'\n' not in result:
            block = sock.recv(65536)
            if not block:
                break
            result.extend(block)
            if len(result) > MAX_RESPONSE:
                raise ControlError('OCS response exceeds 16 MiB; query a narrower scope')
    if not result:
        raise ControlError('OCS closed the connection without a response')
    return json.loads(bytes(result).split(b'\n', 1)[0])


def descriptors(explicit=None, session=None):
    found = {}
    for path in candidate_paths(explicit):
        try:
            d = load_descriptor(path)
        except (OSError, ValueError, ControlError):
            if explicit:
                raise
            continue
        if session is None or d['session_id'] == session:
            found[d['session_id']] = d
    return list(found.values())


def execute_checked(d, payload, allow_write=False, timeout=15, transport=request):
    if not allow_write:
        raise ControlError('Write refused: --allow-write requires existing author authorization')
    if any(k in payload for k in ('token', 'protocol', 'session_id')):
        raise ControlError('Authentication/envelope fields are supplied by the helper')
    if payload.get('op') in READ_OPS:
        raise ControlError('Use read for read-only operations')
    if not isinstance(payload.get('op'), str) or not payload['op']:
        raise ControlError('Missing operation')
    if not isinstance(payload.get('request_id'), str) or not 1 <= len(payload['request_id']) <= 128:
        raise ControlError('Write requires a caller-stable request_id (1..128 characters)')
    for field in ('document_id', 'revision'):
        if type(payload.get(field)) is not int:
            raise ControlError('Write requires integer ' + field)
    # Reject non-JSON/NaN/Infinity before any preflight or mutation I/O.
    json.dumps(payload, allow_nan=False)
    state = transport(d, {'op': 'state'}, timeout)
    if not isinstance(state, dict) or state.get('ok') is not True:
        raise ControlError('Could not establish current OCS state; write not sent')
    if state.get('read_only') is True:
        raise ControlError('OCS session is read-only; write not sent')
    for field in ('document_id', 'revision'):
        if state.get(field) != payload[field]:
            raise ControlError('Current ' + field + ' differs; write not sent')
    if 'geometry_revision' in payload and payload['geometry_revision'] != state.get('geometry_revision'):
        raise ControlError('Current geometry_revision differs; write not sent')
    try:
        return transport(d, payload, timeout)  # exactly once; never retry automatically
    except (OSError, ValueError, ControlError):
        raise WriteUncertain(payload['request_id']) from None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='mode', required=True)
    for mode in ('discover', 'read', 'execute'):
        p = sub.add_parser(mode)
        p.add_argument('--descriptor')
        p.add_argument('--session')
        p.add_argument('--timeout', type=float, default=15)
        if mode != 'discover':
            sources = p.add_mutually_exclusive_group(required=True)
            sources.add_argument('--request')
            sources.add_argument('--request-file')
        if mode == 'execute':
            p.add_argument('--allow-write', action='store_true')
    args = parser.parse_args(argv)
    payload = None
    try:
        if args.timeout <= 0 or not args.timeout < float('inf'):
            raise ControlError('Timeout must be finite and positive')
        ds = descriptors(args.descriptor, args.session)
        if args.mode == 'discover':
            sessions = []
            for d in ds:
                try:
                    r = request(d, {'op': 'hello'}, args.timeout)
                    sessions.append({k: r.get(k) for k in (
                        'ok', 'session_id', 'version', 'document_id', 'revision', 'documents')})
                except (OSError, ValueError, ControlError) as e:
                    sessions.append({'session_id': d['session_id'], 'error': str(e)})
            print(json.dumps({'sessions': redact(sessions)}, indent=2))
            return 0 if any(s.get('ok') for s in sessions) else 2
        if len(ds) != 1:
            raise ControlError('Select exactly one existing session with --session or --descriptor')
        text = Path(args.request_file).read_text() if args.request_file else args.request
        payload = json.loads(text)
        if not isinstance(payload, dict):
            raise ControlError('Request must be a JSON object')
        if args.mode == 'read':
            if payload.get('op') not in READ_OPS:
                raise ControlError('Operation is not in the read-only allowlist')
            result = request(ds[0], payload, args.timeout)
        else:
            result = execute_checked(ds[0], payload, args.allow_write, args.timeout)
        print(json.dumps(redact(result), indent=2, allow_nan=False))
        if isinstance(result, dict) and (result.get('ok') is False or result.get('status') in {'failed', 'rejected'}):
            return 1
        return 0
    except WriteUncertain as e:
        print(json.dumps({'error': 'write_response_unavailable', 'completion': 'unknown',
                          'request_id': e.request_id,
                          'next_action': 'Inspect state/operation; do not replay under a new request_id'}))
        return 3
    except (TimeoutError, socket.timeout):
        print(json.dumps({'error': 'timeout', 'write_request_sent': False,
                          'next_action': 'Read/discovery or preflight timed out; no mutation request was sent'}))
        return 3
    except (OSError, ValueError, ControlError) as e:
        print(json.dumps({'error': type(e).__name__, 'message': str(e)}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
