#!/usr/bin/env python3
"""Normalize the census into a queryable derived layer.

census.json and census-repartitioned.json are left untouched. Every claim gains:

  lexeme_ids / phrases / class_id   mechanical, from the expression's \\mention forms
  subcategory                       from the lexeme table (extended here) or the class
  construction_id                   controlled catalogue: the 11 ids of the expanded run
                                    plus the extensions below; assigned by an external
                                    model in strict-JSON batches, then compared with the
                                    56 keyed manuscript claims of the expanded run
  basis_signals                     mechanical: what the manuscript shows at the locus
  evidence_type_reconciled          a stated precedence rule over basis_signals, falling
                                    back to the census label

Outputs: census-normalized.json, normalize-log.json, normalize-key-check.json.
Model calls (Haiku 4.5 via the Claude CLI, structured output, tools and MCP off) are cached in
normalize-cache/ by prompt hash, so reruns are free.
"""
import collections, concurrent.futures as cf, hashlib, json, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CACHE = HERE / "normalize-cache"; CACHE.mkdir(exist_ok=True)
TEX = ROOT / "determinatives-as-nouns.tex"
ENRICHED = ROOT / "analysis/claims/claims-enriched.json"
MODEL = "Claude Haiku 4.5 (claude CLI --model haiku, tools and MCP disabled)"
BATCH = 20

EXT = [
    ("genitive_marking", "The phrase takes genitive marking or has a genitive form (Kim's, my/mine, whose)."),
    ("number_agreement", "The phrase controls or transmits subject-verb agreement or number (number transparency, singular/plural selection)."),
    ("number_inflection", "The phrase inflects for number (plural -s) or lacks a number contrast."),
    ("grade_inflection", "The phrase has comparative or superlative inflection or a grade paradigm (fewer/fewest, more/most, less/least)."),
    ("predeterminer_mod", "The phrase functions as predeterminer modifier before a determined NP (all the books, both these)."),
    ("coordination_marker", "The phrase functions as a marker of coordination (both ... and, either ... or, neither ... nor)."),
    ("compound_base", "The phrase is the determinative base of a compound (anyone, something, nothing) or the claim concerns a compound's modifier domain."),
    ("fused_head", "The claim concerns the fused-head analysis (fused determiner-head or modifier-head) of the phrase, or an ordinary-Head versus fusion comparison."),
    ("external_determination", "The phrase, itself determinative-headed, takes an external determiner (the few, the lucky few, a certain, the very few)."),
    ("taxonomic_or_meta", "The sentence makes a taxonomic, analytical, or methodological statement about a category or class, not a claim about a specific construction."),
    ("other", "None of the above. Give other_label in a few words."),
]
RULES = """Assignment rules (they align this task with an existing keyed extraction):
- subject, object, complement of a preposition, 'independent use', pro-form or anaphoric use, NP use without a following nominal -> independent_argument. A relative-clause postmodifier on such a phrase does not change this.
- an independent phrase with a partitive of-PP -> independent_partitive.
- Det or determiner before a separate nominal (the book, few doctors, some teachers) -> dependent_det. Internal Mod / attributive position before a separate nominal (numerous people, the rich man) -> dependent_internal_mod.
- a degree adverb attached INSIDE the phrase (very few, so many, too much, how little, as few as, quite a few) -> internal_mod_admission. An adjective inside the phrase (the lucky few, poor old me, lucky you) -> internal_mod_admission.
- an approximative or focusing adverb attached OUTSIDE (almost every, nearly all, hardly any, practically no, only you, absolutely nothing) -> peripheral_mod_admission.
- the phrase itself modifies an adjective (a great deal better, enough good, plenty big, two years old) -> degree_modifier_adj; the phrase modifies a verb, adverb, preposition, determinative or comparative (I hadn't prepared enough, this big, a lot more) -> degree_modifier_nonadj.
- predicative complement of a copula (they are many, that is mine) -> predicative_complement; than-phrase -> comparative_complement; existential there -> existential_displaced_subject.
- if the sentence is about the analysis of the phrase (ordinary Head, fusion, ultimate lexical head, constraint fragment rows that only restate a permission) choose the construction the permission concerns, not fused_head, unless fusion itself is the point.
- Use taxonomic_or_meta only when no construction is at issue. Use other only when nothing fits, and say what in other_label."""

