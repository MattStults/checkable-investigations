# Baseline adversarial review — REPORT

**Start (wall clock):** 2026-09-02 13:13:50 PDT
**End (wall clock):** 2026-09-02 14:41:00 PDT
**Total time:** 1 h 27 min

Repository under test: `~/Documents/ai_safety_projects/semi-formal-document-analysis`,
verified at the pinned commit `48e66ce04a4d9f06771c42f89cb37b075583c5f6`
("README: publication links and CI badge filled", 2026-09-01 17:44:18 -0700),
working tree clean (`git status --porcelain` empty).

## Environment note (bears on every live_run claim)

The working tree carries `semi-formal-experiment/.venv`, but it is a symlink
farm pointing **outside the repository**:

```
semi-formal-experiment/.venv/bin/python3 ->
  /Users/mattstults/Documents/ai_safety_projects/introspection_leakage/.venv/bin/python3
semi-formal-experiment/.venv/pyvenv.cfg:  version = 3.10.6
$ semi-formal-experiment/.venv/bin/python -V
Python 3.12.14
```

That out-of-repo interpreter has since moved to 3.12, so the venv's own
`lib/python3.10/site-packages` (92 packages; pytest/clingo/pydantic all present)
is invisible to it and every `.venv/bin/python` invocation fails with
`No module named …`. `.venv*/` is `.gitignore`d, so this is **machine state, not
part of the record**. Where the README says `.venv/bin/python`, I ran
`/usr/local/bin/python3.10` with
`PYTHONPATH=<repo>/semi-formal-experiment/.venv/lib/python3.10/site-packages`,
which reconstitutes exactly the interpreter+package set `pyvenv.cfg` and
`requirements.txt` describe. Every live-run result below is from that
reconstruction; the as-written failure is reported separately where it matters
(Q40, Q43).

---

## Quantitative / checkable claims

### Q01
State: verified
Evidence: `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/HANDOFF_CURRENT.md`:106-108
Quote: "CRITERION STANDING (in-sample, all-truth): caution 0.941, harm 0.953, help 0.960 under match-or-adjudicated-defensible; raw match 0.81-0.85; the human-panelist baseline 71%. NOT yet certified — that is round-4's job."
Reason: 0.941–0.960 over the three dev behaviours is exactly the README's 0.94–0.96, at the claimed metric and tier (match-or-adjudicated-defensible, in-sample, all-truth). **Supersession, reported as required:** the round-4 certification cells for the same three behaviours are far lower on both columns — `ROUND4_DEV_TABLE.json` gives raw engaged precision 0.625 / 0.8235 / 0.675 and *headline* (match-or-adjudicated-defensible) 0.725 / 0.8824 / 0.75. Denominators are **not recoverable**: no artifact names the per-behaviour engaged-set size these three numbers were computed over, and no committed script regenerates them.

### Q02
State: contradicted
Evidence: `semi-formal-experiment/REPO_TRAPS.md`:74-76; `semi-formal-experiment/HANDOFF.md`:865; `walkthrough/…/behavior_pilot/GENERALIZATION_PREREG_DRAFT.md`:80-84
Quote: "## 6. No inter-judge kappa exists in this repo … **No `.py` computes one** (verified)." / "Inter-judge Jaccard is 0.16–0.62 and gold is the intersection of two judges." / "(A former anchor — \"the human-panelist baseline 71%\" — is STRUCK 2026-08-21: no artifact establishes it and its presumed source does not recognize it…)"
Reason: The README says 0.94–0.96 is "comparable to the panel's own internal agreement." The record's only admissible panel-agreement statistic is arc-1's inter-judge Jaccard of **0.16–0.62** — not comparable. The one figure that could read as a panel baseline (71%) is explicitly **struck** as sourceless (also `HANDOFF_CURRENT.md`:210: "currently has NO source artifact; it must be sourced or struck before it appears in any writeup"), and is not comparable either. Excluded per the claim's own dimensions: seat self-agreement, mint stability (0.98), F4/F5 split rates.

### Q03
State: verified
Evidence: `walkthrough/…/behavior_pilot/ROUND4_DEV_TABLE.json`; `round4_helpfulness_scored_final_raw.json`; `round4_harm_scored_raw.json`; `round4_caution_scored_raw.json`
Quote: "ROUND-4 DEV-BEHAVIOR TABLE COMPLETE (2026-08-24, recovered lineage venue, E4/registered bands, one-pass defensibility per amendment 1). Raw = strict panel-majority truth; headline = match-or-adjudicated-defensible. Both publish."
Reason: All three tuned behaviours have completed raw-match certification cells. **Per-behaviour raw outcome (record-supplied, README-silent):** helpfulness `"raw_verdict": "F1 (prec below floor); decl above band"` (0.625 vs band 0.71-0.87 — falsifier FIRED); harm-avoidance `"prec IN BAND (closed population n=17)"` (0.8235, band 0.81-0.97); avoiding-over-and-under-caution `"F1 by ONE node (27/40 vs floor 28)"` (0.675, band 0.69-0.85 — falsifier FIRED). Two of three raw cells fired their falsifier.

