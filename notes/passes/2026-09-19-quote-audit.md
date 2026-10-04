# Quote audit, 19 September 2026

<!-- SUMMARY: quotation re-audit after the 19 September cuts: 36 quotations remain, none new or reworded, all still attributed; one slide title corrected from the file name to the deck's title · status: clean after one repair · updated: 2026-09-19 -->

Text: `determinatives-as-nouns.tex` after commit af63c84. Procedure: the registry's `quote-audit` entry. Model: Claude Opus 5. Baseline: the full audit of 18 September (`notes/passes/2026-09-18-quote-audit.md`, text at 664c586), which checked 14 source quotations and 24 corpus lines character by character.

## What moved since the full audit

Every `\enquote` span was extracted from the text at 664c586 and from the current text and compared as strings. Result: 55 spans then, 36 now; **no span is new or reworded**, and 19 were removed by the cuts:

- the eleven *be much / there is little / too much / a lot* corpus lines, and the inner *topping*;
- *CGEL*'s "doesn't provide a structure with potential for replacements and expansion" (351–352), now paraphrased as "appeals to the potential for replacement and expansion" with the same page cite, which the text still supports;
- the *few have the durability* line and the *Obialor* and *privileged few* lines.

The Opus cuts assessment flagged "the hurt cannot be much" as quoted without a source. It is no longer in the manuscript (`grep -n "hurt cannot"`: no hits).

## Attribution check on the 36 remaining

Each span was printed with the 110 characters after it. Every corpus line is still followed by its outlet and year, and every source quotation still closes on its `\citep` or `\textcite`. None of the cuts separated a quotation from its attribution.

## Mechanical layer

`check-quotes.py determinatives-as-nouns.tex --gate`: 11 PASS, 3 MISSING, 2 NOSOURCE, 15 spans without page cites.

- The 3 MISSING are the two *select few* NOW lines (l. 293) and the slide title (l. 137), which the script attributes to the nearest *CGEL* cite. They aren't *CGEL* quotations. The *select few* lines were matched in `few_who.jsonl` on 18 September and are unchanged.
- The 2 NOSOURCE are Palmer 1924 p. 24, read on HathiTrust (uc1.$b14634, seq. 64) on 18 September; unchanged.
- *CGEL* pages were re-derived from the PDF text layer (offset 20 between PDF and printed pages): "denote the set of people bearing this name" and "takes a full range of dependents, including determiners and restrictive modifiers" both on printed p. 521, matching the single `\citep[521]` that now closes l. 752; *a little something* on p. 423, matching the conversion cite; "inflect for number and hence" on p. 385.
- Van Eynde 2007 §5 "lexically select a nominal ..." remains a gate miss only because of the *fi* ligature in the sidecar; verified verbatim on 18 September.

## Finding and repair

**Slide citation (l. 137).** The footnote quoted "Codeswitching LLMs" as the title of the source for *Bluer is better*. That string is the PDF's file name. The deck, fetched from the cited URL on 19 September 2026, is titled "Code Switching for/with Multilingual LLMs", by Alice Oh (KAIST), dated Nov 2025, and slide 8 carries "Bluer is better" over a "Results" colour scale, as the footnote says. The footnote now reads: "in Alice Oh's slides \enquote{Code Switching for/with Multilingual LLMs} for Stanford CS329X (November 2025), slide~8". The URL is unchanged.

## Still open (optional, from 18 September)

Palmer's own term is *qualificative* adjectives; the appendix's "qualifying adjectives" is a paraphrase and not wrong.

## Addendum, after the source-reread repairs (same day)

The source reread added one quoted span: Lyons's feature name in "share the feature \enquote{definite}" (l. 827). Checked against `literature/lyons1968-grammatical-categories.md` ("They all 'include' the feature 'definite'"), on printed p. 279 (running head "7.2. Deictic categories 279", PDF p. 10; established by the source reread, reader D). PASS. The other repairs changed paraphrase and page numbers, not quotations; the one new citation key, `vanlangendonck1994`, carries no quotation. The *Norman Foster*, *the weather recently*, and *almost textbook* examples are mentions, not quotations.

## Addendum, 4 October 2026: four quotations added to §2.4

Brett's specialization argument added four *CGEL* quotations, each read on 4 October against the printed-page text split from `literature/huddlestonpullum2002.pdf` (offset 20, re-split that day):

| Quotation | Page | Verdict |
|---|---|---|
| "most central members are characteristically used deictically or anaphorically" | 425 | PASS: "Pronouns constitute a closed category of words whose most central members are characteristically used deictically or anaphorically." |
| "characteristically express quantification" | 358 | PASS: "The determiners, we have seen, serve to mark the NP as definite or indefinite, but at the same time the basic ones characteristically express quantification." |
| "no one-to-one relation" | 358 | PASS: "We use quantification and quantifier as semantic terms, noting that there is no one-to-one relation between them and the syntactic category of determinatives." |
| "need not be realised by a determinative" | 358 | PASS: "As we have seen, moreover, it need not be realised by a determinative, but can itself have the form of an embedded NP, in either genitive or plain case." (*it* = the determiner; CGEL's spelling kept.) |

The pro-form gloss is paraphrase, not quotation (p. 68: "we call such anaphors 'pro-forms', a term which also covers various forms which are not pronouns, such as *so*"), and the inventory of interrogative and relative determinatives is cited, not quoted (p. 356).
