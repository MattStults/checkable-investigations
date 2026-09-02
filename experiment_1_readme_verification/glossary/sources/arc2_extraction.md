<!-- Source extraction for the glossary. Extractor: general-purpose subagent, model opus, read-only over the target record, README.md excluded by instruction. Committed untouched; the glossary cites this document's citations, which are path:line into the target repo at the pin. -->

Base path for all citations (absolute):
`/Users/mattstults/Documents/ai_safety_projects/semi-formal-document-analysis/walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/` — written below as `<BP>/`.

---

# Arc-2 record: source extraction of its own definitions

## 1. Engaged precision

**Nearest thing to a formal definition (the only formula-shaped one in the sources):**

> `<BP>/PREREG_panel_equivalence.md:79-81` — "3. **Precision against truth:** fraction of seat-engaged nodes ruled\n   relevant."

**Companion definition under a different name ("engagement defensibility"):**

> `<BP>/PREREG_panel_equivalence.md:47-49` — "* engagement defensibility = share of tool engagements the truth tier\n     rules relevant (both where the panel agreed and where it did not);"

**Authoritative artifact for the value:** varies by venue, and the record says so explicitly per run.
- Round-4 dev behaviours: `<BP>/ROUND4_DEV_TABLE.json:1-2` — "ROUND-4 DEV-BEHAVIOR TABLE COMPLETE (2026-08-24, recovered lineage venue, E4/registered bands, one-pass defensibility per amendment 1). Raw = strict panel-majority truth; headline = match-or-adjudicated-defensible. Both publish."
- Tradeoffs repair loop: the per-attempt `ITER*_SCORED.json`, with the re-measurement declared FINAL: `<BP>/ITER2_REMEASURE_SCORED.json:2` — "RE-MEASUREMENT SCORED per ITER2_VOID_RULING_AND_REMEASURE_PREREG.md — uniform panel tier on the frozen draws, full-extension move gate, one shot, FINAL."

**Denominator / population — the record uses at least four different ones, and does not reconcile them:**
1. 40-node stratified draw of engaged nodes: `<BP>/ROUND4_PREREG.md:20-22` — "Draws: seeded per behavior (seeds registered below), stratified 40 ENGAGED\n  + 40 NOT-engaged at the frozen instrument's states; every node with ANY\n  prior ruling excluded".
2. 20-node draws in the repair loop: `<BP>/ITER1_ATTEMPT2_SCORED.json:5` — `"n": "20+20"`.
3. A **closed population**, not a sample, for harm: `<BP>/ROUND4_PREREG.md:75-78` — "the unruled engaged pool is 17 <= 48,\n  so the engaged side is drawn WHOLE (population CLOSED — the certified\n  engaged-precision claim for harm is then a population figure, not a\n  sample)"; echoed at `<BP>/ROUND4_DEV_TABLE.json:35` — "engaged cell is a POPULATION figure (all 17 unruled engaged nodes ruled)".
4. The **exhaustive ruled engaged set** for user-autonomy: `<BP>/ITERATION_NOTES.md:556-559` — "THE NUMBER: visible engaged precision is EXACTLY\n32/122 = 0.262 (seal: 38 nodes untouched, single-use)."

**Conflict the record leaves standing (quoting both):** whether a precision number is over a *draw* or over the *ruled set*. Sample view: `<BP>/ITERATION_NOTES.md:257-258` — "n=20 draws carry ±~0.2; attempts\n  2 (0.75) and 3 (0.40) are compatible with pool precision ~0.55-0.60." Exhaustive view: `<BP>/ITERATION_NOTES.md:529-531` — "THE\n  MEMOIZED-EXHAUSTIVE ARCHITECTURE JUST EARNED ITS KEEP: no n=20\n  sample was ever going to reveal a 0.3-precision module reliably."

**Distinct tier/variant names for it:** `engaged_precision_raw`, `engaged precision` (panel tier), `raw_wave` vs `panel_tier` (`<BP>/ITER2_REMEASURE_SCORED.json:27,31`), `pooled panel-tier engaged precision`, `match-or-defensible`, `match-or-adjudicated-defensible` / `headline`, `quarantine_adjusted` (`<BP>/ITER3_ATTEMPT4_SCORED.json:191-193`), `corrected_estimator` (`<BP>/ITER2_ATTEMPT3_SCORED.json:192`), `visible engaged precision-so-far`, `extension_precision` (move gate, `<BP>/ITER2_REMEASURE_SCORED.json:4`).

---

## 2. Decline rate / declined set

**Definition (prereg form):**

> `<BP>/PREREG_panel_equivalence.md:49-51` — "* decline defensibility = share of tool declines on panel-cited nodes the\n     truth tier rules NOT relevant (i.e. the tool was right to decline)."

**Round-4 form, a different population** — the not-engaged half of the stratified draw, per `<BP>/ROUND4_PREREG.md:20-22` (quoted above). The scored files carry it as `decline_correctness_raw` over `n_not_engaged: 40`: `<BP>/round4_caution_scored_raw.json:4-6`; `<BP>/round4_harm_scored_raw.json:4-6`.

**These two are in conflict and the record does not resolve it:** PREREG_panel_equivalence scores declines *on panel-cited nodes only*; round-4 scores declines on a *uniform 40-node not-engaged draw*. Both are called the decline side.

**Names used:** `decline_correctness`, `decline_correctness_raw`, `decl` (`<BP>/ROUND4_DEV_TABLE.json:6,11`), "decline defensibility", "P4_decline" (`<BP>/ITER1_ATTEMPT2_SCORED.json:103`), "decline 0.70" (`<BP>/ITERATION_NOTES.md:348-349`).

**Falsifier attached:** `<BP>/ROUND4_PREREG.md:40` — "F2: any decline-correctness below band floor."

**A recorded interpretive ruling on P4's failure:** `<BP>/ITERATION_NOTES.md:154-157` — "P4 FAILED (decline_correctness 0.60 vs predicted >=0.80) and the failure\n  is a PREDICTION-CALIBRATION error, not a repair defect".

---

## 3. Recall-side measures ("declined nodes panel-relevant")

**Definition (prereg):**

> `<BP>/PREREG_panel_equivalence.md:76-78` — "2. **Recall against truth:** fraction of truth-relevant nodes the seat\n   engaged. Reported with the structural coverage ceiling (truth-relevant\n   clauses with no translated span) stated beside it."

**The record's own "honest headline" statement, in recall terms:**

> `<BP>/ITERATION_NOTES.md:280-283` — "THE HONEST HEADLINE IS RECALL, NOT PRECISION: 23/40 pooled declined\n  nodes are panel-relevant. The module's engaged side sits ~0.6-0.7;\n  its DECLINED side leaks a large relevant mass — the provide-class and\n  definitional-lane reach limits, now measured, not just characterized."

**Denominator:** 40 pooled declined nodes across the two frozen draws (attempts 2 and 3), panel-tier truth. Authoritative artifact: `<BP>/ITER2_REMEASURE_SCORED.json` (`panel_tier_misses.not_engaged_FN`, 10 for attempt-2 at lines 44-55, 13 for attempt-3 at lines 79-93).

**Related recall-side count in the same entry:** `<BP>/ITERATION_NOTES.md:290-291` — "FINAL QUEUE handed to future work: 15 panel-tier FPs + 23 panel-tier\n  FNs".

**Falsifier on the recall side:** `<BP>/ROUND4_PREREG.md:41-42` — "F3: >=3 unanimous-relevant not-engaged nodes in one behavior sharing one NEW\n    failure locus."

**Panel-agreement tool's recall-side vocabulary** (three-way states): `<BP>/panel_agreement.py:322-325` — `"seat_engaged_panel_cold"`, `"panel_hot_seat_declined"`, `"panel_hot_never_retrieved"`; described at `<BP>/panel_agreement.py:337-342` as "adjudication queue A" / "adjudication queue B".

---

## 4. The measurement tiers: raw match, panel tier, panel-tier re-measurement, adjudicated, match-or-defensible, match-or-adjudicated-defensible, "headline"

**Raw vs headline, defined:**

> `<BP>/ROUND4_DEV_TABLE.json:2` — "Raw = strict panel-majority truth; headline = match-or-adjudicated-defensible. Both publish."

> `<BP>/ROUND4_PREREG.md:106-113` — "1. DEFENSIBILITY PASS (project owner's decision, 2026-08-24): round-4 misses receive a\n   pre-declared ONE-PASS blind Fable defensibility adjudication, same shape\n   and outcome-branch discipline as DEFENSIBILITY_BATCH_PROTOCOL.md (one\n   pass, no iteration, no second batch). HEADLINE metric =\n   match-or-adjudicated-defensible; RAW match is reported alongside in the\n   same table, always. The registered predictions above are RAW-basis; the\n   defensibility pass cannot move a cell below its raw value, only up, and\n   both numbers publish."

**Raw match rate range for the in-sample criterion standing:**

> `<BP>/HANDOFF_CURRENT.md:106-108` — "- CRITERION STANDING (in-sample, all-truth): caution 0.941, harm 0.953, help\n  0.960 under match-or-adjudicated-defensible; raw match 0.81-0.85; the\n  human-panelist baseline 71%. NOT yet certified — that is round-4's job."

**Single-wave (raw wave) vs uniform panel tier:**

> `<BP>/ITERATION_NOTES.md:272-275` — "- FINAL NUMBERS (raw single-wave vs uniform panel tier):\n  attempt-1 transfer 0.40 (frozen) | attempt-2 0.75 raw / 0.70 panel |\n  attempt-3 0.40 raw / 0.55 panel. Pooled panel-tier engaged precision\n  over both frozen draws: 23/38 = 0.605."

**Single-wave truth's measured self-agreement (why panel tier exists):**

> `<BP>/CALCULUS_RUNBOOK.md:130-132` — "(b) Rule at\nPANEL TIER the FIRST time (certified venue): single-wave truth cannot\nbe memoized (0.846 self-agreement) and buying it first just prepays an\nupgrade."

**Panel-tier re-measurement (the "same samples, higher tier" move):**