CITE = re.compile(r"\\(?:textcite|citep|citealp|citeyear|cite)\s*(?:\[[^\]]*\])*\s*\{([^}]+)\}")
MENTION = re.compile(r"\\mention\{([^{}]+)\}")
SENT_SPLIT = re.compile(r"(?<=[.?!])\s+(?=[A-Z\\(\u2018\u201c])")
CLASS_PAT = [("class:proper_noun", r"proper[- ]noun", "proper noun"), ("class:common_noun", r"common[- ]noun", "common noun"),
             ("class:pronoun", r"pronoun", "pronoun"), ("class:article", r"\barticles?\b", "determinative"),
             ("class:determinative", r"determinative", "determinative"), ("class:adjective", r"adjectiv", "adjective (control)"),
             ("class:quantifier", r"quantif", None), ("class:numeral", r"numeral|cardinal", "determinative")]


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def orx(system, prompt, max_tokens=None, schema=None):
    """Call Haiku 4.5 through the Claude CLI with structured output. Cached by prompt hash."""
    key = hashlib.sha256((MODEL + system + prompt + json.dumps(schema, sort_keys=True)).encode()).hexdigest()
    hit = CACHE / f"{key}.json"
    if hit.exists():
        return json.loads(hit.read_text()), True
    last = None
    for attempt in range(3):
        cmd = ["claude", "-p", "--model", "haiku", "--safe-mode", "--restricted", "--tools", "",
               "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}', "--setting-sources", "",
               "--no-session-persistence", "--output-format", "json", "--json-schema", json.dumps(schema),
               "--system-prompt", system]
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=600)
        try:
            env = json.loads(r.stdout)
            parsed = env.get("structured_output")
            if parsed is None:
                raise ValueError(f"no structured_output; is_error={env.get('is_error')} result={str(env.get('result'))[:200]!r}")
            out = {"parsed": parsed, "usage": env.get("usage"), "cost_usd": env.get("total_cost_usd"),
                   "model": env.get("model") or MODEL, "provider": "Anthropic via Claude CLI", "attempts": attempt + 1,
                   "duration_ms": env.get("duration_ms")}
            hit.write_text(json.dumps(out, indent=1))
            return out, False
        except Exception as e:  # noqa
            last = f"{type(e).__name__}: {e}; stdout[:300]={r.stdout[:300]!r}; stderr[-300:]={r.stderr[-300:]!r}"
    sys.exit(f"claude CLI failed after 3 attempts: {last}")


SUBCAT_SCHEMA = {"type": "object", "required": ["forms"], "additionalProperties": False, "properties": {"forms": {"type": "array", "items": {
    "type": "object", "required": ["form", "lemma", "subcategory", "grounding"], "additionalProperties": False, "properties": {
        "form": {"type": "string"}, "lemma": {"type": "string"},
        "subcategory": {"type": "string", "enum": ["determinative", "common noun", "proper noun", "pronoun", "adjective (control)", "adverb", "preposition", "verb", "other"]},
        "grounding": {"type": ["string", "null"]}}}}}}


def construction_schema(ids):
    return {"type": "object", "required": ["assignments"], "additionalProperties": False, "properties": {"assignments": {"type": "array", "items": {
        "type": "object", "required": ["id", "construction_id", "other_label"], "additionalProperties": False, "properties": {
            "id": {"type": "string"}, "construction_id": {"type": "string", "enum": sorted(ids)}, "other_label": {"type": ["string", "null"]}}}}}}


# ---------- mechanical: lexemes and classes ----------
def link_lexemes(claims, lexemes):
    by_form = {}
    for lx in lexemes:
        for f in lx["forms"]:
            by_form.setdefault(f.lower(), lx["id"])
    new_forms = collections.OrderedDict()
    for c in claims:
        ids, phrases = [], []
        for m in MENTION.findall(c["expression"]):
            m = m.strip().strip(".,;:")
            gen = re.fullmatch(r"([A-Za-z][A-Za-z-]+)['\u2019]s", m)
            if gen:
                m = gen.group(1); c.setdefault("lexeme_note", "genitive form mapped to its base lexeme")
            if re.fullmatch(r"[A-Za-z][A-Za-z'\u2019-]*", m):
                key = m.lower()
                if key not in by_form:
                    lid = "lex_" + re.sub(r"[^a-z]", "", key)
                    by_form[key] = lid
                    new_forms.setdefault(lid, {"id": lid, "forms": [m], "quotes": []})
                if by_form[key] in new_forms:
                    q = new_forms[by_form[key]]["quotes"]
                    if len(q) < 3 and c["quote"] not in q: q.append(c["quote"])
                if by_form[key] not in ids: ids.append(by_form[key])
            else:
                phrases.append(m)
        c["lexeme_ids"], c["phrases"] = ids, phrases
        c["class_id"] = None
        if not ids:
            low = c["expression"].lower()
            for cid, pat, _ in CLASS_PAT:
                if re.search(pat, low): c["class_id"] = cid; break
    return new_forms


