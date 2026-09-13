# Audit of §5 “The matched fragment and comparative costs” (lines 588–748)

## Overall assessment

The section is internally coherent as a demonstration of *coverage parity*: the four implementations are laid out in a clean 2×2 design, the sample derivations at 654–660 are correct, and the text is unusually candid about what is stipulated rather than derived (article exclusion, 660; definiteness and single-Det, 634). The main weaknesses are in the *cost accounting*, not the logic. The schemata push almost all differential work into the unstated conditions $C_h$ (“The head's entry and construction restrict every dependent”, 638), and several of those conditions are exactly where the accounts differ. As written, the ordinary-Head schemata overgenerate in Det function (Finding 1); the use-permission inventory omits a function the fragment's own examples require (Finding 2); one attachment asymmetry that favours fusion is not tallied (Finding 3); and one argument that genuinely favours D-noun over separate-D is left as a restatement (“alignment”, 690) when it could be made explicit (Finding 4). The section's favourable conclusion is a fit judgment, which 746 concedes; a few sentences (“consolidates”, 634; “favour”, 690; “advantage”, 748) describe it as a cost result the section does not establish.

Nothing in this task raised an epistemic, authorization, coordination, or oversight risk requiring escalation.

## Findings, in priority order

### 1. Det/Mod-function restrictions on determinative-headed NPs are unstated; the ordinary-Head schemata overgenerate, and the omission bears directly on the criterion at 748

**Where.** §5.2, rules at 644–646; 650; 662; consolidation claim 627–634; 672; 686; criterion at 748.

**Rule at issue.** $\mathrm{Nom}_h \to (\mathrm{Mod}_{\mathrm{pre}})\ \mathrm{Head}{:}\mathrm{N}_h\ (\mathrm{Comp})\ \mathrm{Mods}_{\mathrm{post}}$; $\mathrm{NP}_h \to (\mathrm{Mod}_{\mathrm{periph}})\ (\mathrm{Det})\ \mathrm{Head}{:}\mathrm{Nom}_h$; licensing $f\in U_h \wedge C_h(f,c)$. Line 662 says “*Some* and *few* permit a partitive *of*-phrase within their nominal projection” with no function restriction; Table 5 gives *some* Dependent: yes.

**Derivation.** $\mathrm{NP}_{apples} \to \mathrm{Det}{:}\mathrm{NP}_{some},\ \mathrm{Head}{:}\mathrm{Nom}_{apples}$, with $\mathrm{NP}_{some} \to \mathrm{Nom}_{some} \to [\mathrm{Head}{:}some][\mathrm{Comp}{:}\text{of them}]$. Output: \**some of them apples*. Checks: Det $\in U_{some}$ ✓; plural-count target ✓; nothing stated in §5 makes $C_{some}(\mathrm{Det},c)$ fail. The same rules yield \**few who came people* ($\mathrm{Mods}_{\mathrm{post}}$ inside a Det NP), a spurious second parse of *the few apples* with *the few* as Det NP ($\mathrm{NP}_{few}\to\mathrm{Det}{:}\mathrm{NP}_{the},\ \mathrm{Head}{:}\mathrm{Nom}_{few}$, then $\mathrm{NP}_{apples}\to\mathrm{Det}{:}\mathrm{NP}_{few}\ldots$; *few* permits external Det per 662), and *lucky few apples* with *lucky few* as Det NP. Meanwhile comparative complements must stay licensed in Det function (*fewer than ten apples*), so the condition must also discriminate Comp types.

By contrast the fusion schema (678, 674) excludes all of these by construction: $\mathrm{DP}_h \to (\mathrm{Mod}_{\mathrm{pre}})\ \mathrm{Head}{:}\mathrm{D}_h\ (\mathrm{Comp})$ has no Det slot, no $\mathrm{Mods}_{\mathrm{post}}$, no AdjP premodifier, and the partitive sits in Nom. The D-noun/fusion account's “NP already projected” (686) needs the same bare-internal restriction, or *some of them* gets two parses (Comp inside the inner NP or on the outer Nom).

**Consequence.** All three NP-projecting accounts require a function-indexed constraint of roughly this shape: *in Det (and internal Mod) function, a determinative-headed NP contains only its head, its licensed AdvP premodifiers/peripheral modifier, and a comparative complement.* That constraint is CGEL's DP rule restated as a lexical/constructional condition. It is not stated, not in Table 7, and it is precisely the difference between determinative-headed and genitive Det NPs (*a friend's car* has an internal Det; *the man I met's car* a relative). Line 748 sets the section's own test: if the two “require different projection rules after their independently motivated restrictions are held fixed, the shared-projection proposal in §5.2 loses its advantage.” The bundle is not independently motivated in the relevant sense — under CGEL it *is* the DP rule. So the “consolidation” at 634 removes one phrase label and adds one construction-specific expansion restriction; net economy is at best neutral. This does not damage D-noun's viability, but it removes projection economy as a ground for the preference.

**Status.** Overgeneration as written: demonstrated. Net cost: open, but the manuscript's own criterion puts the burden on it.

**Repair.** Add the constraint as one explicit constructional statement in §5.2 (after 662); enter it in Table 7 for the three NP-projecting rows; revise 634 and 748 to “shared schema with head-class-specific expansions”; rest the preference on the profile (§2) and the labelling argument in Finding 4, not on projection economy.

### 2. $U_h$ lacks a Mod permission that the fragment's covered constructions require

**Where.** §5.1 definitions at 596; Table 5 (605–610); licensing at 646–650; 662; 742; scope statement 594 (which includes “the modifier … comparisons in §4”).

**Claim at issue.** *Dependent* is defined as heading “a phrase in Det function before another nominal”; *Independent* as subject/object use. $U_{few}=\{\text{Dependent},\text{Independent}\}$.

**Missing step.** The fragment's own cases put determinative-headed NPs in internal Mod function: *the few mistakes* (*few* = Mod, 450), *the very few people* (“the resulting *very few* NP functions as Mod in the larger NP”, 532), *these two hundred books* (“*two hundred* is an internal modifier”, 742), and *two* modifying *hundred* (742). Under 646, licensing $\mathrm{NP}_{few}$ in *the few mistakes* requires $\mathrm{Mod}\in U_{few}$, which Table 5 does not supply. The definition at 596 excludes it. These NPs also need the bare-internal restriction of Finding 1 (\**the few of them people*).

**Consequence.** The fragment as stated does not license several of the constructions it claims to cover, including the one that grounds the “one internal permission covers both constructions” claim (532, 662).

**Status.** Demonstrated inconsistency; easily fixed.

**Repair.** Add a third permission (internal Mod after an external Det) for *few/many/much/little* and cardinals, with the same internal restriction as Det use; amend 596 accordingly.

### 3. Approximative attachment is non-uniform under ordinary Head; the cost is acknowledged as “explicit” but not tallied against fusion's single site

**Where.** 638; 664; 736; Table 7 rows 726–728; with §4.4 at 512, 538 and §2.4 at 227.

**Rule at issue.** $\mathrm{Mod}_{\mathrm{periph}}$ precedes Det in the NP rule (645), so an approximative after an external Det must be Nom-internal: *the almost thirty who came* (538, 664). Elsewhere approximatives are peripheral: *almost every … teacher* (512, 664).

**Derivation.** Compare *the almost thirty people who came* (thirty in Mod function; *almost* peripheral to $\mathrm{NP}_{thirty}$ by the stated policy) with *the almost thirty who came* (*thirty* in Head function; *almost* internal to $\mathrm{Nom}_{thirty}$). Same string, same adverb, two attachment sites depending on the host's function. Under fusion, both are DP-internal (678), as is *almost every* and *hardly anyone*. Both frameworks additionally need NP-peripheral attachment for non-determinative hosts (*almost my entire life*, 510), so both have two sites overall; but fusion's split follows the category of the host, whereas ordinary Head's follows the construction (external Det + cardinal + Head function). This is the same kind of non-uniformity the manuscript counts against fusion for *few* (498).

Note also that the peripheral choice for *almost every* is motivated in §2.4 (227) by the wish to separate approximatives from the degree series; within the fragment nothing forces it — $\mathrm{Nom}_{every}\to\mathrm{Mod}_{\mathrm{pre}}{:}almost\ \mathrm{Head}{:}every$ is generable and would make approximatives Nom-internal on determinative hosts uniformly (mirroring fusion's carving and the manuscript's own treatment of *very*).

**Consequence.** Table 7's “Peripheral NP premodifiers; head-specific internal modifiers” understates: the ordinary-Head rows use both sites for one adverb class, while row 3 uses one. The manuscript's simplicity argument for ordinary Head is correspondingly weaker than stated.

**Status.** Asymmetry demonstrated; whether it is a net cost is open (it depends on constituency evidence for peripheral attachment in *almost every*, which the section does not supply).

**Repair.** Either adopt Nom-internal attachment for approximatives on determinative heads (retaining peripheral attachment for the CGEL 430–431 cases) and adjust §4.4/§2.4, or keep the analysis and enter the second site as a cost in Table 7 with the evidence that motivates it.

### 4. “Same NP projection” for separate D depends on a labelling stipulation; the “alignment” claim at 690 is a restatement that could be an argument

**Where.** 623; 627–634 (Det: {NP, PP} for “the three NP-projecting accounts”); 666–672; 690; 746; Table 7 row 727.

**Missing step.** The manuscript's own convention (caption at 389: “NP, DP, and VP mark their phrases”; $\mathrm{N}_{\mathrm{D}}$/$\mathrm{NP}_{\mathrm{D}}$ subscripts throughout) names phrases for their heads. Under separate D, the projection $\mathrm{Nom}_h \to \mathrm{Head}{:}\{\mathrm{N}_h,\mathrm{D}_h\}$ with $h\in\mathrm{D}$ yields a D-headed phrase, which by that convention is a DP. Calling it NP (672, “eliminating DP … while retaining primary D”) either redefines NP/Nom as construction labels detached from head category, or duplicates: DP with identical Nom-internal structure. Neither is free.

**Consequence.** (i) The consolidation Det: {NP, PP} holds without stipulation only for the two D-noun accounts; row 2 of Table 7 should record the stipulation. (ii) More usefully for the manuscript: this is an independent argument of the same type the paper uses against D-noun/fusion at 688 (structure that does no work). As phrased at 690 (“alignment of category and structure”), it reads as a restatement of the package's premise — sharing projection is by construction under ordinary Head, so it cannot favour one taxonomy unless the labelling consequence is spelled out.

**Status.** Not a defect; an untallied cost for one alternative and an under-exploited argument for the preferred package.

**Repair.** One paragraph after 672 stating the convention and its consequence for separate-D ordinary Head; rephrase 690 accordingly.

### 5. Number/count features of determinative-headed targets are never stated, and 615 restricts the target check to common nouns

**Where.** 615 (“The target restrictions concern the common-noun nominal being determined”); 650; 662; Table 5 (605–610).

**Derivation.** *The few* = $\mathrm{NP}_{few}\to\mathrm{Det}{:}\mathrm{NP}_{the},\ \mathrm{Head}{:}\mathrm{Nom}_{few}$. $C_{the}(\mathrm{Det},c)$ must check the target's number/count. Table 5 gives *few*'s own target (plural count), not *few*'s value *as* a target; §5 nowhere assigns number/count to determinative heads. Same for *these three* (*these* requires plural), *this much* (534), *the almost thirty*. All four accounts need it (CGEL's *the* must check a Nom whose head is a fused DP), so it is non-differential — but the fragment's showcase (*the few*, *the lucky few*) is unlicensed as stated, and 615's wording contradicts 650's.

