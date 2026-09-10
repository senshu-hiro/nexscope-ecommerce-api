#!/usr/bin/env python3
"""Validate offline coverage, catalog links, definitions and attribution."""
import ast
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def validate():
    catalog = json.loads((ROOT / 'catalog/apis.json').read_text())
    apis = catalog['apis']
    assert len(apis) == catalog['count'] == 225
    assert len({a['slug'] for a in apis}) == 225
    assert Counter(a['family'] for a in apis) == catalog['counts'] == {'data': 172, 'creative': 53}
    assert Counter(a['category'] for a in apis) == {c['name']: c['count'] for c in catalog['categories']}
    assert len(catalog['categories']) == 20
    readme = (ROOT / 'README.md').read_text()
    referenced = set()
    for api in apis:
        slug = api['slug']
        assert re.fullmatch(r'[a-z0-9-]+', slug)
        assert api['endpoint'] == f'https://api.nexscope.ai/api/skill-api/v1/skills/{slug}/run'
        assert f'[{api["name"]}]({api["localDoc"]})' in readme
        assert api['asyncTask'] == (api['family'] == 'creative')
        if api['asyncTask']:
            assert api['taskResultEndpoint'] == f'https://api.nexscope.ai/api/skill-api/v1/skills/{slug}/tasks/{{taskId}}'
        for field in ('localDoc', 'requestSchema', 'responseSchema', 'payload', 'responseExample'):
            path = ROOT / api[field]
            assert path.is_file(), path
            referenced.add(path)
        for kind in ('request', 'response'):
            schema = json.loads((ROOT / api[kind + 'Schema']).read_text())
            assert ('field-descriptors' if 'fields' in schema else 'json-schema') == api[kind + 'SchemaFormat']
    actual = set((ROOT/'docs/data').glob('*.md')) | set((ROOT/'docs/creative').glob('*.md'))
    actual |= set((ROOT/'schemas').glob('*.json')) | set((ROOT/'payloads').glob('*.json')) | set((ROOT/'examples/responses').glob('*.json'))
    assert referenced == actual, 'Missing or orphaned API artifacts'
    for path in ROOT.rglob('*'):
        if not path.is_file() or any(p in ('.git','__pycache__') for p in path.parts): continue
        if path.suffix == '.json': json.loads(path.read_text())
        if path.suffix == '.py': ast.parse(path.read_text())
        if path.suffix == '.md':
            text = path.read_text()
            for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                if link.startswith(('https://', 'http://', '#')): continue
                assert (path.parent / link.split('#')[0]).exists(), (path, link)
            for url in re.findall(r'https://www\.nexscope\.ai/[^\s)]+', text):
                assert 'co-from=github-ecommerce-api' in url, (path, url)
    print('PASS: 225 APIs, 20 categories, 225 docs, 450 definitions, 225 payloads, 225 response fixtures; links and attribution checked.')

if __name__ == '__main__':
    validate()
