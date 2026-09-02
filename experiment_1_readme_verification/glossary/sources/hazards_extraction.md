<!-- Source extraction for the glossary: hazard classes and git/ledger conventions. Extractor: general-purpose subagent, model opus, read-only over the target record and git history, README.md excluded by instruction. All substantial report messages from the extractor's transcript are concatenated here in order, untouched. -->

I have complete coverage. The item-3 agent is still running, but I gathered that material directly. Producing the report.

---

# Hazard classes and conventions in `semi-formal-document-analysis`

Repo root: `~/Documents/ai_safety_projects/semi-formal-document-analysis`. HEAD `48e66ce0`, branch `d3-worked-example` (not `main`). All paths below are repo-relative. Top-level `README.md` excluded per instruction.

Shorthand: `BP/` = `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/`, `G2/` = `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/`.

---

## 1. Superseded ledger entries and the record's marking conventions

### 1.1 The record's own stated conventions

Three distinct marking systems coexist, and they do not agree.

**(a) The ledger convention — append-only, numbered, dated, never struck.**

`BP/ITERATION_NOTES.md:1-5`
```
# ITERATION NOTES — append-only learning ledger for the calculus loop
(Convention, binding via CALCULUS_RUNBOOK step 5b: EVERY step of every
iteration appends a dated entry here — what surprised, what the docs got
wrong, what the next agent must know. This file is the SOURCE for runbook
rewrites; learning that is not an artifact here does not exist.)
```

`BP/README.md:10-11` — `"ITERATION_NOTES.md — the append-only ledger, entries 0000–0043. The primary artifact: every step, erratum, and withdrawal, written at the time."`

`BP/README.md:64` — `"results) are adjudicated ledgers: append-only, never regenerated."`

Under this convention a superseded entry is **not** edited; a later numbered entry withdraws it. Entry 0042's title is the canonical form:

`BP/ITERATION_NOTES.md:832` — `"## 0042 — 0041 WITHDRAWN: THE INTEGRATION CENSUS FAILS ITS ADVERSARIAL REVIEW, 2026-08-25"`

**(b) The star/stop-sign convention (HANDOFF.md).** Star count = recency/priority of a state block; ⛔ = do not act on this; ⚠️ = caveat; `~~strikethrough~~` = retracted-but-retained text.

`semi-formal-experiment/HANDOFF.md:292-294`
```
Everything below this section is history: correct when written, load-bearing as
provenance, and in several named places **superseded** (each such place now carries
a ⛔/⚠️ marker pointing back here — nothing was silently deleted).
```

Marker inventory in `HANDOFF.md`: ⭐ on 6 lines, ⛔ on 11, ⚠️ on 14, `~~` on 12.

Star levels observed: `HANDOFF.md:5` (⭐⭐⭐⭐⭐, 2026-08-18), `:3` (⭐⭐⭐⭐, 2026-08-06), `:99` (⭐⭐⭐, 2026-08-05), `:131` (⭐⭐, 2026-08-04), `:955` and `:1142` (⭐). `BP/HANDOFF_CURRENT.md:1` is ⭐⭐.

`AGENTS.md:16-18` tells the reader how to use it:
```
1. **`semi-formal-experiment/HANDOFF.md`** — its top starred section only. Current state,
   what is closed, what is parked, and the standing rulings. Everything below that
   section is history (self-marked, some superseded).
```

**(c) The delete-don't-annotate rule — which contradicts (b).** The same file also states that annotation is *insufficient* and superseded numbers must be removed:

`HANDOFF.md:1352-1357`
```
## ~~THE RESULT (2026-08-01, first version)~~ — DELETED, IT WAS ALL BUG ARTIFACT

This section held an F1 table, a "MCC near chance" claim, and a channel ablation ending in an instruction to delete a channel. **Every number in it came from the broken loader and was ranked on F1.** The numbers and the instruction have been REMOVED rather than quoted-and-annotated, because a reviewer found the annotated version still being followed and `grep` still returned the instruction. Under the repaired loader and MCC ranking that ablation row is *vacuous* anyway — it is bit-identical to `full`.

Two general lessons, both earned the expensive way:
- **A superseded number left in a doc is an instruction, not a footnote.** Delete it.
```

Repeated at `HANDOFF.md:1382-1386` and `HANDOFF.md:1425-1426`. **Conflict to warn the translator about:** `:292-294` says "nothing was silently deleted"; `:1352`, `:1380`, `:1420` say content *was* deleted with only a stub left. Both are true of different parts of the same file.

**(d) The publication redaction convention — `[operational; redacted]`.** Introduced by one commit (see §8). Only three instances exist, all in `ITERATION_NOTES.md`.

### 1.2 Complete marker inventory — `BP/ITERATION_NOTES.md`

| line | verbatim marker text |
|---|---|
| 16 | `voided (rule: prompts ONLY from committed packet files, never retyped).` |
| 44 | `- RUNBOOK ERRATUM (first command, first failure): STEP 1's` |
| 71 | `## 0002 — BUDGET RULING (2026-08-24) — [operational; redacted]` |
| 81-82 | `.json — supersedes single-wave entries FOR REPAIR ROUTING ONLY; the` / `attempt-1 transfer claim (0.40, F2) stays frozen.` |
| 129 | `- RUNBOOK ERRATUM (STEP 4): nothing documents how attempt-1 wave items` |
| 209 | `tripwire >1 disagreement voids the Opus wave.` |
| 234 | `## 0008 — FINAL-BLOCK BUDGET CHECKPOINT (2026-08-24) — [operational; redacted]` |
| 249 | `registration is invalid-by-construction.` |
| 261 | `registered revert; (b) rule the P1 realization void-for-coverage and` |
| 284-289 | `- TRUTH-INSTABILITY FINDING (do not let dict order hide it): / l3239_3382_n005 carries two OPPOSING unanimous Fable panels …` |
| 310-311 | `RUNBOOK RULE CANDIDATE: check every truth supersession for / the opposing-unanimous pattern before letting recency precedence decide.` |
| 315 | `- Queue refiltered against the CURRENT module first (lesson: never route / a stale miss list)` |
| 337 | `RULING: the final-iteration-on-Fable overlay is rescinded (for now).` |
| 341 | `DRIVER ERRATUM banked for the runbook` |
| 356-359 | `Response was mechanical: quarantine / the 43 dispute resolutions (assembly's own rule) …` |
| 367 | `notes 0001-0014 now carrying FOUR banked errata.` |
| 418 | `RUNBOOK ERRATUM #13: verify` |
| 424 | `## 0018 — USER-AUTONOMY ATTEMPT-1 (PROVISIONAL) + ERRATUM #14, 2026-08-24` |
| 425-427 | `PROVISIONAL result: / engaged precision 0.60 … clause (c) holds provisionally` |
| 430 | `ERRATUM #14 (runbook):` |
| 434 | `- Scoring stands PROVISIONAL pending post-reset Fable verification:` |
| 438-440 | `- Q1 DATA POINT: this fresh run produced one new erratum — the process / layer is STILL amending (errata series 4,4,4,2*,1 …)` |
| 445 | `## 0019 — TRUTH ECONOMICS RULING (Matt) + ERRATUM #15, 2026-08-24` |
| 453 | `ERRATUM #15: the prereg's` |
| 479 | `the errata series is NOT converged; manual driving remains correct.` |
| 481 | `## 0021 — ENVELOPE + PLAN-V2 DISPATCH (2026-08-24) — [operational; redacted]` |
| 534 | `(batch sized on stale per-seat costs); logged, not hidden.` |
| 541-543 | `## 0025 — ERRATUM #16 (stale reset belief) + CONTINUE RULING, 2026-08-24 / The reset I had been scheduling against had already passed; I carried / the stale anchor forward through several plans. ERRATUM #16` |
| 569-570 | `— DISCLOSED; the cost-estimation erratum is now twice repeated: #17, / fix the model before the next sizing.` |
| 577 | `ERRATUM #18: measure shelf data sources'` |
| 694 | `- Errata: #19 (my coding vocabulary under-specified …` |
| 739 | `## 0037 — ERRATUM #20: CLOSED-VOCABULARY CIRCULARITY (Matt's suspicion, upheld), 2026-08-25` |
| 749-751 | `RULE: saturation studies with closed / vocabularies measure vocabulary coverage, never space completeness` |
| 772 | `- Errata this arc: designer-vocabulary smuggling caught THREE times` |
| 832 | `## 0042 — 0041 WITHDRAWN: THE INTEGRATION CENSUS FAILS ITS ADVERSARIAL REVIEW, 2026-08-25` |
| 855 | `pass condition satisfiable by noise is void as registered.` |
| 861-864 | `Erratum #21: the third instance this / session of a pass condition that could not fail …` |
| 866 | `## 0043 — L1/L2 THEMSELVES FAIL REVIEW: DOES-NOT-LICENSE, 2026-08-25` |
| 875-876 | `not even significant — a pass condition that cannot fail, erratum / #21's FOURTH recurrence, this time authored in the same document / that adopted the null-model rule` |

**Errata are a numbered series running #13→#21** (plus unnumbered "RUNBOOK ERRATUM", "DRIVER ERRATUM", and E1–E4 in `ROUND4_PREREG.md`). The series is explicitly declared *not converged* (`:479`).

**Key withdrawal chain to warn about:** 0041 ("INTEGRATION TEST PASSES") → withdrawn by 0042 → 0042's replacement experiments L1/L2 → withdrawn by 0043. A reader who stops at 0041 gets the opposite of the record's conclusion.

### 1.3 Complete marker inventory — `BP/HANDOFF_CURRENT.md`

| line | verbatim |
|---|---|
| 1 | `# ⭐⭐ ENTRY POINT (2026-08-25 end; INTEGRATION CLAIMS WITHDRAWN BY REVIEW)` |
| 3-5 | `HEADLINE: the adversarial review of the retranslation / integration census (RETRANS_REVIEW_DISPOSITION.md — read it before / citing any census number) returned P1/P2 UNSUPPORTED` |
| 12-13 | `What survives: 39/39 blind coverage / with ZERO new coinages, mid reuse 0.57 — necessary conditions only.` |
| 16-18 | `L1/L2 were then THEMSELVES reviewed and WITHDRAWN / (DOES-NOT-LICENSE; L1L2_ADVERSARIAL_REVIEW.md + disposition, notes / 0043)` |
| 45 | `consensus = per-field intersection, actor disagreement voids claim.` |
| 72-78 | `## Terminality language (READ THIS FIRST — 9g-addendum) / Every "TERMINAL" verdict in this repo is RELATIVE to a frozen mechanism inventory / and EXPIRES when vocabulary/declarations grow. … Do not treat any node as unfixable-forever` |
| 106-108 | `- CRITERION STANDING (in-sample, all-truth): caution 0.941, harm 0.953, help / 0.960 under match-or-adjudicated-defensible; raw match 0.81-0.85; the / human-panelist baseline 71%. NOT yet certified — that is round-4's job.` |
| 201-203 | `- Round-3 prereg (signed, sha 69631bf3...) is SUPERSEDED unrun: it froze / contract v13; the instrument has moved to v18. Round-4 needs a fresh / prereg re-derived from v18 all-truth.` |
| 210-211 | `- The handoff's "the human-panelist baseline 71%" currently has NO source / artifact; it must be sourced or struck before it appears in any writeup.` |
| 213 | `Arc1-b mint CLOSED (adversarial CLEAR-WITH-NITS, 2 rounds: M1 held, M2 held 3/3, errata addendum 5)` |

**Self-contradiction inside this file:** line 108 says the 71% baseline *is* the human-panelist baseline; line 210-211 says it "has NO source artifact; it must be sourced or struck". Both stand in the current file. It was struck in the generalization prereg (`GENERALIZATION_PREREG_DRAFT.md:81-84`) but not here.

### 1.4 Complete marker inventory — `semi-formal-experiment/HANDOFF.md`

Chronologically **inverted** file: newest state at top, history below, ~1,500 lines. Every marker:

