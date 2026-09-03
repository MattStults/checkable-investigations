#!/usr/bin/env python3
"""Counterfactual impact of a record fact being fabricated.

For every fact the README items rest on (a metric+value carried by claims the
queries cite), remove every claim carrying that fact — from every source, as a
fabrication would propagate through restatements — re-run the queries, and
count which README items (Q/H/V) change state. Also records the tiers behind
the fact: a fact supported only at tier `stated` has no artifact behind it in
the record and is the kind that could have been fabricated without trace.
Output: results/probe/impact_ranking.json. Nothing is edited."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); RES = os.path.dirname(HERE); X = os.path.dirname(RES)
sys.path.insert(0, RES)
import queries as qe
def norm(s): return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()
def main():
    claims = [json.loads(l) for l in open(os.path.join(X, "ledger/claims.jsonl")) if l.strip()]
    inv = json.load(open(os.path.join(X, "claim_inventory/inventory.json")))
    live = json.load(open(os.path.join(RES, "live_runs.json")))
    qe.bind_values(inv)
    base = qe.evaluate(claims, inv, live)
    by_id = {c["id"]: c for c in claims}
    # facts: (norm metric, value) of value/rate claims cited by any Q/H result
    cited = {i for r in base.values() for i in r.get("claims", []) if i in by_id}
    facts = {}
    for i in cited:
        c = by_id[i]
        if c["kind"] in ("value", "rate") and c["value"] not in (None, ""):
            facts.setdefault((norm(c["metric"]), str(c["value"])), set()).add(i)
    out = []
    for (m, v), ids in facts.items():
        carriers = [c for c in claims if norm(c["metric"]) == m and str(c["value"]) == v]
        cids = {c["id"] for c in carriers}
        rest = [c for c in claims if c["id"] not in cids]
        r = qe.evaluate(rest, inv, live)
        flips = [(k, base[k]["state"], r[k]["state"]) for k in base if base[k]["state"] != r[k]["state"]]
        tiers = sorted({c["tier"] for c in carriers}); srcs = sorted({c["source"]["path"].split("/")[-1] for c in carriers})
        out.append({"metric": m, "value": v, "carriers": len(carriers), "sources": srcs, "tiers": tiers, "stated_only": tiers == ["stated"],
                    "flips": flips, "n_flips": len(flips), "example_quote": carriers[0]["quote"][:140]})
    out.sort(key=lambda o: (o["n_flips"], o["stated_only"], o["carriers"]), reverse=True)
    json.dump(out, open(os.path.join(HERE, "impact_ranking.json"), "w"), indent=1, ensure_ascii=False)
    print(f"facts tested: {len(out)}; with any flip: {sum(1 for o in out if o['n_flips'])}")
    for o in out[:20]:
        print(f"{o['n_flips']} flips | {o['metric'][:34]!r}={o['value']:<10} carriers={o['carriers']:3} tiers={o['tiers']} stated_only={o['stated_only']} srcs={len(o['sources'])} | {[f[0] for f in o['flips']]} | {o['example_quote'][:70]}")
if __name__ == "__main__":
    main()

def spans_mode():
    """Counterfactual: one record span (a ledger entry, a section, a commit) is fabricated —
    remove every claim translated from it and count README items that change state."""
    claims = [json.loads(l) for l in open(os.path.join(X, "ledger/claims.jsonl")) if l.strip()]
    inv = json.load(open(os.path.join(X, "claim_inventory/inventory.json")))
    live = json.load(open(os.path.join(RES, "live_runs.json")))
    qe.bind_values(inv)
    base = qe.evaluate(claims, inv, live)
    by_id = {c["id"]: c for c in claims}
    cited = {i for r in base.values() for i in r.get("claims", []) if i in by_id}
    spans = {}
    for i in cited:
        c = by_id[i]; spans.setdefault((c["source"]["path"], c["source"]["commit"], c["source"]["lines"]), set()).add(i)
    out = []
    for (p, cm, ln), _ in spans.items():
        rest = [c for c in claims if not (c["source"]["path"] == p and c["source"]["commit"] == cm and c["source"]["lines"] == ln)]
        removed = len(claims) - len(rest)
        r = qe.evaluate(rest, inv, live)
        flips = [(k, base[k]["state"], r[k]["state"]) for k in base if base[k]["state"] != r[k]["state"]]
        head = next(c for c in claims if c["source"]["path"] == p and c["source"]["commit"] == cm and c["source"]["lines"] == ln)["quote"][:100]
        out.append({"path": p.split("/")[-1], "commit": cm[:8], "lines": ln, "claims_removed": removed, "flips": flips, "n_flips": len(flips), "first_quote": head})
    out.sort(key=lambda o: (o["n_flips"], -o["claims_removed"]), reverse=True)
    json.dump(out, open(os.path.join(HERE, "impact_ranking_spans.json"), "w"), indent=1, ensure_ascii=False)
    print(f"spans tested: {len(out)}; with any flip: {sum(1 for o in out if o['n_flips'])}")
    for o in out[:20]:
        print(f"{o['n_flips']} flips | {o['path']}:{o['lines']} ({o['commit']}) removed={o['claims_removed']:3} | {[f[0]+':'+f[1][:4]+'>'+f[2][:4] for f in o['flips']]} | {o['first_quote'][:60]}")
if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "spans":
    spans_mode()