> `<BP>/CALCULUS_RUNBOOK.md:89-92` — "unless the measurement itself fails a\n  RESULT-BLIND validity criterion (coverage), in which case halt and\n  surface; the remedy is re-adjudicating the SAME frozen samples at a\n  higher tier, both verdict directions, thresholds fixed pre-dispatch,\n  one shot — NEVER a new draw (notes 0010)."

Named in the runbook's own list of carried lessons at `<BP>/ITERATION_NOTES.md:382` — "same-samples-higher-tier re-measurement".

**Match-or-defensible (the contradiction rule):**

> `<BP>/ITER2_REMEASURE_SCORED.json:188` — "MATT RULING (2026-08-24, post-final, append-only — registered numbers above untouched): a node carrying OPPOSING UNANIMOUS panel rulings on identical text under the identical brief is DEFENSIBLE BY CONTRADICTION — the contradiction itself is the certificate; no seat is spent. Scored as non-error in the match-or-defensible view (campaign-precedented metric shape, cf. the mature behaviours' 0.94-0.96 match-or-adjudicated-defensible). Qualifying nodes require two full panels both unanimous and opposed; a 2-1 panel vs a wave (l3877_3953_n002) does NOT qualify and stays contested-pending."

> `<BP>/ITERATION_NOTES.md:299-311` — "Matt's ruling on the n005 flag: opposing UNANIMOUS panels on identical\ntext/brief = the node is defensible either way and must not hit the\ntop-line — score it match-or-defensible, the campaign's standing metric\nshape. […] Applied append-only to ITER2_REMEASURE_SCORED.json: pooled\nmatch-or-defensible engaged = 24/38 = 0.632; registered final numbers\nuntouched."

Values: `<BP>/ITER2_REMEASURE_SCORED.json:193-194` — `"pooled_engaged": "24/38 = 0.632 (n005 credited as defensible)"`, `"attempt3_engaged": "12/20 = 0.60 (was 0.55 panel-tier; n005 was in the attempt-3 engaged draw)"`.

**Adjudicated / defensibility outcome triples (round 4):** `<BP>/ROUND4_DEV_TABLE.json:66-70`:
```
"defensibility": { "help": "FP 0/4/11, FN 0/4/1",
                   "harm": "FP 0/1/2, FN 0/8/0",
                   "caution": "FP 0/3/10, FN 0/3/2" }
```

**Single-wave:** `<BP>/ITERATION_NOTES.md:88-91` — "The 25%-of-batch overturn rate also says single-wave\n  FP truth on a THIN engaged draw is noisy — future batches should\n  expect R1 escalation to dissolve a nontrivial fraction."

**Certified-Opus venue:**

> `<BP>/ITERATION_NOTES.md:347` — "Attempt-4 (certified-Opus venue per A10 Q3, coverage-valid registration):"

> `<BP>/ITERATION_NOTES.md:189-196` — "OPUS PARITY CERTIFICATE GRANTED (ITER1_OPUS_PARITY_CERTIFICATE.json;\n  prereg gates committed BEFORE dispatch; zero Fable): 3 Opus seats on\n  the 23-node panel-tier key -> majority 0.913, mean single 0.884\n  (ABOVE Fable's own 0.846 single-wave baseline on the same key),\n  per-class 8/9 + 13/14. Scope: lineage ruling seat, THIS brief,\n  tradeoffs venue; re-measures on brief change; does NOT touch the 0.38\n  flip-adjudication doctrine. Deployment: Opus waves + seeded 20% Fable\n  spot-checks + >1-disagreement tripwire; final iteration all-Fable."

**Fable spot-check:**

> `<BP>/CALCULUS_RUNBOOK.md:38-40` — "VENUE (A10 Q3, notes 0006/0013): the cheapest CERTIFIED tier + seeded\n    ~20% spot-check + tripwire."

Instances: `<BP>/ITER2_ATTEMPT3_SCORED.json:105-108` (`"spot_check_vs_opus": {"agreement": "3/3", "tripwire": "NOT FIRED"}`); `<BP>/ITER3_ATTEMPT4_SCORED.json:116-119` (`"wave_vs_opus": "1/8 disagreements (ok)"`, `"dispute_vs_panel": "4/9 disagreements (TRIPWIRE FIRED)"`); `<BP>/ITER2_REMEASURE_SCORED.json:170` (`"tripwire": "not fired (2/13 disagreements: ...)"`).

---

## 5. Attempt, iteration, block, draw, frozen draw, pooled, re-measurement

**Attempt 1 (transfer) vs attempts 2-4 (repair) — the record insists these answer different questions:**

> `<BP>/ITER1_ATTEMPT2_SCORED.json:2` — "ITERATION 1 attempt-2 REALIZATION scored against the registered prediction (ITERATION1_V5_PREDICTION.json). Measures THE REPAIR, never transfer; attempt-1's 0.40 transfer verdict is frozen. Venue: wave+panel."

> `<BP>/ITER1_ATTEMPT2_SCORED.json:167-168` — `"note": "comparison only; the two numbers answer different questions (transfer vs repair)"`

Attempt series, three separate statements of the same series (values differ by tier):
- `<BP>/ITER2_ATTEMPT3_SCORED.json:143-147` — `"attempt1_transfer_frozen": 0.4, "attempt2": 0.75, "attempt3": 0.4`
- `<BP>/ITER3_ATTEMPT4_SCORED.json:141-146` — `"a1_transfer_frozen": 0.4, "a2_panel": 0.7, "a3_panel": 0.55, "a4": 0.85`
- `<BP>/ITERATION_NOTES.md:351-352` — "Attempt series:\n  0.40 transfer -> 0.70 -> 0.55 -> 0.85/0.895."

**Iteration:** iterations 1-3 are entries 0001-0005 (iter 1), 0007-0011 (iter 2), 0012-0014 (iter 3). Iteration 2 declared terminal at `<BP>/ITERATION_NOTES.md:229-232` — "Iteration 2 is the FINAL in-scope iteration (post-move queue is\n  entirely fixed-or-suspended), so its confirmation venue is ALL-FABLE\n  per the standing ruling: 1 wave (40) + 3 panels (8) + 1 probe seat (5) +\n  the pending 3-node spot-check."

**Block (as budget/attention unit):** `<BP>/ITERATION_NOTES.md:510-512` — "BLOCK LEDGER: 4 Fable seats spent (3 key + 1 dispute);\nreserve intact; envelope respected."

**Block (attended vs autonomous):** `<BP>/ITERATION_NOTES.md:643-651` — "## 0032 — CONSTRAINED-AUTONOMY BLOCK, 2026-08-25\nThe block ran unattended under a registered incremental frontier-seat\ncap, with instructions to use less capable models wherever possible. […] With no resource meter readable by the agent,\nno frontier dispatch at all this block (strictly safer than the cap)." And `<BP>/ITERATION_NOTES.md:673-675` — "## 0034 — AUTONOMOUS BLOCK CLOSE, 2026-08-25\nFull block ran at ZERO frontier seats."

**Draw / frozen draw / seed:**

> `<BP>/ITERATION_NOTES.md:138-139` — "Draw seed\n  20260824; pools 231/531; 5 ruled-ledger overlaps (fresh rulings anyway)."

> `<BP>/ROUND4_PREREG.md:79-80` — "Seeds: base 20260824; caution 20260824, harm 20260825, help 20260826\n  (sorted-slug index, the registered-base-plus-index convention)."

Frozen draw: `<BP>/ITER2_REMEASURE_SCORED.json:2` — "uniform panel tier on the frozen draws, full-extension move gate, one shot, FINAL."

**Draw-luck rule:** `<BP>/ITERATION_NOTES.md:222-228` — "DRAW LUCK IS REAL (next agent must know): the attempt-3 seeded draw\n  sampled ZERO of the 16 gained nodes (p~0.26) — P3 would have been\n  vacuously true. […] RUNBOOK RULE CANDIDATE: after computing a confirmation draw,\n  CHECK it samples the move's gain/fix classes; if not, register a\n  seeded probe in the same pre-dispatch commit."

**Pooled:** `<BP>/ITERATION_NOTES.md:274-275` — "Pooled panel-tier engaged precision\n  over both frozen draws: 23/38 = 0.605." And the recall pooling at `<BP>/ITERATION_NOTES.md:280-281`. The record separately **prohibits** pooling in one place: `<BP>/L1L2_ADVERSARIAL_REVIEW.md:108` — "**all metrics are computed per seat and reported per seat — pooling across seats is prohibited**"; and `<BP>/L1L2_ADVERSARIAL_REVIEW.md:106` — "Two blind seats agreed on the exact dimension set for **23/39** nodes (41% disagreement), masked by pooling."

**Re-measurement (the void-for-coverage remedy):** `<BP>/ITERATION_NOTES.md:266-268` — "## 0010 — RE-MEASUREMENT FINAL + ITERATION 2 CLOSE, 2026-08-24\nExecuted exactly per ITER2_VOID_RULING_AND_REMEASURE_PREREG.md; one\nshot; numbers FINAL." Trigger at `<BP>/ITERATION_NOTES.md:260-263` — "OPTIONS SURFACED FOR RULING […] (b) rule the P1 realization void-for-coverage and\n  re-measure under a coverage-valid registration".

---

## 6. In-sample vs out-of-sample / fresh-draw; certification; criterion standing; "all-truth"

**Criterion standing (in-sample, all-truth) — verbatim already quoted above:** `<BP>/HANDOFF_CURRENT.md:106-108`.

**All-truth as the instrument-state baseline:**

> `<BP>/HANDOFF_CURRENT.md:33-39` — "## Instrument state (frozen, all-truth baseline)\n- modules_contract_v18.json + behaviors_canonical_v13.json; engagement =\n  relevance_by_act.py (act channel + walls + purpose channel SCOPED to assert\n  lane — see "channel jurisdiction" comments in the file; definitional keys\n  nid|c{i} never feed purpose_hit).\n- Baseline (no definitional layers): caution TP102/FP12, harm TP73/FP11,\n  help TP178/FP12 (truth = satisfiability_census.truth_all())."

**Certification, definition of what round 4 certifies:**

