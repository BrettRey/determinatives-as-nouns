#!/usr/bin/env python3
"""The forms table: every matrix row, with the plain label blind coders see
(no category names), the CGEL category (hidden from coders), and its source.
Reference-set rows (nouns and adjectives, 24 Oct 2026) are included, as forms:
dog and dogs separately. Claude's proposals; labels follow the 2021 forms.

Writes analysis/codebook/forms.csv (form, blind_label, category, source).
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

SPECIAL = {
    "a_certain": "a certain, as in a certain person", "a_few": "a few", "few": "few, as in Few people came (not a few)", "little": "little, as in little time (not a little)", "a_great_many": "a great many",
    "a_little": "a little, as in a little water", "many_a": "many a, as in many a day",
    "no_one": "no one", "one_det": "one, the numeral, as in one book", "two_det": "two",
    "three_det": "three", "us_det": "us, as in us linguists", "we_det": "we, as in we linguists",
    "you_det": "you, as in you linguists", "what_det": "what, as in What book? / what money we had",
    "whatever_det": "whatever, as in whatever book you like", "which_rel_det": "which, relative, as in during which time",
    "which_int_det": "which, interrogative, as in Which book? / Which do you want?",
    "whichever_rel_det": "whichever, as in whichever book you choose",
    "whichever_int_det": "whichever, as in Whichever do you mean? (interrogative)",
    "zero_det": "zero, the numeral", "various_det": "various", "each_other": "each other",
    "one_another": "one another", "her_acc": "her, as in I saw her", "her_dep": "her, as in her book",
    "it_plain": "it, referring, as in It broke", "it_dum": "it, as in It's raining",
    "one_pron": "one, generic, as in One shouldn't judge", "one_s": "one's", "their_sing": "their, of one person",
    "theirs_sing": "theirs, of one person", "their_plur": "their, of several", "theirs_plur": "theirs, of several",
    "them_sing": "them, of one person", "them_plur": "them, of several", "they_sing": "they, of one person",
    "they_plur": "they, of several", "we_pron": "we, as in We left", "us_pron": "us, as in They saw us",
    "what_pron": "what, as in What happened?", "whatever_pron": "whatever, as in Whatever happened, happened",
    "which_rel_pron": "which, as in the book which I read", "who_int": "who, as in Who came?",
    "who_rel": "who, as in the person who came", "whom_int": "whom, as in Whom did you see?",
    "whom_rel": "whom, as in the person whom I saw", "whose_int": "whose, as in Whose is this?",
    "whose_rel": "whose, as in the person whose book I took", "whoever_s": "whoever's",
    "whosoever_s": "whosoever's", "you_pron_sing": "you, of one person", "you_pron_plur": "you, of several",
    "your_sing": "your, of one person", "yours_sing": "yours, of one person", "your_plur": "your, of several",
    "yours_plur": "yours, of several", "there": "there, as in There's a problem",
    "last": "last, as in last week", "next": "next, as in next week", "once": "once, as in once a day",
    "twice": "twice", "thrice": "thrice", "somewhat": "somewhat", "such": "such, as in such a day",
    "certain": "certain, as in certain people", "sufficient": "sufficient", "enough": "enough",
    "the": "the", "a": "a / an", "I": "I",
}
REFERENCE = [  # (form, blind label, category)
    ("lot", "lot, as in a lot of people, A lot was spent", "common noun"),
    ("number", "number, as in a number of problems", "common noun"),
    ("numbers", "numbers, as in huge numbers of ants", "common noun"),
    ("plenty", "plenty, as in plenty of time, There's plenty", "common noun"),
    ("dozen", "dozen, as in a dozen eggs", "common noun"),
    ("dozens", "dozens, as in dozens of errors", "common noun"),
    ("majority", "majority, as in the majority of voters", "common noun"),
    ("dog", "dog", "common noun"), ("dogs", "dogs", "common noun"), ("water", "water", "common noun"),
    ("Kim", "Kim, a personal name", "proper noun"), ("Toronto", "Toronto, a place name", "proper noun"),
    ("numerous", "numerous", "adjective"), ("multiple", "multiple, as in multiple problems", "adjective"),
    ("countless", "countless", "adjective"), ("rich", "rich", "adjective"), ("poor", "poor", "adjective"),
    ("tall", "tall", "adjective"),
]


def main():
    cat = {}
    for r in csv.DictReader((ROOT / "analysis" / "data" / "word-mapping.csv").open()):
        cat[r["working_name"]] = r["category"]
        cat[r["public_name"]] = r["category"]
    cat["whomever"] = "pronoun"
    m = list(csv.reader((ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv").open()))
    rows = []
    for r in m[1:]:
        f = r[0]
        rows.append((f, SPECIAL.get(f, f.replace("_", " ")), cat[f], "matrix-2026-10"))
    rows += [(f, lab, c, "reference set 2026-10-24") for f, lab, c in REFERENCE]
    with (HERE / "forms.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "blind_label", "category", "source"])
        w.writerows(rows)
    leaks = [l for _, l, _, _ in rows if any(k in l for k in ("_det", "_pron", "determin", "pronoun"))]
    print(len(rows), "forms; labels containing category words:", leaks)


if __name__ == "__main__":
    main()
