# Baseline adversarial review — REPORT

**Start (wall clock):** 2026-09-02 13:13:50 PDT
**End (wall clock):** 2026-09-02 13:40:59 PDT
**Total time:** 27 min (13:13:50 → 13:41 PDT)

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

---

## Universally quantified prose claims (hypotheses)

### H01
State: contradicted
Evidence: arc-1 — `semi-formal-experiment/cycles/*/review_verdict.json` (6 of 6 closed cycles) and `cycles/CYCLE_LOG.jsonl`; arc-2 — `ITERATION_NOTES.md`:141 (0005), :266 (0010), :346 (0014), :178 (0006)
Quote: arc-1 — `chain-repair-2026-08-04/review_verdict.json`: "{'verdict': 'proceed', 'by': 'change-review seat, Claude (Fable 5), independent session 2026-08-03 — not the implementer'}"; arc-2 counterexample — "## 0006 — **POST-CLOSE**: PATH AUDIT + OPUS PARITY CERTIFICATE, 2026-08-24"
Reason: Arc-1 verifies cleanly: all six cycles listed in CYCLE_LOG.jsonl carry a `review_verdict.json` by a named independent, clean-context, not-the-implementer reviewer; the seventh directory (`segmentation-variants-2026-08-04`) has no decision/state/review and was never closed, so it is not a close. Arc-2 **fails the universal**: the three iteration closes (0005 "ITERATION 1, STEPS 4-5 (REALIZATION + CLOSE)", 0010 "ITERATION 2 CLOSE", 0014 "ITERATION 3 CLOSE") record no adversarial review at or before the close, and the nearest review artifact — the path audit in 0006 — is explicitly labelled POST-CLOSE. Arc-2's adversarial reviews (0020, 0031, 0042, 0043) attach to plans and to withdrawals, not to iteration closes. Both values: 6/6 arc-1 closes reviewed; 0/3 arc-2 iteration closes reviewed at-or-before.

### H02
State: verified
Evidence: arc-1 — `cycles/*/state.json` `frozen_prediction_sha` in all 6 closed cycles, with `prediction_check.json` alongside; arc-2 — `ITERATION_NOTES.md`:135-139 (0004), :406-411 (0016), `ROUND4_PREREG.md`, `ROUND4_FREEZE_DERIVATION.json`
Quote: arc-1 — `patient-pricing-2026-08-04/decision.json`: "the frozen prediction (prediction.json sha c99260f031c991fccbc7a506033cc5a1b89dd90f2e9951e417708587fb621923) pre-registered max_regressions = 0 as this cycle's falsifiable bound"; arc-2 — "V5 prediction registered (ITERATION1_V5_PREDICTION.json) **BEFORE any attempt-2 ruling**"
Reason: Within the rule's stated scope (cycles and iterations that record a measurement) every measurement is preceded by a frozen, sha-pinned prediction: six arc-1 cycles each carry `frozen_prediction_sha`; arc-2 iterations 1–3 each register a V5 prediction before rulings; round 4 registers per-behaviour predictions with a seed and an exclusion-list sha in `ROUND4_FREEZE_DERIVATION.json`; block 2 freezes `BLOCK2_TRANSFER_PREDICTIONS.md` before any block-2 ruling. Two weaknesses the record logs rather than hides: entry 0009 finds one registration "invalid-by-construction" for lack of coverage of the move it gated; and entries 0027/0028/0035/0036 report ad-hoc $0 probe measurements with no prediction freeze — outside the rule's scope (neither cycles nor iterations), but a reader taking "pre-registered predictions" at full generality would count them against it.

