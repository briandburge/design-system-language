from pathlib import Path
import json, re, sys

root = Path(__file__).resolve().parents[1]
errors = []

required = [
    'README.md', 'rules/rules.yaml', 'audit/rubric.md',
    'audit/report-template.md', 'schemas/rules.schema.json'
]
for item in required:
    if not (root / item).exists():
        errors.append(f'Missing required file: {item}')

text = (root / 'rules/rules.yaml').read_text(encoding='utf-8')
ids = re.findall(r'^  - id: (DL-\d{3})$', text, re.M)
if len(ids) != len(set(ids)):
    errors.append('Duplicate rule IDs found')
if not ids:
    errors.append('No rule IDs found')

try:
    json.loads((root / 'schemas/rules.schema.json').read_text(encoding='utf-8'))
except Exception as exc:
    errors.append(f'Invalid JSON schema: {exc}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)

print(f'Validation passed: {len(ids)} rules found.')
