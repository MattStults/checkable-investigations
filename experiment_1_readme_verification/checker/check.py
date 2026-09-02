#!/usr/bin/env python3
"""Mechanical checker for the claim ledger.

Usage:
  check.py ledger/claims.jsonl [--repo PATH] [--pin SHA] [--json OUT]
  check.py --citations citations.jsonl [--repo PATH] [--pin SHA] [--json OUT]

Ledger mode checks every claim (see README.md for the rule list) and prints a
pass/fail line per claim id. Citations mode checks only that each entry's
quote is a verbatim substring of its cited file at the pin (used to re-verify
the baseline arm's citations). Exit status 1 if anything fails.
"""
import argparse, json, os, re, subprocess, sys
from collections import Counter, defaultdict

DEFAULT_REPO = os.path.expanduser("~/Documents/ai_safety_projects/semi-formal-document-analysis")
DEFAULT_PIN = "48e66ce04a4d9f06771c42f89cb37b075583c5f6"

TIERS = {"raw", "panel", "adjudicated", "human", "live_run", "git", "filesystem", "stated", "cove"}
THRESH = {"in_sample", "label_free", "LOBO", "oracle", "training_folds", "n/a", "unstated"}
UNIV = {"published", "true", "n/a", "unstated"}
REGION = {"starred_block", "archive_block", "body", "n/a"}
SUP = {"current", "superseded", "struck", "contested", "unknown"}
RELS = {"supersedes", "restates", "flags_unsourced", "strikes", "withdraws", "contradicts", "re_derives", "amends", "quarantines", "forbids_citation"}
KINDS = {"value", "rate", "event", "existence"}
ETYPES = {"annotation", "trigger", "cycle_close", "iteration_close", "adversarial_review", "prediction_freeze", "measurement",
          "ledger_entry", "erratum", "withdrawal", "seat_dispatch", "certification_run", "registration",
          "commit", "prune", "redaction", "engine_failure", "cove", "ruling", "hunk"}
ACTORS = {"owner", "driver", "seat", "panel", "reviewer", "script", "unstated"}
REQ = ["id", "kind", "source", "quote", "metric", "value", "numerator", "denominator", "tier", "venue",
       "snapshot", "population", "scope", "threshold_rule", "universe", "provenance_region", "anti_rule",
       "stance", "refs", "event", "translator", "notes"]
EREQ = ["type", "ts", "ordinal", "actor", "model_tier", "session", "context_origin", "links", "finding",
        "kind", "erratum", "recurrence_of", "caught_by", "asserted_transfer"]

GENERATED_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ledger", "spans")
_blob = {}
def blob(repo, commit, path):
    key = (commit, path)
    if key not in _blob:
        if path.startswith("GENERATED:"):
            fp = os.path.join(GENERATED_DIR, path[len("GENERATED:"):])
            _blob[key] = open(fp).read() if os.path.exists(fp) else None
            return _blob[key]
        try:
            _blob[key] = subprocess.check_output(["git", "-C", repo, "show", f"{commit}:{path}"],
                                                 stderr=subprocess.DEVNULL).decode("utf-8", "replace")
        except subprocess.CalledProcessError:
            _blob[key] = None
    return _blob[key]

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def check_quote(repo, pin, src, quote):
    """Returns (ok, reason)."""
    if not isinstance(src, dict) or not all(k in src for k in ("path", "commit", "lines")):
        return False, "source missing path/commit/lines"
    commit = pin if src["commit"] == "pin" else src["commit"]
    text = blob(repo, commit, src["path"])
    if text is None:
        return False, f"source not found: {commit[:8]}:{src['path']}"
    if not quote or not norm(quote):
        return False, "empty quote"
    m = re.match(r"^(\d+)-(\d+)$", str(src["lines"]))
    if not m:
        return False, "lines must be 'a-b'"
    a, b = int(m.group(1)), int(m.group(2))
    lines = text.split("\n")
    if a < 1 or b > len(lines) or a > b:
        return False, f"line range {a}-{b} outside file (1-{len(lines)})"
    window = norm("\n".join(lines[a - 1:b]))
    if norm(quote) in window:
        return True, "verbatim within cited lines"
    if norm(quote) in norm(text):
        return False, "verbatim in file but not within cited lines"
    return False, "not a verbatim substring of the source"