> `<BP>/ROUND4_PREREG.md:12-17` — "## What round 4 certifies\nThe three dev behaviours (helpfulness, harm-avoidance-to-third-parties,\navoiding-over-and-under-caution) on the Model Spec corpus, under the FROZEN\npost-9b instrument, on nodes NEVER before ruled — converting the in-sample\ncriterion standing (0.94-0.96 match-or-adjudicated-defensible) into a\ncertified out-of-sample claim. Scored ONCE."

> `<BP>/HANDOFF_CURRENT.md:132-134` — "f. ROUND-4 CERTIFICATION (post reset): frozen instrument, fresh\n    draws, 9e fresh-pool bands, prospective bucket assignment. This is what\n    converts 0.94-0.96 in-sample into the certified claim."

**Success criterion:** `<BP>/ROUND4_PREREG.md:47-51` — "## Success criterion (carried)\nAll cells within/above band, no falsifier -> the behaviors are CERTIFIED on\nthis document and the generalization runs + next-document arc unblock per\nthe campaign mandate. Above-band results get the leak-signature check before\nthey are celebrated."

**Fresh draw / out-of-sample:** operationalized by the exclusion rule at `<BP>/ROUND4_PREREG.md:22-23` — "every node with ANY\n  prior ruling excluded (the exclusion list is a deterministic script output\n  committed with its sha: round4_freeze.py -> ROUND4_FREEZE_DERIVATION.json)."

**The all-truth vs fresh-draw conflict, named as an erratum by the record itself:**

> `<BP>/ROUND4_PREREG.md:202-206` — "(b) mis-derived registered predictions: the\n   freeze script implemented "over all-truth" literally (0.9336) where\n   every actual fresh draw under the SAME judge landed 0.57-0.78 and prior\n   rounds registered lineage bands (round-2 passed at 0.78 in band\n   0.71-0.87) — the in-sample rate ignores the known generalization gap."

**The record's own note that "all-truth" is composition-biased (a second, conflicting characterization):**

> `<BP>/L1L2_ADVERSARIAL_REVIEW.md:314-316` — "### F31. The assembled truth ledger is composition-biased: positives and negatives were selected by different processes. […] Negative-class nodes enter partly through dedicated "agreed negative" draws; positive-class nodes partly through escalation panels."
> and `<BP>/L1L2_ADVERSARIAL_REVIEW.md:316` — "It also means the 0.560/0.443/0.540 base rates are properties of the assembly, not of the document."

Disposition accepting it: `<BP>/L1L2_REVIEW_DISPOSITION.md:66-68` — "ACCEPT A16 (score on single-process uniform fresh-draw partitions,\n  ~537 rulings, never the assembled truth_all() ledger — composition\n  bias F31)".

**Human-panelist baseline — asserted and then flagged as unsourced (two conflicting statements, both quoted):**
- `<BP>/HANDOFF_CURRENT.md:108` — "the\n  human-panelist baseline 71%."
- `<BP>/HANDOFF_CURRENT.md:210-211` — "- The handoff's "the human-panelist baseline 71%" currently has NO source\n  artifact; it must be sourced or struck before it appears in any writeup."

---

## 7. Certification falsifiers (F1 etc.), floor, band

**The falsifier list, verbatim:**

> `<BP>/ROUND4_PREREG.md:37-45` —
> "## Falsifiers (carried from round 3; apply unchanged)
> F1: any sampled engaged-precision below band floor; population figure below
>     its registered floor.
> F2: any decline-correctness below band floor.
> F3: >=3 unanimous-relevant not-engaged nodes in one behavior sharing one NEW
>     failure locus.
> F4: >30% of panels split 2-1 in any behavior.
> F5: single-vs-panel overturn rate >10% in any behavior -> remaining nodes
>     escalate to panels."

**Band units, defined:**

> `<BP>/ROUND4_PREREG.md:114-116` — "2. BAND UNITS (project owner's decision): bands are in NODES (+-2 nodes per cell).\n   The "+-5 pts" gloss holds only at n=40; for harm's CLOSED engaged\n   population (n=17) the band is +-2 nodes = +-11.8 pts. Nodes are the\n   registered unit everywhere."

**Registered bands, two incompatible sets — the record supersedes but keeps both on the page:**
- All-truth-derived (recorded as erratum): `<BP>/ROUND4_PREREG.md:70-74` — "caution: engaged precision 0.8843 (basis n=121), decline-correctness\n  0.8214 (n=84);\n  harm: engaged precision 0.8706 (n=85), decline-correctness 0.7785 (n=149);\n  help: engaged precision 0.9336 (n=211), decline-correctness 0.7849 (n=186)."
- Lineage-derived, superseding: `<BP>/ROUND4_PREREG.md:214-220` — "- REGISTERED PREDICTIONS, re-derived from lineage (supersede the\n     all-truth figures, which stand in the freeze section as a recorded\n     erratum): engaged precision band 0.71-0.87, decline-correctness band\n     0.61-0.77 […] F1/F2 read against these bands."

**Falsifier results as scored:** `<BP>/ROUND4_DEV_TABLE.json:54-58`:
```
"falsifiers": { "F3": "pending locus analysis",
                "F4": "0/19, 0/11, 1/21 — all clear",
                "F5": "2/19 (fired->escalated, help), 0/11, 1/21" }
```
Per-behaviour: `<BP>/round4_caution_scored_raw.json:11-14` — `"verdict_engaged": "F1 FIRES"`, `"F4_split_rate": "1/21"`, `"F5_overturn_rate": "1/21"`; `<BP>/ROUND4_DEV_TABLE.json:50` — "F1 by ONE node (27/40 vs floor 28); decl above band"; `<BP>/round4_harm_scored_raw.json:11-14` — `"verdict_engaged": "IN BAND"`, `"F4_split_rate": "0/11"`, `"F5_overturn_rate": "0/11"`.

**Floor as a hard rule:** `<BP>/HANDOFF_CURRENT.md:155` — "- Never lower a floor to pass; labels direct ATTENTION never TRUTH". Also a stop condition: `<BP>/CALCULUS_RUNBOOK.md:143-146` — "any floor that a\nchange would lower".

**Above-band leak check:** `<BP>/ROUND4_DEV_TABLE.json:65` — "decline cells above band in all three behaviors: seats were fresh file-fenced subagents with no repo access beyond the packet (coordinator-verified), panels near-unanimous (F4 clear); the shared cause is the residual pool's composition (peripheral nodes easy to decline), not seat contamination — recorded, cells stand".

**Repair-loop falsifiers use a different naming (P1-P4), not F1-F5:** `<BP>/ITER1_ATTEMPT2_SCORED.json:99-104` — `"P1_primary (>=0.55)": "PASS"`, `"P2_point (0.65+/-0.10)": "WITHIN"`, `"P3_mechanism (no fixed-class recurrence among engaged FPs)": "PASS"`, `"P4_decline (>=0.80)": "FAIL"`.

---

## 8. Dev behaviours vs repair-loop behaviours

**Dev behaviours (named):** `<BP>/ROUND4_PREREG.md:13-14` — "The three dev behaviours (helpfulness, harm-avoidance-to-third-parties,\navoiding-over-and-under-caution)". Table keys confirm: `<BP>/ROUND4_DEV_TABLE.json:4,20,37`.

What was tuned/iterated on them, per the record:
- `<BP>/ROUND4_PREREG.md:58-60` — the frozen instrument is "(= v18 + helpfulness purpose_concern [empowerment] + caution\n  purpose_concern [harm-prevention], adoption FINAL per\n  DEFENSIBILITY_BATCH_PROTOCOL.md ADJUDICATION RESULT)".
- `<BP>/HANDOFF_CURRENT.md:94-97` — "net-positive hypotheses: help purpose_concern +empowerment (+7/-3), caution\n    +harm-prevention (+2/0), caution +epistemic-autonomy (+2/-2);"
- `<BP>/HANDOFF_CURRENT.md:83-84` — "OBJECTIVITY AMENDMENTS REJECTED by name (instrument-wrong FPs 2/4 and 4/6);\n  narrowed conditional left open".
- Lineage: `<BP>/ROUND4_PREREG.md:7-10` — "round-1\n(protocol proof-out), round-2 (help PASSED, harm F1, caution F1-by-2, all\nfixed), round-3 (signed 2026-08-19, SUPERSEDED UNRUN…)".

**Repair-loop behaviour #1 — how-to-approach-tradeoffs.** Named in all four scored files (`<BP>/ITER1_ATTEMPT2_SCORED.json:3`, `<BP>/ITER2_ATTEMPT3_SCORED.json:3`, `<BP>/ITER3_ATTEMPT4_SCORED.json:3`). What was tuned:
- Iteration 1, candidate B: `<BP>/ITERATION_NOTES.md:112-115` — "ADOPTED (pending V5): candidate B = governs_concern wall + the corpus's\n  FIRST live governs_conditional (tone_manner:[vulnerable_interaction]).\n  V1 5/0, V2 drift 0/0/0, V3 held-out 48/48 […] V4 zero new ruled flips."
- Iteration 2, machinery gate: `<BP>/ITERATION_NOTES.md:216-218` — "Resolved by a new\n  typed gate machinery_concern:[acts] (I1 build; engine + registry +\n  handshake test one commit; inert unless declared; 43 tests green)".
- Iteration 3, ARB mint: `<BP>/ITERATION_NOTES.md:319-323` — "Drafted as MINT_ARBITRATES_PREREG_DRAFT.md — per-assert\n  ARBITRATES mark, consumed as an act-channel wall (precision) + an\n  additive channel (recall)." Outcome `<BP>/ITERATION_NOTES.md:348-350` — "P3 move gate 10/14 extension\n  nodes relevant — the arbitrates_channel adoption REALIZED AND KEPT."
- Quiescence: `<BP>/ITERATION_NOTES.md:374-376` — "STEP-1 triage of attempt-4 misses: 9/9 into standing states, no new\n  mechanism -> the tradeoffs loop is at its QUIESCENT FIXED POINT at\n  inventory k (ITER4_MISS_TRIAGE.json)."

