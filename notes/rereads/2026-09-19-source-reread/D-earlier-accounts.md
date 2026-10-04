# Source reread D: earlier and competing accounts
<!-- SUMMARY: source-reread pass, earlier/competing accounts (Hudson, Van Eynde, Spinillo, Lyons, Palmer, Postal, Sommerstein) · status: complete; 20 SUPPORTED, 8 NUANCE, 5 UNVERIFIED (all Spinillo) · updated: 2026-09-19 -->

**Summary.** I checked 26 citation contexts and 7 uncited attributions against manuscript SHA-256 `2c6c7953…`, which didn't change during the pass. Of the 26 citation contexts, 17 are SUPPORTED, 4 NUANCE and 5 UNVERIFIED. Of the 7 uncited attributions, 3 are SUPPORTED and 4 NUANCE. None came out OVERSTATED, MISATTRIBUTED or PAGE. All five UNVERIFIED contexts are Spinillo page citations: UCL Discovery sits behind a Cloudflare bot check. The most consequential finding: the manuscript describes Hudson as having a "determiner category" nested in pronoun (ll. 766, 819, 833), but Hudson says outright that there is no determiner word class (2004: 10; 2010: 254).

Checked by Claude (Opus 5), 19 September 2026. The manuscript was read-only.

## Sources, files, and page offsets

| Key | File read | PDF→printed offset (how established) |
|---|---|---|
| `hudson2004determiners` | `literature/Hudson2004_Are_determiners_heads.pdf` (+ .md) | PDF 1 = p. 7 (+6); running heads "8 Richard Hudson", "Are determiners heads? 9" |
| `hudson2010wordgrammar` | `literature/hudson-2010-introduction-to-word-grammar.pdf` | PDF 271 = p. 253 (+18); running head "English words 253" |
| `vaneynde2003determiner` | `literature/VanEynde2003_On_the_notion_determiner.pdf` (+ .md) | PDF 2 = p. 392 (+390); page footers 392–396 |
| `VanEynde_2007_BigMess` | `literature/VanEynde_2007_BigMess.pdf` (+ .md) | PDF 16 = p. 430 (+414); page footers |
| `lyons1968` pp. 232–235 | `~/pdf-inbox/grammatical_structure.pdf` (ch. 6; **not** the ch. 7 file in `literature/`) | PDF 24 = p. 232 (+208); running heads |
| `lyons1968` p. 279 | `literature/lyons1968-grammatical-categories.pdf` (ch. 7) | PDF 10 = p. 279 (+269); running head "7.2. Deictic categories 279" |
| `lyons1999` | `literature/Lyons1999_Definiteness.pdf` | PDF 349 = p. 331 (+18); page footers |
| `palmer1924` | `~/pdf-inbox/mdp-39015030925641-66-1788830062.pdf` (+ .md), single page | printed p. 24 (folio on page) |
| `postal1966` | `literature/Postal1969_On_so-called_pronouns.pdf` (+ .md). **This is not the 1966 original or the 1969 reprint** (see Postal below) | PDF 3 = p. 14 (+11); running heads "14 Postal" |
| `sommerstein1972` | `literature/sommerstein-1972-so-called-definite-article-english.pdf` (+ .md) | PDF 2 = p. 197 (+195); PDF 1 is the JSTOR cover |
| `spinillo2004reconceptualising` | **not obtained** (see Spinillo below); abstract only, via OpenAlex API | n/a |
| `spinillo2000determiners` | **not obtained**; bibliographic check only | n/a |

## Citation contexts

### Van Eynde