| line | verbatim |
|---|---|
| 45 | `Those numbers stand; they are simply no longer the bar.` |
| 96 | `**UNREVIEWED**; do not cite as settled, and do not iterate it (fitting hazard, named there).` |
| 97 | `* Design: `HARNESS_REDESIGN.md`. Supersedes `RELATIONAL_PAPER_ENCODING.md`.` |
| 101 | `This section supersedes the 2026-08-04-LATE section below for WHAT IS CURRENT.` |
| 119-129 | `⚠️ **CORRECTED 2026-08-05.** This paragraph previously named `backfill_author.md` "for the attribution seat", and said "the seat briefs are in place; the build is ready". Both were wrong.` |
| 133-136 | `This section supersedes the one below it … where the two disagree about *what has been executed*, this section wins.` |
| 204-205 | `S3's revert withdraws the three / `behaviours_query.json` declarations; the code stays.` |
| 213-214 | `Its own report flags three of its design's predictions as **refuted by measurement** — read them before merging.` |
| 224-228 | `⛔ `SECTION_PRIOR_DESIGN.md` §5 says "cycle-4 config if cycle 5 reverts"; that parenthetical is **STALE and wrong**` |
| 233-235 | `**F6's worry that S1's join would void this pre-registration did NOT materialize.** … Do not discard the pre-registration as stale.` |
| 292-297 | `Everything below this section is history … in several named places **superseded** (each such place now carries a ⛔/⚠️ marker pointing back here — nothing was silently deleted).` |
| 322-323 | `KEEP. Superseded by v1; v0's / overlay bytes no longer exist on disk (in-place-edit lesson).` |
| 446-463 | `### What this supersedes below (each site is also marked in place)` — 6 named supersessions (plan of record; preferred artifacts; nested/held-out threshold selection; test count; `section@any_atom`; the old recommendation) |
| 469 | `> ## ⛔ READ FIRST — EVERY PREVIOUSLY PUBLISHED NUMBER IN THIS FILE IS WRONG` |
| 504 | `## ⚠️ MUTATION TESTING IN THIS REPO CAN LIE TO YOU — clear the bytecode cache` |
| 535-540 | `**⇒ ⛔ SUPERSEDED 2026-08-04: `LADDER_PLAN.md` is no longer the plan of record.** … kept as the 2026-08-02 state it was: ~~FOR CURRENT STATE AND THE ACTIVE PLAN, READ `LADDER_PLAN.md`. It is the agreed plan of record (2026-08-02)~~` |
| 586 | `## The floors — see the banner; the table that was here is superseded` |
| 621-625 | `## THE STRUCTURAL RESULT — the earlier NULL WAS WRONG. Retracted. … **Both statements are retracted.**` |
| 646 | `**a significant result was overridden by an obsolete constant.**` |
| 705 | `## ⛔ THE DIAGNOSIS WAS WRONG. IT IS THE QUERY MECHANISM. DO NOT BUY ANNOTATION.` |
| 726 | `### Where the retracted +0.258 came from` |
| 775 | `## ⛔ THE LABEL-FREE LEADS ARE CLOSED (two by proof, a third measured).` |
| 781 | `### Lead 3 … ⚠️ UNREVIEWED.` |
| 823-825 | `**Do not iterate this.** Sweeping embedding families/k/scorer forms until MCC rises is the withdrawn `rho` lead one level out.` |
| 867-868 | `The +0.278 → +0.591 gap should no longer be assumed recoverable` |
| 927 | `**⚠️ THE SCORE-1 TRUNCATION INFLATES THE JUDGES BY ~+0.089 MCC.**` |
| 1007-1018 | `### ~~THE ONE LEAD LEFT~~ — WITHDRAWN, it was a fitting vector … the recurring failure mode of this project is a fitting-shaped sentence surviving in prose until it becomes the plan of record.` |
| 1038 | `## ⛔ `act_match` DOES NOT TRANSFER — structural's +0.310 was a 3-behaviour number` |
| 1090 | `## ⚠️ The noise floor is 0.035–0.037, not 0.0295` |
| 1095-1104 | `## ⛔ THE CONTRACT-COMPLIANT MODULE IS WORSE THAN THE ONE IT REPLACES` + `> **⛔⛔ THIS SECTION IS RETRACTED. Read the retraction 84 lines below … a reader who stops at this heading leaves with the opposite of the conclusion, which is exactly what happened for three cycles.** ` |
| 1188 | `## ⛔⛔ RETRACTED: "THE COMPLIANT MODULE IS WORSE". It was an `act_match` artifact.` |
| 1229 | `### 5. RETRACTED: "the gain is the partition, not the extra prediction mass"` |
| 1241 | `### 7. ⚠️ `combined.MEASURED` and `section.MEASURED` ARE HAND-TRANSCRIBED CONSTANTS` |
| 1259-1264 | `> **⚠️ FLAGGED UNRECONCILED (2026-08-04).** … No recorded decision reverses this paragraph; the two simply have not been reconciled.` |
| 1275-1276 | `The published-universe bar 0.764/0.780/0.500 is superseded and must not be quoted.` |
| 1280-1282 | `> ⚠️ Count superseded 2026-08-04: the suite is now ~1,960 tests` |
| 1352 | `## ~~THE RESULT (2026-08-01, first version)~~ — DELETED, IT WAS ALL BUG ARTIFACT` |
| 1361-1367 | `## Update — full-coverage artifact ~~(use these, not the originals)~~` + `> ⚠️ SUPERSEDED AGAIN 2026-08-04` |
| 1374 | `### ⚠️ Every ablation number recorded before 2026-08-01 12:18 is void` |
| 1380 | `### ~~Current headline~~ — DELETED (published universe, superseded)` |
| 1388 | `### ⚠️ The `section_path` fix was a CALIBRATION fix, not a recovery` |
| 1420-1426 | `### (deleted) "the section signal is unexploited" … It is deleted here rather than annotated` |
| 1431-1432 | `> ⚠️ STALE (2026-08-04): this section describes the 2026-08-02 state.` |
| 1442-1458 | five `~~struck~~` numbered next-actions; item 5 `**SUPERSEDED 2026-08-04**` |
| 1461-1468 | `### Deleted from this list, deliberately — do not reinstate … which is precisely how a retracted reframe becomes the plan of record.` |

The record's own diagnosis of why this matters (`HANDOFF.md:1102-1104`): *"a reader who stops at this heading leaves with the opposite of the conclusion, which is exactly what happened for three cycles."*

---

## 2. Opposing panel rulings on the same node

### 2.1 Representation mechanisms

The record has **four** distinct mechanisms for disagreement. A translator must not conflate them.

**(i) Consensus-by-intersection with a dispute list** (`BP/arb_marks_consensus.json`). Schema:

| key | type | value |
|---|---|---|
| `_` | str | provenance/rule prose |
| `inter_seat_agreement` | float | `0.944` |
| `marks` | dict, 260 entries | `node_id → "yes"` |
| `no` | dict, 459 entries | `node_id → true` |
| `disputes` | list, 43 entries | bare node ids |

`BP/arb_marks_consensus.json:2` (the `_` field), verbatim:
```
MINT-ARB corpus consensus (two blind Opus seats per chunk, frozen signed criteria). Consensus = seat agreement; disagreements -> escalation queue (unresolved nodes carry NO mark until escalated — fail-conservative for the additive channel, fail-open for the wall is NOT allowed: disputed nodes are excluded from BOTH channels until resolved... see assembly rule in ITERATION_NOTES 0013).
```

**(ii) Majority folding.** Commit `b8ac6498` (2026-08-24): `"Final marks layer (283, dispute panel majorities folded, 9/43 splits)"` — the 43 disputes were resolved by 3-seat Opus panel majority, yielding 283 marks.

**(iii) Quarantine — reversal of a folded majority when a tripwire fires.**

`BP/ITER3_ATTEMPT4_SCORED.json:190`
```
Appended post-scoring, registered numbers above untouched: the dispute spot-check tripwire fired (4/9) -> all 43 dispute-panel mark resolutions quarantined per the assembly rule (arb_marks_final.json r2). Under the quarantined instrument the drawn engaged set loses only l3596_3876_n039 (fresh verdict not_relevant): quarantine-adjusted engaged precision 17/19 = 0.895; P3 move gate 10/12 (still PASS). The channel adoption is validated on BOTH the as-measured and quarantined views; the quarantine is itself charter-positive (removes measured FPs, breaks nothing ruled).
```

`BP/ITERATION_NOTES.md:353-362`
```
- TRIPWIRE WORKED AS DESIGNED (blog material): the dispute-class
  spot-check fired (4/9) — the Opus certificate measurably does NOT
  cover the boundary-item annotation sliver, exactly the population
  2-seat disagreement selects for. Response was mechanical: quarantine
  the 43 dispute resolutions (assembly's own rule), marks 283->260,
  engagement 393->384; the only measured affected node was a fresh FP,
  so the quarantine RAISED the adjusted precision to 0.895 and P3 holds
  at 10/12. Lesson for certificates: measure parity ON THE DISPUTE
  CLASS separately before letting a cheap tier resolve escalations —
  consensus items and boundary items are different tasks.
```

**(iv) Quarantine closure by a higher tier** (`BP/arb_marks_final.json`). Schema: `_` (str), `n_marked` (int, 269), `marks` (dict, 269 entries `node_id → "yes"`), `dispute_resolutions_fable` (dict, 43 entries `node_id → "yes"|"no"`).

`BP/arb_marks_final.json:2`
```
ARBITRATES marks, FINAL r3 (2026-08-24): the 43 quarantined disputes RESOLVED at the trusted tier (one fresh Fable seat per the reviewed plan-v2, unbundled) — 9 yes / 34 no, vs the voided Opus-panel resolutions' 23 yes (the boundary-class permissiveness gap measured again, same direction as the UA gate). Marks = 260 consensus + 9 Fable-resolved = 269. Suspensions cleared; quarantine closed.
```

So the same 43 nodes carry **three incompatible resolutions in the record**: 2-seat Opus disagreement (unmarked), 3-seat Opus panel (23 yes), and 1-seat Fable (9 yes). Only the last is `final`.

**(v) Per-seat ruling files.** Schema for `BP/panel_run1/fresh_draw4/*_rulings.json`: `{"rulings": {node_id: {"verdict": "relevant"|"not_relevant", "grounds": str}}}`. For ARB dispute files: `{"annotations": {node_id: {"mark": "yes"|"no", "grounds": str}}}`.

**(vi) Defensible-by-contradiction.** The record's rule for what to *do* with opposing unanimous panels:

`BP/ITERATION_NOTES.md:299-311`
```
## 0011 — MATT RULING: DEFENSIBLE-BY-CONTRADICTION, 2026-08-24
Matt's ruling on the n005 flag: opposing UNANIMOUS panels on identical
text/brief = the node is defensible either way and must not hit the
top-line — score it match-or-defensible, the campaign's standing metric
shape. MECHANIZED AS A ZERO-COST RULE: the contradiction IS the
defensibility certificate (no seat, no panel-of-record needed — that
queued item is closed by this ruling). Qualification bar: two full
panels, both unanimous, opposed. l3239_3382_n005 qualifies;
l3877_3953_n002 (2-1 panel vs wave) does NOT and stays contested.
Applied append-only to ITER2_REMEASURE_SCORED.json: pooled
match-or-defensible engaged = 24/38 = 0.632; registered final numbers
untouched. RUNBOOK RULE CANDIDATE: check every truth supersession for
the opposing-unanimous pattern before letting recency precedence decide.
```

### 2.2 Concrete example — node `l3239_3382_n005`

Claim under judgment (`BP/panel_run1/fresh_draw4/iter1_tradeoffs_escalation_panel.json`, item 0): *"When producing output that will be consumed programmatically, the assistant should just follow transformation instructions without comment."* Behaviour: `how-to-approach-tradeoffs`.

This one node carries **eight recorded rulings across six venues, in both directions**:

| venue | file | verdict |
|---|---|---|
| single wave seat (attempt-1) | `BP/panel_run1/fresh_draw4/gen_how-to-approach-tradeoffs_wave_rulings.json` | `not_relevant` |
| iter-1 escalation panel A | `.../iter1_tradeoffs_escalation_panel_A_rulings.json` | `relevant` |
| iter-1 escalation panel B | `.../iter1_tradeoffs_escalation_panel_B_rulings.json` | `relevant` |
| iter-1 escalation panel C | `.../iter1_tradeoffs_escalation_panel_C_rulings.json` | `relevant` |
| Opus parity A/B/C | `.../iter1_parity_opus_{A,B,C}_rulings.json` | `relevant` ×3 |
| attempt-3 panel A | `.../iter2_attempt3_panel_A_rulings.json` | `not_relevant` |
| attempt-3 panel B | `.../iter2_attempt3_panel_B_rulings.json` | `not_relevant` |
| attempt-3 panel C | `.../iter2_attempt3_panel_C_rulings.json` | `not_relevant` |
| attempt-3 wave | `.../iter2_attempt3_wave_rulings.json` | `not_relevant` |

Grounds, verbatim, from the two unanimous panels:

`BP/panel_run1/fresh_draw4/iter1_tradeoffs_escalation_panel_A_rulings.json` →
```
"verdict": "relevant", "grounds": "The span structures a conflict between flagging that 'changes to the text are warranted' and compliance by context — 'in an interactive setting, the assistant may want to alert the user... But when producing output that'll be consumed programmatically... just[...]"
```

`BP/panel_run1/fresh_draw4/iter2_attempt3_panel_A_rulings.json` →
```
"verdict": "not_relevant", "grounds": "The instruction that for programmatic output 'the assistant should just follow transformation instructions without comment' is formatting/task-execution guidance, not a norm about weighing conflicting values or goals."
```

The escalation result file records the supersession explicitly — `BP/panel_run1/fresh_draw4/ITER1_TRADEOFFS_ESCALATION_RESULT.json`:
```json
{"node": "l3239_3382_n005", "seat_verdicts": ["relevant","relevant","relevant"], "majority": "relevant", "split": false, "supersedes": "gen_how-to-approach-tradeoffs_wave_rulings.json (single-wave not_relevant)", "outcome": "OVERTURN -> C-T (mismatch dissolves)"}
```
…and `/truth/l3239_3382_n005 = "relevant"` in the same file — which the later attempt-3 panel contradicts 3-0.

The ledger flags this as a hazard in its own words, `BP/ITERATION_NOTES.md:284-289`:
```
- TRUTH-INSTABILITY FINDING (do not let dict order hide it):
  l3239_3382_n005 carries two OPPOSING unanimous Fable panels (iter-1
  escalation 3-0 relevant; attempt-3 panel 3-0 not_relevant). The
  scorer's recency precedence currently rules; the node needs a
  panel-of-record with the contradiction in front of it. Same watch on
  l3877_3953_n002 (2-1 R then wave NR).
```

**The same node also has opposing ARB marks**, in a different judgment task:
- `mint_arb_corpus_chunk3_X.json` → `"yes"`; `mint_arb_corpus_chunk3_Y.json` → `"no"` (2-seat disagreement → dispute)
- `mint_arb_dispute_{A,B,C}.json` → `"yes"` ×3 (unanimous Opus panel)
- `mint_arb_dispute_fable_rulings.json` → `{"mark": "no", "grounds": "'Just follow without comment' promotes the single consideration of compliance; per the in-brief hard boundary, comply-without-questioning with no two-sided resolution rule is not arbitration."}` — the Fable seat overturns the unanimous Opus panel and is the `final` value.

Across the 43 disputes, **15 nodes have an Opus-panel majority of `yes` overturned to `no` by the single Fable seat**; 22 of 43 show either an intra-Opus split or an Opus-vs-Fable reversal. Another clean instance: `l3041_3146_n014` — A/B/C all `"yes"`, Fable `{"mark": "no", "grounds": "One consideration (steerability of defaults); no two-sided resolution rule, failing clause (a)."}`.

**Also flagged in the record:** `BP/ITERATION_NOTES.md:884-886` names *"THREE incompatible relevance ledgers (node ledger 0.443-0.560 positive vs panel-v5 majority 0.008-0.114 vs rubric-v3w) with L1 naming none — truth-shopping surface"*.

---

## 3. In-sample vs fresh-draw certification

*(The dedicated agent for this item was still running at report time; the following is from my own direct reading of the prereg set.)*

### 3.1 Definitions

`BP/ROUND4_PREREG.md:12-17` — the core distinction:
```
## What round 4 certifies
The three dev behaviours (helpfulness, harm-avoidance-to-third-parties,
avoiding-over-and-under-caution) on the Model Spec corpus, under the FROZEN
post-9b instrument, on nodes NEVER before ruled — converting the in-sample
criterion standing (0.94-0.96 match-or-adjudicated-defensible) into a
certified out-of-sample claim. Scored ONCE.
```

`BP/HANDOFF_CURRENT.md:106-108`
```
- CRITERION STANDING (in-sample, all-truth): caution 0.941, harm 0.953, help
  0.960 under match-or-adjudicated-defensible; raw match 0.81-0.85; the
  human-panelist baseline 71%. NOT yet certified — that is round-4's job.
```

`BP/HANDOFF_CURRENT.md:132-134`
```
 f. ROUND-4 CERTIFICATION (post reset): frozen instrument, fresh
    draws, 9e fresh-pool bands, prospective bucket assignment. This is what
    converts 0.94-0.96 in-sample into the certified claim.
```

