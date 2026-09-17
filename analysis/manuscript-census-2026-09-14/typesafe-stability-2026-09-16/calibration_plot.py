#!/usr/bin/env python3
"""Calibration curve for TypeSafe's construction confidence (phrasing A).

x: confidence, in equal-count bins. y: observed proportion, with Wilson 95% intervals.
Left panel, all 658 claims: agreement with the Haiku layer, and label stability across
the three phrasings. Right panel, the 156 keyed pairings: agreement with the keyed
construction id. None of the three references is ground truth; the Haiku layer is a
three-pass labelling by another model, and the keyed set is the expanded run's
non-random 56-claim sample.
"""
import json, math, sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
CEN = HERE.parent
ROOT = CEN.parents[1]
sys.path.insert(0, str(ROOT.parents[2] / ".house-style"))
import plot_style
plot_style.setup()
C = plot_style.COLORS


def wilson(k, n, z=1.96):
    if n == 0: return (0, 0, 0)
    p = k / n; d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, centre - half, centre + half


def binned(conf, hit, nbins):
    order = np.argsort(conf); conf, hit = np.asarray(conf)[order], np.asarray(hit)[order]
    out = []
    for chunk in np.array_split(np.arange(len(conf)), nbins):
        c, h = conf[chunk], hit[chunk]
        p, lo, hi = wilson(int(h.sum()), len(h))
        out.append((c.mean(), p, lo, hi, len(h)))
    return out


def draw(ax, series, title, nbins_note):
    ax.plot([0, 1], [0, 1], ls="--", lw=0.8, color=C["light"], zorder=1)
    for pts, (label, color, marker) in series:
        xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
        ax.errorbar(xs, ys, yerr=[[max(0.0, q[1] - q[2]) for q in pts], [max(0.0, q[3] - q[1]) for q in pts]], fmt=marker, color=color,
                    ms=5, lw=1, capsize=2, label=label, zorder=3)
        ax.plot(xs, ys, color=color, lw=0.8, alpha=0.6, zorder=2)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xlabel("TypeSafe confidence, phrasing A (bin means)")
    ax.set_ylabel("Observed proportion, 95% Wilson interval")
    ax.set_title(title, loc="left")
    ax.text(0.02, 0.97, nbins_note, transform=ax.transAxes, va="top", fontsize=8, color=C["dark"])
    plot_style.remove_spines(ax); plot_style.add_grid(ax)
    ax.legend(loc="lower right", frameon=False)


rows = json.loads((HERE / "per-claim.json").read_text())
confA = [r["A"][1] for r in rows]
agree_hk = [r["A"][0] == r["haiku"] for r in rows]
stable = [r["kind"] == "stable" for r in rows]

kc = json.loads((CEN / "normalize-key-check.json").read_text())
byid = {r["id"]: r for r in rows}
conf_k = [byid[p["census"]]["A"][1] for p in kc["pairs"]]
agree_k = [byid[p["census"]]["A"][0] == p["construction"][0] for p in kc["pairs"]]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.2))
draw(ax1, [(binned(confA, agree_hk, 10), ("agrees with the Haiku layer", C["primary"], "o")),
           (binned(confA, stable, 10), ("label stable across three phrasings", C["tertiary"], "s"))],
     "All 658 census claims", "10 equal-count bins of about 66 claims")
draw(ax2, [(binned(conf_k, agree_k, 5), ("agrees with the keyed construction", C["secondary"], "o"))],
     "156 pairings with the keyed set", "5 equal-count bins of about 31 pairings")
for ax, conf in ((ax1, confA), (ax2, conf_k)):
    ax.plot(conf, [0.005] * len(conf), "|", color=C["dark"], alpha=0.25, ms=6, zorder=1)
fig.suptitle("TypeSafe jev-1.13.0 construction labelling: confidence against three observed rates", x=0.01, ha="left", fontsize=11)
fig.tight_layout()
plot_style.save_figure(fig, HERE / "calibration")
# numbers behind the plot
out = {"all_658": {"agree_haiku": binned(confA, agree_hk, 10), "stable": binned(confA, stable, 10)}, "keyed_156": {"agree_key": binned(conf_k, agree_k, 5)}}
(HERE / "calibration-bins.json").write_text(json.dumps(out, indent=1) + "\n")
for name, pts in (("agree_haiku", out["all_658"]["agree_haiku"]), ("stable", out["all_658"]["stable"]), ("agree_key", out["keyed_156"]["agree_key"])):
    print(name, " ".join(f"{x:.2f}:{p:.2f}[{lo:.2f},{hi:.2f}]" for x, p, lo, hi, n in pts))
