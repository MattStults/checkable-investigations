#!/usr/bin/env python3
"""Exhaustive span assignment over the named primary sources.

Spans are cut mechanically, never by content relevance (the orchestrator has
read the README; targeting spans would leak). Rules:
  * ITERATION_NOTES.md: one span per numbered entry (heading to next heading).
  * Markdown documents: one span per H2/H3 section, split at 60 lines.
  * JSON files: one span per top-level key (or the whole file if small),
    rendered as the file's own lines.
  * git log: one span per commit (hash, date, author, trailers, subject, body)
    written to a generated text file that is itself committed under
    ledger/spans/ so quotes remain checkable.
  * Pre-redaction blobs: the same cut applied to the file at 6d01415b^ for
    every file that commit modified among the named sources.

Usage: spans.py OUT_DIR [--repo R] [--pin SHA]
Writes OUT_DIR/spans.jsonl (one span per line: id, path, commit, lines,
text, source_class) and OUT_DIR/generated/<name>.txt for synthetic sources.
"""
import argparse, json, os, re, subprocess, sys

DEFAULT_REPO = os.path.expanduser("~/Documents/ai_safety_projects/semi-formal-document-analysis")
PIN = "48e66ce04a4d9f06771c42f89cb37b075583c5f6"
REDACT = "6d01415be03a62ccaafa8a2fb8ca437c9f428094"
BP = "walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/"
G2 = "walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/"
SFE = "semi-formal-experiment/"

SOURCES = {
    "ledger": [BP + "ITERATION_NOTES.md"],
    "arc2_docs": [BP + "HANDOFF_CURRENT.md", BP + "CALCULUS_RUNBOOK.md", BP + "ROUND4_PREREG.md",
                  BP + "PREREG_panel_equivalence.md", BP + "L1L2_ADVERSARIAL_REVIEW.md",
                  BP + "L1L2_REVIEW_DISPOSITION.md", BP + "RETRANS_REVIEW_DISPOSITION.md",
                  BP + "GENERALIZATION_PREREG_DRAFT.md", BP + "BLOCK2_TRANSFER_PREDICTIONS.md",
                  BP + "TRANSLATION_CONTRACT_V2.md", G2 + "SEMANTIC_AUDIT.md", G2 + "PRUNED.md"],
    "arc2_json": [BP + "ROUND4_DEV_TABLE.json", BP + "round4_caution_scored_raw.json",
                  BP + "round4_harm_scored_raw.json", BP + "round4_helpfulness_scored_final_raw.json",
                  BP + "round4_helpfulness_scored_v2.json", BP + "round4_helpfulness_scored.json",
                  BP + "ITER1_ATTEMPT2_SCORED.json", BP + "ITER2_ATTEMPT3_SCORED.json",
                  BP + "ITER2_REMEASURE_SCORED.json", BP + "ITER3_ATTEMPT4_SCORED.json",
                  G2 + "semantic_audit.json"],
    "arc1_docs": [SFE + "HANDOFF.md", SFE + "MODULE_MAP.md", SFE + "REPRODUCIBILITY.md",
                  SFE + "CYCLE_DESIGN.md", SFE + "machine/README.md", SFE + "adversarial_review_1.md",
                  SFE + "cycles/CYCLE_LOG.jsonl", "ARTIFACTS.md", "AGENTS.md", ".github/workflows/ci.yml",
                  "LICENSE", "data/panel-v5/LICENSE", "data/panel-v5/NOTICE"],
    "arc1_cycles": [],  # filled from ls at runtime: every decision.json, review_verdict.json, prediction.json
}

def git(repo, *a):
    return subprocess.check_output(["git", "-C", repo, *a], stderr=subprocess.DEVNULL).decode("utf-8", "replace")

def show(repo, commit, path):
    try:
        return git(repo, "show", f"{commit}:{path}")
    except subprocess.CalledProcessError:
        return None

def cut_markdown(lines, maxlen=60, entry_mode=False):
    """Yield (a, b) 1-based inclusive ranges."""
    heads = [i for i, l in enumerate(lines) if (l.startswith("## ") if entry_mode else re.match(r"^#{1,3} ", l))]
    if not heads or heads[0] != 0:
        heads = [0] + heads
    bounds = heads + [len(lines)]
    for a, b in zip(bounds, bounds[1:]):
        if b - a <= maxlen or entry_mode:
            yield a + 1, b
        else:
            for s in range(a, b, maxlen):
                yield s + 1, min(s + maxlen, b)