### H03
State: verified
Evidence: `git log --numstat -- walkthrough/…/behavior_pilot/ITERATION_NOTES.md` over all 45 commits touching it; errata at `ITERATION_NOTES.md`:417 (#13), :430 (#14), :453 (#15), :541 (#16), :568 (#17), :578 (#18), :770 (#19), :739 (#20), :863 (#21)
Quote: the only deleting commit — "6d01415b +89 -121  2026-08-31  Publication prep: prune superseded evidence with manifest, redact operational plumbing…"
Reason: Of 45 commits that touch the ledger, **exactly one** deletes prior entry text, and every one of its hunks removes operational content (weekly-bar percentages, `/usage` pastes, per-seat raw-token counts, budget-point arithmetic) or replaces a verbatim conversational quote with an unattributed paraphrase of the same ruling — all inside the README's declared redaction scope ("usage plumbing, working notes"). Three hunks carry explicit `[operational; redacted]` markers (0002, 0008, 0021); the rest are met by the "operational_only" disjunct rather than "marked_redaction". No finding, number, verdict, or erratum was altered. Numbered errata exist (#13–#21). Adversarial note: the unmarked de-identification hunks (e.g. `Matt: "Let's ignore my 'final run' message for now"` → `RULING: …` at entry 0013) are a judgement call — they are working notes, but a stricter reader could call them unmarked edits to prior entry text.

### H04
State: verified
Evidence: `ITERATION_NOTES.md`:14-17 (0000); `ROUND4_PREREG.md`:26-29; `HANDOFF_CURRENT.md`:56; `panel_run1/convergence/definitional_lane_prereg.md`
Quote: round-4 venue — "seats execute as fresh Fable subagents receiving **only the packet prompt string plus the recorded content-free tool fence**"; dispatch rule — "Seat must be BLIND (packet = claims+span only; never truth or this file)"; seed entry — "one seat fabricated-from-memory dispatch was voided (rule: prompts ONLY from committed packet files, never retyped)"
Reason: Every seat-dispatch record in the ledger and preregs specifies packet-only inputs with truth, design documents, and prior verdicts excluded, and the record includes the one violation it caught and voided. The truth-injection at entry 0001 ("injecting the FROZEN attempt-1 verdicts into SC.truth_all for this slug only") is scorer-side, not seat-side, and is disclosed as read-only consumption. **Qualification:** blindness here is self-attested by the dispatch records; no independent audit of any dispatch's actual inputs exists in the repository, so the hypothesis is verified as recorded, not as externally confirmed.

### H05
State: verified
Evidence: programmatic reconstruction — for each of the 44 entries, the first commit in `git log --reverse -- ITERATION_NOTES.md` whose blob contains that `## NNNN — ` heading, compared to the date stated in the heading
Quote: "entries found: 44 0000 0043 / gapless 0000-0043: True / entries with NO stated date in heading: 0 / entries whose stated date differs from first-commit date by >1 day: 0"
Reason: All 44 entries carry a date in the heading and every one is within one day of the commit that first introduced it — zero exceptions across the full history. "Written at the time" is borne out at the entry level.

### H06
State: verified
Evidence: `ITERATION_NOTES.md`:832-865 (0042) and :866-907 (0043); `RETRANS_REVIEW_DISPOSITION.md`; `L1L2_REVIEW_DISPOSITION.md`; commits `bf0d4978`, `365d68b3`
Quote: 0042 — "Clean-context Opus reviewer: P1 **UNSUPPORTED** (as measured), P2 **UNSUPPORTED**, 8 findings. CoVe'd per standing rule"; 0043 — "Clean-context Opus review (full text: L1L2_ADVERSARIAL_REVIEW.md, 36 findings + 20 amendments): verdict **DOES-NOT-LICENSE**, accepted after CoVe"
Reason: Arc-2 has exactly two withdrawal events, and both are preceded (same entry, review first, disposition second) by a clean-context adversarial review whose finding is in the admissible set — UNSUPPORTED/null-dominated for the census, DOES-NOT-LICENSE for L1/L2 — with the withdrawal linked to the review by named disposition document and commit. The third item the README lists (query-class, `1143a921`) is not a withdrawal and had no review; that is scored against Q29 and V07, not here.

### H07
State: verified
Evidence: as Q41 — `ITERATION_NOTES.md`:554-570 (0026), :406-411 (0016), :698-712 (0035)
Quote: "visible engaged precision is EXACTLY 32/122 = 0.262 (seal: 38 nodes untouched, single-use)"
Reason: No untuned behaviour has any certified measurement at or above 0.94, and none has two draws at or above 0.94 — user-autonomy's measurements are 0.60 / 0.45 / 0.262, and proportionate-risk and general-welfare have no measurements at all. The universal holds, but partly by **vacuity**: for two of three untuned behaviours the record contains nothing to falsify it, and for the third the available metric (engaged precision) is not the match-or-defensible metric the 0.94 threshold is defined on.

### H08
State: unverifiable
Evidence: repo-wide search for an enumeration of symbolic-engine failures classified refusal-vs-wrong-answer; `grep -rn "refusals, not wrong"` over all `*.md`
Quote: the only hit in the entire repository is the README itself — "worked — its failures were refusals, not wrong answers."
Reason: The record holds **no enumeration of symbolic-engine failures**, so the universal has no domain to quantify over and no artifact decides it. The nearest candidate, `semi-formal-experiment/S3B_FINDING_RECLASSIFICATION.md`, buckets *adversarial-review findings* (INEXPR / EXPR-UNVER / PROCESS / DOC), not engine outputs. Pulling the other way, `semi-formal-experiment/adversarial_review_1.md` finding 11 records one instance that reads as a wrong answer rather than a refusal — "at EXTRACTION time a missing atom fails silently (finding 7 is a live instance — missing self-regarding-harm distinction **silently produced the headline conflict**)" — though the repo's own scoping rule (README C04: a conflict is a claim about an encoding, not the document) would reclassify it as an encoding defect. Either way, "every recorded failure" cannot be checked because the failures were never recorded as a set.

### H09
State: verified
Evidence: live run — `benchmark.py --tool …`, §"Head-to-head — tool vs judge, one row per gold" (9 rows) and §"Threshold-free"
Quote: the closest row — "| helpfulness | fable+kimi | sol | **+0.207** | +0.308 | …"; and "**judge wins 9 / 9 cells at its own operating point.**"
Reason: In all nine head-to-head cells the tool's MCC is strictly below the held-out judge's on the TRUE universe (tool 0.172/0.223/0.207, 0.359/0.316/0.375, 0.276/0.296/0.276 vs judges 0.697/0.706/0.308, 0.705/0.677/0.464, 0.535/0.552/0.354). Narrowest gap +0.101 (helpfulness vs sol). No tie, no exceedance; the threshold-free table gives the same verdict without the fitted threshold.

### H10
State: contradicted
Evidence: `walkthrough/…/graph_v2/PRUNED.md`; `git cat-file -t` on sampled object ids; `git log --format='%G?'`
Quote: "each entry pins the exact content by git object id (tree/blob sha at the pre-prune commit). To restore any entry: `git checkout <pre-prune-commit> -- <path>`"
Reason: The prune event exists (`6d01415b`), the manifest carries restore instructions, and sampled entries resolve in git (4/4 clean, so listed artifacts do exist in an earlier commit). But `signed(manifest(k))` **fails**: no signature of any admissible kind on the manifest, and no signed commits anywhere in the repository. The conjunction fails on its middle clause. Two lesser gaps: the restore recipe leaves `<pre-prune-commit>` unresolved, and two of ~90 rows pin `untracked-or-file` rather than an object id, so those two artifacts are not shown to exist in any earlier commit.

### H11
State: verified
Evidence: `git show 6d01415b` (full ledger diff, +89/−121) and `git show 6d01415b^:…/ITERATION_NOTES.md`; markers at `ITERATION_NOTES.md`:71, :234, :481
Quote: pre-redaction text for 0008 — "## 0008 — FINAL-BLOCK BUDGET CHECKPOINT (Matt, 2026-08-24) / /usage pasted at 27% Fable; Matt: \"Please continue.\" — explicit authorization for the final all-Fable block…"
Reason: Both conjuncts hold. Every marked-redacted section has content in the immediately preceding commit (checked for all three: 0002, 0008, 0021). And every hunk that deletes prior entry text lives in the single commit `6d01415b` and removes only operational content or replaces a quote with a paraphrase preserving the ruling. The `[REDACTED]` strings at `specs/openai-model-spec/model_spec.md`:884,888 are upstream OpenAI redactions in the vendored source document, not this repo's.

### H12
State: verified
Evidence: live run — `cd semi-formal-experiment && .venv/bin/python relevance.py helpfulness --top 3` and `… --explain m0452`
Quote: hit line — "1.000  m0452  model_spec@2025-12-18 > Do the best work > Be creative > ¶4"; explain — `"locator": "model_spec@2025-12-18 > Do the best work > Be creative > ¶4"`, `"quote": "Context matters, because creativity should not come at the expense of truthfulness, clarity, or usefulness[^uotj]…"`, `"channels": {"lex": 0.348…, "atom": 1.825…, "kind": 0.0, "section": 0.746…}`, `"matched_atoms": [{"name": "truthful_communication", …}]`
Reason: Every hit carries a resolvable span locator, the verbatim quote at that locator, and — via `--explain` — a decomposed reason (per-channel contributions, channel shares, and the named atoms that matched). The locator format is the one `engine/spec-cite/cite.py resolve` consumes (Q36), so the span is verifiably verbatim. Minor gap: the reason requires the `--explain` flag; the ranking output alone gives locator + quote + score but not the reason.

### H13
State: verified
Evidence: `walkthrough/…/behavior_pilot/RETRANS_REVIEW_DISPOSITION.md`:9-27; `L1L2_REVIEW_DISPOSITION.md`; `ITERATION_NOTES.md`:838-843 (0042), :869-872 and :899-901 (0043)
Quote: "## CoVe re-derivations (driver-run, $0, deterministic) … CONFIRMED by re-derivation (exactly 23/39)." and 0043 — "Reviewer errors corrected in disposition: its panel-v5 rates and its 1-NN p-values were wrong (findings survive on my re-derived numbers)."
Reason: For both withdrawal reviews, each decisive finding was re-derived by the driver — an actor distinct from the clean-context Opus reviewer — before the corrected verdicts were written, and both dispositions record re-derivation results alongside the reviewer's originals. The independence is real enough to have caught reviewer errors in both directions (0042: "One reviewer slip corrected: 'ua'=user-autonomy"; 0043: two reviewer numbers wrong, findings surviving on the driver's numbers). **Qualification:** the re-deriving actor is the driver who authored the claims under review, so the independence is from the *reviewer*, not from the claim's author — weaker than the word "independent" suggests.

