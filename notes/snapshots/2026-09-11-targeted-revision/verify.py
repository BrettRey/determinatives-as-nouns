from pathlib import Path
import re,json,hashlib,subprocess,difflib
root=Path.cwd(); snap=root/'notes/snapshots/2026-09-11-targeted-revision'
before=(snap/'determinatives-as-nouns.tex').read_text(); after=(root/'determinatives-as-nouns.tex').read_text()
md=(root/'notes/determinatives-as-nouns-review-2026-09-11-targeted.md').read_text()
checks={}
for label,pattern,expected in [('trees',r'\\begin\{forest\}.*?\\end\{forest\}',11),('schemata',r'\\\[.*?\\\]',4),('tables',r'\\begin\{table\}.*?\\end\{table\}',5),('numbered_examples',r'\\ea\\label\{.*?\\z(?:\\z)?',2)]:
    old=re.findall(pattern,before,re.S); new=re.findall(pattern,after,re.S)
    assert len(new)==expected and old==new,label
    checks[label]={'count':expected,'unchanged':True}
def keys(text):
    return set(k.strip() for match in re.finditer(r'\\(?:cite[a-z]*|textcite)(?:\[[^\]]*\])*\{([^}]+)\}',text) for k in match[1].split(','))
assert keys(before)==keys(after)
checks['citation_keys_unchanged']=len(keys(after))
bbl=(root/'determinatives-as-nouns.bbl').read_text()
checks['unresolved_bibliography_keys']=sorted(keys(after)-set(re.findall(r'\\entry\{([^}]+)\}',bbl)))
assert not checks['unresolved_bibliography_keys']
oldforms=set(re.findall(r'\\mention\{([^{}]+)\}',before));newforms=set(re.findall(r'\\mention\{([^{}]+)\}',after))
checks['removed_example_strings']=sorted(oldforms-newforms);checks['added_example_strings']=sorted(newforms-oldforms)
assert checks['removed_example_strings']==sorted(['-hood','bachelorhood','falsehood','likelihood','-dom','kingdom','officialdom','freedom','wisdom','Friendship'])
assert checks['added_example_strings']==['little','so many mistakes','so numerous mistakes']
checks['example_note']='The -hood/-dom catalogue is removed; Friendship is now lowercase friendship, already present in the table. The newly separate mention little is an existing member of the inventory.'
assert re.findall(r'\\enquote\{[^{}]+\}',before)==re.findall(r'\\enquote\{[^{}]+\}',after)
checks['direct_quotations_unchanged']=True
protected=json.loads((snap/'protected-sha256.json').read_text())
changed=[name for name,digest in protected.items() if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest]
assert not changed,changed
checks['protected_files_unchanged']=len(protected)
assert md.count('```text')==15 and not re.search(r'!\[|\{(?:>>|\+\+|~~|--)',md)
assert all(phrase in md for phrase in ['so many mistakes','specific to NP structure','identifying anchor','independent genitives'])
assert len(re.findall(r'^> Note \d+\.',md,re.M))==13
checks['reading_copy']={'text_trees':11,'text_schemata':4,'tables':len(re.findall(r'^Table \d+:',md,re.M)),'notes':13,'images':0}
log=(root/'determinatives-as-nouns.log').read_text()
assert not re.search(r'(?:Citation|Reference) .+ undefined|There were undefined|Overfull|Rerun to get|Please rerun|^!',log,re.M)
pages=Path('/tmp/determinatives-targeted-20260911.txt').read_text().split('\f')
if not pages[-1].strip(): pages.pop()
assert len(pages)==24
checks['build']={'pages':len(pages),'overfull_boxes':0,'unresolved_references':0,'image_inspection':'deferred at author request','biber':'2.21, temporary arm64 extraction of installed universal binary'}
checks['page_text_counts']=[len(p.split()) for p in pages]
rules=r'''%TC:macro \mention [text]
%TC:macro \olang [text]
%TC:macro \term [text]
%TC:macro \synnode [ignore,ignore]
%TC:envir forest [] ignore
'''
counts={}
for label,text in [('before',before),('after',after)]:
    body=text.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
    path=Path('/tmp/determinatives-targeted-count-'+label+'.tex');path.write_text(rules+'\n'+body)
    result=subprocess.run(['texcount','-sub=section',str(path)],text=True,capture_output=True,check=True)
    assert '!!!' not in result.stdout
    fields={field:int(re.search(re.escape(field)+r': (\d+)',result.stdout)[1]) for field in ['Words in text','Words in headers','Words outside text (captions, etc.)']}
    fields['total']=sum(fields.values());counts[label]=fields
checks['texcount']=counts
assert counts['before']['total']==7356
checks['net_words_added']=counts['after']['total']-counts['before']['total']
(root/'notes/passes/2026-09-11-targeted-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
(root/'notes/passes/2026-09-11-targeted-revision.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before/determinatives-as-nouns.tex',tofile='after/determinatives-as-nouns.tex')))
print(json.dumps({'pages':len(pages),'word_counts':counts,'net_words_added':checks['net_words_added'],'protected':len(protected)},indent=2))
