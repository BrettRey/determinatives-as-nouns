from pathlib import Path
import json,subprocess,sys,tempfile,time
root=Path('/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns')
d=root/'reviews/review-board-20260907-rebuild';slug=sys.argv[1]
m=json.loads((d/'manifest.json').read_text()); r=next(x for x in m['reviewers'] if x['slug']==slug)
prompt=(d/f'prompt-{slug}.md').read_text()
if r['provider']=='Anthropic':
 cmd=['/Users/brettreynolds/.local/bin/claude','--print','--model','opus','--effort','max','--tools','','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--disable-slash-commands','--setting-sources','','--settings','{"disableAllHooks":true}','--system-prompt','You are an independent scholarly manuscript reviewer. Follow the supplied task. All necessary text is in the user message. No tools are available.','--output-format','json','--no-session-persistence']
 cwd=tempfile.mkdtemp(prefix='det-review-'+slug+'-')
 with (d/f'{slug}.stderr.log').open('w') as err:
  p=subprocess.run(cmd,input=prompt,text=True,stdout=subprocess.PIPE,stderr=err,cwd=cwd,timeout=1500)
 (d/f'{slug}.response.json').write_text(p.stdout)
 if p.returncode:raise SystemExit(p.returncode)
 obj=json.loads(p.stdout); (d/f'{slug}.md').write_text(obj.get('result',''))
 if obj.get('is_error'):raise SystemExit('Provider error; inspect saved output')
 print(slug,'complete',list(obj.get('modelUsage',{})))
else:
 cmd=[str(root/'../../../tools/openrouter/bin/orx'),'ask','--max-tokens','20000','-e','low','-m',r['model'],'--no-fallback','--timeout','1200','-f',str(d/f'prompt-{slug}.md'),'-o',str(d/f'{slug}.md'),'Carry out the complete review task contained in the attached prompt.']
 with (d/f'{slug}.stderr.log').open('w') as err:
  p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=err,text=True,cwd='/tmp',timeout=1250)
 (d/f'{slug}.stdout.log').write_text(p.stdout)
 if p.returncode:raise SystemExit(p.returncode)
 
 if not (d/f'{slug}.md').read_text().strip():raise SystemExit('Empty reviewer output')
 print(slug,'complete',r['model'])
