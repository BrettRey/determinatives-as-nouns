#!/usr/bin/env python3
"""Inventory existing CGELBank annotations; no independent category validation.

Usage: python corpus_inventory.py /path/to/pinned/cgelbank
The first non-Head edge above a lexical D identifies its local function.
This avoids attributing an outer NP's Det-Head status to a D inside its
complement (for example the article in 'some of the books').
"""
import argparse
from collections import Counter
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
PIN = 'd0a2c2d8c522b23d5aa879fc9cb94948f4285b2c'
FILES = ['twitter.cgel', 'ewt.cgel', 'ewt-test_pilot5.cgel', 'ewt-test_iaa50.cgel']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('checkout', type=Path)
    args = parser.parse_args()
    repo = args.checkout.resolve()
    commit = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    assert commit == PIN, (commit, PIN)
    spec = importlib.util.spec_from_file_location('cgel', repo / 'cgel.py')
    cgel = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cgel)
    rows, denominators, files = [], [], []
    for name in FILES:
        path = repo / 'datasets' / name
        trees = lexical = dets = 0
        with path.open() as stream:
            for tree in cgel.trees(stream):
                trees += 1
                lexical += sum(bool(n.text) for n in tree.tokens.values())
                for index, node in tree.tokens.items():
                    if node.constituent != 'D' or not node.text:
                        continue
                    dets += 1
                    local = index
                    chain = [index]
                    while tree.tokens[local].deprel == 'Head' and tree.tokens[local].head in tree.tokens:
                        local = tree.tokens[local].head
                        chain.append(local)
                    anchor = tree.tokens[local]
                    parent = tree.tokens.get(anchor.head)
                    np_index = local
                    while np_index in tree.tokens and tree.tokens[np_index].constituent != 'NP':
                        np_index = tree.tokens[np_index].head
                    np_node = tree.tokens.get(np_index)
                    rows.append(dict(file=name, sent_id=tree.sentid, node=index,
                        form=node.text, lemma=(node.lemma or '[deleted]:'+node.text).lower(),
                        correction=node.correct if node.correct is not None else '[none]',
                        local_function=anchor.deprel or 'Root', local_category=anchor.constituent,
                        parent_category=parent.constituent if parent else '',
                        local_phrase=tree.node_yield(local),
                        parent_phrase=tree.node_yield(anchor.head) if parent else '',
                        nearest_np_function=np_node.deprel if np_node else '',
                        nearest_np=tree.node_yield(np_index) if np_node else '',
                        chain=' > '.join(f'{tree.tokens[j].deprel}:{tree.tokens[j].constituent}' for j in chain),
                        sentence=tree.text or tree.sent))
        denominators.append(dict(file=name, trees=trees, lexical_nodes=lexical, D_tokens=dets))
        files.append(dict(file='datasets/'+name, sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    out = ROOT / 'results'
    out.mkdir(exist_ok=True)
    def write(name, data):
        with (out/name).open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
    write('corpus-concordance.csv', rows)
    write('corpus-denominators.csv', denominators)
    counts = Counter((r['lemma'], r['local_function'], r['local_category']) for r in rows)
    write('corpus-by-lemma-function.csv', [dict(lemma=l, function=f, category=c, count=n)
          for (l, f, c), n in sorted(counts.items())])
    candidates = [r for r in rows if r['local_function']=='Det-Head']
    write('corpus-det-head-review.csv', candidates)
    manifest = dict(repository='https://github.com/nert-nlp/cgel', commit=commit,
        scope='Four top-level gold dataset files; trial, oneoff, and duplicate IAA files excluded.',
        inference_limit='Annotation inventory, not a random sample or independent test of CGEL categories.',
        files=files, totals={k:sum(r[k] for r in denominators) for k in ['trees','lexical_nodes','D_tokens']},
        functions=dict(Counter(r['local_function'] for r in rows)),
        det_head_lemmas=sorted({r['lemma'] for r in candidates}))
    (out/'corpus-manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    main()