`BP/FRESH_DRAW_PREREG_DRAFT.md:3-6` — what makes a draw "fresh":
```
Purpose: certify the project owner's gate ("the 3 behaviors all match
perfectly or have valid explanations") with an honest number from the FIXED instrument on
nodes it has never been tuned or adjudicated against. This is the measurement the next
behavior/document is gated on.
```

`BP/FRESH_DRAW_PREREG_DRAFT.md:16-22` — the pool definition:
```
Per behavior: from the never-adjudicated pool (762 corpus modules minus that behavior's
existing truth set; pools measured 605/608/637), draw a STRATIFIED sample with seed
20260819: 40 currently-ENGAGED + 40 currently-NOT-engaged nodes … Stratification is
declared here, so the headline metrics are the per-stratum rates, never a pooled
"accuracy" (the pool engagement rates — help 62%, harm 8%, caution 64% — make pooled
accuracy incomparable across behaviors and inflatable; rejected by name).
```

`BP/ROUND4_PREREG.md:20-23` — exclusion mechanised:
```
- Draws: seeded per behavior (seeds registered below), stratified 40 ENGAGED
  + 40 NOT-engaged at the frozen instrument's states; every node with ANY
  prior ruling excluded (the exclusion list is a deterministic script output
  committed with its sha: round4_freeze.py -> ROUND4_FREEZE_DERIVATION.json).
```

`BP/GENERALIZATION_PREREG_DRAFT.md:1` + `:7-14` — the third mode, zero-adaptation transfer:
```
# GENERALIZATION PRE-REGISTRATION — zero-adaptation runs on six never-consulted behaviours (DRAFT, awaits the project owner's signature)
...
## What this measures
Whether a NEW behaviour costs a fixed procedure, not another campaign. The
instrument … was built around three dev behaviours. Six behaviours it has never seen — never
consulted in any design, tuning, or adjudication decision — are run through
the same procedure, once each, with no adaptation before scoring. The
PRIMARY result is the fix ledger: what repairs are needed AFTER scoring,
classified. The score is secondary.
```

`BP/GENERALIZATION_PREREG_DRAFT.md:52-53`
```
- Instrument runs ONCE per behaviour on the frozen corpus. Zero adaptation:
  no wall tweaks, no vocabulary additions, no re-runs after looking.
```

### 3.2 The "do not report one as the other" warnings

**Transfer vs repair (the strongest, and repeatedly restated).** `BP/GENERALIZATION_PREREG_DRAFT.md:100-111`:
```
## Re-measurement protocol (attempts budget, added 2026-08-21 at the project owner's ruling)
n=40 chosen over n=60 because the binding resource is ATTEMPTS, not band
width …
- ATTEMPT 1 (zero adaptation) carries the TRANSFER verdict exclusively —
  the generalization claim. Nothing done later can change it.
- ATTEMPT 2+ exists for repairs: … the behaviour is re-measured with a fresh seeded draw + fresh
  blind rulings, labeled attempt-N. Attempt-N verdicts measure THE REPAIR,
  never transfer; writeups keep the two claims separate.
```

Applied in the ledger, `BP/ITERATION_NOTES.md:80-82`:
```
  .json — supersedes single-wave entries FOR REPAIR ROUTING ONLY; the
  attempt-1 transfer claim (0.40, F2) stays frozen.
```
and `BP/ITERATION_NOTES.md:150-151`:
```
  Also clears S1's 0.70 bar at the repair venue — reported as exactly that, never as a transfer claim.
```

**Cold-start vs tuned.** `BP/PREREG_panel_equivalence.md:116-138`:
```
* **Cold-start (arm 1, above):** what the system delivers on first contact
  — frozen blind atoms, one shot. …
* **Tuned (arm 2):** what a user reaches by iterating the behavior. … the
  behavior's adjudicated node set is split 50/50 by fixed seed (20260817,
  sorted-id order). The tuner sees verdicts-with-grounds on the TUNING half
  only. Scoring runs on the HELD-OUT half plus any new engagements the
  tuned matcher produces, judged by FRESH adjudicator instances shown
  neither the tuning history nor the tuning half's verdicts. Same
  instrument type, disjoint verdicts and instances — the tuned number
  measures reach, not memorization. …
* Reported side by side, always both, labeled: the cold-start number is
  the generalization claim, the tuned number is the expressiveness ceiling,
  and the GAP between them is the measured value of the iteration feature
  itself. Reporting the tuned number alone is forbidden by this
  registration.
```

**In-sample rates must not be used to set fresh-draw bands.** `BP/ROUND4_PREREG.md:202-206` (erratum E4):
```
   (b) mis-derived registered predictions: the
   freeze script implemented "over all-truth" literally (0.9336) where
   every actual fresh draw under the SAME judge landed 0.57-0.78 and prior
   rounds registered lineage bands (round-2 passed at 0.78 in band
   0.71-0.87) — the in-sample rate ignores the known generalization gap.
```

**Anti-Goodhart / anti-leak rules.** `BP/PREREG_panel_equivalence.md:94-96`:
```
Nothing in the matching layer may change after this
  registration is signed, and no matching parameter may be tuned against
  these numbers.
```
`BP/PREREG_panel_equivalence.md:97-105` (Q3 ruling) rejects by name *"applying the party-scope fix to the base tool before signing — legitimate in principle, but it would make the cold-start number describe a tool improved after seeing where it failed."*

`AGENTS.md:28-30`: *"**Never lower a quality floor to make a run pass.** … Scoring far *above* a floor is a **leak signature**, not a win."*

`BP/ITERATION_NOTES.md:473-474`: *"the held-out seal requirement (tuning against a fully visible key is Goodhart bait the anti-cheat perimeter already names)"*.

### 3.3 Registered bars

- `BP/ROUND4_PREREG.md:216-220`: `engaged precision band 0.71-0.87, decline-correctness band 0.61-0.77 (round-2's passed bands, the last same-judge fresh-draw measurement …); F1/F2 read against these bands.` Errata rule at `:35`: `registered numbers are never edited; corrections append.`
- `BP/GENERALIZATION_PREREG_DRAFT.md:78-84`: `S1 TRANSFER: engagement precision >= 0.70 at the 40-node draw AND fix ledger contains no FATAL entry. Basis: below the dev trio's converged standing (0.94-0.96 in-sample after a full campaign — not expected cold), anchored on the round-2 prediction lineage (0.73-0.89). (A former anchor — "the human-panelist baseline 71%" — is STRUCK 2026-08-21: no artifact establishes it and its presumed source does not recognize it; the floor stands on the prediction lineage alone.)`
- Falsifiers `F1`/`F2`/`F3` at `:85-93`; fix-ledger classes EXPECTED / ALARMING / FATAL at `:94-98`.
- `BP/BLOCK2_TRANSFER_PREDICTIONS.md:1-11`: frozen *before* any block-2 ruling exists, from `modules_contract_GENERALIZATION.json` definitions and truth-free pools; `"Corrections append, never edit. These freeze NOW regardless of when — or whether — block 2 is measured"`. Per-behaviour bands, e.g. `:26-27` — `ATTEMPT-1 ENGAGED PRECISION BAND: 0.55-0.75. Fix-ledger class: EXPECTED.`

### 3.4 Conflicts the record does not resolve

**(a) The in-sample number is stated *both* as a standing criterion and as uncertified.** `BP/HANDOFF_CURRENT.md:106-108` gives 0.941/0.953/0.960 as "CRITERION STANDING (in-sample, all-truth)" and in the same sentence says "NOT yet certified".

**(b) The measured sample series shows samples systematically misestimating the exhaustive truth** — `BP/ITERATION_NOTES.md:557-560`:
```
THE NUMBER: visible engaged precision is EXACTLY
32/122 = 0.262 (seal: 38 nodes untouched, single-use). The sample
series that pointed here: 0.60 (n=20 wave) -> 0.45 (corrected) ->
0.262 (exhaustive). NO SAMPLE WAS CLOSE.
```
This is a direct caution against reading any n=40 fresh-draw number as a population figure.

**(c) `BP/ITERATION_NOTES.md:886-889`** says the assembled truth used to score is itself composition-biased:
```
assembled truth_all() is composition-biased (positives/negatives acquired by different
processes) — score only on the ~537 single-process fresh-draw
rulings
```

**(d) Whether round-4 certification ever ran.** `BP/HANDOFF_CURRENT.md:24-26` lists `round-4 certification` under `PARKED FOR SIGN-OFF`. Commit `3f87fd40` (2026-09-01) states: *"README: certification claim corrected (raw ran to completion, defensible pass never ran)"*.

**(e) All eight prereg files were edited after signature by the publication commit — see §8.4.**

---

## 4. The three `behaviours.json` files

Five files carry the name or a variant. They are **not interchangeable** and their key vocabularies differ.

| file | bytes | top-level type | entries | counted as |
|---|---|---|---|---|
| `data/behaviours.json` | 1,082,124 | object, 3 keys | **3** | `len(json["behaviours"])` |
| `engine/panel/behaviours.json` | 10,303 | bare keyed object | **11** | `len(json)` (top-level keys) |
| `semi-formal-experiment/behaviours_query.json` | 1,367 | object, 3 keys | **3** | `len(json["behaviours"])` |
| `site/spec-reader-test/data/behaviours.json` | 356,572 | object, 2 keys | **12** | `len(json["behaviours"])` |
| `semi-formal-experiment/cycles/patient-pricing-2026-08-04/pre_change/behaviours_query.json` | 1,367 | — | 3 | byte-identical to the query file (md5 `59d1c7bc…`) |

### 4.1 Schemas

**`data/behaviours.json`** — top level `generatedFrom` (list, `['engine/panel/build_site_data.py (v3w)']`), `provenance` (dict, 8 keys), `behaviours` (list). Per entry: `['id','slug','name','definition','category','coverage']`; `coverage` → `{anthropic, openai}` → `{verdict, depth, note, verifiedDate, passages}`; passage → `{id, locator, quote, exampleBlock, role, adjacent, verdicts, score}`. Passage counts: helpfulness 197/377, harm-avoidance-to-third-parties 199/333, avoiding-over-and-under-caution 77/153. Passage ids `<spec>-<slug>-panel-<n>`. Provenance: `"panel": ["sol (gpt-5.6-sol)", "fable (claude-fable-5)", "kimi (moonshotai/Kimi-K3)"]`, `"runDate": "2026-07-30"`.

**`engine/panel/behaviours.json`** — no wrapper; the 11 top-level keys *are* the ids: `no-sycophancy, undermine-oversight, helpfulness, harmlessness-to-user, third-party-harm, proportionate-risk, tradeoffs, over-under-caution, objectivity, user-autonomy, general-welfare`. Per entry `{label, source, query, boundary}` (+ optional `title`; `general-welfare` adds `query_v2`, `note_v2`). It is **byte-identical to `data/behaviour-definitions.json`** (md5 `68fef491…`). Note the field renames: `label` not `name`, `query` not `definition`, no `id`, no `slug`.

**`semi-formal-experiment/behaviours_query.json`** — `_comment`, `_source`, `behaviours` (3). Per entry `['slug','name','definition','category']`; no `id`, **no `coverage`** — that omission is the point.

**`site/spec-reader-test/data/behaviours.json`** — same per-entry schema as `data/`, 12 slugs, a *third* naming scheme (`harmlessness-to-the-user`, `how-to-approach-tradeoffs`, `objectivity-on-contested-questions`, `proportionate-risk-mitigation`, `animal-welfare-impacts`, `general-welfare-impacts-strict`), no `provenance` block, and `name` fields ending `— DEMO` on two entries. `animal-welfare-impacts` has `name` "General welfare impacts".

### 4.2 Overlap (measured)

- `data` slugs **== ** `behaviours_query` slugs; all three `definition` strings byte-equal. The query file is the panel file minus `id` and `coverage`.
- `data` slugs ∩ `engine` keys = **{`helpfulness`} only**. But all three `data` definitions appear verbatim as some `engine` entry's `query` value. Same concepts, different keys, different field names.
- `data` slugs ⊂ `site` slugs; shared definitions byte-equal.
- `engine` ∩ `site` keys = 4: `{helpfulness, no-sycophancy, undermine-oversight, user-autonomy}`.

### 4.3 Every warning in the record (README.md excluded)

**The explicit collision warning** — `semi-formal-experiment/benchmark.py:70-78`:
```
#: THE BAR. Was an absolute path into a THIRD repo (`ai_character_index-mvp`),
#: which meant this module only worked on one machine with three checkouts
#: side by side. Now vendored at `data/behaviours.json` in this repo.
#: NOTE there are three different files named `behaviours.json` in that
#: workspace and they are NOT interchangeable: this one is the panel WITH
#: citations (377/333/153); `data/behaviour-definitions.json` is the 11-entry
#: label/definition file; `site/spec-reader-test/data/behaviours.json` is
#: panel_v2's metadata. Loading the wrong one yields empty queries and a
#: silently de-behaviourised score.
```
(Note: it names `data/behaviour-definitions.json`, not `engine/panel/behaviours.json`, for the 11-entry file. They are the same bytes.)

**The split rationale, in the data** — `semi-formal-experiment/behaviours_query.json:2`:
```
"QUERY-SIDE ONLY. Behaviour name and definition are legitimate tool inputs. The panel labels are the answer key and must never be reachable from the query path. They lived in one file, which put a leak one line away and made it invisible to every test. Split so the leak is structurally impossible, not merely forbidden. See test_no_reference_leak.py."
```
`:3` — `"_source": "derived from the panel file; definitions only"`

**The wrong-file failure mode, measured** — `semi-formal-experiment/behavior_atoms.py:7-12`:
```
the query side of that comparison did not exist: behaviour atoms were read from
`behaviours.json`, whose entries carry only category/coverage/definition/id/
name/slug. `raw.get("atoms")` was therefore ALWAYS empty, the atom channel was
always multiplied by zero, and the ontology tier could only ever contribute
clause-side bag-of-words expansion. The tool looked like an ontology and scored
like a lexical baseline.
```

**The file is a *filtered* artifact** — `semi-formal-experiment/test_structural.py:1119-1125`:
```
# ⚠️ THE EVALUATION UNIVERSE. The published `behaviours.json` is a FILTERED
# artifact: the panel graded all 589 model-spec passages in one prompt, and
# `build_site_data.keeps_citation()` then dropped every passage that scored 0.
# The published 377/333/153 are the survivors. Scoring on them silently deletes
# the true negatives every judge got right, which flatters everything and
# distorts the comparison. `panel_universe.py` OWNS the reconstruction and is
# the authority (join rate 1.000 on all six cells)
```
Restated as the banner at `semi-formal-experiment/HANDOFF.md:469-476`.

**Mechanised leak fences** — `semi-formal-experiment/test_no_reference_leak.py:91-93`:
```
#: Names that only appear when the answer key is being consulted.
FORBIDDEN = (
    "behaviours.json",      # the panel file itself
```
`:300-303` and `:367-370` allowlist `"behaviours_query.json"` for query modules. `:342-344` names the laundering path: *"`panel_universe` legitimately reads `behaviours.json` … A query module that imports it reaches the answer key while naming NONE of the original forbidden tokens"*.