### H14
State: unverifiable
Evidence: `ITERATION_NOTES.md` entries 0001, 0003, 0004, 0005 (iteration 1 steps), 0007/0009/0010 (iteration 2), 0012/0014 (iteration 3); `CALCULUS_RUNBOOK.md`; `ITERATION_NOTES.md`:378-381 (entry 0015)
Quote: entry headings — "## 0001 — ITERATION 1, STEP 1 (TRIAGE)", "## 0003 — ITERATION 1, STEP 2a (R1 ESCALATION)", "## 0004 — ITERATION 1, STEPS 2b-3 (C-D MOVE + V1-V4) and STEP-4 PREP", "## 0005 — ITERATION 1, STEPS 4-5 (REALIZATION + CLOSE)"; and 0015 — "CALCULUS_RUNBOOK v1 rewritten FROM notes 0001-0014 (execution-derived; docs-tests 5/5)"
Reason: Step-headed entries exist for iterations 1–3 and each names its steps and cites artifacts by filename, so the hypothesis is well supported in the direction sampled. But the quantifier runs the other way — over every step the runbook says emits a committed artifact — and the runbook at the pin was itself rewritten *from* the very ledger entries it would be used to audit. The step→artifact→entry mapping is therefore circular at the pin, and closing it would need the pre-0015 runbook plus a step-artifact inventory, neither of which the repository holds.