SUBCAT_SYS = ("You label English word forms for a linguistics dataset. For each form you receive up to three sentences from a manuscript "
              "(LaTeX markup kept) in which the form is discussed. Return strict JSON only: {\"forms\":[{\"form\":..., \"lemma\":..., "
              "\"subcategory\":..., \"grounding\":...}]}. subcategory is one of: determinative, common noun, proper noun, pronoun, "
              "adjective (control), adverb, preposition, verb, other. Follow the manuscript's own categorization where a sentence states it "
              "(it treats compound forms like anyone/something and cardinal numerals as determinatives, and treats numerous/multiple/countless/"
              "rich/second as adjectives used as controls). grounding must be an exact substring (at most 120 characters) of one supplied "
              "sentence that shows the categorization, or null if none does.")


def label_new_forms(new_forms, log):
    items = list(new_forms.values())
    out = {}
    for i in range(0, len(items), 40):
        chunk = items[i:i + 40]
        prompt = json.dumps([{"form": x["forms"][0], "sentences": x["quotes"]} for x in chunk], ensure_ascii=False, indent=0)
        res, cached = orx(SUBCAT_SYS, prompt, schema=SUBCAT_SCHEMA)
        log["calls"].append({"stage": "subcategory", "n": len(chunk), "cached": cached, "usage": res.get("usage"), "cost_usd": res.get("cost_usd"), "attempts": res.get("attempts")})
        for r in res["parsed"]["forms"]:
            out[r["form"].lower()] = r
    lexemes_new = []
    enriched_lex = {l["id"]: l for l in json.loads(ENRICHED.read_text())["lexemes"]}
    parity = enriched_lex["lex_anyone"]
    overrides = json.loads((HERE / "lexeme-overrides.json").read_text()) if (HERE / "lexeme-overrides.json").exists() else {}
    tex = TEX.read_text()
    for lid, x in new_forms.items():
        r = out.get(x["forms"][0].lower(), {})
        g = r.get("grounding")
        if g and not any(g in q for q in x["quotes"]): g = None
        entry = {"id": lid, "forms": x["forms"], "lemma": r.get("lemma"), "subcategory": r.get("subcategory"),
                 "subcategory_grounding": g, "subcategory_provenance": f"{MODEL} 2026-09-16 from census sentences; unkeyed"}
        form = x["forms"][0].lower()
        if re.fullmatch(r"(some|any|every|no)(one|body|thing|where)", form):
            entry.update(subcategory="determinative", subcategory_grounding=None,
                         subcategory_provenance=f"rule 2026-09-16: compound determinative, by parity with lex_anyone in the enriched claim set ({parity.get('subcategory_grounding')})")
        if form in overrides:
            o = overrides[form]
            if o.get("grounding") and o["grounding"] not in tex:
                sys.exit(f"override grounding for {form} is not in the manuscript")
            entry.update(subcategory=o["subcategory"], subcategory_grounding=o.get("grounding"),
                         subcategory_provenance=f"override 2026-09-16: {o['reason']}")
        lexemes_new.append(entry)
    return lexemes_new


# ---------- model: construction ids ----------
def construction_prompt(catalogue):
    lines = ["You assign each claim about an English expression to one construction id from this catalogue.", ""]
    lines += [f"- {c['id']}: {c['description']}" for c in catalogue]
    lines += ["", RULES, "", "Each claim gives the manuscript's own free-text construction label, the expression, the sentence (LaTeX kept) and a note.",
              "Return strict JSON only: {\"assignments\":[{\"id\":..., \"construction_id\":..., \"other_label\":...}]}. other_label is null unless construction_id is other. Every input id exactly once."]
    return "\n".join(lines)


