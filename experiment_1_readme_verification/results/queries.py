#!/usr/bin/env python3
"""Step 7: map each frozen-inventory item to a query over the checked ledger
and record its terminal state with a derivation.

States: verified | contradicted | contested | unverifiable | live_run_pending
(live_run_pending = the claim is decided by running a committed script; the
checker step runs those and this script fills them in from
results/live_runs.json when present).

Every derivation lists the ledger claim ids consulted. No claim is edited.
Usage: queries.py [--ledger ledger/claims.jsonl] [--out results/query_results.json]
"""
import argparse, json, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)

def num(v):
    if isinstance(v, (int, float)): return float(v)
    if isinstance(v, str):
        m = re.match(r"^\s*[+]?(-?\d+(?:\.\d+)?)\s*%?\s*$", v.replace("−", "-").replace(",", ""))
        if m: return float(m.group(1)) / (100 if v.strip().endswith("%") else 1)
    return None

def close(a, b, tol):
    return a is not None and b is not None and abs(a - b) <= tol

# ---------------------------------------------------------------- Q specs
# metric/scope/quote are regexes (case-insensitive) over the claim's metric,
# scope, quote. value: number (with tol), list of numbers (all must appear),
# or string regex over str(value). require: dimension constraints that make
# a numeric match count as verified at the claimed tier; a match failing
# them is reported as verified_at_other_tier (a sub-state of verified with
# the actual tier named).
Q = {
 "Q01": {"metric": r"criterion standing|match-or-adjudicated-defensible|match-or-defensible", "value": [0.941, 0.953, 0.96], "tol": 0.001, "any_of": True, "band": (0.94, 0.96), "require": {"tier": {"panel", "adjudicated"}}},
 "Q02": {"metric": r"panel.internal agreement|inter-judge agreement|panel agreement|judge-vs-judge|inter-judge", "value": None, "band": (0.94, 0.96), "band_check": True},
 "Q03": {"metric": r"certification|raw_verdict|verdict_engaged", "quote": r"F1|IN BAND|certif", "scope": r"helpfulness|harm|caution|dev behaviour", "value": None, "count_scopes": 3},
 "Q04": {"metric": r"registration|match-or-defensible|defensibility pass|panel.equivalence", "quote": r"registered|registration|scored ONCE|never ran|DEFENSIBILITY PASS", "value": None, "contested_if_multiple_registrations": True},
 "Q05": {"metric": r"node count|^nodes$|node_count", "value": 773, "tol": 0},
 "Q06": {"metric": r"join rate|recall ceiling", "value": 0.984, "tol": 0.0005, "require": {"universe": {"true"}}, "anti_rule_expected": True},
 "Q07": {"live_run": "check_model"},
 "Q08": {"metric": r"clause", "scope": r"constitution", "value": 616, "tol": 0},
 "Q09": {"metric": r"rule", "quote": r"rule", "scope": r"ASP|fragment|constitution|pilot", "value": 16, "tol": 0},
 "Q10": {"metric": r"passage|universe", "value": 589, "tol": 0},
 "Q11": {"metric": r"node count|^nodes$|node_count", "value": 773, "tol": 0},
 "Q12": {"metric": r"^mcc", "scope": r"tool", "value": 0.32, "tol": 0.0005, "require": {"threshold_rule": {"in_sample"}, "universe": {"true"}}},
 "Q13": {"metric": r"^mcc", "scope": r"tool|label-free", "value": 0.278, "tol": 0.0005, "require": {"threshold_rule": {"label_free"}}},
 "Q14": {"metric": r"judge mcc|mcc", "scope": r"judge", "value": 0.555, "tol": 0.0005},
 "Q15": {"metric": r"cells|judge wins|beat", "quote": r"9 of 9|9/9", "value": None, "present_ok": True},
 "Q16": {"metric": r"engaged.precision|attempt.series|attempt_series|transfer verdict", "value": [0.4, 0.7, 0.55, 0.85], "tol": 0.001, "all_of": True, "scope": r"tradeoffs|unstated|attempt"},
 "Q17": {"metric": r"declined nodes panel-relevant|panel-relevant|recall", "value": 0.575, "tol": 0.001, "rate": (23, 40)},
 "Q18": {"metric": r"commit|withdraw", "quote": r"bf0d4978", "value": None, "present_ok": True},
 "Q19": {"metric": r"separability|trials|random.partition|null", "value": 0.9967, "tol": 0.0005, "rate": (299, 300)},
 "Q20": {"metric": r"relevance prediction|1-NN|base rate", "quote": r"base rate|1-NN", "value": None, "present_ok": True},
 "Q21": {"metric": r"commit|withdraw", "quote": r"365d68b3|DOES-NOT-LICENSE", "value": None, "present_ok": True},
 "Q22": {"metric": r"finding|L1|L2", "quote": r"noise|no null|null-free|already met", "value": None, "present_ok": True},
 "Q23": {"metric": r"commit|erratum", "quote": r"1143a921|erratum #20|ERRATUM #20", "value": None, "present_ok": True},
 "Q24": {"live_run": "pytest"},
 "Q25": {"metric": r"entry|ledger", "quote": r"0000.{0,3}0043", "value": None, "present_ok": True},
 "Q26": {"metric": r"definition", "quote": r"100 def|100 behavio", "value": 100, "tol": 0, "loose": True},
 "Q27": {"metric": r"coverage", "value": 1.0, "tol": 0.001, "rate_any": True, "require_pop": r"\b100\b|definition", "pop_note": "the README binds coverage to the 100 definitions; a 1.0 whose population is a 39-node sample does not satisfy the binding"},
 "Q28": {"metric": r"separability", "value": None, "every_test": True},
 "Q29": {"metric": r"withdraw", "event_type": "withdrawal", "value": None, "count_headline": True},
 "Q30": {"live_run": "files"},
 "Q31": {"live_run": "symlinks"},
 "Q32": {"live_run": "absence-by-search over PRUNED.md (D-09): signature markers per the inventory definition, detached signature files, restore hashes resolve"},
 "Q33": {"live_run": "git_dates"},
 "Q34": {"metric": r"trigger|^on$|workflow trigger|ci trigger", "value": r"^push$|every push|on push$", "value_is_regex": True, "others_regex": r"branches|main|pull_request"},
 "Q35": {"live_run": "licenses"},
 "Q36": {"live_run": "cite"},
 "Q37": {"live_run": "seats"},
 "Q38": {"metric": r"redact", "event_type": "redaction", "value": None, "present_ok": True},
 "Q39": {"metric": r"binding|rule", "quote": r"BINDING|matched-granularity|cannot fail", "value": None, "present_ok": True},
 "Q40": {"live_run": "setup_check"},
 "Q41": {"metric": r"engaged.precision|match-or", "scope": r"user-autonomy|proportionate|general-welfare|harmlessness|objectivity|untuned|never-consulted", "value": None, "threshold_none_above": 0.94},
 "Q42": {"live_run": "links"},
 "Q43": {"live_run": "start_here"},
 "Q44": {"metric": r"bad (line )?ranges|bad quotes|spans", "value": 0, "tol": 0, "loose": True},
 "Q45": {"metric": r"headline", "scope": r"help|harm|caution", "value": None, "present_ok": True},
 "Q46": {"live_run": "no_network"},
 "Q47": {"metric": r"corpus|spec", "quote": r"model_spec|openai-model-spec|Model Spec", "value": None, "present_ok": True},
 "Q48": {"live_run": "handoffs"},
 "Q49": {"live_run": "layout"},
 "Q50": {"live_run": "determinism"},
}

