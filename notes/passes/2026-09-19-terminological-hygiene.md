# Terminological hygiene, 19 September 2026
<!-- SUMMARY: report-only pass over the working tree (sha256 05d22789..., HEAD af63c84 plus uncommitted edits); 17 defects with minimal repairs (two regressions of yesterday's fixes, two permission/condition slips, projection and D-noun used for the Head analysis, NP-modifier ambiguity, a second sense of domain), one analytical flag for Brett (peripheral a versus predeterminer many), 7 optional preferences; term gate fails on three abstract terms · status: report-only, repairs proposed, none applied · updated: 2026-09-19 -->

Procedure: the registry's `terminological-hygiene` entry (mechanical gate, then the judgment layer). Baseline: `2026-09-18-terminological-hygiene.md` and its ledger `planning/terms.md`. Scope: whole manuscript, with attention to the paragraphs in `2026-09-19-incremental/changed-paragraphs.txt`. Model: Claude Opus 5.

**Report-only.** Nothing in the manuscript, the ledger, `amendments.json`, or `.passes.jsonl` was changed. Every "old" string below was checked to match exactly once.

**Text inspected.** `determinatives-as-nouns.tex`, 841 lines, sha256 `05d22789d4ec968c3045540c69a30e49b2ba57ab1f75d9c2c4280f027f1b5c97` (HEAD `af63c84` plus uncommitted edits). Another session modified the file at 15:54:54 while this pass ran: the Hudson row of Table 7 (l.819) changed from "His determiner category within pronoun, which is within noun" to "Determiners as pronouns with a common-noun dependent, not a separate class; pronoun within noun". The line count didn't change, and all targets were re-verified against the hash above at 16:00.

Each defect is marked *new* (introduced since commit 6e86966, the state yesterday's pass left) or *older* (present then, missed by yesterday's pass).

## Mechanical layer

`check-terms.py determinatives-as-nouns.tex --gate --ledger planning/terms.md` **fails** on three abstract terms: *nominal*, *determiner*, *domain*. The first two need only ledger rows (see the end of this report). *Domain* needs a text repair first (D10), because the abstract uses it in a sense the body never glosses.

## Local contrasts and terms ledger (updated)

| Term | Sense the paper fixes | First use / gloss | Today |
|---|---|---|---|
| determinative / determiner | category / function | l.29 abstract; gloss l.44 | Held throughout. Gate needs a ledger row for *determiner*. |
| Noun (capital) | superordinate category; "existing/established Noun" for *CGEL*'s | l.40 | Held; l.819 now writes Hudson's category "noun" beside "Noun" at l.766 and l.818 (O4). |
| dependent / independent (use) | with / without a nominal target | gloss l.48 | Held. Ordinary-sense *independent* is back at l.73 (new) and l.285 (D13). Extension to adjectives in §2.4 (l.202 to 206) reads naturally. |
| D-noun categorization / D-noun analysis; bare *D-noun* = categorization | l.52 | gloss l.52 | Two leaks where bare *D-noun* carries an ordinary-Head claim (D7). |
| ordinary Head / ordinary headedness / ordinary-Head analysis | Head alone, no fused function | gloss l.50 | Held, but "ordinary fused Head" at l.281 pairs the names of the two rival analyses (D12). "full Head chain" (l.714) and "direct Head chain" (l.716, 726) sit a sentence apart; transparent, left. |
| Head analysis | the ordinary-Head-versus-fusion question | Table 1 caption, l.71 | l.257 calls this question "the projection" (D5). |
| projection | the phrase a word heads; *NP/DP projection* = that phrase's category | l.54; gloss now l.329 | Gloss moved from §1 to §4.1 with the unique-parentage paragraph, so the ledger row is false (D6). Third sense at l.257 (D5). |
| nominal (Nom) | *CGEL*'s layer inside NP | l.48, l.50; notation l.81; gloss l.325 | Held. Gate needs a ledger row. |
| fusion; Det–Head, Mod–Head | a dependent function fused with Head | l.50 | Abstract calls *the lucky few* determiner–Head fusion; Table 3 has Mod–Head (D8). |
| inheritance | constraints stated for Noun apply to its subcategories | gloss l.391 | l.546 (new) uses *inherits* for what a compound takes from its base lexeme (D11). l.732's inheritance within D in a separate-D grammar is a natural extension. |
| inherited nominal feature | one feature assigned to Noun and to D, inherited within each | l.29; l.732 | New today and consistent: "inherited nominal feature", "nominal feature ... with inheritance", "the feature", "the inherited feature" name one thing. |
| category condition / Noun condition | the condition on $\operatorname{Cat}(h)$ for a word filling Head in Nom; *Noun condition* is its D-noun value, separate D adds a disjunct | gloss l.642 to 649 | Yesterday's repair regressed: abstract "broader head condition" (D1); new "lexical-head condition" at l.732 (D2). l.651 "derivations" imports procedural vocabulary (D14). |
| use permission / condition | which functions a lexeme's phrase may fill / what its dependents and target must satisfy | gloss l.590, l.623 | Two slips (D3, D4). l.615's "separate modifier permission" (new) **is** a use permission (peripheral Mod function), consistent with the reservation and with DECISIONS 2026-09-19; the collocation is the one yesterday's pass removed in the other sense (O1). l.617, 663, 679 correct. |
| peripheral (modifier) | *CGEL*: external modifier "before any predeterminer"; paper's gloss: any modifier outside the NP's internal dependents, before its determiner | first l.113; gloss l.486, l.640 | Used about 15 times before the gloss, and the gloss is broader than *CGEL*'s term, so it also covers predeterminer *many* (flag B1). "peripheral NP modifiers" parses two ways (D9). |
| predeterminer (modifier / function) | *CGEL*'s other external modifier | l.163; l.303 quotation, l.305 | "predeterminer membership" treats a function as a category (D15). Relation to *peripheral*: B1. |
| internal (modifier, attachment) | inside Nom | l.113; l.325, l.484 | Held. |
| NP modifier | a modifier realized by an NP (l.510, 689, 693, 702, 738) | l.510 | Clashes with "peripheral NP modifier" = modifier peripheral to NP (D9). |
| restrictor | Payne, Huddleston and Pullum's post-head, non-recursive modifier function in compounds | gloss l.518 | Held; checked against the source (below). |
| secondary (set-denoting) use / conversion | the set-denoting use itself, neutral about category; *conversion* is *CGEL*'s label for the compound case only | l.29; §6.1 l.750, l.758 | No drift. Yesterday's row ("secondary use within a category") was too narrow: *CGEL*'s own cardinal secondary use changes category (quoted l.756), and l.730 and l.760 correctly speak of category change *for* secondary uses. §6.1 alternates "rule" and "schema" (O2). |
| domain | **partitive** domain, glossed with `\term` at l.95 | l.29 abstract; gloss l.95 | New second sense (the set of words a rule covers): l.29 ×2, l.734 ×2, l.740, l.794 ×2 (D10). "Modifier domain(s)" (§4.5, l.552, 712, 716) is a fixed compound; left. |
| quantifier | across categories (l.95) | l.29, l.44; gloss l.95 | Abstract's "with the quantifiers" excludes the quantificational nouns the gloss includes (D16). |
| fragment | a set of conditions on specified constructions | l.71; gloss l.566 | Used at l.71 and l.393 before the gloss; l.393 also makes the fragment an agent (O5). |
| implementation / account / grammar / combination | the four stated versions / the general type | l.54, 71, 73 | New contrast in §5.6: *implementation* (stated, audited) against every separate-D *grammar* (l.730), but l.732 calls the same family an *account* (O3). |
| profile | functions, dependents, forms, meanings of a category's members | gloss l.87 | Held; ledger should say §2 (was §1). |
| target | the nominal determined or modified | l.48; l.617 | Held. |
| external | (a) function of the whole phrase (l.89, 119, 623, 691); (b) outside Nom (external determiner, determination) | | No collision within a sentence; noted only. |

## Defects, with proposed repairs

Ordered by importance.

**D1 (new; regression).** l.29 abstract.
Old: `through a broader head condition or an inherited nominal feature`
New: `through a disjunct in its category condition or an inherited nominal feature`
Reason: yesterday's pass aligned the abstract with §5.2's *category condition*; today's rewrite introduced a fourth name for it, and "broader" doesn't say how.

**D2 (new).** l.732.
Old: `The lexical-head condition and head-genitive definition could each refer to that feature`
New: `The condition on lexical Heads in Nom and the head-genitive definition could each refer to that feature`
Reason: another unratified name for the same condition. l.726, 730, and 794 already say "condition on lexical Heads in Nom"; lowercase *head* also points at the word, not the function.

**D3 (older).** l.653.
Old: `These permissions don't transfer to \mention{every} or the articles.`
New: `These dependent conditions don't transfer to \mention{every} or the articles.`
Reason: the antecedent is the dependents independent *some* and *few* admit (partitives, relatives, determination, premodification). Those are conditions; §5.1 reserves *permission* for use permissions. Yesterday's twelve repairs missed this one.

**D4 (older).** l.663.
Old: `The article's exclusion from argument use remains a separate condition.`
New: `The article itself lacks argument permission (Table~\ref{tab:permissions}).`
Reason: by Table 4 and the three checks of l.623, being excluded from a function means lacking a use permission, not failing a condition.

**D5 (older; paragraph reworded today).** l.257.
Old: `The projection, ordinary Head or fusion, is the question of`
New: `The Head analysis, ordinary Head or fusion, is the question of`
Reason: elsewhere *projection* is the phrase a word heads (l.329) or that phrase's category (NP versus DP: Table 5, l.629, 638, 706), and Table 5's fused D-noun row pairs NP projection with fused Head, so the two questions are independent. Table 1 and l.71 already call this question the Head analysis.

**D6 (regression of a ledger claim).** l.54 and l.329.
Old (l.54): `a noun's projection can fill a fused function`
New: `a noun's projection, the phrase it heads, can fill a fused function`
Old (l.329): `the determinative's projection, the phrase it heads, needs no such join`
New: `the determinative's projection needs no such join`
Reason: the ledger says *projection* is glossed at its first body use in §1. The gloss moved to §4.1 with the unique-parentage paragraph. (Alternative: leave the text and change the ledger row to "glossed l.329".)

**D7 (older; l.426 reworded today).** Bare *D-noun* used for the analysis.
Old (l.331): `Independent \mention{some} has ordinary Head under D-noun;`
New: `Independent \mention{some} has ordinary Head under the D-noun analysis;`
Old (l.426): `Under D-noun, \mention{few} heads an ordinary NP`
New: `Under the D-noun analysis, \mention{few} heads an ordinary NP`
Old (l.388, caption): `and D-noun (second pair)`
New: `and the D-noun analysis (second pair)`
Reason: l.52 fixes bare *D-noun* as the categorization. Table 1's fourth row (D-noun, fused Head) gives independent *some* Det–Head and *the few* Mod–Head, so both claims are true only of the analysis. The figure panel is already headed "D-noun analysis".

**D8 (older).** l.29 abstract.
Old: `I replace the grammar's fusion of determiner and Head functions with ordinary Head relations`
New: `I replace the grammar's fusion of determiner (or modifier) and Head functions with ordinary Head relations`
Reason: the sentence's second example, *the lucky few*, has Mod–Head fusion in *CGEL* (l.428; Table 3), not determiner–Head fusion.

**D9 (older).** "NP modifier" parses two ways.
Old (l.578): `Peripheral NP premodifiers` → New: `NP-peripheral premodifiers`
Old (l.712): `distinguish peripheral NP modifiers from` → New: `distinguish NP-peripheral modifiers from`
Old (l.780): `Both groups permit peripheral NP modifiers` → New: `Both groups permit NP-peripheral modifiers`
Reason: elsewhere an *NP modifier* is a modifier realized by an NP (l.510, 689, 693, 702, 738), so "peripheral NP modifier" reads as a peripheral modifier that is an NP. l.484's *NP-peripheral* is unambiguous and already in the text.

**D10 (new; also the gate failure).** Two senses of *domain*.
Old (l.95): `quantify over a partitive \term{domain}:`
New: `quantify over a \term{partitive domain}:`
Plus a ledger row making bare *domain* free in its ordinary sense (the set of words a rule or category covers).
Reason: the `\term`-glossed sense is the partitive one; seven uses new today (l.29 ×2, l.734 ×2, l.740, l.794 ×2) use the word for a rule's coverage. Narrowing the gloss invalidates no earlier use (only the abstract precedes it), and the later bare partitive uses (l.208, 407, 411, 617) all sit in partitive context. Alternative, if Brett wants one sense per word: replace the seven rule-sense uses with *range*.

**D11 (new).** l.546.
Old: `inherits nominal projection from Noun and its premodifier conditions from its determinative base`
New: `inherits nominal projection from Noun and takes its premodifier conditions from its determinative base`
Reason: l.391 glosses inheritance as taxonomic (Noun to its subcategories). A compound's base lexeme isn't its supercategory. l.550 and l.657 already say the base "supplies" these conditions.

**D12 (older; paragraph reworded today).** l.281, text and footnote.
Old: `\mention{every} never stands as an ordinary fused Head` → New: `\mention{every} never stands as a straightforward fused Head`
Old: `shows an ordinary fused-head use` → New: `shows a straightforward fused-head use`
Reason: *ordinary* is the technical name for the non-fused Head analysis, so "ordinary fused Head" joins the names of the two rival analyses.

**D13 (l.73 new; l.285 older).** Ordinary-sense *independent*.
Old (l.73): `The paper advances two independent claims.` → New: `The paper advances two separable claims.`
Old (l.285): `they aren't three independent reasons` → New: `they aren't three separate reasons`
Reason: yesterday's pass removed this kind of use in §5.5 because the technical *independent* is glossed at l.48. *Separable* matches §2.6's "Four separable questions" and l.54's "Neither commitment requires the other".

**D14 (older; minor).** l.651.
Old: `The coverage audit marks the derivations that go through it`
New: `The coverage audit marks the cells that use it`
Reason: §5 is constraint-based (l.566; "no sequence of fusion operations assumed", l.677). The audit records cells (l.730: "the audit's 32 Dn cells record applications of this single condition"), and `coverage-audit.tex` never uses *derivation*.

**D15 (older; minor).** l.307.
Old: `as predeterminer membership is anyway`
New: `as admission to predeterminer function is anyway`
Reason: predeterminer is a function; *membership* elsewhere is category membership (Noun membership). This is a category/function slip.

**D16 (older; minor).** l.29 abstract.
Old: `restricted dependents with the quantifiers`
New: `restricted dependents with determinative quantifiers`
Reason: l.95 defines *quantifier* across categories, which makes quantificational common nouns quantifiers too.

**D17 (new, edited during this pass; minor, canon-adjacent).** l.819, Table 7.
Old: `not a separate class`
New: `not a separate category`
Reason: canon `category-not-word-class`. Its regex (`word[- ]class|parts? of speech|lexical class`) doesn't catch bare *class*, but the row uses it for a lexical category.

## Flag for Brett: *peripheral a* against *predeterminer many* (no wording proposed)

§3.2 and the conclusion rest on a contrast between two function names: "peripheral \mention{a}" and "predeterminer \mention{many}" (l.277, 297, 311, 661, 740, 796: "peripheral modification by *a* and predeterminer modification by *many*"). As the paper currently glosses them, the two terms don't separate:

- *CGEL* treats both as **external modifiers**. Predeterminers are one type (§12, p.433: "Predeterminer modifiers, or predeterminers, are one type of external modifier"). Peripheral modifiers occur "at the periphery of the NP, mainly in initial position (before any predeterminer)" (§13, p.436), in six semantic types (focusing, scaling, and so on). At p.392 *CGEL* calls *quite* "the peripheral modifier *quite*" (checked in `literature/00-CGEL.md`), so l.113's attribution holds for *quite*.
- The paper's gloss (l.486: peripheral modifiers "attach outside an NP's internal dependents" and "precede any determiner belonging to the NP they modify") and its third structural condition (l.640) fit predeterminer *many* in *many a man* just as well. On those definitions, predeterminer modification is a case of peripheral modification, not a sister of it.
- In *quite a few mistakes*, *a* sits after peripheral *quite* and before the determiner *few*. By *CGEL*'s ordering, that is the predeterminer position, so the extension of *CGEL*'s term to *a* is unmarked.
- *Peripheral* is also used about 15 times (l.113, 163, 231, 277 to 311) before its gloss at l.486.

A candidate repair that leaves the analysis alone: use *CGEL*'s cover term *external modifier* in the l.486 gloss and in l.640's third condition; keep *peripheral* and *predeterminer* as *CGEL*'s two subtypes; add one clause in §3.2 stating what puts *a* with the peripherals rather than the predeterminers; and add a pointer (§\ref{sec:payne}) at l.113. The criterion is Brett's to state: DECISIONS 2026-09-19 records his analysis ("few as the Determiner with a as a peripheral modifier"), and this pass doesn't question it, only whether the terms as glossed can carry it.

## Optional preferences

**O1.** l.615. Old: `has a separate modifier permission` → New: `has a separate use permission as peripheral modifier`. The sense is already correct (a use permission). The rewording keeps readers from taking it as the "modifier permissions" (dependent conditions) that yesterday's pass removed.

**O2.** l.758, l.760. Old: `The rule can be stated once` → New: `The schema can be stated once`; Old: `Within Noun the rule has three inputs` → New: `Within Noun the schema has three inputs`. l.760 currently uses "rule" and "schema" in adjacent sentences for one thing; elsewhere it's "schema" (l.73, 732, 736, 746, 796).

**O3.** l.732. Old: `A separate-D account could instead` → New: `A separate-D grammar could instead`. This matches l.730's contrast between "the implementation compared" and "every separate-D grammar" (and l.391), keeping *account* for the four stated versions.

**O4.** l.819 (edited during this pass). Old: `pronoun within noun` → New: `pronoun within Noun`, matching l.766 ("inside Noun") and the *CGEL* row above it.

**O5.** l.393. Old: `The fragment compares the remaining selectional conditions (§\ref{sec:det-uniform}).` → New: `Section~\ref{sec:det-uniform} compares the remaining selectional conditions.` The current wording uses *fragment* before its gloss (l.566) and makes it the agent of the comparison.

**O6.** l.653. Old: `ordinary \mention{some} and \mention{few} exclude` → New: `dependent \mention{some} and \mention{few} exclude`. *Ordinary* again sits two paragraphs after "ordinary-Head accounts" (l.640, 651), and *dependent* is the defined term.

**O7.** l.752. Old: `Under the D-noun analysis no category change is involved` → New: `Under the D-noun categorization no category change is involved`. The categorization is what does the work here; the analysis isn't wrong, only broader than needed.

## Canon and imported terms

**Canon.** No *word class*, *part of speech*, *lexical class*, *mass*, *predicate*, *subjunctive*, or *aspect*. *Determinative* is the category and *determiner* the function throughout; *determiner* as a category word occurs only for Van Eynde's and Hudson's categories, each attributed. *DP* is *CGEL*'s determinative phrase (l.79). Bare *class* at l.819 (D17).

**Imported terms.**
- *Restrictor*: Payne, Huddleston and Pullum (2007) call it "a specialized modifier function, termed the 'restrictor' function; this function is non-recursive and can only be realized by constituents in post-head position", and their tree (13d) labels *present* "Mod". The paper's l.518 gloss, Figure 5's Mod labels, and the caption's "Both post-head Mod positions realize the specialized restrictor" follow them. (Yesterday's artifact attributes the term to "Payne and Huddleston 2007"; the bibliography entry `Payne2007` has three authors. The manuscript cites the key and renders correctly.)
- *Peripheral modifier*: *CGEL*'s term, broadened without marking (B1).
- *Predeterminer modifier*: *CGEL*'s, quoted at l.303.
- *Fusion of functions*, *number-transparent*, *head genitive*: *CGEL*'s senses.
- *Functor* and *marking*: attributed to Van Eynde at l.249.

