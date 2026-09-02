#!/usr/bin/env python3
"""Render glossary.json to glossary.md and verify every path:line citation
points at an existing file in the target repo at the pin (line count checked
where a line number is given). Exit 1 on any bad citation."""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "glossary.json")))
REPO = os.path.expanduser("~/Documents/ai_safety_projects/semi-formal-document-analysis")
PIN = "48e66ce04a4d9f06771c42f89cb37b075583c5f6"
P = d["paths"]

def expand(c):
    for k, v in P.items():
        if c.startswith(k + "/"):
            return v + c[len(k) + 1:]
    return c

_cache = {}
def nlines(path):
    if path not in _cache:
        try:
            out = subprocess.check_output(["git", "-C", REPO, "show", f"{PIN}:{path}"], stderr=subprocess.DEVNULL)
            _cache[path] = out.count(b"\n") + 1
        except subprocess.CalledProcessError:
            _cache[path] = None
    return _cache[path]

bad = []
def check(c):
    if c.startswith("sources/"):
        return os.path.exists(os.path.join(HERE, c.split(" ")[0]))
    m = re.match(r"^([^:\s]+)(?::(\d+)(?:-(\d+))?)?", c)
    if not m:
        return False
    path = expand(m.group(1))
    n = nlines(path)
    if n is None:
        return False
    if m.group(2):
        hi = int(m.group(3) or m.group(2))
        return hi <= n
    return True

out = []
w = out.append
w("# Glossary — definitions and authoritative-artifact map\n")
w(d["_about"] + "\n")
w("Path prefixes: " + "; ".join(f"`{k}` = `{v}`" for k, v in P.items()) + "\n")
w("## Tiers (closed enum)\n")
for k, v in d["tiers"].items():
    if not k.startswith("_"):
        w(f"- **{k}** — {v}")
if "tier_procedure" in d:
    w("\n### Tier decision procedure (apply per value, in order, stop at first match)\n")
    for i, step in enumerate(d["tier_procedure"], 1):
        w(f"{i}. {step}")
w("\n## Entries\n")
for e in d["entries"]:
    w(f"### {e['term']}  (arc {e['arc']})\n")
    w(f"**Definition.** {e['definition']}\n")
    if e.get("authoritative"):
        w(f"**Authoritative artifact.** {e['authoritative']}\n")
    if e.get("denominator"):
        w(f"**Denominator / population.** {e['denominator']}\n")
    if e.get("variants"):
        v = e["variants"]
        w("**Variants.** " + (", ".join(v) if isinstance(v, list) else v) + "\n")
    if e.get("conflicts"):
        w("**Conflicts in the record (unresolved).**")
        for c in e["conflicts"]:
            w(f"- {c}")
        w("")
    if e.get("hazards"):
        w("**Hazards for translators.**")
        for h in e["hazards"]:
            w(f"- {h}")
        w("")
    w("**Cites.** " + "; ".join(f"`{c}`" for c in e["cite"]) + "\n")
    for c in e["cite"]:
        if not check(c):
            bad.append((e["term"], c))
w("## Authoritative artifact map\n")
for k, v in d["authoritative_artifact_map"].items():
    w(f"- **{k}** — {v}")
w("\n## Record conventions\n")
for k, v in d["conventions"].items():
    if not k.startswith("_"):
        if isinstance(v, dict):
            w(f"### {k}\n")
            for kk, vv in v.items():
                w(f"- **{kk}** — {vv}")
            w("")
        else:
            w(f"- **{k}** — {v}")
if d.get("amendments"):
    w("\n## Amendments (post-freeze, numbered, logged in results/intervention_log.md)\n")
    for a_ in d["amendments"]:
        w(f"- **{a_['id']}** ({a_['date']}, {a_['logged_as']}) — {a_['change']} Cites: " + "; ".join(f"`{c}`" for c in a_["cite"]))
        for c in a_["cite"]:
            if not check(c):
                bad.append((a_["id"], c))
w("\n## Citation check\n")
w("All entry citations resolve to an in-range line at the pin (line-bound check only; support is not machine-verified.)" if not bad else "**FAILED**: " + "; ".join(f"{t}: {c}" for t, c in bad))
open(os.path.join(HERE, "glossary.md"), "w").write("\n".join(out) + "\n")
print("rendered glossary.md; bad citations:", bad)
sys.exit(1 if bad else 0)