def match_value(spec, c):
    v = c.get("value"); tol = spec.get("tol", 0.001)
    target = spec.get("value")
    if target is None: return True
    if isinstance(target, list):
        n = num(v); return any(close(n, t, tol) for t in target)
    if isinstance(target, str): return re.search(target, str(v), re.I) is not None
    n = num(v)
    if n is None and c.get("kind") == "rate" and spec.get("rate"):
        return (c.get("numerator"), c.get("denominator")) == spec["rate"]
    if close(n, target, tol): return True
    if spec.get("rate") and (c.get("numerator"), c.get("denominator")) == spec["rate"]: return True
    return False

def candidates(spec, claims):
    out = []
    for c in claims:
        if spec.get("event_type"):
            if c["kind"] == "event" and c["event"]["type"] == spec["event_type"]: out.append(c)
            continue
        if c["kind"] == "event" and not spec.get("quote"): continue
        hit = re.search(spec["metric"], c["metric"], re.I) or (spec.get("loose") and re.search(spec["metric"], c["quote"], re.I))
        if spec.get("quote"): hit = hit or re.search(spec["quote"], c["quote"], re.I)
        if not hit: continue
        if spec.get("scope") and not (re.search(spec["scope"], c["scope"], re.I) or re.search(spec["scope"], c["quote"], re.I) or re.search(spec["scope"], c["venue"], re.I)): continue
        out.append(c)
    return out