### H15
State: verified
Evidence: `ARTIFACTS.md`; existence check on all 26 routed paths at the pin
Quote: 26 of 26 resolve, including both symlinked roots (`LEDGER.md`, `ARC2_HANDOFF.md`) and the directory route `semi-formal-experiment/machine/`
Reason: Zero dangling routes. Two incidental drifts noticed but outside the claim: ARTIFACTS.md says "the 348 files there" for `behavior_pilot/` (`ls` gives 346 at the pin), and describes the certified graph as "773 nodes, zero bad spans of 846", which matches Q44 exactly. The converse (every star artifact is listed) is out of scope per the claim.

---

## Verdict statements

### V01
State: contested
Evidence: needs — (a) in-sample tuned rate: `HANDOFF_CURRENT.md`:106-107 (0.941/0.953/0.960) ✔; (b) untuned rate: `ITERATION_NOTES.md`:556 (user-autonomy 32/122 = 0.262) ✔ *at a different metric*; (c) the bar defined: `README.md`:6-7 ✔
Quote: bar — "Frontier-model panels were the calibration instrument — the tool should match the panel, or give an answer a frontier model would accept as justifiable."
Reason: The verdict's direction is right and two of three needs verify outright. Need (b) does not verify at the claim's dimensions: the only untuned measurement is *engaged precision* (0.262), not match-or-defensible, and the two remaining untuned behaviours were never measured — so "did not reach that bar on generalization" rests on one behaviour at a non-comparable metric plus two absences. The bar's definitional provider is the README's own opening sentence: adequate, though circular. Contested because the two rates the verdict compares are not on the same instrument.

