# Review-board synthesis

The paper's principal question is now legible, and the full readers consistently recover the distinction between nounhood, ordinary headedness and rank within Noun. The most useful remaining objection concerns the criterion for preferring inheritance through Noun over the separate-D account that shares the same nominal projection. This warrants focused argument work; it does not warrant treating the proposal as refuted or implementing the reviewers' expansion requests wholesale.

The six named perspectives all recommend revision. Their agreement is a simulated response to a shared task, not evidence of field consensus. The two readers given only the artifact, goal and audience independently raise the criterion, adjective comparison and restricted-member questions. That increases confidence that these are properties of the draft rather than products of the named-review prompt. Their preferred remedies still differ and require editorial judgment.

## Inputs and limits

The run examined the frozen article with source SHA-256 `46cdd40308ebe997cd0294131848b5c5eca7ba13691f889c6015c4f39f29afb1`, plus the two supplementary sources. Exact prompts, complete responses and model/provider metadata are preserved beside this report. The main article was supplied in full, including its table and tree source. The generated bodies of the two supplementary tables were omitted from the initial packets. They are now preserved in `supplement-table-inputs.md`, explicitly identified as a later addition; the original readers did not see them. This board supplies no independent numerical validation. The earlier computational audit and Sol check provide that separate evidence.

The native readers used GPT-6 Astra. The Anthropic sessions report Claude Opus 5, with auxiliary Haiku usage in their metadata. The OpenRouter readers used GLM-5.3 Flash. None saw another reader's report or the earlier revision history.

## Findings by reading lane

| Lane | Most useful finding | Qualification |
|---|---|---|
| [Pullum / Astra](pullum.md) | The strongest separate-D account states shared projection too; the adjective comparison and article integration must justify the preferred boundary. | Does not demand unique coverage or a numerical economy metric. |
| [Hudson / Astra](hudson.md) | Apply a consistent standard to inheritance through Noun and through an intermediate pronoun category. | Correctly distinguishes testing a hierarchy within fixed rules from testing a complete dependency grammar. |
| [Payne / Opus](payne.md) | A rule stated once over N-or-D challenges the “otherwise repeated generalizations” criterion. | Several further objections overlook the current scope of the few comparison or explicit modifier restrictions. |
| [Van Eynde / Opus](van-eynde.md) | A potentially adjectival subset deserves consideration; make the allocation of conditions inspectable. | The asserted co-variation of English diagnostics is not established by this review. It must not be treated as a result. |
| [Spinillo / GLM](spinillo.md) | Restricted-member integration and the redistribution alternative need comparison. | Its inference from matrix separation to hierarchy is invalid, and its description of clustering stability conflicts with the supplied prose. |
| [Lyons / GLM](lyons.md) | The weight given to nominal structure needs justification relative to modifier differences. | Required typological predictions and a new cross-linguistic subsection exceed this paper's stated synchronic English scope. |
| [Reader without supplied diagnosis / Astra](clean-astra.md) | Coherence is demonstrated more clearly than preference; put adjectives and determinatives on equal comparative terms. | Offers useful alternatives, but broad cutting and reordering remain editorial suggestions. |
| [Reader without supplied diagnosis / Opus](clean-opus.md) | Clarify the criterion and the two-step restricted-member inference; spell out selected conditions. | Introduces a stronger unique-coverage demand, questionable diagnostic claims, and requests to restore empirical material the author deliberately relocated. |
| [Potential citing reader / GLM](audience.md) | Can recover the main claim and the supplements' limited roles. | Understates the separate-D ordinary-Head rival, overstates what is settled, and misnumbers several references. Its confident summary is not evidence that the argument succeeds. |

## What direct checking adds

The adjective concern has a specific source basis beyond the reviewers' general pressure. CGEL pp. 416–417 describes ordinal fused heads and independent expressions involving colour, provenance, age and size, including bare NPs. The current manuscript discusses human-class and comparative/superlative cases, but does not compare these further families. Its local statement about *the rich* is accurate; the broader comparison is incomplete. Exact text from PDF pages 436–437 is preserved under `notes/passes/2026-09-09-adjective-source-page-*.txt`.

The concern about the intermediate category is also directly inspectable. §5 says it would be useful if it collected otherwise repeated generalizations, whereas §7.2 gives the separate-D rival one shared nominal rule. This exposes a question about the criterion's application; it does not show that coordination is asserted as an established result. The text repeatedly marks it provisional.

The articles' inference is conditional rather than formally circular: their integration into determinative, together with the category-level nounhood argument, supports their inclusion. The open question is the strength of those two premises. Substitution in Det cannot by itself distinguish lexical membership, because the paper expressly admits other categories in that function. The *my/mine* comparison supplies a precedent for restricted members but a different kind of paradigmatic connection.

Other checks defeat several purported omissions. The manuscript explicitly retains fusion with nounhood through *mine*, restricts the ordinary-Head unification claim to independent uses, states base-specific compound premodification and post-head restrictor conditions, and already cites *the other two*, *these few here* and *the many who did*. The original numerical auditor both reran the scripts and independently recomputed DISCO components and corpus counts. A description of that work as mere repeat execution would be inaccurate; identifying it as model-assisted is a useful clarification.

## Contradictions to preserve

Payne and Lyons regard the restricted-member section as a strength; Pullum and both readers without a supplied diagnosis find its inferential connection insufficient. Van Eynde proposes a heterogeneous determinative category, whereas the other readings often assume the retained inventory. These are different analytical pressures, not a single consensus remedy.

The Opus reader without a supplied diagnosis asks for differential predictions or a reframing around criteria. Pullum and Hudson explicitly accept that a defended architectural principle could suffice without superior coverage. The synthesis does not promote the stronger demand into an acceptance condition.

Several readers recommend reducing qualifications or moving the fragment earlier. Others regard the present distinctions and fair treatment of fusion as the paper's chief virtues. Given the recent author-directed reordering and the earlier loss of premises during cutting, these recommendations do not justify a fresh broad rewrite.

## Priorities

1. Compare the wider adjectival families with determinatives before choosing a stronger criterion or adjusting the conclusion.
2. State and apply one criterion consistently to shared Noun membership and the optional intermediate pronoun category.
3. Make the restricted-member inference explicit about its different kinds of positive connection; compare redistribution where it changes the accounting.
4. Consider a compact ledger of already stated lexical and constructional conditions, without treating condition counts as a theory-neutral economy metric.
5. Clarify computational-audit provenance and complete ordinary mechanics. Preserve the corpus relocation, the inclusion claim and the author's hierarchy of commitments pending the substantive decision.

The detailed dispositions are in [the objection ledger](../../notes/review-triage/2026-09-09-objection-ledger.md). Proposed author-facing next steps are in [the morning note](../../notes/2026-09-09-overnight-pass-review.md).
