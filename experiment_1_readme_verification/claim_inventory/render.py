#!/usr/bin/env python3
"""Render inventory.json to inventory.md and verify every quoted sentence is a
verbatim substring (whitespace-normalised; ' ... ' joins non-adjacent spans) of
the pinned README. Usage: python3 render.py [path/to/pinned/README.md]

Exit status 1 if any quote is not verbatim."""
import json, re, sys, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
INV = os.path.join(HERE, "inventory.json")
d = json.load(open(INV))

def norm(s):
    return re.sub(r"\s+", " ", s)

readme_text = None
if len(sys.argv) > 1:
    readme_text = open(sys.argv[1]).read()
else:
    repo = os.path.expanduser("~/Documents/ai_safety_projects/semi-formal-document-analysis")
    try:
        readme_text = subprocess.check_output(
            ["git", "-C", repo, "show", f"{d['pin']['commit']}:README.md"], text=True)
    except Exception as e:  # pragma: no cover
        print("could not read pinned README:", e)

bad = []
if readme_text is not None:
    R = norm(readme_text)
    for grp in ("claims", "hypotheses", "verdict_nodes", "commitments", "residue"):
        for c in d[grp]:
            for part in [x.strip() for x in c["sentence"].split(" ... ")]:
                if norm(part) not in R:
                    bad.append((c["id"], part[:80]))

out = []
w = out.append
w("# Claim inventory — README of semi-formal-document-analysis\n")
w(f"Pinned: `{d['pin']['commit']}` ({d['pin']['commit_date']}), file `{d['pin']['file']}`.\n")
w("Generated from `inventory.json` by `render.py`; the JSON is the source of truth.\n")
w("## Dimension vocabulary\n")
for k, v in d["dimension_vocabulary"].items():
    w(f"- **{k}** — {v}")
w("\n## Event predicates (for hypotheses)\n")
for k, v in d["event_predicates"].items():
    w(f"- `{k}` — {v}")
w("\n## Quantitative / checkable claims\n")
for c in d["claims"]:
    w(f"### {c['id']}\n")
    w("> " + c["sentence"].replace("\n", "\n> ") + "\n")
    w("**Values:** `" + json.dumps(c["values"], ensure_ascii=False) + "`\n")
    w("**Dimensions:**")
    for k, v in c["dimensions"].items():
        w(f"- {k}: {v}")
    if c.get("note"):
        w(f"\n*Note:* {c['note']}")
    w("")
w("## Prose-claim hypotheses (round-trip for owner confirmation)\n")
w("Each hypothesis has: the README words; my English reading (in); the rule; the rule rendered back to English (out). Owner confirms in == out.\n")
for h in d["hypotheses"]:
    w(f"### {h['id']}\n")
    w("> " + h["sentence"] + "\n")
    w(f"- **English (in):** {h['english_in']}")
    w(f"- **Rule:** `{h['rule']}`")
    w(f"- **English (out):** {h['english_out']}")
    w(f"- **Declared dimensions translators must carry:** {'; '.join(h['declared_dimensions'])}")
    w(f"- **Scope:** {h['scope']}")
    w("")
w("## Verdict nodes (named needs and candidate providers)\n")
w("A verdict verifies exactly when all its needs resolve to providers that verify. A need with no provider is loose language and is printed by name in results.\n")
for v in d["verdict_nodes"]:
    w(f"### {v['id']}\n")
    w("> " + v["sentence"] + "\n")
    w("- **Needs:** " + "; ".join(v["needs"]))
    w("- **Candidate providers:** " + (", ".join(v["providers"]) if v["providers"] else "**none — dangling**"))
    if v.get("note"):
        w(f"- *Note:* {v['note']}")
    w("")
w("## Author commitments (typed; declare no needs)\n")
for c in d["commitments"]:
    w(f"- **{c['id']}** — > {c['sentence']}")
w("\n## Evaluative residue (out of scope, listed verbatim)\n")
for r in d["residue"]:
    line = f"- **{r['id']}** — > {r['sentence']}"
    if r.get("note"):
        line += f"  \n  *{r['note']}*"
    w(line)
w("")
w("## Verbatim check\n")
if readme_text is None:
    w("Pinned README not available at render time; quotes not checked.")
elif bad:
    w("**FAILED** — non-verbatim quotes: " + ", ".join(f"{i} ({s}...)" for i, s in bad))
else:
    n = sum(len(d[g]) for g in ("claims", "hypotheses", "verdict_nodes", "commitments", "residue"))
    w(f"All {n} quoted sentences are verbatim substrings of the pinned README.")

open(os.path.join(HERE, "inventory.md"), "w").write("\n".join(out) + "\n")
print("rendered inventory.md;", "non-verbatim:", bad)
sys.exit(1 if bad else 0)
