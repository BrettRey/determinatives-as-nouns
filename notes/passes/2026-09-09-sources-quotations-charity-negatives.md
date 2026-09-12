# Sources, quotations, charitable engagement and negative claims

Completed 9 September 2026. Scope: the current manuscript and its two supplements. The source reread targets the premises on which the argument depends, as specified in the agreed sequence; it is not a fresh literature survey or a claim to have reread every cited book. Existing direct page checks remain useful where the attribution has not changed. No image checks were performed in this round.

## Source reread

The local catalogue was consulted for CGEL, Payne 2007/2010, Reynolds 2021, Pullum and Wilson, Spinillo and Anderson. Missing catalogue matches were followed through the held files and existing source records. The catalogue's missing-copy result for Palmer was false: the previously downloaded original page is held in the PDF inbox.

| Source | Passage and evidence checked | Current attribution |
|---|---|---|
| Huddleston and Pullum 2002 | Full local sidecar, printed p. 327, “Pronouns included in the category of nouns”; nearby noun profiles and bare-role discussion; pp. 410–411 on independent genitives. Earlier direct checks of pp. 411–417, 429–430, 470–471, 517–520 and 536 are documented in the September 7–8 records. | Pronoun membership is justified through the functions of headed phrases despite inflectional and dependent differences. Both pure and fused heads occur with independent genitives. The retained argument and its limitations match these passages. |
| Payne, Huddleston and Pullum 2007 | Local full text: introductory fusion definition; §§1.2–1.3; pp. 581–583 including (13d) and the post-head, non-recursive restrictor discussion. | Two functions are jointly realized subject to structural and adjacency constraints. The compound comparison preserves DP versus Nom modifier domains and the specialized restrictor requirement. The compressed generic definition was clarified; the concrete analysis remains unchanged. |
| Payne, Huddleston and Pullum 2010 | Local full text on pronoun/determinative modification and dependent/independent continuity; the “almost textbook” footnote. Printed pp. 40–42, 60–61 and 75 n. 3 were directly checked in the preceding revision. | Category continuity, the limits of distribution-only classification and the cost of systematic adverbial premodification within a noun subcategory are all retained accurately. The text does not reinstate an exceptionless ban on adverbs modifying nouns. |
| Hudson 2004/2010 | Re-extracted the 2010 book's printed pp. 253–254 from PDF pages 271–272. The earlier page record covers 2004 pp. 7–12. | Determiners fall within pronoun, which falls within noun; determining use is specified through valency. No extra category node is required merely to identify the valency-defined subset. Dependency, phrase headedness and the two sources' inventories remain distinguished. |
| Reynolds 2021 | Local article's results, discussion and code appendix, compared with the preserved public matrix and numerical audit. | The discussion explicitly leaves nested alternatives open. Separation of the supplied profiles does not decide rank. The supplement distinguishes the reported 232 features from the public 155 and the coding/implementation discrepancies. |
| Pullum and Wilson 1977 | Held publisher article, text extracted afresh; opening and abstract on printed p. 741. | The all-auxiliaries-as-verbs analysis provides the limited taxonomic precedent claimed. It is not used as evidence that the nominal proposal follows automatically. |
| Spinillo 2004 | Reused the recorded primary UCL reading of printed pp. 140–144, checked during argument restoration. The present attribution and wording were compared with that record. | The account includes forms such as some and all, preserves category across complement alternation, and proposes redistribution. No return to the inaccurate demonstratives-only or “no positive taxonomy” descriptions in old planning notes. |
| Van Eynde 2003 | Local complete proceedings text, abstract and morphological/agreement argument in §1. | A/N redistribution and separation of lexical category from determining features are represented accurately, with Italian and Dutch evidence explicitly distinguished from the English proposal. |

For Reynolds 2021 the result record was considered separately from the discussion: the public file reproduces the numerical decomposition; clustering agreement is initialization- and feature-sensitive; none of those results tests superordinate Noun. The source discussion's openness to nesting is compatible with, but does not supply, that statistical limitation.

The supplement's “archived manuscript” was ambiguous. `git show 7710120:main.tex`, opening footnote, establishes that the erroneous claim about singleton features was in an earlier draft of *Determinatives as nouns*. Both the supplement and analysis README now identify that draft. The 2021 article is not blamed for this particular statement.

Supporting prior records: `notes/source-page-checks-2026-09-07.md`, `notes/argument-restoration-2026-09-07.md`, and `notes/comparative-revision-2026-09-08.md`. These distinguish direct primary readings from retained verifications. No new bibliographic entry was added.

## Quotation audit

The shared `check-quotes.py` was run because this project's snapshot lacks the script. It reports one NOSOURCE candidate and one non-prose quoted title. The complete source search for `enquote`, quotation environments and literal quotation marks yields these two spans; neither supplement adds a literary quotation.

