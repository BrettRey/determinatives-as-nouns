# *These rich* with no noun: COCA, iWeb, NOW, 21 October 2026
<!-- SUMMARY: 14 distinct lines have adjective "rich" heading the nominal after "these" (COCA 2, iWeb 5, NOW 7), plus 2 NOW lines of "many educated" (addendum), mostly in blogs, comments, and news from Pakistan, India, the Philippines, and Nigeria, often after an earlier "the rich"; the rest are attributive (3), a name (1), spam (1), a duplicate (1); against CGEL p. 417 (determined by the definite article; *these very poor), with Glass 2019: 7 · status: record; labels Claude's · updated: 2026-10-21 -->

**Source.** The query was *these rich [v\*]*, named by Brett Reynolds for COCA. He ran it by hand on 21 October 2026 in COCA, iWeb, and NOW and pasted the displays into the Claude session.
- COCA: 2 rows.
- iWeb: 7 rows.
- NOW: rows 1–5 and 8–13. Rows 6 and 7 are absent from the site's display itself; Brett confirms he pasted everything it returned (as with the gap in the *every of* display, 19 October).

Whether the displays are the whole frequency isn't recorded. Raw lines and per-line labels are kept privately in the fusion repo (`reviews/corpus-these-rich-20261021/`, gitignored; raw.txt sha256 4629dc03…, labels.tsv sha256 68f35874…). Labels are by Claude (Opus 5.5), in one pass.

**Why it was run.** *CGEL* says NPs of the *rich* type "are determined by the definite article – we couldn't even substitute a demonstrative: ∗*these very poor*" (p. 417). The fusion paper already reports genitives (`mod-head.tex`, 19 of 500 COCA lines). Glass (2019: 7) cites *These rich live in apartment houses* from the web, along with *some fired*, *many educated*, and *too many homeless*. The side-agent check of 21 October flagged that Table 1 says *rich* takes only *the* or a genitive.

**Result.**

| Label | Lines | Example |
|---|---|---|
| *These* + *rich* heading the nominal | 14 | *These rich earn enormous income* (*Daily Times*, Pakistan, 2019, NOW 9); *These rich want to run the schools like a business* (cliffmass.blogspot.com, iWeb 5); *How many of these rich have taken the time …* (scotsnewsletter.com, iWeb 6) |
| *Rich* attributive, noun follows | 3 | *these rich playing resources* (NOW 2); *these rich entitled impenetrable alphas* (*Guardian*, US, NOW 10) |
| Personal name | 1 | *these Rich remembers* (BBC, NOW 13) |
| Spun or spam text | 1 | iWeb 4 |
| Duplicate | 1 | iWeb 7, a near-copy of iWeb 6 |

**Sources of the 14.**
- COCA: 2, both from one blog post.
- iWeb: 5, from blogs, a newsletter, a travel site, and a translation on marxists.org.
- NOW: 7, from news sites in Pakistan (2), India (2), the Philippines (1), and Nigeria (1), plus a British paper. The British line is a reader's comment quoted in the article. One Indian line is inside a quotation.

None comes from edited US or British news prose. In at least five, an earlier *the rich* or *you rich* is in view: COCA 1 and 2, iWeb 1, and NOW 9 and 11.

**Bearing.**
- *These* does occur with *rich* heading the nominal, so *CGEL*'s "determined by the definite article" is too strict here as it is for the genitive.
- The use is marked. It's concentrated in unedited web text and in outer-circle news, which matches Glass's own caution (2019: 6) and the pattern in the fusion paper's *lucky few* footnote.
- *CGEL*'s star is on *these very poor*, with a degree modifier, and none of these lines has one. So the lines show the demonstrative with *rich*. They don't refute the starred example as such.
- On both analyses the range of determiners is stated word by word. The result changes Table 1's cell and `mod-head.tex`'s sentence, not the comparison.

## Addendum: *many educated*, 21 October 2026

**Source.** Brett ran *many educated [v\*]* by hand the same day. The two lines reappear in his later *many/some educated [v\*]* display, recorded in `2026-10-21-brett-supplied-some-educated-many-unemployed.md`. It returned nothing in COCA or iWeb and 2 lines in NOW, both pasted. The raw lines are in the same private directory (raw-many-educated.txt, sha256 215dee2c…).

**Result.** Both lines have *educated* heading the nominal after *many*:
- *That's why many educated want to join PAP and stand for election* (*The Independent*, Singapore, 2016);
- *Many educated feel that denying access to knowledge resources is detrimental …* (*The Hans India*, India, 2016).

Glass's example (2019: 7) is from the web: *Many educated are far from role models*.

**Parsing.** *Educated* here is the *rich* type (*CGEL* includes participle-based adjectives such as *the unemployed*, p. 417). It isn't a post-head restrictor after a bare *many*, because bare *educated* doesn't follow a noun the way *present* does (\**people educated*, though *people educated at Oxford* is fine).

**Bearing.** *Many* occurs as the determiner of a nominal headed by an adjective of the *rich* type, but rarely. Both lines are from news outside Britain and the United States, the same distribution as *these rich*.