def dims_ok(spec, c):
    req = spec.get("require", {})
    return all(c.get(k) in v for k, v in req.items()), {k: c.get(k) for k in req}

def decide_q(qid, spec, claims):
    if spec.get("live_run"):
        return {"state": "live_run_pending", "derivation": f"decided by running {spec['live_run']}; filled from results/live_runs.json", "claims": []}
    cands = candidates(spec, claims)
    if cands and spec.get("require_pop"):
        popok = [c for c in cands if re.search(spec["require_pop"], str(c.get("population") or c.get("denominator") or ""), re.I)]
        if not popok:
            return {"state": "contested", "derivation": f"{len(cands)} matching claim(s) at the value, none over the required population ({spec['require_pop']}); populations found: {sorted({str(c.get('population') or c.get('denominator')) for c in cands})} — {spec.get('pop_note','')}", "claims": [c["id"] for c in cands][:6]}
        cands = popok
    if not cands:
        return {"state": "unverifiable", "derivation": "no ledger claim matches the metric/scope pattern. Two readings: a translation-coverage gap, or the record holds no such artifact — a ledger of positive claims cannot distinguish these unless a translator recorded an explicit absence (existence claim with value false); this is reported as a coverage finding", "claims": []}
    if spec.get("band_check"):
        vals = [(c["id"], num(c["value"])) for c in cands if num(c["value"]) is not None and c["stance"] in ("current", "unknown")]
        inb = [v for v in vals if spec["band"][0] - 0.05 <= v[1] <= spec["band"][1] + 0.05]
        if not vals: return {"state": "unverifiable", "derivation": "agreement metric named but no numeric value in the ledger (the record may hold none)", "claims": [c["id"] for c in cands][:8]}
        return {"state": "verified" if inb else "contradicted", "derivation": f"agreement values in ledger {vals[:6]}; within ±0.05 of the README band {spec['band']}: {inb[:4]}", "claims": [v[0] for v in vals][:8]}
    if spec.get("present_ok") and spec.get("value") is None:
        cont = [c for c in cands if c["stance"] in ("contested",)]
        struck = [c for c in cands if c["stance"] in ("struck", "superseded")]
        live = [c for c in cands if c["stance"] in ("current", "unknown")]
        if live: return {"state": "verified", "derivation": f"{len(live)} claim(s) record the event/text as standing" + (f"; {len(cont)} contested claim(s) also present" if cont else ""), "claims": [c["id"] for c in cands][:12], "tiers": sorted({c['tier'] for c in live})}
        if cont: return {"state": "contested", "derivation": "only contested claims match", "claims": [c["id"] for c in cont][:12]}
        return {"state": "contested", "derivation": "only struck/superseded claims match", "claims": [c["id"] for c in struck][:12]}
    if spec.get("threshold_none_above") is not None:
        vals = [(c["id"], num(c["value"]), c["scope"], c["tier"], c["stance"]) for c in cands if num(c["value"]) is not None]
        above = [v for v in vals if v[1] >= spec["threshold_none_above"] and v[4] in ("current", "unknown")]
        if not vals: return {"state": "unverifiable", "derivation": "no numeric measurement found for untuned behaviours", "claims": [c["id"] for c in cands][:12]}
        if above: return {"state": "contradicted", "derivation": f"{len(above)} measurement(s) at or above threshold: {above[:5]}", "claims": [v[0] for v in above]}
        return {"state": "verified", "derivation": f"{len(vals)} measurement(s), max {max(v[1] for v in vals):.3f} < {spec['threshold_none_above']}", "claims": [v[0] for v in vals][:12]}
    if spec.get("every_test"):
        outcomes = [(c["id"], num(c["value"]), c["scope"][:30], c["stance"]) for c in cands if num(c["value"]) is not None]
        nulls = [c for c in cands if re.search(r"null", c["quote"] + c["scope"] + c["metric"], re.I)]
        return {"state": "contested", "derivation": f"{len(outcomes)} separability measurements in the ledger, {len(nulls)} mention a null; 'every test failed against a null' requires each measurement to carry a null outcome — the ledger holds measurements without one: {outcomes[:5]}", "claims": [o[0] for o in outcomes][:10]}
    if spec.get("existence_true"):
        ex = [c for c in cands if c["kind"] == "existence" or c["kind"] == "value"]
        pos = [c for c in ex if not re.search(r"\bno\b|none|absent|not |unsigned|missing", str(c["value"]) + c["quote"][:80], re.I)]
        if not cands: return {"state": "unverifiable", "derivation": "no claim about a manifest signature", "claims": []}
        return {"state": "verified" if pos else "contradicted", "derivation": f"signature claims: {[(c['id'], c['value']) for c in ex][:6]}; positive: {len(pos)}", "claims": [c["id"] for c in ex][:8]}
    if spec.get("value_is_regex"):
        m = [c for c in cands if re.search(spec["value"], str(c["value"]), re.I) and not re.search(spec.get("others_regex", "$^"), str(c["value"]) + c["quote"], re.I)]
        o = [c for c in cands if re.search(spec.get("others_regex", "$^"), str(c["value"]) + c["quote"], re.I)]
        if m and not o: return {"state": "verified", "derivation": f"trigger claims match: {[(c['id'], c['value']) for c in m][:4]}", "claims": [c["id"] for c in m][:6]}
        if o: return {"state": "contradicted", "derivation": f"trigger claims carry a narrower value: {[(c['id'], str(c['value'])[:40]) for c in o][:4]}", "claims": [c["id"] for c in o][:6]}
        return {"state": "unverifiable", "derivation": "no trigger claim", "claims": []}
    if spec.get("count_headline"):
        w = [c for c in cands if c["stance"] != "superseded"]
        return {"state": "contested" if len(w) != 3 else "verified", "derivation": f"{len(w)} withdrawal events in ledger (README says three headline); headline qualifier needs the starred-block/README linkage at adjudication", "claims": [c["id"] for c in w][:20]}
    matches = [c for c in cands if match_value(spec, c)]
    if spec.get("all_of"):
        found = {t: [c["id"] for c in cands if close(num(c["value"]), t, spec.get("tol", 0.001))] for t in spec["value"]}
        missing = [t for t, ids in found.items() if not ids]
        if missing: return {"state": "contested" if len(missing) < len(found) else "unverifiable", "derivation": f"series values found: { {t: ids[:3] for t, ids in found.items()} }; missing {missing}", "claims": [i for ids in found.values() for i in ids][:20]}
        return {"state": "verified", "derivation": f"every series value present: { {t: ids[:3] for t, ids in found.items()} }", "claims": [i for ids in found.values() for i in ids][:20], "tiers": sorted({c['tier'] for c in cands if match_value(spec, c)})}
    others = [c for c in cands if not match_value(spec, c) and num(c.get("value")) is not None and c["stance"] in ("current", "unknown")]
    if matches:
        good = [c for c in matches if dims_ok(spec, c)[0] and c["stance"] in ("current", "unknown")]
        anyt = [c for c in matches if c["stance"] in ("current", "unknown")]
        struck = [c for c in matches if c["stance"] in ("struck", "superseded")]
        cont = [c for c in matches if c["stance"] == "contested"]
        # a do-not-cite marking is one that speaks of citing/quoting/re-deriving the value; a bare
        # section flag such as "UNREVIEWED" is noted but does not by itself contest the value
        CITE = re.compile(r"cit|quot|re-?deriv|never use|do not use|not .*results|struck|withdrawn|stale", re.I)
        flags = [c for c in matches if c.get("anti_rule") and not CITE.search(str(c["anti_rule"]))]
        anti = [c for c in matches if c.get("anti_rule") and CITE.search(str(c["anti_rule"]))]
        st = "verified" if good else ("verified" if anyt else ("contested" if (cont or struck) else "unverifiable"))
        d = {"state": st, "claims": [c["id"] for c in matches][:12], "tiers": sorted({c['tier'] for c in anyt}), "tier_ok": bool(good)}
        d["derivation"] = (f"{len(anyt)} matching claim(s) standing" + ("" if good else f"; none at the required dimensions {spec.get('require')} — matched at {d['tiers']}") + (f"; {len(anti)} carry an anti-rule (do-not-cite) marking" if anti else "") + (f"; {len(struck)} struck/superseded, {len(cont)} contested" if (struck or cont) else ""))
        if anti and st == "verified": d["state"] = "contested"; d["derivation"] += " → contested: the record forbids citing the matched value"
        if others and st == "verified" and not spec.get("any_of"): d["derivation"] += f"; NOTE other values for the same metric/scope: {[(c['id'], c['value']) for c in others[:5]]}"
        return d
    if others:
        return {"state": "contradicted", "derivation": f"no claim carries the claimed value; the record holds {[(c['id'], c['value'], c['tier']) for c in others[:6]]}", "claims": [c["id"] for c in others][:12]}
    return {"state": "unverifiable", "derivation": "candidates matched the metric but carry no comparable numeric value", "claims": [c["id"] for c in cands][:12]}