### Q04
State: contradicted
Evidence: `walkthrough/…/behavior_pilot/ROUND4_PREREG.md`:104-113 (registration) vs `ROUND4_DEV_TABLE.json` and `ROUND4_HELP_CANARY_RESULT.json` (the run)
Quote: registration — "1. DEFENSIBILITY PASS (project owner's decision, 2026-08-24): round-4 misses receive a pre-declared ONE-PASS blind Fable defensibility adjudication … HEADLINE metric = match-or-adjudicated-defensible; RAW match is reported alongside in the same table, always." / run — `ROUND4_HELP_CANARY_RESULT.json`: "ROUND-4 helpfulness canary COMPLETE (recovered lineage venue, E4 bands, F5 full-panel escalation, **one-pass defensibility per amendment 1**)", `"headline_match_or_defensible": {"engaged_precision": 0.725, "decline_correctness": 0.975}`
Reason: The README says the registered match-or-defensible pass never ran. The record holds exactly one such registration (ROUND4_PREREG.md pre-signature amendment 1) and **it ran to completion on all three dev behaviours**, citing the registration by amendment id and scoring against the registered bands (`"headline_verdict": "prec IN BAND; decl above"`). Claimed `run_exists: false`; record: run exists, headline cells 0.725 / 0.8824 / 0.75 (precision), 0.975 / 1.0 / 0.95 (decline). Only one registration exists, so the CONTESTED branch of the claim's own rule does not fire.

### Q05
State: verified
Evidence: live run — `python3 walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/graph_check.py walkthrough/…/runs/ds7/root_graph.production.json` (exit 0, 0.29 s wall); also a direct `json.load(...)["nodes"]` length
Quote: "nodes: 773   uncovered entries: 733"
Reason: Both the committed checker and a direct read of the JSON give exactly 773 nodes in the graph_v2 production root graph at the pin.

### Q06
State: contested
Evidence: live run — `cd semi-formal-experiment && .venv/bin/python measure_join.py` (10.06 s, exit 0) vs `semi-formal-experiment/MODULE_MAP.md`:54
Quote: run — "all | 849 | 863 | 98.4%"; anti-rule — "⚠️ the recall ceiling. **Do not quote 849/863** — that is the published-universe figure, and the published universe deleted every passage the panel scored 0. Re-run it; never cite the number from this table."
Reason: The join rate reproduces exactly (849/863 = 98.4%) and 14 unmatched passages print with behaviour, score and a text prefix (identified by opening text, not by clause/node id — "printed by name" is loose). But **the record marks this exact figure do-not-cite**: it is the *published* universe (863 rows, score-0 passages already deleted), while the README's own arc-1 headline three paragraphs later runs on the *true* 589-passage universe. The claim's `anti_rule` dimension asked for exactly this, and it fires.

### Q07
State: verified
Evidence: live run — `cd semi-formal-experiment && .venv/bin/python machine/check_model.py` (exit 0)
Quote: "PASS (a) SOURCE CHECK / PASS (b) DIFFERENTIAL CHECK vs cycle.py (282 comparisons) / PASS (c) KNOWN-ANSWER SET / PASS (*) ACCEPTANCE TEST"
Reason: Four checks, all four PASS, exit 0. (It also prints "60 contradiction(s) reported by rules.lp" — an output of the model, not a check failure.)

### Q08
State: verified
Evidence: `semi-formal-experiment/constitution_clauses.json` (`len(d["clauses"]) == 616`); `semi-formal-experiment/segmentation_summary.md`:5
Quote: "**Total clauses: 616**"
Reason: The inventory the summary names as the pilot's (`constitution_clauses.json`) holds exactly 616 clauses; `MODULE_MAP.md`:227 corroborates ("616 clauses, same schema, loads today"). No later inventory in the repo differs.

### Q09
State: verified
Evidence: `semi-formal-experiment/rules.lp` — `grep -cE "^active\(" rules.lp` = 16, 16 distinct norm ids; `semi-formal-experiment/adversarial_review_1.md`:39
Quote: "**2. \"15-rule fragment\" is actually 16 rules** (16 norm IDs / source facts). Fix count or state convention."
Reason: The arc-1 ASP fragment ("Prototype: solver-based conflict enumeration over the 'faithfulness to the user' fragment of Claude's Constitution") declares 16 `active(NormID, …)` rules: h1/h2/h4/h5/h7, g1_immediate/g1_reliance/g3/g5/g6, p1/p1b/p2/p3/p4/p4b. The record's own correction of an earlier "15-rule" claim to 16 is the supersession requested, and the README carries the corrected count.

### Q10
State: verified
Evidence: live run — `benchmark.py --tool --annotations annotations_b8.json --behaviour-atoms behavior_atoms_b8.json`, §"Judged universe — reconstruction provenance"
Quote: "1. **THE UNIVERSE.** The panel graded EVERY passage of the spec in one prompt: 589 for the model spec, 374 for the constitution."
Reason: 589 is the **TRUE** (reconstructed) Model Spec universe — every passage the judges graded. Universe recorded as required. The *published* file holds only 377/333/153 of those 589 per behaviour (863 rows total), so 589 cannot be read off `data/behaviours.json`; it is the reconstruction the benchmark computes and prints, and the README names it correctly.

### Q11
State: verified
Evidence: same as Q05 — live `graph_check.py` on `runs/ds7/root_graph.production.json`
Quote: "nodes: 773   uncovered entries: 733"
Reason: Identical metric, snapshot, and scope to Q05; the README's two uses of 773 are consistent with each other and with the artifact.