| Line | Claim (brief) | Pages checked | Source wording | Verdict |
|---|---|---|---|---|
| 71 | Van Eynde argues from inflection that determiners are heterogeneous, some adjectives and some nouns | 391 (abstract), 394, 396 | "some determiners are members of A, whereas others are members of N. The argumentation is mainly based on inflectional morphology and on morpho-syntactic agreement data." (p. 391) | SUPPORTED |
| 245 | From Italian and Dutch: no category of their own; adjective-like inflecting/agreeing ones are adjectives, genitives and non-agreeing pronouns are nouns | 392–394 | "Summing up, the specifiers of NP do not belong to a separate part of speech, but are either adjectives or nouns. In the former case they show the same inflectional variation and the same agreement as the prenominal adjectives, in the latter, they do not show any agreement." (p. 394) | SUPPORTED |
| 820 (table) | Same, "Lexical taxonomy, cross-linguistic" | 391–396 | as above; the claim concerns part-of-speech membership (p. 393: inflection is "one of the main criteria for motivating part of speech membership") | SUPPORTED |
| 311 | Van Eynde 2007 §5: *such a*, *what a* aren't Big Mess, since *what*, *such* "are invariably lexical" and "lexically select a nominal which is either unmarked or introduced by the indefinite article" | §5, pp. 430–431 | Both quotations exact (p. 430: "what and such are invariably lexical"; p. 431: "the exclamative what and the demonstrative such lexically select a nominal which is either unmarked or introduced by the indefinite article"). *how long a bridge* is his Big Mess example (abstract, p. 415). | SUPPORTED. Note: the second quotation gives his positive (head-functor) analysis, not the ground for exclusion; the exclusion grounds are lexical status and compatibility with bare nominals (p. 430). The manuscript's "since" is acceptable because his Big Mess analysis is defined against lexical selection. |

### Hudson

| Line | Claim (brief) | Pages checked | Source wording | Verdict |
|---|---|---|---|---|
| 619 | Hudson 2004: 7–8 distinguishes dependency from external headedness; D and N depend on each other, only one connects the phrase outward | 7–8 | "dependency is separate from head-hood … head-hood is a relation between a word and a phrase, whereby that word is the only word in the phrase which depends on some other word outside the phrase." (p. 8); "the determiner and the common noun … each depend on the other, so either (but not both) of them may be the head" (p. 7) | SUPPORTED |
| 619 | "His temporal adjunct evidence supports common-noun headedness": *that day* vs \**that point in time* (10–12) | 10–12 | "My main source for the following pieces of evidence is Van Langendonck (1994)" (p. 11); "(13) I saw him that time/moment/day/\*point in time." (p. 11); "the head of this morning must be morning, not this. The logic is irresistible." (p. 12) | **NUANCE** (see below) |
| 766 (uncited) | "Hudson puts his determiner category inside pronoun, which is itself inside Noun" | 2004: 9–10, 40 n. 2; 2010: 253–254 | "there's no need to recognize a separate class of determiners. In short, having replaced 'article' by 'determiner', I'm now replacing 'determiner' by 'pronoun'." (2010: 254); "there is no need for a word class 'determiner'" (2004: 10) | **NUANCE** (see below) |
| 768 | Hudson 2010: 253–254 makes taxonomic inclusion explicit | 253–254 | "In this analysis, then, 'pronoun' isA 'noun', and stands alongside two well established traditional subclasses, 'common noun' and 'proper noun'. In 'pronoun' we find ANY and THE …" (p. 254; Figure 10.1) | SUPPORTED |
| 768 | Noun contains common, proper, pronoun; a determiner is a pronoun whose valency permits the common-noun dependent (2004: 9–10) | 2004: 9–10 | "determiners are merely the subset of pronouns which allow a common noun as their complement … Since this is a matter of valency, it need not be expressed in terms of word classes" (p. 10) | SUPPORTED. Note: the first clause (common/proper/pronoun under noun) is in 2010: 254, not 2004: 9–10 (2004 has no mention of proper nouns; its closest statement is p. 40 n. 2, "pronouns are a kind of noun"). The preceding sentence's 2010 citation covers it, but a reader may take the end-of-sentence 2004 citation as covering both clauses. |
| 768 (uncited) | Category constant across independent and dependent uses, which differ in permitted dependents | 2010: 253 | "ANY belongs to the same word-class whether it is followed by a noun (Any book will do) or not (Any will do)." (p. 253) | SUPPORTED |
| 770 | Criteria: licensing a singular count common noun and mutual exclusion; sets aside *all*, cardinals, plural/non-count quantifiers (9–10) | 8–10 | Rules (2)–(3), p. 8: "A singular countable common noun normally needs a determiner … Only one determiner is possible per common noun." *all* "never qualifies as a determiner" (p. 9); numerals as determiners "hard to justify" (p. 9); CGEL's list includes words "irrelevant to rules (4) and (5) because they only combine with plural or mass nouns (e.g. a few, a little, many, much, enough, sufficient)" (p. 10) | SUPPORTED. Minor: the criteria themselves are stated on p. 8 (rules 2–3) and restated on p. 10 (rules 4–5), and rule (3) isn't restricted to singular count use, so "in that use" is slightly narrower than Hudson. |
| 819 (table) | "His determiner category within pronoun, which is within noun … Lexical taxonomy" | 2004: 9–10, 40 n. 2; 2010: 253–254 | "determiners are pronouns that take common nouns as their complement, and pronouns are a kind of noun" (2004: 40 n. 2); "a matter of valency, not word-class" (2010: 254) | **NUANCE** (same issue as l. 766) |
| 287 (uncited) | "*CGEL*, Hudson, and the D-noun analysis can all preserve [category continuity]" | 2010: 253 | "When a verb may be used either with or without an object noun, we don't put it into two fundamentally different classes; for instance, SING is still a verb …" (p. 253) | SUPPORTED. Note for §articles: Hudson (2010: 253) draws the same verb analogy that l. 287 attributes to Spinillo. |
| 685, 833 (uncited) | "Applying Hudson's nesting …"; "Hudson's explicit nesting" | as for l. 766 | as for l. 766 | Part of the l. 766 NUANCE: "nesting" is accurate for pronoun within noun, but not for a determiner class within pronoun. |