## Proposed rows for `planning/terms.md` (not applied)

| Term | Status | Where glossed / why free |
|---|---|---|
| determiner | free | *CGEL*'s function term, owned by the assumed reader; the category/function distinction is glossed at l.44 (§1) |
| nominal | free | *CGEL*'s Nom layer; notation l.81, gloss l.325 (§4.1) |
| domain | free (after D10) | ordinary sense in the abstract, §5.6, and the conclusion (the set of words a rule or category covers); the technical term is *partitive domain*, glossed at l.95 |
| projection | update | if D6 is applied, "glossed at first body use, l.54 (§1)"; otherwise "glossed l.329 (§4.1)" |
| quantifier | update | defined in §2.1 (l.95), not §2.2 |
| profile | update | glossed at first body use in §2 (l.87), not §1 |

## Noticed outside this pass

Two anaphors in reworded §2.2 paragraphs reach back across corpus paragraphs: l.133 "That unity" (antecedent: Solt's one semantics, l.127) and l.135 "The same relation". This is reader-pass material, not terminology.

## Disposition (parent session, same day)

Applied: D1, D2, D3, D4, D5, D6, D7 (l. 331, l. 426, and the Figure 1 caption, with "In the D-noun pair" shortened to "In the second pair"), D9, D10 (the term at l. 95; the ledger row for bare *domain* is left to the ledger's owner), D11, D13, D14, D15, D16, D17. D8 and D12 were already applied through the level-category audit (as "fusion of Head with a determiner or modifier function" and "ordinary independent use").

Held for Brett: B1 (whether peripheral *a* and predeterminer *many* need CGEL's cover term "external modifier" and a criterion in §3.2) and the optional items.

## Second round, same day: *nominal* reserved for the Nom layer

Brett's instruction: "use nominal only for the category between N and NP", with "be flexible, choose as appropriate, see what CGEL would do".

What CGEL does, checked in its text: *nominal* is the Nom category and appears as a noun ("a nominal", "the nominal", "head nominal", "composite nominal"). For the noun-like sense it writes "properties of nouns" (5 occurrences), "noun-like" (2), "noun properties" (1). It does not use *nominal* as an adjective meaning "of nouns".

Applied on that model, 40 changes in three groups:

- **Kept** (about 20): the Nom sense, as in "a \term{nominal} (Nom) contains a head and its internal dependents", "before another nominal", "the understood nominal description", "internal nominal modification".
- **Named as the phrase or the layer** (14): "nominal projection" became NP projection; "nominal structure" became Nom structure, "inside Nom", or "structure within the nominal", according to which was meant; "the same nominal layers" became "the same Nom layers".
- **Rephrased in CGEL's idiom** (26): "each nominal property" → "each property of nouns"; "the nominal profile of §2.1" → "the properties of nouns set out in §2.1"; "The nominal connections recur" → "The connections with nouns recur"; "nominal premodifiers" → "noun premodifiers"; "are nominal arguments" → "are NP arguments"; "the nominal grouping" → "the grouping with nouns"; "a nominal feature" → "the same feature"; §2.5's title lost "nominal independence" for "independent use".

The abstract changed in two places ("consolidate the rules stated for nouns"; "an inherited feature").

### Register consequence

The sweep broke 31 hash-pinned quotations. All were re-anchored in `analysis/manuscript-census-2026-09-14/amendments.json` (20 claim amendments, 11 `_evidence` span rewrites), each derived from the substitution that caused it, never from a fuzzy match. Three of those were stale before this sweep, from earlier repairs today: the *such* reclassification, Payne et al.'s *almost* hedge, and the replacement of *the changes globally to the climate*. One more chained a pre-publication repair ("NPs containing fused-head adjective phrases") that had not been carried through. `check_sources.py` now reports 1,422/1,422 resolving, and all four generated-table checks pass.
