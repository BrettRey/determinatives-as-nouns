# Source reread, 19 September 2026: shared instructions

Manuscript: `/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns/determinatives-as-nouns.tex` (commit af63c84 plus one footnote edit at l. 137; SHA-256 of the text at dispatch: 2c6c7953c659274969e88599c6d86369313bb0212fd57df0e3b0cb2480158afe). Brett Reynolds's paper "Determinatives as nouns in English", a CGEL-framework syntax paper. The manuscript is READ-ONLY for you: do not edit it or any other project file except your own report.

## Task

This is the `source-reread` pass: check that each source says what the manuscript says it says. You have a list of citation contexts (sentence, line number, cited pages). For each one:

1. Open the cited page(s) in the source. Read the source, not your memory of it. Prefer the `.md` sidecar for searching; use the PDF (`pdftotext -f N -l N -layout file.pdf -`) when you need the printed page number. Work out the PDF-to-printed-page offset from running heads before trusting a page.
2. Quote the decisive source wording exactly (one to three sentences at most; these reports are committed to a public repository, so never paste long passages) with its printed page.
3. Give a verdict:
   - **SUPPORTED**: the source says it, at that page.
   - **NUANCE**: supported, but the manuscript's wording drops a hedge, broadens scope (some → all), shifts level (category vs function, word vs phrase), or otherwise says slightly more or less than the source. Say exactly what and propose minimal replacement wording.
   - **OVERSTATED** or **MISATTRIBUTED**: the source doesn't say it, or says something different. Quote what it does say. Propose a repair.
   - **PAGE**: content right, page wrong. Give the correct printed page and how you established it.
   - **UNVERIFIED**: you couldn't get the source. List every place and search string you tried.
4. Also sweep your line range (or your authors' surnames across the whole manuscript) for attributions that carry no `\cite` ("CGEL treats…", "Hudson argues…", "Van Eynde's…") and check those too.

For an empirical source, write down what the tables/figures show before reading the authors' interpretation, and keep the two apart in your report.

Pay particular attention to terminology levels. In CGEL, *determinative* is a lexical category and *determiner* a function; *fused head*, *Head*, *Det*, *Nom*, *NP*, *DP* (a determinative phrase, not Abney's DP) are distinct. A paraphrase that swaps category for function, or word for phrase, is a NUANCE finding at least.

A negative ("the source never says X") needs the search shown: the exact strings and files searched.

## Output

Write your full report to the path given in your task, as Markdown: a one-line summary, then a table or list with one entry per citation context (line, claim in brief, pages checked, quoted source wording, verdict, proposed repair if any), then any uncited attributions you found. Record which file and which page-offset you used for each source.

Return to the parent: counts per verdict, and every non-SUPPORTED item in full (line, problem, proposed wording). Keep the return under 600 words.

## Responsibility

You retain an individual duty to notify Brett of credible, material epistemic risks. If you find something material (a misattribution the argument depends on, a source that says the opposite), put a `RESPONSIBILITY NOTICE` at the start of your return. Do not seek unauthorized workarounds for an unavailable source; UNVERIFIED with the search shown is a valid result.