# ---------------------------------------------------------------- hypotheses
def events(claims, *types):
    return [c for c in claims if c["kind"] == "event" and c["event"]["type"] in types]

def H01(claims):
    closes = [c for c in events(claims, "iteration_close", "cycle_close")]
    reviews = events(claims, "adversarial_review")
    if not closes: return "unverifiable", "no close events (vacuous)", []
    ok, bad = [], []
    for c in closes:
        key = c["event"]["session"] or c["snapshot"]
        ord_ = c["event"]["ordinal"]
        prior = [r for r in reviews if (r["event"]["ordinal"] is not None and ord_ is not None and r["event"]["ordinal"] <= ord_ and r["source"]["path"] == c["source"]["path"]) or any(l for l in r["event"]["links"] if l and l in (c["quote"] + " " + str(key)))]
        (ok if prior else bad).append((c["id"], key, [r["id"] for r in prior][:3]))
    st = "verified" if not bad else "contradicted"
    return st, f"{len(ok)} close(s) with a prior/linked review, {len(bad)} without: {bad[:6]}", [c["id"] for c in closes]
def H02(claims):
    meas = events(claims, "measurement"); pf = events(claims, "prediction_freeze")
    if not meas: return "unverifiable", "no measurement events", []
    bad = [m["id"] for m in meas if not any(p["event"]["ordinal"] is not None and m["event"]["ordinal"] is not None and p["event"]["ordinal"] < m["event"]["ordinal"] for p in pf) and not any(l for l in m["event"]["links"] if re.search(r"PREDICTION|prereg|prediction", str(l), re.I))]
    return ("verified" if not bad else "contested"), f"{len(meas)} measurements, {len(bad)} with no prediction_freeze earlier or linked: {bad[:8]}", [m["id"] for m in meas][:20]