### V02
State: unverifiable
Evidence: as H08 — no enumeration of engine failures exists anywhere in the record
Quote: `semi-formal-experiment/adversarial_review_1.md` finding 11 — "at EXTRACTION time a missing atom fails silently (finding 7 is a live instance — missing self-regarding-harm distinction silently produced the headline conflict)"
Reason: Need 2 ("an enumeration of engine failures exists in the record") has no provider, which the claim itself anticipated as the vacuity condition; need 1 (classification of every engine failure) is therefore unreachable. **Dangling need:** the enumeration of engine failures. The one candidate wrong-answer instance the record does hold points the opposite way from the verdict.

### V03
State: unverifiable
Evidence: `semi-formal-experiment/segmentation_summary.md` (constitution, 616 clauses); `semi-formal-experiment/modelspec_segmentation_summary.md`; `modelspec_classification_summary.md`
Quote: "**Total clauses: 616** … **Formalizable fraction (conditional): 31.7%**"
Reason: The record holds post-segmentation *inventories* for both specs with kind distributions, but I could locate no artifact pairing (i) a named segmentation-failure event, (ii) a repair event linked to it, and (iii) a post-repair measurement of segmentation quality. **Dangling needs: all three.** The summaries state what the segmentation produced, not that it failed, was repaired, and then measured better. "Worked after repair" is a narrative the README supplies; the record supplies only the "worked" end state.

### V04
State: verified
Evidence: all four needs verify — Q12 (tool MCC +0.32 in-sample / +0.278 label-free), Q14 (judge LOO mean +0.555), Q15 (9/9 cells), plus per-judge values from the head-to-head table
Quote: "**judge wins 9 / 9 cells at its own operating point.**"
Reason: Tool MCC, judge MCC per judge and as LOO mean, and the per-cell comparison at matched false-positive rate are all present and mutually consistent on the TRUE universe. The tool loses every cell by every comparator offered. No dangling needs.

### V05
State: contested
Evidence: coverage need — `RETRANS_REVIEW_DISPOSITION.md`:57 (39/39, over nodes) ✔ *at the wrong denominator*; per-test separability need — only one test ever faced a null ✘
Quote: "two blind seats retranslated 39/39 full spans with the schema and ZERO new coinages (coverage-in-form)"
Reason: Inherits Q27 and Q28. The coverage need is met by a measurement over 39 stratified nodes, not the 100 definitions the sentence binds it to; the per-test need is met for exactly one separability test out of at least three separability measurements in the record. The sentence compresses two differently scoped results into one clause the record does not support as a whole.

### V06
State: contested
Evidence: pre-registered predictions H02 ✔ (both arcs); blind seats H04 ✔ (as attested); append-only ledger with errata H03 ✔ (arc 2 only); adversarial review before every close H01 ✘ (arc-2 iteration closes)
Quote: `cycles/CYCLE_LOG.jsonl` — six closed arc-1 cycles each with a `review_verdict.json`; against `ITERATION_NOTES.md`:178 — "## 0006 — POST-CLOSE: PATH AUDIT…"
Reason: Three of the four named discipline elements instantiate in both arcs. The fourth — adversarial review before *every* close — instantiates in arc 1 (6/6 cycles) but not at arc-2's three iteration closes, so the element that most needs the word "transferred" is the one that did not transfer intact. Additionally the append-only ledger with numbered errata is an arc-2 construct with no arc-1 counterpart (arc 1 uses per-cycle records), so "transferred" runs backwards for that element. Contested rather than contradicted because each element does exist in both arcs in some form.

