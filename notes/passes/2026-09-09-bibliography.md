# Bibliography integrity and merge check

The current article and both standalone supplements were checked, including their generated table inputs and the central/local bibliography arrangement. The active main source is `determinatives-as-nouns.tex`; scanning obsolete `main.tex` paths would miss this paper.

The central bibliography contains 2,190 entries; the local file contains four. There are 23 distinct main-text citation keys and 24 across the three documents. None is missing. Cited entries have non-empty author, title and year/date fields, with plausible years. All four local entries are used. The 2,170 central entries unused in this project belong to a shared bibliography and are not deletion candidates. The final Biber runs resolve all citations without a rerun request.

The structured check, complete key lists and relevant field comparisons are in `2026-09-09-bibliography-check.json`. This is an integrity check; bibliographic and source verification is documented in the preceding source pass and September 7 records, rather than regenerated from memory.

## Central merge

The sanctioned push-bib dry run found these cases:

| Local key | Central comparison | Result |
|---|---|---|
| sommerstein1972 | No duplicate | New entry eligible to merge once the central file is ready. |
| reynolds2021matrixpublic | reynolds2021matrix | Duplicate title/year; central note incorrectly describes the inspected public file as having 232 features. Preserve the locally verified 155-feature description. |
| reynolds2023unified | arora2023unified | Duplicate title/year; central author order is wrong and its record is less complete. The local record has Reynolds, Arora and Schneider, and the verified ACL DOI. |
| reynolds2025proformgender | reynolds2025proform | Duplicate title/year; central note says in preparation, while the verified local record says submitted. |

No entry was merged or substituted with degraded central metadata. The central file already has uncommitted changes. The [push-bib skill](</Users/brettreynolds/.codex/skills/push-bib/SKILL.md>) requires: “The script refuses to write when the central bib has uncommitted changes.” I did not use an override or commit/stash unrelated work. The correct local entries keep the manuscript build complete. The merge is explicitly deferred, not recorded as completed.
