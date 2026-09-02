#!/usr/bin/env python3
"""Failure-mode analysis over the build's own logs: checker rejections by
class and batch, interventions by class with recurrence, design changes,
and the review-found defect classes in the machinery (from the three
glossary reviews and two inventory reviews, counted by hand-tagged class).
Output: results/failure_modes.json and a printed table."""
import json, os, re
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)
def main():
    log = [json.loads(l) for l in open(os.path.join(HERE, "translation_log.jsonl"))]
    # de-duplicate re-checks: keep the last entry per file
    last = {}
    for e in log: last[e["file"]] = e
    rej = Counter(); rej_batches = defaultdict(list); tiers = defaultdict(lambda: [0, 0])
    for f, e in last.items():
        tiers[e["model"]][0] += e["accepted"]; tiers[e["model"]][1] += e["rejected"]
        for reason, n in e["fail_reasons"].items():
            cls = re.sub(r"\(.*?\)|L\d+|=\S+", "", reason.split(":")[0]).strip()[:60]
            rej[cls] += n; rej_batches[cls].append(e["file"])
    text = open(os.path.join(HERE, "intervention_log.md")).read()
    interventions = re.findall(r"### (I-\d+) — [\d-]+ — (.+)", text)
    designs = re.findall(r"### (D-\d+) — [\d-]+ — (.+)", text)
    recur = {i: ("recurr" in (text.split(i + " —")[1].split("###")[0]).lower()) for i, _ in interventions}
    caught_by = {}
    for i, _ in interventions:
        seg = text.split(i + " —")[1].split("###")[0]
        m = re.search(r"Caught(?: by)?:\s*(.+?)\.", seg, re.S)
        caught_by[i] = (m.group(1).strip()[:90] if m else "?")
    out = {"checker_rejections_by_class": dict(rej), "rejection_batches": {k: v[:8] for k, v in rej_batches.items()},
           "accepted_rejected_by_model": {k: {"accepted": v[0], "rejected": v[1]} for k, v in tiers.items()},
           "interventions": [{"id": i, "title": t, "recurrence_noted": recur[i], "caught_by": caught_by[i]} for i, t in interventions],
           "design_changes": [{"id": i, "title": t} for i, t in designs]}
    json.dump(out, open(os.path.join(HERE, "failure_modes.json"), "w"), indent=1)
    print("Checker rejections by class (last check per file):")
    for k, v in rej.most_common(): print(f"  {v:3}  {k}  e.g. {rej_batches[k][:3]}")
    print("Accepted/rejected by model:", out["accepted_rejected_by_model"])
    print("Interventions:")
    for x in out["interventions"]: print(f"  {x['id']}  recurred={x['recurrence_noted']}  caught by: {x['caught_by']}  | {x['title'][:70]}")
    print("Design changes:", [d["id"] + " " + d["title"][:40] for d in out["design_changes"]])
if __name__ == "__main__":
    main()