**Repair-loop behaviour #2 — user-autonomy (UA).** What was tuned:
- `<BP>/ITERATION_NOTES.md:654-656` — "R3 enumeration (64 compounds, $0): admissible optimum = governs wall\n  {substance, tone, objectivity}: 18/90 fixes, 0 breaks, 0 new FPs.\n  ADOPTED (UA_REPAIR_MOVE1.json, ua_contract_r2.json). Seal UNTOUCHED."
- OPERATIVE_TARGET mint held: `<BP>/ITERATION_NOTES.md:657-663` — "STABILITY 0.98 mean pairwise, ZERO 3-way splits — the\n  most stable layer ever measured here. FP-side separation PASSES\n  (0.20 <= 0.30). TP-side coverage FAILS the gate: 0.67 vs >=0.70 […] so a PURE WALL is\n  inadmissible (would break 5 TPs). HELD FOR SIGN-OFF".
- Measured precision trajectory: `<BP>/ITERATION_NOTES.md:558-560` — "The sample\nseries that pointed here: 0.60 (n=20 wave) -> 0.45 (corrected) ->\n0.262 (exhaustive). NO SAMPLE WAS CLOSE."

**Block-2 / never-consulted behaviours named, with frozen predictions and what was (not) tuned:**
- `<BP>/ITERATION_NOTES.md:401-408` — "BLOCK2_TRANSFER_PREDICTIONS.md FROZEN before any block-2 ruling:\n  user-autonomy (single-consideration FPs + machinery FNs; existing\n  channels; 0 mints; 0.55-0.75), proportionate-risk (HEADLINE: the\n  tradeoffs ARB mint transfers as a zero-annotation arbitrates_channel\n  declaration — calibration IS arbitration; 0.60-0.80), general-welfare\n  (C-V: does still carries ASP-literal names, the F1 class unrepaired in\n  this module — checkable from the contract file alone; measure-after-\n  repair, not before)."
- The general-welfare prediction falsified before any measurement: `<BP>/ITERATION_NOTES.md:414-417` — "D5' question resolved by FALSIFICATION: general-welfare has no\nC-V defect — behavior_acts() regex-extracts canonical heads from the\nASP-literal form; the F1 class was bespoke NAMES, not ASP SYNTAX."
- Full six-behaviour scope ruling: `<BP>/HANDOFF_CURRENT.md:174-179` — "SCOPE RULING (2026-08-21): ALL SIX never-consulted\nbehaviours run, 3+3 SEQUENTIAL with a FATAL-class stop rule. First three in\ndiagnostic order: harmlessness-to-user (adjacent-family protects-wall flip),\nobjectivity-on-contested-questions (maximal-distance answer-quality shape),\n+ one of {tradeoffs, user-autonomy, proportionate-risk, general-welfare};\nremaining three run as confirmation IF the first three transfer cleanly."
- Slot-accretion tracking per behaviour: `<BP>/ITERATION_NOTES.md:603-606` — "TRACKED METRIC: slots-vs-values per behaviour. Current curve: tradeoffs\n+2 slots (ARB, machinery); UA +1 projected (locus); PREDICTIONS ALREADY\nIN PLACE: proportionate-risk = 0 slots (pure ARB reuse, frozen);\ngeneral-welfare = 0 slots (protects VALUE growth: animal/AI welfare)."
- Additional behaviour names appearing only in the review inventory: `<BP>/L1L2_ADVERSARIAL_REVIEW.md:305` — "helpfulness, third-party-harm, over-under-caution, tradeoffs, user-autonomy, harmlessness-to-user, objectivity, general-welfare, proportionate-risk. panel-v5's two additional defined behaviours (`no-sycophancy`, `undermine-oversight`) are *also* in the corpus and have **zero rulings** in the runlog. The one behaviour outside the 100 — `animal-welfare-impacts` — has citation coverage only […] and **zero** adjudicated relevant/not_relevant rulings anywhere."

---

## 9. Panel: judges, panel-v5, majority, split, dispute, quarantine, panel-internal agreement, test-retest, human-panelist baseline

**Which judges (frontier panel):**

> `<BP>/PREREG_panel_equivalence.md:12-14` — "The node-matching pipeline […] identifies spec material relevant to a behavior at a\nquality equivalent to the frontier panel (`data/behaviours.json`, judges\nsol / kimi / fable / opus / kimi-k2)"

> `<BP>/panel_agreement.py:4-8` — "Matt's question (2026-08-16): run the behaviors the FRONTIER PANEL judged\n[…] avoiding-over-and-under-caution — judges sol/kimi/fable/opus/kimi-k2) through\n[…] agreement/disagreement with the panel's clause citations as a QUALITY CHECK."

**Panel tiers in code (two, by score threshold):**

> `<BP>/panel_agreement.py:232` — `for tier, min_s in (("consensus_ge5", 5), ("any_ge2", 2)):`

**Panel is never truth:**

> `<BP>/panel_agreement.py:10-11` — "⛔ LABELS DIRECT ATTENTION, NEVER TRUTH (standing rule). The panel is a"

> `<BP>/HANDOFF_CURRENT.md:189` — "Truth doctrine unchanged: v5 panel is comparison layer ONLY, never truth."

**panel-v5:**

> `<BP>/HANDOFF_CURRENT.md:181-184` — "Grounds: the collaborator v5 frontier panel (ingested 2026-08-21 as\ndata/panel-v5/, see PROVENANCE.md) supplies 3 full seats on all 9 behaviours\nx both specs, removing the truth-scarcity reason for holding at two;\ncomparison statistics are free for all six".

> `<BP>/L1L2_ADVERSARIAL_REVIEW.md:310` — "9 behaviours × 589 model-spec passages, 3 judges each (5 for proportionate-risk), rubric committed, provenance byte-identical to an external repo — i.e. truth the project did not author, already frozen, at $0. It is unexploited."

