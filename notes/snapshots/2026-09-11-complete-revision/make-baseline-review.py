from pathlib import Path
import re, subprocess, json

base = Path.cwd()
source = (base / 'determinatives-as-nouns.tex').read_text()
aux = (base / 'determinatives-as-nouns.aux').read_text()
labels = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}', aux))
old_review = (base / 'notes/determinatives-as-nouns-review-2026-09-11-targeted.md').read_text()
baseline = (base / 'notes/snapshots/2026-09-11-method-criteria/determinatives-as-nouns.tex').read_text()
assert re.findall(r'\\\[.*?\\\]', source, re.S) == re.findall(r'\\\[.*?\\\]', baseline, re.S)

def argument(s, pos):
    assert s[pos] == '{', (pos, s[pos:pos+100])
    start = pos + 1
    depth = 1
    pos += 1
    while depth:
        if s[pos] == '{': depth += 1
        elif s[pos] == '}': depth -= 1
        pos += 1
    return s[start:pos-1], pos

def plain(s):
    s = s.strip()
    s = re.sub(r',\s*head edge', '', s)
    s = re.sub(r',\s*(?:name=\w+|no edge|before drawing tree=\{[^}]+\})', '', s)
    if s.startswith('{'):
        content, end = argument(s, 0)
        if end == len(s): s = content
    if s.startswith(r'\synnode'):
        function, pos = argument(s, len(r'\synnode'))
        category, pos = argument(s, pos)
        return plain(function) + ': ' + plain(category)
    s = re.sub(r'\\textsubscript\{([^}]+)\}', r'_\1', s)
    s = re.sub(r'\\(?:mention|textit|textsc|term)\{([^}]+)\}', r'\1', s)
    s = re.sub(r',\s*roof\s*$', '', s)
    return s.replace('--', '–').replace('~', ' ')

def parse_tree(s):
    s = re.sub(r'\s*\{\\draw[^}]+\}', '', s)
    pos = s.index('[')
    def node():
        nonlocal pos
        assert s[pos] == '['
        pos += 1; start = pos; braces = 0
        while pos < len(s):
            c = s[pos]
            if c == '{': braces += 1
            elif c == '}': braces -= 1
            elif c in '[]' and braces == 0: break
            pos += 1
        label = plain(s[start:pos].strip())
        children = []
        while True:
            while s[pos].isspace(): pos += 1
            if s[pos] == ']': pos += 1; break
            children.append(node())
        return label, children
    result = node()
    assert not s[pos:].strip(), s[pos:]
    return result

def tree_text(tree):
    out = [tree[0]]
    def walk(children, prefix):
        for n, (label, children2) in enumerate(children):
            last = n == len(children)-1
            out.append(prefix + ('└── ' if last else '├── ') + label)
            walk(children2, prefix + ('    ' if last else '│   '))
    walk(tree[1], '')
    return '\n'.join(out)

body = source.split(r'\begin{document}', 1)[1].split(r'\end{document}', 1)[0]
body = body.replace(r'\maketitle', '').replace(r'\begin{abstract}', r'\section*{Abstract}').replace(r'\end{abstract}', '')
body = re.sub(r'(?m)^%.*\n', '', body)
body = re.sub(r'\\tablebody\{([^}]+)\}', lambda m: (base/m[1]).read_text(), body)
replacements = {}
tree_count = 0