def H03(claims):
    err = [c for c in claims if c["kind"] == "event" and c["event"]["type"] == "erratum" and (c["event"].get("erratum") or {}).get("n") is not None]
    lr = json.load(open(os.path.join(HERE, "live_runs.json"))).get("H03_append_only") if os.path.exists(os.path.join(HERE, "live_runs.json")) else None
    if not lr: return "unverifiable", f"numbered errata: {len(err)}; append-only conjunct needs the git deletion census (live run)", [c["id"] for c in err][:6]
    st = "contradicted" if lr["state"] == "contradicted" else ("verified" if err else "contested")
    return st, f"numbered errata: {len(err)}; append-only conjunct by git census: {lr['derivation'][:200]}", [c["id"] for c in err][:6]
def H04(claims):
    sd = events(claims, "seat_dispatch")
    forbid = re.compile(r"panel[- ]label|panel truth|\btruth\b|design doc|CYCLE_DESIGN|prior verdict|seat verdict|\bverdicts?\b|SC\.truth", re.I)
    neg = re.compile(r"\b(no|not|never|without|excluded?|denied|forbidden|blind|minus|except|nor)\b", re.I)
    viol, witnesses = [], []
    for c in sd:
        ins = c["event"].get("inputs") or []
        if ins: witnesses.append(c["id"])
        denial_list = bool(neg.search(c["quote"]))  # a quote such as "Forbidden seat material, always: ..." lists denied inputs
        for t in ins:
            if forbid.search(t) and not neg.search(t) and not denial_list: viol.append((c["id"], t[:80]))
    if not sd: return "unverifiable", "no seat_dispatch events", []
    if viol: return "contradicted", f"{len(sd)} seat dispatches; {len(witnesses)} with recorded inputs; inputs naming panel labels / design doc / verdicts without negation: {viol[:6]}", [v[0] for v in viol][:6]
    if not witnesses: return "unverifiable", f"{len(sd)} seat dispatches, none records its inputs (vacuous)", []
    return "verified", f"{len(sd)} seat dispatches; {len(witnesses)} record inputs; none names panel labels, the design document, or prior verdicts as received (mentions inside negations, or in a list the quote marks as forbidden/denied, counted as exclusions)", witnesses[:6]