### Q12
State: verified
Evidence: live run — `benchmark.py --tool …`, disclosure note 5 (also `semi-formal-experiment/benchmark.py`:1701)
Quote: "so every thresholded number here is a HINDSIGHT-THRESHOLD number and the in-sample mean MCC (+0.274 published / +0.320 true) is a CEILING, not a result."
Reason: +0.320 on the TRUE 589-passage universe, in-sample (threshold fitted on these same three behaviours) — matching "+0.32 in-sample" at the universe the README's own sentence names. Universe recorded: **true**. Adversarial note: the artifact labels this figure "a CEILING, not a result", which the README does not carry over; the published-universe counterpart is +0.274.

### Q13
State: verified
Evidence: live run — `benchmark.py --tool …`, "Universe delta" mean row; `semi-formal-experiment/HANDOFF.md`:43-44
Quote: benchmark — "| **mean** | | **+0.278** | +0.219 | +0.059 | **+0.555** | …"; HANDOFF — "label-free sits at +0.278, best compliant config +0.316, judge mean +0.555"
Reason: +0.278 is the tool's mean MCC on the TRUE universe at the label-free (Otsu-derived) operating point; per behaviour +0.201 / +0.350 / +0.283. Universe: **true**; threshold rule: **label_free**. Published-universe counterpart +0.219.

### Q14
State: verified
Evidence: live run — `benchmark.py --tool …`, "Universe delta" and "TRUE universe — the headline" tables
Quote: "The judge aggregate quoted is the MEAN LOO, not the best single judge — it is the only judge aggregate computed over the same three golds the tool is scored on." with judge MCC true +0.571 / +0.615 / +0.481, mean **+0.555**
Reason: Denominator recovered: three behaviours × three leave-one-out judge positions = 9 cells; rosters fable/kimi/sol (helpfulness), kimi/opus/sol (harm), fable/kimi-k2/sol (caution). Universe: **true** (published counterpart +0.394).

### Q15
State: verified
Evidence: live run — `benchmark.py --tool …`, §"Threshold-free — AUC, and the tool at each judge's own operating point"
Quote: "**judge wins 9 / 9 cells at its own operating point.**"
Reason: Nine rows, one per behaviour×judge, each holding the tool to the judge's own false-positive rate; the winner column reads **judge** in all nine. Universe: **true**. This is the one table in the report not selected on these behaviours.

### Q16
State: verified
Evidence: `walkthrough/…/behavior_pilot/ITERATION_NOTES.md`:352 (entry 0014); components at :271-274 (entry 0010)
Quote: "Attempt series: 0.40 transfer -> 0.70 -> 0.55 -> 0.85/0.895."
Reason: Behaviour = **how-to-approach-tradeoffs** (entry 0001). Per-element tiers, as the dimension demands: attempt-1 = 0.40 frozen transfer, single-wave truth; attempt-2 = 0.70 **panel-tier** (raw 0.75); attempt-3 = 0.55 **panel-tier** (raw 0.40); attempt-4 = 0.85 at the **certified-Opus venue**, adjusted to 0.895 after the dispute-class quarantine. Denominators: attempts 1–3 are n=40 draws with n=20 engaged (entry 0009: "n=20 draws carry ±~0.2"); attempt-4's move gate is 10/14 extension nodes, 10/12 post-quarantine. The series is tier-mixed and the README does not say so; the record does. Supersession: the README quotes 0.85, not the record's adjusted 0.895.

### Q17
State: verified
Evidence: `walkthrough/…/behavior_pilot/ITERATION_NOTES.md`:280-281 (entry 0010)
Quote: "THE HONEST HEADLINE IS RECALL, NOT PRECISION: 23/40 pooled declined nodes are panel-relevant."
Reason: 23/40 = 0.575, panel tier, same behaviour as Q16. Snapshot = **pooled** over both frozen draws (attempts 2 and 3), which the README's flat "23 of 40 declined passages" does not disclose. The record's unit is **nodes**; the README says "passages" — a glossary substitution, not an error of value.

### Q18
State: verified
Evidence: commit `bf0d4978103fe7eeb8b584d9a677ab8b13f92307` (2026-08-25 10:04:21 -0700)
Quote: "0041 withdrawn: integration census fails adversarial review (P1/P2 UNSUPPORTED) — CoVe re-derivations confirm the decisive findings (random-partition null dominates the pass condition 299/300; …)"
Reason: The commit exists at the stated short hash, withdraws exactly the separability/integration census (ledger entry 0041, "INTEGRATION TEST PASSES"), and touches `ITERATION_NOTES.md` (+34), `HANDOFF_CURRENT.md`, and the new `RETRANS_REVIEW_DISPOSITION.md`.

### Q19
State: verified
Evidence: `walkthrough/…/behavior_pilot/RETRANS_REVIEW_DISPOSITION.md`:10-16 (tier: CoVe, driver-run, deterministic, $0)
Quote: "F1 NULL MODEL: a content-free random 4-bucket-per-family partition of the leaf vocabulary achieves separability 1.00 in 299/300 seeded trials with reuse trivially 1.00 — dominating the real mid lattice (1.00 sep / 0.57-0.58 reuse) on the census's own pass condition. CONFIRMED by re-derivation."
Reason: 299/300 exactly, against the census's registered pass condition; corroborated verbatim in ledger 0042 and in `bf0d4978`'s commit message. Tier recorded: **cove** (reviewer finding, independently re-derived by the driver).

