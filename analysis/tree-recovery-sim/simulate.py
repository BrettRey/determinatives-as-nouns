#!/usr/bin/env python3
"""Fake-data check of the planned tests (24 Oct 2026; codebook section 9).

Question: can the tests tell the rival trees apart, and at what noun count?
A side agent noted that leaving out one form at a time can't, since the rivals
differ only above the subcategory level. This generates binary cells under each
tree, runs leave-one-form-out and leave-one-group-out, and counts how often each
test picks the tree that generated the data (Gelman et al. 2020, Bayesian
workflow §4.1: recover known structure from fake data before trusting the fit).

Trees (leaves: C common noun, P proper noun, R pronoun, D determinative, A adjective):
  coordinate (Brett):  root{ Noun{C, P, R, D}, A }
  nested (Hudson):     root{ Noun{C, P, Pron{R, D}}, A }
  separate (CGEL):     root{ Noun{C, P, R}, D, A }
Generator, per column c: logit p = a_c + (sum of node effects on the leaf's path)
+ v_fc. a_c ~ N(mu, s_a); in a share pi of columns each node below the root gets
N(0, tau) (else 0); v_fc ~ N(0, sigma) is form-level variation. The four
parameters are calibrated so that pronoun and determinative cells match the
2021 matrix on four summaries (calibrate()).
Estimators are deliberately simple (beta-smoothed rates; a parent node's rate
is the mean of its children's, each child one unit, so copies of a form can't
add weight). Scores are mean log-likelihood per held-out form.

Usage: python3 analysis/tree-recovery-sim/simulate.py  (writes results.csv and RESULTS.md here)
"""
import csv
import itertools
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TREES = {
    "coordinate": {"root": ["Noun", "A"], "Noun": ["C", "P", "R", "D"]},
    "nested": {"root": ["Noun", "A"], "Noun": ["C", "P", "Pron"], "Pron": ["R", "D"]},
    "separate": {"root": ["Noun", "D", "A"], "Noun": ["C", "P", "R"]},
}
LEAVES = ["C", "P", "R", "D", "A"]
SEED = 20261024


def path(tree, leaf):
    """Nodes from just below the root down to the leaf."""
    parent = {ch: n for n, chs in tree.items() for ch in chs}
    out, x = [], leaf
    while x != "root":
        out.append(x)
        x = parent[x]
    return out[::-1]


def generate(rng, tree, sizes, ncol, mu, s_a, tau, sigma, pi):
    nodes = sorted({n for n in tree if n != "root"} | set(LEAVES))
    a = rng.normal(mu, s_a, ncol)
    inf = rng.random(ncol) < pi
    eff = {n: rng.normal(0, tau, ncol) * inf for n in nodes}
    data = {}
    for leaf in LEAVES:
        eta = a + sum(eff[n] for n in path(tree, leaf))
        v = rng.normal(0, sigma, (sizes[leaf], ncol))
        data[leaf] = (rng.random((sizes[leaf], ncol)) < 1 / (1 + np.exp(-(eta + v)))).astype(float)
    return data


def rate(x):
    """Beta(0.5, 0.5)-smoothed rate per column over the rows of x."""
    return (x.sum(0) + 0.5) / (x.shape[0] + 1)


def node_rate(tree, node, data, exclude=None):
    """A node's rate per column: the mean of its children's, each child one unit."""
    if node in LEAVES:
        return None if node == exclude else rate(data[node])
    parts = [node_rate(tree, ch, data, exclude) for ch in tree[node]]
    parts = [p for p in parts if p is not None]
    return np.mean(parts, axis=0) if parts else None


def ll(x, p):
    p = np.clip(p, 0.01, 0.99)
    return (x * np.log(p) + (1 - x) * np.log(1 - p)).mean()


def logo(tree, data):
    """Leave one group out: predict each leaf from its nearest ancestor with other data."""
    parent = {ch: n for n, chs in tree.items() for ch in chs}
    score = 0.0
    for leaf in LEAVES:
        node, p = parent[leaf], None
        while p is None:
            p = node_rate(tree, node, data, exclude=leaf)
            node = parent.get(node, "root") if p is None else node
        score += ll(data[leaf], p)
    return score / len(LEAVES)


def tree_cov(tree):
    """Shared-path matrix: K[i, j] is the number of nodes below the root on both leaves' paths."""
    P = {l: set(path(tree, l)) for l in LEAVES}
    return np.array([[len(P[a] & P[b]) for b in LEAVES] for a in LEAVES], dtype=float)


