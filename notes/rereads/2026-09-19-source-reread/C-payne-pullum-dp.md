# Source reread C: Payne, Pullum, and the DP literature
<!-- SUMMARY: source-reread pass, group C (Payne 2007/2010/2013, Pullum & Miller 2022, Bruening 2020, Abney 1987, Pullum & Wilson 1977, Pullum 2020, Huddleston et al. 2022) · status: complete · updated: 2026-09-19 -->

**Summary:** 19 citation contexts. 13 SUPPORTED, 5 NUANCE, 1 MISATTRIBUTED (an example only), 0 PAGE, 0 UNVERIFIED. The one misattribution: l. 512 gives *the changes globally to the climate* as Payne et al.'s (2010) example, but it doesn't occur in that paper. The 17 September pass removed the "constructed" tag that used to mark it.

Manuscript checked: `determinatives-as-nouns.tex`, SHA-256 2c6c7953c659274969e88599c6d86369313bb0212fd57df0e3b0cb2480158afe (matches dispatch). Read-only; no project file edited.

## Sources, files, and page offsets

| Key | File read | Page offset / basis |
|---|---|---|
| `Payne2007` | `literature/Payne_Huddleston_Pullum_2007_Fusion.pdf` (publisher PDF, header "J. Linguistics 43 (2007), 565–603") | printed = PDF + 564 (running heads; PDF 18 = 582) |
| `payne2010` | `literature/Payne, Huddleston, Pullum - 2010 - …(2) copy.pdf` (Edinburgh Research Explorer copy, cover sheet says "Early version, also known as pre-print"; typeset pagination runs 31–81, matching the published range) | printed = PDF + 29 (PDF 1 is the repository cover; PDF 11 = 40). Pages not checked against the publisher PDF. |
| `payne2013anaphoric` | `~/Documents/Mendeley Desktop/Payne et al/Language/Payne et al. - 2013 - Anaphoric one and its implications.pdf` (publisher PDF) | printed = PDF + 793 (PDF 4 = 797) |
| `pullummiller2022nps` | `~/Documents/Mendeley Desktop/Pullum, Miller/Unknown/… Why Chomsky was right(2).pdf` (draft dated 4 Oct 2022; the other copy is the 3 Oct draft; `.md` sidecar is the 3 Oct draft) | the draft's own page numbers |
| `bruening2020nominal` | `~/Documents/Mendeley Desktop/Bruening/Glossa/Bruening - 2020 - …pdf` | article pages 1–19 (Art. 15) |
| `abney1987` | `literature/Abney1987_English_NP_sentential_aspect.md` and PDF | dissertation pagination; abstract on p. 2 (PDF 2) |
| `pullumwilson1977` | `~/Documents/Mendeley Desktop/Pullum, Wilson/Langu/…Autonomous syntax….pdf` (JSTOR; identical to the copy in `…/1977/`) | printed = PDF + 739 (PDF 1 is the JSTOR cover; PDF 2 = 741) |
| `pullum2020theorizing` | Not held locally (search below). The open-access PDF was downloaded from `cadernos.abralin.org/index.php/cadernos/article/download/279/18` to the session scratchpad and read there. It hasn't been added to `literature/`. | article pages 1–33 |
| `Huddleston2021` | bib entry only (per task); `literature/huddlestonpullumreynolds2022-sieg2-errata.md` for the book's online-resources statement | n/a |

