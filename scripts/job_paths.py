"""Resolve portable CAD paths from selected job inputs and local setup."""

from pathlib import Path
import re

try:
    from .operation_catalogue import load, location
except ImportError:
    from operation_catalogue import load, location


NAMED_PATH = re.compile(r'\$\{([A-Za-z_][A-Za-z0-9_]*)\}/(.*)')
NAME = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')
SKILL_ROOT = Path(__file__).resolve().parent.parent


def parse_roots(entries):
    """Read optional overrides for historic named roots."""
    roots = {}
    for entry in entries:
        name, separator, value = entry.partition('=')
        if not separator or not NAME.fullmatch(name) or not Path(value).is_absolute():
            raise ValueError('--root requires NAME=ABSOLUTE_PATH')
        if name in roots:
            raise ValueError('Duplicate configured path root: ' + name)
        roots[name] = Path(value).resolve()
    return roots


def selected_roots(overrides=None, *, job=None, project=None, cad=None,
                   evidence=None, output=None, index=None, work_index=None):
    """Derive known folder origins from normal arguments and catalogue settings."""
    roots = dict(overrides or {})
    origins = {
        'PROJECT_ROOT': project,
        'CAD_ROOT': cad,
        'JOB_ROOT': Path(job).resolve().parent if job is not None else None,
        'EVIDENCE_ROOT': evidence,
        'OUTPUT_ROOT': Path(output).resolve().parent if output is not None else None,
        'INDEX_ROOT': Path(index).resolve().parent if index is not None else None,
        'WORK_INDEX_ROOT': Path(work_index).resolve().parent if work_index is not None else None,
        'SKILL_ROOT': SKILL_ROOT,
    }
    for name, path in origins.items():
        if path is not None:
            roots.setdefault(name, Path(path).resolve())
    try:
        parts = parts_roots()
    except (OSError, ValueError, KeyError, TypeError):
        # Jobs using other origins can run even if the optional catalogue is unavailable.
        parts = {}
    for name, path in parts.items():
        roots.setdefault(name, path)
    return roots


def configured_parts(catalogue=None):
    """Yield saved parts resources and their declared search methods."""
    for resource in load(catalogue or location())['resources']:
        methods = [method for method in resource.get('methods', []) if method.get('probe') == 'parts']
        if methods:
            yield resource, methods


def parts_root_name(resource_id):
    return 'PARTS_' + resource_id.encode('utf-8').hex()


def parts_roots():
    roots = {}
    parts = set()
    for resource, _ in configured_parts():
        path = Path(resource['location'])
        if not path.is_absolute():
            raise ValueError('Configured parts catalogue path must be absolute')
        path = path.resolve()
        resource_id = resource['id']
        # Encode the complete ID without collisions between catalogue names.
        roots[parts_root_name(resource_id)] = path
        parts.add(path)
    if len(parts) == 1:
        roots = {'PARTS_ROOT': next(iter(parts)), **roots}
    return roots


def rooted_path(locator, roots, base=None):
    """Resolve a locator against its declared or supplied context."""
    if not isinstance(locator, (str, Path)) or not str(locator).strip():
        raise ValueError('Path must be a nonempty locator')
    value = str(locator)
    match = NAMED_PATH.fullmatch(value)
    if match:
        name, suffix = match.groups()
        if '${' in suffix:
            raise ValueError('Malformed path root locator: ' + value)
        if name not in roots and name.startswith('PARTS_'):
            try:
                roots = {**parts_roots(), **roots}
            except (OSError, ValueError, KeyError, TypeError) as error:
                raise ValueError(f'Cannot read saved parts catalogue for {name}: {error}') from error
        if name not in roots:
            detail = ' (select a specific configured parts catalogue)' if name == 'PARTS_ROOT' else ''
            raise ValueError('Missing configured path root: ' + name + detail)
        root = Path(roots[name])
        if not root.is_absolute():
            raise ValueError('Configured path root must be absolute: ' + name)
        root = root.resolve()
        path = (root / suffix).resolve()
        if not path.is_relative_to(root):
            raise ValueError('Path escapes its configured root: ' + value)
        return path
    if '${' in value:
        raise ValueError('Malformed path root locator: ' + value)
    path = Path(value)
    if path.is_absolute():
        return path.resolve()
    if base is None:
        raise ValueError('Relative path requires a selected record directory')
    return (Path(base) / path).resolve()


def add_job_sources(roots, job, directory):
    """Bind external source directories to stable aliases from selected locators."""
    sources = []
    for field, key in (('features', 'source'), ('source_files', 'path')):
        rows = job.get(field)
        if isinstance(rows, list):
            sources.extend(row.get(key) for row in rows if isinstance(row, dict))
    for index, locator in enumerate(sources, 1):
        if isinstance(locator, str) and locator.strip() and '${' not in locator:
            path = rooted_path(locator, roots, directory)
            if not any(path.is_relative_to(Path(root).resolve()) for root in roots.values()):
                roots.setdefault(f'INPUT_{index}_ROOT', path.parent)
    return roots