def assign_constructions(claims, catalogue, log):
    system = construction_prompt(catalogue)
    ids = {c["id"] for c in catalogue}
    schema = construction_schema(ids)
    batches = [claims[i:i + BATCH] for i in range(0, len(claims), BATCH)]

    def run(b):
        prompt = json.dumps([{"id": c["id"], "expression": c["expression"], "construction": c["construction"], "quote": c["quote"], "note": c.get("note")} for c in b], ensure_ascii=False)
        res, cached = orx(system, prompt, schema=schema)
        got = {a["id"]: a for a in res["parsed"]["assignments"]}
        want = [c["id"] for c in b]
        missing = [i for i in want if i not in got]
        bad = [i for i in want if i in got and got[i].get("construction_id") not in ids]
        if missing or bad:
            sys.exit(f"batch {want[0]}..{want[-1]}: missing={missing} bad={bad}")
        return b, got, cached, res

    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for b, got, cached, res in ex.map(run, batches):
            log["calls"].append({"stage": "construction", "ids": [c["id"] for c in b], "cached": cached, "usage": res.get("usage"), "cost_usd": res.get("cost_usd"), "attempts": res.get("attempts"), "model": res.get("model"), "provider": res.get("provider")})
            for c in b:
                a = got[c["id"]]
                c["construction_id"] = a["construction_id"]
                c["construction_other"] = a.get("other_label") if a["construction_id"] == "other" else None
                c["construction_provenance"] = f"{MODEL} 2026-09-16; compared with the expanded run's keyed claims (see normalize-key-check.json)"


REFINE = """These claims were labelled taxonomic_or_meta in a first pass, and that label was over-used. Re-examine each one.
If the manuscript's free-text construction label or the sentence names a function or construction for the expression (Det, internal Mod, subject, object, complement of a preposition, predicative complement, partitive, agreement or number, genitive, compound, fused head, degree modifier, predeterminer, coordination marker, comparative complement, existential), assign that construction, following the rules above. Keep taxonomic_or_meta only when the sentence is purely about category membership, taxonomy, method, or the analysis as a whole and names no construction for the expression."""


def refine_taxonomic(claims, catalogue, log):
    system = construction_prompt(catalogue) + "\n\n" + REFINE
    ids = {c["id"] for c in catalogue}
    schema = construction_schema(ids)
    todo = [c for c in claims if c["construction_id"] == "taxonomic_or_meta"]
    batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]

    def run(b):
        prompt = json.dumps([{"id": c["id"], "expression": c["expression"], "construction": c["construction"], "quote": c["quote"], "note": c.get("note")} for c in b], ensure_ascii=False)
        res, cached = orx(system, prompt, schema=schema)
        got = {a["id"]: a for a in res["parsed"]["assignments"]}
        return b, got, cached, res

    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for b, got, cached, res in ex.map(run, batches):
            log["calls"].append({"stage": "refine_taxonomic", "ids": [c["id"] for c in b], "cached": cached, "usage": res.get("usage"), "cost_usd": res.get("cost_usd"), "attempts": res.get("attempts")})
            for c in b:
                a = got.get(c["id"])
                if not a or a["construction_id"] not in ids: continue
                c["construction_id_pass1"] = "taxonomic_or_meta"
                c["construction_id"] = a["construction_id"]
                c["construction_other"] = a.get("other_label") if a["construction_id"] == "other" else None


def map_other(claims, log):
    """An `other` whose label names external determination is that catalogue id. No other rule:
    a regex residue rule tried on 2026-09-16 was contradicted by an independent model on all 23
    of its assignments (see typesafe-full-2026-09-16/), so the two model passes stand as final."""
    n = 0
    for c in claims:
        if c["construction_id"] == "other" and c.get("construction_other") and re.search(r"external determination", c["construction_other"], re.I):
            c["construction_id_pass2"], c["construction_id"], c["construction_other"] = "other", "external_determination", None
            c["construction_provenance"] = "rule 2026-09-16: other_label named external determination"
            n += 1
    log["residue_rule_assignments"] = n


# ---------- mechanical: basis at the locus ----------
def locus(text, quote):
    pos = text.find(quote)
    if pos < 0: return None
    pstart = text.rfind("\n\n", 0, pos) + 2
    pend = text.find("\n\n", pos + len(quote))
    para = text[pstart: pend if pend > 0 else None]
    sents, off = [], 0
    for s in SENT_SPLIT.split(para):
        i = para.find(s, off); sents.append((i, i + len(s), s)); off = i + len(s)
    qs, qe = pos - pstart, pos - pstart + len(quote)
    sent = " ".join(s for a, b, s in sents if a < qe and b > qs) or para
    line_start = text.rfind("\n", 0, pos) + 1
    line = text[line_start: text.find("\n", pos)]
    last_ea, last_z = text.rfind("\\ea", 0, pos), text.rfind("\\z", 0, pos)
    return {"sentence": sent, "paragraph": para, "line": line, "in_example": last_ea > last_z}


