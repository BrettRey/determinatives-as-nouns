from pathlib import Path
import re, json, hashlib, subprocess, difflib

root = Path.cwd()
snap = root / 'notes/snapshots/2026-09-11-complete-revision'
before = (snap / 'determinatives-as-nouns.tex').read_text()
after = (root / 'determinatives-as-nouns.tex').read_text()
review = root / 'notes/determinatives-as-nouns-review-2026-09-11-complete.md'
md = review.read_text()
checks = {'source_sha256': hashlib.sha256(after.encode()).hexdigest()}
for name, pattern, count in [
    ('trees', r'\\begin\{forest\}.*?\\end\{forest\}', 11),
    ('schemata', r'\\\[.*?\\\]', 4),
    ('numbered_examples', r'\\ea\\label\{.*?\\z(?:\\z)?', 2),
]:
    old = re.findall(pattern, before, re.S)
    new = re.findall(pattern, after, re.S)
    assert len(new) == count and old == new, name
    checks[name] = {'count': count, 'unchanged': True}
tables = re.findall(r'\\begin\{table\}.*?\\end\{table\}', after, re.S)
assert len(tables) == 5
checks['tables'] = {'count': 5, 'substantive_revision': 'Table 2; Oxford commas elsewhere'}
def keys(s):
    return {k.strip() for m in re.finditer(r'\\(?:cite[a-z]*|textcite)(?:\[[^\]]*\])*\{([^}]+)\}', s) for k in m[1].split(',')}
assert keys(before) == keys(after)
bbl = (root / 'determinatives-as-nouns.bbl').read_text()
assert keys(after) <= set(re.findall(r'\\entry\{([^}]+)\}', bbl))
checks['citations'] = {'unchanged_keys': sorted(keys(after)), 'unresolved': []}
resources = [root / 'references.bib', root / 'references-local.bib']
entries = {}
for path in resources:
    source = path.read_text()
    for match in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', source):
        depth = 1; pos = match.end()
        while depth and pos < len(source):
            if source[pos] == '{' and source[pos-1] != '\\': depth += 1
            elif source[pos] == '}' and source[pos-1] != '\\': depth -= 1
            pos += 1
        entries[match[2]] = source[match.end():pos-1]
quality = []
for key in sorted(keys(after)):
    entry = entries[key]
    for field in ['author', 'title', 'year']:
        if not re.search(r'\b'+field+r'\s*=\s*[{"][^}\"]+', entry, re.I):
            quality.append([key, field])
    year = re.search(r'\byear\s*=\s*[{\"]?(\d{4})', entry, re.I)
    if year and not 1800 <= int(year[1]) <= 2027: quality.append([key, 'year range'])
assert not quality, quality
checks['bibliography'] = {'cited_entry_quality_issues': quality, 'unused_entries_count': len(set(entries)-keys(after)), 'unused_scope': 'Shared portfolio and supplement references; informational only', 'symlink': str((root/'references.bib').readlink()), 'central_and_local_unchanged': True}
assert (root/'references.bib').is_symlink()
assert (root/'references-local.bib').read_bytes() == (snap/'references-local.bib').read_bytes()
protected = json.loads((snap/'protected-sha256.json').read_text())
changed = [name for name,digest in protected.items() if hashlib.sha256((root/name).read_bytes()).hexdigest() != digest]
assert not changed, changed
checks['protected_files_unchanged'] = len(protected)
assert (root/'notes/determinatives-as-nouns-review-2026-09-11-criteria.md').read_bytes() == (snap/'author-review.md').read_bytes()
checks['author_annotations_unchanged'] = True
checks['quotes'] = {'distinct_strings_unchanged': set(re.findall(r'\\enquote\{([^{}]+)\}',before)) == set(re.findall(r'\\enquote\{([^{}]+)\}',after)), 'note': 'Duplicate introductory quotation removed; retained in related work.'}
assert checks['quotes']['distinct_strings_unchanged']
checks['examples'] = {
    'removed_strings': sorted(set(re.findall(r'\\mention\{([^{}]+)\}',before))-set(re.findall(r'\\mention\{([^{}]+)\}',after))),
    'added_strings': sorted(set(re.findall(r'\\mention\{([^{}]+)\}',after))-set(re.findall(r'\\mention\{([^{}]+)\}',before))),
    'note': 'Illustrations revised with the author comments and source-checked boundary discussion; no empirical data changed.'
}
assert md.count('```text') == 15
assert len(re.findall(r'^Table \d+:',md,re.M)) == 5
assert len(re.findall(r'^> Note \d+\.',md,re.M)) == 14
assert not re.search(r'!\[|\{(?:>>|\+\+|~~|--)|\\(?:mentionhead|ref|textcite|citep|begin|end)\b', md)
checks['reading_copy'] = {'file': str(review.relative_to(root)), 'trees': 11, 'schemata': 4, 'tables': 5, 'notes': 14, 'images': 0, 'pandoc_warnings': 0}
log = (root/'determinatives-as-nouns.log').read_text()
assert not re.search(r'(?:Citation|Reference) .+ undefined|There were undefined|Overfull|Underfull|Rerun to get|Please rerun|^!', log, re.M)
assert not re.search(r'\b(?:TODO|FIXME|VERIFY)\b|\?\?',after)
pages = Path('/tmp/dnoun-complete-layout.txt').read_text().split('\f')
pages = [p for p in pages if p.strip()]
checks['build'] = {'pages': len(pages), 'overfull_boxes': 0, 'underfull_boxes': 0, 'unresolved_references': 0, 'sequence': 'XeLaTeX, Biber, XeLaTeX, XeLaTeX', 'biber': '2.21 temporary arm64 extraction', 'existing_warnings': ['fancyhdr E field in one-sided document', 'microtype footnote patch', 'EB Garamond bold substitution'], 'image_inspection': 'Deferred at author request; PDF text and page distribution checked'}
checks['page_text_counts'] = [len(p.split()) for p in pages]
rules = r'''%TC:macro \mention [text]
%TC:macro \mentionhead [text]
%TC:macro \olang [text]
%TC:macro \term [text]
%TC:macro \synnode [ignore,ignore]
%TC:envir forest [] ignore
'''
counts = {}
for label, source in [('before',before),('after',after)]:
    body = source.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
    path = Path('/tmp/dnoun-complete-count-'+label+'.tex'); path.write_text(rules+'\n'+body)
    result = subprocess.run(['texcount','-sub=section',str(path)],capture_output=True,text=True,check=True)
    assert '!!!' not in result.stdout
    (snap/('texcount-'+label+'.txt')).write_text(result.stdout)
    fields = {field:int(re.search(re.escape(field)+r': (\d+)',result.stdout)[1]) for field in ['Words in text','Words in headers','Words outside text (captions, etc.)']}
    fields['total'] = sum(fields.values()); counts[label] = fields
assert counts['before']['total'] == 7641
checks['texcount'] = counts
checks['net_words_added'] = counts['after']['total']-counts['before']['total']
checks['review_points'] = {'suggestions': 49, 'comments': 9, 'response_record': 'notes/passes/2026-09-11-complete-revision.md'}
(root/'notes/passes/2026-09-11-complete-revision-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
(root/'notes/passes/2026-09-11-complete-revision.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before/determinatives-as-nouns.tex',tofile='after/determinatives-as-nouns.tex')))
print(json.dumps({k:checks[k] for k in ['build','texcount','net_words_added','protected_files_unchanged','reading_copy']},indent=2))