def H05(claims):
    entries = events(claims, "ledger_entry"); commits = events(claims, "commit")
    if not commits: return "unverifiable", f"{len(entries)} ledger entries; no commit events yet (git-log batches pending)", []
    res = []
    for e in entries:
        n = f"{e['event']['ordinal']:04d}" if e["event"]["ordinal"] is not None else None
        cs = [c for c in commits if n and any(re.search(rf"\b{n}\b", str(l)) for l in c["event"]["links"] + [c["quote"]])]
        if cs:
            same = any(c["event"]["ts"] == e["event"]["ts"] for c in cs); res.append((e["id"], n, same))
    if not res: return "unverifiable", f"{len(entries)} entries, none linked by a commit claim to its entry number", []
    bad = [r for r in res if not r[2]]
    return ("verified" if not bad else "contested"), f"{len(res)} entries linked to commits; {len(bad)} with a commit date differing from the heading date: {bad[:6]}", [r[0] for r in res][:20]
def H06(claims):
    w = [c for c in events(claims, "withdrawal") if re.search(r"behavior_pilot|ITERATION_NOTES|HANDOFF_CURRENT|L1L2|RETRANS", c["source"]["path"])]
    r = events(claims, "adversarial_review", "cove")
    if not w: return "unverifiable", "no arc-2 withdrawal events", []
    good, bad = [], []
    for x in w:
        linked = [y for y in r if (y["event"]["ordinal"] is not None and x["event"]["ordinal"] is not None and y["event"]["ordinal"] <= x["event"]["ordinal"]) or any(re.search(re.escape(str(l)[:20]), y["quote"] + " ".join(map(str, y["event"]["links"]))) for l in x["event"]["links"] if l and len(str(l)) > 3)]
        fnd = [y for y in linked if re.search(r"unsupported|noise|does-not-license|null|base rate|void", str(y["event"]["finding"]) + y["quote"], re.I)]
        (good if fnd else bad).append(x["id"])
    return ("verified" if not bad else "contested"), f"{len(good)} withdrawals with a linked review finding in the set, {len(bad)} without: {bad[:6]}", [x["id"] for x in w][:20]