def logo_gls(tree, data, taus=np.exp(np.linspace(np.log(0.05), np.log(10), 30))):
    """Leave one group out, model-based. Per column, the leaf logits are
    N(a_c, tau^2 K + S_c), K the tree's shared-path matrix and S_c the sampling
    variances; tau is estimated on the remaining leaves (profiling a_c out),
    and the held-out leaf is predicted by its conditional mean and variance."""
    K = tree_cov(tree)
    n = np.array([data[l].shape[0] for l in LEAVES])
    r = np.array([rate(data[l]) for l in LEAVES])                       # 5 x ncol
    x = np.log(r / (1 - r))
    S = 1 / ((n[:, None] + 1) * r * (1 - r))
    score = 0.0
    for i, leaf in enumerate(LEAVES):
        keep = [j for j in range(len(LEAVES)) if j != i]
        Kk, xk, Sk = K[np.ix_(keep, keep)], x[keep].T, S[keep].T       # ncol x (leaves - 1)
        one = np.ones(len(keep))

        def fit(t):
            V = t ** 2 * Kk[None] + Sk[:, :, None] * np.eye(len(keep))[None]
            Vi = np.linalg.inv(V)
            w = Vi @ one
            a = (w * xk).sum(1) / (w @ one)
            e = xk - a[:, None]
            q = np.einsum("ci,cij,cj->c", e, Vi, e)
            return -0.5 * (q + np.linalg.slogdet(V)[1]).sum(), Vi, a
        t = max(taus, key=lambda t: fit(t)[0])
        _, Vi, a = fit(t)
        k = t ** 2 * K[i, keep]
        mu = a + np.einsum("j,cjk,ck->c", k, Vi, xk - a[:, None])
        var = np.maximum(t ** 2 * K[i, i] - np.einsum("j,cjk,k->c", k, Vi, k), 0)
        pred = 1 / (1 + np.exp(-mu / np.sqrt(1 + np.pi * var / 8)))
        score += ll(data[leaf], pred)
    return score / len(LEAVES)


def loo_form(tree, data, alpha=2.0):
    """Leave one form out: its leaf's rate without it, shrunk toward the leaf's parent."""
    parent = {ch: n for n, chs in tree.items() for ch in chs}
    score = 0.0
    for leaf in LEAVES:
        x = data[leaf]
        prior = node_rate(tree, parent[leaf], data, exclude=leaf)
        if prior is None:
            prior = rate(x)
        tot = x.sum(0)
        s = 0.0
        for i in range(x.shape[0]):
            p = (tot - x[i] + alpha * prior) / (x.shape[0] - 1 + alpha)
            s += ll(x[i], p)
        score += s / x.shape[0]
    return score / len(LEAVES)


def summaries(data):
    r, d = data["R"].mean(0), data["D"].mean(0)
    return np.array([np.abs(r - d).mean(), (np.abs(r - d) > 0.3).mean(),
                     (r * (1 - r)).mean(), ((r == 0) | (r == 1)).mean()])