### Lyons

| Line | Claim (brief) | Pages checked | Source wording | Verdict |
|---|---|---|---|---|
| 804 | Lyons 1968: 232–235: distribution compared at different levels; same at one level, different at a more specific level | 231–235 (ch. 6, §6.4.1) | "we can say that two elements have the same distribution at various specified 'depths' … At a lower level two nouns might have a different distribution, one being 'animate' and the other 'inanimate', etc." (p. 233) | SUPPORTED. The point is on p. 233 (set up at 232); 234–235 concern rewrite rules and categorial grammar. Suggest narrowing to 232–233. |
| 827 | Lyons 1968: 279: "articles, demonstratives, and personal pronouns share definiteness and deictic contrasts"; a "semantic connection" | 278–280 | "They all 'include' the feature 'definite' … But the man and he, being undetermined with respect to proximity, are both in contrast with this man ('proximate') and that man ('remote'). The traditional separation of the 'articles', the 'personal pronouns' and the 'demonstrative pronouns' obscures these relationships." (p. 279) | **NUANCE** (see below) |
| 817 (table) | "Articles, demonstratives, and personal pronouns linked by definiteness and deixis. \| Semantic relationship" | 279 | as above | **NUANCE** (same) |
| 289 | Definite articles from demonstratives, cardinal articles from numerals (Lyons 1999: 331–336) | 331–336 (§9.2) | "the sources of definite and cardinal articles … in the reanalysis of some substantive determiner, usually a demonstrative or numeral." (p. 331); §9.2.3 "Numeral to cardinal article" (pp. 335–336) | SUPPORTED. Note: Lyons (p. 332) calls the change "not just a matter of feature loss" but reanalysis into DP position; in *CGEL* terms that position is a function, so the manuscript's "bears on content and use, not on the categorization" is compatible with his framing. |

### Palmer

| Line | Claim (brief) | Pages checked | Source wording | Verdict |
|---|---|---|---|---|
| 827 | Palmer 1924: 24 proposed placing "determinative adjectives" with pronouns | 24 | "To group with the pronouns all determinative adjectives (e.g. article-like, demonstratives, possessives, numerals, etc.)" | SUPPORTED |
| 827 | Contrasted with qualifying adjectives, "which permit predicative use, comparison, and adverbial modification" | 24 | qualificatives "alone bear the characteristic attributes of adjectives (e.g. epithetic and predicative uses, susceptibility to comparison, and susceptibility of being modified by adverbs)" | SUPPORTED. Palmer's term is *qualificative*, and his list also includes epithetic (attributive) use; leaving it out is defensible because determinatives also occur prenominally. |
| 814 (table) | "Determinative adjectives grouped with pronouns. \| Lexical grouping; inclusive Noun unspecified" | 24 | as above; p. 24 keeps Noun and Pronoun as separate parts of speech | SUPPORTED |

### Postal

