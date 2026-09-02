# Glossary — definitions and authoritative-artifact map

Definitions layer for experiment 1. Written before translation, from the target record only (README.md excluded from every source pass). Each entry cites the record document that defines it as path:line into the target repo at commit 48e66ce04a4d9f06771c42f89cb37b075583c5f6; full quotes are in sources/*.md. Where the record conflicts with itself both sides are listed under 'conflicts' and NOT resolved. Translators receive this file and the brief; they never receive the sources or the inventory. The tier enum and its non-arc-specific definitions (human, live_run, git, filesystem, stated) are the experiment's own controlled vocabulary, not quoted from the record.

Path prefixes: `SFE` = `semi-formal-experiment/`; `BP` = `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/`; `G2` = `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/`

## Tiers (closed enum)

- **raw** — CONFLICT in the record, resolved only by field name (rule 1): round 4 'Raw = strict panel-majority truth' (BP/ROUND4_DEV_TABLE.json:2) vs repair loop 'raw single-wave vs uniform panel tier' (BP/ITERATION_NOTES.md:272). Both are tier=raw with venue recording which sense.
- **panel** — a frontier-judge panel ruling: arc 1 = the 3-judge frontier panel per behaviour (data/behaviours.json provenance block); arc 2 = 3-instance panels, majority supersedes (BP/ROUND4_PREREG.md:24-25)
- **adjudicated** — a defensibility or dispute overlay on top of raw/panel: one-pass blind defensibility adjudication (BP/ROUND4_PREREG.md:106-113), match-or-defensible addenda (BP/ITER2_REMEASURE_SCORED.json:188), quarantine adjustment (BP/ITER3_ATTEMPT4_SCORED.json:190)
- **human** — an owner ruling; markers: 'MATT RULING' | 'RULING:' | 'the project owner' | 'project owner's decision' | 'COUNTERSIGNED' | decision.json signed_by (the 2026-08-31 publication commit replaced 'Matt' with role language in retained entries, so both forms occur)
- **live_run** — produced by running a committed script now; record the command and wall clock
- **git** — commit metadata or history
- **filesystem** — existence or shape of a committed file
- **stated** — a number stated in prose with no scored artifact named in the span
- **cove** — the span itself says CoVe / re-derived / re-derivation (BP/L1L2_REVIEW_DISPOSITION.md:12-13; BP/ITERATION_NOTES.md:836-838); record the actor verbatim; independence is decided at query time, not by the translator

## Entries

### engaged precision  (arc 2)

**Definition.** the record defines 'engagement defensibility' (share of tool engagements the truth tier rules relevant, BP/PREREG_panel_equivalence.md:47-49) and 'precision against truth' (fraction of seat-engaged nodes ruled relevant, :79-81); the scored files report fields named engaged_precision / engaged_precision_raw with no definition in the file; the record does not state these are one metric — carry the field name from the file

**Authoritative artifact.** per venue: round-4 dev behaviours = BP/ROUND4_DEV_TABLE.json (raw and headline columns, 'Both publish'); tradeoffs repair loop = the per-attempt BP/ITER*_SCORED.json with BP/ITER2_REMEASURE_SCORED.json declared FINAL for attempts 2-3

**Denominator / population.** copy the n_engaged / n_not_engaged field from the same JSON object verbatim; if the source is prose, copy the fraction the span writes (e.g. 32/122), never a normalised label. Populations seen in the record: 40-node stratified draw (BP/ROUND4_PREREG.md:20-22); n='20+20' (BP/ITER1_ATTEMPT2_SCORED.json:5); CLOSED population n=17 for harm (BP/ROUND4_PREREG.md:75-78); exhaustive 32/122 (BP/ITERATION_NOTES.md:556-559)

**Variants.** engaged_precision_raw, engaged precision (panel tier), raw_wave vs panel_tier, pooled panel-tier engaged precision, match-or-defensible, match-or-adjudicated-defensible / headline, quarantine_adjusted, corrected_estimator, extension_precision (move gate)

**Conflicts in the record (unresolved).**
- sample view (n=20 draws carry ±~0.2, BP/ITERATION_NOTES.md:257-258) vs exhaustive view (BP/ITERATION_NOTES.md:529-531)

**Hazards for translators.**
- the same numeric value can appear at two attempts or two tiers (e.g. a raw and a panel figure for the same attempt in one line, BP/ITERATION_NOTES.md:272-275); carry attempt AND tier on every value
- an attempt's figure may carry an adjusted companion in the same entry (quarantine-adjusted, BP/ITER3_ATTEMPT4_SCORED.json:190); record both as separate claims linked by supersession

**Cites.** `BP/PREREG_panel_equivalence.md:79-81`; `BP/PREREG_panel_equivalence.md:47-49`

### decline correctness / declined set  (arc 2)

**Definition.** the record defines 'decline defensibility' (share of tool declines on panel-cited nodes the truth tier rules NOT relevant, BP/PREREG_panel_equivalence.md:49-51) and reports fields named decline_correctness / decline_correctness_raw in the scored files with no definition; the record does not state they are the same metric — carry the field name from the file

**Authoritative artifact.** same artifacts as engaged precision

**Denominator / population.** CONFLICT: panel-cited nodes only (PREREG_panel_equivalence) vs a uniform 40-node not-engaged draw (round 4). Record which population.

**Variants.** decline_correctness, decline_correctness_raw, decl, decline defensibility, P4_decline

**Conflicts in the record (unresolved).**
- attempt-2 decline recorded as 0.6 (BP/ITER1_ATTEMPT2_SCORED.json:7; BP/ITERATION_NOTES.md:153) and as 0.55 (BP/ITER2_REMEASURE_SCORED.json:29)

**Cites.** `BP/PREREG_panel_equivalence.md:49-51`; `BP/round4_caution_scored_raw.json:4-6`

### recall against truth / declined nodes panel-relevant  (arc 2)

**Definition.** fraction of truth-relevant nodes the seat engaged; its complement is reported as 'declined nodes that are panel-relevant' (not-engaged false negatives)

**Authoritative artifact.** BP/ITER2_REMEASURE_SCORED.json panel_tier_misses.not_engaged_FN per attempt; pooled figures in the ledger entry that states them

**Denominator / population.** pooled declined nodes over the frozen draws it pools; a pooled value carries snapshot=pooled plus the attempt set

**Hazards for translators.**
- numerator collision: the same numerator can appear on adjacent lines with different denominators and different metrics (a precision and a recall-side figure); carry the metric name and the denominator population, never just the fraction

**Cites.** `BP/PREREG_panel_equivalence.md:76-78`; `BP/ITERATION_NOTES.md:280-283`

### raw / panel tier / single-wave / uniform panel tier / re-measurement  (arc 2)

**Definition.** raw = strict panel-majority truth or a single seat's (single-wave) verdict; panel tier = 3-instance panel majority; uniform panel tier = every node in the frozen draws re-adjudicated at panel tier; re-measurement = re-adjudicating the SAME frozen samples at a higher tier, never a new draw

**Hazards for translators.**
- single-wave self-agreement is 0.846 (BP/CALCULUS_RUNBOOK.md:130-132): a single-wave figure is not a panel figure even for the same draw

**Cites.** `BP/ROUND4_DEV_TABLE.json:2`; `BP/ITERATION_NOTES.md:272-275`; `BP/CALCULUS_RUNBOOK.md:89-92`; `BP/CALCULUS_RUNBOOK.md:130-132`

### match-or-defensible / match-or-adjudicated-defensible / headline  (arc 2)

**Definition.** a view in which a node carrying opposing unanimous panel rulings on identical text under the identical brief is scored as non-error ('defensible by contradiction'), or in which a miss adjudicated defensible by a one-pass blind seat is scored as non-error; 'headline' is the round-4 name for match-or-adjudicated-defensible, always published beside raw

**Authoritative artifact.** BP/ROUND4_DEV_TABLE.json headline column (dev behaviours); BP/ITER2_REMEASURE_SCORED.json addendum_matt_ruling_defensibility (tradeoffs)

**Hazards for translators.**
- the defensibility pass 'cannot move a cell below its raw value, only up'; a headline figure is never lower than its raw
- BP/ROUND4_PREREG.md:106-113 registers a one-pass defensibility adjudication as amendment 1; a separate prereg (BP/PREREG_panel_equivalence.md) registers a match-or-defensible scoring that the record describes as scored ONCE after conditions. When a span names a registration, copy the name the span uses verbatim.

**Cites.** `BP/ITER2_REMEASURE_SCORED.json:188`; `BP/ITERATION_NOTES.md:299-311`; `BP/ROUND4_PREREG.md:106-113`

### criterion standing (in-sample, all-truth)  (arc 2)

**Definition.** per-behaviour match-or-adjudicated-defensible rates the handoff labels 'CRITERION STANDING (in-sample, all-truth)' and 'NOT yet certified — that is round-4's job'; the all-truth ledger is satisfiability_census.truth_all() (BP/HANDOFF_CURRENT.md:33-39)

**Authoritative artifact.** BP/HANDOFF_CURRENT.md (the line that states it); certification cells in BP/ROUND4_DEV_TABLE.json are the out-of-sample counterpart

**Conflicts in the record (unresolved).**
- all-truth is called composition-biased and 'never' to be scored on (BP/L1L2_ADVERSARIAL_REVIEW.md:314-316; BP/L1L2_REVIEW_DISPOSITION.md:66-68) while HANDOFF_CURRENT.md:33-39 uses it as the baseline

**Hazards for translators.**
- provenance region: this figure lives below the starred block of the handoff; record provenance_region
- the same line carries 'the human-panelist baseline 71%'. The record's status for it CONFLICTS: BP/HANDOFF_CURRENT.md:210-211 says it 'has NO source artifact; it must be sourced or struck'; BP/GENERALIZATION_PREREG_DRAFT.md:81-84 says it 'is STRUCK 2026-08-21: no artifact establishes it'. Translate the value with supersession.status=contested, by = the claim translating whichever of those two spans is in the batch, and quote the flag verbatim in notes.

**Cites.** `BP/HANDOFF_CURRENT.md:106-108`; `BP/ROUND4_PREREG.md:12-17`; `BP/ROUND4_PREREG.md:202-206`

### certification / round 4 / falsifiers F1-F5 / band / floor  (arc 2)

**Definition.** round 4 certifies the three dev behaviours on nodes never before ruled, converting in-sample criterion standing into an out-of-sample claim, scored ONCE; falsifiers F1 (engaged precision below band floor), F2 (decline below floor), F3 (≥3 unanimous-relevant not-engaged nodes sharing a new locus), F4 (>30% panels split), F5 (single-vs-panel overturn >10% → escalate); bands are in NODES (±2 per cell)

**Authoritative artifact.** BP/ROUND4_DEV_TABLE.json (raw_verdict, headline_verdict per behaviour); per-behaviour BP/round4_*_scored*.json

**Conflicts in the record (unresolved).**
- two registered band sets: all-truth-derived (BP/ROUND4_PREREG.md:70-74, kept as a recorded erratum) vs lineage-derived superseding bands (BP/ROUND4_PREREG.md:214-220)
- helpfulness has three scored files with three different raw cells: BP/round4_helpfulness_scored.json (0.625/0.625; BP/ROUND4_PREREG.md:150-161 marks canary attempt 1 VOID), BP/round4_helpfulness_scored_v2.json (0.575/0.85, header 'canary RE-RUN scored'), BP/round4_helpfulness_scored_final_raw.json:2 (0.625/0.875, 'FINAL raw cells after F5 full-panel escalation'; the cells BP/ROUND4_DEV_TABLE.json:5-7 carries). Only the first is marked void in the record.

**Hazards for translators.**
- file naming asymmetry: caution and harm are round4_<slug>_scored_raw.json; helpfulness is round4_helpfulness_scored_final_raw.json; no file round4_help*_scored_raw.json exists and the record does not say why
- 'certification ran to completion' and 'certification passed' are different facts: record the raw_verdict text (e.g. 'F1 FIRES', 'IN BAND') with every certification claim
- repair-loop predictions use P1-P4, not F1-F5

**Cites.** `BP/ROUND4_PREREG.md:12-17`; `BP/ROUND4_PREREG.md:37-45`; `BP/ROUND4_PREREG.md:114-116`; `BP/ROUND4_PREREG.md:47-51`

### attempt / iteration / block / draw / frozen draw / pooled / seed / seal  (arc 2)

**Definition.** attempt 1 = the transfer measurement (frozen, never re-measured); attempts 2+ = repair measurements; iteration = the runbook cycle producing an attempt (iter 1 → attempt 2, iter 2 → attempt 3, iter 3 → attempt 4); block = a working block, the record's session-like unit, marked in its heading when autonomous ('CONSTRAINED-AUTONOMY BLOCK', 'AUTONOMOUS BLOCK CLOSE'); the record never marks a block attended — if the heading carries no autonomy marker, record attended BY EXPERIMENT CONVENTION with inferred=true; draw = a seeded sample of nodes; frozen draw = a draw re-used for re-measurement; pooled = a figure over more than one draw; seed = the registered RNG base; seal = a seeded 25% of exhaustive purchases held out single-use

**Hazards for translators.**
- attempt 1 and attempt 3 can share a numeric value at different tiers; never match on value alone
- pooling is used for the pooled panel-tier figure (BP/ITERATION_NOTES.md:274-275) and prohibited across seats (BP/L1L2_ADVERSARIAL_REVIEW.md:108); record pooled figures with the set pooled and do not merge them with per-attempt figures
- close events: iteration closes are entries whose heading contains 'CLOSE' with an iteration number (0005 'ITERATION 1, STEPS 4-5 (REALIZATION + CLOSE)', 0010 'ITERATION 2 CLOSE', 0014 'ITERATION 3 CLOSE'); block closes are 0023 'BLOCK WRAP', 0024 'BLOCK CLOSE', 0034 'AUTONOMOUS BLOCK CLOSE'; 0038 'QUERY-CLASS ARC CLOSED'. Step headings have the form 'ITERATION n, STEP k' and exist only for entries 0001-0014.

**Cites.** `BP/ITER1_ATTEMPT2_SCORED.json:2`; `BP/ITER1_ATTEMPT2_SCORED.json:167-168`; `BP/ITERATION_NOTES.md:643-651`; `BP/ITERATION_NOTES.md:673-675`; `BP/ROUND4_PREREG.md:79-80`; `BP/CALCULUS_RUNBOOK.md:134-136`; `BP/ITERATION_NOTES.md:141`; `BP/ITERATION_NOTES.md:266`; `BP/ITERATION_NOTES.md:346`; `BP/ITERATION_NOTES.md:673`

### dev behaviours vs repair-loop behaviours  (arc 2)

**Definition.** dev behaviours = helpfulness, harm-avoidance-to-third-parties, avoiding-over-and-under-caution (the three round-4 certifies); repair-loop behaviours = how-to-approach-tradeoffs (iterations 1-3, attempts 1-4) and user-autonomy (attempt-1 provisional, exhaustive 0.262); never-consulted block-2 behaviours also named: proportionate-risk, general-welfare, harmlessness-to-user, objectivity-on-contested-questions

**Hazards for translators.**
- a source may say 'tuned', 'mature', 'dev', 'iterated', 'never-consulted' for different sets; translate the behaviour NAME the span gives, AND record the span's own class word verbatim in a status field (never normalised, never inferred)

**Cites.** `BP/ROUND4_PREREG.md:13-14`; `BP/ITER1_ATTEMPT2_SCORED.json:3`; `BP/ITERATION_NOTES.md:556-559`; `BP/HANDOFF_CURRENT.md:174-179`

### panel / judges / panel-v5 / majority / split / dispute / quarantine  (arc 2)

**Definition.** frontier panel = data/behaviours.json, judges sol / kimi / fable / opus / kimi-k2 (3 per behaviour, 5 distinct); panel-v5 = data/panel-v5/, externally authored, 9 behaviours × both specs (BP/HANDOFF_CURRENT.md:181-184), 589 Model Spec passages in the review's cut (BP/L1L2_ADVERSARIAL_REVIEW.md:297), comparison layer only, never truth; majority supersedes single rulings; 2-1 majorities are 'split'; a dispute is a disagreement between seat and panel or between panels; quarantine = removing dispute resolutions from the instrument after a tripwire fires

**Conflicts in the record (unresolved).**
- panel-v5 positive rates: reviewer 0.012/0.044/0.007 (BP/L1L2_ADVERSARIAL_REVIEW.md:297) vs driver re-derivation 0.085/0.098/0.071 (BP/L1L2_REVIEW_DISPOSITION.md:35-37)
- three relevance ledgers with three constructs all called 'relevance' (BP/L1L2_ADVERSARIAL_REVIEW.md:296-300)

**Hazards for translators.**
- opposing unanimous panels on the same node exist (l3239_3382_n005, BP/ITERATION_NOTES.md:284-289); when a span records two rulings on one node, translate BOTH as separate claims marked contested; never let recency or dict order pick

**Cites.** `BP/PREREG_panel_equivalence.md:12-14`; `BP/HANDOFF_CURRENT.md:181-189`; `BP/ROUND4_PREREG.md:24-25`; `BP/ITERATION_NOTES.md:353-362`

### panel-internal agreement / test-retest / human-panelist baseline  (arc 2)

**Definition.** panel-internal agreement = inter-judge agreement on relevance verdicts over the same set, proposed as the ceiling and recorded as CURRENTLY UNMEASURED; test-retest = a seat's self-agreement (Fable single-wave 0.846); human-panelist baseline 71% = a figure asserted in the handoff and flagged as having NO source artifact

**Hazards for translators.**
- do not translate seat self-agreement, mint stability (0.98), split rates, or the owner's 21/22 spot-check as 'panel-internal agreement'; each is its own metric name

**Cites.** `BP/L1L2_ADVERSARIAL_REVIEW.md:215-217`; `BP/CALCULUS_RUNBOOK.md:130-132`; `BP/HANDOFF_CURRENT.md:108`; `BP/HANDOFF_CURRENT.md:210-211`; `BP/PREREG_panel_equivalence.md:68-75`

### node / passage / span / definition  (arc both)

**Definition.** node = a unit of the arc-2 document graph; passage = the panel's unit (589 in the true Model Spec universe, 374 constitution per SFE/HANDOFF.md:469-486 and the benchmark provenance table); span = a line range attached to a node, optionally carrying a quote; definition = (a) the behaviour definition text a seat receives, (b) one of the 100 query-class corpus items, (c) a norm-free 'definitional lane' node

**Conflicts in the record (unresolved).**
- node count: 773 (graph_v2/node_corpus_all.json and runs/ds7/root_graph.production.json) vs '593 at root unwind per GRAPH_OVERVIEW.md' vs 183 translated (coverage_translated.json) — all on BP/L1L2_ADVERSARIAL_REVIEW.md:288 and BP/L1L2_REVIEW_DISPOSITION.md:17-19; record which artifact a count is over

**Hazards for translators.**
- coverage figures exist over nodes (39/39) and over definitions (94/100, 100 defs); record the unit with every coverage figure
- passages→nodes is not an identity map (BP/L1L2_ADVERSARIAL_REVIEW.md:312)

**Cites.** `BP/L1L2_ADVERSARIAL_REVIEW.md:288`; `BP/L1L2_ADVERSARIAL_REVIEW.md:302`; `BP/L1L2_REVIEW_DISPOSITION.md:17-19`; `G2/graph_check.py:60-70`; `ARTIFACTS.md:19`; `BP/ITERATION_NOTES.md:769-771`

### erratum / recurrence / CoVe / tripwire / seat / certificate / brief-local / venue / handoff / seed  (arc 2)

**Definition.** erratum = an appended correction (registered numbers are never edited); numbered errata run #13-#21 in the ledger, four are unnumbered (entries 0001, 0004, 0009, 0013) and the ledger's own series tally counts them; recurrence = the record's own 'Nth instance/recurrence' of a defect class; CoVe = driver re-derivation of a reviewer's claim from data on disk (never expanded in the record); tripwire = a registered disagreement threshold whose firing is mechanical (quarantine or re-run); seat = a dispatched model instance receiving only a packet; certificate = a measured parity result licensing a cheaper tier, brief-local and task-class-local; venue = the concrete instrument configuration (wave+panel, all-Fable, certified-Opus, recovered lineage); handoff = a fresh session booting from committed files ('no compaction ritual, no handoff prompt'); seed = RNG base; decisive finding = a review finding the disposition marks as decisive and re-derives ('the three decisive findings were RE-DERIVED by the driver', BP/ITERATION_NOTES.md:836-838; 'The four decisive defects', entry 0043); review findings carry the record's own top-line words, copied verbatim: UNSUPPORTED, DOES-NOT-LICENSE, 'satisfiable by noise', 'at base rate', 'null-free', 'no null', BLOCKING, upheld

**Hazards for translators.**
- 'seat' in the ledger = a dispatched model instance; 'seats' in SFE/machine/query.py = a governance role with a producer and validator. Same word, two ontologies.
- 'reset' = a provider usage-window (capacity) reset, never a context reset (BP/HANDOFF_CURRENT.md:186-188; BP/ITERATION_NOTES.md:541-545)
- 'block' = a working block; unmarked blocks are attended

**Cites.** `BP/ROUND4_PREREG.md:35`; `BP/ITERATION_NOTES.md:438-441`; `BP/ITERATION_NOTES.md:861-864`; `BP/L1L2_REVIEW_DISPOSITION.md:12-13`; `BP/CALCULUS_RUNBOOK.md:43-44`; `BP/ROUND4_PREREG.md:26-28`; `BP/ITERATION_NOTES.md:429-433`; `BP/CALCULUS_RUNBOOK.md:110-113`; `BP/ITERATION_NOTES.md:832-840`; `BP/L1L2_REVIEW_DISPOSITION.md:7-10`

### MCC  (arc 1)

**Definition.** Matthews correlation coefficient, THE PRIMARY METRIC of benchmark.py; 0 by construction for degenerate predictors

**Authoritative artifact.** SFE/benchmark.py output on the named annotation config; HANDOFF tables are stated copies

**Denominator / population.** passages: 589 true universe / 377-333-153 published universe per behaviour

**Variants.** at least 30 distinct tool MCC values exist in SFE/HANDOFF.md (lines 44, 359, 480, 754-755, 777, 792, 829, 1046-1048, 1066-1073, 1116-1118, 1150-1152, 1233, 1257, 1390, 1402-1406), separated by threshold_rule and universe and annotation config

**Conflicts in the record (unresolved).**
- whether MCC is the metric at all: 'NOT MCC' (SFE/HANDOFF.md:61) vs 'Use MCC as the primary metric' (SFE/HANDOFF.md:592)
- SFE/benchmark.py's preamble text (item 5, 'the in-sample mean MCC (+0.274 published / +0.320 true) is a CEILING') vs its computed universe-delta table in the same run (+0.219 / +0.278 mean, b8 config); SFE/HANDOFF.md:480 carries +0.274/+0.320 for the @0.18 config
- gap 0.119→0.236 (HANDOFF:482) vs 0.120→0.235 (benchmark preamble)

**Hazards for translators.**
- every tool MCC must carry threshold_rule AND universe AND annotation config; a value matching without all three is not a match
- the in-sample figure is described by the record itself as 'a CEILING, not a result' (hindsight threshold)

**Cites.** `SFE/benchmark.py:661-684`; `SFE/HANDOFF.md:480-482`; `SFE/HANDOFF.md:44`

### judge MCC / leave-one-out / LOO / best per behaviour / LOBO  (arc 1)

**Definition.** leave-one-out (LOO) = one judge scored against the consensus of the other two, the record's stated bar; 'judges (mean of 3)' +0.555 on the true universe / +0.394 published; 'best per behaviour' +0.654; per-judge cells exist in benchmark output; LOBO = leave-one-BEHAVIOUR-out, a different thing, refused as a point estimate

**Authoritative artifact.** SFE/benchmark.py head-to-head table (per-judge, per-cell)

**Denominator / population.** 3 judges averaged per behaviour, from a 5-judge roster (fable/kimi/sol; kimi/opus/sol; fable/kimi-k2/sol)

**Hazards for translators.**
- 'mean LOO' in some HANDOFF lines is F1 (0.636/0.697/0.419), not MCC
- the small-model v2 panel (gpt-mini/haiku/qwen-small) is 'NEVER THE BAR'; label any judge figure by roster

**Cites.** `SFE/benchmark.py:25-28`; `SFE/benchmark.py:258-260`; `SFE/HANDOFF.md:481`; `SFE/HANDOFF.md:722`; `SFE/HANDOFF.md:602`

### universe (published vs true)  (arc 1)

**Definition.** true universe = every passage the judges graded (589 Model Spec / 374 constitution); published universe = after build_site_data.keeps_citation dropped every passage with summed score 0 (377/333/153 per behaviour; 863 total on the Model Spec side)

**Authoritative artifact.** SFE/panel_universe.py reconstruction (join 1.000 on all six cells)

**Hazards for translators.**
- 'Anything below quoting 377/333/153, 863 passages, 0.764/0.780/0.500, +0.274, +0.187 ... is a published-universe number and must be re-derived' (SFE/HANDOFF.md:501); translate such values with universe=published and the anti_rule flag

**Cites.** `SFE/HANDOFF.md:469-501`; `SFE/panel_universe.py:45-47`; `SFE/MODULE_MAP.md:61`

### join rate / recall ceiling (measure_join.py)  (arc 1)

**Definition.** fraction of panel passages that match a clause; matched/total over data/behaviours.json coverage passages

**Authoritative artifact.** live run of SFE/measure_join.py (prints 849/863 = 98.4% at the pin, wall 9.6 s)

**Denominator / population.** 863 = the PUBLISHED universe; measure_join.py never uses panel_universe.py

**Conflicts in the record (unresolved).**
- SFE/MODULE_MAP.md:54 'Do not quote 849/863 ... never cite the number from this table' vs SFE/HANDOFF.md:529, :1287, :1326-1331 quoting it

**Hazards for translators.**
- anti_rule: any translation of 849/863 or 98.4% carries the SFE/MODULE_MAP.md:54 prohibition verbatim
- SFE/measure_join.py:85-87 prints 'unmatched (N):' followed by the first 10 unmatched passages with the quote truncated to 100 characters; 14 are unmatched at the pin

**Cites.** `SFE/measure_join.py:1-9`; `SFE/measure_join.py:33-47`; `SFE/measure_join.py:74`; `SFE/measure_join.py:85-87`; `SFE/MODULE_MAP.md:54`

### clause inventory / ASP fragment  (arc 1)

**Definition.** SFE/modelspec_clauses.json = 593 clauses (SFE/MODULE_MAP.md:218); SFE/constitution_clauses.json = 616 clauses (SFE/MODULE_MAP.md:227); SFE/machine/rules.lp = 27 rules with ':-', SFE/machine/semantics.lp 18; SFE/machine/facts.lp 282 sourced facts (SFE/machine/README.md:47 says 281)

**Conflicts in the record (unresolved).**
- clause counts 593 / 589 / 587 / 586 circulate for the Model Spec (segmentation / ext_v1 annotation / b8 annotation / panel-visible) with the relation never stated
- a '15-rule fragment' count was corrected to 16 by adversarial review (SFE/adversarial_review_1.md:39); the machine/ rules.lp count is a different object (27)

**Hazards for translators.**
- 'rules' can mean the arc-1 pilot's ASP fragment (16) or machine/rules.lp (27); record the file

**Cites.** `SFE/MODULE_MAP.md:218`; `SFE/MODULE_MAP.md:227`; `SFE/machine/README.md:47`; `SFE/adversarial_review_1.md:39`

### behaviour-gold cell / judge's own false-positive rate  (arc 1)

**Definition.** gold cell = (behaviour × held-out judge), gold for judge j = both other judges relevant; 9 cells for the 3-behaviour panel; comparison at the judge's own FPR = tool TPR at the judge's (FPR, TPR) point; distinct from scoring cell = (behaviour × spec), 6 or 18

**Authoritative artifact.** SFE/benchmark.py ROC head-to-head table (judge wins 9/9 at the pin)

**Cites.** `SFE/benchmark.py:825-830`; `SFE/benchmark.py:715-721`; `SFE/HANDOFF.md:497-498`; `SFE/HANDOFF.md:574-575`

### cycle / cycle close / prediction freeze / adversarial review / decision.json  (arc 1)

**Definition.** a cycle = OPEN→PREDICT→IMPLEMENT→MEASURE→ADJUDICATE→CENSUS→DECIDE→CLOSE; close = one line appended to SFE/cycles/CYCLE_LOG.jsonl; prediction freeze = prediction.json sha-frozen, recorded as frozen_prediction_sha in state.json; adversarial review = review_verdict.json {verdict: proceed|blocked, by, notes} by someone other than the implementer; decision.json = signed keep/revert with justification

**Authoritative artifact.** SFE/cycles/<name>/ files and CYCLE_LOG.jsonl (6 closed cycles, 1 draft: segmentation-variants)

**Hazards for translators.**
- SFE/MODULE_MAP.md:121 says '7 cycle dirs, 5 of them closed ..., 2 open (join-integrity-v2, segmentation-variants)'; SFE/HANDOFF.md:249 says those two are 'drafts, pre-OPEN, not live work'; on disk at the pin CYCLE_LOG.jsonl has 6 lines and segmentation-variants holds drafts only. Three states in the record; translate each span's own words.
- the review verdict is stored three times (review_verdict.json, state.json gate.review, decision.json gate.review); translate once from review_verdict.json and link

**Cites.** `SFE/CYCLE_DESIGN.md:24-39`; `SFE/CYCLE_DESIGN.md:26-27`; `SFE/cycles/decoration-blind-join-2026-08-04/assignments/review.md:14-25`; `SFE/HANDOFF.md:284-286`

### seat / validator (machine/query.py)  (arc 1)

**Definition.** a governance seat = an LLM/human judgment step under a versioned brief between a deterministic producer and validator (sandwich rule); '*** NO VALIDATOR ***' = the model asserts the seat has none; '(none recorded)' = the model says nothing either way

**Authoritative artifact.** live run of SFE/machine/query.py seats (12 seats; attribution_author NO VALIDATOR; golden_review none recorded)

**Cites.** `SFE/REPRODUCIBILITY.md:38-41`; `SFE/machine/query.py:90-91`; `SFE/machine/README.md:66-70`; `SFE/machine/README.md:66-70`

### check_model.py checks  (arc 1)

**Definition.** the validator prints four PASS lines: (a) SOURCE CHECK, (b) DIFFERENTIAL CHECK vs cycle.py (282 comparisons), (c) KNOWN-ANSWER SET, (*) ACCEPTANCE TEST; it also reports 60 contradictions from rules.lp without failing

**Conflicts in the record (unresolved).**
- SFE/machine/README.md:98 heading says 'three independent checks'; SFE/machine/README.md:16 says 'the validator: 4 checks'; the run prints four PASS lines

**Cites.** `SFE/machine/README.md:16`; `SFE/machine/README.md:98`; `SFE/machine/check_model.py:1-40`

### graph_check.py output  (arc 2)

**Definition.** live run on runs/ds7/root_graph.production.json prints: nodes 773; bad line ranges 0 / 846 spans; bad quotes 0 / 602; spans with quotes 602 / 846; dangling (no provider) 25; authority-tagged headings captured 50 / 59 (wall 0.14 s at the pin). ARTIFACTS.md:19 summarises it as '773 nodes, zero bad spans of 846'

**Authoritative artifact.** live run (wall 0.14 s); CI runs the same command (.github/workflows/ci.yml:35)

**Hazards for translators.**
- 'zero bad spans of 846' is about line ranges; quote verification covers only the 602 quoted spans

**Cites.** `G2/graph_check.py:55-75`; `ARTIFACTS.md:19`; `.github/workflows/ci.yml:35`

### the three behaviours files  (arc 1)

**Definition.** data/behaviours.json = the panel answer key (3 behaviours, 6 cells, 1,336 passages per SFE/HANDOFF.md:618, verdicts+scores; FORBIDDEN token on the query path); engine/panel/behaviours.json = the vendored harness's 11-behaviour catalogue (definitions only, short slugs); semi-formal-experiment/behaviours_query.json = 3 behaviour definitions, no labels, the only legitimate query input

**Hazards for translators.**
- slug schemes differ (third-party-harm vs harm-avoidance-to-third-parties); never join on slug across files
- SFE/validate_behaviours.py still opens data/behaviours.json though filed superseded (SFE/MODULE_MAP.md:212; SFE/CYCLE5_REVIEW.md:30)

**Cites.** `SFE/behaviours_query.json:2-3`; `SFE/test_no_reference_leak.py:92-108`; `SFE/panel_v2.py:11-15`; `SFE/HANDOFF.md:618`; `SFE/HANDOFF.md:576-578`

### PRUNED.md  (arc 2)

**Definition.** evidence-prune manifest dated 2026-08-30: a four-column table (path, git object id, files, bytes) of 87 entries pinned by git tree/blob sha plus a TOTAL row; two entries carry the literal 'untracked-or-file' with 0 files; the restore instruction reads 'git checkout <pre-prune-commit> -- <path>' with <pre-prune-commit> unfilled; a 'Restored post-prune' section dated 2026-08-30 lists files restored after the first pass over-pruned. Translate the file's shape and text; do not summarise what it lacks.

**Cites.** `G2/PRUNED.md:1-12`; `G2/PRUNED.md:73`; `G2/PRUNED.md:99`; `G2/PRUNED.md:110-121`

### cite.py  (arc 1)

**Definition.** locator → verbatim text for both specs; 'outline model-spec' prints 80 sections; 'resolve' prints the sentence; CI runs resolve only

**Cites.** `engine/spec-cite/cite.py:2-33`; `.github/workflows/ci.yml:33`

### test suite counts  (arc 1)

**Definition.** every count written into a doc has gone stale; 'The command is the source of truth, not any number in this file'

**Authoritative artifact.** live run of pytest -q in SFE/ (the checker step runs it once and records the count and wall clock)

**Cites.** `SFE/MODULE_MAP.md:237`; `SFE/MODULE_MAP.md:246-250`; `SFE/HANDOFF.md:455`

### measurement modes: in-sample / fresh-draw / held-out (sealed) / generalization (transfer) / cross-document  (arc 2)

**Definition.** five non-interchangeable modes: (1) in-sample = on the accumulated adjudicated ledger ('all-truth'); (2) fresh-draw = new nodes with every prior-ruled node excluded, same behaviours; (3) held-out/sealed = a seeded partition of already-bought truth, withheld and single-use; (4) generalization/transfer = new behaviours never consulted (attempt 1 is the transfer verdict; attempts 2+ measure the repair, never transfer); (5) cross-document = a second document, which does not exist in the record and is stated as not measurable

**Conflicts in the record (unresolved).**
- round-4 registered bands were derived from all-truth (BP/ROUND4_PREREG.md:69-74) against contract §9e which forbids it; erratum E4 re-registers lineage bands so the file holds two registered prediction sets, the first retained as 'a recorded erratum'
- three transfer modules were repaired before scoring (BP/GENERALIZATION_BUILD_SPEC.md:33-42) yet their verdicts are reported as attempt-1 transfer claims

**Hazards for translators.**
- the record states explicit 'never report one as the other' rules, e.g. BP/PREREG_panel_equivalence.md:134-138 ('Reporting the tuned number alone is forbidden'), BP/GENERALIZATION_PREREG_DRAFT.md:109-110 ('Attempt-N verdicts measure THE REPAIR, never transfer'), BP/BLOCK2_TRANSFER_PREDICTIONS.md:107-111 (exhaustive precision 'never substitutes'), BP/ROUND4_PREREG.md:75-78 ('a population figure, not a sample'); every value carries its mode, attempt index, pool, and band basis
- no glossary in the record defines 'in-sample' or 'fresh draw'; both are defined only by what a pool excludes
- 'F1' names both an adversarial-review finding and a falsifier (BP/GENERALIZATION_BUILD_SPEC.md:53-61); record which

**Cites.** `BP/CHEAP_TIER_DRIVER_DESIGN.md:31-33`; `BP/ROUND4_PREREG.md:20-23`; `BP/UA_PLAN_REVIEW_DISPOSITION.md:11-17`; `BP/GENERALIZATION_PREREG_DRAFT.md:109-110`; `BP/ROSETTA.md:36-40`; `BP/TRANSLATION_CONTRACT_V2.md:188-192`

### opposing panel rulings on one node / defensible by contradiction  (arc 2)

**Definition.** a node can carry two unanimous panels on identical text under the identical brief with opposite verdicts (worked example: l3239_3382_n005); the scorer's recency precedence rules by default and the record flags this as unsafe; the owner's ruling scores such nodes as non-error in the match-or-defensible view only when both panels are full and unanimous; a 2-1 panel vs a wave does not qualify and stays contested-pending

**Hazards for translators.**
- translate each ruling on such a node as its own claim, mark the pair contested, never pick one

**Cites.** `BP/ITERATION_NOTES.md:284-289`; `BP/ITERATION_NOTES.md:299-311`; `BP/ITER2_REMEASURE_SCORED.json:188`

### semantic audit (SEMANTIC_AUDIT.md / semantic_audit.json)  (arc 2)

**Definition.** the stage-4 go/no-go audit of translation fidelity (module vs span), blind Fable auditors per cohort, rule: ≥85% faithful in the new-prompt cohort or pause; 16 cohorts; scope is ASP fidelity, explicitly partitioned from relevance matching

**Hazards for translators.**
- two earliest cohorts lack 'total' and 'verdict' fields; a per-cohort rate needs both

**Cites.** `G2/SEMANTIC_AUDIT.md:1-19`; `G2/semantic_audit.json:2`; `BP/PREREG_panel_equivalence.md:145`

### separability / matched-granularity random-partition null / base rate / binding method rule  (arc 2)

**Definition.** separability = the census's pass statistic over the leaf vocabulary (reported as 'sep 1.00'); the null = 'a content-free random 4-bucket-per-family partition of the leaf vocabulary' that 'achieves separability 1.00 in 299/300 seeded trials with reuse trivially 1.00'; base rate = the majority-class rate a relevance predictor is compared against ('1-NN relevance prediction over mid signatures = 0.72/0.70 vs bases'); the BINDING METHOD RULE: 'Every separability/representability claim ships with a MATCHED-GRANULARITY RANDOM-PARTITION NULL ... and the claim is only as strong as its MARGIN over that null'

**Authoritative artifact.** BP/RETRANS_REVIEW_DISPOSITION.md (CoVe re-derivations, driver-run); BP/ITERATION_NOTES.md 0042

**Denominator / population.** 300 seeded trials for the null; per-behaviour node sets for base rates (copy the fraction the span writes)

**Hazards for translators.**
- 'separability' values exist over definitions (0.37-0.40) and over nodes (0.85) (BP/ITERATION_NOTES.md:786-788); carry the unit
- the reviewer's numbers and the driver's re-derivations differ for some findings (BP/L1L2_REVIEW_DISPOSITION.md:35-43); translate both, tier=stated for the reviewer's, tier=cove for the re-derivation

**Cites.** `BP/RETRANS_REVIEW_DISPOSITION.md:9-14`; `BP/RETRANS_REVIEW_DISPOSITION.md:46-50`; `BP/RETRANS_REVIEW_DISPOSITION.md:60-66`; `BP/ITERATION_NOTES.md:836-840`

### symbolic engine: ASP/clingo evaluation, conflict enumeration, witness scenario, satisfiability (coherence) check, refusal  (arc 1)

**Definition.** conflict enumeration = 'Enumerate distinct norm conflicts in rules.lp and print one minimal-ish witness scenario per conflict' (SFE/run_conflicts.py:1-3) via clingo brave consequences; witness = 'One witness scenario for a given conflict, minimizing true ctx/interp atoms' (SFE/run_conflicts.py:37-38); coherence check = 'the definition/rule trigger is satisfiable under the vocabulary's composability axioms (via clingo)' (SFE/checker.py:7-9), returning a witness world for coherent definitions (SFE/checker.py:74-79); refusal = a deterministic module declining to emit a number or an answer, e.g. 'Degenerate inputs return refusals or floor values, never flattering ones' (SFE/MODULE_MAP.md:318), 'REFUSED' headline rows in benchmark.py, the '{{DOCFACTS marker is a refusal' (SFE/REPRODUCIBILITY.md:134), cycle.py 'REFUSED: 2 open cycles' (SFE/MODULE_MAP.md:34)

**Hazards for translators.**
- an engine failure event is any span recording the engine giving no answer (refusal, UNSAT with no witness, 'cannot enumerate') or a wrong answer (a conflict or witness later shown false, e.g. 'witnesses may describe impossible situations', SFE/emit_asp.py:285-290); record kind from the span's own words, refusal vs wrong_answer, and 'unstated' if the span does not say

**Cites.** `SFE/run_conflicts.py:1-13`; `SFE/run_conflicts.py:37-38`; `SFE/checker.py:1-13`; `SFE/checker.py:74-79`; `SFE/emit_asp.py:1-23`; `SFE/MODULE_MAP.md:318`; `SFE/REPRODUCIBILITY.md:134`; `SFE/MODULE_MAP.md:34`

### relevance-query output: hit / span locator / reason  (arc both)

**Definition.** arc 2: BP/panel_run1/relevance_by_act.json maps node_id → a list of act:polarity reason strings; the node id resolves to the graph node's spans (which may or may not carry a quote). arc 1: SFE/relevance.py Scorer.explain() returns matched_atoms with the spans licensing them; the record holds no committed per-hit explanation artifact for arc 1, so hits there come from a live run

**Hazards for translators.**
- a hit's span 'resolves to verbatim text' only if the node's span carries a quote that is a substring of the spec; 244 of 846 spans carry no quote (G2/graph_check.py output)

**Cites.** `BP/panel_run1/relevance_by_act.json:1-5`; `SFE/relevance.py:715-725`

### CI (.github/workflows/ci.yml)  (arc both)

**Definition.** copy the 'on:' block and the run steps verbatim from the file; do not summarise the trigger

**Cites.** `.github/workflows/ci.yml:1-35`

## Authoritative artifact map

- **arc2_ledger** — BP/ITERATION_NOTES.md entries 0000-0043 (LEDGER.md at root is a symlink to it); append-only by rule (BP/ROUND4_PREREG.md:35)
- **arc2_current_state** — BP/HANDOFF_CURRENT.md starred top block only (ARC2_HANDOFF.md at root symlinks to it); below the block is self-marked stale
- **arc1_current_state** — SFE/HANDOFF.md ⭐⭐⭐⭐ block (line 3) with a nested later ⭐⭐⭐⭐⭐ banner (line 5); 19 self-marked stale/retracted sections below
- **arc2_scored_values** — BP/ROUND4_DEV_TABLE.json; BP/round4_*_scored*.json; BP/ITER*_SCORED.json
- **arc1_scored_values** — live SFE/benchmark.py on a named annotation config; SFE/snapshots/*.json for cycle-era numbers
- **withdrawals_arc2** — BP/ITERATION_NOTES.md 0042 (integration census), 0043 (L1/L2); BP/L1L2_ADVERSARIAL_REVIEW.md + BP/L1L2_REVIEW_DISPOSITION.md; BP/RETRANS_REVIEW_DISPOSITION.md
- **withdrawals_arc1** — SFE/HANDOFF.md retraction sections (e.g. :469, :621, :705, :1097, :1188, :1352, :1380); SFE/WITHDRAWN_EXAMPLE_ASYMMETRY.md; SFE/structural.py:308, :323, :353 gate comments
- **routing** — ARTIFACTS.md
- **rules_and_anti_rules** — SFE/MODULE_MAP.md §11; AGENTS.md
- **git** — the full history to 48e66ce (656 commits); conventions below
- **symlinks** — LEDGER.md → BP/ITERATION_NOTES.md; ARC2_HANDOFF.md → BP/HANDOFF_CURRENT.md; CLAUDE.md → AGENTS.md (all at repo root; check with git ls-tree at the pin, mode 120000)

## Record conventions

- **ledger_entry_format** — '## NNNN — TITLE, YYYY-MM-DD'; entry 0000 embeds its date in the title; the three redacted stubs carry the date in parentheses. No entry carries a time. Entries 0000-0031 are all dated 2026-08-24 (32 entries); 0032-0043 are dated 2026-08-25. Sort by entry number, never by date. (BP/ITERATION_NOTES.md:7, :41, :71, :832)
- **ordering** — entry numbers are strictly monotone with the introducing commit's date for all 44 entries (checked); the order relation for ledger events is (date, entry number); for commits, (commit date, first-parent ordinal). Introducing commit of an entry: git log -S '## NNNN — ' --reverse (prefix only: six headings were rewritten on 2026-08-31, so searching the full current title finds the wrong commit).
- **append_only** — 45 commits touch ITERATION_NOTES.md; 44 are pure appends; exactly one deletes lines: 6d01415b (2026-08-31, +89/−121, 'Publication prep ... redact operational plumbing'). It replaced three entries by stubs marked '— [operational; redacted]' (0002, 0008, 0021), stripped quantitative operational data (usage %, points, token counts) from retained entries, replaced named owner attributions and verbatim quoted speech with role language ('Matt: ...' → 'RULING:' / 'the project owner'), and renamed the headings of 0032-0034. 29 retained entries were edited without a marker. (git log --stat -- BP/ITERATION_NOTES.md; git show 6d01415b)
- **redaction_marker** — the only in-place marker form is '— [operational; redacted]', three instances, all in ITERATION_NOTES.md. The commit says it redacted 'across ~60 docs' and modified 53 .md files; only the ledger received markers. Examples of unmarked edits with deletions: HANDOFF_CURRENT.md (removed a pre-existing ⚠️ correction line), ROUND4_PREREG.md, EXPERIMENTS.md, GENERALIZATION_PREREG_DRAFT.md. Pre-redaction content: git show 6d01415b^:<path>.
- **prereg_integrity** — all eight prereg documents plus PREREG_panel_equivalence.md were edited by 6d01415b. PREREG_panel_equivalence.md's own text says 'Editing this file after approval voids the registration' and carries a sha sidecar (PREREG_panel_equivalence.sha256) that matched immediately before 6d01415b and does not match after. The record nowhere adjudicates this; translators record the mechanical facts (file, hunk, sha before/after) and nothing more.
- **marking_systems** — three coexisting systems that do not agree: (a) ledger: append-only, superseded entries are withdrawn by a later numbered entry (0042 withdraws 0041); (b) handoffs: star count = recency of a state block, ⛔ = do not act on, ⚠️ = caveat, ~~strike~~ = retracted-but-retained; (c) delete-don't-annotate: 'A superseded number left in a doc is an instruction, not a footnote. Delete it' (SFE/HANDOFF.md:1357), applied in some sections and contradicted by 'nothing was silently deleted' (SFE/HANDOFF.md:292-294). (BP/ITERATION_NOTES.md:1-5; SFE/HANDOFF.md:292-294, :1352-1357; AGENTS.md:16-18)
- **git_totals** — 656 commits, 2026-08-02 to 2026-09-01; one merge; HEAD (branch d3-worked-example) == origin/main == public/main == 48e66ce0; local main is behind. Run git log from the pinned hash, never from 'main'.
- **git_trailers** — 620/656 commits carry one co-author trailer: 'Claude Fable 5' 460, 'Claude Opus 5 (1M context)' 104, 'Claude Opus 5' 14, 'Qwen-Coder' 41 (lowercase 'Co-authored-by'), 'Qwen Code' 1; 36 carry none. 'Claude-Session:' trailers on 361 commits. The driver's model tier is recoverable only from these trailers, never from the span. Two Opus trailer strings are one tier; a case-sensitive grep misses the Qwen commits.
- **history_rewrites** — reflog complete (661 entries); no rebase, filter-branch, or force-push recorded; six 'reset' entries are no-ops; exactly one amend (HEAD@{416}, message-only, diff empty, orphan 16bbbe59 survives). Consistent with 'History is published unrewritten' except for that message-only amend.
- **withdrawal_commit_conventions** — no fixed prefix; keywords in subjects: 'withdrawn:' (bf0d4978, 365d68b3, ecb2e9df, 86a703c1), 'WITHDRAW' (47779d8c), 'retracted' (94c24b3d, 2254f925, c04b80ef), 'rescinded' (a7a8ca8c), 'struck' (ae00660f, 12181ba0, 999f1403), 'Erratum #N' (#13-#21 each has a subject-visible commit), 'VOIDED' (2b1505bb). Subject-only and full-message keyword filters return different sets; record which filter produced a list.
- **overloaded_words** — reset = provider capacity reset; block = working block (attended unless marked autonomous); seat = model instance (ledger) vs governance role (machine/query.py); seed = RNG base; venue = instrument configuration; withheld = blinding a seat, not publication redaction; '[REDACTED]' inside specs/openai-model-spec/model_spec.md is upstream source content, not this project's redaction; F1 = falsifier or review finding; 'definition' has three senses (see node/passage/span/definition entry).; headline = (a) the round-4 match-or-adjudicated-defensible column, (b) 'THE HONEST HEADLINE IS RECALL' (a ledger entry's own summary line, BP/ITERATION_NOTES.md:280), (c) a 'headline claim' in a handoff starred block or writeup; 'README' unqualified in this glossary always means the file named in the citation (e.g. SFE/machine/README.md), never the repo root README

## Citation check

All entry citations resolve to an in-range line at the pin (line-bound check only; support is not machine-verified — see review_1.md).