### Q20
State: verified
Evidence: `walkthrough/…/behavior_pilot/RETRANS_REVIEW_DISPOSITION.md`:17-22 and :45-49
Quote: "F4 RELEVANCE PREDICTION: 1-NN over mid-level signatures (Jaccard) predicts panel relevance at 0.72 (tradeoffs, base 0.60) and 0.70 (user-autonomy, base 0.59). CONFIRMED by re-derivation — at or near majority-class base rate." … "the representation does not predict relevance above base rate."
Reason: Values supplied: 0.72 vs base 0.60 and 0.70 vs base 0.59, prediction set n=39 nodes per behaviour. The record's own corrected verdict states flatly that the representation "does not predict relevance above base rate", so the README's wording is the record's. **Adversarial caveat:** the raw numbers are nominally +0.12/+0.11 above base; the equality reading rests on non-significance, quantified only later — ledger 0043 / commit `365d68b3`: "my CoVe found those numbers are p~0.15 vs baseline, i.e. not even significant."

### Q21
State: verified
Evidence: commit `365d68b3f550379153b13b89c571672a92e5e396` (2026-08-25 10:23:55 -0700)
Quote: "L1/L2 withdrawn: the licensing experiments fail their own adversarial review (DOES-NOT-LICENSE, accepted after CoVe)."
Reason: The commit exists at the stated short hash, carries the DOES-NOT-LICENSE verdict, and adds `L1L2_ADVERSARIAL_REVIEW.md` (+372) and `L1L2_REVIEW_DISPOSITION.md` (+96).

### Q22
State: verified
Evidence: `walkthrough/…/behavior_pilot/ITERATION_NOTES.md`:872-880 (entry 0043); commit message of `365d68b3`
Quote: "The four decisive defects: (1) **L1's** relevance clause is met on a point-estimate reading by the very numbers 0042 dismissed as base rate — and my CoVe found those numbers are p~0.15 vs baseline … a pass condition that cannot fail …; (2) **L2** has no null and its coverage clause is elastic"
Reason: Which-is-which recovered: **L1** is the bar already met by noise-level numbers; **L2** is the one with no null. `L1L2_ADVERSARIAL_REVIEW.md`:150 corroborates ("### F11. L2 ships with no null — in direct violation of the binding rule adopted in the same document.").

