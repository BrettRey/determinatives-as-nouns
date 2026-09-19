# Quote audit, 18 September 2026

<!-- SUMMARY: every quotation in the manuscript checked against its source: 14 source quotations verbatim with pages confirmed, 24 corpus lines verbatim in their saved files; no finding · status: clean · updated: 2026-09-18 -->

Text: `determinatives-as-nouns.tex` at commit 664c586. Procedure: the registry's `quote-audit` entry. Mechanical layer first (`check-quotes.py --gate`), then every quotation the script did not clear resolved and matched character by character. Model: Claude Fable 5.1, with the sources read in this session (the *CGEL* PDF text through the gate script, the Van Eynde 2007 sidecar, the corpus files, and the 1924 Palmer page on HathiTrust).

## Mechanical layer

`python3 .house-style/check-quotes.py determinatives-as-nouns.tex --gate`: 12 PASS, 6 MISSING, 2 NOSOURCE, 29 quoted spans without a page cite.

- The 6 MISSING are corpus lines in footnotes (*It won't be much*, *Pay won't be much*, *There hasn't been much*, the two *select few* lines, and the Stanford slide title) that the script attributed to the nearest `\citep`, which is *CGEL*. They are not *CGEL* quotations. Each is checked below against its corpus file.
- The 2 NOSOURCE are Palmer 1924, not held locally. Resolved below.
- Of the 29 uncited spans, 24 are corpus lines with their source named in parentheses, 4 are glosses in `\enquote*` (*my car*, *belongs to me*, *my contribution*, *my slides*) or a formula reading, and 1 is a web title (*List of determinatives in English*).

## Source quotations (14)

| Quotation | Cited | Checked against | Verdict |
|---|---|---|---|
| "the inflection of the head noun" | *CGEL* 479 | PDF text (gate) | PASS |
| "admits *very*, *good*, and *fair*"; "sui generis" | *CGEL* 392, 394 | PDF text (gate) | PASS |
| "doesn't provide a structure with potential for replacements and expansion" | *CGEL* 351–352 | PDF text (gate) | PASS |
| "fails all of the determinative criteria (a)–(c)" | *CGEL* 539–540 | PDF text (gate) | PASS |
| "a small range of adjectives (e.g. *such* in [ic])"; "a predeterminer modifier normally precedes a determiner" | *CGEL* 331 | PDF text (gate) | PASS |
| "syntactically inert" | *CGEL* 394 | PDF text (gate) | PASS |
| "denote the set of people bearing this name" | *CGEL* 423 n. 43 | PDF text (gate) | PASS |
| "takes a full range of dependents, including determiners and restrictive modifiers" | *CGEL* 521 | PDF text (gate) | PASS |
| "primarily determinatives but they have a secondary use in which they inflect for number and hence belong in the noun category" | *CGEL* 385 | PDF text (gate) | PASS |
| "are invariably lexical" | Van Eynde 2007 §5 | `literature/VanEynde_2007_BigMess.md` | PASS: "what and such are invariably lexical" |
| "lexically select a nominal which is either unmarked or introduced by the indefinite article" | Van Eynde 2007 §5 | same sidecar; the gate missed it because the sidecar has the *fi* ligature in "indeﬁnite" | PASS: "I assume that the exclamative what and the demonstrative such lexically select a nominal which is either unmarked or introduced by the indeﬁnite article" |
| "determinative adjectives" | Palmer 1924, 24 | HathiTrust uc1.$b14634, seq. 64 = p. 24, read in the text-only view on 18 Sept 2026 (public domain, Google-digitized) | PASS: "To group with the pronouns all determinative adjectives (e.g. article-like, demonstratives, possessives, numerals, etc.), shortening the term to determinatives" |
| "be used indifferently as pronouns or as modifiers of nouns" | Palmer 1924, 24 | same page | PASS: "most of the members of this category may be used indifferently as pronouns or as modifiers of nouns" |

Palmer note. The Internet Archive copy (`grammarofspokene0000haro`) is the 1969 third edition, rewritten by Blandford, whose preface says "the now widely used term Determiners has been substituted for his Determinatives" and whose p. 31 reads "as pronouns or as qualifiers of nouns". The paper cites the 1924 edition, and the 1924 page has "modifiers" and "determinatives", as quoted. The paper's paraphrase "qualifying adjectives, which permit predicative use, comparison, and adverbial modification" renders Palmer's "qualificative adjectives ... epithetic and predicative uses, susceptibility to comparison, and susceptibility of being modified by adverbs"; his term is *qualificatives*, which the appendix could use in place of "qualifying".

## Corpus quotations (24)

All found verbatim in the saved files under `corpus/exclusion_tests/` and `corpus/independent_argument/`, with the cited dates matching the line stamps: the two *every* lines (`every-reading.md`, `every_v.report.md`); the three *each of* lines (`each_of_them_...report.md`, `each_of_the_nn2_...report.md`); the eleven *be much / there is little / too much / a lot* lines (`2026-09-18-brett-supplied-...md`), of which the *topping* line was restored to COCA's inner quotation marks in the numbers audit; the two *select few* lines (`few_who.jsonl`); the three *few would / few have* lines and the *thousand flowers* line (`few_would.report.md`, `few_have.report.md`); the four *lucky/privileged few* lines (`few_who.report.md`); the four compound lines (*anonymous someone*, *responsible someone*, *furry something*, *such an anyone*) and *I qualified as an anybody* (`readings.md`, `at_someone_...report.md`). Search strings and results are in the session record; the two compound lines from *Bones* and *Skiing* rest on `readings.md`, a hand record of a COCA reading on 17 September, not on a saved KWIC file.

## Attribution under blinding

Two self-citations carry quotations or paraphrases: none. The Palmer, Van Eynde, and *CGEL* attributions are third-party and survive anonymization unchanged.

## Findings

None requiring a change. One optional wording: "qualifying adjectives" to Palmer's own "qualificatives" in the appendix.