**A module on the wrong side of the fence** — `semi-formal-experiment/CYCLE5_REVIEW.md:29-32`:
```
4. **Anchor check assigned to a panel-reading module (F4).**
   validate_behaviours.py opens data/behaviours.json (FORBIDDEN). House the
   patients-field license check panel-blind (patient.py or a new scanned
   validate_query.py).
```
Resolved at `semi-formal-experiment/validate_query.py:1-8` and `CYCLE5_DESIGN.md:64-71`.

**Panel-file confusion of a different pair** — `semi-formal-experiment/MODULE_MAP.md:73`:
```
| `panel_v2.py` | the 9-behaviour × 2-spec panel … **`panel_universe.py` is the 3-behaviour predecessor — do not confuse them.** Several conclusions that held at n=3 invert at n=9. |
```
`semi-formal-experiment/panel_v2.py:11-16`: *"It is **NOT a new bar.** … the frontier panel (`behaviours.json`: sol / kimi / fable / opus / kimi-k2) remains the only thing that answers it."*

**The query/panel split restated in arc 2** — `BP/panel_agreement.py:16-21`:
```
  * `match` (phase A, QUERY-SIDE): reads ONLY `behaviours_query.json`
    (definitions; built exactly so the panel labels are unreachable from the
    query path) … Never imports benchmark or touches
    data/behaviours.json. Its artifacts are written before any label loads.
```

**Registration rule** — `AGENTS.md:38-40`: *"**Registration, not documentation, fences a module.** New query-side module → `test_no_reference_leak.QUERY_MODULES`; new panel-reading module → `FORBIDDEN` … Same diff, every time."*

**Index entry** — `ARTIFACTS.md:29`: `| Panel roster | The three-behavior frontier-panel verdicts (arc-1 comparator) | data/behaviours.json | the calibration instrument |`

**Dangling reference** — `engine/panel/README.md:20`: `- build_site_data.py -- runlog -> site/llm-panel-review/data/behaviours.json.` — that path does not exist in this repo.

**Notable gap:** `semi-formal-experiment/REPO_TRAPS.md` — the file whose stated purpose is *"things a careful reader gets wrong"* (`:1-6`) — contains **no** entry for the `behaviours.json` name collision. Its only behaviour-related entry (`:16-21`) concerns `behavior_atoms.json`'s `source: "definition"` field.

---

## 5. `semantic_audit.json` / `SEMANTIC_AUDIT.md`

Both under `G2/`.

### 5.1 What they audit

`G2/SEMANTIC_AUDIT.md:1` — `# Stage-4 semantic audit — the go/no-go for the bulk run (2026-08-16)`

`G2/SEMANTIC_AUDIT.md:3-8`
```
Matt's challenge, verbatim in spirit: the panel-agreement adjudication
validated node RELEVANCE (prose), not ASP fidelity — so what is the semantic
confidence in the translations the bulk run is mass-producing? This audit is
the answer, run while chunk 0 sat in the batch queue, with the pre-declared
rule: **new-prompt cohort ≥85% faithful with no dropped obligations in the
faithful set → bulk continues; below → pause and wait for the owner.**
```

`G2/SEMANTIC_AUDIT.md:15-19`
```
Protocol: blind Fable-tier auditors, one per cohort, never shown gate
results or each other's work. Per module: read the module JSON and its span
(`prompt_user.txt`), report DROPPED / INVENTED / WRONG-POLARITY / HOLLOW
normative content with the decisive words quoted. Strict on content, lenient
on style. Raw verdicts: `semantic_audit.json`.
```

`G2/semantic_audit.json:2` — `"protocol": "blind Fable auditors, module-vs-span, 2026-08-16; rule: >=85% faithful new-prompt or pause"`

`G2/SEMANTIC_AUDIT.md:9-13` — the amendment that changes what a breach means:
```
**COUNTERSIGNED (Matt, 2026-08-16), with one amendment: a breach does not
end in a parked pause. The standing rule is investigate → verify a fix on
the failing sample → restart.** A pause is the state while the fix is being
verified, not the destination; only a fix that cannot be verified leaves the
run stopped for the owner.
```

Scope is explicitly partitioned from the relevance work — `BP/PREREG_panel_equivalence.md:145`: *"ASP fidelity (SEMANTIC_AUDIT.md owns that), contradiction detection (needs"*; `BP/report_threeway.py:19-20`: *"Scope: RELEVANCE matching only. Translation fidelity is measured in semantic_audit.json"*.

### 5.2 Schema

`semantic_audit.json` — object, 4 keys: `protocol` (str), `cohorts` (list of 16 objects), `verdict` (str), `note_on_92pct` (str).

Per cohort: `cohort` (str, 16/16), `faithful` (int, 16/16), `defective` (list[str] module ids, 16/16), `total` (int, 14/16), `verdict` (str, 14/16), `audits_note` (str, 1/16). The two earliest cohorts lack both `total` and `verdict`.

Representative entry, `G2/semantic_audit.json:71-81`:
```json
{
 "cohort": "bulk-chunk-02 (first chunk under the fully amended prompt; assert-bearing stratum)",
 "faithful": 3,
 "total": 6,
 "defective": ["l1707_1973_n009","l1974_2125_n002","l2126_2404_n003"],
 "verdict": "Below the 85% floor on the hard stratum, BUT the fix-loop classes are GONE …"
}
```

### 5.3 Counts

16 cohort records. Sum `faithful` = 67; sum `len(defective)` = 42 (33 unique ids, 5 repeat); sum `total` where present = 89 over 14 records; 6 records have `defective == []`; 6 verdicts contain `EMPTY`. Cohort families: `bulk` 6, `frontier` 6, `fixloop` 2, `new` 1, `old` 1. Repeated defective ids: `l171_426_n022` ×3, `l461_608_n008` ×3, `l461_608_n012` ×3, `l609_698_n002` ×3, `l797_830_n006` ×2.

Per-cohort: new-prompt-redraws 12/1, old-prompt 5/2, bulk-chunk-00 5/10 (of 15), fixloop-verification 7/5 (12), fixloop-iteration-2 0/5 (5), frontier-repair-verification 8/0 (8), bulk-chunk-02 3/3 (6), frontier-repair-2 3/0 (3), bulk-chunk-03 2/4 (6), frontier-repair-3 4/0 (4), bulk-chunk-04 3/3 (6), frontier-repair-4 3/0 (3), bulk-chunk-05 1/5 (6), frontier-repair-5 5/0 (5), bulk-chunk-06 2/4 (6), frontier-repair-6 4/0 (4).

Markdown table, `G2/SEMANTIC_AUDIT.md:23-26`:
```
| cohort | faithful | defective | rate |
| **new-prompt redraws** (run 20260816-221213 — what the bulk run replicates) | 12 | 1 | **92.3%** |
| old-prompt sample (pre-ruling drafts) | 5 | 2 | 71% |
```

### 5.4 Verdict text

`G2/semantic_audit.json:166` — `"verdict": "CONTINUE"`

`G2/SEMANTIC_AUDIT.md:28-29`
```
**Verdict: CONTINUE.** 92.3% clears the 85% floor; the corrected prompt
cohort beats the old baseline; the bulk run was not paused.
```

`G2/SEMANTIC_AUDIT.md:44-51`
```
⭐ **Two of three defects are the same mechanism: an "only"/exclusivity
clause encoded as its inclusion with the exclusion dropped or inverted.**
This is now a named candidate class for the review-list fold and for a
mechanical check (a span containing "only"/"solely"/"exclusively" whose
module has no forbid, no cnpa closure, and no forbid_body is a cheap
attention flag — untested, follow the graveyard discipline before trusting
it). The battery's prediction that consistent deletion evades the mechanical
gate is confirmed on real traffic: all three defects passed every check.
```

Per-cohort verdicts of note:
- `:36` — `"FLOOR BREACH (33% < 85%) — D1 loop entered 2026-08-17: chunks 2-6 held, fix package committed (FM18-20, PROVIDES contract 4, literal-diff repair feedback), verification redraw of 12 addressable failures in flight"`
- `:49` — `"PARTIAL: modal downgrades, unless-negation, until-conditions, PROVIDES-definition, declaration-freezes all FIXED; three classes persist"`
- `:62` — `"FAILED: refusal-inversion recurred a 3rd time; condition-voiding derivations recurred THROUGH the failure-mode entry naming them. These classes resist prompt instruction at this tier; detection checks added to corpus_gate instead (refusal_inverted / rebranding_derivation / readback_status_conflict: 10/23 known defects caught, 2/12 faithful false-flagged)"`
- `:163` — `"4/4 VERIFIED FIRST-PASS … Chunk-6 cohort seals 6/6. ALL SIX BULK CHUNKS SEALED. Known-defect set: EMPTY."`

### 5.5 Caveats — the top-line verdict is disputed by its own file

`G2/semantic_audit.json:167`, the decisive caveat:
```
"note_on_92pct": "the 92.3% new-prompt figure came from the 14-redraw cohort, which was biased toward simple structural/heading nodes; chunk 0 shows complex conditional/agentic clauses run far lower. Quote the per-cohort numbers, never a single rate."
```

**The `.md` file was never updated.** `SEMANTIC_AUDIT.md` records only the 2026-08-16 cohorts and the `CONTINUE` verdict; the 14 later cohorts — including the chunk-0 `FLOOR BREACH` at 33% — exist only in the JSON. Git confirms the caveat was retrofitted: commit `01234e3a` — `"record chunk-0 floor breach in semantic_audit.json; caveat the 92% as cohort-biased"`, after `71b100a8` — `"stage-4 semantic audit: new-prompt cohort 92.3% faithful — bulk run CONTINUES"`.

Also: `SEMANTIC_AUDIT.md:25` reports 12/13 = 92.3%; `semantic_audit.json:167` calls it "the 14-redraw cohort".

Sharpest external dispute, `G2/DECISION_NEEDED_bulk_restart.md:12-14`:
```
* Chunk 0's blind audit breached the floor: **5/15 faithful (33%)** —
  the earlier 92% was cohort bias (simple structural nodes); complex
  conditional/agentic clauses are where DeepSeek breaks.
```
and `:36-41` states the unbounded residual:
```
checks, flagged modules frontier-repaired … Accepts a
residual UNDETECTED defect rate on hard clauses — best estimate 10–25% of
the read-required classes on conditional/agentic nodes, concentrated where
the audit found them. Full coverage removes the equivalence prereg's
structural ceiling.
```

Open unresolved auditor-consistency items: `semantic_audit.json:117` (`OPEN BRIEF-CONSISTENCY ITEM … two auditor instances split on should->oblige for positive acts … per the working rules, divergence on the same brief is a seat defect.`) and `:144`.

Neither file contains the words "provisional", "superseded", or "do not cite". The nearest equivalent is `"Quote the per-cohort numbers, never a single rate."`

Downstream: `G2/RUNTIME_WATCH.md:12-25` makes the audit the per-chunk runtime gate; `:64-74` calls the sample *"unchanged, and still the authority"*; `G2/cheap_alarm_probe.py:7-8` uses the 20 audited modules as *"the first labeled set this project has had for the purpose"* — with the outcome `RUNTIME_WATCH.md:76`: `### Layer 1 verdict (2026-08-17): NOT DEPLOYED`.

---

## 6. Git conventions

### (a) Totals and range

- **656 commits** reachable from HEAD (`d3-worked-example`).
- Author and commit dates both span **2026-08-02 → 2026-09-01**.
- First: `d9d2369f 2026-08-02 12:23:40 -0700 Initial commit`. Last: `48e66ce0 2026-09-01 17:44:18 -0700 README: publication links and CI badge filled`.
- 1 merge commit: `92ed8832 Merge pull request #3 from MattStults/guardrails-fixes`.
- Branch tips: `d3-worked-example == origin/main == public/main == 48e66ce0`; local `main` is at `6d8e65a4`, **3 commits behind**. Two remotes: `origin` → `…-private.git`, `public` → `…-public` repo. HEAD is not on `main` — a translator running `git log main` gets a different history than `git log`.

### (b) Trailer conventions

Two trailer keys are systematic: `Co-Authored-By:` (579 lines) and `Claude-Session:` (361 lines, of the form `https://claude.ai/code/session_<id>`). A further 41 lines use the lowercase `Co-authored-by:`.

**620 of 656 commits (94.5%) carry exactly one co-author trailer; 36 carry none.** Distinct model names, with counts:

| trailer value | commits |
|---|---|
| `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>` | 460 |
| `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>` | 104 |
| `Co-authored-by: Qwen-Coder <qwen-coder@alibabacloud.com>` | 41 |
| `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` | 14 |
| `Co-Authored-By: Qwen Code <noreply@qwen.ai>` | 1 |
| **total** | **620** |

Hazard: `Claude Opus 5` and `Claude Opus 5 (1M context)` are two distinct trailer strings for what the prose calls "Opus"; the Qwen trailers use lowercase `by`. A naive `grep -c 'Co-Authored-By'` misses 41 commits.

Many messages also use ad-hoc colon-prefixed lines that look like trailers but are not (`resolve:` ×8, `Suite:` ×6, `walkthrough:` ×4, `README:` ×4, `HANDOFF:` ×4, `prereg:` ×3, `guard:` ×3, `Verdict:` ×2, `RULED:` ×2, and ~20 singletons). `git interpret-trailers` will pick these up.

### (c) The commit that deleted the most lines from `ITERATION_NOTES.md`

**Exactly one commit has ever deleted a line from the ledger:** `6d01415be03a62ccaafa8a2fb8ca437c9f428094`, 2026-08-31 08:23:49 -0700, author Matt Stults, `+89 / −121` on that file. Of the 45 commits that touch `ITERATION_NOTES.md`, the other 44 are pure appends — the append-only convention held 44/45 times and was broken once, by the publication commit.

Whole-commit scale: **9,352 files changed, 2,591 insertions, 4,594,986 deletions.**

Subject: `Publication prep: prune superseded evidence with manifest, redact operational plumbing, add reader-facing layer`. Body (relevant clauses):
```
- Evidence prune: 9,273 files of superseded iteration runs removed per
  graph_v2/PRUNED.md (tree-sha manifest; 2,050 load-bearing module files
  retained after test-driven restore, documented in the manifest).
- Redactions at HEAD: subscription/quota mechanics, /usage plumbing,
  verbatim conversational quotes, and private-service references removed
  across ~60 docs; API spend figures and all design/ruling attributions
  kept (published by decision). History is published unrewritten; see
  README disclosure.
...
- Committed --no-verify: the pre-commit guard hook overflows argv on
  11k staged paths; the guard itself was run by hand at this exact
  staged state and is GREEN (8/8 watched files at review points).
```

