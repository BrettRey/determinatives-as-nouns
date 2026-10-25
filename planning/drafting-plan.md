# Drafting plan: the category paper (rebuild for ELL)
<!-- SUMMARY: how the category paper ("Determinatives as nouns in English") will be rebuilt for English Language and Linguistics as an entirely new paper: budget, counting method, order of work, and the changes from the fusion paper's process · status: steps 1–3 done 24 Oct; discovery loop built (drafts/needs.tex, tools/evidence_needs.py) and ledger seeded (planning/evidence-ledger.md, 25 rows); next: the structure review · updated: 2026-10-24 -->

Agreed with Brett on 24 Oct 2026 ("OK, let's get to work on it"; "proceed"). Venue record: `submission/venue-decision-2026-10-24-taxonomic.md` (gitignored). Terms: `planning/terms.md`.

## Target and budget

- **Venue:** *English Language and Linguistics*, as an entirely new submission (ELL-2026-0119 is superseded).
- **Limit:** "no more than 10,000 words, including references and footnotes" (ELL, read 15 Oct). An exception can be argued in the cover letter; don't plan on one.
- **Target: 9,000 words** on the inclusive PDF count, leaving 10% for review changes.
- **Rough allocation:** references about 900 (the combined paper had 62 entries; aim for about 45); title, abstract, and AI statement about 300; body, footnotes, examples, tables, and trees about 7,800. Section budgets are set at the structure review and must sum to that.
- **Counting:** `python3 tools/pdfwords.py <built pdf>` from the first build on, the same method the fusion paper ended on. It counts everything on the page, tree labels included, so it errs high. Don't use texcount for the limit.
- **Scale check:** the combined manuscript counts 19,972 on this method, so the rebuild is about half its length.

## The paper (Brett's choice, 24 Oct)

The English-grammar paper: English corpus evidence, argued against *CGEL* and the Postal / Sommerstein / Lyons / Hudson / Abney tradition, with no cross-linguistic section beyond what the framing needs. Opening question: **is there a lexical category Determiner?**, on the model of the auxiliary debate (Pullum & Wilson 1977; Gazdar, Pullum & Sag 1982), with Hudson 2000, 2004 (determiners inside pronoun, inside noun) and Van Eynde 2003 (determiners "categorially heterogeneous") as the prior answers. Claims to state as new: every English determinative is nominal (against Van Eynde's split), and determinative is coordinate with pronoun (against Hudson's nesting). A cross-linguistic section from Lyons 1999 and Diessel 1999 is the later route to *Language* or *Linguistics*; it doesn't change the question.

## Order of work

1. ✅ Venue approved; term sheet; budget; counting tool (24 Oct).
2. ✅ Neighbouring papers adjudicated (DECISIONS, 24 Oct).
3. ✅ **Seed the evidence ledger** (`planning/evidence-ledger.md`), not a full inventory. Done 24 Oct: 25 rows, 3 open; the ledger's closing section says what the seed shows. One row per diagnostic already in hand (from `notes/split/2026-10-15-allocation.md`, the ELL triage's punch list, and the records in `corpus/`), with the four rival predictions filled in: *CGEL* (a separate category), Hudson (nested in pronoun), Van Eynde (split between adjective and noun), and coordinate (this paper). Mark which rows discriminate. The existing records were not built to test coordination against nesting (`analysis/README.md` says so), so expect gaps; they are found and filled during drafting, not before it.
4. **Structure review.** Muse, told to ignore the old manuscript and plan for ELL's reader, given the seeded ledger; plus a self-described outsider reader (an English linguist who doesn't use *CGEL*). Output: sections with budgets summing to about 7,800 body words.
5. **Draft section by section** in `drafts/`, in the agreed order, introduction and abstract last. Each section runs the **discovery loop** (Brett, 24 Oct: "often it's only in writing the paper that I realize what I should be looking for"):
   - draft quickly; wherever a claim needs data we don't have, drop `\needs[id]{what would show it}` (defined in `drafts/needs.tex`; prints red in draft builds) rather than stopping;
   - at the end of the section, `python3 tools/evidence_needs.py` merges the markers into the ledger;
   - fill the four prediction columns for each new row; rows where all four agree are illustration, not evidence, and aren't worth a search;
   - for the discriminating rows, Claude proposes the search (corpus, query, what count would settle it); Brett runs it by hand or approves `/corpus-screen`; the record goes in `corpus/` and its path in the ledger;
   - revise the section on the results. A result that surprises us (a failed prediction, a new contrast) is flagged in the ledger and in `drafts/SECTION-NOTES.md`, and triggers a quick check of the structure before the next section;
   - then verify pages, quotations, examples and numbers (the fusion paper's claim and quotation ledgers, adapted); one review and one triage round; the section's result in one sentence in `drafts/SECTION-NOTES.md`.
   - The submission build sets `\needsfinaltrue`, so any open marker stops it; `python3 tools/evidence_needs.py --check` is the same check for the gate.
6. **Assemble, then the reader pass at once** (in-order read by a fresh reader), then terminology hygiene.
7. **One outside review round** after assembly: two model families plus the outsider persona. No further rounds unless the text changes structurally.
8. **Finish:** contribution alignment, negative claims, numbers audit (Codex), proofread, AI statement from the log, anonymized copy, submission gate.

## Changes from the fusion paper's process, and why

| Change | Fusion-paper problem it answers |
|---|---|
| A discovery loop with a ledger, instead of evidence-first (revised 24 Oct at Brett's point that needs appear while writing) | Claims changed only after corpus checks ran mid-draft (the genitive concession, 16 Oct); needs found while drafting were tracked ad hoc in prose and DECISIONS. The rival-prediction columns decide which needs are worth a search. |
| Verify each section as drafted | Deferred checking left 12 source errors for the 23 Oct reread and uncredited *CGEL* examples for the 24 Oct proofread. |
| Term sheet first | "Ordinary Head" named two things until the final reader pass; "word class" leaked through a day of venue work. |
| One count method, budget to 90% | Mixed counting tools cost a correction; the draft reached 17,095 words before trimming. |
| Outsider reader at the structure stage | The April persona boards were all *CGEL* insiders (venue lessons, 7 Sep). |
| Reader pass right after assembly | Its structural findings came after the polishing passes. |
| AI-use log from day one | The 24 Oct disclosure had to be reconstructed and missed five tools. |
| Fewer review rounds | Five model reviews and four triage rounds on 18–21 Oct, partly contradictory. |

## AI use

Log every tool and use in `notes/ai-use-log.md` as it happens.
