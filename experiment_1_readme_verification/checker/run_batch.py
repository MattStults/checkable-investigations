#!/usr/bin/env python3
"""Check one translator output file, split it into accepted / rejected, and
append a line to results/translation_log.jsonl. Never edits a claim.
Usage: run_batch.py ledger/out/batch_001_opus.jsonl"""
import json, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)
def main():
    src = sys.argv[1]; base = os.path.basename(src).replace(".jsonl", "")
    t0 = time.time()
    res_path = os.path.join(X, "ledger/out", base + ".check.json")
    subprocess.run([sys.executable, os.path.join(HERE, "check.py"), src, "--json", res_path], capture_output=True)
    res = json.load(open(res_path))
    verdict = {r["id"]: r for r in res["results"]}
    acc, rej = [], []
    for line in open(src):
        if not line.strip():
            continue
        c = json.loads(line)
        (acc if verdict.get(c.get("id"), {}).get("pass") else rej).append(c)
    with open(os.path.join(X, "ledger/out", base + ".accepted.jsonl"), "w") as f:
        for c in acc: f.write(json.dumps(c, ensure_ascii=False) + "\n")
    with open(os.path.join(X, "ledger/out", base + ".rejected.jsonl"), "w") as f:
        for c in rej:
            c["_rejection"] = verdict[c["id"]]["fails"]; f.write(json.dumps(c, ensure_ascii=False) + "\n")
    tr = acc[0]["translator"] if acc else (rej[0].get("translator", {}) if rej else {})
    entry = {"file": base, "model": tr.get("model"), "brief_version": tr.get("brief_version"), "batch": tr.get("batch"),
             "claims": len(acc) + len(rej), "accepted": len(acc), "rejected": len(rej),
             "fail_reasons": res["summary"]["fail_reasons"], "checked_at": time.strftime("%Y-%m-%dT%H:%M:%S"), "check_seconds": round(time.time() - t0, 1)}
    with open(os.path.join(X, "results/translation_log.jsonl"), "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(json.dumps(entry))
if __name__ == "__main__":
    main()
