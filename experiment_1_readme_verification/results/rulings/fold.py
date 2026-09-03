#!/usr/bin/env python3
"""Fold model-made rulings (D-12) into a summary: per item the two arms' states,
the ruling, which arm was right, substance vs label, owner input needed, and
README disposition. Writes results/rulings/SUMMARY.md and rulings_summary.json."""
import json, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); RES = os.path.dirname(HERE); X = os.path.dirname(RES)

def main():
    rows = {}
    for l in open(os.path.join(HERE, "rulings.jsonl")):
        if l.strip():
            r = json.loads(l); rows[r["id"]] = r  # last write wins
    cmp = {r["id"]: r for r in json.load(open(os.path.join(RES, "arm_comparison.json")))["rows"]}
    out = []
    for k in sorted(rows, key=lambda s: (s[0], s)):
        r = rows[k]; c = cmp.get(k, {})
        out.append({"id": k, "ledger": c.get("ledger"), "baseline": c.get("baseline"), "ruling": r.get("ruling"),
                    "arm_right": r.get("arm_right"), "substance_or_label": r.get("substance_or_label"),
                    "owner_input_needed": r.get("owner_input_needed"), "disposition": r.get("disposition")})
    right = collections.Counter(o["arm_right"] for o in out)
    agree_ruling = {"ledger": sum(1 for o in out if o["ledger"] == o["ruling"]), "baseline": sum(1 for o in out if o["baseline"] == o["ruling"])}
    md = ["# Rulings summary (model adjudication, D-12)", "",
          f"Items ruled: {len(out)}. Arm judged right: {dict(right)}. Arm's state equals the ruling: {agree_ruling}. Owner input still needed on {sum(1 for o in out if o['owner_input_needed'])} item(s).", "",
          "| item | ledger | baseline | ruling | arm right | substance/label | owner input | README disposition |", "|---|---|---|---|---|---|---|---|"]
    for o in out:
        md.append(f"| {o['id']} | {o['ledger']} | {o['baseline']} | {o['ruling']} | {o['arm_right']} | {o['substance_or_label']} | {'yes' if o['owner_input_needed'] else 'no'} | {str(o['disposition'])[:90]} |")
    md += ["", "Every ruling here was made by a Fable adjudicator from the packets, the read-only repository and the owner's recorded testimony; rulings marked as needing owner input are provisional. Per-item basis in `<id>.md`."]
    open(os.path.join(HERE, "SUMMARY.md"), "w").write("\n".join(md) + "\n")
    json.dump({"rows": out, "arm_right": dict(right), "state_equals_ruling": agree_ruling}, open(os.path.join(HERE, "rulings_summary.json"), "w"), indent=1)
    print("\n".join(md[:4]))
    for o in out: print(o["id"], o["ledger"], "/", o["baseline"], "->", o["ruling"], "|", o["arm_right"], "|", o["substance_or_label"])

if __name__ == "__main__":
    main()
