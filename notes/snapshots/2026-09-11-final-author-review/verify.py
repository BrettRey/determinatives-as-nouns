from pathlib import Path
import re, json, hashlib, subprocess, difflib

root = Path.cwd()
snap = root / 'notes/snapshots/2026-09-11-final-author-review'
before = (snap / 'determinatives-as-nouns.tex').read_text()
after = (root / 'determinatives-as-nouns.tex').read_text()
review = root / 'notes/determinatives-as-nouns-review-2026-09-11-final-author.md'
md = review.read_text()
checks = {'source_sha256': hashlib.sha256(after.encode()).hexdigest()}

old_trees = re.findall(r'\\begin\{forest\}.*?\\end\{forest\}', before, re.S)
new_trees = re.findall(r'\\begin\{forest\}.*?\\end\{forest\}', after, re.S)
assert len(new_trees) == 11 and old_trees == new_trees
checks['trees'] = {'count': 11, 'tex_unchanged': True, 'markdown': 'Unary branches rendered vertically; fusion links retained'}

old_schemata = re.findall(r'\\\[.*?\\\]', before, re.S)
new_schemata = re.findall(r'\\\[.*?\\\]', after, re.S)
assert len(new_schemata) == 4
expected = [x.replace(r'\mathrm{NP}_{h} &\to (\mathrm{Det})', r'\mathrm{NP}_{h} &\to (\mathrm{Mod}_{\mathrm{periph}})\quad (\mathrm{Det})') for x in old_schemata]
assert expected == new_schemata
checks['schemata'] = {'count': 4, 'change': 'Author s50: optional peripheral premodifier in NP schema; other schemata unchanged'}

def normalize_brackets(s):
    return s.replace(r'\textup{[}', '[').replace(r'\textup{]}', ']')
old_examples = re.findall(r'\\ea\\label\{.*?\\z(?:\\z)?', before, re.S)
new_examples = re.findall(r'\\ea\\label\{.*?\\z(?:\\z)?', after, re.S)
assert len(new_examples) == 2 and [normalize_brackets(x) for x in new_examples] == old_examples
checks['numbered_examples'] = {'count': 2, 'words_unchanged': True, 'format_change': 'Upright square brackets'}
assert len(re.findall(r'\\begin\{table\}', after)) == 5
checks['tables'] = {'count': 5, 'changes': 'Inventory-caption scope, dependent/independent labels, clearer restrictions and projection description'}

def keys(s):
    return {k.strip() for m in re.finditer(r'\\(?:cite[a-z]*|textcite)(?:\[[^\]]*\])*\{([^}]+)\}', s) for k in m[1].split(',')}
assert keys(before) == keys(after)
bbl = (root / 'determinatives-as-nouns.bbl').read_text()
assert keys(after) <= set(re.findall(r'\\entry\{([^}]+)\}', bbl))
checks['citations'] = {'unchanged_keys': sorted(keys(after)), 'unresolved': []}
assert (root / 'references.bib').is_symlink()
assert (root / 'references-local.bib').read_bytes() == (snap / 'references-local.bib').read_bytes()
protected = json.loads((root / 'notes/snapshots/2026-09-11-complete-revision/protected-sha256.json').read_text())
changed = [name for name, digest in protected.items() if hashlib.sha256((root/name).read_bytes()).hexdigest() != digest]
assert not changed, changed
checks['protected_files_unchanged'] = len(protected)
assert (root/'notes/determinatives-as-nouns-review-2026-09-11-complete.md').read_bytes() == (snap/'author-review.md').read_bytes()
checks['author_annotations_unchanged'] = True

assert md.count('```text') == 15
assert len(re.findall(r'^Table \d+:',md,re.M)) == 5
assert len(re.findall(r'^> Note \d+\.',md,re.M)) == 15
assert not re.search(r'!\[|\{(?:>>|\+\+|~~|--)|\\(?:mentionhead|ref|textcite|citep|begin|end)\b', md)
assert '`Mod_periph` adds' in md
assert 'NP_h → (Mod_periph) (Det)' in md
assert '`_`' not in md
assert not re.search(r'└── present', md)
checks['reading_copy'] = {'file': str(review.relative_to(root)), 'trees': 11, 'schemata': 4, 'tables': 5, 'notes': 15, 'images': 0, 'pandoc_warnings': 0}

log = (root/'determinatives-as-nouns.log').read_text()
assert not re.search(r'(?:Citation|Reference) .+ undefined|There were undefined|Overfull|Underfull|Rerun to get|Please rerun|^!', log, re.M)
assert not re.search(r'\b(?:TODO|FIXME|VERIFY)\b|\?\?',after)
prose_without_urls = re.sub(r'https?://[^}]+','',after)
assert not re.search(r'\b(?:class|classif\w*|reclassif\w*)\b',prose_without_urls,re.I)
pages = [p for p in Path('/tmp/dnoun-final-author-review-layout.txt').read_text().split('\f') if p.strip()]
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
    path = Path('/tmp/dnoun-final-author-count-'+label+'.tex'); path.write_text(rules+'\n'+body)
    result = subprocess.run(['texcount','-sub=section',str(path)],capture_output=True,text=True,check=True)
    assert '!!!' not in result.stdout
    (snap/('texcount-'+label+'.txt')).write_text(result.stdout)
    fields = {field:int(re.search(re.escape(field)+r': (\d+)',result.stdout)[1]) for field in ['Words in text','Words in headers','Words outside text (captions, etc.)']}
    fields['total'] = sum(fields.values()); counts[label] = fields
assert counts['before']['total'] == 9055
checks['texcount'] = counts
checks['net_words_added'] = counts['after']['total']-counts['before']['total']
markups = json.loads((snap/'author-markup.json').read_text())
checks['review_points'] = {'suggestions': sum(m['kind'] != '>>' for m in markups), 'comments': sum(m['kind'] == '>>' for m in markups), 'response_record': 'notes/passes/2026-09-11-final-author-review.md'}
response = (root / checks['review_points']['response_record']).read_text()
covered = set()
for row in response.splitlines():
    if not row.startswith('| '): continue
    field = row.split('|')[1]
    for match in re.finditer(r'([cs])(\d+)(?:–[cs]?(\d+))?', field):
        start, end = int(match[2]), int(match[3] or match[2])
        covered.update(match[1]+str(n) for n in range(start,end+1))
assert {m['id'] for m in markups} == covered
checks['review_points']['all_ids_addressed'] = True
(root/'notes/passes/2026-09-11-final-author-review-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
(root/'notes/passes/2026-09-11-final-author-review.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before/determinatives-as-nouns.tex',tofile='after/determinatives-as-nouns.tex')))
print(json.dumps({k:checks[k] for k in ['build','texcount','net_words_added','protected_files_unchanged','reading_copy','review_points']},indent=2))
