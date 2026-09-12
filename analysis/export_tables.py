#!/usr/bin/env python3
"""Export manuscript tables directly from the audited result files."""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'generated'
OUT.mkdir(exist_ok=True)


def read(name):
    return list(csv.DictReader((ROOT/'results'/name).open()))


def main():
    fits = {r['variant']: r for r in read('kgroups-summary.csv')}
    disco = {r['variant']: r for r in read('disco-sensitivity.csv')}
    selected = [('public155', 'Public matrix'),
                ('no_word_component_columns', 'Without word-component columns'),
                ('syntax50', 'Syntactic columns'),
                ('syntax_without_four_analysis_labels', 'Syntactic, four labels removed')]
    lines = []
    for key, label in selected:
        r, d = fits[key], disco[key]
        lines.append(f"{label} & {r['features']} & {float(d['F']):.3f} & "
                     f"{r['single_start_min']}--{r['single_start_max']} & "
                     f"{r['best_of_100_matched']}/138 \\\\")
    (OUT/'matrix-table.tex').write_text('\n'.join(lines)+'\n')
    rows = read('corpus-concordance.csv')
    # Displayed forms come from the manuscript's motivating comparisons.
    # Complete lemma/function counts remain available in the CSV.
    forms = ['the', 'a', 'every', 'this', 'that', 'some', 'all', 'both', 'many',
             'a few', 'each', 'enough']
    lines = []
    for form in forms:
        counts = Counter(r['local_function'] for r in rows if r['lemma']==form)
        total = sum(counts.values())
        other = total-counts['Det']-counts['Det-Head']
        lines.append(f"\\mention{{{form}}} & {total} & {counts['Det']} & "
                     f"{counts['Det-Head']} & {other} \\\\")
    (OUT/'corpus-table.tex').write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    main()
