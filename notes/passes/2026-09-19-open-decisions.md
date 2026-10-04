# Open decisions after the 19 September pass round

<!-- SUMMARY: everything from today's pass round that still needs Brett: three follow-ups to the four-findings repairs, nine held items from the audits, and five admin items · status: awaiting review · updated: 2026-09-19 -->

Comment inline. Anything you accept, I'll apply to the manuscript and the affected supplements; anything you reject, I'll record as declined so a later pass doesn't raise it again.

## A. Follow-ups to this evening's repairs

### A1. The polarity reply belongs in the paper, not the notes

§3.2 now says peripheral *a* "licenses a positive quantificational interpretation in these constructions" and that the interpretation "remains a convention of the construction". That states the problem rather than answering it, and polarity is now the strongest remaining reason for a reader to keep *a few* as a lexical unit. The reasoning that answers it exists, in `2026-09-19-four-analytical-findings.md`, and was deliberately kept out of the manuscript.

Proposed addition after that sentence:

> {++A conventional interpretation doesn't by itself establish a lexical unit. Minimizers such as \mention{a bit} in \mention{doesn't matter a bit} take a specialized interpretation in a particular environment while remaining syntactically decomposable, and \textit{CGEL} distinguishes negative items from expressions that are merely negatively oriented \citep[822--823]{huddleston2002}. What the combination fixes is the interpretation, not the constituency.++}

Or tell me the argument you'd rather make, and I'll draft it instead.

### A2. Table 5's dashes for *every*

The permissions table still shows `--` for *every* under Subj and Obj, with no note. §3.1 now says you treat dependence as the ordinary pattern and limit the fragment to it, so the table is inside that scope, but a reader looking at the table alone sees an absolute exclusion, which is what we just withdrew. The four-findings plan said to annotate it.

Proposed, in the paragraph after the table:

> {++The dashes record the fragment's scope, the ordinary dependent pattern, rather than the unattested status of every combination (§\ref{sec:article-membership}).++}

### A3. l. 490 still limits retained fusion to adjectives

l. 677 now says fusion is held fixed "for adjectives and the nominal \mention{nylon} and \mention{double} constructions". l. 490 still reads "even when fusion remains available for adjectives".

> l. 490: {~~even when fusion remains available for adjectives~>even when fusion remains available for adjectives and for the nominal constructions of §\ref{sec:genitive-head}~~}

## B. Held from the audits (each has a proposed wording in the report named)

| # | Item | Where | Report |
|---|---|---|---|
| B1 | *each of them* plural rate: 13 of the 75 saved plural lines aren't plural agreement with it (non-finite *have*, or a verb agreeing with another head), so "about a sixth" overstates. The singular lines were never saved, so a corrected rate can't be computed without another gather | l. 99 and its footnote | `2026-09-19-measurement-construction-audit.md`, M1 |
| B2 | *the hurt can not be much* is listed among amount-denoting subjects, but *hurt* isn't one, and it's the frame Solt stars. (The claim that the line is Shakespeare is an agent's from memory, unverified) | l. 129, l. 131 n., `quantifier-controls.tex` l. 118 | `2026-09-19-negative-claims.md`, 4 |
| B3 | "Exclamative *what* has no predicative use" has no starred example and no source | l. 315 area | same, 3 |
| B4 | Abstract and conclusion credit the grouping with the complex-determinative reanalysis, which §5.5 gives either ordinary-Head taxonomy | l. 29, l. 796 | `2026-09-19-contribution-alignment-2.md` |
| B5 | The secondary-use schema lists three inputs instead of naming the property they share, so it predicts nothing about unexamined words (including *the hes and shes*); its input class also says "name" where the category is proper noun | l. 758–760 | `2026-09-19-projectibility-audit.md` P2; level-category D10 |
| B6 | l. 52 credits the grouping with a structural regularity §5.5 grants to both ordinary-Head taxonomies | l. 52 | projectibility P1 |
| B7 | Nine coherence joins, as CriticMarkup: two vague antecedents in §2.2, an orphan sentence before Table 2, "listed above" pointing past the Hudson paragraphs, a duplicated verdict across §5.5 and §6.1, and four smaller ones | various | `2026-09-19-coherence-cohesion.md` |
| B8 | Smaller source items: *Kim isn't much of an actor* (CGEL's non-affirmative degree use), *Henrietta … blue* (CGEL analyses it as a fused modifier-head), bare *the few* (CGEL p. 416 wants a following modifier), Payne et al.'s continuity argument used against the pronoun subclass, the Reynolds 2024 "survey" wording | §§2.2, 4.4, 6.2 | `notes/rereads/2026-09-19-source-reread.md`, held items 3–5, 8–9 |
| B9 | Peripheral *a* attaches to the outer NP in dependent use but to *few*'s NP independently; Figure 4 groups *almost* with *every* on the reasoning that would group *a* with *few*. A sentence giving the reason would help | §3.2 | level-category, question |

## C. Admin

- **Spinillo 2004** page citations are unverified: UCL Discovery is behind a bot check, so the PDF needs downloading in a browser. "(earlier Spinillo 2000)" may also misdescribe the 2000 paper (Denison 2006 groups it with Hudson on D as a kind of pronoun).
- **Postal**: `literature/Postal1969_On_so-called_pronouns.pdf` is actually the abridged 2014 excerpt from Kayne, Leu and Zanuttini. Nobody has read the 1966 edition the paper cites.
- **Central bibliography**: the `reynolds2014determinatives` entry is wrong (vol. 31, no. 2, pp. 89–91, "Lenchuk" in the title). Needs `/push-bib --update` at polish.
- **Review board**: held. Worth running once A and B are settled; it's stale by 16 sections and would otherwise rediscover these.
- **Figure plan**: needs trimming. The one I'd build now is *quite a few mistakes* beside *many a man* (`figure-plan.md`, #6–7).

## D. Nothing is committed

41 changed and untracked paths, including today's two rounds of repairs, the pass reports and `notes/rereads/`. Say the word and I'll commit; the payload is worth a look first, since the reread folder carries the raw subagent reports.