| Span | Verification | Verdict |
|---|---|---|
| “be used indifferently as pronouns or as modifiers of nouns” | Palmer, printed p. 24, §40, paragraph 2. The original HathiTrust single-page PDF is `/Users/brettreynolds/pdf-inbox/mdp-39015030925641-66-1788830062.pdf`. Text was extracted afresh and matched, including “modifiers,” to the current source. The 1927 impression/1924 first-edition distinction was previously verified. | Exact consecutive wording. The surrounding “most members” qualification remains. No ellipsis, insertion or changed emphasis. |
| “List of determinatives in English” | Linked resource title in the first determinative-definition footnote, attached to the named Cambridge grammar's resource link. | A title, not an unattributed assertion or scholarly quotation. Retain as a title. |

The unrelated `/tmp/determinatives-palmer.txt` is a later-edition text with different wording (“qualifiers”); it was not used to clear the 1924 quotation. The source page above resolves the quotation-checker's missing-copy warning without an override.

The corpus attestations were retained verbatim during relocation and remain tied to pinned sentence identifiers. The Honda and something sentences preserve original source text. The corpus supplement distinguishes original “good looking” from normalized “good-looking.” The politicians/lawyers attestation remains in the concordance supplement. Blinding has not been applied and no attribution is orphaned.

## Charitable engagement

| Target | Re-expression, agreement and acknowledged debt | Criticism and verdict |
|---|---|---|
| CGEL's separate determinative category | Its category/function distinction, noun-membership rationale, lexical restrictions, adjectival and genitive fusion, and internal modifier evidence are presented positively. | The disagreement concerns primary rank and allocation of generalizations. The paper does not claim that CGEL misses the constructions. |
| Payne's fusion and modifier analysis | Dependent/independent continuity and the DP–Nom separation of modifier domains are preserved; the comparison acknowledges reuse of fusion for adjectives and genitives. | Ordinary headedness offers a different grouping of constructions. Both retain restrictor conditions. No automatic economy advantage is assigned to either reuse claim. |
| Separate D with ordinary Head | The manuscript supplies the shared Nom projection rule, dependent as well as independent D-headed NPs, the same permissions, and the same reduced phrase inventory. | This is the strongest explicit separate-D competitor, not a nominal proposal weakened by unnecessary DP duplication. The preferred inheritance account is argued on organizational grounds. |
| Hudson | Nested inclusion, valency, inventory scope and headedness distinctions are stated before comparison. Shared pro-form properties are acknowledged. | Coordination is explicitly provisional. The fragment does not refute nesting. An additional captured generalization can favour Hudson's organization. |
| Spinillo and Van Eynde | The agreement on category continuity and category/function separation precedes the different redistribution choices. | The positive links retaining every among quantifiers are given, and the different language evidence is named. No dismissive or motive-attributing wording remains. |
| Null-head alternatives | Context can supply a generic restriction; absence of an overt antecedent is not presented as a disproof. | Preference for an overt head is conditional on otherwise equivalent analyses. Fusion remains available. |

Palmer, Lyons, Postal, Sommerstein, Anderson, Déchaine and Wiltschko, Bruening and Reynolds's numeral/pro-form work are situated as relevant comparisons, not represented as defeated by the fragment. Searches for “fails to see,” “conflates,” “simply assumes,” and equivalent dismissive formulations found no current instance.

## Negative claims

Searches covered all three current `.tex` files for `no one`, `nobody`, `has not been`, `there is no`, `the literature`, `unexplored`, `to my knowledge`, `first to`, `novel`, `unlike`, `no existing`, `never`, and negative construction-specific formulations. A continuous reading supplied implicit comparisons beyond those strings.

No literature-wide priority or absence claim remains. The relevant negatives are bounded:

- The matrix has no common/proper-noun rows: checked against the input and the 73/65 partition. This is an inventory fact, not an unsearched claim about available datasets.
- The corpus lacks bare few/either/neither in this sample: retained as a sample-specific gap with an explicit warning against an ungrammaticality inference.
- The fragment does not distinguish coordination from nesting: a consequence of the stipulated equal rules and permissions, limited to this fragment.
- Ordinary every and article-headed arguments are excluded; antecedent requirements and adjectival determination are qualified by construction and interpretation. These are the grammatical judgments under comparison, not absence claims about a literature.
- Shared phrase inventory and external coverage are not unique benefits of nominal D: the separate-D ordinary-Head rule explicitly supplies the comparison.
- The correction notice has not been posted: a local action record, not a claim of having changed the original resource.

No outward novelty search or new citation was needed. The abstract's hierarchy-versus-construction formulation remains queued for contribution alignment; it does not require changing the rivals' analyses in the body.