def figure(m):
    global tree_count
    block = m[0]
    label = re.search(r'\\label\{([^}]+)\}', block)[1]
    number = labels[label]
    caption, _ = argument(block, block.index(r'\caption{') + len(r'\caption'))
    caption = caption.replace('(left)', '(first tree)').replace('(right)', '(second tree)')
    caption = caption.replace('on the left', 'in the first tree').replace('on the right', 'in the second tree')
    trees = re.findall(r'\\begin\{forest\}(.*?)\\end\{forest\}', block, re.S)
    tree_count += len(trees)
    token = f'REVIEWFIGURE{number}TOKEN'
    rendered = []
    tree_labels = ['CGEL: take some apples', 'CGEL: take some', 'D-noun analysis: take some apples', 'D-noun analysis: take some']
    for i, t in enumerate(trees):
        diagram = tree_text(parse_tree(t))
        if r'\draw' in t:
            rows = diagram.splitlines()
            dst = next(j for j, row in enumerate(rows) if 'Det–Head: DP' in row or 'Mod–Head: DP' in row)
            def depth(row):
                return (row.index('── ')-1)//4+1 if '── ' in row else 0
            src = next(j for j in range(dst-1,-1,-1) if depth(rows[j]) == depth(rows[dst])-2)
            col = max(len(row) for row in rows[src:dst+1]) + 5
            rows[src] += ' ' + '─'*(col-len(rows[src])-1) + '┐'
            for j in range(src+1, dst): rows[j] = rows[j].ljust(col) + '│'
            rows[dst] += ' ◄' + '─'*(col-len(rows[dst])-2) + '┘'
            diagram = '\n'.join(rows)
        lead = tree_labels[i]+'\n\n' if label == 'fig:some' else ''
        rendered.append(lead+'```text\n'+diagram+'\n```')
    replacements[token] = '\n\n'.join(rendered)
    if label == 'fig:some':
        caption = r'The first pair shows \textit{CGEL}; the second pair shows the D-noun analysis. Each pair compares \mention{take some apples} with \mention{take some}. In the second tree, DP fills Det of NP and Head of Nom. In the third and fourth trees, \mention{some} heads an NP through the same N\textsubscript{D}--Nom--NP sequence; that NP functions as Det in the third tree and Obj in the fourth.'
    return f'\n\n{token}\n\nFigure {number}: {caption}\n\n'

body = re.sub(r'\\begin\{figure\}.*?\\end\{figure\}', figure, body, flags=re.S)
math_blocks = [m for m in re.findall(r'```text\n(.*?)\n```', old_review, re.S) if m.startswith(('CGEL:', 'Nom_h', 'DP_h'))]
assert len(math_blocks) == 4
math_count = 0
def display(m):
    global math_count
    token = f'REVIEWSCHEMA{math_count}TOKEN'
    replacements[token] = '```text\n' + math_blocks[math_count] + '\n```'
    math_count += 1
    return '\n\n' + token + '\n\n'
body = re.sub(r'\\\[.*?\\\]', display, body, flags=re.S)
assert math_count == 4

def example(m):
    label, block = m[1], m[2]
    lines = re.split(r'\\ex\s+', block.strip())
    return '\n\n' + '\n\n'.join(f'({labels[label]}{chr(97+i)}) ' + line.strip().replace(r'\qquad', r'\quad --- \quad') for i, line in enumerate(lines)) + '\n\n'
body = re.sub(r'\\ea\\label\{([^}]+)\}\s*\\ea\s*(.*?)\\z\\z', example, body, flags=re.S)
body = re.sub(r'\\ea\\label\{([^}]+)\}\s*(.*?)\\z', lambda m: '\n\n(' + labels[m[1]] + ') ' + m[2].strip() + '\n\n', body, flags=re.S)
body = re.sub(r'\\ref\{([^}]+)\}', lambda m: labels[m[1]], body)
table_count = 0
def table(m):
    global table_count
    block = m[0]
    label = re.search(r'\\label\{([^}]+)\}', block)[1]
    table_count += 1
    return block.replace(r'\caption{', r'\caption{Table ' + labels[label] + ': ', 1)
body = re.sub(r'\\begin\{table\}.*?\\end\{table\}', table, body, flags=re.S)
section = 0; subsection = 0; appendix = False; lines = []
for line in body.splitlines():
    if line.strip() == r'\appendix':
        appendix = True; subsection = 0; continue
    if line.startswith(r'\section{'):
        section += 1; subsection = 0
        prefix = 'A' if appendix else str(section)
        line = line.replace(r'\section{', r'\section{' + prefix + ' ', 1)
    elif line.startswith(r'\subsection{'):
        subsection += 1; prefix = 'A' if appendix else str(section)
        line = line.replace(r'\subsection{', r'\subsection{' + prefix + '.' + str(subsection) + ' ', 1)
    lines.append(line)