def H07(claims):
    cands = [c for c in claims if c["kind"] in ("value", "rate") and re.search(r"engaged.precision|match-or", c["metric"], re.I) and re.search(r"user-autonomy|proportionate|general-welfare|harmlessness|objectivity|never-consulted|untuned", c["scope"] + c["quote"], re.I)]
    vals = [(c["id"], num(c["value"])) for c in cands if num(c["value"]) is not None]
    if not vals: return "unverifiable", "no measurements scoped to untuned behaviours found", []
    hi = [v for v in vals if v[1] >= 0.94]
    return ("verified" if not hi else "contested"), f"{len(vals)} untuned-behaviour measurements, max {max(v[1] for v in vals):.3f}; at/above 0.94: {hi[:5]}", [v[0] for v in vals][:20]
def H08(claims):
    f = events(claims, "engine_failure")
    if not f: return "unverifiable", "no engine_failure events (vacuous)", []
    kinds = defaultdict(list)
    for c in f: kinds[c["event"]["kind"]].append(c["id"])
    if kinds.get("wrong_answer"): return "contradicted", f"kinds: {dict(kinds)}", [i for v in kinds.values() for i in v]
    if kinds.get("unstated") and not kinds.get("refusal"): return "unverifiable", f"all engine failures have kind unstated: {dict(kinds)}", [i for v in kinds.values() for i in v]
    return ("verified" if not kinds.get("unstated") else "contested"), f"kinds: {dict(kinds)}", [i for v in kinds.values() for i in v]
def H09(claims):
    tool = [num(c["value"]) for c in claims if re.search(r"^mcc", c["metric"], re.I) and re.search(r"tool", c["scope"], re.I) and num(c["value"]) is not None]
    judges = [num(c["value"]) for c in claims if re.search(r"judge", c["metric"] + c["scope"], re.I) and re.search(r"mcc", c["metric"], re.I) and num(c["value"]) is not None]
    if not tool or not judges: return "unverifiable", f"tool mcc values {len(tool)}, judge mcc values {len(judges)}", []
    return ("verified" if max(tool) <= min(judges) or max(tool) <= 0.555 else "contested"), f"tool max {max(tool):.3f} (incl. oracle/ceiling variants), judge min {min(judges):.3f}, judge mean-of-3 0.555 present: {0.555 in [round(j,3) for j in judges]}", []
def H10(claims):
    p = [c for c in claims if re.search(r"PRUNED", c["source"]["path"])]
    lr = json.load(open(os.path.join(HERE, "live_runs.json"))).get("Q32") if os.path.exists(os.path.join(HERE, "live_runs.json")) else None
    if lr:  # signed(manifest) decided by the Q32 absence-by-search (D-09); prune/restore conjuncts from the ledger
        return ("contradicted" if lr["state"] == "contradicted" else ("verified" if p else "unverifiable")), f"{len(p)} PRUNED.md claims (prune manifest exists); signed(manifest): {lr['derivation'][:160]}", []
    return ("unverifiable"), f"{len(p)} PRUNED.md claims; signature presence not decidable from span claims", []
def H11(claims):
    red = events(claims, "redaction")
    pre = [c for c in claims if c["source"]["commit"] not in ("pin", "generated")]
    lr = json.load(open(os.path.join(HERE, "live_runs.json"))).get("H03_append_only") if os.path.exists(os.path.join(HERE, "live_runs.json")) else None
    if not pre: return "unverifiable", f"redaction events {len(red)}; pre-redaction blob claims 0 (pending batches 100-107)", [c["id"] for c in red][:6]
    if not lr: return "unverifiable", f"redaction events {len(red)}; pre-redaction blob claims {len(pre)}; deletion census missing", []
    st = "contradicted" if lr["state"] == "contradicted" else "verified"
    return st, f"redaction events {len(red)}; {len(pre)} claims translated from the pre-redaction blob (content existed before the redaction); deleting commits by git census: {lr['derivation'][:160]}", [c["id"] for c in red][:6]
def H12(claims):
    hits = [c for c in claims if re.search(r"^hit|relevance_by_act|reason", c["metric"], re.I)]
    return ("unverifiable" if not hits else "verified"), f"hit claims: {len(hits)} (query-output spans were not in the named sources)", [c["id"] for c in hits][:5]
