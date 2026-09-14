# Proofread: Determinatives as nouns in English

13 September 2026 · Codex · current 36-page working draft

The manuscript is largely clean. I found one omission in the acknowledgements, one minor page-break issue, and three small wording or formatting improvements. This is a read-only proofread; the source and PDF are unchanged. No skills or additional reviewers were used.

1. Acknowledgements, p. 34 ([source line 895](/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns/determinatives-as-nouns.tex:895)). The model list omits the Fable reviews whose findings informed the revision. The [review manifest](../../reviews/fable-pairwise-2026-09-13/manifest.json) records `claude-fable-5-1`. Add the model to the existing list:

   GPT-6 (Astra), {++Claude Fable 5.1, ++}{#s1}Claude Opus 5, Claude Haiku 4.5, and GLM-5.3-Flash

2. Example (2), pp. 7–8 ([source lines 195–198](/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns/determinatives-as-nouns.tex:195)). Its last item, (2e) *multiple were injured*, is stranded at the top of p. 8. Keep (2d–e) together. The current `samepage` wrapper hasn't prevented this break; check the resulting placement of their footnotes when adjusting it.

3. Section 3.1, p. 15 ([source line 344](/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns/determinatives-as-nouns.tex:344)). The sentence shifts from singular *absence* to distributive *all* and plural *they*. I recommend aligning the subject with the three exclusions being compared:

   {~~Absence of bare, predicative, and partitive uses all limits~>The exclusions of bare, predicative, and partitive uses all limit~~}{#s2} occurrence without a following nominal; they aren't three independent reasons for a primary category.

4. Figure 2 caption, p. 17 ([source line 440](/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns/determinatives-as-nouns.tex:440)). Make the attachment of *ultimately headed by preferences* explicit. The present supplementary phrase can initially be read as describing the subject, *the genitive NP Kim's*:

   The genitive NP *Kim's* functions as determiner {~~within *Kim's preferences*, ultimately headed by *preferences*~>in the larger NP *Kim's preferences*, whose ultimate lexical head is *preferences*~~}{#s3}. The representation abstracts from the internal realization of genitive marking.

5. Two minor typography/source-consistency points. In example (3b), p. 8 ([source line 205](/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns/determinatives-as-nouns.tex:205)), *deeply concerned* drops out of the example's italics. Keep its source quotation marks but include the quoted words inside `\mention{}`: `\mention{he has heard from numerous who are \enquote{deeply concerned}}`. In §2.3 ([source line 152](/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns/determinatives-as-nouns.tex:152)), use `\enquote*{sure}` for the gloss currently entered as raw curly quotes, matching the gloss markup in §4.6. The latter change has no intended visual effect.

The spelling and repeated-word checks found no errors. Original source spellings such as *photo's* and the unhyphenated measure examples are explicitly preserved evidence. All 24 cited works occur in the compiled bibliography, all source cross-references resolve, and there are no duplicate labels or unresolved placeholders. Main prose paragraphs remain below 100 words after excluding their citations and footnotes.

The source matches the version underlying the verified 36-page PDF. I read the entire source, checked the rendered bibliography and all remaining pages, and reused the fifteen page inspections just completed on that identical PDF. Apart from the split example above, I found no clipping or collisions. The existing header, footnote-patching, and bold-font fallback warnings remain. This check covers citation presentation and internal consistency; it doesn't repeat the earlier external source-verification work.

---
suggestions:
  s1:
    by: Codex
    at: 2026-09-14T01:11:59.953Z
  s2:
    by: Codex
    at: 2026-09-14T01:11:59.953Z
  s3:
    by: Codex
    at: 2026-09-14T01:11:59.953Z
comments:
  c1:
    body: this didn't need an RD check. But you haven't aligned it to house style,
      have you?
    by: user
    at: 2026-09-14T01:13:27.810Z
