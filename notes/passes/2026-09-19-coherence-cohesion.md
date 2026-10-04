# Coherence and cohesion pass, 19 September 2026

<!-- SUMMARY: spine mapped for all 25 sections (every line writable); nine join repairs proposed as CriticMarkup for approval, none applied: two vague antecedents in §2.2, an orphan sentence before Table 2, an unlinked Van Eynde turn, Hudson interrupting the permission checks, an unmarked turn to numerals in §5.4, one duplicated verdict across §5.5/§6.1, and two small joins · status: proposals for Brett · updated: 2026-09-19 -->

Text: `determinatives-as-nouns.tex` after commit af63c84 with the 19 September quote-audit repair. Procedure: the registry's `coherence-cohesion` entry (spine first, then a three-paragraph sliding window, edits delivered for approval). Model: Claude Opus 5, one reader over the whole text in order (no per-section fan-out; the text had just been read end to end for the projectibility audit). Today's reader pass (current on the board) covered first uses and cross-references; this pass looks only at joins, antecedents, duplicated verdicts, and unmarked turns.

## 1. Spine

| § | Question it answers | What it establishes |
|---|---|---|
| 1 | What is the categorial relation among *some*, *me*, *apple*, *Brett*? | Two separable choices (taxonomy, Head analysis), four combinations, the category/function terms, what's new, the roadmap. |
| 2 | How should determinatives be compared with Noun and Adjective? | Compare whole profiles; weigh breadth, recurrence, specificity; four evidence types. |
| 2.1 | What connects quantificational common nouns with determinatives? | Partitives, number transparency, restricted dependents, degree modifiers; *each* agreement as variation. |
| 2.2 | What is the adjectival profile, and how far does it reach? | Grade + degree selection + comparative complements for the gradable four; approximatives are NP-general; predicative uses and Solt's semantics don't decide category. |
| 2.3 | Do inflection and reference connect determinatives with nouns? | Partially: demonstrative number, compound head genitives, pro-form gender. |
| 2.4 | Do determinative expressions share nominal functions? | Argument, Det, modifier and adjunct functions, relatives, post-head adjectives. |
| 2.5 | Is independent use just quantity meaning? | No: *numerous* etc. overlap; independent use alone would be circular. |
| 2.6 | Which profile wins? | Nominal connections recur more widely; Van Eynde's split declined; Noun favoured. |
| 2.7 | What else is separable? | Category, projection, semantic type, construction. |
| 3 | How can restricted members be included? | Two-stage argument for articles; *every*; Spinillo. |
| 3.2 | What happens to complex determinatives? | *a few* etc. reanalysed with peripheral *a*; *many a*, *such a*, *what a* as predeterminers. |
| 3.3 | How are dependent/independent forms handled? | *no*/*none* as form selection. |
| 4 | Ordinary Head or fusion? (framing) | Compared in three constructions. |
| 4.1–4.6 | Head relations; completeness; partitives; modifiers; compounds; genitives | One Head chain across uses; modifier domains preserved; genitives extended. |
| 5 | What does each of four implementations state? (framing) | Table 6. |
| 5.1–5.4 | Scope and permissions; constraints; degree uses; comparison | Shared conditions; category condition; degree uses as NP modifiers; the trade-off. |
| 5.5 | What does the taxonomy add? | Profile supports Noun; the inherited-feature alternative shares the rules; no strict length advantage. |
| 6.1 | Secondary set-denoting uses | One schema over three inputs. |
| 6.2 | Coordinate or nested? | Coordinate preferred; nesting coherent. |
| 7 | Conclusion | Mirrors 2–6. |

Every line could be written. No section lacks a question.

## 2. Proposed repairs (CriticMarkup, not applied)

Each item gives the line, the problem, and the edit. Defects first.

### C1. l. 133: "That unity" points three paragraphs back (defect)

"That unity" means Solt's single semantics (l. 127), but l. 129 and l. 131 (the predicative *much*/*little* evidence) intervene, and l. 131 ends on *Kim isn't much of an actor*.