def observed():
    m = list(csv.reader((ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv").open()))
    h = m[0]
    cat = {r["form"]: r["category"] for r in csv.DictReader((ROOT / "analysis" / "codebook" / "forms.csv").open())}
    types = {r["column"]: r["type"] for r in csv.DictReader((ROOT / "analysis" / "codebook" / "columns.csv").open())}
    use = [i for i, c in enumerate(h) if types.get(c) in ("possibility", "universal", "superseded")]
    val = lambda rows: np.array([[1.0 if r[i] in ("y", "m", "marginal") else 0.0 for i in use] for r in rows])
    R = val([r for r in m[1:] if cat.get(r[0]) == "pronoun"])
    D = val([r for r in m[1:] if cat.get(r[0]) == "determinative"])
    return summaries({"R": R, "D": D}), len(use), R.shape[0], D.shape[0], R.mean()


def calibrate(rng, target, ncol, nR, nD, ybar):
    mu = np.log(ybar / (1 - ybar))
    best = None
    for s_a, tau, sigma, pi in itertools.product([1.5, 2.5, 3.5], [0.5, 1.0, 1.5, 2.0], [0.5, 1.0, 1.5, 2.5], [0.3, 0.6, 1.0]):
        stats = np.mean([summaries(generate(rng, TREES["coordinate"], {"C": 1, "P": 1, "R": nR, "D": nD, "A": 1},
                                            ncol, mu, s_a, tau, sigma, pi)) for _ in range(6)], axis=0)
        dist = float(((stats - target) / np.maximum(target, 0.05)) ** 2 @ np.ones(4))
        if best is None or dist < best[0]:
            best = (dist, (mu, s_a, tau, sigma, pi), stats)
    return best


def main():
    rng = np.random.default_rng(SEED)
    target, ncol_obs, nR, nD, ybar = observed()
    dist, params, stats = calibrate(rng, target, ncol_obs, nR, nD, ybar)
    mu, s_a, tau, sigma, pi = params
    rows = []
    scenarios = [("now: 12 nouns, 2 proper nouns, 6 adjectives", {"C": 12, "P": 2, "A": 6}),
                 ("planned: 40 nouns, 12 proper nouns, 12 adjectives", {"C": 40, "P": 12, "A": 12}),
                 ("large: 100 nouns, 24 proper nouns, 24 adjectives", {"C": 100, "P": 24, "A": 24}),
                 ("12 nouns, 12 proper nouns, 12 adjectives", {"C": 12, "P": 12, "A": 12}),
                 ("40 nouns, 2 proper nouns, 6 adjectives", {"C": 40, "P": 2, "A": 6}),
                 ("40 nouns, 24 proper nouns, 24 adjectives", {"C": 40, "P": 24, "A": 24})]
    NSIM = 40
    for ncol in (ncol_obs, 140):
        for label, extra in scenarios:
            sizes = {"R": nR, "D": nD, **extra}
            for true in TREES:
                win = {"logo": 0, "gls": 0, "loo": 0}
                margin = {"logo": [], "gls": [], "loo": []}
                for _ in range(NSIM):
                    data = generate(rng, TREES[true], sizes, ncol, mu, s_a, tau, sigma, pi)
                    for test, fn in (("logo", logo), ("gls", logo_gls), ("loo", loo_form)):
                        sc = {t: fn(TREES[t], data) for t in TREES}
                        ranked = sorted(sc, key=sc.get, reverse=True)
                        win[test] += ranked[0] == true
                        margin[test].append(sc[true] - max(v for t, v in sc.items() if t != true))
                rows.append({"columns": ncol, "sample": label, "true_tree": true,
                             "gls_recovery": win["gls"] / NSIM, "naive_group_recovery": win["logo"] / NSIM,
                             "form_out_recovery": win["loo"] / NSIM, "gls_margin": float(np.mean(margin["gls"])),
                             "naive_group_margin": float(np.mean(margin["logo"])), "form_out_margin": float(np.mean(margin["loo"]))})
    with (HERE / "results.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    L = ["# Tree-recovery simulation: results", "",
         "<!-- SUMMARY: fake-data check of whether leave-one-form-out and leave-one-group-out tell the rival trees apart, by noun and column count · status: for Brett · updated: 2026-10-24 -->", "",
         f"Generated by `simulate.py` (seed {SEED}, {NSIM} simulated datasets per row). Calibrated to the 2021 matrix's pronoun and determinative cells ({ncol_obs} columns, {nR} pronoun and {nD} determinative forms): "
         f"target summaries {np.round(target, 3).tolist()}, simulated {np.round(stats, 3).tolist()} "
         "(mean |pronoun rate - determinative rate|, share of columns where they differ by more than 0.3, mean within-group variance, share of columns constant among pronouns). "
         f"Parameters: mu {mu:.2f}, s_a {s_a}, tau {tau}, sigma {sigma}, pi {pi}.", "",
         "Recovery is the share of datasets in which a test scores the generating tree highest (chance is a third). Margin is the true tree's score minus the best rival's, in mean log-likelihood per cell (positive is right). Three tests: group out, model-based (the held-out group predicted from the others through the tree's covariance, with the between-node spread estimated from the data); group out, naive (predicted from the plain mean of its siblings; biased toward trees that give a group more siblings); and form out.", "",
         "| columns | sample | true tree | group out, model-based | group out, naive | form out | margin, model-based |", "|---|---|---|---|---|---|---|"]
    L += [f"| {r['columns']} | {r['sample']} | {r['true_tree']} | {r['gls_recovery']:.2f} | {r['naive_group_recovery']:.2f} | {r['form_out_recovery']:.2f} | {r['gls_margin']:.4f} |" for r in rows]
    (HERE / "RESULTS.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[4:]))


if __name__ == "__main__":
    main()