def cut_json(lines, maxlen=80):
    """One span per top-level key INCLUDING its full nested value (brace/bracket
    depth tracked on the pretty-printed text; strings are not parsed, so a
    brace inside a string can mis-cut — the checker's verbatim rule catches
    any resulting bad quote). Values longer than maxlen lines are split into
    consecutive windows that each restate the key line first."""
    text = "\n".join(lines)
    starts = [i for i, l in enumerate(lines) if re.match(r'^ {0,2}"[^"]+":', l)]
    if len(starts) < 2:
        yield 1, len(lines)
        return
    bounds = []
    for s in starts:
        depth = 0
        end = s
        for j in range(s, len(lines)):
            depth += lines[j].count("{") + lines[j].count("[") - lines[j].count("}") - lines[j].count("]")
            end = j
            if depth <= 0:
                break
        bounds.append((s, end))
    for s, e in bounds:
        if e - s + 1 <= maxlen:
            yield s + 1, e + 1
        else:
            k = s
            while k <= e:
                yield k + 1, min(k + maxlen, e + 1)
                k += maxlen

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--pin", default=PIN)
    a = ap.parse_args()
    os.makedirs(os.path.join(a.out, "generated"), exist_ok=True)
    spans = []
    n = 0
    def add(path, commit, lines_, a_, b_, cls):
        nonlocal n
        n += 1
        spans.append({"id": f"S{n:05d}", "path": path, "commit": commit, "lines": f"{a_}-{b_}",
                      "text": "\n".join(lines_[a_ - 1:b_]), "source_class": cls})
    # cycles
    cyc = git(a.repo, "ls-tree", "-r", "--name-only", a.pin, SFE + "cycles/").split("\n")
    SOURCES["arc1_cycles"] = [p for p in cyc if p.endswith(("decision.json", "review_verdict.json", "prediction.json", "state.json"))]
    for cls, paths in SOURCES.items():
        for path in paths:
            text = show(a.repo, a.pin, path)
            if text is None:
                print("missing at pin:", path, file=sys.stderr)
                continue
            lines = text.split("\n")
            if path.endswith(".json") or path.endswith(".jsonl"):
                cuts = cut_json(lines) if path.endswith(".json") else [(i + 1, i + 1) for i in range(len(lines)) if lines[i].strip()]
            else:
                cuts = cut_markdown(lines, entry_mode=(cls == "ledger"))
            for x, y in cuts:
                if "\n".join(lines[x - 1:y]).strip():
                    add(path, "pin", lines, x, y, cls)
    # pre-redaction blobs for named sources touched by the redaction commit
    changed = set(git(a.repo, "show", "--name-only", "--format=", REDACT).split("\n"))
    for cls, paths in SOURCES.items():
        for path in paths:
            if path in changed:
                text = show(a.repo, REDACT + "^", path)
                if text is None:
                    continue
                lines = text.split("\n")
                cuts = cut_markdown(lines, entry_mode=(cls == "ledger")) if not path.endswith(".json") else cut_json(lines)
                pre = git(a.repo, "rev-parse", REDACT + "^").strip()
                for x, y in cuts:
                    if "\n".join(lines[x - 1:y]).strip():
                        add(path, pre, lines, x, y, cls + "_preredaction")
    # git log as a generated source file
    log = git(a.repo, "log", "--first-parent", "--reverse", "--format=commit %H%nordinal %%ORD%%%ndate %ci%nauthor %an%nsubject %s%n%b%n----END----", a.pin)
    out_lines, ordinal = [], 0
    for line in log.split("\n"):
        if line.startswith("commit "):
            ordinal += 1
        out_lines.append(line.replace("%ORD%", str(ordinal)))
    gen = os.path.join(a.out, "generated", "git_log_first_parent.txt")
    open(gen, "w").write("\n".join(out_lines) + "\n")
    lines = out_lines
    starts = [i for i, l in enumerate(lines) if l.startswith("commit ")]
    bounds = starts + [len(lines)]
    for x, y in zip(bounds, bounds[1:]):
        add("GENERATED:generated/git_log_first_parent.txt", "generated", lines, x + 1, y, "git_log")
    with open(os.path.join(a.out, "spans.jsonl"), "w") as f:
        for s in spans:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    from collections import Counter
    print(json.dumps({"spans": len(spans), "by_class": Counter(s["source_class"] for s in spans),
                      "total_lines": sum(len(s["text"].split("\n")) for s in spans)}, default=dict))

if __name__ == "__main__":
    main()