body = '\n'.join(lines)
body = re.sub(r'\\label\{[^}]+\}', '', body)
body = body.replace(r'\printbibliography', '').replace(r'\clearpage', '')
body = body.replace(r'$\phi$', 'φ')
body = body.replace(r'$\{\mathrm{N},\mathrm{D}\}$', r'\texttt{\{N, D\}}')
body = re.sub(r'\$([^$]+)\$', lambda m: r'\texttt{' + m[1].replace('_', r'\_') + '}', body)
macros = r'''\newcommand{\mention}[1]{\textit{#1}}
\newcommand{\term}[1]{#1}
\newcommand{\ungram}[1]{*#1}
\newcommand{\olang}[1]{\textit{#1}}
\newcommand{\nolinkurl}[1]{\texttt{#1}}
\newcommand{\textsubscript}[1]{\texttt{\_#1}}
'''
temp = Path('/tmp/determinatives-text-review.tex')
temp.write_text(macros + '\n' + body)
result = subprocess.run(['pandoc', str(temp), '-f', 'latex', '-t', 'gfm', '--wrap=none', '--citeproc', '--bibliography', str(base/'references.bib'), '--bibliography', str(base/'references-local.bib'), '-M', 'reference-section-title=References'], check=True, text=True, capture_output=True)
md = result.stdout
for token, value in replacements.items():
    assert md.count(token) == 1
    md = md.replace(token, value)
md = re.sub(r'<span class="smallcaps">(.*?)</span>', lambda m: m[1], md)
md = re.sub(r'<span id="[^\"]+"[^>]*></span>', '', md)
md = re.sub(r'</?div\b[^>]*>', '', md)
md = re.sub(r' \{#tab:[^}]+\}', '', md)
md = re.sub(r'(?m)^: Table ', 'Table ', md)
md = re.sub(r'(N(?:P)?)`(_(?:D|common|proper))`', r'`\1\2`', md)
md = re.sub(r'(?m)(\|[^\n]+\n(?:\|[^\n]+\n)+)\n(Table [^\n]+)', r'\2\n\n\1', md)
md = md.replace('*— ', '* — ')
footnotes = dict(re.findall(r'(?m)^\[\^(\d+)\]: (.*)$', md))
md = re.sub(r'(?m)^\[\^\d+\]: .*\n?', '', md)
for number, note in footnotes.items():
    marker = '[^'+number+']'
    assert md.count(marker) == 1
    pos = md.index(marker)
    end = md.index('\n\n', pos)
    md = md[:end] + '\n\n> Note '+number+'. '+note + md[end:]
    md = md.replace(marker, '')
md = re.sub(r'(?m)^(#{1,3} [^\n]+)\n(?!\n)', r'\1\n\n', md)
md = re.sub(r'\n{3,}', '\n\n', md)
header = '# Determinatives as nouns in English\n\nBrett Reynolds — 11 September 2026 working draft\n\nRevised with explicit comparison criteria and the qualified harmony argument. Trees and schemata are shown as text; footnotes appear beside their paragraphs. [Typeset PDF](../determinatives-as-nouns.pdf).\n\n'
out = base/'notes/snapshots/2026-09-11-complete-revision/baseline-review.md'
md = md.replace('(*CGEL*; Huddleston and Pullum (2002))', '(*CGEL*; Huddleston and Pullum 2002)').replace('((Abney 1987); §2.1)', '(Abney 1987; §2.1)').replace('\u00ad', '')
md = md.replace('f∈ U_h\\ ∧\\ C_h(f,c)', 'f ∈ U_h ∧ C_h(f,c)')
if out.exists():
    assert not re.search(r'\{(?:>>|\+\+|~~|--)', out.read_text()), 'Preserve reviewed copy'
out.write_text(header + md)
assert tree_count == 11 and table_count == 5
print(json.dumps({'file':str(out), 'trees':tree_count, 'tables':table_count, 'schemata':math_count, 'pandoc_warnings':result.stderr}, indent=2))
