# Build integrity

The full `make all supplements` sequence completed with XeLaTeX, Biber and the resolving XeLaTeX passes, serially for the three documents. The log is `2026-09-09-final-build.log`; the final-log summary is `2026-09-09-build-check.json`.

| Document | Pages | Result |
|---|---:|---|
| determinatives-as-nouns.pdf | 24 | Builds; 23 citation keys; 33 labels resolve; six figures, eleven trees and five tables retained. |
| matrix-audit.pdf | 3 | Builds; its table input and references resolve. |
| corpus-documentation.pdf | 3 | Builds; its table input, example labels and references resolve. |

The fingerprint driver finds the main source and its preamble without unresolved inputs. The generated supplement inputs exist and were included by the builds. No year-pinned TeX Live path occurs in the preamble. `references.bib` is the expected symlink to the central house bibliography. `git diff --check` passes; the three current untracked TeX sources also have no trailing-whitespace issue. No TODO/FIXME/VERIFY placeholder or literal unresolved `??` was found.

There are no compilation errors, unresolved citations/references, or outstanding rerun requests. The article retains four small overfull lines: 4.47, 5.04, 4.29 and 1.28 pt. The supplements have none. The existing preamble also reports fancyhdr one-sided-header warnings, a microtype footnote patch warning, and an EBGaramond bold-shape substitution in the article. No font-loading failure occurs. These presentation issues remain for the deferred visual/layout pass.

PDF text extracts without replacement characters or unresolved-reference marks. The article's complete extracted text is byte-identical to the version read by the independent board: the only subsequent article-source edit removed an unused macro. Supplement audit-provenance wording is current in the built files.

This confirms build and text integrity. It does not claim a new image, layout or accessibility proof; the author asked to pause image inspection.
