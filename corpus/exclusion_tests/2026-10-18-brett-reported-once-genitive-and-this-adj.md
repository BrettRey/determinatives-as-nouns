# *Once*, *twice*, and *thrice*: genitive, and *this* + adjective (18 October 2026)
<!-- SUMMARY: two negative results reported by Brett, lines not pasted; once/twice/thrice 's: no genitive in COCA, NOW, or iWeb (used in the structural paper's §5); this last.[j*]: no hits, but CLAWS7 tags last MD; rerun this last.[md*] once: none in COCA or NOW, 4 iWeb lines, none the NP · status: done; the last twice not yet searched · updated: 2026-10-18 -->

Both searches were run by hand by Brett Reynolds on english-corpora.org, in COCA, NOW, and iWeb. He reported the results in the session and confirmed the query strings; no lines were pasted, so there is nothing to classify. In this syntax `/` separates alternatives (confirmed by Brett, and by `[at*] someone/somebody/something`, which returned all three words), and `word.[pos]` restricts a word to a tag.

## 1. Genitive

**Question.** §3 of the structural paper (*Fusion of functions revisited*) finds that the genitive divides the fused determiner-heads word by word (*either's*, *each's*, *everyone's* against *many's*, *few's*). Do *once*, *twice*, and *thrice* take the genitive?

**Search.** `once/twice/thrice 's`, in COCA, NOW, and iWeb.

**Result.** "No relevant hits" (Brett, 18 October). Hits that aren't genitives, such as *'s* for *is* or *has*, weren't relevant.

## 2. *This* + adjective

**Question.** Payne, Huddleston & Pullum (2007: 589) exclude \**last once* "for the same reason as" \**last one time*, while *this last once* is fine. Their (16b) is *just this last once* (p. 586), and their examples are "for the most part direct attestations from web-based sources" (p. 584 n. 22); one *JL* referee judged it ungrammatical (p. 586 n. 26). Does *this* with an adjective before *once*, *twice*, or *thrice* occur in the corpora?

**Search.** `this last.[j*] once/twice/thrice`: *this*, then *last* tagged as an adjective, then *once*, *twice*, or *thrice*. COCA, NOW, and iWeb.

**Result.** No hits in any of the three corpora.

**Why the result can't be used.** In the CLAWS7 tagset, MD is "ordinal number (e.g. first, second, next, last)" (UCREL, ucrel.lancs.ac.uk/claws7tags.html, checked 18 October 2026), while `[j*]` matches the JJ tags (general, comparative, and superlative adjectives). That English-Corpora.org's corpora are tagged with CLAWS7 is from memory, not checked here. If they are, `last.[j*]` matches only the rare tokens of *last* tagged JJ, and the zero says little about *this last once*. The search to run is `this last once/twice/thrice`, with no tag, and for Payne et al.'s *the last twice* (p. 595, (33b)), `the last once/twice/thrice`.

**Rerun.** Brett reran it as `this last.[md*] once`, with *last* tagged as an ordinal (18 October). COCA and NOW: no hits. iWeb: four lines, pasted, none with *this last once* as an NP:

| Line | Reading |
|---|---|
| *How long does this last once the oils are mixed?* (humblebeeandme.com) | verb *last*, sequential *once* |
| *how long does this last once made??* (carnation.co.uk) | verb *last*, sequential *once* |
| *is it best to go clockwise to do this last once aclimatised?* (outdoorsmagic.com) | *do this last*, then sequential *once* |
| *This last once focuses on type* (vanseodesign.com) | slip for *this last one* |

The four hits confirm that the `[md*]` tag finds *last* in iWeb. `this last.[md*] twice/thrice` and Payne et al.'s *the last twice* (`the last.[md*] once/twice/thrice`) aren't searched yet.

## Reading

The genitive is absent from *once*, *twice*, and *thrice* in all three corpora, as it is from *many* and *few*; the structural paper's §5 uses this in a footnote. The first run of the second search didn't test Payne et al.'s *this last once*, for the reason above. The rerun did: no *this last once* in COCA, NOW, or iWeb, which §5 now reports beside the referee's dissent.
