#!/usr/bin/env python3
"""Completeness of a claim set against deterministic denominators per span:
numeric literals (excluding dates and single digits), event markers, backticked paths.
Usage: completeness_audit.py [claims.jsonl]  (default ledger/claims.jsonl). Prints per source class."""
import json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)
NUM = re.compile(r"(?<![\w./-])[+-]?\d+(?:,\d{3})*(?:\.\d+)?%?(?![\w/-])")
MARK = re.compile(r"\b(ERRATUM|RULING|SIGNED|COUNTERSIGNED|WITHDRAWN|WITHDRAWAL|STRUCK|VOID(?:ED)?|SUPERSEDED|REGISTERED|REGISTRATION|BINDING|ADDENDUM|DISPATCH(?:ED)?|CoVe|re-derived)\b")
PATH = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|json|py|jsonl|lp|yml|txt))`")
def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(X, "ledger/claims.jsonl")
    spans = [json.loads(l) for l in open(os.path.join(X, "ledger/spans/spans.jsonl"))]
    cl = [json.loads(l) for l in open(path) if l.strip()]
    byspan = collections.defaultdict(list)
    for c in cl: byspan[(c["source"]["path"], c["source"]["lines"])].append(c)
    agg = collections.defaultdict(collections.Counter); uncovered = []
    for s in spans:
        claims = byspan.get((s["path"], s["lines"]), [])
        if not claims: continue
        sc = s["source_class"].replace("_preredaction", ""); text = s["text"]
        if sc == "git_log": text = "\n".join(l for l in text.split("\n") if not l.startswith(("commit ", "ordinal ", "date ", "author ")))
        for tok in [m.group(0) for m in NUM.finditer(text) if not re.fullmatch(r"\d{4}-\d{2}-\d{2}|[+-]?\d", m.group(0))]:
            t = tok.replace(",", "").replace("+", "").rstrip("%")
            ok = any(str(c.get(k)).replace("+", "") == t for c in claims for k in ("value", "numerator", "denominator")) or any(re.search(r"(?<![\w.])" + re.escape(tok) + r"(?![\w])", c["quote"]) for c in claims)
            agg[sc]["num_total"] += 1; agg[sc]["num_covered"] += ok
            if not ok: uncovered.append({"span": s["id"], "kind": "number", "token": tok})
        for m in MARK.finditer(text):
            ok = any(re.search(re.escape(m.group(0)), c["quote"]) for c in claims); agg[sc]["mark_total"] += 1; agg[sc]["mark_covered"] += ok
            if not ok: uncovered.append({"span": s["id"], "kind": "marker", "token": m.group(0)})
        for m in PATH.finditer(text):
            ok = any(m.group(1) in c["quote"] for c in claims); agg[sc]["path_total"] += 1; agg[sc]["path_covered"] += ok
    tot = collections.Counter()
    for sc, a in sorted(agg.items()):
        tot.update(a); f = lambda k: (f"{a[k+'_covered']}/{a[k+'_total']} ({a[k+'_covered']/a[k+'_total']:.0%})" if a[k + "_total"] else "n/a")
        print(f"{sc:22} numbers {f('num'):16} markers {f('mark'):14} paths {f('path')}")
    f = lambda k: f"{tot[k+'_covered']}/{tot[k+'_total']} ({tot[k+'_covered']/tot[k+'_total']:.0%})"
    print(f"{'ALL':22} numbers {f('num'):16} markers {f('mark'):14} paths {f('path')}")
    json.dump(uncovered, open(os.path.join(HERE, "completeness_uncovered.json"), "w"), indent=0)
if __name__ == "__main__":
    main()
