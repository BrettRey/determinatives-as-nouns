# Measurement-construction audit, 19 September 2026

<!-- SUMMARY: each measured variable in the article checked against its saved lines and logs: the independent-every absence claim is contradicted by three saved NOW lines no human has read; the each-of-them plural rate counts 13 non-agreeing lines out of 75; the plural-compound counts drop the log's own caveats · status: findings for Brett, no manuscript change · updated: 2026-09-19 -->

Text: `determinatives-as-nouns.tex` after commit af63c84, with the 19 September quote-audit repair. Procedure: the registry's `measurement-construction-audit` entry. Model: Claude Opus 5, reading the saved corpus files and logs, not the prose describing them. The 9 September audit (`2026-09-09-measurement-estimand-inference-numbers.md`) covered the 2021 matrix and the CGELBank counts; the 26 analysis files it checked still match their 9 September SHA-256 checksums (`notes/snapshots/2026-09-09-empirical-relocation/analysis-checksums.json`: 26 unchanged, 0 changed, 0 missing), so those rows stand. This pass covers the corpus variables added since then.

## Object map

| Variable (line) | Construct claimed | Raw source and rule | Validation | Verdict |
|---|---|---|---|---|
| Independent *every*, fused Head (l. 281 and footnote) | *every* never stands as an ordinary fused Head | COCA `each/every [v*]` export (618 *every* lines) and NOW `every was` / `every has` (96 + 68 saved lines); TypeSafe screen, escalated lines read | **Read by Claude, "not yet by Brett"** (`corpus/exclusion_tests/every-reading.md`, status line) | **Defect: claim contradicted by the saved record** (M1) |
| Plural agreement after *each of them* (l. 99) | plural verb forms are about a sixth of the relevant query hits | COCA List counts, *each of them* + is/has/was 389, + have/are/were 78; 75 plural lines saved in `coca_each_of_them_v.jsonl` | TypeSafe labelled all 75 as plural agreement | **Defect: proxy includes non-agreeing lines** (M2) |
| Independent *each* before a finite verb (l. 281 n.) | frequent independent *each* | COCA List counts, *each has/was/will* 3,090 | none; List counts only, no lines saved | **Proxy, stated as the thing** (M3) |
| Plural compound determinatives (l. 750 n.) | "The plural forms are common" in support of the secondary set-denoting use | COCA List counts, 17 September (`log.md`) | none; List counts only | **Caveats in the log dropped from the footnote** (M4) |
| Bare generic *few would* (l. 397 n.) | 82 of 94 lines have no set in the visible context | NOW, 94 lines, read in full by Brett | human reading of every line; window limit stated ("7 can't be decided") | Sound |
| *each of the* + plural noun (l. 99 n.) | plural agreement occurs, including in edited prose | COCA 151 was / 73 were | footnote already says the share is inflated by agreement with another head | Sound as worded |
| Coverage-audit cells (l. 728) | 103 cells, 35 identical lexical facts, 32 Dn cells | `analysis/coverage-audit.json` | presented as the author's classification, "the analysis, not data" (`coverage-audit.tex` l. 25) | Sound; no reliability claim is made or needed |

## M1. Independent *every*: the absence claim and the NOW residue

The article says: "in the screened COCA and NOW lines, \mention{every} never stands as an ordinary fused Head", and the footnote: "None of 618 COCA lines for \mention{every} before a verb and 164 NOW lines for \mention{every was/has} shows an ordinary fused-head use. Residues include [ellipsis] and [a binomial]."

The saved NOW lines contain three edited-prose cases of independent *every* with an antecedent set, found and listed in `every-reading.md` on 17 September and confirmed in `every_has.jsonl` today:

- "each car offers something unique to the market. Every has its strengths and will speak to its unique audience" (wheels24.co.za, ZA, 30 April 2020)
- "a special monument decorated with the city seal and the park name. Every has a story, many with themed play structures" (patch.com, US, 30 July 2025)
- "a batch of one-off pressure plans tailored to each opponent's pass protection rules. Every has different blocking mechanics" (theguardian.com, GB, 10 February 2024)

Borderline: "how kind and generous every was that attended" (Bolton News, 2023); "every has a right to do what they feel is right" (RNZ, 2017, quoted speech).

