# Quote audit, 15 October 2026

<!-- SUMMARY: quote-audit pass on determinatives-as-nouns.tex at 2e586d1; 30 cited quotations: 24 PASS mechanically, 4 MISSING are corpus lines mis-attributed by the script (all match their corpus records), 2 NOSOURCE are Palmer 1924 (verified 18 Sept on HathiTrust, text unchanged); 18 corpus quotations added since 4 Oct checked against records, 17 exact, 1 added to its record · status: no manuscript changes needed · updated: 2026-10-15 -->

Text: `determinatives-as-nouns.tex` at `2e586d1`. Procedure: the registry's `quote-audit` entry. Model: Claude Opus 5.5 (session), with sources read in this session: the CGEL PDF text through the gate script, Halm 2021 (`literature/halm_2021_virtual_performatives_modified_pronouns.*`), and the corpus records under `corpus/`.

## Mechanical layer

`check-quotes.py --gate`: MISSING 4, NOSOURCE 2, PASS 24, SCAREQUOTE 24 (exit 1, from the MISSING and NOSOURCE).

**PASS (24).** These include all the CGEL quotations added since 4 October:
- p. 410, "occurs with just the determiner function"
- p. 385, "approximately"
- p. 377, "cannot occur in internal modifier function"
- p. 549, "as in NP structure, before the and that"
- p. 920, "occurs only as modifier in NP structure"

The Halm example also passes: "The 12-year-old me is kicking myself", p. 19.

**MISSING (4): all corpus lines the script attributed to the nearest `\citep`.**

| Quote | Line | Script's attribution | Actual source | Verdict |
|---|---|---|---|---|
| "I shouldn't have to leave for a select few who are uncomfortable" | 338 | CGEL p. 392 | NOW, *New York Daily News* 2022; `corpus/independent_argument/few_who.jsonl` | PASS against record |
| "for those select few who know" | 338 | CGEL p. 392 | NOW; `few_who.jsonl` ("for those select few who know where one might be hiding") | PASS (truncation at a phrase boundary) |
| "Jamie didn't want to be a he or a she but a they" | 836 | CGEL p. 429 n. 46 | COCA, NPR *Hidden Brain* 2017; `corpus/exclusion_tests/2026-10-04-brett-supplied-a-he-or-a-she.md` | PASS against record |
| "someday the real you will wish he knew where to call" | 838 | Halm pp. 19, 29–30 | COCA, *Virginia Quarterly Review* 2004 ("And someday the real you will wish he knew where to call"); `corpus/exclusion_tests/2026-10-15-brett-supplied-the-adj-pronoun.md` | PASS against record |

The fourth case is worth a look. The sentence reads "…set against each other \citep[19, 29--30]{halm2021virtual}, as in \enquote{someday the real you will wish he knew where to call}". The citation comes before the example, and the *Virginia Quarterly Review* source sits in the previous sentence's footnote, so a reader as well as the script could take the example for Halm's. Optional fix: add "(\textit{Virginia Quarterly Review}, 2004)" after the quotation.

**NOSOURCE (2): Palmer 1924, p. 24.** "determinative adjectives" and "be used indifferently as pronouns or as modifiers of nouns". Verified on 18 September against HathiTrust uc1.$b14634, seq. 64 = p. 24 (`2026-09-18-quote-audit.md`). `git log -S"be used indifferently"` since 18 September shows no change to the passage. Not re-read today.

## Corpus quotations added since 4 October

Each was matched as a fixed string against `corpus/`:
- Exact (17): *Does the real you smell like a rose garden?*; *I took the old me, and I crumpled her up*; *someday the real you will wish he knew where to call*; *The old me rarely left the office. The new me rarely went in*; *when times are bad, the some will become the many*; *Perhaps the author is one of the some who hope for a return to the good old days*; *one of the some who are required to have the crusading attitude*; *benefit the all rather than the some*; *drove the some into Louisiana, Arkansas and Oklahoma*; *the some who say it is the General Accounting Office*; *our country needs some of us to sacrifice, the some of us who can*; *the fact the some people don't care*; *the some people can't hope to play while others seem unaffected*; *The costume is a bit much*; *Antonio Pinto's score is a bit much at times*; *The retreat may have been too little, too late*; *the rescue efforts were too little, too late*.
- In the paste but not yet in its record (1): *derided the move as too little, too late* (*USA Today*, 2007, line 98). The verbatim line is now added to `2026-10-15-brett-supplied-too-little-too-late.md`.

Normalization: COCA tokenizes punctuation with spaces (*too little , too late*). The manuscript closes them up, as it does elsewhere.

## Outcome

No quotation is wrong. One optional clarification (the *Virginia Quarterly Review* source inline at line 838). One record completed.