> {~~That unity is the semantic side~>Solt's unified semantics is the semantic side~~} of this adjectival profile, and it sits as well with Noun as with Adjective: the same four carry the nominal profile of §\ref{sec:quant-nouns}.

### C2. l. 135: "The same relation" has no clear referent (defect)

The intended relation is "doesn't decide category" (semantic unity is compatible with both categories); the sentence reads as if some relation had been named.

> {~~The same relation holds between distribution and category.~>Distribution likewise leaves category open.~~} \textcite{reynolds2024why} explains why ...

### C3. l. 214: orphan sentence between the table's introduction and the table (defect)

"Proper names permit nominal premodifiers such as *architect Norman Foster*" stands alone after the paragraph that introduces Table 2 and before the table. It is the source for one cell (proper noun, "Restricted AdjP and nominal premodifiers"). Fold it into the introducing paragraph:

> ... where they attach is the analysis of §\ref{sec:payne}.{++ The proper-noun cell rests on premodifiers such as \mention{architect Norman Foster} \citep[517--518]{huddleston2002}.++}
>
> {--Proper names permit nominal premodifiers such as \mention{architect Norman Foster} \citep[517--518]{huddleston2002}.--}

### C4. l. 623: "listed above" now points past two Hudson paragraphs (defect)

The three-check paragraph refers to the uses in Table 5, but l. 619–621 (Hudson on dependency and reciprocal selection) intervene.

> In the external uses {~~listed above~>of Table~\ref{tab:permissions}~~}, an expression has to pass three checks: ...

(Alternative, larger: move l. 619–621 after l. 623, so the permission description is continuous and Hudson follows it as a comment on headedness. The one-phrase fix is enough.)

### C5. l. 736 and l. 760: the same verdict twice, each pointing at the other (duplicated verdict)

l. 736 (§5.5): "With *CGEL*'s categories the compound and cardinal inputs change category; a separate-D account can share the schema as just described." l. 760 (§6.1): "With separate D and *CGEL*'s output categories, the compound and cardinal inputs change category; a shared schema can still state their common behaviour (§5.5)." l. 732 already says the feature account's "One secondary-use schema could cover the same three input types, with category change specified for the D inputs". l. 736 also describes §6.1's content before the reader reaches it. Cut l. 736; §5.5 keeps the point at l. 732 and §6.1 keeps it at l. 760.

> {--The secondary set-denoting use of §\ref{sec:secondary-use} covers names, compound determinatives, and cardinals within Noun. With \textit{CGEL}'s categories the compound and cardinal inputs change category; a separate-D account can share the schema as just described.--}

If cut, l. 738's "can likewise be stated once" still reads correctly after l. 734.

### C6. l. 718: unmarked turn from the four-way comparison to numerals and *one* (join)

§5.4 compares the implementations through l. 716, then l. 718–722 turn to numeral and *one* categorization without saying why. The reason is Table 6's "Taxonomic consequences" column. A clause makes the turn:

> {++The taxonomic column of Table~\ref{tab:economy} concerns numerals and \mention{one}.++} \textcite{reynolds2026numerals} distinguishes determinative numerals ...

### C7. l. 245: Van Eynde arrives without a link to the weighing (join)

l. 243 sets the two profiles side by side; l. 245 starts on Van Eynde's Italian and Dutch argument; only at l. 247 does the reader learn that his criterion would split the English inventory along those profiles. A link at the start:

> {++One alternative divides the inventory between the two profiles.++} \textcite{vaneynde2003determiner} argues from Italian and Dutch that determiners form no category of their own: ...

### C8. l. 279: "instead" contrasts with a paragraph two back (join, optional)

"Spinillo ... instead retains *the*, *a*, and *every*" follows the peripheral-*a* paragraph (l. 277), but the contrast is with l. 271–273 (articles within the determinative system).

> \textcite[153--158]{spinillo2004reconceptualising} (earlier \citealp{spinillo2000determiners}) {~~instead retains~>separates the articles from that system: she retains~~} \mention{the}, \mention{a}, and \mention{every} as an expanded article category ...

### C9. l. 762: one-sentence orphan closing §6.1 (join, optional)

The locative-compound sentence forestalls a misreading of the schema but stands alone after the footnoted l. 760. Join it to l. 760, before the footnote:

> ... a shared schema can still state their common behaviour (§\ref{sec:overall-assessment}).{++ Locative compounds before a noun (\mention{an anywhere operation}) are a different case, the ordinary noun-as-modifier use, with the article belonging to the head noun.++}\footnote{...}
>
> {--Locative compounds before a noun (\mention{an anywhere operation}) are the ordinary noun-as-modifier use and take their article from the head noun.--}

## 3. Checked, no change

- Announcing openers: l. 321 ("This section compares that treatment with fusion") names the three constructions compared, so it does work.
- §3.3 closer (l. 317) and §4.6 closer (l. 562) each hand the next section its question; both kept.
- The "available under either ordinary-Head taxonomy" point recurs at l. 117, 391, 562, 740, 786, each time attached to a different generalization; not a duplicated verdict.
- Evidence-type and level shifts: §2's l. 91 announces the four evidence types, and §6.2 (l. 774) marks the matrix as a different kind of evidence; no unmarked shift found.

## C1 and C2 applied, 19 September (evening), with §2.2's closer moved

Brett asked whether §2.2 needed a summative paragraph. It didn't: the section already held the move ("That unity is the semantic side of this adjectival profile…"), three paragraphs from the end, so the section closed on the bare-colour caveat instead of on its result, while §2.1 and §2.3 both close on a consolidating sentence. A new summary would also have duplicated §2.6, which is the designated weighing section.

Applied instead:

- the mid-section paragraph was cut, which disposes of **C1** (its "That unity" pointed back past the predicative *much* material);
- **C2**: "The same relation holds between distribution and category" became "Distribution likewise leaves category open";
- §2.2 now ends: "The adjectival profile is real but narrow: grade, the degree series, and comparative complementation pick out *few*, *many*, *much*, and *little*, and no more of the inventory. Solt's single semantics for those four is the semantic side of it. Neither settles the category, since the same four carry the partitive, transparency, and dependent patterns of §2.1."

C3–C9 are still open.