| Line | Claim (brief) | Pages checked | Source wording | Verdict |
|---|---|---|---|---|
| 815 (table) | "Personal pronouns analysed as articles, with deeper noun features. \| Intermediate and underlying representations" | excerpt pp. 14–15 | "the so-called pronouns I, our, they, etc. are really articles, in fact types of definite article. However, article elements are only introduced as segments in intermediate syntactic structures. In the Deepest structures they are … represented as syntactic features of nouns" (excerpt p. 15) | SUPPORTED (edition caveat below) |
| 829 | Develops the article–pronoun connection through reflexives and *we men* | excerpt pp. 15, 18–20 | "Most important in this regard are the reflexive forms" (p. 15); *we men* forms are "among the strongest evidence for our overall claim" (p. 20) | SUPPORTED |
| 829 (uncited) | Category assignment depends on level: article segments at intermediate stages, deepest counterparts noun features, surface pronouns can receive derivative Noun status | excerpt pp. 14–15 | "one can ask whether such and such occurrence of a form F is a noun in the Deep structure, a noun in such and such intermediate structure, a noun in the Surface structure" (p. 15); "in many cases assigned a derivative Noun status in Surface structures" (p. 15) | SUPPORTED |

**Edition caveat (Postal).** The bib entry cites the 1966 original (Dinneen, ed., *Report of the Seventeenth Annual Round Table Meeting*, Monograph Series on Languages and Linguistics 19, Georgetown UP, pp. 177–206). The held file, `literature/Postal1969_On_so-called_pronouns.pdf` (a symlink to Mendeley `Postal/1969/…`), isn't the 1969 Reibel and Schane reprint either. It's the abridged excerpt, with editorial "[ . . . ]" cuts, in Kayne, Leu and Zanuttini (eds.), *An Annotated Syntax Reader* (Blackwell, 2014), ch. 1, printed pp. 12–25. The Mendeley `Postal/1969` and `Postal/…Annotated Syntax Reader…/2014` PDFs are byte-identical (same MD5). All three manuscript claims appear in the excerpted Postal text, and the manuscript cites no Postal page, so the claims stand. But nobody has read the cited 1966 edition, and the 1966 page range rests only on a web-search summary. Sommerstein (1972) cites Postal from the 1969 reprint (e.g. "I969, 203", "I969, 2I7–22I"). **Recommendation:** re-label the held file as the 2014 excerpt in `literature/` and Mendeley. If a Postal page is ever cited, get the 1966 volume or the 1969 reprint first.

### Sommerstein

| Line | Claim (brief) | Pages checked | Source wording | Verdict |
|---|---|---|---|---|
| 816 (table) | "Definite article and personal pronouns given NP structure. \| Underlying representation" | 197–199, 203 | "the so-called definite article the is really (that is, in remote structures) a pronoun" (p. 197), with n. 1: "the is directly dominated in remote structures by an NP node"; "the and also I, he, and so forth, are not underlying articles but underlying pronouns (that is, NPs in their own right)" (p. 199) | SUPPORTED |
| 831 | Sommerstein 1972: 197–203 argues the opposite way, giving article and personal pronouns underlying NP structure | 197–203 | as above; "the converse conclusion" (p. 197) | SUPPORTED |
| 831 (uncited) | His comparison includes the count restriction on anaphoric *one*, "whereas *it* can refer to a quantity of a substance" | 200–201 | "one can only replace countable nouns" (p. 200); n. 8 (p. 201), reporting the journal's anonymous reader: *it* "can replace countable and uncountable nouns alike" | **NUANCE** (see below) |

### Spinillo

