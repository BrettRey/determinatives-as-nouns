#!/usr/bin/env python3
"""Histogram of TypeSafe's construction confidence over all runs (phrasings A, B, C),
with the top-option probability alongside, and the same split by whether the top option
was taxonomic_or_meta. One bin per returned value; the API rounds to two decimals, so coarser
bins alias (a 0.02 bin catches two or three values and produces a sawtooth)."""
import glob, json, sys
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

conf, top, taxo = [], [], []
for d, tag in ((CEN / "typesafe-full-2026-09-16/responses", "A"), (CEN / "typesafe-keyed-2026-09-16/responses", "A"),
               (HERE / "responses-B", "B"), (HERE / "responses-C", "C")):
    for f in glob.glob(str(d / "*.json")):
        a = json.load(open(f))["answers"]["construction"]
        conf.append(a["confidence"]); top.append(max(a["probabilities"].values())); taxo.append(a["choice"] == "taxonomic_or_meta")
conf, top, taxo = np.array(conf), np.array(top), np.array(taxo)
bins = np.arange(-0.005, 1.0051, 0.01)  # one bin per returned value: the API rounds to two decimals

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 3.8), sharey=True)
ax1.hist(conf, bins=bins, color=C["primary"], alpha=0.85, label="confidence")
ax1.hist(top, bins=bins, histtype="step", color=C["secondary"], lw=1.2, label="top-option probability")
ax1.axvline(0.5, color=C["dark"], lw=0.6, ls=":")
ax1.set_title(f"All construction answers, three phrasings (n = {len(conf)})", loc="left")
ax1.legend(frameon=False, loc="upper left")
ax2.hist([conf[~taxo], conf[taxo]], bins=bins, stacked=True, color=[C["primary"], C["quinary"]], alpha=0.85,
         label=[f"top option a specific construction ({(~taxo).sum()})", f"top option taxonomic_or_meta ({taxo.sum()})"])
ax2.axvline(0.5, color=C["dark"], lw=0.6, ls=":")
ax2.set_title("Confidence, split by the chosen option", loc="left")
ax2.legend(frameon=False, loc="upper left")
for ax in (ax1, ax2):
    ax.set_xlim(0, 1); ax.set_xlabel("value (one bin per two-decimal value the API returns)"); plot_style.remove_spines(ax); plot_style.add_grid(ax)
ax1.set_ylabel("answers")
fig.tight_layout()
plot_style.save_figure(fig, HERE / "confidence-histogram")
mid = ((conf >= 0.45) & (conf < 0.55)).mean(); hi = (conf >= 0.9).mean()
print(f"share in [0.45,0.55): {mid:.3f}   share >= 0.9: {hi:.3f}   taxonomic share of [0.45,0.55): {taxo[(conf >= 0.45) & (conf < 0.55)].mean():.2f}   taxonomic share overall: {taxo.mean():.2f}")