Search for `pullum2020theorizing` before download: `lit resolve pullum2020theorizing`, `lit resolve "Theorizing about the syntax"`, `lit resolve 10.25189/2675-4916.2020.v1.n1.id279` (all "no match"); `mdfind "Theorizing about the syntax of human language"` (only this project's files); `mdfind -name Theorizing`; `find ~/Documents ~/Downloads ~/pdf-inbox ~/projects ~/Desktop -iname "*theoriz*"`, `-iname "*cadernos*"`, `-iname "*pullum*2020*"`; `ls` of every `~/Documents/Mendeley Desktop/Pullum*` folder; `grep -rl "radical alternative to generative" literature` (only `steedman2024model.md` and `potts2024characterizing.md`, which cite it).

## Citation contexts

**1. l. 44, `Huddleston2021`: the online "List of determinatives in English" accompanies the book.**
Bib: *A Student's Introduction to English Grammar*, 2nd edn, CUP 2022, doi 10.1017/9781009085748. That matches the book the footnote describes. The SIEG2 text refers readers to online resources at "www.cambridge.org/SIEG2" (errata sidecar). The URL itself wasn't fetched, as instructed. The key says 2021 but the entry's year is 2022, so the citation renders as 2022. **SUPPORTED** (bib matches). The key/year mismatch is cosmetic.

**2. l. 77, `payne2010` (no page): an NP can function as determiner (*Kim's book*), and a determinative-headed phrase can function as modifier (*the many people*).**
Payne 2010 supports only the first half: "the noun-headed NP takes a determiner (a genitive NP or a determinative: *this*, *the*, etc.)" (p. 74, n. 1). I found no statement that a determinative (phrase) functions as modifier. Search: all 14 hits for "determinative" in the PDF text (pp. 33, 39, 40–42, 51, 63, 66, 74); "the many|the few|many people|the two|all the" in the `.md`. Payne 2007 states both halves on one page: the determiner "can also be realized by NPs – usually genitive, as in *this guy's shoes*", and the cardinal numeral determinatives are "modifiers in *that one time, the two times I tried it myself*" (p. 567). **NUANCE** (one of the two sources supports only half, with no pinpoint). Repair: `\parencites[567]{Payne2007}{pullummiller2022nps}` in place of `\citep{payne2010,pullummiller2022nps}`.

**3. l. 77, `pullummiller2022nps`.**
"although determinatives most commonly occur in determiner function, they can marginally function as modifiers instead … *one* is a determiner in *one mint julep* but a modifier in *the one thing you shouldn't do*". The determiner function goes "also (very frequently) to genitive NPs" (draft p. 3). **SUPPORTED.** The manuscript drops their "marginally", but "can function" doesn't claim frequency.

**4. l. 79, `abney1987`: under the DP hypothesis D heads expressions such as *some apples*.**
"This dissertation is a defense of the hypothesis that the noun phrase is headed by a functional element (i.e., 'non-lexical' category) D, identified with the determiner" (abstract, p. 2). **SUPPORTED.** A note, not a defect: Abney's D is a functional, non-lexical category, while the manuscript's l. 81 defines D as a lexical-category label. Pullum and Miller argue that the DP analysis's D is in fact lexical. The sentence at l. 79 is consistent with either reading.

**5. l. 79, `pullummiller2022nps`: reject DP for English.**
"Overall, data and theory suggest that the head of the substantive phrase is N and not D, at least in languages like English and French" (p. 24). They hedge that "we cannot claim that either hypothesis could ever be declared decisively refuted" (p. 24). The manuscript claims no refutation. **SUPPORTED.**

**6. l. 79, `bruening2020nominal`.**
"The patterns of conventionalized expressions are incompatible with the DP Hypothesis and require that the head of the nominal is N, not any functional head" (abstract, p. 1). And "The head of the nominal really has to be N, not D" (§6, Art. 15, p. 17 of 19). His positive argument (§5) uses English idioms and collocations. §§3–4 rebut Shona and BCS defences. **SUPPORTED.**

**7. l. 87, `pullumwilson1977`: auxiliaries within Verb as a precedent for keeping distinctive properties within a broader category.**
"it is possible to adduce overwhelming evidence that no line can or should be drawn between them and the items which are categorized uncontroversially as verbs … Our analysis treats all auxiliaries as verbs" (p. 741). The distinctive properties stay in lexical entries. Split entries record the contracted negatives (*won't*), and missing forms mark the modals. [+AUX] and [+MODAL] could be defined from those entries if a rule ever needed them (pp. 771–772, (56)). **SUPPORTED.** Optional pinpoint: `\citep[741, 771--772]{pullumwilson1977}`.

**8. l. 135, `payne2010` p. 61: complementary distribution alone doesn't assign category.**
"it is not the distribution per se which leads us to think of a derivational relation between *wood* and *wooden*, and an inflectional relation between *soldat* and *soldatom* … factors other than simple distribution are the crucial ones" (p. 61). The question is posed on p. 60: "does the distribution per se … have any bearing on the single category claim? In fact, we believe not." **SUPPORTED.** An optional page change is 60–61.

**9. l. 186, `Payne2007` §1.3: *someone* is a compound determinative.**
"*somebody, everything, anyone*, etc.: these are compound determinatives functioning as fused determiner-head (CGEL: 423f.)" (§1.3, p. 581). **SUPPORTED.** Two notes: Payne et al. credit the categorization to CGEL 423–424, and §1.3 spans pp. 581–584 if page pinpoints are preferred.

**10. l. 403, `Payne2007` (no page): one constituent jointly realizes Head and a dependent function, subject to structural and adjacency conditions.**
Fusion lets "two functions which are realized canonically by discrete expressions … be realized jointly by a single expression" (p. 568). They list: "(ii) FF is permitted in a category XP only between the head of XP and either an immediate dependent of XP or an immediate dependent of the immediate dependent of XP. (iii) The fused functions are adjacent." (p. 571). **SUPPORTED.** Optional pinpoint `[568--571]`.

**11. l. 506, `payne2010` 40–42: keep *few*, *any* in one category across dependent and independent uses.**
"it is an unnecessary complication to assign them to different categories according as they are or are not followed by a head" (p. 41). **NUANCE.** The attributed point is accurate, but on the same pages the continuity argument serves Payne et al.'s case that these words aren't pronouns, a subclass of Noun, because their modifiers are adverbs. They write: "If these words were pronouns, the attributive modifier function would have to admit adverbs as well as adjectives" (p. 41). They also say CGEL's pronoun-within-noun analysis "predicts (correctly) that any internal modifier of a pronoun will be adjectival" (p. 40). That argument bears directly on D-noun. The manuscript answers its substance at l. 512 (adverbs postmodify nouns; *almost textbook*) and through peripheral attachment, but never says Payne et al. made the argument. Proposed wording: "\textcite[40--42]{payne2010} keep \mention{few}, \mention{any}, and related forms in one lexical category across dependent and independent uses, and exclude them from the pronoun subclass of Noun because their premodifiers are adverbs." The rest of the paragraph stands, and l. 512 then reads as the reply.

**12. l. 506, `payne2010` 41–42: adverbial premodification (*almost anybody*) versus adjectival postmodification (*nothing absolute*).**
"(12c) [*Almost anybody*] could do it" (p. 41). Also: "the premodifiers of such forms are adverbs while postmodifiers, as internal modifiers within NP, are adjectival. Compare the adverb in *absolutely nothing* with the adjective in *nothing absolute*" (p. 42). **SUPPORTED.**

**13. l. 512, `payne2010` 42–47: adverbs postmodify common nouns, "as in *the changes globally to the climate*".**
The claim is supported by §5, "Adverbs as postmodifiers of nouns" (pp. 42–52): "The existence of this overlooked but important construction shows that the complementarity claim is simply false" (p. 43). The example isn't in the paper. Search: "changes" has 0 hits in the `.md` and in `pdftotext` of the whole PDF. "globally" occurs only in (17a) *the unique role globally of the Australian Health Promoting Schools Association* (p. 43) and a p. 44 list. "climate" occurs only in a list of noun types (p. 47). `analysis/manuscript-census-2026-09-14/amendments.json` entry `pay-030` records that "the constructed" was removed on 2026-09-17. Under the §1 convention ("attested examples name theirs"), the example now reads as Payne et al.'s. **MISATTRIBUTED (example only).** Repair with their own example: "…as in their \mention{the weather recently} \citep[46]{payne2010}" (ex. 24c, p. 46), or *the impact internationally of the publicity* (24b, p. 46), or *the use temporarily of Australian troops* (16, p. 42). Alternatively, restore "the constructed".

**14. l. 512, `payne2010` p. 75 n. 3: *almost* modifies "the attributive nominal *textbook*".**
"There is one genuine adverb, *almost*, which appears to be able to function as a pre-head modifier … Here *almost* modifies the noun *textbook*" (p. 75, n. 3). **NUANCE.** First, a level shift: the source says "the noun", while the manuscript uses "nominal" as its technical term for Nom (l. 325). Second, the hedges drop out ("appears to be able", "one genuine adverb"). Proposed: "They also note one adverb, \mention{almost}, that appears to premodify a noun: \mention{textbook} in \mention{an almost textbook case} \citep[p.~75, n.~3]{payne2010}."

**15. l. 518, `Payne2007` 581–583: *hardly* in DP structure, *present* in nominal structure.**
In (13d), "*anyone* functions as the head of the DP, allowing modification by *hardly*, but also simultaneously as the head of the whole NP in which there is an adjectival modifier" (pp. 582–583). The compounds "take exactly the same pre-head modifiers as the determinative bases they contain: compare … *hardly anyone present* and *hardly any writer present*" (p. 581). The restrictor "is non-recursive and can only be realized by constituents in post-head position" (p. 583). **SUPPORTED** (both follow-on sentences too).

**16. l. 543 (caption), `Payne2007` p. 582 (13d): DP fills Det of NP and Head of Nom.**
Checked on the rendered page image. In (13d) the node "Det-Head: DP" has two mother lines, one from NP and one from Nom, and "Mod: Adj" (*present*) sits under Nom (p. 582). **SUPPORTED.**

**17. l. 566, `pullum2020theorizing`: conditions describe structures directly (constraint-based approach).**
MTS "defines grammars as finite sets of statements that are true (or false) in certain kinds of structure … Such statements provide a direct description of syntactic structure" (abstract, p. 1). "A grammar consists of constraints, each making a statement that is true or false of any given individual expression" (§3, p. 8). **SUPPORTED** (from the downloaded open-access PDF).

**18. l. 720, `payne2013anaphoric` 797–798: three lexemes spelled *one*, "determinative, anaphoric common noun, and generic personal pronoun".**
"English has three distinct lexemes with *one* as their orthographic base form" (p. 797). Table (5) lists "Pronoun / CATEGORY: regular third-person singular indefinite pronoun … 'an arbitrary person'", "indefinite cardinal numeral determinative", and "regular common count noun … Anaphoric" (p. 797). **NUANCE.** "Personal pronoun" is CGEL's label ("a personal pronoun (*One should keep oneself informed…*)", CGEL sidecar l. 11739; "belongs with the personal pronouns", l. 12918). Payne et al. 2013 call it an indefinite pronoun. Proposed: "determinative, anaphoric common count noun, and generic pronoun". Alternatively, keep "personal" and add the CGEL citation.

**19. l. 831 (footnote), `payne2013anaphoric` 797–798: anaphoric *one* as a common count noun, distinct from determinative *one* and "personal pronoun *one*".**
Same source wording as item 18. **NUANCE** (same label issue). Proposed: "…distinct from determinative \mention{one} and pronoun \mention{one}."

## Uncited attributions (surname sweep across the whole file)

Grep: `payne|pullum|miller|bruening|abney|wilson|huddleston2021|DP hypothesis|DP analysis`, plus `fusion|fused|restrictor|et al|auxiliar|constraint-based`.

- **l. 329**: "Fusion allows branches to converge on a shared constituent with two parents." This is uncited but matches Payne 2007. Their fusion diagrams violate Sampson's "single mother condition", and "the single category which realizes them will in effect have two mothers" (p. 570). SUPPORTED. Suggest adding `\citep[570]{Payne2007}`. Their qualification ("in the simple case the two mothers happen to coincide") doesn't affect the manuscript's configurations, which have an intervening Nom.
- **l. 79**: "Here DP means determinative phrase, as in *CGEL*." SUPPORTED. The CGEL abbreviations list gives "DP determinative phrase", and Payne 2007 n. 2 (p. 566) and Payne 2010 (p. 39) use the label the same way.
- No other uncited attributions to these authors were found. Every "Payne", "Pullum", "Miller", "Bruening", "Abney", and "Wilson" match carries a `\cite`. `sec:payne` is only a label.

## Bibliography entries versus editions read

- `Payne2007`: *JL* 43, 565–603, doi 10.1017/S002222670700477X. Matches the PDF header. The issue number (3) isn't printed on the PDF.
- `payne2010`: *Word Structure* 3(1), 31–81, doi 10.3366/E1750124510000486. Matches the repository cover sheet. The copy read is labelled a pre-print, though its pagination matches.
- `payne2013anaphoric` (local bib): *Language* 89(4), 794–829. Matches the running heads and page span. The DOI wasn't visible in the extracted text.
- `pullummiller2022nps`: LingBuzz 006845, 2022. The PDF is the October 2022 English draft, "a translated and significantly revised version of a paper in French … in a special issue of CORELA", which is consistent with the note. The LingBuzz number couldn't be confirmed (lingbuzz.net returned 502).
- `bruening2020nominal`: *Glossa* 5(1): 15, doi 10.5334/gjgl.1031. Matches the PDF header.
- `abney1987`: MIT PhD thesis, 1987. Matches.
- `pullumwilson1977`: *Language* 53(4), 741–788, JSTOR 412911. Matches.
- `pullum2020theorizing` (local bib): 1(1), 01–33, doi 10.25189/2675-4916.2020.v1.n1.id279. Matches the landing-page metadata. House style may prefer `1--33`.
- `Huddleston2021`: SIEG2, 2nd edn, 2022. Matches the book described (see item 1).

## Leads outside the verdicts (optional)

- Payne 2010, n. 5 (p. 75): "Some works treat *many* and *few* in this use as nouns rather than pronouns." This is a prior nominal treatment of independent *many*/*few*. It may deserve a place in the related-proposals discussion or table.
- Payne 2010, p. 63 bears on §2.4's degree-series argument. If *many, much, few, little* are determinatives, "even comparative and superlative morphology is not restricted to adjectives and adverbs. Category alone is simply not the determining factor here".
- Other lines where the 17 September pass removed "constructed" next to a CGEL citation: l. 182 (*There are several*, beside `\citep[1391--1393]{huddleston2002}`) and l. 208 (*There was a second*, after `\citep[416]{huddleston2002}`). Both are outside this group's scope. They should be checked by the CGEL reread to confirm they don't now read as CGEL's examples.