**What the diff changed in retained entries.** Three categories, all within entries that were kept:

1. **Whole entries replaced by a stub** (3 entries: 0002, 0008, 0021).
2. **Quantitative operational data stripped** — token counts, percentages, point costs, dollar figures — leaving qualitative paraphrase.
3. **Named attribution to the project owner replaced by role language** — "Matt" → "the project owner" / "the standing ruling"; verbatim quoted speech removed.

Three representative hunks, verbatim:

**Hunk 1 — entry 0002 replaced wholesale by a stub** (`@@ -73,26 +68,12 @@`):
```
-## 0002 — BUDGET RULING (Matt, 2026-08-24, transcript->artifact)
-The 12% weekly-bar cap registered in the SEED entry was already crossed
-before iteration 1 spent anything: Matt pasted /usage = 23% Fable at the
-step-1 checkpoint. STOP CONDITION fired and was surfaced, not improvised
-past. Matt's ruling: ITERATION 1 MAY SPEND UP TO 3 POINTS — next hard
-halt at 26% — and should ideally land the COMPLETE fix arc (escalation,
-moves, V1-V5, confirmation wave) inside that envelope. This supersedes
-the 12% registration for this exercise only. Checkpoint discipline
-unchanged: ask Matt to paste /usage at every checkpoint; 26% is a
-halt-and-surface line, not a soft target.
-- BUDGET PLAN registered against SEED wave economics (40-node seat
-  ~35-70k raw, cache reads 0.10x): R1 escalation 3 seats x 9 nodes
-  ~0.5-1 pt; V4 per-flip adjudication ~0.5 pt; STEP-4 fresh
-  confirmation wave ~1-1.5 pt. Orchestration stays lean; every wave is
-  preceded by a /usage checkpoint.
+## 0002 — BUDGET RULING (2026-08-24) — [operational; redacted]
```

**Hunk 2 — quantitative measurement removed from a retained entry (0024)** (`@@ -560,27 +529,26 @@`):
```
-- BUDGET DISCLOSURE: escalation seats ran ~41k vs the ~33k estimate ->
-  est ~36.4%, ~0.4pt past the 36 line. The overshoot is mine (batch
-  sized on stale per-seat costs); logged, not hidden. NO further Fable
-  this bar.
+- BUDGET DISCLOSURE: escalation seats ran over their per-seat estimate,
+  putting the batch past its registered line. The overshoot is mine
+  (batch sized on stale per-seat costs); logged, not hidden. NO further
+  frontier seats this block.
```

**Hunk 3 — verbatim owner speech and named attribution rewritten (entries 0013, 0043)** (`@@ -358,12 +334,11 @@` and `@@ -891,15 +858,15 @@`):
```
-Matt: "Let's ignore my 'final run' message for now" — the
-final-iteration-on-Fable overlay is rescinded (for now). With it gone,
+RULING: the final-iteration-on-Fable overlay is rescinded (for now). With it gone,
...
-spot-checks + tripwire. Remaining Fable this week: two spot-check seats
-(~0.6 pt from the 30% mark). DRIVER ERRATUM banked for the runbook
+spot-checks + tripwire. Remaining Fable this block: two spot-check
+seats. DRIVER ERRATUM banked for the runbook
```
```
-Matt (correctly) declined to fund a retranslation campaign on the
-0042 licensing experiments and asked whether L1/L2 would actually
-answer his questions. Clean-context Opus review (full text:
+The project owner (correctly) declined to fund a retranslation
+campaign on the 0042 licensing experiments and asked whether L1/L2
+would actually answer the standing questions. Clean-context Opus review (full text:
```

Entries edited in place by this commit but **not** stub-marked: 0000, 0003, 0004, 0005, 0006, 0007, 0009, 0010, 0012, 0013, 0014, 0015, 0016, 0017, 0018, 0019, 0020, 0022, 0023, 0024, 0025, 0026, 0032, 0033, 0034, 0035, 0038, 0040, 0043. Entry headings for 0032, 0033, 0034 were also renamed (`AFK ENVELOPE`/`AFK BLOCK CLOSE` → `CONSTRAINED-AUTONOMY BLOCK`/`AUTONOMOUS BLOCK CLOSE`).

**A factual correction was bundled in**: `HANDOFF_CURRENT.md:3` changed `0001-0042` → `0000-0043`.

### (d) Force-push / history-rewrite evidence available locally

The reflog is intact and complete: **661 entries**, `d9d2369f HEAD@{660}: branch: Created from origin/main`. Operation breakdown: `commit` 648, `reset` 6, `checkout` 5, `pull` 1, `branch` 1.

**All 6 `reset` entries are no-ops.** Each reads `reset: moving to HEAD` and I verified the sha is identical before and after in every case (HEAD@{7}/{8} both `365d68b3`; {484}/{485} both `dff232fd`; {513}/{514}/{515}/{516} all `5aeab2d6`; {541}/{542} both `2d3703bf`). No `rebase`, no `filter-branch`, no `push --force` is recorded.

**Exactly one history rewrite exists** — `HEAD@{416}: commit (amend)`. It replaced `16bbbe59f51e62b0e6d345c8d3d4741c3d5d4443` with `713f8aef91d3770db7eb6e713a530f736b144fbb`. Both share parent `06e20502`; `git diff 16bbbe59 713f8aef` is **empty** — the amend added only a message paragraph:
```
Also resolves OPEN_QUESTIONS Q-4 ("regenerate it"): dryrun.txt regenerated
alongside the ruling, the strict xfail XPASSed and blocked the commit as
designed, and is removed. test_prompt_examples now 16 passed.
```
The orphan survives: `git fsck` lists `dangling commit 16bbbe59f51e62b0e6d345c8d3d4741c3d5d4443`.

**Orphans:** 24 dangling commits, 4 dangling trees, 4 dangling blobs. Of the 24 commits, 20 are `git stash` entries (`WIP on <branch>: …`, dated 2026-08-08 → 2026-08-30), 3 are worktree/branch leftovers (`07f54688`, `b31c8ad6`, `cd809744`, `e63165de` from the index_builder / certification-followup work), and **1 is the genuine pre-amend orphan `16bbbe59`**.

The record's own claim about this is at commit `6d01415b`: *"History is published unrewritten; see README disclosure."* Local evidence is consistent with that, with the one message-only amend as the sole exception.

### (e) Withdrawal-commit conventions

There is **no fixed prefix**. Withdrawal is signalled by keyword-in-subject, in several shapes: `<thing> withdrawn:`, `WITHDRAW <thing>`, `M1 withdrawn`, `RETRACTED`, `rescinded`, `Erratum #N`, `struck`, `VOIDED`.

Keyword counts over all refs (full message, case-insensitive): `withdraw` 15, `withdrawn` 11, `retract` 4, `rescind` 1, `erratum` 23, `errata` 7, `struck` 4.

**Commits whose subject line carries the keyword** (hash + first line, truncated):

*withdraw / withdrawn (7):*
- `365d68b3` 2026-08-25 — `L1/L2 withdrawn: the licensing experiments fail their own adversarial review (DOES-NOT-LICENSE, accepted after CoVe). …`
- `bf0d4978` 2026-08-25 — `0041 withdrawn: integration census fails adversarial review (P1/P2 UNSUPPORTED) — CoVe re-derivations confirm the decisive findings …`
- `ecb2e9df` 2026-08-14 — `M1 withdrawn pending rework (census review)`
- `86a703c1` 2026-08-14 — `build policy: all fixes now, separate commits, shelve at launch; M2 ruling withdrawn`
- `0d930b4f` 2026-08-07 — `self-test: drop the check that pinned the withdrawn anonymous-variable guard`
- `3759e554` 2026-08-07 — `stage 4: the renderer is total, and the restrictions it justified are withdrawn`
- `47779d8c` 2026-08-06 — `WITHDRAW the example-asymmetry finding entirely -- the judges saw the dialogues`

*(related, reverses a withdrawal:)* `b7c663e0` 2026-08-07 — `RESTORE the anonymous-variable guard: I withdrew it on the wrong tool`

*retract (3):*
- `94c24b3d` 2026-08-21 — `mint review round-2 resolution: … A2 timing claim retracted and restated on its actual ground …`
- `2254f925` 2026-08-19 — `queued work executed: gradient claim retracted+corrected in charter …`
- `c04b80ef` 2026-08-19 — `FACTORIZATION EXPERIMENT: … 'irreducibly relational' claim RETRACTED with evidence; granularity subtype test FAILED its pre-registered bar …`

*rescind (1):*
- `a7a8ca8c` 2026-08-24 — `Notes 0013: final-run-on-Fable overlay rescinded (Matt) -> A10 Q3 venue prescription applies …`

*struck (3):*
- `ae00660f` 2026-08-24 — `Theory review + blind spot-check, mutually confirming: map corrected append-only (Hohfeld error fixed, locus attribution struck, ARB demoted from defeasibility …)`
- `12181ba0` 2026-08-22 — `generalization prereg FROZEN — signed by Matt 2026-08-21: … 71% anchor struck (no artifact; restoration only by erratum if the manual-test artifact surfaces) …`
- `999f1403` 2026-08-20 — `DEFINITIONAL LANE ADOPTED (all prereg gates pass): 3-node Fable escalation struck 2 credits/upheld 1 …`