These have the structure the article treats as ordinary fused-head use for *each* and *some*: an independent determinative whose set is supplied by the discourse (§4.2: "In \mention{I'll take some}, the relevant substance or set may still be supplied by discourse"). The reading note concluded that "A categorical exclusion is too strong as stated". The 17 September DECISIONS entries summarize the residue as "ellipsis, reply fragments and binomials" and never mention these three lines, and the manuscript's footnote does the same. No human has read the lines.

What it costs: the article's one quantified negative, and the example the opportunity-frequency reasoning (DECISIONS 17 September, "adopted") rests on. The three-in-164 rate against the *each* counts would still support a strong restriction, which is the reading note's own proposal: attested marginally in the *each*-like anaphoric reading, not attested without an antecedent set, so #*Every arrived* keeps its star. Whether these three are ordinary fused heads, slips, or something the article should name is Brett's call. **No manuscript change made.**

## M2. The *each of them* plural rate

Body (l. 99): "plural verb forms account for about a sixth of the relevant COCA query hits." That is 78 / (389 + 78) = 16.7 percent of List-count hits.

All 75 saved plural lines were read for two string facts: whether the verb is finite, and whether *each of them* is its subject. Thirteen are not plural agreement with *each of them*:

- non-finite *have* after an auxiliary or a perception/causative verb: *could not each of them have made*, *What did each of them have to contribute?*, *what did each of them have to do*, *did each of them have two senators?*, *does each of them have a need* (singular *does*), *witnessed each of them have*, *seeing each of them have*, *let each of them have their say* (8 lines: have-list nos. 18, 21, 35, 42, 45, 25, 31, 38);
- a verb agreeing with another head: *the profoundest thinkers in each of them have*, *One hundred different ways of writing each of them have*, *The passwords to each of them are*, *the consequences of denying each of them are*, *Snatches from each of them were* (5 lines: have 40, 41; are 1, 5; were 9).

(*Do each of them have* is counted as plural agreement, on *do*.) So 62 of 75 saved plural lines show a finite plural verb agreeing with *each of them*. TypeSafe labelled all 75 `verb_number=plural`, another instance of the positional weakness recorded in the TypeSafe profile. The 389 singular hits were never saved or screened, so a corrected rate can't be computed; scaling the plural side alone gives about 14 percent. This classification is Claude's reading of string facts, a candidate until Brett has checked it.

Proposed repair (not applied; the sentence was accepted this morning): body "Plural agreement after \mention{each of them} is well attested." and in the footnote after "+ \mention{have/are/were} 78": "; of the 75 plural lines saved, 62 have a finite plural verb agreeing with \mention{each of them}, the rest non-finite \mention{have} (\mention{did each of them have}) or a verb agreeing with another head (\mention{the passwords to each of them are})". If the rate is wanted in the body, "about one in seven" requires screening the singular lines first.

## M3. *each has/was/will* as independent *each*

The footnote's 3,090 are List counts for the strings; no lines were saved. *each will* (507) can include floating *each* after a plural subject (*they each will*), which isn't independent *each*. The body now says only "frequent independent \mention{each} before a finite verb", which *each has* and *each was* (2,583) support even if every *each will* were floating, so the claim survives. The footnote could say "string counts" or drop *will*; optional.

## M4. Plural compound counts

`corpus/exclusion_tests/log.md` (17 September) records the caveats: "*nothings* is largely *sweet nothings*; ... *somethings* includes *thirty-somethings* (CGEL p. 1716)". The footnote keeps the *-wheres* exclusion but drops these two. Neither undermines "plural forms are common" (*sweet nothings* is itself a plural with a pre-head adjective), but a reader checking *somethings* 590 would find a different formation among them. Suggested footnote addition: "many lexicalized (\mention{sweet nothings}), and \mention{somethings} includes \mention{thirty-somethings}". Whether COCA's tokenizer returns hyphenated *thirty-somethings* for the string *somethings* wasn't checked here.

## No finding

- *few would*: the strongest-measured variable in the article: every line read by a human, with the window limit in the text.
- The article reports no rate, frequency, or proportion as a population estimate; no normalization or cross-corpus aggregation occurs.