def check_rate(c):
    n, d, v = c.get("numerator"), c.get("denominator"), c.get("value")
    if not isinstance(n, int) or not isinstance(d, int) or d == 0:
        return False, "rate needs integer numerator and non-zero integer denominator"
    if not isinstance(v, (int, float)):
        return False, "rate value must be numeric"
    s = repr(v)
    decimals = len(s.split(".")[1]) if "." in s else 0
    if abs(n / d - v) > 0.5 * 10 ** (-decimals) + 1e-12:
        return False, f"{n}/{d} = {n/d:.6f} does not re-derive value {v}"
    return True, f"{n}/{d} re-derives {v}"

def check_claim(c, repo, pin, ids):
    fails, notes = [], []
    for k in REQ:
        if k not in c:
            fails.append(f"missing field {k}")
    if fails:
        return fails, notes
    if not re.match(r"^L\d{5,8}$", str(c["id"])):
        fails.append("id must be L+5 digits")
    if c["kind"] not in KINDS:
        fails.append(f"kind {c['kind']!r} not in {sorted(KINDS)}")
    ok, why = check_quote(repo, pin, c["source"], c["quote"])
    (notes if ok else fails).append(f"quote: {why}")
    if c["tier"] not in TIERS:
        fails.append(f"tier {c['tier']!r} not in enum")
    elif norm(str(c["quote"])).startswith('"wave"') and c["tier"] != "raw":
        fails.append("a wave-seat verdict (quote key \"wave\") must be tier raw (I-02 / G-01)")
    if c["threshold_rule"] not in THRESH:
        fails.append(f"threshold_rule {c['threshold_rule']!r} not in enum")
    if c["universe"] not in UNIV:
        fails.append(f"universe {c['universe']!r} not in enum")
    if c["provenance_region"] not in REGION:
        fails.append(f"provenance_region {c['provenance_region']!r} not in enum")
    for k in ("snapshot", "scope", "metric", "venue", "population"):
        if not isinstance(c[k], str) or not c[k].strip():
            fails.append(f"{k} must be a non-empty string ('unstated' or 'n/a' allowed)")
    if c["kind"] == "rate":
        ok, why = check_rate(c)
        (notes if ok else fails).append(f"rate: {why}")
    if c["stance"] not in SUP:
        fails.append("stance not in enum")
    if not isinstance(c["refs"], list):
        fails.append("refs must be a list")
    else:
        for r in c["refs"]:
            if not isinstance(r, dict) or r.get("rel") not in RELS or not isinstance(r.get("target_text"), str) or not r["target_text"].strip():
                fails.append("each ref needs rel (enum) and non-empty target_text")
                continue
            tid = r.get("target_id")
            if tid is not None:
                if tid not in ids:
                    fails.append(f"ref target_id {tid} does not resolve")
                elif tid == c["id"]:
                    fails.append("ref target_id is self")
    ev = c["event"]
    if c["kind"] == "event":
        if not isinstance(ev, dict):
            fails.append("event kind requires an event object")
        else:
            for k in EREQ:
                if k not in ev:
                    fails.append(f"event missing {k}")
            if not fails:
                if ev["type"] not in ETYPES:
                    fails.append(f"event.type {ev['type']!r} not in enum")
                if ev["ts"] != "unstated" and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(ev["ts"])):
                    fails.append("event.ts must be YYYY-MM-DD or 'unstated'")
                if not isinstance(ev["actor"], list) or not ev["actor"] or not set(ev["actor"]) <= ACTORS:
                    fails.append("event.actor must be a non-empty list from the actor enum")
                if not isinstance(ev["links"], list):
                    fails.append("event.links must be a list")
                co = str(ev["context_origin"])
                if co not in ("fresh", "continued", "compacted", "unstated") and not co.startswith("seeded_by:"):
                    fails.append("event.context_origin not in enum")
                if ev["type"] == "engine_failure" and ev["kind"] not in ("refusal", "wrong_answer"):
                    fails.append("engine_failure requires kind refusal|wrong_answer")
                if ev["erratum"] is not None and (not isinstance(ev["erratum"], dict) or "class" not in ev["erratum"]):
                    fails.append("event.erratum must be null or {n, class}")
                elif ev["erratum"] is not None and ev["erratum"].get("n") is not None:
                    nn = str(ev["erratum"]["n"])
                    src_ = c["source"]; commit_ = pin if src_["commit"] == "pin" else src_["commit"]
                    text_ = blob(repo, commit_, src_["path"]) or ""
                    m_ = re.match(r"^(\d+)-(\d+)$", str(src_["lines"]))
                    window_ = norm("\n".join(text_.split("\n")[int(m_.group(1)) - 1:int(m_.group(2))])) if m_ else norm(c["quote"])
                    if not re.search(r"(?i)(erratum\s*#?\s*|#)" + re.escape(nn) + r"\b", window_):
                        fails.append(f"erratum.n={nn} does not appear as an erratum number within the cited source lines (I-01)")
                if ev["caught_by"] is not None and (not isinstance(ev["caught_by"], dict) or "set" not in ev["caught_by"] or "inferred" not in ev["caught_by"]):
                    fails.append("event.caught_by must be null or {set, inferred}")
                p_ = c["source"]["path"]
                ordered_source = (p_.endswith("ITERATION_NOTES.md") and not str(c["source"]["lines"]).startswith("1-")) or p_.startswith("GENERATED:")
                if ordered_source and ev["ordinal"] is None:
                    fails.append("events sourced from the ledger or the git log require an ordinal (entry number or commit ordinal)")
    elif ev is not None:
        fails.append("non-event kinds must have event: null")
    tr = c["translator"]
    if not isinstance(tr, dict) or not all(k in tr for k in ("model", "brief_version", "glossary_version", "batch")):
        fails.append("translator must carry model, brief_version, glossary_version, batch")
    return fails, notes

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ledger", nargs="?")
    ap.add_argument("--citations")
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--pin", default=DEFAULT_PIN)
    ap.add_argument("--json")
    a = ap.parse_args()
    results = []
    if a.citations:
        for line in open(a.citations):
            if not line.strip():
                continue
            e = json.loads(line)
            src = {"path": e["path"], "commit": e.get("commit", "pin"), "lines": e.get("lines", "1-999999")}
            text = blob(a.repo, a.pin if src["commit"] == "pin" else src["commit"], src["path"])
            if text is not None and src["lines"] == "1-999999":
                src["lines"] = f"1-{text.count(chr(10)) + 1}"
            ok, why = check_quote(a.repo, a.pin, src, e.get("quote", ""))
            results.append({"id": e.get("id"), "pass": ok, "fails": [] if ok else [why], "notes": [why] if ok else []})
    else:
        claims = [json.loads(l) for l in open(a.ledger) if l.strip()]
        ids = Counter(c.get("id") for c in claims)
        dups = {i for i, n in ids.items() if n > 1}
        seen = defaultdict(list)
        for c in claims:
            fails, notes = check_claim(c, a.repo, a.pin, set(ids))
            if c.get("id") in dups:
                fails.append("duplicate id")
            key = (json.dumps(c.get("source"), sort_keys=True), norm(str(c.get("quote"))), c.get("metric"), json.dumps(c.get("value")))
            seen[key].append(c.get("id"))
            results.append({"id": c.get("id"), "pass": not fails, "fails": fails, "notes": notes})
        for key, lst in seen.items():
            if len(lst) > 1:
                for r in results:
                    if r["id"] in lst:
                        r["notes"].append(f"duplicate content with {[x for x in lst if x != r['id']]}")
    npass = sum(r["pass"] for r in results)
    for r in results:
        print(("PASS" if r["pass"] else "FAIL"), r["id"], "; ".join(r["fails"] or r["notes"]))
    summary = {"total": len(results), "passed": npass, "failed": len(results) - npass,
               "fail_reasons": Counter(f.split(":")[0] for r in results for f in r["fails"])}
    print(json.dumps(summary, default=dict))
    if a.json:
        json.dump({"summary": summary, "results": results}, open(a.json, "w"), indent=1, default=dict)
    sys.exit(0 if npass == len(results) else 1)

if __name__ == "__main__":
    main()