def keys_in(s):
    return {k.strip() for g in CITE.findall(s) for k in g.split(",")}


def basis(text, c):
    L = locus(text, c["quote"])
    sig = []
    ks, kp = keys_in(L["sentence"]), keys_in(L["paragraph"])
    cg = lambda K: any("huddleston2002" in k for k in K)
    oth = lambda K: any("huddleston2002" not in k for k in K)
    if cg(ks): sig.append("cgel_cited_sentence")
    elif cg(kp): sig.append("cgel_cited_paragraph")
    if oth(ks): sig.append("other_cited_sentence")
    elif oth(kp): sig.append("other_cited_paragraph")
    if "\\ungram" in c["quote"]: sig.append("ungrammaticality_marked")
    if re.search(r"\\footnote\{[^}]*(\\href|\\nolinkurl|\\url|\bNOW\b|COCA|Treebank|corpus)", L["sentence"]) or \
       re.search(r"(\\href|\\nolinkurl|\\url|Treebank sentence)", c["quote"]): sig.append("attestation_footnote")
    if L["in_example"]: sig.append("example_env")
    if " & " in L["line"] and L["line"].rstrip().endswith("\\\\"): sig.append("table_row")
    c["basis_signals"] = sig
    c["cited_keys_sentence"] = sorted(ks)
    et = c["evidence_type"]
    if "attestation_footnote" in sig: rec = "retained_attestation"
    elif "ungrammaticality_marked" in sig: rec = "constructed_ungrammatical"
    elif et == "searched_not_found": rec = et
    elif "cgel_cited_sentence" in sig: rec = "cgel_restricted" if et == "cgel_restricted" else "cgel_described"
    elif "other_cited_sentence" in sig: rec = "other_source_described"
    else: rec = et
    c["evidence_type_reconciled"] = rec
    c["label_uncited_at_locus"] = et in ("cgel_described", "cgel_restricted", "other_source_described") and not (ks or kp)


# ---------- comparison with the keyed manuscript claims ----------
def key_check(claims, enriched):
    keyed = [x for x in enriched["participation_claims"] if any(e["source_id"] == "M" for e in x["evidence"])]
    pairs, agree = [], collections.Counter()
    for x in keyed:
        quotes = [e["quote"].strip() for e in x["evidence"] if e["source_id"] == "M"] + [x["evidence_type_basis_quote"].strip()]
        for y in claims:
            q = y["quote"].strip()
            if x["form"].lower() in y["expression"].lower() and any(a in q or q in a for a in quotes):
                p = {"keyed": x["id"], "form": x["form"], "census": y["id"], "construction": [x["construction_id"], y["construction_id"]],
                     "evidence_type": [x["evidence_type"], y["evidence_type"]], "reconciled": [x["evidence_type"], y["evidence_type_reconciled"]]}
                for k in ("construction", "evidence_type", "reconciled"):
                    agree[k, p[k][0] == p[k][1]] += 1
                pairs.append(p)
    summary = {k: {"agree": agree[k, True], "disagree": agree[k, False]} for k in ("construction", "evidence_type", "reconciled")}
    per = collections.defaultdict(lambda: {"construction": False, "evidence_type": False, "reconciled": False, "n": 0})
    for p in pairs:
        d = per[p["keyed"]]; d["n"] += 1
        for k in ("construction", "evidence_type", "reconciled"):
            d[k] = d[k] or p[k][0] == p[k][1]
    summary["per_keyed_claim_any_match"] = {k: f"{sum(d[k] for d in per.values())}/{len(per)}" for k in ("construction", "evidence_type", "reconciled")}
    summary["keyed_claims_with_no_pairing"] = len(keyed) - len(per)
    return {"keyed_manuscript_claims": len(keyed), "pairings": len(pairs), "summary": summary,
            "note": "Pairings share a quotation and the keyed form. The keyed claims aggregate several sentences, so a pairing is an agreement measure, not a strict key.",
            "pairs": pairs}


