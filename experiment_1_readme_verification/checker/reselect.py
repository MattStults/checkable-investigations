#!/usr/bin/env python3
"""Mechanical reselection after a glossary amendment: over the CURRENT ledger
state (accepted outputs minus superseded ids, retries overriding), find spans
whose claims show the defect class the amendment fixes, and write a whole-span
retry batch. Selectors are regex-on-span-text + predicate-on-claims; no
content judgment. Usage: reselect.py OUT_BATCH_NAME"""
import glob, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE); OUT = os.path.join(X, "ledger/out")
def current_claims():
    superseded = set()
    for rb in glob.glob(os.path.join(X, "ledger/batches/retry_*.json")):
        h = json.load(open(rb))["header"]; name = os.path.basename(rb).replace(".json", "")
        if os.path.exists(os.path.join(OUT, name + "_opus.accepted.jsonl")):
            for s in h.get("superseded_claims", []): superseded.update(s["ids"])
    claims = {}
    for f in sorted(glob.glob(os.path.join(OUT, "*.accepted.jsonl")), key=os.path.getmtime):
        for l in open(f):
            if l.strip():
                c = json.loads(l)
                if c["id"] not in superseded and not (c["translator"]["batch"] == "batch_001" and c["translator"]["model"] == "sonnet"):
                    claims[c["id"]] = c
    return claims
SELECTORS = {
    "G-02": (re.compile(r"((^|\n)\s*[-*#>\d.]*\s*(MATT RULING|RULING:|COUNTERSIGNED|[A-Z ]*RULING \(|SIGNED)|\((the )?project owner|CoVe|re-derived|re-derivation)", re.I),
             lambda cs: cs and all(c["tier"] == "stated" for c in cs)),
    "G-03": (re.compile(r"(Matt:|\(Matt\)|Matt's (ruling|amendment|correction|decision|directive|question)|Matt ruled|Matt confirmed|owner's (ruling|correction|decision))", re.I),
             lambda cs: cs and not any(c["tier"] == "human" for c in cs)),
    "G-04": (re.compile(r"(coordinator|orchestration seat)", re.I),
             lambda cs: any(c["kind"] == "event" and c["event"]["actor"] == ["unstated"] for c in cs)),
    "G-06": (re.compile(r"^(?!.*(Matt|project owner|owner)).*(COUNTERSIGNED|SIGNED|RULING:)", re.I | re.M),
             lambda cs: any(c["tier"] == "human" for c in cs)),
}
def main():
    name = sys.argv[1]
    claims = current_claims()
    by_span = {}
    for c in claims.values(): by_span.setdefault((c["source"]["path"], c["source"]["commit"][:8], c["source"]["lines"]), []).append(c)
    spans = [json.loads(l) for l in open(os.path.join(X, "ledger/spans/spans.jsonl"))]
    sel, sup = [], []
    for s in spans:
        cs = by_span.get((s["path"], s["commit"][:8], s["lines"]), [])
        if not cs: continue
        hits = [k for k, (rx, pred) in SELECTORS.items() if rx.search(s["text"]) and pred(cs)]
        if hits:
            sel.append(s); sup.append({"span": s["id"], "selectors": hits, "ids": [c["id"] for c in cs]})
    brief_v = [l for l in open(os.path.join(X, "brief/BRIEF.md")) if l.startswith("# Translator brief")][0].split("v")[1].split()[0]
    gv = "frozen " + subprocess.check_output(["git", "-C", os.path.dirname(X), "log", "-1", "--format=%h", "--", "experiment_1_readme_verification/glossary/glossary.json"], text=True).strip()
    amend = json.load(open(os.path.join(X, "glossary/glossary.json"))).get("amendments", [])
    hdr = {"brief_version": brief_v, "glossary_version": gv + (" +" + amend[-1]["id"] if amend else "")}
    json.dump({"header": {**hdr, "batch": name, "retranslation_of": "reselect.py over current ledger state", "superseded_claims": sup}, "spans": sel},
              open(os.path.join(X, "ledger/batches", name + ".json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps({"spans": len(sel), "claims_superseded": sum(len(x["ids"]) for x in sup), "by_selector": {k: sum(1 for x in sup if k in x["selectors"]) for k in SELECTORS}}))
    for x in sup: print(x["span"], x["selectors"], len(x["ids"]))
if __name__ == "__main__":
    main()
