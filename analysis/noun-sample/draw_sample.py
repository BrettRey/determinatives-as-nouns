#!/usr/bin/env python3
"""Draw the random noun (and outgroup) sample, 24 Oct 2026.

Brett: "the number of pronouns and determinatives is bounded; it's the full
universe. Will the number of nouns we analyze bias the results?" and "I'm not
sure how to draw and partition the nouns. In such cases, I ask 'what would
gelman do'?" (canon what-would-gelman-do). The design, fixed before drawing:

- Frame: SUBTLEX-UK (van Heuven, Mandera, Keuleers & Brysbaert 2014), the copy
  in papers/development/diagnostic-validity/data/ (that project's frame too).
  Not copied here; its SHA-256 is recorded in the output's header.
- Units: lemmas whose dominant part of speech is noun (common nouns), name
  (proper nouns), or adjective (the outgroup); the row for the lemma itself,
  alphabetic, at Zipf 2 or above; common nouns and adjectives must pass
  SUBTLEX's spell check. Lemmas already in the matrix are excluded.
- Strata: Zipf bands [2,3), [3,4), [4,5), [5,+). Frequency is known for every
  unit before any coding, so stratifying on it is ignorable once the band is
  in the model (BDA3 §8.2-8.3: "we must include x in the analysis if x is
  involved in the data collection mechanism ... Examples include stratum
  indicators in sampling"). Countability is not a stratum: it is one of the
  properties being coded, and stratifying on it would select on the outcome.
- Order: within each stratum, a random permutation with a fixed seed. Any
  prefix of a stratum's order is itself a simple random sample of it, so how
  many to code can be set later (by fake-data simulation of the planned
  analysis: Gelman et al. 2020, Bayesian workflow §4.1) without biasing which.
- Replacement: a drawn lemma that isn't a noun (or adjective) in its dominant
  use (a tagging error) is replaced by the next one in its stratum's order,
  and the replacement is logged; nothing else is replaced.
- The seven quantity nouns already coded (lot, number(s), plenty, dozen(s),
  majority) stay as a separate boundary stratum, chosen for being near the
  determinatives, so the model carries an indicator for them and the analysis
  runs with them in and out. Dog, water, Kim, Toronto stay as anchors.

Writes analysis/noun-sample/frame-order.csv.
"""
import csv
import hashlib
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FRAME = ROOT.parents[1] / "development" / "diagnostic-validity" / "data" / "SUBTLEX-UK.txt"
SEED = 20261024
BANDS = [(2, 3), (3, 4), (4, 5), (5, 99)]
POS = {"noun": "common noun", "name": "proper noun", "adjective": "adjective"}


def main():
    sha = hashlib.sha256(FRAME.read_bytes()).hexdigest()
    rows = list(csv.DictReader(FRAME.open(encoding="utf-8", errors="replace"), delimiter="\t"))
    forms = {}
    for r in rows:
        forms.setdefault((r["DomPoS"], r["DomPoSLemma"]), []).append(r["Spelling"])
    coded = {f["form"].lower() for f in csv.DictReader((ROOT / "analysis" / "codebook" / "forms.csv").open())}
    coded |= {f.split("_")[0] for f in coded}
    out = []
    rng = random.Random(SEED)
    for pos, cat in POS.items():
        for lo, hi in BANDS:
            units = []
            for r in rows:
                try:
                    z = float(r["LogFreq(Zipf)"])
                except ValueError:
                    continue
                w = r["Spelling"]
                if (r["DomPoS"] != pos or w != r["DomPoSLemma"] or not w.isalpha() or not lo <= z < hi
                        or w in coded or (pos != "name" and r["Spell_check"] not in ("UK", "US", "UKUS"))):
                    continue
                units.append((w, z))
            units.sort()
            rng.shuffle(units)
            for k, (w, z) in enumerate(units, start=1):
                others = sorted(set(forms.get((pos, w), [])) - {w})
                out.append({"stratum": cat, "band": f"{lo}-{hi if hi < 99 else ''}", "rank": k, "lemma": w,
                            "zipf": z, "other_forms": " ".join(others)})
    with (HERE / "frame-order.csv").open("w", newline="") as fh:
        fh.write(f"# SUBTLEX-UK sha256 {sha}; seed {SEED}; draw_sample.py, 24 Oct 2026\n")
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    from collections import Counter
    print("units per stratum and band:", dict(Counter((r["stratum"], r["band"]) for r in out)))
    for cat in POS.values():
        print(cat, ": first five per band:",
              {b: [r["lemma"] for r in out if r["stratum"] == cat and r["band"] == b][:5]
               for b in sorted({r["band"] for r in out})})


if __name__ == "__main__":
    main()
