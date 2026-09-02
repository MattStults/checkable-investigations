#!/usr/bin/env python3
"""Cut spans.jsonl into translator batches. Deterministic: spans in id order
within source class, N spans per batch (lines-capped). Writes
ledger/batches/batch_NNN.json = {header, spans[]} where header carries the
brief and glossary versions in force and the batch id the translator must
copy into every claim. Usage: batch.py [--per 15] [--max-lines 400]"""
import argparse, json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)
def ver(path):
    return subprocess.check_output(["git", "-C", X, "log", "-1", "--format=%h", "--", path], text=True).strip()
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--per", type=int, default=15); ap.add_argument("--max-lines", type=int, default=400)
    a = ap.parse_args()
    spans = [json.loads(l) for l in open(os.path.join(X, "ledger/spans/spans.jsonl")) if l.strip()]
    order = ["ledger", "arc2_json", "arc2_docs", "arc1_docs", "arc1_cycles", "git_log", "ledger_preredaction", "arc2_docs_preredaction", "arc1_docs_preredaction"]
    bid, out = 0, []
    brief_v = [l for l in open(os.path.join(HERE, "BRIEF.md")) if l.startswith("# Translator brief")][0].split("v")[1].split()[0]
    for cls in order:
        cur, lines = [], 0
        for s in [s for s in spans if s["source_class"] == cls]:
            n = s["text"].count("\n") + 1
            if cur and (len(cur) >= a.per or lines + n > a.max_lines):
                bid += 1; out.append((bid, cls, cur)); cur, lines = [], 0
            cur.append(s); lines += n
        if cur:
            bid += 1; out.append((bid, cls, cur))
    for bid, cls, cur in out:
        hdr = {"batch": f"batch_{bid:03d}", "source_class": cls, "brief_version": brief_v, "glossary_version": "frozen " + ver("experiment_1_readme_verification/glossary/glossary.json"), "spans": len(cur), "first_span": cur[0]["id"], "last_span": cur[-1]["id"]}
        json.dump({"header": hdr, "spans": cur}, open(os.path.join(X, "ledger/batches", f"batch_{bid:03d}.json"), "w"), indent=1, ensure_ascii=False)
    json.dump([{"batch": f"batch_{b:03d}", "source_class": c, "spans": len(s), "lines": sum(x["text"].count("\n") + 1 for x in s)} for b, c, s in out], open(os.path.join(X, "ledger/batches/index.json"), "w"), indent=1)
    print(len(out), "batches")
if __name__ == "__main__":
    main()
