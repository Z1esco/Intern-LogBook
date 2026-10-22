#!/usr/bin/env python3
"""Validate date, section structure, links, and registry of internship logbook."""
from pathlib import Path
from datetime import datetime
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FIELDS = (
    "## 🏷️ Title",
    "## 📋 Descriptions of Jobs/Tasks/Project",
    "## 🛠️ Activities/Work Produced",
    "## 💡 Comments/Conclusion",
)
errors = []
entries = sorted((ROOT / 'logbook').glob('20[0-9][0-9]/*/20[0-9][0-9]-[0-1][0-9]-[0-3][0-9]-day-*.md'))

if not entries:
    errors.append('No daily Markdown entries found')

for path in entries:
    raw = path.read_text(encoding='utf-8')
    relative = path.relative_to(ROOT)
    match = re.fullmatch(r'(\d{4}-\d{2}-\d{2})-day-(\d{2})\.md', path.name)
    if not match:
        errors.append(f'{relative}: invalid filename')
        continue
    iso, sequence = match.groups()
    day = datetime.strptime(iso, '%Y-%m-%d')
    if f'date: {iso}' not in raw:
        errors.append(f'{relative}: missing matching date metadata')
    if f'day: {int(sequence):02d}' not in raw:
        errors.append(f'{relative}: missing matching day metadata')
    if day.strftime('%B').lower() not in path.parent.name:
        errors.append(f'{relative}: month folder does not match date')
    positions = [raw.find(field) for field in FIELDS]
    if -1 in positions or positions != sorted(positions):
        errors.append(f'{relative}: expected four form sections in order')
        continue
    for i, field in enumerate(FIELDS):
        start = positions[i] + len(field)
        end = positions[i + 1] if i + 1 < len(FIELDS) else raw.find('\n---', start)
        if end == -1:
            end = len(raw)
        body = raw[start:end].strip()
        body = re.sub(r'\n+<sub>.*?</sub>\s*', '', body, flags=re.S)
        if not body:
            errors.append(f'{relative}: empty section {field}')
        if re.search(r'(?m)^\s*(?:[-*+] |\d+\. )', body):
            errors.append(f'{relative}: bullet/numbered list inside {field}')
        if len(re.split(r'\n\s*\n', body)) > 1:
            errors.append(f'{relative}: multiple paragraphs inside {field}')
    actual_header = day.strftime('%A, %-d %B %Y')
    if actual_header not in raw:
        errors.append(f'{relative}: incorrect or absent weekday/date header: {actual_header}')

for path in ROOT.rglob('*.md'):
    raw = path.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)', raw):
        if target.startswith(('https://','http://','#','mailto:')):
            continue
        target = target.split('#', 1)[0]
        if not target:
            continue
        resolved = path.parent / target
        if not resolved.exists():
            errors.append(f'{path.relative_to(ROOT)}: broken local link {target}')

root_readme=(ROOT/'README.md').read_text(encoding='utf-8')
entry_badge=f'Entries-{len(entries):02d}'
if entry_badge not in root_readme:
    errors.append(f'README.md: entries badge does not show {len(entries):02d}')
if f'<br/>{len(entries):02d}</td>' not in root_readme:
    errors.append('README.md: Days logged dashboard count may be outdated')
for path in entries:
    rel=str(path.relative_to(ROOT)).replace('\\','/')
    if rel not in root_readme:
        errors.append(f'README.md: missing link to {rel}')

if errors:
    for error in errors:
        print('FAIL:', error)
    sys.exit(1)
print(f'PASS: {len(entries)} entries, form structure, metadata, relative links, and README references validated.')