**Three incompatible relevance ledgers (the record's own conflict, stated as such):**

> `<BP>/L1L2_ADVERSARIAL_REVIEW.md:296-300` — "- Graph-node ledger (`satisfiability_census.truth_all()` […]): helpfulness 477 nodes at **0.560** positive, harm-avoidance 291 at **0.443**, caution 285 at **0.540**.\n- panel-v5 […] majority-verdict≥2 positive rates of **0.012 (helpfulness), 0.044 (third-party-harm), 0.007 (over-under-caution)** […]\n- The original frontier panel (`data/behaviours.json`, rubric v3w) gives a third set: 377/333/153 passages at 0.536/0.550/0.614.\n\nThree artifacts, three constructs, all called "relevance.""

Corrected numbers, driver's own re-derivation (the two versions conflict; both are on record):

> `<BP>/L1L2_REVIEW_DISPOSITION.md:35-39` — "- panel-v5 majority(>=2) positive rates are 0.008-0.114 (driver\n  re-derivation; e.g. helpfulness 0.085, third-party-harm 0.098,\n  over-under-caution 0.071), not the reviewer's 0.012/0.044/0.007.\n  The F28 incompatibility with the node ledger (0.443-0.560) is\n  5-50x either way; the three-ledgers/truth-shopping finding stands."

**Majority / split, as scored:** the panel row schema is `{node, wave, seats[3], majority, split}` — `<BP>/ITER1_ATTEMPT2_SCORED.json:9-19`. Rule: `<BP>/ROUND4_PREREG.md:24-25` — "Rulings: single blind Fable rulings + 3-instance panels on a seeded 20%;\n  majority supersedes." Split memoization: `<BP>/CALCULUS_RUNBOOK.md:132-134` — "(2-1 majorities\nmemoize tagged SPLIT; entries carry definition-sha + brief-version +\nvenue and are voided by definition changes…)".

**Split rates observed:** `1/8` (`<BP>/ITER1_ATTEMPT2_SCORED.json:98`), `0/8` (`<BP>/ITER2_ATTEMPT3_SCORED.json:97`; `<BP>/ITER3_ATTEMPT4_SCORED.json:96`), 6 splits listed at `<BP>/ITER2_REMEASURE_SCORED.json:161-168`, `panel_split_rate_all80: 0.1` (`<BP>/round4_helpfulness_scored_final_raw.json:5`).

**Dispute + quarantine:**

> `<BP>/ITERATION_NOTES.md:353-362` — "TRIPWIRE WORKED AS DESIGNED (blog material): the dispute-class\n  spot-check fired (4/9) — the Opus certificate measurably does NOT\n  cover the boundary-item annotation sliver, exactly the population\n  2-seat disagreement selects for. Response was mechanical: quarantine\n  the 43 dispute resolutions (assembly's own rule), marks 283->260,\n  engagement 393->384; the only measured affected node was a fresh FP,\n  so the quarantine RAISED the adjusted precision to 0.895 and P3 holds\n  at 10/12. Lesson for certificates: measure parity ON THE DISPUTE\n  CLASS separately before letting a cheap tier resolve escalations —\n  consensus items and boundary items are different tasks."

> `<BP>/ITER3_ATTEMPT4_SCORED.json:190` — "Appended post-scoring, registered numbers above untouched: the dispute spot-check tripwire fired (4/9) -> all 43 dispute-panel mark resolutions quarantined per the assembly rule (arb_marks_final.json r2). Under the quarantined instrument the drawn engaged set loses only l3596_3876_n039 (fresh verdict not_relevant): quarantine-adjusted engaged precision 17/19 = 0.895; P3 move gate 10/12 (still PASS)."

Dispute closure: `<BP>/ITERATION_NOTES.md:499-502` — "Trusted-tier resolution of the 43 ARB disputes: 9 yes / 34 no — the\nOpus boundary-class permissiveness bias measured a SECOND time,\nindependently, same direction as the UA gate failure. Marks final r3 =\n269".

**Panel-internal agreement — defined as a ceiling, and recorded as currently unmeasured:**

> `<BP>/L1L2_ADVERSARIAL_REVIEW.md:216-217` — "If panel-internal agreement is, say, 0.85, a representation at 0.83 is functionally perfect but reads as a fail against any absolute bar.\n**Fix.** Register: panel-internal agreement (or the adjudication seat's own test-retest) is measured and published as the ceiling; the representation is scored as **% of ceiling attained**, with the pass threshold expressed in those terms."

> `<BP>/L1L2_ADVERSARIAL_REVIEW.md:215` — "### F22. Panel truth is itself noisy, so the achievable ceiling is below 1.0 and is currently unmeasured."

Adopted: `<BP>/L1L2_REVIEW_DISPOSITION.md:56-59` — "MCC(R) >= MCC(T)-0.05 AND above 99th null percentile, per\n  behaviour, worst-behaviour headline, ceiling = panel-internal\n  agreement".

**Test-retest:** appears only inside the F22 fix, quoted above (`<BP>/L1L2_ADVERSARIAL_REVIEW.md:217` — "or the adjudication seat's own test-retest"). No measured value is given anywhere in the sources.

**A separate, non-panel consistency benchmark ("median pairwise judge-vs-judge agreement"):**

> `<BP>/PREREG_panel_equivalence.md:68-75` — "1. **Consistency:** seat-vs-truth agreement (Jaccard over\n   relevant sets) >= the frontier panel's own **median pairwise\n   judge-vs-judge agreement** on the same behavior (benchmark.judge_set /\n   jaccard at threshold 1, spec_key openai, computed over the panel's\n   passage universe mapped through clause_joins to the same nodes). If the\n   pipeline agrees with an independent reader at least as well as the\n   panel's judges agree with each other, "panel-equivalent" is earned on\n   that behavior."

**Human-panelist baseline 71%:** see §6 — asserted at `<BP>/HANDOFF_CURRENT.md:108`, flagged as unsourced at `<BP>/HANDOFF_CURRENT.md:210-211`. These two statements conflict and the record does not resolve them.

**Owner's human spot-check (a distinct human baseline):** `<BP>/PREREG_panel_equivalence.md:23-25` — "The project owner's stratified spot-check (2026-08-18, `panel_run1/spotcheck_owner_result.json`):\n21/22 agreement with the tier across four strata and three behaviors; one\ndisagreement (Fable not_relevant, owner relevant)." Its status: `<BP>/PREREG_panel_equivalence.md:29` — "The spot-check is diagnostic, not part of the score."

**Truth tier (the panel's counterpart):** `<BP>/PREREG_panel_equivalence.md:18-23` — "## Truth tier (per D2)\n\nBlind Fable-tier adjudicators, one clean context per behavior, given ONLY\nthe behavior definition and each node's ESTABLISHES + SOURCE TEXT. Never\nshown seat verdicts, panel citations, or queue membership".

---

## 10. Node vs passage vs span vs definition — what each counts

**Node (the unit the campaign produces):**

> `<BP>/L1L2_ADVERSARIAL_REVIEW.md:302` — "Register the graph-node ledger at node granularity as primary (it is the only one at the unit the campaign produces)".

Counts: `<BP>/L1L2_ADVERSARIAL_REVIEW.md:288` — "The graph is **773 nodes** (`graph_v2/node_corpus_all.json`; 593 at root unwind per `GRAPH_OVERVIEW.md`), not ~600. More importantly: `behavior_pilot/coverage_translated.json` records **`translated_nodes: 183`**." Confirmed by the driver: `<BP>/L1L2_REVIEW_DISPOSITION.md:17-19` — "coverage_translated.json translated_nodes = 183 (of 773): L1's\n  "half the spec's nodes" do not exist in translated form".

**Passage (the panel's unit) and the passage→node join:**

> `<BP>/panel_agreement.py:208-210` — `"""{slug: {tier: set(node ids)}} — panel reference passages joined to\n    clauses, clause lines intersected with translated node spans. Also\n    returns per-slug coverage facts (reference clauses outside every span)."""`

> `<BP>/L1L2_ADVERSARIAL_REVIEW.md:312` — "passages→nodes is not an identity map, and the join must be built, hashed, and its coverage/ambiguity rate published before any metric is computed."

Passage counts: 589 model-spec passages × 9 behaviours (panel-v5, `<BP>/L1L2_ADVERSARIAL_REVIEW.md:297`); 377/333/153 passages for the original panel (`<BP>/L1L2_ADVERSARIAL_REVIEW.md:298`).

**Span:**

> `<BP>/PREREG_panel_equivalence.md:77-78` — "Reported with the structural coverage ceiling (truth-relevant\n   clauses with no translated span) stated beside it."

> `<BP>/panel_agreement.py:243-245` — `cov[tier] = {"reference_passages": len(pids), "joined_clauses": len(cids), "clauses_outside_translated_spans": len(uncovered)}`

**Definition — two senses, both in the record.**
(a) The behaviour definition given to a seat: `<BP>/ROUND4_PREREG.md:182-183` — "Round-4 ruling packets are: the ruling\n   question + behaviour definition + PASSAGE…".
(b) The 100-item query-class corpus unit: `<BP>/ITERATION_NOTES.md:769-771` — "THE BOUND:\n  24 dimensions x 105 values addresses the sampled character-spec\n  query class completely, ~1.2 handles/definition." Corpus composition: `<BP>/L1L2_ADVERSARIAL_REVIEW.md:305` — "`query_class_corpus.json`'s 100 ids break down as `ms:` 29, `sparrow:` 24, `anthropic-constitution:` 12, `anthropic-aup:` 10, **`adria:` 11**, `hhh:` 9, `llamaguard:` 6."
(c) A "definitional lane" of norm-free nodes, a third sense: `<BP>/HANDOFF_CURRENT.md:44-46` — "179 norm-free nodes annotated by TWO independent Opus seats (parity-passed\n   lane), consensus = per-field intersection, actor disagreement voids claim."

**The measured separability difference between the two units:** `<BP>/ITERATION_NOTES.md:786-788` — "Defensible numbers: dimension-set separability 0.37-0.40\n(definitions) / 0.85 (nodes)."

**Unit ambiguity named as a defect:** `<BP>/L1L2_ADVERSARIAL_REVIEW.md:300` — "L1 says "relevance prediction over the representation must beat majority baseline" without naming the ledger, the unit (node vs passage), or the threshold (any-judge≥2 vs majority≥2 vs score≥2)."

---

## 11. Erratum, recurrence, CoVe, tripwire, seat, certificate, brief-local, venue, reset, block, handoff, seed

**Erratum (the append-only rule):**

> `<BP>/ROUND4_PREREG.md:35` — "- Errata rule: registered numbers are never edited; corrections append."

> `<BP>/ROUND4_PREREG.md:148-149` — "## ERRATA (2026-08-24, post-signature, append-only; each ratified by the project owner in\n## session before taking effect)"

**Recurrence — two distinct senses.**
(a) Fixed-class recurrence as a prediction clause: `<BP>/ITER1_ATTEMPT2_SCORED.json:102` — `"P3_mechanism (no fixed-class recurrence among engaged FPs)": "PASS"`; audit rows carry `"fixed_class_recurrence": false` (`<BP>/ITER1_ATTEMPT2_SCORED.json:130`).
(b) Problem-node recurrence across behaviours: `<BP>/ITERATION_NOTES.md:581-585` — "## 0028 — RECURRENCE ANALYSIS: SECTIONS NOT STATEMENTS, 2026-08-24\nMatt's question answered with counts (PROBLEM_NODE_RECURRENCE.json):\nzero retranslations ever; 7/138 statement-recurrers (contested +\nsuspended-by-design); the mass is sectional (style/formatting +\nobjectivity + authority-machinery)."
(c) Erratum recurrence counting: `<BP>/ITERATION_NOTES.md:861-864` — "Erratum #21: the third instance this\nsession of a pass condition that could not fail (designer vocabulary,\ngrandfathered places, now a noise-satisfiable census) — the fix each\ntime was the same shape: build the null first." And its fourth: `<BP>/ITERATION_NOTES.md:873-877` — "a pass condition that cannot fail, erratum\n#21's FOURTH recurrence, this time authored in the same document\nthat adopted the null-model rule".

**CoVe** — never expanded or defined in the sources; used as a verb for driver re-derivation:

> `<BP>/ITERATION_NOTES.md:467-468` — "Clean-context Opus review returned 8 findings; CoVe verified every\nfactual claim before disposition (all checked out…)"

> `<BP>/L1L2_REVIEW_DISPOSITION.md:12-13` — "## CoVe results (driver re-derivations; the review is accepted only\n## where these confirm or the claim is structural)"

> `<BP>/ITERATION_NOTES.md:836-838` — "CoVe'd per standing rule — the three decisive\nfindings were RE-DERIVED by the driver and reproduced exactly"

**Tripwire:**

> `<BP>/ITERATION_NOTES.md:209` — "tripwire >1 disagreement voids the Opus wave."

> `<BP>/CALCULUS_RUNBOOK.md:43-44` — "A fired tripwire is mechanical: quarantine or\n    re-run, never silently accept."

Budget tripwire (a different one): `<BP>/ROUND4_PREREG.md:30-32` — "Budget tripwire carries over: a\n  wave consuming registered capacity disproportionately to its ruling count\n  stops the run for inspection."

**Seat:**

> `<BP>/ROUND4_PREREG.md:26-28` — "VENUE […] seats execute as fresh Fable subagents receiving\n  only the packet prompt string plus the recorded content-free tool fence."

Seat cost: `<BP>/ROUND4_PREREG.md:134-136` — "the lean seat (ruling-seat agent) measures 6,765 raw tokens per\n   seat instance — 3.5x below the fat-harness seat".

Seat failure modes: `<BP>/ITERATION_NOTES.md:13-16` — "SEAT FAILURE MODES seen live: ultra-short fragment passages push seats\n  into document-completion (fix: the anti-completion fence line, pinned in\n  E3/round4_pilot.py FENCE); one seat fabricated-from-memory dispatch was\n  voided (rule: prompts ONLY from committed packet files, never retyped)."

Seat noise measured: `<BP>/ITERATION_NOTES.md:254-258` — "SEAT NOISE IS REAL AND MEASURED: this wave seat agrees 4/7 with\n  standing ledger truth on the draw's known nodes, contradicting TWO\n  panel-tier rulings […]. Baseline\n  single-wave-vs-panel is 0.846."

**Certificate + brief-local:**

> `<BP>/ITERATION_NOTES.md:429-433` — "the Opus parity\n  certificate was measured on the TRADEOFFS brief; I deployed it on the\n  user-autonomy brief without re-measurement. ERRATUM #14 (runbook):\n  parity certificates are BEHAVIOUR-BRIEF-LOCAL — a new behaviour's\n  venue needs its own (cheap: the panel rows are the free key). The\n  spot-check architecture caught the stretch at a cost of one seat."

> `<BP>/CALCULUS_RUNBOOK.md:40-44` — "Certificates are brief-local AND\n    task-class-local: parity measured on consensus items does NOT cover\n    the dispute/boundary class (tripwire fired 4/9 there, notes 0014) —\n    measure the dispute class separately or keep escalation resolution\n    at the trusted tier."

Asymmetric certificate: `<BP>/ITERATION_NOTES.md:487-491` — "Measured conditional reliability: Opus NOT_RELEVANT\nverdicts 14/14 vs the key; Opus RELEVANT verdicts 5/10 — an asymmetric-\ncertificate candidate (per-verdict-class certification, an A10 Q3\nextension needing its own registered gate if adopted)." Validated: `<BP>/ITERATION_NOTES.md:515-517` — "ASYMMETRIC CERTIFICATE VALIDATED IN USE: negative spot-check 10/10\n  (tripwire clear) -> 74 Opus negatives memoized as trusted truth at\n  ~zero Fable."

Certificate doctrine finding: `<BP>/ITERATION_NOTES.md:505-509` — "CONVERGENT\nFINDING FOR THE CERTIFICATE DOCTRINE: two independent measurements now\nshow Opus over-marking/over-including on BOUNDARY items specifically —\nper-task-class AND per-brief certification is not optional caution, it\nis the measured shape of the capability gap."

**Venue:**

> `<BP>/ITERATION_NOTES.md:141-146` — "Confirmation venue as registered: 1 wave seat (40 nodes) +\n3 panel seats (8 pre-registered rows). Wave rulings were\ncommitted and the venue decision (dispatch panels vs wave-only) was made\non budget alone BEFORE any scoring — keep that sequencing; it removes the\noptional-stopping question entirely."

Venue values used: `"venue": "wave+panel"` (`<BP>/ITER1_ATTEMPT2_SCORED.json:4`); "FINAL-ITERATION ALL-FABLE VENUE (wave + 3-seat panel override + registered machinery probe)" (`<BP>/ITER2_ATTEMPT3_SCORED.json:2`); "Certified-Opus venue per A10 Q3" (`<BP>/ITER3_ATTEMPT4_SCORED.json:2`); "recovered lineage venue" (`<BP>/ROUND4_DEV_TABLE.json:2`); "generalization venue" (`<BP>/CALCULUS_RUNBOOK.md:17`).

Model-tier doctrine: `<BP>/HANDOFF_CURRENT.md:161-162` — "- Judgment-tier doctrine: adjudication/rulings = Fable only; annotation = Opus\n  OK; mechanical execution = any tier with written plan." And `<BP>/HANDOFF_CURRENT.md:152-153` — "Adjudication/flip rulings are\nFable-doctrine (Opus failed parity 0.38)."

**Reset (capacity reset):**

> `<BP>/HANDOFF_CURRENT.md:186-188` — "Capacity ruling:\nadjudication queues until after the next capacity reset; all\nreset-independent work proceeds before it."

> `<BP>/ITERATION_NOTES.md:541-545` — "## 0025 — ERRATUM #16 (stale reset belief) + CONTINUE RULING, 2026-08-24\nThe reset I had been scheduling against had already passed; I carried\nthe stale anchor forward through several plans. ERRATUM #16: budget\nscheduling must use dates, not remembered anchors; the actual reset\nschedule is the project owner's to state."

**Block (attended vs autonomous):** see §5. Also the constraint discipline that governs it: `<BP>/CALCULUS_RUNBOOK.md:115-122` — "CONSTRAINT DISCIPLINE (notes 0013; entries 0002/0008 are redacted stubs): the agent cannot read its\nown resource meter — confirm remaining capacity with the human before\nevery frontier dispatch. When a standing capacity cap and a standing\nvenue ruling conflict, that is a conflict between two HUMAN rulings:\nsurface the CONSTRAINT STRUCTURE […] never\na design menu. Certified cheap-tier seats do not draw on the frontier\nallocation."

**Handoff:**

> `<BP>/CALCULUS_RUNBOOK.md:110-113` — "HANDOFF = a fresh session booting CLAUDE.md -> HANDOFF_CURRENT.md ->\n  this runbook -> ITERATION_NOTES.md. No compaction ritual, no handoff\n  prompt: if a departing instance holds uncommitted context, THAT is\n  the bug — commit it here before ending."

> `<BP>/HANDOFF_CURRENT.md:2-3` — "Boot: CLAUDE.md -> this file -> CALCULUS_RUNBOOK.md -> ITERATION_NOTES\n0000-0043."

**Seed:** see §5. Additional seeds on record: 20260816 (agreed-negative sample, `<BP>/PREREG_panel_equivalence.md:37-38`), 20260817 (tuning half-split, `<BP>/PREREG_panel_equivalence.md:126`), 20260827 (paired-format pilot, `<BP>/ROUND4_PREREG.md:171`).

**Seal (related to seed/held-out):** `<BP>/CALCULUS_RUNBOOK.md:134-136` — "a SEEDED 25% of every\nexhaustive purchase is SEALED as held-out until a registered stopping\npoint — deltas tune only against the visible partition". Its inventory: `<BP>/L1L2_ADVERSARIAL_REVIEW.md:333` — "38 nodes (11 relevant / 27 not, 0.289), marked **"SEALED — single-use at the registered confirmation; must not enter visible truth.""

---

## 12. The scored JSON schema — fields and actual counts

### 12a. `<BP>/round4_caution_scored_raw.json` (121 lines)
Fields: `slug`, `n_engaged`, `n_not_engaged`, `engaged_precision_raw`, `decline_correctness_raw`, `bands{engaged,decline}`, `verdict_engaged`, `verdict_decline`, `F4_split_rate`, `F5_overturn_rate`, `misses{engaged_FP,not_engaged_FN}`, `verdicts{node: relevant|not_relevant}`.
Counts as found: `n_engaged` 40, `n_not_engaged` 40, `engaged_precision_raw` 0.675, `decline_correctness_raw` 0.875, bands `0.69-0.85` / `0.7-0.86`, `verdict_engaged` "F1 FIRES", `verdict_decline` "ABOVE (leak check)", F4 `1/21`, F5 `1/21`, **13 engaged_FP** (lines 17-29), **5 not_engaged_FN** (lines 32-37), **80 verdicts** (lines 40-119).

### 12b. `<BP>/round4_harm_scored_raw.json` (91 lines)
Same field set. `n_engaged` 17, `n_not_engaged` 40, `engaged_precision_raw` 0.8235, `decline_correctness_raw` 0.8, bands `0.81-0.97` / `0.59-0.75`, `verdict_engaged` "IN BAND", `verdict_decline` "ABOVE (leak check)", F4 `0/11`, F5 `0/11`, **3 engaged_FP** (lines 17-20), **8 not_engaged_FN** (lines 22-30), **57 verdicts** (lines 33-89).

### 12c. Helpfulness — three files, three different numbers, all on disk
- `<BP>/round4_helpfulness_scored.json` — fields `_`, `n_engaged` 40, `n_not_engaged` 40, `cells{engaged_precision_raw: 0.625, decline_correctness_raw: 0.625}`, `misses` (15 FP / 15 FN), `falsifiers{F4_panel_split_rate: 0.15789…, F5_overturn_rate: 0.05263…}`, `verdicts_by_node` (80 entries). Header: "ROUND-4 helpfulness scored cells (RAW; defensibility pass per amendment 1 runs on the misses next)". These are the VOIDED canary-attempt-1 numbers per E1.
- `<BP>/round4_helpfulness_scored_v2.json` — `_` "ROUND-4 helpfulness canary RE-RUN scored (recovered lineage venue, E4 bands)", `engaged_precision_raw` 0.575, `decline_correctness_raw` 0.85, `bands{engaged: 0.71-0.87, decline: 0.61-0.77}`, `in_band{engaged:false, decline:false, engaged_above:false, decline_above:true}`, `falsifiers{F4_panel_split_rate: 0.0, F5_overturn_rate: 0.10526…}`, misses 17 FP / 6 FN, `verdicts` 80.
- `<BP>/round4_helpfulness_scored_final_raw.json` — `_` (line 2) "ROUND-4 helpfulness canary FINAL raw cells after F5 full-panel escalation (all 80 nodes 3-seat majorities; registered 19 panels stand, remainder = wave seat + escalation seats B/C)", `engaged_precision_raw` 0.625, `decline_correctness_raw` 0.875, `panel_split_rate_all80` 0.1, misses **15 engaged_FP** (lines 8-22) / **5 not_engaged_FN** (lines 24-30), `verdicts` 80.

Only the third matches `<BP>/ROUND4_DEV_TABLE.json:5-7` (`"prec": 0.625, "decl": 0.875`). The v2 file's 0.575/0.85 and the first file's 0.625/0.625 are on disk and are not the table's numbers; the record does not annotate the v2 file as superseded.

### 12d. `<BP>/round4_pilot_scored.json`
`_` "Pilot gate scoring per ROUND4_PREREG.md erratum E2", `agreement_T_trimmed` 0.75, `agreement_C_corrected` 0.7, `difference_C_minus_T` −0.05, `gate` "FAIL -> lane STOPPED for design review", `per_node` (40 entries).

### 12e. `<BP>/ROUND4_DEV_TABLE.json` (71 lines)
`_`, `table{<slug>: {raw{prec,decl}, headline{prec,decl}, bands{prec,decl}, raw_verdict, headline_verdict, (note)}}`, `falsifiers{F3,F4,F5}`, `prediction_scorecard{4 keys}`, `above_band_leak_check`, `defensibility{help,harm,caution}`. Three slugs.

### 12f. `<BP>/ITER1_ATTEMPT2_SCORED.json` (212 lines)
`_`, `behaviour`, `venue`, `n` ("20+20"), `engaged_precision` 0.75, `decline_correctness` 0.6, `panel` (**8 rows**, each `{node, wave, seats[3], majority, split}`), `panel_split_rate` "1/8", `prediction_checks` (P1 PASS / P2 WITHIN / P3 PASS / P4 FAIL), `misses` (**5 engaged_FP**, **8 not_engaged_FN**), `p3_engaged_fp_audit` (**5 rows**, `{node, governs[], contexts[], fixed_class_recurrence}`), `attempt1_comparison`, `verdicts` (**40 entries**).

### 12g. `<BP>/ITER2_ATTEMPT3_SCORED.json` (197 lines)
`_`, `behaviour`, `n` "20+20", `engaged_precision` 0.4, `decline_correctness` 0.5, `panel` (**8 rows**), `panel_split_rate` "0/8", `machinery_probe` (**5 nodes, all relevant**), `spot_check_vs_opus{agreement: "3/3", tripwire: "NOT FIRED"}`, `prediction_checks` (P1 FAIL→REVERT / P2 OUTSIDE / P3 PASS 5/5 / P4 FAIL), `misses` (**12 engaged_FP**, **10 not_engaged_FN**), `attempt_series`, `verdicts` (**40**), `diagnostics{venue_vs_ledger_on_known_nodes, corrected_estimator, move_coverage, variance_note, status}`.

### 12h. `<BP>/ITER2_REMEASURE_SCORED.json` (197 lines)
`_`, `move_gate{extension_precision: 0.875, threshold: 0.6, outcome: "MOVE STANDS", extension_verdicts (**16 nodes**, 14 relevant / 2 not)}`, `attempt2{raw_wave{0.75,0.55}, panel_tier{0.7,0.5}, panel_tier_misses(6 FP, 10 FN)}`, `attempt3{raw_wave{0.4,0.5}, panel_tier{0.55,0.35}, panel_tier_misses(9 FP, 13 FN)}`, `attempt1_transfer_frozen` 0.4, `new_panel_majorities` (**62 nodes**), `panel_splits` (**6 nodes**), `spot_check{tripwire, rulings (13 nodes)}`, `addendum_matt_ruling_defensibility{_, auto_defensible[1], match_or_defensible_view{pooled_engaged, attempt3_engaged}}`.

Note a discrepancy the record does not flag: `attempt2.raw_wave.decline_correctness` is `0.55` (line 29) while `<BP>/ITER1_ATTEMPT2_SCORED.json:7` records `"decline_correctness": 0.6` and `<BP>/ITERATION_NOTES.md:154` says "decline_correctness 0.60".

### 12i. `<BP>/ITER3_ATTEMPT4_SCORED.json` (196 lines)
`_`, `behaviour`, `engaged_precision` 0.85, `decline_correctness` 0.7, `panel` (**8 rows**), `panel_split_rate` "0/8", `move_extension{verdicts (**14 nodes**), relevant: "10/14"}`, `spot_checks{wave_vs_opus: "1/8 disagreements (ok)", dispute_vs_panel: "4/9 disagreements (TRIPWIRE FIRED)"}`, `prediction_checks` (P1 PASS / P2 OUTSIDE / P3 PASS 10/14 / P4 PASS), `misses` (**3 engaged_FP**, **6 not_engaged_FN**), `attempt_series`, `verdicts` (**40**), `addendum_tripwire_quarantine{_, quarantine_adjusted{engaged_precision: 0.895, p3: "10/12"}}`.

---

## 13. (1) Entries marked superseded / stale / provisional / withdrawn / redacted

**Redacted (3), all self-labelled "[operational; redacted]" by the driver in the entry heading:**
- `<BP>/ITERATION_NOTES.md:71` — "## 0002 — BUDGET RULING (2026-08-24) — [operational; redacted]"
- `<BP>/ITERATION_NOTES.md:234` — "## 0008 — FINAL-BLOCK BUDGET CHECKPOINT (2026-08-24) — [operational; redacted]"
- `<BP>/ITERATION_NOTES.md:481` — "## 0021 — ENVELOPE + PLAN-V2 DISPATCH (2026-08-24) — [operational; redacted]"
Acknowledged in the runbook: `<BP>/CALCULUS_RUNBOOK.md:115` — "(notes 0013; entries 0002/0008 are redacted stubs)". Note 0021 is *not* listed there.

**Withdrawn (1):**
- `<BP>/ITERATION_NOTES.md:832` — "## 0042 — 0041 WITHDRAWN: THE INTEGRATION CENSUS FAILS ITS ADVERSARIAL REVIEW, 2026-08-25". Entry **0041** is the withdrawn one; withdrawn by the clean-context Opus adversarial reviewer, accepted by the driver after CoVe (`<BP>/ITERATION_NOTES.md:836-847`), recorded in `<BP>/RETRANS_REVIEW_DISPOSITION.md`. Also flagged in the handoff banner: `<BP>/HANDOFF_CURRENT.md:1` — "# ⭐⭐ ENTRY POINT (2026-08-25 end; INTEGRATION CLAIMS WITHDRAWN BY REVIEW)".
- Secondary withdrawal: L1/L2 (registered inside 0042's disposition) withdrawn at `<BP>/ITERATION_NOTES.md:866` — "## 0043 — L1/L2 THEMSELVES FAIL REVIEW: DOES-NOT-LICENSE" and `<BP>/L1L2_REVIEW_DISPOSITION.md:7-10` — "L1/L2 as registered\nin RETRANS_REVIEW_DISPOSITION.md are WITHDRAWN as licensing\nexperiments".

**Provisional (1):**
- `<BP>/ITERATION_NOTES.md:424-426` — "## 0018 — USER-AUTONOMY ATTEMPT-1 (PROVISIONAL) + ERRATUM #14, 2026-08-24\nVenue executed as amended; all seats machine-checked. PROVISIONAL result:\nengaged precision 0.60 (WITHIN the frozen 0.55-0.75 band…)". Conditions for lifting: `<BP>/ITERATION_NOTES.md:434-437` — "Scoring stands PROVISIONAL pending post-reset Fable verification:\n  (a) brief-local parity vs the 10 panel-tier rows, (b) re-verification\n  of the 3 disputed rulings, (c) the deferred 43-dispute re-resolution." Later superseded in effect by 0022's F5 rescoring (`<BP>/ITERATION_NOTES.md:492-494` — "F5 rescoring\nexecuted once as registered: attempt-1 corrected = 0.45/0.80 -> clause\n(c) FAILED low") and 0026's exhaustive 0.262.

**Superseded (partial supersessions, by whom and where):**
- `<BP>/ITERATION_NOTES.md:80-82` — "Artifact: fresh_draw4/ITER1_TRADEOFFS_ESCALATION_RESULT\n  .json — supersedes single-wave entries FOR REPAIR ROUTING ONLY; the\n  attempt-1 transfer claim (0.40, F2) stays frozen." (driver, entry 0003)
- `<BP>/ITERATION_NOTES.md:336-338` — "## 0013 — RULING AMENDMENT + MACHINE-PRESCRIBED VENUE, 2026-08-24\nRULING: the final-iteration-on-Fable overlay is rescinded (for now)." (rescinds the 0006 ruling at `<BP>/ITERATION_NOTES.md:181-182`)
- `<BP>/CALCULUS_RUNBOOK.md:124-126` — "TRUTH ECONOMICS (standing ruling, 2026-08-24, notes 0019 — supersedes the\nfresh-rulings-per-attempt inertia)"
- `<BP>/ITERATION_NOTES.md:377-378` — "CALCULUS_RUNBOOK v1 rewritten FROM notes 0001-0014 (execution-derived;\n  docs-tests 5/5)." — v0 superseded, "v0's draft-from-design text is in git\nhistory" (`<BP>/CALCULUS_RUNBOOK.md:4-5`).
- Round-3 prereg: `<BP>/HANDOFF_CURRENT.md:201-203` — "- Round-3 prereg (signed, sha 69631bf3...) is SUPERSEDED unrun: it froze\n  contract v13; the instrument has moved to v18." Also `<BP>/ROUND4_PREREG.md:9-10`.
- All-truth predictions superseded by lineage bands: `<BP>/ROUND4_PREREG.md:214-216` (quoted §7), signed by the project owner at `<BP>/ROUND4_PREREG.md:224-226`.
- Venue text superseded: `<BP>/ROUND4_PREREG.md:142-146` — "the fat-harness venue text in DEFENSIBILITY_BATCH_PROTOCOL.md's\n   venue ruling is superseded for round 4 by this measured configuration".
- E3's dispatch form superseded: `<BP>/ROUND4_PREREG.md:208-210` — "E3's packet anatomy stands, its\n     one-packet-per-seat dispatch form is superseded for round 4".
- Truth-precedence supersession flagged as unsafe: `<BP>/ITERATION_NOTES.md:284-289` — "TRUTH-INSTABILITY FINDING (do not let dict order hide it):\n  l3239_3382_n005 carries two OPPOSING unanimous Fable panels […] The\n  scorer's recency precedence currently rules; the node needs a\n  panel-of-record with the contradiction in front of it."

**Stale (three uses, all as a named failure):**
- `<BP>/ITERATION_NOTES.md:314-315` — "Queue refiltered against the CURRENT module first (lesson: never route\n  a stale miss list)" (entry 0012; bound into the runbook at `<BP>/CALCULUS_RUNBOOK.md:11-13`)
- `<BP>/ITERATION_NOTES.md:541-544` — erratum #16, "stale reset belief" (entry 0025)
- `<BP>/ITERATION_NOTES.md:533-534` — "The overshoot is mine\n  (batch sized on stale per-seat costs); logged, not hidden." (entry 0024)

**Voided (a fourth marker the sources use):**
- `<BP>/ROUND4_PREREG.md:150-153` — "E1 — CANARY ATTEMPT 1 VOIDED (protocol event; option A directed by the project owner).\n   The helpfulness canary's 120 seat rulings […] are VOID as a\n   certification measurement". Total: `<BP>/ROUND4_PREREG.md:159-161` — "The void is TOTAL (all 80 rows, not selective)".
- `<BP>/ITERATION_NOTES.md:266-267` — the iteration-2 void-for-coverage ruling (`ITER2_VOID_RULING_AND_REMEASURE_PREREG.md`).

---

## 14. (2) Every numbered and unnumbered erratum

**Unnumbered / iteration-attributed (the record counts these as errata 1-12 without individually numbering them; `<BP>/ITERATION_NOTES.md:367` — "runbook rewrite from\n  notes 0001-0014 now carrying FOUR banked errata"):**

| Entry | Line | One-line description |
|---|---|---|
| 0001 | `<BP>/ITERATION_NOTES.md:44-46` | RUNBOOK ERRATUM (STEP 1): `route.py <slug> <node>` KeyErrors for generalization slugs — truth lives outside `truth_all`'s fmap. |
| 0004 | `<BP>/ITERATION_NOTES.md:129-131` | RUNBOOK ERRATUM (STEP 4): nothing documents how attempt-1 wave items were built from ctx packets; reverse-engineered and verified byte-identical. |
| 0009 | `<BP>/ITERATION_NOTES.md:244-247` | "MY REGISTRATION ERROR: the pre-ruling addendum caught exactly this for P3 […] and did not extend the same coverage requirement to P1/P2." Counted to its iteration per `<BP>/ITERATION_NOTES.md:439-441`. |
| 0013 | `<BP>/ITERATION_NOTES.md:341-344` | DRIVER ERRATUM: "when surfacing a halt, name the CONSTRAINT STRUCTURE (which standing rulings conflict), never a design menu — two of the three 'options' I offered were not mine to offer." |
| 0013 (2nd) | `<BP>/CALCULUS_RUNBOOK.md:57-60` | "notes 0013 erratum: never bundle them [a mint's consumption mechanisms] into one adoption decision or escalate their selection to a human". |
| 0020 | `<BP>/ITERATION_NOTES.md:478-479` | "the review+CoVe cycle added 4 process rules in one pass — the errata series is NOT converged". |

**Numbered:**

| # | Entry | Line | One-line description |
|---|---|---|---|
| 13 | 0017 | `<BP>/ITERATION_NOTES.md:418-421` | "verify contract-level predictions against the engine before freezing (the check was one line and I skipped it)." |
| 14 | 0018 | `<BP>/ITERATION_NOTES.md:430-433` | "parity certificates are BEHAVIOUR-BRIEF-LOCAL — a new behaviour's venue needs its own." |
| 15 | 0019 | `<BP>/ITERATION_NOTES.md:453-455` | "the prereg's fresh-rulings-per-attempt clause was justified for attempt-1 transfer only; carrying it into repair attempts was inertia." |
| 16 | 0025 | `<BP>/ITERATION_NOTES.md:543-545` | "budget scheduling must use dates, not remembered anchors; the actual reset schedule is the project owner's to state." |
| 17 | 0026 | `<BP>/ITERATION_NOTES.md:568-570` | "the cost-estimation erratum is now twice repeated: #17, fix the model before the next sizing." |
| 18 | 0027 | `<BP>/ITERATION_NOTES.md:577-579` | "measure shelf data sources' certificate-ability BEFORE the dominant spend, not after the question." |
| 19 | 0034 | `<BP>/ITERATION_NOTES.md:694-696` | "my coding vocabulary under-specified — same lesson as the mint-criteria discipline: MEASURE the brief before scaling." |
| 20 | 0037 | `<BP>/ITERATION_NOTES.md:739-751` | CLOSED-VOCABULARY CIRCULARITY: endogeneity + a coding vocabulary written with knowledge of the built layers; "saturation studies with closed vocabularies measure vocabulary coverage, never space completeness." |
| 21 | 0042 | `<BP>/ITERATION_NOTES.md:861-864` | "the third instance this session of a pass condition that could not fail (designer vocabulary, grandfathered places, now a noise-satisfiable census)." |
| 21 (4th recurrence) | 0043 | `<BP>/ITERATION_NOTES.md:873-877` | L1's relevance clause is "a pass condition that cannot fail, erratum #21's FOURTH recurrence, this time authored in the same document that adopted the null-model rule." |

**Errata series count as the record itself tracks it:** `<BP>/ITERATION_NOTES.md:438-441` — "Q1 DATA POINT: this fresh run produced one new erratum — the process\n  layer is STILL amending (errata series 4,4,4,2*,1 — trending down,\n  not yet zero; *0013/0009 counted to their iterations). The automation\n  decision correctly waits."

**Round-4 errata (a separate, E-prefixed series in `<BP>/ROUND4_PREREG.md`):**
- E1 (`:150-167`) — canary attempt 1 VOIDED; packet format divergence (SOURCE TEXT only vs ESTABLISHES + SOURCE TEXT); plus a fabricated-seat-material void and 4 malformed replies.
- E2 (`:168-180`) — paired-format pilot registered as the gate for the canary re-run; 40 seats, seed 20260827, gate C ≥ 0.80 and (C − T) ≥ 0.10.
- E3 (`:181-191`) — seat-material format PINNED ("the gap the canary exposed: the prereg never specified packet anatomy").
- E4 (`:192-222`) — pilot gate FAILED (T 0.75 / C 0.70, format hypothesis refuted); lineage venue recovered verbatim from round-3 transcripts, replicated 20/20; registered predictions re-derived to lineage bands. Signed `:224-226`.

**Errata in the disposition documents:**
- `<BP>/ITERATION_NOTES.md:772-776` — "Errata this arc: designer-vocabulary smuggling caught THREE times (Matt twice, the vacuousness check once)".
- `<BP>/ITERATION_NOTES.md:903-907` — "LEARNING: I wrote L1/L2 in the same commit that adopted 'build the null first' and still gave L1 a bar already met and L2 no null — adopting a method rule is not applying it".

---

## 15. (3) Does `round4_help*_scored_raw.json` exist?

**No file matching `round4_help*_scored_raw.json` exists.** Directory listing of the pattern `round4_*scored*` returns exactly:
```
round4_caution_scored_raw.json
round4_harm_scored_raw.json
round4_helpfulness_scored_final_raw.json
round4_helpfulness_scored_v2.json
round4_helpfulness_scored.json
round4_pilot_scored.json
```
So the `_scored_raw` suffix exists only for caution and harm; the helpfulness equivalent is named `round4_helpfulness_scored_final_raw.json`.

**What the record says about the helpfulness scoring artifacts (why there are three, and what each is):**
- Attempt 1's rulings are preserved but void: `<BP>/ROUND4_PREREG.md:151-155` — "The helpfulness canary's 120 seat rulings (raw file\n   round4_helpfulness_rulings_raw.json, preserved) are VOID as a\n   certification measurement: seat material diverged from the format that\n   built the truth ledger." The corresponding scored file is `round4_helpfulness_scored.json` (0.625/0.625, F1/F2 firing) — the prereg names those exact cells: `<BP>/ROUND4_PREREG.md:157-159` — "the F1/F2 firings (raw cells 0.625/0.625 vs 0.9336/0.7849) are\n   measurement artifacts of the divergence, not adjudicated instrument\n   failures."
- The re-run under the recovered lineage venue is `round4_helpfulness_scored_v2.json` (`_`: "ROUND-4 helpfulness canary RE-RUN scored (recovered lineage venue, E4 bands)", 0.575/0.85).
- The number the dev table treats as authoritative comes from `round4_helpfulness_scored_final_raw.json` after the F5 escalation: `<BP>/round4_helpfulness_scored_final_raw.json:2` — "ROUND-4 helpfulness canary FINAL raw cells after F5 full-panel escalation (all 80 nodes 3-seat majorities; registered 19 panels stand, remainder = wave seat + escalation seats B/C)". The F5 escalation trigger is recorded at `<BP>/ROUND4_DEV_TABLE.json:57` — "F5": "2/19 (fired->escalated, help), 0/11, 1/21".

The record contains **no statement naming or explaining the absence of a file called `round4_help*_scored_raw.json`**; the naming asymmetry is undocumented.

---

## 16. Conflicting definitions the record leaves unresolved (summary of the pairs quoted above)

1. **Decline population:** panel-cited nodes (`<BP>/PREREG_panel_equivalence.md:49-51`) vs a uniform 40-node not-engaged draw (`<BP>/ROUND4_PREREG.md:20-22`).
2. **Registered predictions basis:** all-truth in-sample (`<BP>/ROUND4_PREREG.md:70-74`) vs lineage fresh-draw bands (`<BP>/ROUND4_PREREG.md:214-220`); the first is retained on the page as "a recorded erratum".
3. **Helpfulness raw cells:** 0.625/0.625 vs 0.575/0.85 vs 0.625/0.875 across the three scored files (§12c).
4. **Attempt-2 decline:** 0.6 (`<BP>/ITER1_ATTEMPT2_SCORED.json:7`, `<BP>/ITERATION_NOTES.md:154`) vs 0.55 (`<BP>/ITER2_REMEASURE_SCORED.json:29`).
5. **Human-panelist baseline 71%:** asserted (`<BP>/HANDOFF_CURRENT.md:108`) vs declared source-less (`<BP>/HANDOFF_CURRENT.md:210-211`).
6. **panel-v5 positive rates:** 0.012/0.044/0.007 (`<BP>/L1L2_ADVERSARIAL_REVIEW.md:297`) vs 0.008-0.114, e.g. 0.085/0.098/0.071 (`<BP>/L1L2_REVIEW_DISPOSITION.md:35-37`).
7. **1-NN significance:** p=0.0015 / p=0.0097 (`<BP>/L1L2_ADVERSARIAL_REVIEW.md:95`) vs p=0.154 / p=0.157 (`<BP>/L1L2_REVIEW_DISPOSITION.md:40-43`).
8. **Same effect size, opposite verdicts:** "best 0.70 vs 0.59 base" as a *failure* (`<BP>/ITERATION_NOTES.md:633-634`) vs the same numbers as a *pass* under L1 (`<BP>/L1L2_ADVERSARIAL_REVIEW.md:96` — "The same numbers cannot be a failure in 0031 and a pass in L1.").
9. **Truth ledger for scoring:** assembled `truth_all()` (`<BP>/HANDOFF_CURRENT.md:39`) vs "never the assembled truth_all() ledger" (`<BP>/L1L2_REVIEW_DISPOSITION.md:66-68`).
10. **Pooling:** used for the pooled panel-tier figure (`<BP>/ITERATION_NOTES.md:274-275`) vs "pooling across seats is prohibited" (`<BP>/L1L2_ADVERSARIAL_REVIEW.md:108`).
11. **Graph size:** "~600 nodes" (L1's frame) vs 773 / 593-at-root-unwind / 183 translated (`<BP>/L1L2_ADVERSARIAL_REVIEW.md:288`).