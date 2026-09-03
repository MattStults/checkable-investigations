#!/usr/bin/env python3
"""Score a capability-probe translation against the merged ledger's claims on the
same spans (Opus for document spans, Sonnet for git-log spans; both accepted by
the checker). Per lane: checker pass rate, numeric (span,value) recall and
precision, event (span,type) recall and precision, and the event types missed.
Usage: capability_probe_score.py <probe_output.jsonl> [<more.jsonl>...]"""
import json, os, re, subprocess, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)

def numv(v):
    try: return round(float(str(v).replace("+", "").replace("%", "")), 4)
    except Exception: return None

def main():
    lanes = json.load(open(os.path.join(HERE, "span_lanes.json")))
    spans = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(X, "ledger/spans/spans.jsonl"))}
    key2id = {(s["path"], s["lines"], s["commit"]): i for i, s in spans.items()}
    ref = collections.defaultdict(list)
    for l in open(os.path.join(X, "ledger/claims.jsonl")):
        c = json.loads(l); ref[(c["source"]["path"], c["source"]["lines"])].append(c)
    out = {}
    for f in sys.argv[1:]:
        probe = [json.loads(l) for l in open(f) if l.strip()]
        # checker pass rate via check.py on the probe file
        r = subprocess.run([sys.executable, os.path.join(X, "checker/check.py"), f, "--json", f + ".check.json"], capture_output=True, text=True)
        chk = json.load(open(f + ".check.json")).get("summary", {})
        by_lane = collections.defaultdict(lambda: {"probe_claims": 0, "ref_claims": 0, "num_shared": 0, "num_probe": 0, "num_ref": 0, "ev_shared": 0, "ev_probe": 0, "ev_ref": 0, "missed_types": collections.Counter(), "extra_types": collections.Counter(), "spans": 0})
        touched = {(c["source"]["path"], c["source"]["lines"]) for c in probe}
        for k in touched:
            sid = key2id.get((k[0], k[1], "pin")) or key2id.get((k[0], k[1], "generated"))
            lane = lanes.get(sid, "?")[0] if sid else "?"
            d = by_lane[lane]; d["spans"] += 1
            pc = [c for c in probe if (c["source"]["path"], c["source"]["lines"]) == k]; rc = ref.get(k, [])
            d["probe_claims"] += len(pc); d["ref_claims"] += len(rc)
            pn = {numv(c["value"]) for c in pc if c["kind"] in ("value", "rate") and numv(c["value"]) is not None}
            rn = {numv(c["value"]) for c in rc if c["kind"] in ("value", "rate") and numv(c["value"]) is not None}
            d["num_shared"] += len(pn & rn); d["num_probe"] += len(pn); d["num_ref"] += len(rn)
            pe = {c["event"]["type"] for c in pc if c["kind"] == "event" and c.get("event")}
            re_ = {c["event"]["type"] for c in rc if c["kind"] == "event" and c.get("event")}
            d["ev_shared"] += len(pe & re_); d["ev_probe"] += len(pe); d["ev_ref"] += len(re_)
            for t in re_ - pe: d["missed_types"][t] += 1
            for t in pe - re_: d["extra_types"][t] += 1
        print(f"\n== {os.path.basename(f)}: checker {chk.get('passed')}/{chk.get('total')} pass; fail reasons {chk.get('fail_reasons')}")
        for lane, d in sorted(by_lane.items()):
            nr = d["num_shared"] / d["num_ref"] if d["num_ref"] else None; npr = d["num_shared"] / d["num_probe"] if d["num_probe"] else None
            er = d["ev_shared"] / d["ev_ref"] if d["ev_ref"] else None; epr = d["ev_shared"] / d["ev_probe"] if d["ev_probe"] else None
            fmt = lambda x: "n/a" if x is None else f"{x:.0%}"
            print(f"  lane {lane}: spans {d['spans']}, claims probe {d['probe_claims']} vs ref {d['ref_claims']} | numbers recall {fmt(nr)} precision {fmt(npr)} ({d['num_shared']}/{d['num_ref']}) | event types recall {fmt(er)} precision {fmt(epr)} ({d['ev_shared']}/{d['ev_ref']}) | missed {dict(d['missed_types'])} | extra {dict(d['extra_types'])}")
            d["missed_types"] = dict(d["missed_types"]); d["extra_types"] = dict(d["extra_types"])
        out[os.path.basename(f)] = {"checker": chk, "by_lane": dict(by_lane)}
    json.dump(out, open(os.path.join(HERE, "capability_probe_score.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
