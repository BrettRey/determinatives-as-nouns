# Inclusive word count of a built PDF, as used for the fusion paper (Oct 2026):
# pdftotext -layout, drop the running head (first line of each page if it ends in
# the page number) and bare page-number lines, then count whitespace-separated
# tokens. Counts everything on the page, including references, footnotes, tables
# and figure labels, so it errs high against limits that include references.
# Usage: python3 tools/pdfwords.py paper.pdf
import subprocess,re,sys
pdf=sys.argv[1]
t=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout
n=0
for p in t.split('\f'):
    lines=[l for l in p.split('\n') if l.strip()]
    if lines and re.match(r'^\s*\d+\s+\S.*\s{3,}\d+\s*$',lines[0]): lines=lines[1:]
    lines=[l for l in lines if not re.fullmatch(r'\s*\d+\s*',l)]
    n+=sum(len(l.split()) for l in lines)
print(n)
