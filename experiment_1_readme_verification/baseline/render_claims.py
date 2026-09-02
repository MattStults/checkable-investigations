#!/usr/bin/env python3
"""Render the frozen inventory's claim list for the baseline reviewer:
sentences, values, declared dimensions, hypothesis rules with their English,
verdict nodes and commitments. Nothing else from the experiment (no sealed
annex, no glossary, no ledger, no reviews, no notes that reference the
record) reaches the baseline."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)
d = json.load(open(os.path.join(X, "claim_inventory/inventory.json")))
o = []
w = o.append
w("# Claims to verify\n")
w(f"README of https://github.com/MattStults/semi-formal-document-analysis at commit `{d['pin']['commit']}`, file `README.md`. Each item below quotes the README verbatim and names the value(s) asserted and the dimensions a verification must pin down.\n")
w("## Quantitative / checkable claims\n")
for c in d["claims"]:
    w(f"### {c['id']}\n> " + c["sentence"].replace("\n", "\n> ") + "\n")
    w("Values: `" + json.dumps(c["values"], ensure_ascii=False) + "`  ")
    w("Dimensions: " + "; ".join(f"{k}: {v}" for k, v in c["dimensions"].items()) + "\n")
w("## Universally quantified prose claims (hypotheses)\n")
for h in d["hypotheses"]:
    w(f"### {h['id']}\n> {h['sentence']}\n\nReading: {h['english_in']}  \nRule: `{h['rule']}`  \nScope: {h['scope']}\n")
w("## Verdict statements (verify via their needs)\n")
for v in d["verdict_nodes"]:
    w(f"### {v['id']}\n> {v['sentence']}\n\nNeeds: " + "; ".join(v["needs"]) + "\n")
w("## Author commitments (report whether the record bears them out; no state required)\n")
for c in d["commitments"]:
    w(f"- **{c['id']}** > {c['sentence']}")
open(os.path.join(HERE, "CLAIMS.md"), "w").write("\n".join(o) + "\n")
print("rendered", len(d["claims"]), len(d["hypotheses"]), len(d["verdict_nodes"]), len(d["commitments"]))