**Status.** Coverage gap; non-differential.

**Repair.** One sentence: determinative heads carry number/count values used by the target check and agreement (e.g. *few/many/several*, cardinals ≥ 2: plural count; *much/little*: non-count); replace “common-noun nominal” at 615 with “target nominal”.

### 6. Notational gaps in the licensing predicate and in the permission inventory

**Where.** 646–650; 596; 605–610; 615; 638.

- **Signature.** $C_h(f,c)$ does not take the NP as an argument, yet the conditions it must check are conditions on the NP's own internal structure (Det present? Comp partitive or comparative?) relative to $f$ (Findings 1–2). Either write $C_h(\mathrm{NP}_h,f,c)$ or define $c$ to include the phrase's internal structure.
- **Independent** (596) covers subject and object only, but the partitive's inner NP (*the wine* as Comp of *of*, Figure 3) and §2.1's *with [some]* (103) need complement-of-preposition; extend the definition to argument functions generally.
- **Form vs lexeme.** Table 5 rows are word-forms (*she* vs *her*, 615; *my* with *mine* absent; *no/none*), while 638 indexes $h$ as “the lexical head”. §3.2 (322–324) says the account “has to respect” form selection and 734 counts it as non-differential, but the predicate is silent on it. State that $h$ ranges over forms, or add a form-selection clause to $C_h$.
- Common nouns have no rows, though 654–660 rely on their permissions and determination requirement; note that they are implicit.