### Q23
State: verified
Evidence: commit `1143a9213703e9b44c0ac90daefea1a58331f60f` (2026-08-25 08:46:33 -0700); `ITERATION_NOTES.md`:739 (entry 0037)
Quote: commit — "Notes 0037 / erratum #20: Matt's too-tidy-narrative suspicion upheld — endogeneity + closed-vocabulary circularity mean the query-class study's 'no new places' claim is vocabulary-relative, not space-complete"; ledger — "## 0037 — ERRATUM #20: CLOSED-VOCABULARY CIRCULARITY (Matt's suspicion, upheld), 2026-08-25"
Reason: Commit exists at the stated short hash, erratum number is 20, subject is the query-class saturation claim, recorded in the ledger at entry **0037** (the CLAIMS dimension's "ledger entry 0037" matches). The commit touches only `ITERATION_NOTES.md` (+18); it did not amend the handoff.

### Q24
State: verified
Evidence: live run — `cd semi-formal-experiment && <py3.10> -m pytest -q`, 2026-09-02
Quote: "2270 passed, 1 skipped, 14 warnings in 296.08s (0:04:56)"
Reason: Exact match to "2,270 passed, 1 skipped", inside the stated 4-10 min window (4 m 56 s). Denominator 2271 collected. Corroborated at the record's own snapshot by commit `6d01415b`'s message ("semi-formal-experiment 2,270 passed / 1 skipped"). The live run supersedes the stated 2026-08-30 date and agrees with it.

### Q25
State: verified
Evidence: `walkthrough/…/behavior_pilot/ITERATION_NOTES.md`, all `## NNNN — ` headings enumerated programmatically
Quote: "## 0000 — SEED: tacit operational knowledge from the 2026-08-24 sessions" … "## 0043 — L1/L2 THEMSELVES FAIL REVIEW: DOES-NOT-LICENSE, 2026-08-25"
Reason: The set of entry numbers present is exactly {0000…0043} — 44 entries, **gapless**, verified by set equality against `[f"{i:04d}" for i in range(44)]`, not merely by count.

### Q26
State: verified
Evidence: `walkthrough/…/behavior_pilot/ITERATION_NOTES.md`:762-763 (entry 0034); `RETRANS_REVIEW_DISPOSITION.md`:34
Quote: "QUERY-CLASS STUDY: 100-def corpus built (exemplary Opus coordinator run)"; "F5 (both scored behaviours are inside the 100-definition corpus…)"
Reason: The query-class study's input set is a corpus of 100 behaviour definitions, open-coded; ledger 0038 gives "~1.2 handles/definition" over the same 100 and 0034 "9 primary places observed over 100 definitions".

### Q27
State: contested
Evidence: `walkthrough/…/behavior_pilot/RETRANS_REVIEW_DISPOSITION.md`:56-59 and :41-42; `ITERATION_NOTES.md`:790-791 (entry 0038)
Quote: coverage — "two blind seats retranslated **39/39** full spans with the schema and ZERO new coinages (coverage-in-form)"; the 100-denominator figure — "FINAL: **separability 94/100** both seats identically"
Reason: Coverage = 1.0 verifies, but **only over a 39-node sample**, not over the 100 definitions the README's sentence binds it to. The record contains no coverage figure over the 100 definitions; the only 100-denominator number is *separability* 94/100, a different metric. Two artifacts pull the sentence apart, so the referent is contested. Adversarially: the disposition accepts finding F7 — "39-node sample stratified on known-problem nodes; more than half the ontology untested" — so "every sampled span" is true of a sample the record itself calls unrepresentative.

### Q28
State: contradicted
Evidence: `walkthrough/…/behavior_pilot/RETRANS_REVIEW_DISPOSITION.md`:10-16 vs `ITERATION_NOTES.md`:788-790 (0038) and :795-798 (0039)
Quote: null-tested — "F1 NULL MODEL: a content-free random 4-bucket-per-family partition of the leaf vocabulary achieves separability 1.00 in 299/300 seeded trials"; never null-tested — "FINAL: separability 94/100 both seats identically" (0038) and "Defensible numbers: dimension-set separability 0.37-0.40 (definitions) / 0.85 (nodes)" (0039)
Reason: The README says the ontology "failed **every** separability test once a matched random-partition null was run against it." The record documents exactly **one** separability test ever run against a matched-granularity random-partition null — the 0041 integration census, covering leaf and mid levels — and it failed. At least two other separability measurements (0038's 94/100 over definitions; 0039's dimension-set 0.37–0.40 / 0.85) carry **no null at all**. Claimed: 0 of all tests survived. Record: 1 test null-tested, 1 failed, ≥2 never null-tested. The denominator cannot be made to equal "every".

### Q29
State: contradicted
Evidence: git — `bf0d4978`, `365d68b3`, `1143a921`; `git show 1143a921^:…/HANDOFF_CURRENT.md` lines 9-13; `ITERATION_NOTES.md`:768 (entry 0034); `QUERY_CLASS_STUDY_STATUS.json`
Quote: pre-`1143a921` starred block — "(2) QUERY-CLASS BOUND … tripwired twice at full-pattern granularity — choose: coarse bound now / brief v3 / accept-with-noise."; ledger 0034 — "**Halted without publishing a bound.**"; status file — "NO QUERY_CLASS_BOUND.json is published from tripwired data."
Reason: Under the claim's own definition (headline iff the withdrawn claim appeared in a handoff starred block or the README), **two** withdrawals qualify: the separability census (`bf0d4978`, whose message records "HANDOFF headline downgraded") and L1/L2 (`365d68b3`, which edits the starred block). The third README item — the query-class saturation claim (`1143a921`) — was never in a starred block or the README: the record shows it was explicitly *never published as a bound*, `1143a921` touches only `ITERATION_NOTES.md`, and the README itself calls it "bounded", not withdrawn. Nor was it preceded by an adversarial review: entry 0037 records the owner's suspicion "upheld on inspection" by the driver. Claimed 3; record supports 2.

### Q30
State: verified
Evidence: filesystem at pin — `ls -l` and `md5` on the three paths
Quote: `data/behaviours.json` 1,082,124 B md5 `a64f5f9b…`; `engine/panel/behaviours.json` 10,303 B md5 `68fef491…`; `semi-formal-experiment/behaviours_query.json` 1,367 B md5 `59d1c7bc…`
Reason: All three exist at the stated paths and are pairwise distinct in content (three distinct md5s, sizes spanning three orders of magnitude). The warning is accurate.

### Q31
State: verified
Evidence: filesystem at pin — `ls -la LEDGER.md ARC2_HANDOFF.md CLAUDE.md`
Quote: "LEDGER.md -> walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/ITERATION_NOTES.md"; "ARC2_HANDOFF.md -> walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/HANDOFF_CURRENT.md"; "CLAUDE.md -> AGENTS.md"
Reason: All three are real symlinks with the claimed targets, and all three targets exist and resolve.

### Q32
State: contradicted
Evidence: `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/PRUNED.md` (whole file); `git cat-file -t` on sampled object ids; `git log --format='%h %G?'`
Quote: "NOTHING IS LOST: full git history is retained, and each entry pins the exact content by git object id (tree/blob sha at the pre-prune commit). To restore any entry: `git checkout <pre-prune-commit> -- <path>`."
Reason: The file exists at exactly the linked path and its object ids resolve (4/4 sampled: three trees, one blob, all `cat-file -t` clean). But **it is not signed** under the claim's own definition: `grep -in "sign|gpg|sha256|checksum"` over PRUNED.md returns nothing relevant; there is no detached signature, no signer-attested checksum of the manifest, no signer line; and the commits are unsigned (`%G?` = `N` throughout). The claim explicitly rules out content-addressed git object ids as satisfying "signed" — which is all this manifest has. Two further gaps: the restore recipe never resolves `<pre-prune-commit>` (it is `6d01415b^`), and two rows pin nothing at all (`untracked-or-file`).

### Q33
State: contradicted
Evidence: git — `git log --format='%ci' -- semi-formal-experiment/`, `… -- walkthrough/…/behavior_pilot/`, `git log --reverse | head`, `git log --before=2026-08-01`
Quote: repo's first commit — "d9d2369f65a920cdf489f1587865380ef54b28d6 2026-08-02 12:23:40 -0700 Initial commit"; second — "5740a2a6 2026-08-02 12:45:15 -0700 Import semi-formal ontology experiment from ai_character_index"
Reason: Claimed arc-1 window "July–early Aug". By the stated metric, `semi-formal-experiment/` is touched from **2026-08-02** to 2026-08-31, and **zero July commits exist anywhere in this repository** (`--before=2026-08-01` is empty; all 656 commits fall 2026-08-02 → 2026-09-01). Arc-1 work predates the repo and arrived as an import, so July is unrecoverable from this history. Arc-2 verifies: `behavior_pilot/` runs 2026-08-14 → 2026-08-31 (mid–late August). The author is aware of the tension — the preceding commit `3f87fd40` reads "drop the 'six weeks' figure that read against the repo's post-import git history" — but the July label survived.

### Q34
State: contradicted
Evidence: `.github/workflows/ci.yml` (whole file, 33 lines)
Quote: "on:\n  push: { branches: [main] }\n  pull_request: {}"
Reason: Steps enumerate as claimed — three jobs: `semi-formal-experiment` (`.venv/bin/python -m pytest -q`), `walkthrough` (`../semi-formal-experiment/.venv/bin/python -m pytest -q`), and `demo-path` (`cite.py resolve …` plus `graph_check.py … root_graph.production.json`) — matching "both suites plus the citation and graph checks from the demo path". The **trigger is narrower than claimed**: pushes fire only on `main`; a push to any other branch runs nothing. Claimed "every push"; ci.yml states pushes to `main` plus all pull requests. **Additional finding:** every job's first step is `bash setup_env.sh`, which at this pin exits 1 (see Q43), so the workflow as committed cannot be green.

### Q35
State: verified
Evidence: filesystem at pin — `specs/openai-model-spec/README.md`, `specs/claude-constitution/LICENSE`, `data/panel-v5/{LICENSE,NOTICE}`, `LICENSE`
Quote: model spec — "The Model Spec is dedicated to the public domain and marked with the [Creative Commons CC0 1.0](…) deed."; constitution — "Creative Commons Legal Code / CC0 1.0 Universal"; panel-v5 NOTICE — "This directory redistributes data from the ai-character-index project (…, commit ef08e676), by Andres Cotton, licensed under the Apache License, Version 2.0."; root — "MIT License / Copyright (c) 2026 Matt Stults"
Reason: All four license identifiers are as claimed. `specs/openai-model-spec/` has no standalone LICENSE file, but the README's wording is "upstream licence statements **and README files** intact", and the CC0 statement lives in that README — satisfied as worded. `data/panel-v5/` carries both LICENSE and NOTICE.

### Q36
State: verified
Evidence: live run from repo root; both commands exit 0
Quote: `outline` — "model-spec@2025-12-18 / Overview  {#overview} / …" (81 lines); `resolve` — "For objective questions, the factual aspects of the assistant's response should not differ based on how the user's question is phrased."
Reason: Both run under system `python3` with no venv, exit 0, and `resolve` returns a single verbatim sentence confirmed present in `specs/openai-model-spec/model_spec.md`.

### Q37
State: verified
Evidence: live run — `cd semi-formal-experiment && .venv/bin/python machine/query.py seats` (exit 0)
Quote: "attribution_author     haiku            per_worksheet_row  -                                    -> *** NO VALIDATOR ***"
Reason: Exactly one seat prints `*** NO VALIDATOR ***` (`attribution_author`) out of **12 seats reported** — the denominator the dimension asked for. The distinct state is reported separately as required: exactly one seat prints `(none recorded)` (`golden_review`). The README's singular "the seat it reports as unvalidated" is correct for the `NO VALIDATOR` state.

### Q38
State: verified
Evidence: `git show 6d01415b -- walkthrough/…/behavior_pilot/ITERATION_NOTES.md` (+89 / −121); markers at `ITERATION_NOTES.md`:71, :234, :481
Quote: at pin — "## 0002 — BUDGET RULING (2026-08-24) — [operational; redacted]"; at `6d01415b^` — "## 0002 — BUDGET RULING (Matt, 2026-08-24, transcript->artifact) / The 12% weekly-bar cap registered in the SEED entry was already crossed before iteration 1 spent anything: Matt pasted /usage = 23% Fable at the step-1 checkpoint. …"
Reason: Three `[operational; redacted]` markers exist at the pin (entries 0002, 0008, 0021) and the pre-redaction text for each is fully present one commit earlier. The redacted content is exactly what the README says: usage plumbing, quota mechanics, per-seat token counts, budget-point arithmetic. History retains it and is unrewritten (`6d01415b` is an ordinary commit).

### Q39
State: verified
Evidence: `walkthrough/…/behavior_pilot/ITERATION_NOTES.md`:851-856 (entry 0042, committed in `bf0d4978`); `HANDOFF_CURRENT.md`:14-16
Quote: ledger — "BINDING RULE ADOPTED (companion to V5 coverage): every separability/representability claim ships with a seeded matched-granularity random-partition null; the claim is only its MARGIN over the null; **a pass condition satisfiable by noise is void as registered.**"; handoff starred block — "NEW BINDING RULE: every separability claim ships with a matched-granularity random-partition null and is only as strong as its margin over it."
Reason: Recorded, explicitly marked BINDING, in both the ledger and the top starred block, dated after the withdrawal it came out of. `L1L2_ADVERSARIAL_REVIEW.md`:150 then cites it as binding against a later document — operative, not decorative.

### Q40
State: unverifiable
Evidence: live runs of `bash setup_env.sh --check` from repo root — as written: 0.61 / 0.72 s, **exit 1**; with `PY` repointed at a working Python 3.10 carrying the venv's own packages: 1.88 / 2.19 / 3.48 s, **exit 1**
Quote: "15/21 self-test checks passed" / "environment INCOMPLETE — see MISSING/FAILED above."
Reason: The claim is "verifies, ~3 s" — a wall-clock figure for a *verifying* run. No verifying run is reachable at this pin (see Q43): the check exits 1 in both the as-written and the reconstructed environment, so what I timed is a failure path that short-circuits at a different point than the claimed success path. Reported anyway: the reconstructed run is 1.9–3.5 s (median ~2.2 s), consistent with "~3 s"; the as-written run is 0.6 s because it aborts at the first missing import.

### Q41
State: verified
Evidence: `walkthrough/…/behavior_pilot/ITERATION_NOTES.md`:554-570 (entry 0026), :406-411 (0016), :424-430 (0018), :488-494 (0022), :698-712 (0035)
Quote: "THE NUMBER: visible engaged precision is EXACTLY 32/122 = 0.262 (seal: 38 nodes untouched, single-use). The sample series that pointed here: 0.60 (n=20 wave) -> 0.45 (corrected) -> 0.262 (exhaustive). NO SAMPLE WAS CLOSE."
Reason: The untuned behaviours in arc-2 are user-autonomy, proportionate-risk, general-welfare (entry 0016 freezes transfer predictions for all three). **user-autonomy** is the only one ever measured: 0.60 provisional (n=20) → 0.45 corrected → **0.262** exhaustive (n=122, panel/trusted tier), all far below 0.94, none certified. **proportionate-risk** and **general-welfare** were never measured (0016: "measuring any block-2 behaviour awaits a signed prereg amendment"; 0035 still lists the prop-risk test as pending). So no untuned behaviour reached 0.94 on any measurement. Caveat the README omits: these are *engaged precision*, not match-or-defensible — no untuned behaviour has a match-or-defensible measurement at all, so the comparison is metric-mismatched and, for two of three behaviours, true only by absence of data.

### Q42
State: verified
Evidence: programmatic extraction of all markdown links from `README.md` plus existence check at the pin
Quote: 5 relative links, 0 missing — `walkthrough/…/behavior_pilot/ITERATION_NOTES.md`, `…/L1L2_ADVERSARIAL_REVIEW.md`, `…/L1L2_REVIEW_DISPOSITION.md`, `semi-formal-experiment/REPRODUCIBILITY.md`, `walkthrough/…/graph_v2/PRUNED.md` — all OK
Reason: Denominator 5 relative links; all 5 targets exist. Four distinct external URLs (two blog posts, ai-character-index, the CI badge/actions link) flagged, not checked — no network.

### Q43
State: contradicted
Evidence: live run of the Start-here block in order, in the written working directories, with the venv reconstructed
Quote: step 0 — "15/21 self-test checks passed / environment INCOMPLETE — see MISSING/FAILED above."; cause — `walkthrough/paper_pipeline/phase_1/translate.py --self-test`: "AttributeError: '_CrashClient' object has no attribute 'complete_messages'" at `translate.py:3019`, plus two failing sub-checks ("❌ the concept table is written, as data, by a real run"; "❌ a run directory holds what was SENT as well as what came back, for failed clauses too")
Reason: Claimed: all commands run as written and exit 0. Record: **step 0 exits 1** — and not because of the machine's broken venv, since I reproduced it with pytest/clingo/pydantic all importing cleanly; two committed self-tests genuinely fail at this pin. Steps 1–5 (7 command lines: `cite.py outline`, `cite.py resolve`, `graph_check.py`, `measure_join.py`, `benchmark.py --tool`, `query.py seats`, plus the parenthetical `check_model.py`) all exit 0 and produce the documented output, and step 3's `cd` carries correctly into steps 4 and 5. Separately, as *literally* invoked with the committed `.venv` present, steps 3–5 also fail (`No module named …`) — that part is machine state, not the record.

### Q44
State: verified
Evidence: live run — `graph_check.py … root_graph.production.json`, first three lines
Quote: "nodes: 773   uncovered entries: 733 / bad line ranges: 0 / 846 spans  [] / bad quotes: 0 / 602  []"
Reason: Both failure counts are zero. Denominators recovered as the dimension demands: line ranges are checked against **all 846** spans; quotes against the **602** spans that carry one. So "every span checked against the source" is exactly true for line ranges and true for 71% of spans on the stronger quote check — 244 spans have no quote to check. The same run also reports 25 dangling `needs` with no provider and 266 overlapping node pairs.

### Q45
State: verified
Evidence: `walkthrough/…/behavior_pilot/ROUND4_DEV_TABLE.json`; `ROUND4_HELP_CANARY_RESULT.json`
Quote: "\"_\": \"ROUND-4 DEV-BEHAVIOR TABLE COMPLETE (2026-08-24, recovered lineage venue, E4/registered bands, **one-pass defensibility per amendment 1**). Raw = strict panel-majority truth; **headline = match-or-adjudicated-defensible. Both publish.**\"" with `helpfulness.headline.prec = 0.725`, `harm-avoidance-to-third-parties.headline.prec = 0.8824`, `avoiding-over-and-under-caution.headline.prec = 0.75`
Reason: A match-or-adjudicated-defensible ("headline") column **does exist** in the round-4 scored files, per behaviour, with decline cells 0.975 / 1.0 / 0.95 and verdicts scored against the registered bands ("prec IN BAND; decl above" / "both in/above" / "prec IN BAND; decl above"). It cites the registration by amendment id. `ROUND4_HELP_CANARY_RESULT.json` carries the same column under `headline_match_or_defensible`. This is the artifact that decides Q04.

### Q46
State: verified
Evidence: runtime audit — each of the seven demo-path command lines re-run under `sys.addaudithook` watching `socket.connect`, `socket.getaddrinfo`, `socket.gethostbyname`, `urllib.Request`, `socket.bind`, `socket.sendto`; plus a static import-graph walk over 33 first-party modules
Quote: "NETWORK-AUDIT-EVENTS: 0 []" (all seven runs)
Reason: Zero network events at runtime on every Start-here command. The static walk finds `urllib.request`/`urllib.error` in exactly two first-party modules — `semi-formal-experiment/providers.py`:60-61 and `semi-formal-experiment/extract_section.py`:46-47 — and `providers` is reached only via a function-local `import providers` at `extract_section.py`:1101; neither network path executes on the demo path, which the runtime audit confirms.

### Q47
State: verified
Evidence: `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/graph_check.py`:11; `semi-formal-experiment/measure_join.py`:18 → `modelspec_clauses.json`; benchmark output §"Judged universe"
Quote: arc 2 — "RAW = Path(__file__).resolve().parents[5] / 'specs/openai-model-spec/model_spec.md'"; arc 1 — "| helpfulness | model-spec (openai) | 589 | 377 | 212 (36%) | 1.000 |"
Reason: Both arcs read the same primary source, `specs/openai-model-spec/model_spec.md` — arc 2's checker resolves every span against it directly; arc 1's benchmark and join run on clauses segmented from it. `walkthrough/…/behavior_pilot/draw_generalization.py`:38 points at the same file. Corpus shared; representations (clause inventory vs 773-node graph), truth tiers, and metrics disjoint.

### Q48
State: contradicted
Evidence: `walkthrough/…/behavior_pilot/HANDOFF_CURRENT.md` and `semi-formal-experiment/HANDOFF.md`, full heading enumeration
Quote: arc-2 — line 1 "# ⭐⭐ ENTRY POINT (2026-08-25 end; INTEGRATION CLAIMS WITHDRAWN BY REVIEW)"; arc-1 — line 3 "## ⭐⭐⭐⭐ STATE AS OF 2026-08-06 …", line 99 "## ⭐⭐⭐ STATE AS OF 2026-08-05 …", line 131 "## ⭐⭐ STATE AS OF 2026-08-04 LATE …"
Reason: First value verifies: both handoffs have a star-marked top block. Second value does **not**. (a) Arc-1's HANDOFF.md has **four** star-marked blocks stacked at the top (⭐⭐⭐⭐ at :3, a nested ⭐⭐⭐⭐⭐ blockquote inside it, ⭐⭐⭐ at :99, ⭐⭐ at :131), so "the top starred block" does not pick out a unique region and a reader following the README has no way to know where to stop. (b) Several sections below carry neither a date nor a superseded/archive marker: `## ⚠️ MUTATION TESTING IN THIS REPO CAN LIE TO YOU` (:504), `## Where we are in one paragraph` (:525), `## The finding that shapes the architecture` (:548), `## The two invariants that are easiest to violate and hardest to detect` (:557), `## Two protocol defects to state with any number` (:597), `## Settled — do not re-open` (:609); likewise in the arc-2 handoff (`## Instrument state (frozen, all-truth baseline)`, `## Terminality language`). The README's softer phrasing ("self-marked and partly superseded") survives; the claim as dimensioned does not.

### Q49
State: verified
Evidence: filesystem at pin — existence check on all 8 Layout-block paths
Quote: "OK engine / OK specs / OK data / OK semi-formal-experiment / OK walkthrough / OK ARTIFACTS.md / OK LEDGER.md / OK ARC2_HANDOFF.md"
Reason: 8 of 8 exist (the last two as symlinks whose targets resolve).

### Q50
State: verified
Evidence: each demo-path command run twice and byte-compared with `cmp`
Quote: "IDENTICAL 1a/1b / IDENTICAL 2a/2b / IDENTICAL 3a/3b / IDENTICAL 4a/4b / IDENTICAL 6a/6b / IDENTICAL bench"
Reason: `cite.py outline`, `cite.py resolve`, `graph_check.py`, `measure_join.py`, `benchmark.py --tool` (354 lines including every threshold-curve row) and `query.py seats` all produce byte-identical output on consecutive runs. Determinism holds across the whole Start-here block.
