#!/usr/bin/env python3
"""Unseal the blind rulings (D-12b), map A/B back to arms, and compare with the
non-blind rulings (D-12). Scores both label-inclusive and substance-only (a
disagreement is 'label' when both arms' states are in {contested, contradicted,
verified} and differ only by the contested/weighed distinction on the same facts,
as the non-blind adjudicator classified it). Writes SUMMARY.md and summary.json."""
import json, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); RES = os.path.dirname(HERE)

def main():
    mapping = json.load(open(os.path.join(RES, "rulings_blind_mapping.SEALED.json")))
    blind = {}
    for l in open(os.path.join(HERE, "rulings.jsonl")):
        if l.strip(): r = json.loads(l); blind[r["id"]] = r
    nonblind = {}
    for l in open(os.path.join(RES, "rulings/rulings.jsonl")):
        if l.strip(): r = json.loads(l); nonblind[r["id"]] = r
    cmp = {r["id"]: r for r in json.load(open(os.path.join(RES, "arm_comparison.json")))["rows"]}
    rows = []
    for k in sorted(blind, key=lambda s: (s[0], s)):
        b = blind[k]; m = mapping[k]; ar = b.get("arm_right")
        arm = {"A": m["A"], "B": m["B"]}.get(ar, ar)
        c = cmp.get(k, {}); nb = nonblind.get(k, {})
        rows.append({"id": k, "ledger": c.get("ledger"), "baseline": c.get("baseline"), "blind_ruling": b.get("ruling"), "blind_arm_right": arm,
                     "nonblind_ruling": nb.get("ruling"), "nonblind_arm_right": nb.get("arm_right"), "substance_or_label": nb.get("substance_or_label"),
                     "ledger_matches": c.get("ledger") == b.get("ruling"), "baseline_matches": c.get("baseline") == b.get("ruling")})
    agree_rulings = sum(1 for r in rows if r["blind_ruling"] == r["nonblind_ruling"])
    tally = collections.Counter(r["blind_arm_right"] for r in rows)
    # NOTE: substance_or_label is NOT a partition of disagreements. The adjudicator brief asked
    # whether "the disagreement was substance or label", but the field was filled on items where
    # the arms AGREED too (meaning "the agreement was on substance"). Tally over three sets so the
    # reader can see which comparison a number comes from.
    subst = [r for r in rows if r["substance_or_label"] == "substance"]
    disag = [r for r in rows if r["ledger"] != r["baseline"]]
    subst_disag = [r for r in subst if r["ledger"] != r["baseline"]]
    tally_s = collections.Counter(r["blind_arm_right"] for r in subst)
    tally_d = collections.Counter(r["blind_arm_right"] for r in disag)
    match = {"ledger": sum(r["ledger_matches"] for r in rows), "baseline": sum(r["baseline_matches"] for r in rows)}
    mk = lambda st: {"ledger": sum(r["ledger_matches"] for r in st), "baseline": sum(r["baseline_matches"] for r in st)}
    match_s = mk(subst); match_d = mk(disag); match_sd = mk(subst_disag)
    md = ["# Blind re-adjudication summary (D-12b)", "",
          f"Items: {len(rows)}. Blind ruling equals non-blind ruling on {agree_rulings}/{len(rows)}.", "",
          f"Arm whose evidence decided it (unsealed): all {len(rows)} items {dict(tally)}; the {len(disag)} items where the arms differed {dict(tally_d)}.", "",
          "Arm's state equals the blind ruling, by set:", "",
          "| set | n | ledger | baseline |", "|---|---|---|---|",
          f"| all non-verified items | {len(rows)} | {match['ledger']} | {match['baseline']} |",
          f"| items where the arms differed | {len(disag)} | {match_d['ledger']} | {match_d['baseline']} |",
          f"| ...of those, differing on substance | {len(subst_disag)} | {match_sd['ledger']} | {match_sd['baseline']} |",
          f"| adjudicator-tagged \"substance\" (mixed: includes {len(subst)-len(subst_disag)} items the arms agreed on) | {len(subst)} | {match_s['ledger']} | {match_s['baseline']} |", "",
          "| item | ledger | baseline | blind ruling | evidence decided by | non-blind ruling | non-blind arm right | substance/label |", "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['id']} | {r['ledger']} | {r['baseline']} | {r['blind_ruling']} | {r['blind_arm_right']} | {r['nonblind_ruling']} | {r['nonblind_arm_right']} | {r['substance_or_label']} |")
    md += ["", "Blind adjudicators saw arms as A/B (randomized per item) with reasoning removed; mapping unsealed only here. Rulings are model-made (Fable)."]
    open(os.path.join(HERE, "SUMMARY.md"), "w").write("\n".join(md) + "\n")
    json.dump({"rows": rows, "agree_rulings": agree_rulings, "tally_all": dict(tally), "tally_substance": dict(tally_s), "tally_disagreements": dict(tally_d),
               "match_all": match, "match_substance": match_s, "match_disagreements": match_d, "match_substance_disagreements": match_sd,
               "note": "substance_or_label is not a partition of disagreements; it was filled on agreement items too"}, open(os.path.join(HERE, "summary.json"), "w"), indent=1)
    print("\n".join(md[:7]))
    for r in rows: print(r["id"], r["ledger"], "/", r["baseline"], "-> blind", r["blind_ruling"], "by", r["blind_arm_right"], "| non-blind", r["nonblind_ruling"], r["nonblind_arm_right"])

if __name__ == "__main__":
    main()