def main():
    census = json.loads((HERE / "census-repartitioned.json").read_text())
    enriched = json.loads(ENRICHED.read_text())
    text = TEX.read_text()
    claims = json.loads(json.dumps(census["claims"]))
    amend = json.loads((HERE / "amendments.json").read_text()) if (HERE / "amendments.json").exists() else {}
    for c in claims:
        if c["id"] in amend:
            c["quote_previous"], c["quote"], c["quote_amended"] = c["quote"], amend[c["id"]]["quote"], amend[c["id"]]["reason"]
    log = {"model": MODEL, "batch": BATCH, "calls": []}

    lexemes = json.loads(json.dumps(enriched["lexemes"]))
    new_forms = link_lexemes(claims, lexemes)
    lexemes += label_new_forms(new_forms, log)
    subcat = {lx["id"]: lx.get("subcategory") for lx in lexemes}
    cls = {cid: sc for cid, _, sc in CLASS_PAT}
    NOUNISH = {"determinative", "common noun", "proper noun", "pronoun", "adjective (control)"}
    by_form = {f.lower(): lx["id"] for lx in lexemes for f in lx["forms"]}
    for c in claims:
        if not c["lexeme_ids"] and c["phrases"]:
            # a multiword mention: take the last word that is a known noun-subcategory lexeme (the lucky few -> few)
            for ph in c["phrases"]:
                words = [w.strip("'\u2019.,;:").lower() for w in ph.split()]
                cands = [by_form[w] for w in words if w in by_form and subcat.get(by_form[w]) in NOUNISH]
                if cands:
                    c["lexeme_ids"] = [cands[-1]]
                    c["lexeme_note"] = f"phrase {ph!r} resolved to its last known noun-subcategory lexeme"
                    break
        s = {subcat.get(i) for i in c["lexeme_ids"]} - {None}
        c["subcategory"] = (s.pop() if len(s) == 1 else "mixed" if s else cls.get(c["class_id"]))

    catalogue = json.loads(json.dumps(enriched["constructions"])) + [{"id": i, "description": d, "added": "normalize.py 2026-09-16"} for i, d in EXT]
    assign_constructions(claims, catalogue, log)
    refine_taxonomic(claims, catalogue, log)
    map_other(claims, log)
    for c in claims: basis(text, c)

    kc = key_check(claims, enriched)
    (HERE / "normalize-key-check.json").write_text(json.dumps(kc, indent=1, ensure_ascii=False) + "\n")

    out = {"derived_from": {"census-repartitioned.json": sha(HERE / "census-repartitioned.json"), "claims-enriched.json": sha(ENRICHED), "determinatives-as-nouns.tex": sha(TEX)},
           "reconciliation_rule": "attestation footnote at the sentence -> retained_attestation; \\ungram in the quote -> constructed_ungrammatical; searched_not_found kept; "
                                  "CGEL cited in the sentence -> cgel_described (cgel_restricted kept); another work cited in the sentence -> other_source_described; otherwise the census label.",
           "catalogue": catalogue, "lexemes": lexemes, "classes": [{"id": cid, "subcategory": sc} for cid, _, sc in CLASS_PAT], "claims": claims}
    (HERE / "census-normalized.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    cost = sum((c.get("cost_usd") or 0) for c in log["calls"] if not c["cached"])
    log["summary"] = {"claims": len(claims), "new_lexemes": len(new_forms), "cost_usd_uncached": round(cost, 4),
                      "construction_ids": collections.Counter(c["construction_id"] for c in claims).most_common(),
                      "other_labels": collections.Counter(c["construction_other"] for c in claims if c["construction_other"]).most_common(),
                      "subcategory": collections.Counter(str(c["subcategory"]) for c in claims).most_common(),
                      "evidence_type_reconciled": collections.Counter(c["evidence_type_reconciled"] for c in claims).most_common(),
                      "label_uncited_at_locus": sum(c["label_uncited_at_locus"] for c in claims),
                      "key_check": kc["summary"],
                      "residue_rule_assignments": log["residue_rule_assignments"],
                      "refined_from_taxonomic": sum(1 for c in claims if c.get("construction_id_pass1")),
                      "taxonomic_remaining": sum(1 for c in claims if c["construction_id"] == "taxonomic_or_meta")}
    (HERE / "normalize-log.json").write_text(json.dumps(log, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(log["summary"], indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