### V07
State: contradicted
Evidence: as Q29 — `bf0d4978` and `365d68b3` qualify; `1143a921` does not
Quote: `git show 1143a921 --stat` — "1 file changed, 18 insertions(+)" (ITERATION_NOTES.md only); pre-`1143a921` starred block — "choose: coarse bound now / brief v3 / accept-with-noise"; `QUERY_CLASS_STUDY_STATUS.json` — "NO QUERY_CLASS_BOUND.json is published from tripwired data."
Reason: The need is three DISTINCT headline withdrawal events, each linked to a review. Two exist and are exemplary. The third is a bounding erratum against a claim that was never published as a headline and was not preceded by an adversarial review — it was the project owner's suspicion upheld by the driver's own inspection. Claimed 3; record supports 2.

### V08
State: verified
Evidence: `bf0d4978` ← `RETRANS_REVIEW_DISPOSITION.md` (clean-context Opus reviewer, CoVe'd); `365d68b3` ← `L1L2_ADVERSARIAL_REVIEW.md` + `L1L2_REVIEW_DISPOSITION.md`
Quote: "0041 withdrawn: integration census fails adversarial review (P1/P2 UNSUPPORTED)" and "L1/L2 withdrawn: the licensing experiments fail their own adversarial review (DOES-NOT-LICENSE, accepted after CoVe)"
Reason: Both actual withdrawals are linked, in the same commit, to a preceding named review document with a recorded verdict. The linkage is tight: review file, disposition file, ledger entry, and commit message all name each other. (This verdict is about the two withdrawals, not the count — the count is V07.)

### V09
State: verified
Evidence: `ITERATION_NOTES.md`:280-284 (entry 0010); `ITER2_REMEASURE_SCORED.json`
Quote: "THE HONEST HEADLINE IS RECALL, NOT PRECISION: 23/40 pooled declined nodes are panel-relevant. The module's engaged side sits ~0.6-0.7; its DECLINED side leaks a large relevant mass"
Reason: Both needs verify: a ledger entry states recall as the honest headline in those words, and supplies the recall-side number (23 of 40 declined nodes panel-relevant, a 57.5% miss rate on the declined set), pooled over the two frozen draws.

### V10
State: verified
Evidence: `ITERATION_NOTES.md`:851-856 (entry 0042, commit `bf0d4978`, 2026-08-25 10:04) and `HANDOFF_CURRENT.md`:14-16
Quote: "BINDING RULE ADOPTED (companion to V5 coverage): every separability/representability claim ships with a seeded matched-granularity random-partition null; the claim is only its MARGIN over the null; a pass condition satisfiable by noise is void as registered."
Reason: The rule is recorded as binding, in the same entry as the first withdrawal and therefore dated at-or-after it, and it is applied against the second withdrawal 19 minutes later (`L1L2_ADVERSARIAL_REVIEW.md`:150: "L2 ships with no null — in direct violation of the binding rule adopted in the same document"). "Came out of these" is supported by the sequence.

### V11
State: verified
Evidence: census ← `RETRANS_REVIEW_DISPOSITION.md` "Corrected verdicts"; L1/L2 ← `L1L2_REVIEW_DISPOSITION.md`; arc-1 relevance ← live `benchmark.py` output; round-4 ← `ROUND4_DEV_TABLE.json`
Quote: "P1 … NOT ESTABLISHED. The measured separability is real but carries no information beyond what a random partition of the vocabulary provides at matched granularity … P2 … NOT ESTABLISHED."; and the benchmark's own per-behaviour verdict column
Reason: Each demonstration attempted is linked to a failing review or a failing measurement: the integration census (review, NOT ESTABLISHED ×2), L1/L2 (review, DOES-NOT-LICENSE), the arc-1 relevance benchmark (the committed scorer's own verdict column reads "below bar" for all three behaviours on the true universe and "BELOW FLOOR"/"UNUSABLE FOR HEADLINE" on the published one), and the round-4 certification (two of three raw cells fire falsifier F1). No demonstration in the record is left standing unreviewed.

### V12
State: contested
Evidence: two of three ended claims have review events (`RETRANS_REVIEW_DISPOSITION.md`, `L1L2_ADVERSARIAL_REVIEW.md`); the third (query-class saturation) does not
Quote: `ITERATION_NOTES.md`:739-741 — "## 0037 — ERRATUM #20: CLOSED-VOCABULARY CIRCULARITY (Matt's suspicion, upheld) … **Upheld on inspection**, two mechanisms: (a) ENDOGENEITY … (b) CIRCULARITY"
Reason: For the two withdrawals the review→claim linkage is explicit and documented. For the query-class saturation claim the "review" is the project owner's suspicion upheld by the driver's own inspection — self-review, not the clean-context adversarial review the sentence advertises. **Dangling need:** a review event for the third ended claim. The README's "the adversarial reviews that ended the headline claims" over-generalises from two cases to three.

---

## Author commitments (reported; no state assigned)

**C01** — "This repo is the complete record of the attempt: the machinery, the measurements, and the discipline that kept the measurements honest."
Largely borne out, with two named holes. The machinery runs (Q05, Q07, Q36, Q37, Q44, Q50), the measurements regenerate from committed data (Q12–Q15, Q24, Q46), and the discipline artifacts are present and internally consistent (Q25, H05, H15). Two things the record does **not** contain: the denominators behind the 0.94–0.96 criterion standing (Q01 — no artifact regenerates those three numbers), and any panel internal-agreement statistic (Q02 — `REPO_TRAPS.md` says outright that none exists). "Complete" also cannot cover arc 1's July work, which predates the repository (Q33). Of the ~9,800 pruned files, the manifest pins all but two rows in git history (Q32/H10), so completeness-by-history is real.

**C02** — "The full commit history is published unrewritten so that every dated claim, pin, and withdrawal is externally checkable."
Borne out for what is in the repo. All three named withdrawal/bounding commits resolve at their short hashes with matching content (Q18, Q21, Q23); the ledger's 45 commits show a single deleting commit whose every hunk is inspectable (H03); `6d01415b` is an ordinary commit, not a rewrite. The caveat is scope, not honesty: history begins at "Initial commit" 2026-08-02 with arc 1 arriving as an import from another repository, so the pre-August record is not published here and the July window is not externally checkable from this history (Q33). Commits are unsigned (`%G?` = N) — which matters for Q32, not for this commitment.

**C03** — "Everything below is deterministic re-analysis of committed data: no API keys, no network, no model calls."
Borne out on substance, overstated on "runs as written". Runtime auditing found **zero** network syscalls across all seven Start-here command lines, and the two modules that import `urllib` are never executed on that path (Q46). Every command's output is byte-identical across runs (Q50). What is not true is the surrounding promise that the block runs clean: step 0, `bash setup_env.sh --check`, exits 1 at this pin with "15/21 self-test checks passed" because two committed self-tests genuinely fail (Q43) — and since CI's first step in all three jobs is `bash setup_env.sh`, the workflow as committed cannot be green (Q34).

**C04** — "Claims are scoped throughout: every separability claim requires its null; every 'unresolved conflict' is a claim about an encoding and a fragment, not about the document."
Borne out prospectively, not retrospectively. The null rule is genuinely binding after 2026-08-25 (Q39, V10) and was enforced against L1/L2 within the hour. But it was adopted *after* the separability claims it would have killed, and the record still carries separability measurements with no null attached (0038's 94/100, 0039's 0.37–0.40 / 0.85) — which is why Q28's "every" fails. The encoding-scoping half is well supported: `rules.lp`'s own header scopes conflicts to "the 'faithfulness to the user' fragment" under explicit `interp/1` assignments, and `check_model.py`'s "60 contradiction(s) reported by rules.lp" is presented as an output of the encoding.

**C05** — "`AGENTS.md` (symlinked as `CLAUDE.md`) is the canonical brief: read it before acting in this repo."
Borne out. `CLAUDE.md -> AGENTS.md` is a real symlink (Q31), and AGENTS.md opens by declaring itself canonical — "**This file is the single canonical brief for every AI agent and every new human contributor.** `CLAUDE.md` is a **symlink to this file**" — and gives an ordered reading list whose five entries all exist. Consistent with ARTIFACTS.md's "Agent brief" row.

**C07** — "This is the primary artifact." (of `ITERATION_NOTES.md` / `LEDGER.md`)
Borne out. The ledger is the load-bearing document for the great majority of arc-2 claims verified here (Q16, Q17, Q19, Q20, Q22, Q23, Q25, Q26, Q28, Q29, Q39, Q41, H03, H05, H06, H07, H13); it is gapless 0000–0043, dated at the time (H05), append-only apart from one auditable redaction commit (H03), and ARTIFACTS.md routes to it first. Where I could not decide a claim it was almost never because the ledger was silent — it was because a *scored artifact* the ledger references (the 0.94–0.96 denominators) or a whole class of artifact (engine-failure enumeration, panel agreement, segmentation failure/repair) does not exist.

---

## Summary

| State | Q01–Q50 | H01–H15 | V01–V12 | **Total** |
|---|---:|---:|---:|---:|
| verified | 38 | 11 | 5 | **54** |
| contradicted | 9 | 2 | 1 | **12** |
| contested | 2 | 0 | 4 | **6** |
| unverifiable | 1 | 2 | 2 | **5** |
| | 50 | 15 | 12 | **77** |

Author commitments C01–C05, C07 reported without a state (6 items).

**contradicted:** Q02, Q04, Q28, Q29, Q32, Q33, Q34, Q43, Q48, H01, H10, V07
**contested:** Q06, Q27, V01, V05, V06, V12
**unverifiable:** Q40, H08, H14, V02, V03

### Dangling needs (V-item needs with no provider in the README)

1. **V02** — an enumeration of symbolic-engine failures. No such enumeration exists anywhere in the repository, so the claim that the engine's "failures were refusals, not wrong answers" has no domain of failures to quantify over.
2. **V03** — a segmentation-failure event; a repair event linked to it; a post-repair measurement of segmentation quality. All three dangle: the record holds post-segmentation inventories only, never the failure, the repair, or a quality delta.
3. **V12** — a review event for the third "ended" headline claim (query-class saturation). The record supplies only the project owner's suspicion upheld by the driver's own inspection.
4. **V01** (partial) — an untuned-behaviour rate *at the match-or-defensible metric*. The only untuned measurement is engaged precision; the metric the bar is defined on was never measured off the tuned trio.
5. **V05** (partial) — a coverage measurement over the 100 definitions. Coverage exists only over a 39-node stratified sample.

### What I could not check, and why

I could not use the network, so the two blog-post URLs, the CI badge, and the actual state of the GitHub Actions runs are flagged and unverified — which matters, because my reading of `.github/workflows/ci.yml` combined with the live failure of `bash setup_env.sh` says the workflow cannot be green at this pin, and only the Actions page would settle that. I could not recover the denominators behind the 0.94–0.96 criterion standing (Q01): the three numbers appear once, in a handoff bullet, with no scored artifact, no regenerating script, and no engaged-set sizes anywhere in the repository, so I can confirm the values are stated but not that they are correct. I could not decide H08/V02 or V03 because the record holds no enumeration of engine failures and no segmentation failure/repair/post-repair triple — absence of the artifact class, not ambiguity within it. H14 is unverifiable for a subtler reason: `CALCULUS_RUNBOOK.md` was rewritten *from* the very ledger entries it would be used to audit, so the step→artifact→entry mapping is circular at the pin. Q40's "~3 s" is unverifiable because no passing run of `setup_env.sh --check` exists at this pin to time. Finally, every live-run result rests on my reconstruction of the venv (an equivalent Python 3.10 plus the venv's own `site-packages`), because the committed `.venv` symlinks to an interpreter outside the repository that has since been upgraded; `.venv*/` is gitignored, so this is machine state rather than a defect in the record, but it does mean I verified the demo path against a reconstructed environment rather than the one a reader gets by running the commands literally on this machine today. The blind spot I am least able to close by inspection is H04: seat blindness is asserted by every dispatch record and contradicted by none, but nothing in the repository independently audits what any seat actually received.