| Line | Claim (brief) | Pages | Verdict |
|---|---|---|---|
| 279 | Spinillo 2004: 153–158 retains *the*, *a*, *every* as an expanded article category … redistributes others among adjectives and pronouns (194–195); her grounds; differences within the trio | 153–158, 194–195 | **UNVERIFIED** at the cited pages. The core claim is supported by the thesis abstract (OpenAlex W3141232431): "only three, namely the articles the and a(n) and every, justify the postulation of the class for English … this category be extended to include every, so that the category determiner can be disposed of"; "the vast majority of these elements display properties which indicate that they belong to other classes". The abstract doesn't name adjectives and pronouns as the receiving classes, and doesn't give the three grounds. |
| 279 | "(earlier Spinillo 2000)" | n/a | **UNVERIFIED** (content). Bib entry plausible (see below). One caution: Denison (2006: 9, manuscript version at hummedia.manchester.ac.uk/oldmedia/david-denison/handbook.pdf) cites "Hudson (2000), Spinillo (2000)" together as arguments for treating D as a kind of pronoun. His sentence is ambiguous, but if it describes Spinillo 2000 accurately, the 2000 paper didn't make the 2004 article-trio proposal, and "earlier" should be checked against the article before submission. |
| 283 | Spinillo 2004: 156–158 recognizes *every*'s differences from *the* and *a*, and the articles' greater phonological dependence | 156–158 | **UNVERIFIED** |
| 287 | Spinillo 2004: 140–144 analogy with verbs and prepositions whose complements can be omitted | 140–144 | **UNVERIFIED in this pass.** A prior primary reading is on record: `notes/argument-restoration-2026-09-07.md` ("printed 140–144 read in the primary PDF; beginning of 145 checked"). It wasn't re-read today. |
| 821 (table) | "Determinatives redistributed; *the*, *a*, *every* retained as articles. \| Lexical recategorization" | abstract | SUPPORTED by the abstract ("re-categorisation proposed here"); no page cited. Counted under SUPPORTED. |

**Attempts made for Spinillo 2004** (all 19 September 2026):
1. `curl -sL -A "Mozilla/5.0" https://discovery.ucl.ac.uk/id/eprint/10101595/` returned a Cloudflare "Just a moment…" managed-challenge page, with no PDF link.
2. WebFetch on the same URL returned HTTP 403.
3. CORE mirror: `https://core.ac.uk/search?q="Reconceptualising the English determiner class"` gave a Cloudflare challenge, and `api.core.ac.uk/v3/search/works` a Cloudflare redirect.
4. OpenAlex `W3141232431`: no `pdf_url` at any location. The OpenGrey/EThOS handle `hdl.handle.net/10068/911031` returned HTTP 500.
5. Local searches: `lit resolve spinillo2004reconceptualising` and `lit resolve spinillo2000determiners` (both "no match"); `mdfind -name spinillo`, which found only review-board files; `mdfind "Reconceptualising the English determiner"`, which found only manuscript copies and prompts; `~/Documents/Mendeley Desktop/` (no Spinillo folder); `~/pdf-inbox` and `~/Downloads`; the project's `literature/` folder; gitignored `notes/passes/*-source-page-*.txt`. No copy of the thesis is held.

I didn't drive the browser through the Cloudflare check: the task authorized curl, and the portfolio rule is not to circumvent bot detection. `notes/prior-art-search.md:92` already records "UCL Discovery repository blocks automated download; Brett should grab via browser."

**Spinillo 2000 bib check.** Journal, volume, and pages (AAA 25, 173–189, 2000) match Denison (2006) reference list: "Spinillo, M. (2000). Determiners: a class to be got rid of? Arbeiten aus Anglistik und Amerikanistik, 25, 173-189." The issue number (`number = {2}`) isn't confirmed by that source. Crossref and OpenAlex have no record.

## Findings in full (non-SUPPORTED)

1. **ll. 766, 819 (table), 833, and 685: Hudson's "determiner category". NUANCE (level: word class vs valency subset).** Hudson denies that determiners form a word class: "there is no need for a word class 'determiner'" and he uses *determiner* only "as an informal name for the particular subset of pronouns that combines with a following common noun" (2004: 10). The 2010 book says the same: "a matter of valency, not word-class, there's no need to recognize a separate class of determiners" (254), and Figure 10.1 has no determiner node. (His 2010: 253 does say "treat determiners as a subclass of pronouns", but p. 254 withdraws the class.) So his taxonomy has two levels, noun > pronoun, and *the*, *any* are simply pronouns. It doesn't nest a determiner class within pronoun. The manuscript's comparison still works, because pronoun is the intermediate category that excludes common and proper nouns, and l. 768 describes Hudson correctly. Proposed wording:
   - l. 766: "Hudson classes the words as pronouns, and pronoun is itself inside Noun; his *determiners* are pronouns distinguished by valency, not a separate class."
   - l. 819: "Determiners are pronouns that take a common-noun dependent (a valency difference, not a class); pronoun within noun."
   - l. 833: "Hudson's pronoun analysis" instead of "Hudson's explicit nesting". l. 685: "Applying Hudson's pronoun classification to the full determinative inventory …"

