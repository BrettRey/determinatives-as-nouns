# Negative claims, 19 September 2026 (incremental)

<!-- SUMMARY: report-only negative-claims pass over the 81 paragraphs new or reworded since 6e86966; four open defects (a certain left out of the complex-determinative negative; CGEL said to state the head genitive separately; exclamative what predicative negative unmarked; a cited be-much line sits in Solt's starred frame), one resolved concurrently (Van Eynde "only"), plus the known independent-every corpus negative; inward novelty search rerun, nothing new · status: report, not applied · updated: 2026-09-19 -->

Procedure: the registry's `negative-claims-audit` entry, restricted to the paragraphs listed in `notes/passes/2026-09-19-incremental/changed-paragraphs.txt`. Manuscript read at HEAD `af63c84` plus the uncommitted footnote edit at l.137 (MD5 `06bfc608873b97cf6f086a058c4c0fb8`). Line numbers are that file's. This pass edited nothing in the manuscript. Another session edited 29 paragraphs in place while it ran (MD5 now `b252f24ee80f4c2536fed20beebc2013`; still 841 lines, one paragraph per line, so the line numbers hold). Every "old" string below was re-checked against the current file and matches, except D3, which that session resolved. Baseline: `2026-09-18-negative-claims.md`; its outcomes stand except where noted below.

Each negative was read against the source it cites or the file behind it. CGEL was read in `literature/00-CGEL.md`, with printed pages confirmed by `pdftotext` on `00-CGEL.pdf` (PDF page minus 20). Corpus claims were read against `corpus/exclusion_tests/` (log, reports, `readings.md`, `every-reading.md`) and `corpus/independent_argument/`.

## Defects

### D1. l.311 (with l.740 and the abstract): *a certain* is missing from the complex-determinative negative

The negative: "no complex determinatives remain in this account; *CGEL*'s other members of that class, cardinals above a hundred, are the subject of Reynolds (2026)". *CGEL* adds a further member, tentatively, on p. 393: "there is a strong association with *a*, and it may be best to treat *a certain* as a complex determinative" (*This gave her a certain authority*; *To a certain extent*). The manuscript never mentions *a certain* outside the set-denoting *a certain someone* (grep of the .tex).

Search: `grep -n -i "complex determinative"` over `literature/00-CGEL.md`, then a `pdftotext` sweep of every page of `00-CGEL.pdf` from PDF p. 360 to p. 1900 for `complex\s*-?\s*determinative`. Every hit: p. 393 (*a certain*), p. 394 (*many a*, *a great many*), p. 621 (*a number of*, rejected), and the index entry "complex determinative 392". The list on p. 356 reads "such as *a few*, *many a*, cardinal numerals expressing numbers greater than 100", an open list.

- **l.311.** Old: `With peripheral \mention{a} in \mention{a few} and predeterminer \mention{many} in \mention{many a}, no complex determinatives remain in this account; \textit{CGEL}'s other members of that class, cardinals above a hundred, are the subject of \textcite{reynolds2026numerals}.` New: `With peripheral \mention{a} in \mention{a few} and predeterminer \mention{many} in \mention{many a}, none of the four remains a complex determinative in this account. Of \textit{CGEL}'s other candidates, cardinals above a hundred are the subject of \textcite{reynolds2026numerals}, and I leave aside \mention{a certain}, which it adds tentatively \citep[393]{huddleston2002}.` (Brett's alternative: analyse *a certain* here, as Det *a* plus internal *certain* with a lexical co-occurrence condition. That is an analysis choice for him, not a wording repair.)
- **l.740.** Old: `The complex determinatives reduce to peripheral \mention{a} and predeterminer \mention{many}` New: `The four complex determinatives analysed here reduce to peripheral \mention{a} and predeterminer \mention{many}`
- **l.29 (abstract; optional once l.311 is fixed).** Old: `reanalyses its complex determinatives \mention{a few}` New: `reanalyses four of its complex determinatives, \mention{a few}`

### D2. l.738: *CGEL* is said to state the head genitive separately for nouns and determinatives

This is an implicit negative about a named source ("*CGEL* doesn't state these once"). For the head genitive it is false. *CGEL* p. 479, [63], lists *Edward's* and *everyone's* together under one definition ("marked ... by the inflection of the head noun"). The manuscript says the same itself at l.147, and l.730 describes the separate-D cost correctly as extending "the head-genitive definition to D". The other three items in the l.738 list (number transparency, degree modifiers, peripheral attachment) are stated in separate places in *CGEL* and weren't challenged.

- Old: `(§\ref{sec:enough}); peripheral attachment in \mention{almost every} and \mention{only you} (§\ref{sec:payne}); and the head genitive in \mention{everyone's} and \mention{Edward's} (§\ref{sec:inflection}).` New: `(§\ref{sec:enough}); and peripheral attachment in \mention{almost every} and \mention{only you} (§\ref{sec:payne}). The head genitive, which \textit{CGEL} states once for \mention{everyone's} and \mention{Edward's}, then keeps its definition by the head noun without stretching it (§\ref{sec:inflection}).`

### D3. l.247: "cites English only for the marking contrast" was too narrow (resolved during this pass)

Van Eynde (2003) applies the inflection-and-agreement criterion only to Italian and Dutch (§1.1–1.2, Tables 1–2). That part held. The "only" clause failed. He also cites English to set out the specifier analysis he rejects (*his many beautiful pictures*, *\*the his pictures*, §1) and to contrast English possessive *'s* with the Dutch affix (fn. 2). The marking contrast is fn. 4. Search: `grep -n -i English` over `literature/VanEynde2003_On_the_notion_determiner.md`, and a reading of §§1–3.

Another session rewrote l.247 while this pass was running. It now reads "(he applies it to Italian and Dutch determiners; his English examples don't test it on determiners)". That's a narrow claim that can be checked, and it holds on the same search: none of his English examples bears on inflection or agreement. No repair needed.

### D4. l.309: "exclamative \mention{what} has no predicative use" is an unmarked negative

Yesterday's pass added starred forms for the grade and degree clause (*\*sucher*, *\*a very such mess*) but not for this clause. It has no star and no source. *CGEL* pp. 539–540 (read) gives exclamative *what* as failing determinative criteria (a)–(c) and says nothing about predicative use. The clause traces to the agent note `notes/2026-09-17-exclamative-such-what.md`, point 3, which also has no source. Under l.91 it must either be recorded as a judgment or be cut.

- Option A (judgment). Old: `and exclamative \mention{what} has no predicative use.` New: `and exclamative \mention{what} has no predicative use (\ungram{\mention{The mess was what!}}).` Brett should choose the example: any *be what* frame also has an echo-question reading with interrogative *what*, and he should confirm that the starred reading is the one he means.
- Option B (cut). Old: `(\ungram{\mention{sucher}}, \ungram{\mention{a very such mess}}), and exclamative \mention{what} has no predicative use.` New: `(\ungram{\mention{sucher}}, \ungram{\mention{a very such mess}}).`

### D5. l.129 (with the l.131 footnote and the supplement): a cited line sits in Solt's starred frame

l.129 says *much* and *little* "take the predicative use only with an amount-denoting subject" (Solt's *\*John's patience is much*), and gives *the hurt can not be much* as an instance of the amount case. Solt (2015: (76d)) stars "*John's patience is little/is much/isn't much*". She includes the negated form to show that the badness "is not due entirely to [much's] NPI-like character" (checked in `literature/solt_2015_q_adjectives_semantics_of_quantity.md`). *The hurt* (a wound) is a subject of the patience kind, in the negated frame Solt stars, so the project's own line undercuts the "only" rather than illustrating it. The line is also Romeo's in *Romeo and Juliet* 3.1, quoted in the film (this identification comes from memory and hasn't been checked against a text). So it isn't synchronic evidence (l.42).

- **l.129.** Old: `is mostly \mention{it won't be much}, \mention{pay won't be much}, \mention{the hurt can not be much}, beside existential` New: `is mostly \mention{it won't be much} and \mention{pay won't be much}, beside existential`
- **l.131 footnote.** Old: `\mention{pay won't be much} (\textit{Ruben's Place}, 2012), \mention{the hurt can not be much} (\textit{Shakespeare in Love}, 1998), and` New: `\mention{pay won't be much} (\textit{Ruben's Place}, 2012), and`
- Make the same deletion in `quantifier-controls.tex` l.118.

### D6 (the parent already knows). l.281 and its footnote: the independent-*every* corpus negative

Recorded, not re-derived. Three things beyond the three NOW lines:

1. The footnote's "164 NOW lines" is `every_was` (96) plus `every_has` (68). The three each-like lines (*Every has its strengths*, *Every has a story*, *Every has different blocking mechanics*) fall inside the counted sample, so "None of ... shows" is contradicted by that sample.
2. `every-reading.md` itself concludes "A categorical exclusion is too strong as stated", and its status is "read by Claude, not yet by Brett". The footnote doesn't say who read the lines, although l.397 does say so for *few would*.
3. The main text's list of residue types (coordinate, preceding turn, binomial) leaves out both the NOW anaphoric cases and the slips for *everyone*, which the supplement's exclusion table records.

The same claim appears in `quantifier-controls.tex` l.114 and in `analysis/exclusion-checks.json`.

Candidate wording, pending Brett's reading of the three clear and two borderline lines:

- Old: `in the screened COCA and NOW lines, \mention{every} never stands as an ordinary fused Head, despite frequent independent \mention{each} before a finite verb. Where it does stand without a noun, the noun is recoverable from a coordinate or the preceding turn, or \mention{every} closes a binomial.` New: `in the screened COCA lines, \mention{every} never stands as an ordinary fused Head, despite frequent independent \mention{each} before a finite verb; where it stands without a noun, the noun is recoverable from a coordinate or the preceding turn, or \mention{every} closes a binomial. NOW adds three edited-prose lines with \mention{every} in \mention{each}'s anaphoric reading after an antecedent set, and informal text uses \mention{every} for \mention{everyone}.`
- Footnote. Old: `None of 618 COCA lines for \mention{every} before a verb and 164 NOW lines for \mention{every was/has} shows an ordinary fused-head use.` New: `None of 618 COCA lines for \mention{every} before a verb shows an ordinary fused-head use; of 164 NOW lines for \mention{every was/has}, three do, after an antecedent set (\enquote{each car offers something unique to the market. Every has its strengths}, Wheels24, 2020).`

## Optional (preferences, not defects)

- **l.307** "Neither \mention{many a} nor \mention{what a} has an independent use". The *many a* half has a *CGEL* basis that the manuscript doesn't quote: *CGEL* p. 394 says "Like *a*, *many a* always functions as determiner". Old: `Neither \mention{many a} nor \mention{what a} has an independent use:` New: `Neither \mention{many a} nor \mention{what a} has an independent use (\textit{CGEL}: \mention{many a} \enquote{always functions as determiner}, p.~394):`. The *what a* half remains a judgment without a star.
- **l.307** *\*most the books*. I didn't search this. Informal *most the time* (from memory, unverified) is the kind of line a referee would find. A register scope, if Brett wants one: `(\ungram{\mention{most the books}} in standard English)`.
- **l.99** "with \mention{some of the people}, by contrast, plural agreement is the only option". This negative has *CGEL*'s number-transparency description behind it but no star. To match l.91, add `(\ungram{\mention{Some of the people was waiting}})`.
- **l.297** "\mention{several} ... excludes peripheral \mention{a}". *CGEL* p. 392 contrasts *several* with *a few* (on *quite*, *not*, *only*) but doesn't state *\*a several*. Add `(\ungram{\mention{a several mistakes}})` if wanted.
- **l.760** "The articles and \mention{every} have no such use (\ungram{\mention{an every}})". The articles have no starred form, and metalinguistic *thes* sits outside the fragment (l.615), so leaving them unstarred is defensible. The string *an every* matches once in `corpus/exclusion_tests/coca_every_v.jsonl` (n 42, CNN 2013, "It's an every" cut off at the KWIC edge after "it's every , it's --"). It reads as an attributive compound (*an every-[...]*), not the set-denoting use. No repair.
- **l.732** (not a negative; corpus awareness). A separate D carrying a nominal feature has a precedent in Brett's literature: Grimshaw (1991), as reported by `literature/Baker2004_Lexical_categories.md` ("the functional heads associated with nouns (such as determiner) bear nominal features"). Citing it would keep the alternative from reading as the paper's own construction. Van Eynde (2003, introduction) also draws the Pullum and Wilson (1977) auxiliary parallel explicitly ("This text makes a similar case for the determiners"), which bears on l.87.

## Negatives checked and standing

| Line | Negative | Basis found |
|---|---|---|
| 29, 111 | grade and degree profile "confined to" the four | *CGEL* 393–395, 431–432; starred forms; COCA check of *very every/some/this* (7 lines, none qualify; supplement exclusion table) |
| 71 | novelty "relative to those accounts" | narrowed yesterday; inward search rerun (below) |
| 89, 119, 123, 163 | "don't determine / doesn't distinguish / don't add evidence" | method and scope statements, argued in place |
| 113 | *\*very a few*, *\*a quite few* | COCA zero hits (`exclusion_tests/log.md`; supplement Table "Checks of stated exclusions") |
| 135 | complementary distribution "alone doesn't assign category" (Payne et al. 2010: 61) | confirmed on printed p. 61 ("factors other than simple distribution are the crucial ones") |
| 137 fn | *CGEL* p. 417 examples "all occur in coordinated contrasts" | confirmed: [25]–[27] are all coordinated |
| 180 | *rich* needs *the* on the generic reading | *CGEL* 417–418 |
| 245 | Van Eynde: determiners "form no category of their own" | confirmed, his §3: "Determiners do not belong to a separate functional category" |
| 295 | modifier in *a great many* obligatory | *CGEL* 394: "one or other of these adjectives is required" |
| 299 | *CGEL* "declines to let semantic motivation alone establish a complex unit" | *CGEL* 621 |
| 397 fn | *few would*: 82 of 94 with no set | `few_would.reading.md`, read by Brett 2026-09-18 |
| 546, 657 | compounds exclude external determination and a pre-head adjective "as determinatives" | corpus attestations reassigned to the set-denoting use by an independent criterion (loss of quantificational force, l.754); supplement records the restatement |
| 730, 734 | "rather than costs established for every separate-D grammar"; "doesn't establish a strict description-length advantage" | scope negatives about the paper's own audit; appropriate |
| 760 fn | "a judgment I haven't tested" | the honest form |
| 774 | "the study contains no common or proper nouns" | checked yesterday |
| 808 | "they don't all specify a surface taxonomy" | Table 6 rows |

## Inward search behind the §1 novelty claim (l.71)

The claim stays narrowed to the accounts the paper surveys, so no outward search was run. Rerun today over `literature/*.md` (1,538 files; none newer than yesterday's report):

- yesterday's three regexes: `determin(er|ative)s? (are|as) (a )?(noun|pronoun)s?\b`; `determin(er|ative)s?[^.]{0,40}(sub-?class|sub-?categor|subtype|kind|species|type) of (noun|pronoun)`; `(noun|pronoun)s?[^.]{0,20}(include|including|comprise)[^.]{0,30}determin(er|ative)s`. New hits since yesterday's list were all false positives: *Events and Grammar* ("any kind of noun"), Buder-Gröndahl 2024 (DP hypothesis), *SIEG2* (determinative lists), Quirk et al. 1985 (determinative elements), Remijsen (Shilluk modifiers).
- new today: `quantifiers? (are|as) (a )?nouns` (0 hits); `determiners? (are|is) (a )?(kind|type|sort) of noun` (0); `determinatives? (are|is) (a )?(kind|type|sort) of noun` (0); `D (is|as) (a )?\[\+N` (0); `articles? (are|as) (a )?(noun|pronoun)s` (Sommerstein 1972, already in Table 6); `pronouns? (are|as) (a )?determin` (*CGEL*, Hudson 2000 and 2004, Quirk); `nominal (category|feature)[^.]{0,60}determin` and its mirror (Lyons 1999, false positive; Baker 2004, which reports Grimshaw's nominal features on D, see the optional l.732 note); `extended projection` (15 files, including Baker 2004 and Hudson 2000, all of them the Grimshaw functional-feature idea, not a lexical taxonomy).
- `lit co-cited hudson2004determiners` and `lit co-cited vaneynde2003determiner`: every held co-citation is already in the paper. The first also lists `anderson1997notional` (John Anderson, *A notional theory of syntactic categories*), which is in the central bibliography but not held in `literature/`. It's an unverified lead for Appendix A. From memory, and unchecked, Anderson's notional grammar treats determiners and names as a functional category defined by the N feature. I can't confirm this without the text.

No account in the corpus proposes the four coordinate subcategories; the claim as worded ("Relative to those accounts") needs nothing further.

## Disposition (parent session, same day)

Applied: 1 (*a certain*: l. 311 now says none of the four remains a complex determinative, sets *a certain* aside with CGEL p. 393, and l. 740 says "the four complex determinatives analysed here"; CGEL p. 393 checked: "it may be best to treat a certain as a complex determinative"), 2 (head genitive: applied through the charitable-engagement pass's wording).

Held for Brett: 3 (unstarred, unsourced "exclamative *what* has no predicative use": needs his judgment and example, or a cut), 4 (*the hurt can not be much* listed among amount-denoting subjects although *hurt* isn't one and the frame is the one Solt stars; the agent's note that the line is Shakespeare is from memory and unverified), 5 (independent *every*; see the measurement audit, M1).

## Item 4 resolved by evidence, 19 September (evening)

Brett ran two COCA searches with their query strings recorded and pasted the displays: `[x*] [be] much .` (30 texts) and `[be] [x*] much .` (198 texts), both saved in full under `corpus/independent_argument/`.

- **The *hurt can not be much* example is Shakespeare**, as the pass suspected from memory and now confirmed from the data: four of the 30 lines are the same line of *Romeo and Juliet* (Mercutio, "Courage, man; the hurt can not be much"), reaching COCA through two films, a screenplay and a fiction text. It is out of §2.2 and out of the quantifier supplement, with a footnote saying why.
- **Solt makes no polarity stipulation.** Her (76) stars the negated entity-subject cases outright (\**John's patience is little/is much/isn't much*), and her parenthetical says she includes the negated form "to show that its infelicity is not due entirely to its NPI-like character". Her condition is the subject's semantic type, her (77) *The amount of water in the bucket was little/wasn't much*.
- **The 198-text set therefore bears on her stated condition**: bare predicative *much* under negation occurs at volume with subjects denoting no amount (*The town isn't much*, *her resume wasn't much*, *The Bahamas really aren't much*). §2.2 now reports that, with the evaluative reading tied to *CGEL*'s *Kim isn't much of an actor* (p. 415, a degree quantifier over a property, strongly non-affirmative), which also settles held item 3 of the source reread.
- **Neither query bears on affirmative predicative *much***, since both require a negator. The 18 September batch of 81 entries was recorded only as "sentence-final *be much*" and its note records affirmative-looking hits that are sentence-splitting artefacts ("it's much. much cheaper"); the query string is still unrecorded.
