# Draft restatements: *each of the people* agreement and the compound exclusions
<!-- SUMMARY: proposed replacement text for three manuscript loci, grounded in the COCA exclusion tests; not applied · status: draft for Brett · updated: 2026-09-17 -->

Two exclusions the COCA tests contradicted, restated so the claims survive as grammatical claims with the usage facts stated. Nothing applied to the manuscript. Corpus quotations are verbatim from the screened lines; the CGEL footnote was checked in the PDF (§9.6, p. 423, n. 43).

## 1. §quant-nouns, number transparency (line 142)

**Current:**

```latex
Singular \mention{each of the people} doesn't take its number from \mention{people}; nor does ordinary \mention{a photograph of the people}. Number transparency specifically connects quantificational \mention{lot} with number-neutral \mention{some}.
```

**Proposed:**

```latex
\mention{Each of the people} takes singular agreement by default, and ordinary \mention{a photograph of the people} takes it categorically, so neither is number-transparent in \textit{CGEL}'s sense. The contrast isn't absolute, though. Plural agreement after \mention{each of them} occurs in about a sixth of COCA tokens, and after \mention{each of the} with a plural noun in about a third, in edited prose as well as speech.\footnote{COCA, List counts (\href{https://www.english-corpora.org/coca/}{english-corpora.org/coca}, 17 September 2026): \mention{each of them} + \mention{is/has/was} 389, + \mention{have/are/were} 78; \mention{each of the} + plural noun + \mention{was} 151, + \mention{were} 73 over 173 noun-specific strings, a share inflated by sentences in which the verb agrees with another head. Attestations: \enquote{Each of them have had a career that is the stuff of dreams} (\textit{USA Today}, 2018); \enquote{Each of the participants were administered the survey packet} (\textit{Professional School Counseling}, 2007); \enquote{Each of the films were selected from a collection of family films} (\textit{Roeper Review}, 2002). Queries and screened lines are in the project repository under \texttt{corpus/exclusion\_tests/}.} That variation is agreement with the nearer or notional plural, the pattern familiar from \mention{a number of the people were}, and it leaves \mention{each} singular; with \mention{some of the people}, by contrast, plural agreement is the only option. Number transparency specifically connects quantificational \mention{lot} with number-neutral \mention{some}.
```

Why this shape: the argument needs *each* and *a photograph of* to differ from *lot* and *some*, and it still does; the difference is now categorical versus variable rather than present versus absent. The 17 percent and 33 percent are in the footnote as counts, not in the prose, and the one-third figure carries its caveat. If the paragraph is getting long, the second and third sentences can go entirely into the footnote and the prose keep only "takes singular agreement by default".

## 2. §compounds, the exclusion and its conversion escape (line 515)

**Current:**

```latex
The compound construction independently excludes external determination and supplies the internal post-head restrictor permission, with the same position and non-recursion conditions as the fusion account. It doesn't license a corresponding pre-head adjective.
```

**Proposed:**

```latex
The compound construction independently excludes external determination and supplies the internal post-head restrictor permission, with the same position and non-recursion conditions as the fusion account. It doesn't license a corresponding pre-head adjective. Both exclusions hold of the compound as a determinative. English also has the compounds as common nouns by conversion, \textit{CGEL}'s \mention{a nobody} and \mention{a little something} \citep[423, n.~43]{huddleston2002}, and in that use they take an article, a pre-head adjective, and plural inflection: lexicalized \mention{a special someone} and \mention{a certain someone}, and productively \mention{an anonymous someone}, \mention{the responsible someone}, \mention{a furry something}.\footnote{COCA: \mention{special someone} 282 tokens and \mention{certain someone} 120 (List counts, 17 September 2026); \enquote{if an anonymous someone with very little solid evidence on his/her claims can get basically every major media outlet} (\textit{Mashable}, 2017); \enquote{The responsible someone has to collect the rents} (\textit{Confrontation}, 2014); \enquote{a furry something swinging indelicately from its mouth. The something plopped wetly into her bowl} (\textit{Analog}, 2002). The last shows the converted noun taking \mention{the} in the next sentence. Screened lines under \texttt{corpus/exclusion\_tests/}.} The article and the pre-head adjective are the diagnostics of conversion, not counterexamples to the determinative's permissions, and the converted noun keeps the common noun's ordinary modifiers rather than the specialized restrictor.\footnote{Whether a converted compound can still take the post-head restrictor (\mention{a certain someone special}) is a judgment I haven't tested; the corpus lines show article and pre-head adjective without it.}
```

Why this shape: the exclusion is kept for the determinative and the counterexamples are given their CGEL analysis, with the corpus supplying the productive cases (*anonymous*, *responsible*, *furry*) that make conversion a rule rather than a list of two idioms. The *Analog* line is the best single citation because the next sentence takes *the something*. The second footnote is honest about the one thing the corpus can't show.

## 3. §det-uniform, the fragment's statement (line 616)

**Current:**

```latex
They exclude external determination and a corresponding pre-head adjective.
```

**Proposed:**

```latex
They exclude external determination and a corresponding pre-head adjective as determinatives; the converted common nouns of §\ref{sec:compounds} (\mention{a special someone}) fall outside the construction.
```

## Not changed

The independent-*every* exclusion (§independent, §fragment) can stay as written for fused-head use; if a hedge is wanted, one clause suffices: "apart from ellipsis with a recoverable nominal (*if not every, then almost every N*) and binomials (*any and every*)", with the two COCA lines in a footnote (see `corpus/exclusion_tests/every-reading.md`). *So numerous*, *very every/some/this*, the reversed orders, and partitive *no* hold; the starred forms can carry a "not attested in COCA (17 September 2026)" note if you want the searches on record.

## Checks before applying

- `\citep[423, n.~43]{huddleston2002}`: the footnote number is CGEL's own (n. 43 of ch. 5, p. 423). Confirm the house style accepts a footnote locator in `\citep`.
- The footnotes cite COCA sources by title and year; the supplement's convention adds a URL where one exists, and none of these has a stable one.
- The claim census will flag the three changed sentences; `amendments.json` needs entries for `qn-013`/`qn-014` (whichever quote the *each* sentence) and the two compound claims once applied.