*erratum-numbered (subject-visible; #13–#21):* `2deacf48` (#13), `e6c0c667` (#14), `10c5544c` (#15), `39df57de` (#16), `cc2e1509` (#17), `24a88ecc` (#18), `e3852aff` (#19), `1143a921` (#20), `365d68b3` (#21 4th recurrence). Plus unnumbered: `31f5da91` 2026-08-24 — `ERRATUM: criticality 'rules adopted' overclaimed …`; `2b1505bb` 2026-08-24 — `canary attempt 1 VOIDED (seat-material divergence …) + errata E1-E3`; `68504bcf`, `b5f187f1`, `ba174536`, `4a83679e`, `c3a20f2c`, `446f2b6e`, `ce87921c`, `4edd8e9a`, `b8ac6498`, `a7a8ca8c`.

**Hazard:** a keyword search over full messages returns commits whose *body*, not subject, carries the word (e.g. `9bb82bc0 Adversarial review of today's stage-3/4 work: 12 findings, 2 high`). Subject-only filtering and full-message filtering give different sets.

---

## 7. Date and ordering conventions

**Entry format.** `## NNNN — TITLE, YYYY-MM-DD` — a zero-padded 4-digit number, an em-dash, a title, and an ISO date. Two variants exist: the date is inside parentheses in the title for the three redacted stubs (`## 0002 — BUDGET RULING (2026-08-24) — [operational; redacted]`), and entry 0000's date is embedded in the title rather than appended (`## 0000 — SEED: tacit operational knowledge from the 2026-08-24 sessions`).

**Times.** No entry carries a time. `grep -cE '[0-9]{1,2}:[0-9]{2}'` over `ITERATION_NOTES.md` returns **0**. Ordering below one-day resolution is recoverable only from git.

**Date distribution.** All 44 entries (0000–0043) fall on two dates:

| date | entries | count |
|---|---|---|
| 2026-08-24 | 0000–0031 | **32** |
| 2026-08-25 | 0032–0043 | **12** |

So 32 entries share a single date. The entire 44-entry ledger covers **two calendar days**, and was authored over ~18.5 wall-clock hours (16:02 on 08-24 → 10:24 on 08-25).

**Monotonicity — entry numbers are strictly monotone with commit order.** Introducing commit for each requested entry (found by `git log -S "## NNNN — " --reverse`):

| entry | introducing commit | commit date (iso-strict) |
|---|---|---|
| 0000 | `ccb7bd18` | 2026-08-24T16:02:49-07:00 |
| 0010 | `ecfe8c4d` | 2026-08-24T18:13:54-07:00 |
| 0020 | `5e6ae279` | 2026-08-24T21:30:59-07:00 |
| 0030 | `7dbccc4c` | 2026-08-24T23:28:00-07:00 |
| 0040 | `07703f4a` | 2026-08-25T09:26:03-07:00 |
| 0043 | `365d68b3` | 2026-08-25T10:23:55-07:00 |

I checked all 44 entries, not just these six: **every one is strictly later than its predecessor**, with no ties and no inversions. The tightest gaps are 0022→0023 (21:39:45 → 21:40:53, 68 s) and 0007→0008 (17:56:26 → 17:58:08). The largest is 0034→0035 (00:22 → 08:26, ~8 h overnight).

Commit subject lines: 0000 `ccb7bd18 learning-as-artifact: ITERATION_NOTES.md append-only ledger created with the SEED entry externalizing all tacit operational knowledge from today …`; 0010 `ecfe8c4d Notes 0010: re-measurement final … l3239_3382_n005 panel-vs-panel contradiction flagged for a panel-of-record …`; 0020 `5e6ae279 ADVERSARIAL REVIEW (Opus, clean-context): BLOCKING …`; 0030 `7dbccc4c NORM_FRAME_THEORY_MAP (design tier, Matt's directive) …`; 0040 `07703f4a Notes 0040 (Matt's correction upheld): values are leaf atoms …`; 0043 `365d68b3 L1/L2 withdrawn …`.

**Hazards for a translator:**
1. The heading date is the *session* date, not the commit date, and 0000 is retrospective — its heading says "the 2026-08-24 sessions" while it was committed at 16:02 that same day summarising work that preceded it.
2. Because 32 entries share `2026-08-24`, sorting by heading date destroys the ordering. Sort by entry number, not date.
3. Entries 0002, 0008, 0021, 0032, 0033, 0034 had their **headings rewritten** on 2026-08-31; a `git log -S` on the *current* heading text still finds the original commit only because the search string is a prefix (`## NNNN — `). Searching on the full current title would find the 2026-08-31 commit instead.
4. The file's own convention line says entries are appended "dated" and "append-only"; that held for 44 of 45 commits (see §6c).

---

## 8. Redaction

### 8.1 The marker

The record has exactly **one** in-place redaction marker form, `— [operational; redacted]`, and exactly **three** instances repo-wide, all in the ledger:

| location | current text |
|---|---|
| `BP/ITERATION_NOTES.md:71` | `## 0002 — BUDGET RULING (2026-08-24) — [operational; redacted]` |
| `BP/ITERATION_NOTES.md:234` | `## 0008 — FINAL-BLOCK BUDGET CHECKPOINT (2026-08-24) — [operational; redacted]` |
| `BP/ITERATION_NOTES.md:481` | `## 0021 — ENVELOPE + PLAN-V2 DISPATCH (2026-08-24) — [operational; redacted]` |

All three were created by commit `6d01415b`.

### 8.2 Pre-redaction contents (first 5 lines of removed content each)

**`BP/ITERATION_NOTES.md:71` — entry 0002.** `git show 6d01415b^:…/ITERATION_NOTES.md`, entry 0002 heading was `## 0002 — BUDGET RULING (Matt, 2026-08-24, transcript->artifact)`; removed body:
```
The 12% weekly-bar cap registered in the SEED entry was already crossed
before iteration 1 spent anything: Matt pasted /usage = 23% Fable at the
step-1 checkpoint. STOP CONDITION fired and was surfaced, not improvised
past. Matt's ruling: ITERATION 1 MAY SPEND UP TO 3 POINTS — next hard
halt at 26% — and should ideally land the COMPLETE fix arc (escalation,
```
(14 lines removed in total; the remainder is the BUDGET PLAN sub-bullet.)

**`BP/ITERATION_NOTES.md:234` — entry 0008.** Heading was `## 0008 — FINAL-BLOCK BUDGET CHECKPOINT (Matt, 2026-08-24)`; removed body (4 lines, quoted entire):
```
/usage pasted at 27% Fable; Matt: "Please continue." — explicit
authorization for the final all-Fable block (~2 points: spot-check 3,
wave 40, 3x panel 8, probe 5), expected landing ~29%. This supersedes
the iteration-1 26% halt line for this block only.
```

**`BP/ITERATION_NOTES.md:481` — entry 0021.** Heading was `## 0021 — ENVELOPE + PLAN-V2 DISPATCH, 2026-08-24`; removed body (5 lines, quoted entire):
```
Matt: "ok do it" at 33% for the ~2.5-3pt plan-v2 -> registered envelope
3pt, halt-and-surface ~36%. Dispatching: 3 Fable key seats (24 nodes),
3 Opus seats (the 14 key nodes lacking Opus majorities), 1 fresh Fable
dispute seat (43 ARB items). Spot-check seat follows the Opus purchase;
0.5pt reserve held for one tripwire response.
```

### 8.3 The larger hazard — unmarked redactions

The three marked stubs are **not** the extent of the redaction. Commit `6d01415b` states it redacted "across ~60 docs", and it modified **53 `.md` files** (not counting deletions). Only `ITERATION_NOTES.md` received markers. Two examples of retained files silently edited:

**`BP/HANDOFF_CURRENT.md` (+24 / −26, no marker).** Sample removed lines:
```
-    (⚠️ CORRECTED 2026-08-21: this line said "post Sat-9pm reset"; Matt confirmed
-    the reset is SUNDAY 9pm PT / Aug 23 — the signed round-3 prereg record agrees.)
```
```
-MANDATE (Matt, 2026-08-21): inside one 10-hour human-attention window
-straddling the Sun-9pm-PT Fable reset (Aug 23), produce (1) round-4
+MANDATE (2026-08-21): inside one bounded human-attention window
+straddling a provider capacity reset, produce (1) round-4
```
```
-  (ROUND4_PREREG_SCAFFOLD.md); EXPERIMENTS.md campaign entries + quota
-  reconciliation (orchestration harness quota != Fable adjudication bar).
+  (ROUND4_PREREG_SCAFFOLD.md); EXPERIMENTS.md campaign entries.
```
Note the first hunk removed a pre-existing ⚠️ *correction* marker — a redaction that erased an erratum.

**`BP/ROUND4_PREREG.md` (+29 / −29, no marker).** Sample:
```
-HARD BUDGET (Matt, 2026-08-24, superseding the orchestration seat's initial
-50% proposal before it was ever committed): the experiment may consume AT
-MOST 5 additional points of the weekly Fable bar — the bar, at 7% at
-signature, HARD-CAPS AT 12%. Checked at every behaviour checkpoint and
+HARD BUDGET (project owner, 2026-08-24, superseding the orchestration seat's
+initial proposal before it was ever committed): the experiment may consume at
+most a registered additional capacity allocation, with a hard cap set at
+signature. Checked at every behaviour checkpoint and
```

Also modified with deletions and no marker: `G2/EXPERIMENTS.md` (+34/−32), `BP/GENERALIZATION_PREREG_DRAFT.md` (+24/−22), `BP/CHEAP_TIER_DRIVER_DESIGN.md` (+16/−16), plus ~48 others. Four blog drafts and `G2/run3/REPORT.md` were deleted outright (149, 127, 125, 114, 68 lines).

### 8.4 Redaction of signed pre-registrations — a self-contradiction

**All eight prereg documents were edited by the publication commit**, despite carrying freeze/signature language:

| file | +/− in `6d01415b` | occurrences of `signed`/`frozen`/`freeze` |
|---|---|---|
| `BP/ROUND4_PREREG.md` | 29/29 | 17 |
| `BP/GENERALIZATION_PREREG_DRAFT.md` | 24/22 | 11 |
| `BP/behavior_pilot_arm3_prereg_DRAFT.md` | 9/10 | 11 |
| `BP/FRESH_DRAW_ROUND3_PREREG_DRAFT.md` | 9/7 | 2 |
| `BP/FRESH_DRAW_PREREG_DRAFT.md` | 8/8 | 2 |
| `BP/FRESH_DRAW_ROUND2_PREREG_DRAFT.md` | 7/7 | 3 |
| `BP/MINT_ARBITRATES_PREREG_DRAFT.md` | 6/6 | 7 |
| `BP/ITER2_VOID_RULING_AND_REMEASURE_PREREG.md` | 1/1 | 3 |

Plus `BP/PREREG_panel_equivalence.md` and `BP/panel_run1/convergence/definitional_lane_prereg.md`.

**`BP/PREREG_panel_equivalence.md` is the sharpest case.** Its own text, `:151-157`:
```
**SIGNED 2026-08-18 (project owner).** Content sha256 at signing:
`6848fb5a489aad2935ae2759f7daf2c14265abb94ebf1ecfb99f5989e54a80f3`. Signed via the coordinator on the owner's instruction after
Q1 (defensibility metric), Q2 (21/22 spot-check calibration) and Q3
(cold-start layer scored as blind-decomposed) were each ruled and recorded
above. From this line on, the registration is FROZEN: any edit to the
sections above voids it; the matching layer may not change; scoring happens
once.
```

The publication commit edited lines **109** and **121** — both above the signature line:
```
-## Second arm (Matt's ruling, 2026-08-17): the TUNED number
+## Second arm (the project owner's ruling, 2026-08-17): the TUNED number
...
-  rounds. The tuning signal is FABLE ADJUDICATION, not the panel (Matt's
+  rounds. The tuning signal is FABLE ADJUDICATION, not the panel (the project owner's
```

**The hash sidecar no longer verifies.** `BP/PREREG_panel_equivalence.sha256` (untouched by the commit) reads:
```
6848fb5a489aad2935ae2759f7daf2c14265abb94ebf1ecfb99f5989e54a80f3  PREREG_panel_equivalence.md  (content hash at signing)
59d85be145dce84c82810fb0aa3e24cbb012a19afe4e09e372ffcbe67b20c1be  PREREG_panel_equivalence.md  (post-signature file hash)
```
Actual current hash: `135b187bf027b4e42f99f930ac1e4f86b408fbbc6f8fc362fd03f29235e17a4f`. Verified: `git show 6d01415b^:…/PREREG_panel_equivalence.md | shasum -a 256` = `59d85be1…` — the sidecar matched immediately before the publication commit and does not match after.

I state the mechanical fact and both quotes; the record does not adjudicate this anywhere.

### 8.5 A different sense of "withheld"

`withheld` appears widely but almost always means *blinding a seat*, not publication redaction — e.g. `walkthrough/paper_pipeline/phase_1/checks.py:144` (`# here would be WITHHELD from the very prompt this check exists to inform.`), `walkthrough/STEP_placement_discrimination.md:75` (`⛔ NAME WITHHELD — gloss + source sentence only`), `walkthrough/paper_pipeline/phase_1/translate.py:2787` (`f"  - ({withheld} finding(s) withheld: they come from a "`). Do not conflate with §8.1.

`specs/openai-model-spec/model_spec.md:884, 888` contain literal `[REDACTED]` tokens — these are **upstream source-document content**, not this project's redaction.

---

## 9. Overloaded terms

### "reset" — 10 senses

1. **Provider capacity / rate-limit quota reset** (dominant; the scheduling anchor for adjudication) — `BP/HANDOFF_CURRENT.md:187`: `"adjudication queues until after the next capacity reset; all"`
2. **"post-reset" as a queue/phase tag on a work item** — `BP/panel_run1/convergence/definitional_escalation_queue.json:2`: `"field-level seat disagreements for Fable escalation (post-reset); consensus layers carry only two-seat-agreed values"`
3. **Generic resource-availability reset in the state machine** — `BP/CALCULUS_RUNBOOK.md:120`: `"machine's default is — usually suspend until the resource resets), never"`
4. **`git reset`** — `walkthrough/SPEC_DRIFT_REVIEW_2026-08-07.md:413`: `` "Method: `cp -a walkthrough` to scratchpad, `readback.py` reset to `HEAD`, mutate one construct," ``
5. **Loop-variable state reset (a bug class)** — `G2/EXPERIMENTS.md:3418`: `` "F2 -- HIGH, CONFIRMED. **D3 has a hole: `prev_shape` is not reset at the" ``
6. **Spend-counter reset** — `walkthrough/paper_pipeline/phase_1/translate.py:2922`: `` "* it sets `self.spent = 0.0` on restart. Nothing here resets any spend:" ``
7. **Parser/accumulator reset at a text boundary** — `walkthrough/paper_pipeline/phase_1/eval_arms/select_category_clauses.py:126`: `"Reset at sentence boundaries: two one-item sentences in a row are not a"`
8. **Per-module reset of an accumulated set (test ceremony)** — `semi-formal-experiment/INDEX_BUILDER_REVIEW.md:75`: `` "ceremony: `driven` resets per module, so `assert len({d for d in driven}) == 3` genuinely" ``
9. **"connection reset" — network error string in fault injection** — `walkthrough/paper_pipeline/phase_1/test_ledger_hole.py:169`: `` raise OSError("connection reset") ``
10. **A remembered-but-stale reset date, as an object of error** — `BP/ITERATION_NOTES.md:541`: `"## 0025 — ERRATUM #16 (stale reset belief) + CONTINUE RULING, 2026-08-24"`

### "block" — 18 senses

1. **Prompt-message block (SYSTEM/USER), the cacheable-prefix unit** — `walkthrough/paper_pipeline/phase_1/config_arm_pre_example.json:36`: `"Concatenated in the order listed to form the SYSTEM block — which is identical for every clause and is therefore the cacheable prefix."`
2. **Pre-registered experimental block (Block 1 / Block 2)** — `BP/GENERALIZATION_PREREG_DRAFT.md:20`: `"Block 1 (probes): 1. harmlessness-to-the-user — adjacent family; the"`
3. **BLOCK2 as a frozen-prediction artifact name** — `BP/BLOCK2_TRANSFER_PREDICTIONS.md:9`: `"never edit. These freeze NOW regardless of when — or whether — block 2"`
4. **A named section of a rendered logic module (`ontology` block)** — `walkthrough/DEFERRED.md:138`: `"artifact**. Every module carries its own **ontology block** — non-deontic classification facts, each"`
5. **Worked-example block = one graph node** — `G2/RECURSE_PROMPT.md:125`: `"groupings). Each worked-example block is ONE node needing the rule it demonstrates; never"`
6. **Commentary block (source-document formatting device)** — `G2/audit/graph_stripped.json:12225`: `"reason": "Meta-commentary block marker"`
7. **`untrusted_text` block (source-document quoting container)** — `G2/node_corpus_all.json:1522`: `"We strongly advise developers to put untrusted data in `untrusted_text` blocks when available…"`
8. **Fenced code block / blockquote (markdown, citation rules)** — `specs/CITATION.md:62`: `"- any other fenced code block, blockquote, or table."`
9. **A contiguous thematic span of document text** — `G2/recurse/c212/division.json:43`: `"…and split a thematically coherent block."`
10. **Spliced block — a delimited region of a prompt sent to the model** — `semi-formal-experiment/test_annotate.py:805`: `"spliced blocks — the commentary outside the blocks may cite the word)"`
11. **Display block (math rendering; a modelled situation predicate)** — `BP/situation_proposals.json:4108`: `"A math expression is to be rendered as a display block on its own lines."`
12. **Verb: to prevent an action (commit hook)** — `walkthrough/model/REVIEW_FINDINGS.md:471`: `` "`guard.py` printed ⛔ STALE with the correct digests, and `hooks/pre-commit` is written to block a" ``
13. **"BLOCKING" as a review-finding severity class** — `semi-formal-experiment/S5_ADVERSARIAL_REVIEW.md:9`: `"**4 BLOCKING · 8 MAJOR · 5 MINOR**"`
14. **"blocker" — a named obstacle** — `walkthrough/paper_pipeline/phase_1/RUNBOOK_AUDIT.md:41`: `"### G1 — ⛔ The documented graph-node command fails out of the box (BLOCKER)"`
15. **"blocked" as recorded work-status** — `semi-formal-experiment/LADDER_PLAN.md:459`: `"### Step 4 — ⛔ BLOCKED by engineering review. Run on luna *(ceiling $5.4, not $2.78)*"`
16. **"blocked" as a modelled/derived state in the logic program** — `walkthrough/paper_pipeline/phase_1/probe_live.py:278`: `"carry glosses (Q-23). Blocked is a reported state, never a silent skip."`
17. **"blocked task" in the subject-matter vocabulary** — `BP/modules_contract_v6.json:478`: `"wasted time, wasted money, a blocked task"`
18. **Platform-level request blocking (source-document text)** — `G2/runs/ds7/root_graph.production.json:6766`: `"…such as blocking specific requests, monitoring for unusual activity…"`

Additionally, a **19th** sense appears in the ledger: a *time* block (a work session) — `BP/ITERATION_NOTES.md:499` `## 0023 — DISPUTE QUARANTINE CLOSED + BLOCK WRAP`, and `:510` `BLOCK LEDGER: 4 Fable seats spent`. Note this sense was *introduced by the redaction* in several places (`~0.5pt, next bar` → `next block`), so "block" carries redaction-substituted meaning in the current text that it did not carry historically.

A **20th**: `adria: block` as a corpus-partition label — `BP/ITERATION_NOTES.md:881`: `"the corpus's adria: block means every truth-bearing behaviour is in-corpus"`.

### "seat" — 12 senses

1. **A model-instance judgment role under a written brief (core)** — `BP/ROUND4_PREREG.md:208`: `"- Seat: LINEAGE_SEAT_INSTRUCTION.md verbatim, wave form (one blind"`
2. **A numbered stage-4 review seat (4a/4b/4c/4d) = a fixed pipeline function** — `walkthrough/OPEN_QUESTIONS.md:539`: `"## Q-3 · Stage 4's four seats need spend, and the amount is not yet estimable"`
3. **A tier-labelled seat by model capability ("cheap seats")** — `BP/TRANSLATION_CONTRACT_V2.md:94`: `"ESCALATION-BY-DISAGREEMENT: two cheap seats label every assert; agreement"`
4. **A task-specific named seat** — `semi-formal-experiment/IMPLIED_EFFECTS_DECISIONS.md:12`: `"attribution seat, the flip-adjudication seat, or the implied-effects approver."`
5. **The anchor seat — a distinguished seat in code** — `walkthrough/paper_pipeline/phase_1/seats.py:843`: `"""⭐ THE ANCHOR SEAT. Note the signature: there is NO PARAMETER through`
6. **Metonymy: `seat` as a JSON field holding the verdict** — `BP/round4_pilot_scored.json:131`: `"seat": "NOT_RELEVANT"` (different value vocabulary at `G2/parity_results_10.json:25`: `"seat": "different_concept"`)
7. **Metonymy: `seat` as the raw reply text** — `G2/splice_seat.py:148`: `"grounds": f"(fail-closed: unparseable seat reply: "`
8. **Code-artifact name component** — `walkthrough/WORK_ORDER_review_agent.md:22`: `` "`promise_repair.py`, `dispatch_core.py`, `translate_exec.py`, `splice_seat.py`," ``
9. **"seat defect" — an error-attribution category** — `BP/L1L2_ADVERSARIAL_REVIEW.md:232`: `"…the project's standing rule is that seat/frontier divergence is a *seat defect*."`
10. **Unit of work-load / verb "seating"** — `G2/instruments_review.md:58`: `"own seat-load estimate (~50–150) is consistent with seating only the queues, not"`
11. **"seated" — a pass conducted under a brief, no script** — `semi-formal-experiment/NEW_DOCUMENT_RUNBOOK.md:175`: `"- **Command:** no script — two seated judgment passes under written briefs:"`
12. **"self-grading seat" — author as own judge (conflict-of-interest role)** — `walkthrough/REVIEW_stage4_2026-08-08.md:269`: `"artifact**. Pooling the author's self-grading seat into it means a defensive or an unusually candid"`

A 13th, adjacent: **"lineage seat"** as a named venue whose certificate is scoped — `BP/LINEAGE_SEAT_INSTRUCTION.md` and `BP/ITERATION_NOTES.md:193-195` (`"Scope: lineage ruling seat, THIS brief, tradeoffs venue; re-measures on brief change"`).

### "seed" — 13 senses

1. **Seed vocabulary — canonical concept names minted by a parent and passed down the recursion** — `G2/RECURSE_PROMPT.md:39`: `"**Seed vocabulary — you are the naming authority for concepts that cross your cuts.**"`
2. **Inherited seed — an individual name carried down a subtree (losable)** — `G2/RECURSE_PROMPT.md:46`: `"so an inherited seed you drop is a name your whole subtree loses. When in doubt, carry it;"`
3. **Verb: to seed a new concept into the vocabulary** — `G2/recurse/c212/division.json:43`: `"Separating them would require seeding a new 'goal_constraint_principle' concept…"`
4. **Seed concept object in a repair plan (`seed_c`)** — `G2/promise_repair.py:1035`: `plans.append({"class": "underexport", "seed": seed_c,`
5. **Fixed literal RNG seed as a determinism contract** — `semi-formal-experiment/cut_stability.py:63`: `"#: Fixed literal seed — the whole determinism contract hangs on this being a"`
6. **Registered draw/shuffle seed for an experimental sample** — `BP/round4_helpfulness_packets.json:2`: `"Shuffle seed = draw seed (registered in ROUND4_PREREG.md); panel rows via the registered sha sampler."`
7. **"seeded N%" — a pre-committed pseudo-random spot-check subset** — `BP/DEFENSIBILITY_BATCH_PROTOCOL.md:17`: `"PROTOCOL: blind Fable adjudication, single rulings + seeded 20% three-"`
8. **Provider/decoding seed on an API envelope** — `walkthrough/paper_pipeline/phase_1/probe_runs/live-main/m0134-within.rep0.r0.raw.json:17`: `"seed": null`
9. **`PYTHONHASHSEED`** — `walkthrough/ENGINEERING_REVIEW_2026-08-07b.md:330`: `` "`ids` is a `set` of `str`, so iteration order varies with `PYTHONHASHSEED`." ``
10. **Seed atoms — starting facts of a derivation** — `walkthrough/deontic_probe/FINDINGS.md:34`: `` "E1b's full prediction set on `harm-avoidance-to-third-parties` from **three seed atoms**" ``
11. **Verb: initialize a program variable** — `semi-formal-experiment/behavior_atoms.py:767`: `"# Only a STATED polarity is remembered: seeding this with"`
12. **"definition-only seeding" — bootstrapping a vocabulary from definitions** — `semi-formal-experiment/HARNESS_REDESIGN.md:1769`: `"| **H-7** | **document-derived vocabulary** … beats definition-only seeding."`
13. **"stale seed ea" — a seed pointer that no longer locates the right leaf (error state)** — `G2/EXPERIMENTS.md:2115`: `"and the stale seed ea is dropped -- never redraw an ea leaf to"`

Additionally, entry 0000's title uses **SEED as an entry-type label** — `BP/ITERATION_NOTES.md:7`: `## 0000 — SEED: tacit operational knowledge from the 2026-08-24 sessions`.

### "venue" — 8 senses

1. **Execution venue — the harness/session a seat actually runs in (subject of formal VENUE RULINGs)** — `BP/DEFENSIBILITY_BATCH_PROTOCOL.md:90`: `"VENUE RULING (2026-08-24, on the project owner's observation that the"`
2. **Deliverability channel — a harness venue rejected by provider input inspection** — `G2/EXPERIMENTS.md:5264`: `"inspection rejected every harness venue (venue ruling + sanitization ruling"`
3. **Human-operated venue** — `BP/CAMPAIGN_REVIEW_BRIEF.md:143`: `"Post-reset (a human-operated venue executes the frontier seat; automated"`
4. **Measurement venue — the scoring configuration a number was produced under** — `BP/ITERATION1_V5_PREDICTION.json:10`: `"attempt-2 engaged_precision >= 0.55 at the venue's own scoring (wave verdicts, panel overrides where sampled)…"`
5. **A computed enum describing which seats were present** — `BP/iteration1_score_attempt2.py:53`: `venue = "wave+panel" if len(panels) == 3 else "wave-only"`
6. **A provenance field forming part of a truth key** — `BP/UA_ASYMMETRIC_CERT_REGISTRATION.json:2`: `"Truth entries carry (definition-sha, brief-version, venue) per F6ii."`
7. **A public forum for publishing (modelled domain predicate)** — `BP/situation_proposals.json:10905`: `"The action involves publishing to a public venue."`
8. **A physical event location (source-document worked-example text)** — `specs/openai-model-spec/model_spec.md:4473`: `"- Venue: Depending on your budget and vibe…"`

Two further project-internal uses worth flagging: **"repair venue"** vs **"transfer venue"** — `BP/ITERATION_NOTES.md:150-151` (`"Also clears S1's 0.70 bar at the repair venue — reported as exactly that, never as a transfer claim."`) — and **"gen-venue"** as a routing context — `BP/ITERATION_NOTES.md:122-123` (`"probe.py extended with --contract/--truth (defaults untouched) — the same gen-venue gap as route.py"`).

**No publication-venue sense (journal/conference) appears anywhere.**

### Where the record flags overloading

None of the five words is flagged by name. The overload warnings that do exist are:

- `walkthrough/resources/03_pipeline.md:1311`: `"**Atom** — ⚠️ *overloaded in this project.* Here: a predicate with its slots filled. Elsewhere in"`
- `walkthrough/model/REVIEW_FINDINGS.md:35`: `"The model asserts the normalise seat **closes** #9 (*same name, different meanings*)."`
- `walkthrough/OPEN_QUESTIONS.md:654`: `"their expectations diverge, that is **problem #9 DETECTED** — the symbol is overloaded — and today it"`
- `walkthrough/paper_pipeline/phase_1/STEP_stage4.md:745`: `"cross-**seat** mechanism would make one function mean two different things, and the tier"`
- Venue-scope confusion caught once — `BP/GEN_UA_ATTEMPT1_SCORED.json:196`: `"deploying it on the user-autonomy venue was a SCOPE STRETCH — certificates are behaviour-brief-local"`

---

## Top hazards, ranked

1. **`ITERATION_NOTES.md` declares itself append-only and is, except for one 2026-08-31 commit that rewrote 121 lines across 29 retained entries.** Every quantitative operational figure and all named-owner speech in entries 0000–0043 is post-hoc paraphrase, not the contemporaneous text.
2. **Eight signed/frozen pre-registrations were edited after signature by that same commit; `PREREG_panel_equivalence.sha256` no longer verifies**, and the file's own text says *"any edit to the sections above voids it."*
3. **Only 3 of ~53 redacted documents carry a redaction marker.** `HANDOFF_CURRENT.md` and `ROUND4_PREREG.md` were silently rewritten; one hunk removed a pre-existing ⚠️ correction notice.
4. **The two withdrawal chains (0041→0042, L1/L2→0043) invert the headline.** Both `HANDOFF.md` and `ITERATION_NOTES.md` are read top-down at the reader's peril; `HANDOFF.md:1102` records that a reader stopping at a retracted heading "leaves with the opposite of the conclusion, which is exactly what happened for three cycles."
5. **`SEMANTIC_AUDIT.md`'s `CONTINUE` / 92.3% verdict was never updated; the 33% floor breach lives only in the JSON**, whose own `note_on_92pct` says *"Quote the per-cohort numbers, never a single rate."*
6. **Four files named `behaviours.json`/`behaviours_query.json` with three incompatible slug vocabularies**; loading the wrong one produces *"a silently de-behaviourised score"* (`benchmark.py:78`), and `REPO_TRAPS.md` does not list it.
7. **In-sample (0.94–0.96) vs fresh-draw vs transfer vs repair vs cold-start vs tuned are five distinct number classes** with explicit non-interchange rules; the exhaustive UA measurement (0.60 → 0.45 → 0.262) shows samples missing the population badly.
8. **Node-level truth is not single-valued.** `l3239_3382_n005` has two opposing unanimous panels plus an ARB mark overturned by a lower-count higher-tier seat; the "final" ARB layer replaces a 3-seat Opus majority with a 1-seat Fable ruling on all 43 disputes.
9. **HEAD is `d3-worked-example`, not `main`** (local `main` is 3 behind), and there are two remotes (private/public).
10. **Five heavily overloaded terms with 8–18 senses each, none flagged by the record**; "block" in particular acquired a new sense *through* the redaction rewrite.

---

Verified. The clause is in the *first* hunk the redaction commit touched — the file declaring that edits void it was edited in 8 places.

---

# Supplement — Section 3 replaced, Section 8.4 strengthened

My Section 3 was written from my own reading while the dedicated agent was still working. Its return added substantially more, and I have spot-verified every load-bearing new citation against the files (`CHEAP_TIER_DRIVER_DESIGN.md:31-33`, `TRANSLATION_CONTRACT_V2.md:188-192`, `R4_HELP_FAILURE_HYPOTHESES.md:54-59`, `BLOCK2_TRANSFER_PREDICTIONS.md:107-111`, `GENERALIZATION_BUILD_SPEC.md:30-31` and `:53-61`, `ROUND4_PREREG.md:150-165`, `ITER2_VOID_RULING_AND_REMEASURE_PREREG.md:3-18`, `PREREG_panel_equivalence.md:4-8`) — all verbatim as reported. **Replace §3 with the following.** `BP/` = `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/`.

## 3. In-sample vs fresh-draw certification (revised)

### 3.0 The headline hazard: there are FIVE modes, not two

The brief asked about two. The record operates five distinct, non-interchangeable measurement modes, and warns separately about each pair. **A translator who models this as a binary will merge claims the record forbids merging.**

| # | mode | varies | pool |
|---|---|---|---|
| 1 | **in-sample** | nothing | the accumulated adjudicated ledger ("all-truth") |
| 2 | **fresh-draw** | new *nodes*, same behaviours | never-adjudicated pool |
| 3 | **held-out / sealed** | partition of *already-bought* truth | seeded 25–50% split, withheld |
| 4 | **generalization / transfer** | new *behaviours* | six never-consulted behaviours |
| 5 | **cross-document** | new *document* | **does not exist; not measurable** |

Mode 5 is explicitly unmeasurable — `BP/ROSETTA.md:36-40`: *"## What is NOT testable yet (deferred by ruling) / The generalization claim itself — global atoms binding meaningfully across documents with different ontologies. Needs the second document"*. And `G2/EXPERIMENTS.md:4511-4514`:
```
⚠️ **THE CAVEAT, and it is the owner's generalisation question exactly: the
regex's 8/8 is IN-SAMPLE** (widened onto these very sentences 2026-08-16)
**and the general judge's is OUT-OF-SAMPLE. That difference is real and NOT
MEASURABLE with the anchors available -- it needs a SECOND DOCUMENT.**
```

**Negative finding worth flagging: there is no glossary anywhere defining "in-sample" or "fresh draw" as terms.** Both are defined only operationally — by what a pool excludes and what a prereg registers before scoring.

### 3.1 Definitions

**The paired definition** — `BP/CHEAP_TIER_DRIVER_DESIGN.md:31-33`:
```
S-E FLOORS NEVER MOVE DOWN; every fix is validated twice: on the ledger
    (in-sample charter) AND on a fresh unscored confirmation draw
    (out-of-sample realization) before any claim is made.
```
So **in-sample = "on the ledger"**; **fresh draw = "a fresh unscored confirmation draw."**

**In-sample** — `BP/HANDOFF_CURRENT.md:106-108`: `- CRITERION STANDING (in-sample, all-truth): caution 0.941, harm 0.953, help / 0.960 under match-or-adjudicated-defensible; raw match 0.81-0.85; the / human-panelist baseline 71%. NOT yet certified — that is round-4's job.`

**Fresh draw = pool with every prior-ruled node excluded** — `BP/ROUND4_PREREG.md:20-23`: `every node with ANY / prior ruling excluded (the exclusion list is a deterministic script output / committed with its sha: round4_freeze.py -> ROUND4_FREEZE_DERIVATION.json)`. The scaffold enumerates the scope — `BP/ROUND4_PREREG_SCAFFOLD.md:22-24`: `every node / with ANY prior ruling excluded (rounds 1-3 fresh draws, convergence / adjudications, arm lanes …)`.

The pool definition **tightens across rounds** — round 1 `BP/FRESH_DRAW_PREREG_DRAFT.md:16` "never-adjudicated pool"; round 2 `BP/FRESH_DRAW_ROUND2_PREREG_DRAFT.md:23` "never-adjudicated **never-drawn** pool"; round 3 `BP/FRESH_DRAW_ROUND3_PREREG_DRAFT.md:16-17` "exclude every node with any prior ruling (pools: help 445, harm 528, caution 557)".

**The conversion statement** — `BP/ROUND4_PREREG.md:12-17` (byte-identical in the scaffold): `on nodes NEVER before ruled — converting the in-sample / criterion standing (0.94-0.96 …) into a / certified out-of-sample claim. Scored ONCE.`

**Held-out/sealed is a third thing** — `BP/UA_PLAN_REVIEW_DISPOSITION.md:11-17`: `HELD-OUT SEAL — the engaged-set purchase includes a seeded / 25% partition (~38 nodes) whose rulings are bought but SEALED / (committed encrypted-by-omission …) … Deltas are / tuned only against the visible 75%.` Its status: `BP/L1L2_ADVERSARIAL_REVIEW.md:332-333` — *"`ua_truth_sealed.json` is the repo's only genuinely held-out truth partition, is single-use, and is at risk of being spent on the wrong question."*

### 3.2 Why in-sample overstates — stated three times, with a measured number

**Contract §9e (binding)** — `BP/TRANSLATION_CONTRACT_V2.md:188-192`:
```
## 9e. Prediction bands come from FRESH-POOL evidence only (round-3 lesson): deriving
bands from all-truth measurements overstates fresh-pool performance because adjudicated
sets are engagement-favorable (measured: helpfulness all-truth precision 0.82 vs
fresh-pool 59/80=0.74; the inflated band fired F1 on an instrument performing at its
demonstrated level).
```

**The mechanism named** — `BP/R4_HELP_FAILURE_HYPOTHESES.md:54-59`:
```
## Why in-sample (0.93) missed this
The ruled truth co-evolved with the instrument: three weeks of
attention-directed fixes enriched the ruled engaged set with genuinely
relevant nodes. The residual pool is what that process never consumed —
disproportionately tone/format/policy periphery, exactly where module
breadth shows. The 0.625 raw cell is the honest price of that selection.
```

**The erratum** — `BP/ROUND4_PREREG.md:202-206`: `the in-sample rate ignores the known generalization gap.`

### 3.3 What invalidates a draw — nine distinct voiding conditions

1. **Editing the prereg after signature** — `BP/PREREG_panel_equivalence.md:4-8`: `⛔ **This measurement is scored ONCE … Nothing here may be / scored, peeked at, or partially computed before the project owner approves this document. / Editing this file after approval voids the registration.**`
2. **Seat material diverging from the ledger format** — `BP/ROUND4_PREREG.md:150-161` (E1): `VOID as a / certification measurement: seat material diverged from the format that / built the truth ledger. … The void is TOTAL (all 80 rows, not selective)`.
3. **Fabricated seat material** — `BP/ROUND4_PREREG.md:161-165`: `one replacement / dispatch was voided for FABRICATED SEAT MATERIAL (the orchestration seat / authored a passage from memory instead of the committed packet …)`.
4. **Zero coverage of the move — result-blind** — `BP/ITER2_VOID_RULING_AND_REMEASURE_PREREG.md:3-18`: `VOID FOR COVERAGE: its / estimator sampled 0 of the batch move's 16 gained nodes … Validity here is a RESULT-BLIND / property: the same ruling would void a passing 0.80 measured on the same / zero-coverage draw.`
5. **Anti-forking: no re-rolls after a void** — same file `:20-26`: `the frozen draws … are the only samples, ever … a bad number routes / surviving mismatches into the ordinary calculus queue … and never triggers another measurement.`
6. **Definition change voids memoized truth** — `BP/UA_PLAN_REVIEW_DISPOSITION.md:41-43`: `every memoized entry carries (behaviour-definition sha, seat-instruction / version, venue); a definition change voids its behaviour's entries.`
7. **Draw-machinery defects → recompute under the same seed** — `BP/GENERALIZATION_PREREG_DRAFT.md:126-134`: `all six draws / RECOMPUTED under the same registered seed (20260822) …`
8. **A hold does NOT invalidate** — `BP/FRESH_DRAW_PREREG_DRAFT.md:38-41`: `A hold is / not a protocol violation … unscored / behaviors stay unscored (no partial peeking).`
9. **Deliberate reuse of ruled nodes to avoid burning the pool** — `BP/ROUND4_PREREG.md:168-172`: `20 already-ruled helpfulness nodes (truth known; permanently excluded / from round-4 draws — zero fresh-draw burn)`.

### 3.4 Thirteen explicit "do not report one as the other" warnings

| # | rule | citation |
|---|---|---|
| W1 | `Reporting the tuned number alone is forbidden by this registration.` — cold-start IS the generalization claim | `BP/PREREG_panel_equivalence.md:134-138` |
| W2 | `Attempt-N verdicts measure THE REPAIR, never transfer; writeups keep the two claims separate.` | `BP/GENERALIZATION_PREREG_DRAFT.md:109-110` |
| W2a | applied: `reported as exactly that, never as a transfer claim` | `BP/ITERATION_NOTES.md:150-151` |
| W2b | applied: `supersedes single-wave entries FOR REPAIR ROUTING ONLY; the / attempt-1 transfer claim (0.40, F2) stays frozen` | `BP/ITERATION_NOTES.md:80-82` |
| W3 | `no block-2 result may be reported as clean transfer` | `BP/GENERALIZATION_PREREG_DRAFT.md:214-222` |
| W4 | `The / exhaustive engaged-set precision is a separate metric and never / substitutes.` | `BP/BLOCK2_TRANSFER_PREDICTIONS.md:107-111`; dup at `BP/UA_PLAN_REVIEW_DISPOSITION.md:32-38` |
| W5 | in-sample standing is `NOT yet certified` | `BP/HANDOFF_CURRENT.md:106-108` |
| W6 | in-sample rate may not set a fresh-draw band | `BP/TRANSLATION_CONTRACT_V2.md:188-192`; `BP/ROUND4_PREREG.md:202-206` |
| W7 | in-sample vs out-of-sample difference `NOT MEASURABLE with the anchors available` | `G2/EXPERIMENTS.md:4511-4514` |
| W8 | `L1 bounds *within-document* transfer only`; `Q-B cannot be answered by any experiment that does not create new out-of-corpus panel truth` | `BP/L1L2_ADVERSARIAL_REVIEW.md:112-113`, `:307` |
| W9 | `score on single-process uniform fresh-draw partitions, ~537 rulings, never the assembled truth_all() ledger` | `BP/L1L2_REVIEW_DISPOSITION.md:66-68` |
| W10 | pooled accuracy `rejected by name`; per-stratum rates are the headline | `BP/FRESH_DRAW_PREREG_DRAFT.md:19-22` |
| W11 | `RAW match is reported alongside in the same table, always … both numbers publish` | `BP/ROUND4_PREREG.md:106-113` |
| W12 | closed population must be labeled `a population figure, not a / sample` | `BP/ROUND4_PREREG.md:75-78` |
| W13 | the seal `must not enter any visible-truth path` | `BP/README.md:63-65` |

### 3.5 Seven self-conflicts

**C1 — Round-4's registered bands were derived from all-truth, against a binding contract rule forbidding exactly that.** `BP/ROUND4_PREREG.md:69-74` registers `(over all-truth at the frozen instrument)` bands (help 0.9336 etc.); `BP/TRANSLATION_CONTRACT_V2.md:188` says `Prediction bands come from FRESH-POOL evidence only`; `BP/HANDOFF_CURRENT.md:132-134` asserts round-4 used `9e fresh-pool bands`. Erratum E4 re-registers lineage bands `0.71-0.87 / 0.61-0.77` — so **`ROUND4_PREREG.md` currently contains two mutually inconsistent registered prediction sets**, the superseded one retained as `a recorded erratum`.

**C2 — "Modules freeze as built; no revision before scoring" vs three modules revised before scoring.** `BP/GENERALIZATION_BUILD_SPEC.md:30-31` vs `:33-42`: `Three builds (tradeoffs, user-autonomy, proportionate-risk) used bespoke / names and engaged nothing; all repaired 2026-08-22`. The record does **not** relabel these as attempt-2, yet reports their verdicts (e.g. tradeoffs 0.40) as attempt-1 transfer claims.

**C3 — general-welfare gate:** `measurable / only AFTER its C-V does-lane repair` (`BP/GENERALIZATION_PREREG_DRAFT.md:223-226`) vs `discharged vacuously: no repair exists to perform` (`BP/BLOCK2_TRANSFER_PREDICTIONS.md:93-99`).

**C4 — the 71% anchor:** `STRUCK 2026-08-21: no artifact / establishes it` (`BP/GENERALIZATION_PREREG_DRAFT.md:81-84`) vs still asserted at `BP/HANDOFF_CURRENT.md:108`. *(This is the same conflict I flagged in §1.3.)*

**C5 — "F1" names two unrelated things, self-declared** — `BP/GENERALIZATION_BUILD_SPEC.md:53-61`: `"F1" is overloaded in the campaign record: … the adversarial-review FINDING … while in / GENERALIZATION_PREREG_DRAFT.md "F1" names a FALSIFIER … They are unrelated.`

**C6 — the stop rule fired, then block 2 ran anyway.** `BP/GENERALIZATION_PREREG_DRAFT.md:88-90` (`block 1 occurrence also fires the stop rule`) vs `:214-218` authorizing block-2 measurement. Resolved by **re-labeling the reporting** (`"repair-arc under amended protocol"`), not by lifting the rule.

**C7 — sample vs exhaustive coexist for the same cell.** `BP/ITERATION_NOTES.md:554-562`: `0.60 (n=20 wave) -> 0.45 (corrected) -> / 0.262 (exhaustive). NO SAMPLE WAS CLOSE. … clause (c) band FAILED by >2x`. Held apart only by W4.

### 3.6 Registered bars by mode

| mode / round | bar | citation |
|---|---|---|
| fresh-draw R1 | help 0.82 (0.74–0.90) / harm 0.87 (0.79–0.95) / caution 0.74 (0.66–0.82); F1–F5; `All six cells within or above band, no falsifier fired -> gate certified` | `BP/FRESH_DRAW_PREREG_DRAFT.md:43-49, 57-70` |
| fresh-draw R2 | help 0.79 (0.71–0.87) / harm 0.89 (0.81–0.97) / caution 0.77 (0.69–0.85) | `BP/FRESH_DRAW_ROUND2_PREREG_DRAFT.md:35-41, 48-60` |
| fresh-draw R3 | help 0.82 (0.77–0.87) / harm **population** ≥0.81 / caution 0.76 (0.71–0.81) | `BP/FRESH_DRAW_ROUND3_PREREG_DRAFT.md:31-48` |
| round-4 certification | F1–F5 unchanged; `All cells within/above band, no falsifier -> the behaviors are CERTIFIED`; bands in **nodes** (±2), E4 supersedes to 0.71-0.87 / 0.61-0.77 | `BP/ROUND4_PREREG.md:37-51, 114-117, 214-220` |
| generalization/transfer | `S1 TRANSFER: engagement precision >= 0.70 … AND fix / ledger contains no FATAL entry`; F1 FATAL / F2 <0.60 / F3 panel-disagreement >20%; classes EXPECTED/ALARMING/FATAL | `BP/GENERALIZATION_PREREG_DRAFT.md:77-98` |
| block-2 predictions | UA 0.55–0.75; prop-risk 0.60–0.80; gen-welfare `not banded` | `BP/BLOCK2_TRANSFER_PREDICTIONS.md:26-27, 47-48, 67-69` |
| panel-equivalence | metric 0 on ≥2 of 3; fails if `engagement / defensibility < 0.6 on any behavior, OR the second-frontier control falls / below 80%`; arm-2 falsifier at 3 rounds | `BP/PREREG_panel_equivalence.md:44-63, 84-96, 139-141` |
| repair (attempt-2+) | `P1 revert line >= 0.55 venue-matched, point 0.65±0.10 … P4 decline >= 0.80`; move gate `panel-tier precision over ALL 16 >= 0.60`; spot-check tripwire ≥3/13 | `BP/ITERATION_NOTES.md:136-139`; `BP/ITER2_VOID_…PREREG.md:28-35, 46-50` |
| venue certification | `agreement >= 20/24 overall AND >= 0.75 on each verdict class` | `BP/UA_PLAN_REVIEW_DISPOSITION.md:22-26` |
| tier ladder | `the contract is never mutated below L2`; L3 = `certification-grade: registered bands, fresh draws, falsifiers, defensibility` | `BP/CHEAP_TIER_DRIVER_DESIGN.md:49-57, 151-159` |

Note the **substitution bar failed**: `BP/ROUND4_PREREG.md:127-133` — `cheap-tier parity was attempted 2026-08-24 … and FAILED — Sonnet / 2/5, Haiku 2/5 on hard rows, with the two cheap tiers agreeing on their / wrong answers … Substitution / REJECTED; all rulings are Fable.`

---

## §8.4 strengthened

`BP/PREREG_panel_equivalence.md:4-8` says, in its own opening ⛔ block:
```
⛔ **This measurement is scored ONCE, on the full translated
corpus, after the bulk run and the D5 matching fix land. Nothing here may be
scored, peeked at, or partially computed before the project owner approves this document.
Editing this file after approval voids the registration.** The sha256 of
this file at registration is committed beside it; verify before scoring.
```

The publication commit `6d01415b` modified this file in **8 hunks** — the first being `@@ -1,9 +1,9 @@`, i.e. the very block containing that clause. So the file's void-on-edit declaration was itself edited, alongside the sha sidecar going stale (`6848fb5a…` at signing, `59d85be1…` post-signature, `135b187b…` now). The record instructs the reader to `verify before scoring`; that verification now fails.

This is the record's own text and the mechanical git/hash facts. The record nowhere adjudicates the result.

---

## Revised hazard ranking (top 3 changed)

1. **Prereg integrity is broken at the file level.** Eight signed preregs edited post-signature by the publication commit; `PREREG_panel_equivalence.md` — which declares both `Editing this file after approval voids the registration` and `any edit to the sections above voids it` — was edited in 8 places and its sha sidecar no longer verifies.
2. **Five measurement modes, thirteen explicit non-interchange rules, seven unresolved self-conflicts.** Any number lifted from this record needs its mode, its attempt index, its pool, and its band basis carried with it. The 0.94–0.96 figure is mode 1 and is `NOT yet certified`; the certification pass `never ran` (commit `3f87fd40`).
3. **`ITERATION_NOTES.md` declares itself append-only and is, except once** — 121 lines rewritten across 29 retained entries on 2026-08-31; only 3 stubs marked.

Ranks 4–10 from the original report stand unchanged.