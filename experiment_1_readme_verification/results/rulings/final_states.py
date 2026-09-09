#!/usr/bin/env python3
"""Final per-item states: the model ruling (D-12), the blind ruling (D-12b) and the
owner ruling where one exists, plus how often each arm's state equals the final one.

Tallied over three sets, because `substance_or_label` is NOT a partition of
disagreements: the adjudicator brief asked whether "the disagreement was substance
or label", but adjudicators filled the field on items where the arms AGREED too
(meaning "the agreement was on substance"). Reporting only the substance subset
therefore mixes agreements into a comparison of the arms. Writes FINAL_STATES.md
and final_states.json."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); RES = os.path.dirname(HERE)

def main():
    load = lambda p: {r["id"]: r for r in (json.loads(l) for l in open(p) if l.strip())}
    model = load(os.path.join(HERE, "rulings.jsonl"))
    owner = load(os.path.join(HERE, "owner_rulings.jsonl"))
    blind = load(os.path.join(RES, "rulings_blind/rulings.jsonl"))
    cmp = {r["id"]: r for r in json.load(open(os.path.join(RES, "arm_comparison.json")))["rows"]}
    rows = []
    for k in sorted(model, key=lambda s: (s[0], s)):
        final = owner[k]["owner_ruling"] if k in owner else model[k]["ruling"]
        c = cmp.get(k, {})
        rows.append({"id": k, "ledger": c.get("ledger"), "baseline": c.get("baseline"),
                     "model_ruling": model[k]["ruling"], "blind_ruling": blind.get(k, {}).get("ruling"),
                     "owner_ruling": owner[k]["owner_ruling"] if k in owner else None, "final": final,
                     "substance_or_label": model[k].get("substance_or_label"),
                     "arms_differed": c.get("ledger") != c.get("baseline"),
                     "ledger_matches": c.get("ledger") == final, "baseline_matches": c.get("baseline") == final})
    disag = [r for r in rows if r["arms_differed"]]
    subst = [r for r in rows if r["substance_or_label"] == "substance"]
    subst_disag = [r for r in subst if r["arms_differed"]]
    mk = lambda st: {"n": len(st), "ledger": sum(r["ledger_matches"] for r in st), "baseline": sum(r["baseline_matches"] for r in st)}
    sets = {"all": mk(rows), "disagreements": mk(disag), "substance_disagreements": mk(subst_disag), "adjudicator_substance_tag": mk(subst)}
    changed = [r["id"] for r in rows if r["owner_ruling"] and r["owner_ruling"] != r["model_ruling"]]
    md = ["# Final states after owner rulings", "",
          f"Owner decisions D1-D6 applied (`results/DECISIONS.md`). Owner ruling differs from the model ruling on: {changed or 'none'}.", "",
          "Arm state equals the final ruling. `substance_or_label` is not a partition of",
          "disagreements (adjudicators filled it on agreement items too), so the fairest",
          "arm-vs-arm number is the second row; the third is the same restricted to",
          "substance, and is small-n.", "",
          "| set | n | ledger | baseline |", "|---|---|---|---|",
          f"| all non-verified items | {sets['all']['n']} | {sets['all']['ledger']} | {sets['all']['baseline']} |",
          f"| items where the arms differed | {sets['disagreements']['n']} | {sets['disagreements']['ledger']} | {sets['disagreements']['baseline']} |",
          f"| ...of those, differing on substance | {sets['substance_disagreements']['n']} | {sets['substance_disagreements']['ledger']} | {sets['substance_disagreements']['baseline']} |",
          f"| adjudicator-tagged \"substance\" (mixed: {sets['adjudicator_substance_tag']['n'] - sets['substance_disagreements']['n']} of these are items the arms agreed on) | {sets['adjudicator_substance_tag']['n']} | {sets['adjudicator_substance_tag']['ledger']} | {sets['adjudicator_substance_tag']['baseline']} |", "",
          "| item | ledger | baseline | model | blind | owner | final | arms differed |", "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['id']} | {r['ledger']} | {r['baseline']} | {r['model_ruling']} | {r['blind_ruling']} | {r['owner_ruling'] or ''} | **{r['final']}** | {'yes' if r['arms_differed'] else 'no'} |")
    open(os.path.join(HERE, "FINAL_STATES.md"), "w").write("\n".join(md) + "\n")
    json.dump({"rows": rows, "sets": sets, "owner_changed": changed,
               "note": "substance_or_label is not a partition of disagreements; adjudicators filled it on agreement items too"},
              open(os.path.join(HERE, "final_states.json"), "w"), indent=1)
    print("\n".join(md[:14]))

if __name__ == "__main__":
    main()