**Status.** Formal slips; low cost; but Findings 1–2 cannot be repaired cleanly without the first two.

### 7. Complex determinatives are underivable from Table 5, and this touches the “one internal permission” claim

**Where.** Table 5 rows 606, 608; 662; with §2.4 at 225 and §4.4 at 532.

**Derivation.** *a few apples*, *a little water*, *many a*: $\mathrm{NP}_{few}\to\mathrm{Det}{:}\mathrm{NP}_{a},\ \mathrm{Head}{:}\mathrm{Nom}_{few}$ fails *a*'s singular-count target (606), correctly — so *a few* must be a complex-determinative entry, absent from the table. Then *a very few mistakes* (225) and *a lucky few* (the indefinite counterpart of the showcase *the lucky few*) interpolate a modifier inside the complex lexeme. The claim at 662 that “Degree *very* modifies *few* internally across dependent and independent uses” and 532's “one internal permission covers both constructions” do not extend to this third construction, on which §2.4 relies.

**Status.** Coverage gap, non-differential (fusion needs a special treatment too); open how the author wishes to enter it.

**Repair.** Add complex-determinative entries, and state whether *very*/*lucky* attach to *few* with *a* as a marker or to the complex head; if the former, note the interaction with *a*'s target.

### 8. §5.3: one systematic asymmetry unaddressed; otherwise the argument holds and is properly hedged

**Where.** 696–712; 594; 700.

- **Position.** 696 makes it a cost if NP degree modifiers' distribution “differed systematically from that of degree determinatives.” One such difference goes unmentioned: every NP degree modifier cited is pre-head (*three years old*, *a great deal smaller*, *lots better*; \**smaller a great deal*), while *enough* is post-head (*good enough*; \**enough good*). Since no other determinative postmodifies adjectives either (\**good much*), this is a lexical property of *enough* under all four accounts — non-differential — but the section should say so rather than leave its own criterion apparently unmet.
- **Attestations.** All four (704) are article-less NPs (*heaps, lots, miles*). They refute a *general* exclusion of NP modifiers from attributive AdjPs (706) but are equally consistent with a narrower exclusion of article-bearing NP modifiers, which CGEL's article-loss note (708) already handles separately. On either reading the attributive contrast is non-differential, which is the conclusion at 712; scope 706 to “as stated”.
- **Permissions.** 594 defers degree uses to §5.3, but §5.3 does not add a “modifier of AdjP/AdvP/VP/PP” permission to $U_h$ for *enough/much/little/no* (700). Add it, or say the fragment's licensing predicate is not extended to these uses.

**Status.** Mostly passes; conclusion appropriately hedged.

### 9. The fusion schema and Figure 5 assign different structures to the same account; one anti-recursion stipulation is untallied

**Where.** 676–686; Figure 5 (466–475); 686 (“Fusion applies once”).

The schema at 679 makes $(\mathrm{Mod}_{\mathrm{pre}})$ and $F{:}\mathrm{DP}_h$ sisters in a single Nom, so *the lucky few* is flat: $\mathrm{Nom}\to\mathrm{Mod}_{\mathrm{pre}}{:}lucky,\ \mathrm{Mod\text{–}Head}{:}few$. Figure 5 (right) draws a two-level Nom with the fused DP as Head of the inner Nom and Mod of the outer. The schema also does not express the double parentage that 684 describes in prose. Separately, “Fusion applies once” (686) is a stipulation the D-noun/fusion account needs to prevent the inner $\mathrm{NP}_h$ from carrying its own Comp/$\mathrm{Mods}_{\mathrm{post}}$; it is untallied, though it strengthens the manuscript's own redundancy argument at 688.

**Status.** Representational inconsistency; low priority.

**Repair.** Align the schema with the figure (recursive Nom or flat) and record the stipulation.

## Checks that pass

- **Design and derivations.** The 2×2 comparison (636) is coherent; 654–660 are correct under the stated rules; the article's exclusion from argument use is honestly stipulated (660); definiteness and single-Det are correctly described as functional statements not derived by recategorization (634).
- **Reciprocal selection.** Encoding Hudson's mutual dependence as two $C_h$ checks on the two heads (619, 652) is coherent and non-differential across accounts; it is also orthogonal to the comparison, since all four keep the common noun as head of *some apples*.
- **Redundancy argument against D-noun/fusion** (686–688): valid and independent — strictly more structure with no coverage gain.
- **Tree identity under the two ordinary-Head accounts** (690): verified against 669; identical modulo the head label (see Finding 4 for what the label costs).
- **Hudson invariance** (692): trivially true given lexical indexing of $U_h$/$C_h$; it also correctly implies the fragment cannot adjudicate §6, which 770 concedes.
- **Non-differential restrictions** (734): sound for the taxonomy comparison; correctly limited to that comparison.
- **Compounds**: Figure 7, 640, 664, 672 are mutually consistent (restrictor position, non-recursion, ordering before relatives at 572).
- **Multiple determinative lexemes per NP** (742) is consistent with the single Det slot in 645.
- **Hedging** at 590, 712, 746, 748 is appropriate; 748 supplies a genuine falsification criterion (Finding 1 engages it).
- **Possible sharpening (my inference, not a manuscript claim).** Given §4.6's ordinary-Head genitives, the package appears to remove Det–Head fusion from the grammar altogether, leaving Mod–Head for adjectives only. That is a crisper economy statement than “reducing fusion's applications” (500); it would need checking against the full CGEL inventory of Det–Head uses, which this packet does not contain.

## Independent argument vs restatement

- Independent: 688 (redundancy), 734 (non-differential restrictions), 704–708 (attributive attestations, with the scoping in Finding 8), 692 (invariance).
- Restatement: 690 (“alignment”), the first sentence of 746, “consolidates” at 634 (the count of realization classes is unchanged, as 634 itself says), and the “Taxonomic consequences” column of Table 7 (consequences of, not evidence for, the categorization — as 744 acknowledges).

## Prioritized repair list

1. State the Det/Mod-function internal restriction on determinative-headed NPs explicitly; enter it in Table 7; revise 634 and 748 (Finding 1).
2. Add an internal-Mod permission to $U_h$ and amend the definition at 596 (Finding 2).
3. Decide approximative attachment: uniform Nom-internal on determinative hosts, or keep peripheral and tally the second site with its evidence (Finding 3).
4. Add the labelling paragraph for separate-D ordinary Head; rephrase 690 as the redundancy argument (Finding 4).
5. Assign number/count values to determinative heads as targets; fix 615 (Finding 5).
6. Fix the $C_h$ signature; extend *Independent* to complement-of-preposition; state form-vs-lexeme indexing (Finding 6).
7. Enter complex determinatives and say where *very*/*lucky* attach in *a very few*/*a lucky few* (Finding 7).
8. In §5.3, note the pre/post-head asymmetry as lexical and non-differential; scope 706; add the modifier permission (Finding 8).
9. Align the fusion schema with Figure 5 and record the “applies once” stipulation (Finding 9).