2. **l. 619: "His temporal adjunct evidence supports common-noun headedness … (10–12)". NUANCE (attribution, scope, page).** Hudson attributes the evidence to Van Langendonck (1994) ("My main source for the following pieces of evidence is Van Langendonck (1994)", p. 11) and then endorses it (p. 12). It establishes N as head of adjunct NPs. Hudson's general position is that "in most cases either word could be [head] — the choice is free; but some constructions demand a common noun as head" (p. 8). Section 2.1 begins on p. 11. Proposed: "The temporal-adjunct evidence he takes from Van Langendonck (1994) requires the common noun as head in adjunct NPs: *I saw him that day* is possible, whereas \**I saw him that point in time* isn't … \citep[11--12]{hudson2004determiners}."

3. **ll. 247 and 249 (uncited, Van Eynde 2003). NUANCE, two points.**
   - (a) l. 247: "(he applies it to Italian and Dutch, and cites English only for the marking contrast)". English also supplies his non-agreement example for a nominal prenominal ("aluminium tubes, in which the singular mass noun aluminium does not show agreement with the plural count noun tubes", p. 394). It also supplies the Pollard and Sag specifier examples (\**the his pictures*, p. 392) and the possessive *'s* note (p. 394 n. 2). Proposed: "(he applies it to Italian and Dutch determiners; his English examples don't test it on determiners)".
   - (b) l. 249: "a marking value a functor contributes to the phrase it selects". The functor selects the nominal head daughter and contributes its MARKING value to the combination, the mother: "functors which select a nominal projection as their head and which contribute their MARKING value to the combination" (p. 395). Proposed: "as a marking value that a functor contributes to the phrase it forms with the nominal it selects".

4. **ll. 827 and 817 (table): Lyons 1968: 279. NUANCE (scope and level).**
   - "Articles" should be "the definite article": Lyons contrasts definite *the man* with *a man*.
   - "Share … deictic contrasts" is loose: *the* and *he* are "undetermined with respect to proximity" and contrast with *this* and *that*.
   - "Semantic connection"/"Semantic relationship" understates Lyons's framing. He analyses these words by deictic features within "grammatical categories" (p. 278 calls it "the correct syntactic analysis … in terms of their component deictic features") and says the traditional separation of these "parts of speech" "obscures these relationships". He doesn't propose a merged class.

   Proposed for l. 827: "\textcite[279]{lyons1968} adds a connection through deictic features: the definite article, demonstratives, and third-person pronouns all include the feature 'definite' and differ in proximity, so that their traditional separation as parts of speech, he says, obscures the relationship." Table: "Definite article, demonstratives, and third-person pronouns related by definiteness and proximity features. | Deictic features; no class proposed".

5. **l. 831 (Sommerstein): "whereas *it* can refer to a quantity of a substance". NUANCE (minor: syntax-to-semantics shift and attribution).** Sommerstein's point is about antecedent nouns: *it* "can replace countable and uncountable nouns alike" (p. 201 n. 8), a point he credits to the journal's anonymous reader. Proposed: "whereas *it* can stand for non-count as well as count nouns."

6. **l. 279, 283, 287 (Spinillo 2004), and l. 279 (Spinillo 2000). UNVERIFIED** (five contexts: l. 279 at 153–158, at 194–195, and the 2000 paper; l. 283; l. 287). See the attempts above. The abstract supports the article-trio claim. Pages 153–158, 156–158, and 194–195 and the three stated grounds are unchecked, as are the "adjectives and pronouns" destination and the 2000 paper's content. Pages 140–144 rest on the 7 September record. Needed: Brett downloads the thesis PDF from UCL Discovery in a normal browser and saves it to `literature/`, and these five contexts are rerun.

## Minor notes (not counted as findings)

- l. 804: narrow `lyons1968` 232–235 to 232–233. The ch. 6 source sits in `~/pdf-inbox/grammatical_structure.pdf` and hasn't been copied into `literature/`.
- l. 768: the common/proper/pronoun clause is supported by 2010: 254, not by the 2004: 9–10 citation at the end of the sentence.
- l. 770: Hudson's criteria are stated on p. 8, and the set-asides on pp. 9–10.
- Corpus note for §articles (l. 287): Hudson (2010: 253) makes the same verb-with-or-without-object analogy (SING) that the manuscript attributes to Spinillo (2004: 140–144).
