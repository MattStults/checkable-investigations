#!/usr/bin/env python3
"""List batches with no accepted output yet, with the claim-id base each must use."""
import json, os, sys
X = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx = json.load(open(os.path.join(X, "ledger/batches/index.json")))
n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
out = []
for b in idx:
    if not os.path.exists(os.path.join(X, "ledger/out", b["batch"] + "_opus.accepted.jsonl")) and not os.path.exists(os.path.join(X, "ledger/out", b["batch"] + "_opus.jsonl")):
        num = int(b["batch"].split("_")[1])
        out.append({**b, "id_base": f"L{num*10000+1}"})
    if len(out) >= n: break
for b in out: print(json.dumps(b))
