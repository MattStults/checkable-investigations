#!/usr/bin/env python3
"""Row-by-row comparison of the two arms over the frozen inventory.

Ledger arm: results/query_results.json (mechanical queries over the checked
ledger plus live runs). Baseline arm: baseline/REPORT.md (one clean-context
frontier agent). Writes results/arm_comparison.json and prints the table.
No state is edited; disagreements are listed with both derivations for the
owner's adjudication packet."""
import json, os, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)

def main():
    q = json.load(open(os.path.join(HERE, "query_results.json")))
    b = open(os.path.join(X, "baseline/REPORT.md")).read()
    bs, breason = {}, {}
    for m in re.finditer(r"^### (Q\d\d|H\d\d|V\d\d)\n(.*?)(?=^### |\Z)", b, re.M | re.S):
        st = re.search(r"^State: \**(\w+)", m.group(2), re.M)
        rs = re.search(r"^Reason: (.*)$", m.group(2), re.M)
        if st: bs[m.group(1)] = st.group(1).lower(); breason[m.group(1)] = (rs.group(1) if rs else "")[:400]
    rows = []
    for k, v in q.items():
        rows.append({"id": k, "ledger": v["state"], "baseline": bs.get(k), "agree": bs.get(k) == v["state"],
                     "ledger_derivation": v["derivation"][:400], "baseline_reason": breason.get(k, "")})
    groups = {}
    for g in ("Q", "H", "V"):
        rs = [r for r in rows if r["id"].startswith(g)]
        groups[g] = {"n": len(rs), "agree": sum(r["agree"] for r in rs),
                     "ledger": dict(Counter(r["ledger"] for r in rs)), "baseline": dict(Counter(r["baseline"] for r in rs))}
    dis = [r for r in rows if not r["agree"]]
    # classify disagreements by direction: who is stricter (verified < contested < contradicted; unverifiable/dangling apart)
    rank = {"verified": 0, "contested": 1, "contradicted": 2}
    for r in dis:
        a, c = r["ledger"], r["baseline"]
        if a in rank and c in rank: r["direction"] = "ledger stricter" if rank[a] > rank[c] else "baseline stricter"
        elif a in rank: r["direction"] = "baseline could not decide"
        elif c in rank: r["direction"] = "ledger could not decide"
        else: r["direction"] = "neither decided"
    cit = None
    cp = os.path.join(X, "baseline/citations_check.json")
    if os.path.exists(cp):
        cc = json.load(open(cp)); res = cc.get("results", cc if isinstance(cc, list) else [])
        cit = {**cc.get("summary", {}), "note": "baseline Quote lines split into segments and re-verified as verbatim (or ellipsis-abridged verbatim) substrings of the cited file at the pin; live-run items have no file quote"}
    chk = json.load(open(os.path.join(X, "ledger/check_result.json"))); chk = chk.get("summary", chk)
    out = {"groups": groups, "agreement_total": f"{sum(r['agree'] for r in rows)}/{len(rows)}", "disagreements": dis,
           "machine_checkable": {"ledger": {"claims": chk.get("total"), "checker_pass": chk.get("passed"), "note": "every ledger claim carries a verbatim quote, source lines and typed fields; all re-verified by check.py"}, "baseline": cit},
           "rows": rows}
    json.dump(out, open(os.path.join(HERE, "arm_comparison.json"), "w"), indent=1)
    print(json.dumps({"agreement": out["agreement_total"], "groups": {g: (v["agree"], v["n"]) for g, v in groups.items()}, "direction": dict(Counter(r["direction"] for r in dis)), "machine_checkable": out["machine_checkable"]}, indent=1))
    for r in dis:
        print(f"{r['id']:4} ledger={r['ledger']:13} baseline={r['baseline']:13} {r['direction']}")

if __name__ == "__main__":
    main()
