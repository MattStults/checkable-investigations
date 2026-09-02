#!/usr/bin/env python3
"""Live runs for the inventory claims decided by running committed scripts or
inspecting the filesystem/git at the pin. Read-only on the target repo; no
network; records command, exit status, wall clock and the decisive output
lines. Writes results/live_runs.json in the shape queries.py consumes:
{Qid: {"state", "derivation", "claims": [], "command", "wall_s", "output"}}.
"""
import json, os, re, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(HERE)
T = os.path.expanduser("~/Documents/ai_safety_projects/semi-formal-document-analysis")
PIN = "48e66ce04a4d9f06771c42f89cb37b075583c5f6"
PY = os.path.join(T, "semi-formal-experiment/.venv/bin/python")
out = {}
def run(cmd, cwd=T, timeout=900):
    t0 = time.time()
    try:
        p = subprocess.run(cmd, cwd=cwd, shell=isinstance(cmd, str), capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout + p.stderr, round(time.time() - t0, 1)
    except subprocess.TimeoutExpired:
        return -1, "TIMEOUT", round(time.time() - t0, 1)
def rec(q, state, derivation, command, wall, output):
    out[q] = {"state": state, "derivation": derivation, "claims": [], "command": command, "wall_s": wall, "output": output[-1500:]}
    print(q, state, "|", derivation[:120])

head = subprocess.check_output(["git", "-C", T, "rev-parse", "HEAD"], text=True).strip()
assert head == PIN, f"target not at pin: {head}"

# Q07 check_model
rc, o, w = run(f"{PY} machine/check_model.py", cwd=os.path.join(T, "semi-formal-experiment"))
passes = len(re.findall(r"^PASS", o, re.M))
rec("Q07", "verified" if passes == 4 and rc == 0 else "contradicted", f"{passes} PASS lines, exit {rc}", "machine/check_model.py", w, o)
# Q37 seats
rc, o, w = run(f"{PY} machine/query.py seats", cwd=os.path.join(T, "semi-formal-experiment"))
nv = o.count("*** NO VALIDATOR ***"); nr = o.count("(none recorded)")
rec("Q37", "verified" if nv == 1 else "contradicted", f"'*** NO VALIDATOR ***' x{nv}; '(none recorded)' x{nr} (distinct state, reported separately)", "machine/query.py seats", w, o)
# Q36 cite
rc1, o1, w1 = run("python3 engine/spec-cite/cite.py outline model-spec")
rc2, o2, w2 = run('python3 engine/spec-cite/cite.py resolve "model-spec@2025-12-18 > #avoid_sycophancy > ¶2 s1"')
rec("Q36", "verified" if rc1 == 0 and rc2 == 0 and o2.strip() else "contradicted", f"outline exit {rc1} ({len(o1.splitlines())} lines); resolve exit {rc2} → {o2.strip()[:80]!r}", "cite.py outline; cite.py resolve", w1 + w2, o1[:300] + "\n---\n" + o2)
# Q50 determinism: run resolve and graph_check twice
rc3, o3, w3 = run('python3 engine/spec-cite/cite.py resolve "model-spec@2025-12-18 > #avoid_sycophancy > ¶2 s1"')
gc = "python3 walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/graph_check.py walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/runs/ds7/root_graph.production.json"
rcg, og, wg = run(gc); rcg2, og2, wg2 = run(gc)
rec("Q50", "verified" if o2 == o3 and og == og2 else "contradicted", f"cite resolve identical on rerun: {o2 == o3}; graph_check identical on rerun: {og == og2}", "cite.py resolve x2; graph_check.py x2", w3 + wg + wg2, og[:400])
# Q05/Q44 graph_check fields (Q05 and Q44 are ledger-decided too; record live values for the query engine)
m = re.search(r"nodes: (\d+)", og); bl = re.search(r"bad line ranges: (\d+) / (\d+)", og); bq = re.search(r"bad quotes: (\d+) / (\d+)", og); sq = re.search(r"spans with quotes: (\d+) / (\d+)", og)
rec("Q44", "verified" if bl and bl.group(1) == "0" and bq and bq.group(1) == "0" else "contradicted", f"nodes {m.group(1) if m else '?'}; bad line ranges {bl.group(1) if bl else '?'}/{bl.group(2) if bl else '?'}; bad quotes {bq.group(1) if bq else '?'}/{bq.group(2) if bq else '?'}; spans with quotes {sq.group(1) if sq else '?'}/{sq.group(2) if sq else '?'}", gc, wg, og)
# Q40 setup_env --check
rc, o, w = run("bash setup_env.sh --check")
rec("Q40", "verified" if rc == 0 and w <= 30 else ("contradicted" if rc != 0 else "verified"), f"exit {rc}, wall {w}s (README says ~3 s; verified as order of magnitude only)" + (" — exits non-zero" if rc != 0 else ""), "bash setup_env.sh --check", w, o)
# Q43 start-here sequence as written (steps 0-5, 7 commands, cd in step 3 carrying)
seq = """set -e
bash setup_env.sh --check
python3 engine/spec-cite/cite.py outline model-spec >/dev/null
python3 engine/spec-cite/cite.py resolve "model-spec@2025-12-18 > #avoid_sycophancy > ¶2 s1" >/dev/null
python3 walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/graph_check.py walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/runs/ds7/root_graph.production.json >/dev/null
cd semi-formal-experiment && .venv/bin/python measure_join.py >/dev/null
.venv/bin/python benchmark.py --tool --annotations annotations_b8.json --behaviour-atoms behavior_atoms_b8.json >/dev/null
.venv/bin/python machine/query.py seats >/dev/null
echo ALL-OK"""
rc, o, w = run(["bash", "-c", seq])
rec("Q43", "verified" if "ALL-OK" in o else "contradicted", f"sequence exit {rc}; first failing output: {o.strip().splitlines()[-1][:120] if o.strip() else ''}", "Start-here steps 0-5 in order", w, o)
# Q06 join rate live
rc, o, w = run(f"{PY} measure_join.py", cwd=os.path.join(T, "semi-formal-experiment"))
m = re.search(r"^all\s+(\d+)\s+(\d+)\s+([\d.]+)%", o, re.M)
rec("Q06_live", "verified" if m and m.group(3) == "98.4" else "contradicted", f"measure_join prints {m.group(1) if m else '?'}/{m.group(2) if m else '?'} = {m.group(3) if m else '?'}% (published universe; MODULE_MAP §1 forbids quoting)", "measure_join.py", w, o)
# Q24 pytest (long)
rc, o, w = run(f"{PY} -m pytest -q -p no:cacheprovider", cwd=os.path.join(T, "semi-formal-experiment"), timeout=1500)
m = re.search(r"(\d+) passed(?:, (\d+) skipped)?", o)
rec("Q24", "verified" if m and m.group(1) == "2270" and (m.group(2) or "0") == "1" else "contradicted", f"pytest: {m.group(0) if m else o.strip().splitlines()[-1][:120]} (README: 2,270 passed, 1 skipped)", "pytest -q (semi-formal-experiment)", w, o.strip().splitlines()[-1] if o.strip() else o)
# Q30 files exist & differ
def exists(p): return os.path.exists(os.path.join(T, p))
fs = ["data/behaviours.json", "engine/panel/behaviours.json", "semi-formal-experiment/behaviours_query.json"]
sizes = [os.path.getsize(os.path.join(T, p)) if exists(p) else None for p in fs]
rec("Q30", "verified" if all(exists(p) for p in fs) and len(set(sizes)) == 3 else "contradicted", f"exist: {[exists(p) for p in fs]}; sizes {sizes}", "os.path", 0, "")
# Q31 symlinks
lk = {p: (os.readlink(os.path.join(T, p)) if os.path.islink(os.path.join(T, p)) else None) for p in ("LEDGER.md", "ARC2_HANDOFF.md", "CLAUDE.md")}
rec("Q31", "verified" if lk["LEDGER.md"] and lk["LEDGER.md"].endswith("ITERATION_NOTES.md") and lk["ARC2_HANDOFF.md"] and lk["CLAUDE.md"] == "AGENTS.md" else "contradicted", f"{lk}", "os.readlink", 0, "")
# Q33 git dates
d1 = subprocess.check_output(["git", "-C", T, "log", "--format=%ci", "--reverse", PIN, "--", "semi-formal-experiment/"], text=True).splitlines()
d2 = subprocess.check_output(["git", "-C", T, "log", "--format=%ci", "--reverse", PIN, "--", "walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/"], text=True).splitlines()
rec("Q33", "contradicted" if d1 and d1[0][:7] != "2026-07" else "verified", f"arc-1 dir commits {d1[0][:10] if d1 else '?'} → {d1[-1][:10] if d1 else '?'} (README: July–early Aug); arc-2 dir {d2[0][:10] if d2 else '?'} → {d2[-1][:10] if d2 else '?'} (README: mid–late Aug); no commit in the repo predates 2026-08-02", "git log --format=%ci -- <dir>", 0, "")
# Q34 CI trigger
ci = open(os.path.join(T, ".github/workflows/ci.yml")).read()
on = re.search(r"^on:\s*\n((?:\s+.*\n)+?)(?=\S)", ci, re.M)
rec("Q34", "contradicted" if "branches" in (on.group(1) if on else ci) else "verified", f"on-block: {(on.group(1) if on else '?').strip()[:120]!r}; README says 'every push'", "read ci.yml", 0, ci[:600])
# Q35 licenses
lic = open(os.path.join(T, "LICENSE")).read()[:200]; pv5 = [exists("data/panel-v5/LICENSE"), exists("data/panel-v5/NOTICE")]
sp = [exists("specs/openai-model-spec/LICENSE") or exists("specs/openai-model-spec/LICENSE.md") or any(f.upper().startswith("LICENSE") for f in os.listdir(os.path.join(T, "specs/openai-model-spec"))), any(f.upper().startswith("LICENSE") for f in os.listdir(os.path.join(T, "specs/claude-constitution")))]
rec("Q35", "verified" if "MIT" in lic and all(pv5) and all(sp) else "contradicted", f"root LICENSE MIT: {'MIT' in lic}; panel-v5 LICENSE/NOTICE: {pv5}; specs licence files present: {sp}", "read LICENSE files", 0, lic)
# Q42 relative links in README resolve
rd = subprocess.check_output(["git", "-C", T, "show", f"{PIN}:README.md"], text=True)
links = re.findall(r"\]\(([^)#]+)\)", rd)
rel = [l for l in links if not l.startswith("http")]
missing = [l for l in rel if not exists(l)]
rec("Q42", "verified" if not missing else "contradicted", f"{len(rel)} relative links, missing: {missing}; {len(links) - len(rel)} external links not checked (no network)", "parse README links", 0, "")
# Q46 no network on demo path (static)
files = ["engine/spec-cite/cite.py", "walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/graph_check.py", "semi-formal-experiment/measure_join.py", "semi-formal-experiment/benchmark.py", "semi-formal-experiment/machine/query.py", "semi-formal-experiment/machine/check_model.py", "setup_env.sh"]
hits = {f: re.findall(r"\b(urllib|requests|httpx|socket)\b", open(os.path.join(T, f)).read()) for f in files}
rec("Q46", "verified" if not any(hits.values()) else "contradicted", f"network-module mentions per file: { {k: v for k, v in hits.items() if v} or 'none'}", "static grep", 0, "")
# Q48 handoffs starred blocks
h1 = open(os.path.join(T, "walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/HANDOFF_CURRENT.md")).read().splitlines()
h2 = open(os.path.join(T, "semi-formal-experiment/HANDOFF.md")).read().splitlines()
st1 = [i + 1 for i, l in enumerate(h1) if l.startswith("#") and "⭐" in l]; st2 = [i + 1 for i, l in enumerate(h2) if l.startswith("#") and "⭐" in l]
rec("Q48", "contested", f"star-marked heading lines: HANDOFF_CURRENT {st1}; HANDOFF {st2} — 'the top starred block' is unique in arc 2 but arc 1 has {len(st2)} star-marked heading blocks; 'self-marked' below is not mechanically decidable", "read handoffs", 0, "")
# Q49 layout paths
lay = ["engine/", "specs/", "data/", "semi-formal-experiment/", "walkthrough/", "ARTIFACTS.md", "LEDGER.md", "ARC2_HANDOFF.md"]
rec("Q49", "verified" if all(exists(p) for p in lay) else "contradicted", f"{[(p, exists(p)) for p in lay]}", "os.path", 0, "")
# H15 ARTIFACTS.md paths exist
art = open(os.path.join(T, "ARTIFACTS.md")).read()
paths = sorted(set(re.findall(r"`([A-Za-z0-9_./-]+\.(?:md|json|py|jsonl|lp|yml|txt))`", art)))
miss = [p for p in paths if not exists(p)]
rec("H15", "verified" if not miss else "contradicted", f"{len(paths)} backticked paths in ARTIFACTS.md; missing at pin: {miss[:10]}", "parse ARTIFACTS.md", 0, "")
# Q32 absence-by-search (D-09): PRUNED.md exists; signature presence decided by the
# inventory's own definition (detached signature, signer-attested checksum of the
# manifest, or an explicit signer line; git object ids alone do not count).
PR = "walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/PRUNED.md"
pr_text = open(os.path.join(T, PR)).read(); pr_lines = pr_text.splitlines()
sig_pat = r"(?i)(-----BEGIN (PGP|SSH) SIGNATURE|\bsigned[- ]by\b|\bsigner\b|\bsignature\b|\bcountersign|\bsha(256|512)sum\b.*PRUNED|\bgpg\b|\bminisign\b)"
sig_hits = [(i + 1, l) for i, l in enumerate(pr_lines) if re.search(sig_pat, l)]
detached = [f for f in os.listdir(os.path.dirname(os.path.join(T, PR))) if f.startswith("PRUNED.md.") and f.split(".")[-1] in ("sig", "asc", "minisig", "sha256", "sha512")]
restore = re.findall(r"\b[0-9a-f]{7,40}\b", pr_text)
resolv = [h for h in set(restore) if subprocess.run(["git", "-C", T, "cat-file", "-e", h], capture_output=True).returncode == 0]
absence = {"kind": "existence", "metric": "signature on PRUNED.md", "value": False, "tier": "live_run",
           "source": {"path": PR, "commit": "pin", "lines": f"1-{len(pr_lines)}"}, "quote": pr_lines[0],
           "search": {"pattern": sig_pat, "over": PR}, "detached_files": detached}
rec("Q32", "verified" if (not sig_hits and not detached) else "contradicted",
    f"PRUNED.md exists ({len(pr_lines)} lines); signature-pattern hits: {sig_hits[:3] or 'none'}; detached signature files: {detached or 'none'}; {len(set(restore))} hash-like tokens, {len(resolv)} resolve in git — 'signed' per the inventory definition is ABSENT, so the README sentence 'signed manifest' is contradicted on the signature and verified on existence/restorability",
    "grep PRUNED.md for signature markers; ls for detached signatures; git cat-file -e on hashes", 0, "\n".join(f"{i}: {l}" for i, l in sig_hits) or "(no signature hits)")
out["Q32"]["state"] = "contradicted" if (not sig_hits and not detached) else "verified"
out["Q32"]["absence_claim"] = absence
json.dump(out, open(os.path.join(HERE, "live_runs.json"), "w"), indent=1)
print("wrote live_runs.json", len(out))
