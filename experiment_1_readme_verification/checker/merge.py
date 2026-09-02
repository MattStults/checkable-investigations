#!/usr/bin/env python3
"""Assemble ledger/claims.jsonl from accepted translator outputs.
- takes every ledger/out/*.accepted.jsonl (not pre_d05/)
- drops claim ids listed as superseded_claims in any ledger/batches/retry_*.json
  header whose retranslation output was accepted (whole-span retranslations)
- for single-claim retranslations (same id), the later accepted file wins
- writes ledger/claims.jsonl, then runs resolve_links.py and check.py on it.
Prints coverage: spans with zero claims."""
import glob, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)
OUT = os.path.join(X, "ledger/out")
def main():
    superseded = set()
    for rb in glob.glob(os.path.join(X, "ledger/batches/retry_*.json")):
        h = json.load(open(rb))["header"]
        name = os.path.basename(rb).replace(".json", "")
        if any(os.path.exists(os.path.join(OUT, f)) for f in (name + "_opus.accepted.jsonl", name + "_sonnet.accepted.jsonl")):
            for s in h.get("superseded_claims", []):
                superseded.update(s["ids"])
    files = sorted(glob.glob(os.path.join(OUT, "*.accepted.jsonl")), key=os.path.getmtime)
    claims = {}
    for f in files:
        for l in open(f):
            if l.strip():
                c = json.loads(l)
                if c["id"] in superseded:
                    continue
                claims[c["id"]] = c  # later file (retry) overwrites same id
    # the sonnet probe of batch_001 is a tier probe, not ledger content: keep opus for batch_001
    PROBES = {("batch_001", "sonnet"), ("batch_052", "sonnet")}  # tier probes: reported, never merged
    claims = {k: v for k, v in claims.items() if (v["translator"]["batch"], v["translator"]["model"]) not in PROBES}
    path = os.path.join(X, "ledger/claims.jsonl")
    with open(path, "w") as f:
        for k in sorted(claims):
            f.write(json.dumps(claims[k], ensure_ascii=False) + "\n")
    spans = [json.loads(l) for l in open(os.path.join(X, "ledger/spans/spans.jsonl"))]
    covered = {(c["source"]["path"], c["source"]["lines"]) for c in claims.values()}
    uncovered = [s["id"] for s in spans if (s["path"], s["lines"]) not in covered]
    print(json.dumps({"claims": len(claims), "superseded_dropped": len(superseded), "spans": len(spans), "spans_without_claims": len(uncovered)}))
    open(os.path.join(X, "ledger/spans_without_claims.json"), "w").write(json.dumps(uncovered))
    subprocess.run([sys.executable, os.path.join(HERE, "resolve_links.py"), path, path + ".resolved", os.path.join(X, "ledger/resolve_log.jsonl")])
    os.replace(path + ".resolved", path)
    r = subprocess.run([sys.executable, os.path.join(HERE, "check.py"), path, "--json", os.path.join(X, "ledger/check_result.json")], capture_output=True, text=True)
    print(r.stdout.strip().split("\n")[-1])
if __name__ == "__main__":
    main()
