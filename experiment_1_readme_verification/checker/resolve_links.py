#!/usr/bin/env python3
"""Fill refs[].target_id by matching target_text to claims. Never edits any
other field. Usage: resolve_links.py claims.jsonl OUT.jsonl LOG.jsonl

Matching basis, tried in order, first hit wins; every decision is logged
with the basis so it can be audited and reversed:
  1. entry number: target_text contains a 4-digit entry number NNNN and a
     claim's source is the ledger with snapshot 'entry NNNN' (event claims
     preferred).
  2. commit hash: target_text contains a >=7-hex token equal to a claim's
     source.commit prefix or a git_log claim's value.
  3. value + metric words: target_text contains a number equal to a claim's
     value and at least one whitespace-separated word (len>=4) of target_text
     appears in that claim's metric or quote.
  4. quote overlap: a claim's quote (normalised) contains target_text or
     target_text contains a >=6-word window of the claim's quote.
Unmatched refs keep target_id null and are logged as unresolved."""
import json, re, sys

def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()

def main():
    src, out, logp = sys.argv[1:4]
    claims = [json.loads(l) for l in open(src) if l.strip()]
    by_id = {c["id"]: c for c in claims}
    log = []
    for c in claims:
        for r in c.get("refs", []):
            if r.get("target_id"):
                continue
            t = r["target_text"]; tn = norm(t)
            hit, basis = None, None
            m = re.search(r"\b(\d{4})\b", t)
            if m:
                cands = [x for x in claims if x["id"] != c["id"] and f"entry {m.group(1)}" in norm(x.get("snapshot", "")) and "ITERATION_NOTES" in x["source"]["path"]]
                cands.sort(key=lambda x: 0 if x["kind"] == "event" else 1)
                if cands:
                    hit, basis = cands[0], f"entry number {m.group(1)}"
            if not hit:
                m = re.search(r"\b([0-9a-f]{7,40})\b", t)
                if m:
                    h = m.group(1)
                    cands = [x for x in claims if x["id"] != c["id"] and (str(x["source"].get("commit", "")).startswith(h) or (isinstance(x.get("value"), str) and x["value"].startswith(h)))]
                    if cands:
                        hit, basis = cands[0], f"commit {h}"
            if not hit:
                nums = re.findall(r"\d+(?:\.\d+)?%?", t)
                words = [w for w in re.findall(r"[a-z][a-z-]{3,}", tn)]
                for x in claims:
                    if x["id"] == c["id"]:
                        continue
                    v = x.get("value")
                    vs = [str(v)] if v is not None else []
                    if isinstance(v, (int, float)):
                        vs += [f"{v:g}", f"{round(v*100):d}%"]
                    if any(n in vs or n.rstrip("%") in vs for n in nums) and any(w in norm(x.get("metric", "")) or w in norm(x.get("quote", "")) for w in words):
                        hit, basis = x, f"value {nums} + metric/quote word"
                        break
            if not hit:
                for x in claims:
                    if x["id"] == c["id"]:
                        continue
                    q = norm(x.get("quote", ""))
                    ws = tn.split()
                    if tn and (tn in q or any(" ".join(ws[i:i+6]) in q for i in range(max(1, len(ws) - 5)))):
                        hit, basis = x, "quote overlap"
                        break
            if hit:
                r["target_id"] = hit["id"]
            log.append({"claim": c["id"], "rel": r["rel"], "target_text": t, "target_id": hit["id"] if hit else None, "basis": basis or "unresolved"})
    with open(out, "w") as f:
        for c in claims:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    with open(logp, "w") as f:
        for e in log:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    n = sum(1 for e in log if e["target_id"])
    print(json.dumps({"refs": len(log), "resolved": n, "unresolved": len(log) - n}))

if __name__ == "__main__":
    main()
