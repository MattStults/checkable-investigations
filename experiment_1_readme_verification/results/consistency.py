#!/usr/bin/env python3
"""Internal-consistency pass over the ledger (X06 query class, plus
record-level conflicts the translation surfaced).

1. Value conflicts: claims with the same normalised metric + scope + snapshot
   whose numeric values differ (excluding stance superseded/struck), grouped.
2. Contested pairs: claims with stance contested, with their contradicts refs.
3. Do-not-cite edges: forbids_citation refs and anti_rule claims — which
   values the record marks as not to be cited, and whether standing claims
   restate them without the marking.
4. Struck values still standing: a value with a strikes/supersedes ref
   pointing at it that also appears as a 'current' claim elsewhere.
Output: results/consistency.json + a printed summary. No claim is edited."""
import json, os, re
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)

def num(v):
    if isinstance(v, (int, float)): return float(v)
    if isinstance(v, str):
        m = re.match(r"^\s*[+]?(-?\d+(?:\.\d+)?)\s*%?\s*$", v.replace("−", "-").replace(",", ""))
        if m: return float(m.group(1)) / (100 if v.strip().endswith("%") else 1)
    return None
def norm(s): return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()

def main():
    claims = [json.loads(l) for l in open(os.path.join(X, "ledger/claims.jsonl")) if l.strip()]
    by_id = {c["id"]: c for c in claims}
    # 1. value conflicts
    groups = defaultdict(list)
    for c in claims:
        if c["kind"] in ("value", "rate") and num(c["value"]) is not None and c["stance"] in ("current", "unknown"):
            groups[(norm(c["metric"]), norm(c["scope"]), norm(c["snapshot"]))].append(c)
    conflicts = []
    for k, cs in groups.items():
        vals = sorted({round(num(c["value"]), 4) for c in cs})
        if len(vals) > 1 and k[0] not in ("verdict", "verdicts", "node verdict", "verdicts by node"):
            conflicts.append({"metric": k[0], "scope": k[1], "snapshot": k[2], "values": vals, "claims": [(c["id"], c["value"], c["tier"], c["source"]["path"].split("/")[-1] + ":" + c["source"]["lines"]) for c in cs][:8]})
    # 2. contested pairs
    contested = [{"id": c["id"], "metric": c["metric"], "value": c["value"], "source": c["source"]["path"].split("/")[-1] + ":" + c["source"]["lines"], "refs": [(r["rel"], r["target_text"][:60], r["target_id"]) for r in c["refs"] if r["rel"] == "contradicts"]} for c in claims if c["stance"] == "contested"]
    # 3. do-not-cite
    forbids = [(c["id"], r["target_text"][:80], r["target_id"]) for c in claims for r in c["refs"] if r["rel"] == "forbids_citation"]
    anti = [c for c in claims if c.get("anti_rule")]
    anti_vals = defaultdict(list)
    for c in anti:
        if num(c["value"]) is not None: anti_vals[round(num(c["value"]), 4)].append(c["id"])
    restated_without = []
    for v, ids in anti_vals.items():
        others = [c for c in claims if num(c["value"]) is not None and round(num(c["value"]), 4) == v and not c.get("anti_rule") and c["stance"] in ("current", "unknown") and norm(c["metric"]) == norm(by_id[ids[0]]["metric"])]
        if others: restated_without.append({"value": v, "marked": ids[:4], "unmarked_standing": [(c["id"], c["source"]["path"].split("/")[-1]) for c in others][:6]})
    # 4. struck values still standing
    struck_targets = [(c["id"], r["target_id"], r["rel"]) for c in claims for r in c["refs"] if r["rel"] in ("strikes", "supersedes", "withdraws") and r["target_id"]]
    still = []
    for src, tgt, rel in struck_targets:
        t = by_id.get(tgt)
        if t and t["stance"] in ("current", "unknown"):
            still.append({"by": src, "rel": rel, "target": tgt, "target_metric": t["metric"], "target_value": t["value"], "target_source": t["source"]["path"].split("/")[-1] + ":" + t["source"]["lines"]})
    out = {"value_conflicts": conflicts, "contested": contested, "forbids_citation_edges": forbids, "anti_rule_claims": len(anti), "restated_without_marking": restated_without, "struck_but_standing": still}
    json.dump(out, open(os.path.join(HERE, "consistency.json"), "w"), indent=1, default=str)
    print(json.dumps({"value_conflict_groups": len(conflicts), "contested_claims": len(contested), "forbids_edges": len(forbids), "anti_rule_claims": len(anti), "restated_without_marking": len(restated_without), "struck_but_standing": len(still)}))
    for g in conflicts[:25]:
        print("CONFLICT", g["metric"][:40], "|", g["scope"][:40], "|", g["snapshot"][:30], "|", g["values"], "|", [x[3] for x in g["claims"]][:4])
    for s in still[:15]:
        print("STRUCK-BUT-STANDING", s)
    for r in restated_without[:10]:
        print("RESTATED-WITHOUT-MARKING", r)

if __name__ == "__main__":
    main()