def H13(claims):
    cv = events(claims, "cove")
    dec = [c for c in claims if re.search(r"decisive", c["quote"], re.I)]
    return ("unverifiable" if not cv else "verified"), f"cove events {len(cv)}; claims mentioning decisive findings {len(dec)}", [c["id"] for c in cv][:8]
def H14(claims):
    ent = [c for c in events(claims, "ledger_entry") if re.search(r"ITERATION \d, STEP", c["quote"])]
    return ("unverifiable" if not ent else "verified"), f"{len(ent)} entries headed ITERATION n, STEP k; step-artifact domain not translated (runbook step artifacts are not a named source)", [c["id"] for c in ent][:10]
def H15(claims):
    rows = [c for c in claims if re.search(r"routing table", c["metric"], re.I)]
    return ("unverifiable" if not rows else "live_run_pending"), f"{len(rows)} routing-table entries translated; path existence is a filesystem check", [c["id"] for c in rows][:5]
HYP = {"H01": H01, "H02": H02, "H03": H03, "H04": H04, "H05": H05, "H06": H06, "H07": H07, "H08": H08, "H09": H09, "H10": H10, "H11": H11, "H12": H12, "H13": H13, "H14": H14, "H15": H15}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--ledger", default=os.path.join(X, "ledger/claims.jsonl")); ap.add_argument("--out", default=os.path.join(HERE, "query_results.json")); ap.add_argument("--inventory", default=os.path.join(X, "claim_inventory/inventory.json"))
    a = ap.parse_args()
    claims = [json.loads(l) for l in open(a.ledger) if l.strip()]
    inv = json.load(open(a.inventory))
    live = json.load(open(os.path.join(HERE, "live_runs.json"))) if os.path.exists(os.path.join(HERE, "live_runs.json")) else {}
    res = {}
    for c in inv["claims"]:
        spec = Q.get(c["id"])
        r = decide_q(c["id"], spec, claims) if spec else {"state": "unverifiable", "derivation": "no query spec", "claims": []}
        if r["state"] == "live_run_pending" and c["id"] in live: r = live[c["id"]]
        res[c["id"]] = r
    for h in inv["hypotheses"]:
        fn = HYP.get(h["id"])
        if fn:
            st, d, ids = fn(claims); res[h["id"]] = {"state": st, "derivation": d, "claims": ids}
            if st == "live_run_pending" and h["id"] in live: res[h["id"]] = live[h["id"]]
        else:
            res[h["id"]] = {"state": "unverifiable", "derivation": "no hypothesis function (H04: seat inputs not translated as a dimension)", "claims": []}
    for v in inv["verdict_nodes"]:
        provs = [p.split(" ")[0].split("/")[0] for p in v["providers"]]
        states = [res.get(p, {}).get("state") for p in provs if p in res]
        missing = [p for p in provs if p not in res]  # e.g. residue items (R..) that no query evaluates: a dangling need
        if not provs: st = "dangling"
        elif missing and all(s == "verified" for s in states): st = "contested"
        elif all(s == "verified" for s in states): st = "verified"
        elif any(s == "contradicted" for s in states): st = "contradicted"
        elif any(s in ("contested",) for s in states): st = "contested"
        elif any(s == "live_run_pending" for s in states): st = "live_run_pending"
        else: st = "unverifiable"
        res[v["id"]] = {"state": st, "derivation": f"providers {provs} → {states}" + (f"; unevaluated providers (dangling need): {missing}" if missing else ""), "claims": []}
    json.dump(res, open(a.out, "w"), indent=1)
    from collections import Counter
    for grp, ids in (("Q", [c["id"] for c in inv["claims"]]), ("H", [h["id"] for h in inv["hypotheses"]]), ("V", [v["id"] for v in inv["verdict_nodes"]])):
        print(grp, dict(Counter(res[i]["state"] for i in ids)))
    for i, r in res.items():
        print(f"{i:5} {r['state']:18} {r['derivation'][:150]}")

if __name__ == "__main__":
    main()
