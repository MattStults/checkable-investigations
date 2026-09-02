# Claim inventory — README of semi-formal-document-analysis

Pinned: `48e66ce04a4d9f06771c42f89cb37b075583c5f6` (2026-09-01 17:44:18 -0700), file `README.md`.

Generated from `inventory.json` by `render.py`; the JSON is the source of truth.

## Dimension vocabulary

- **metric** — Named quantity (see glossary/ once frozen). Examples: match_or_defensible_rate, raw_match_rate, engaged_precision, mcc, node_count, clause_count, passage_count, join_rate, test_count, entry_count, trial_count.
- **tier** — How the number was produced. One of: raw (mechanical string/ID match, no judgment), panel (frontier-judge panel ruling), adjudicated (seat ruling folded with panel/human rulings), human (owner ruling), live_run (produced by running a committed script now), git (from commit metadata/history), filesystem (existence/shape of a committed file), stated (a number stated in a document with no re-derivation available).
- **snapshot** — Which point in the record: an attempt index, an iteration/entry number, a file version, a commit hash, or a date. Per-attempt series values are never pooled; a pooled value carries snapshot=pooled plus the set it pools.
- **denominator** — For every rate or fraction: the count the rate is over and what population it names.
- **scope** — Which behaviour(s), spec, universe, or directory the value is about.
- **supersession** — Whether a later artifact in the record replaces this value, and which.

## Event predicates (for hypotheses)

- `event(id, type, ts, source, quote)` — An event recorded in the record. type is one of: cycle_close, iteration_close, adversarial_review, prediction_freeze, measurement, ledger_entry, erratum, withdrawal, seat_dispatch, certification_run, registration, commit, prune, redaction, engine_failure.
- `links(a, b)` — Event a refers to b by name, id, hash, or entry number in its recorded text.
- `ts(e)` — The timestamp the record gives the event (a date in an entry, or a commit date).
- `inputs(d)` — For a seat_dispatch, the set of materials the record says the seat received.
- `finding(r)` — For a review, the recorded top-line finding (e.g. noise, unsupported, does_not_license, upheld).
- `kind(f)` — For an engine_failure, refusal or wrong_answer.
- `status(b)` — For a behaviour, tuned or untuned in the arc-2 campaign, as the record states.
- `actor(e)` — Who the record says performed the event: owner, driver, seat, panel, reviewer, script, unstated. Copied from the span, never inferred.
- `model_tier(e)` — Model tier the record names for the actor (e.g. Opus, Fable, Sonnet, Haiku), or unstated.
- `session(e)` — The working session the record places the event in: the ledger entry number or block name, plus date. Coarse by design.
- `context_origin(e)` — How the acting agent's context began, when the span states it: fresh, continued, compacted, seeded_by(<artifact>), unstated. A seed is an authored handoff (readable, checkable); a compaction is lossy and visible only by symptoms.
- `asserted_transfer(e, fact)` — A 'next agent must know' style line: event e hands fact forward to a successor.
- `erratum(e, n, class)` — Event e records erratum number n of defect class class (see forensic.defect_classes).
- `recurrence(e, e_prior)` — Event e says the same defect recurred from an earlier event or erratum e_prior.
- `caught_by(e)` — Who or what surfaced the misstep: owner, adversarial_review, tripwire, cove (chain-of-verification re-derivation), self, script, unstated.

## Quantitative / checkable claims

### Q01

> On the behaviors tuned during the arc-2 campaign, in-sample match-or-defensible rates against the panel reached 0.94–0.96, comparable to the panel's own internal agreement (measured on truth the loop iterated against; raw-match certification ran to completion on the three tuned behaviors, and the registered match-or-defensible pass never ran).

**Values:** `{"match_or_defensible_rate_range": [0.94, 0.96]}`

**Dimensions:**
- metric: match_or_defensible_rate
- tier: panel or adjudicated (in-sample: measured on truth the loop iterated against)
- snapshot: per tuned behaviour, final attempt of the arc-2 campaign
- denominator: per-behaviour engaged set size (needed)
- scope: the tuned arc-2 behaviours (README says three)
- supersession: must be the latest measurement per behaviour

### Q02

> On the behaviors tuned during the arc-2 campaign, in-sample match-or-defensible rates against the panel reached 0.94–0.96, comparable to the panel's own internal agreement

**Values:** `{"panel_internal_agreement": "unstated; must be comparable to 0.94-0.96"}`

**Dimensions:**
- metric: panel_internal_agreement (inter-judge)
- tier: panel
- snapshot: whichever the record cites as the panel's agreement figure
- denominator: pairs or nodes compared (needed)
- scope: the panel used for arc-2 truth
- supersession: latest

### Q03

> raw-match certification ran to completion on the three tuned behaviors

**Values:** `{"tuned_behaviour_count": 3, "certification_completed_each": true}`

**Dimensions:**
- metric: count of tuned behaviours; per-behaviour certification_run status
- tier: raw
- snapshot: the certification run per behaviour
- denominator: n/a
- scope: arc-2 tuned behaviours (names needed)
- supersession: n/a

### Q04

> the registered match-or-defensible pass never ran

**Values:** `{"registration_exists": true, "run_exists": false}`

**Dimensions:**
- metric: event presence/absence
- tier: git and ledger
- snapshot: whole record through the pin
- denominator: n/a
- scope: match-or-defensible certification pass
- supersession: n/a

### Q05

> # 2. the 773-node document graph, every span checked against the source

**Values:** `{"node_count": 773}`

**Dimensions:**
- metric: node_count
- tier: live_run (graph_check.py on runs/ds7/root_graph.production.json) and filesystem
- snapshot: runs/ds7/root_graph.production.json at the pin
- denominator: n/a
- scope: graph_v2 production root graph
- supersession: n/a

### Q06

> # 3. the measurement instrument, and its recall ceiling (98.4% join, misses printed by name)

**Values:** `{"join_rate": 0.984}`

**Dimensions:**
- metric: join_rate
- tier: live_run (measure_join.py)
- snapshot: committed inputs at the pin
- denominator: joined / total (both counts needed)
- scope: semi-formal-experiment measurement instrument
- supersession: n/a

### Q07

> (`machine/check_model.py`, the companion source-check for step 5, also runs clean — all four checks pass.)

**Values:** `{"check_count": 4, "all_pass": true}`

**Dimensions:**
- metric: check count and pass status
- tier: live_run
- snapshot: pin
- denominator: 4
- scope: semi-formal-experiment/machine/check_model.py
- supersession: n/a

### Q08

> Constitution pilot (616 clauses, 16-rule ASP fragment, conflict enumeration, expressibility triage)

**Values:** `{"clause_count": 616}`

**Dimensions:**
- metric: clause_count
- tier: filesystem or live_run
- snapshot: the clause inventory artifact the record names as the pilot's
- denominator: n/a
- scope: claude-constitution clause inventory, arc 1
- supersession: later inventories may differ; record which is the pilot's

### Q09

> Constitution pilot (616 clauses, 16-rule ASP fragment, conflict enumeration, expressibility triage)

**Values:** `{"rule_count": 16}`

**Dimensions:**
- metric: rule_count
- tier: filesystem
- snapshot: the ASP fragment artifact
- denominator: n/a
- scope: arc-1 constitution ASP fragment
- supersession: n/a

### Q10

> the Model Spec relevance benchmark against a frontier-judge panel on the full 589-passage universe

**Values:** `{"passage_count": 589}`

**Dimensions:**
- metric: passage_count
- tier: filesystem or live_run (benchmark.py)
- snapshot: the universe file benchmark.py reads at the pin
- denominator: n/a
- scope: Model Spec passage universe, arc 1
- supersession: n/a

### Q11

> Document-graph translation (773 nodes), panel-adjudicated repair iterations, minted-dimension experiments, the query-class ontology study, and the adversarial reviews that ended the headline claims.

**Values:** `{"node_count": 773}`

**Dimensions:**
- metric: node_count
- tier: same as Q05
- snapshot: same as Q05
- denominator: n/a
- scope: same as Q05
- supersession: n/a

*Note:* Same value as Q05, second sentence.

### Q12

> Arc-1 benchmark (Model Spec, 589-passage universe, MCC): the tool reached +0.32 in-sample (+0.278 label-free)

**Values:** `{"mcc_tool_in_sample": 0.32}`

**Dimensions:**
- metric: mcc
- tier: live_run (benchmark.py --tool) or stated
- snapshot: the published arc-1 benchmark run
- denominator: confusion counts over 589 passages x behaviours
- scope: tool, in-sample (tuned threshold), Model Spec
- supersession: the README's own 'true vs published universe' remark: record which universe

### Q13

> the tool reached +0.32 in-sample (+0.278 label-free)

**Values:** `{"mcc_tool_label_free": 0.278}`

**Dimensions:**
- metric: mcc
- tier: live_run or stated
- snapshot: the label-free variant of the arc-1 benchmark
- denominator: as Q12
- scope: tool, label-free threshold
- supersession: as Q12

### Q14

> the frontier judges' leave-one-out mean was +0.555

**Values:** `{"mcc_judges_loo_mean": 0.555}`

**Dimensions:**
- metric: mcc, leave-one-out mean over judges
- tier: panel
- snapshot: arc-1 benchmark
- denominator: number of judges averaged (needed)
- scope: frontier judge panel, Model Spec universe
- supersession: n/a

### Q15

> the judges beat the tool in all nine behavior-gold cells at the judge's own false-positive rate

**Values:** `{"cell_count": 9, "judge_wins": 9}`

**Dimensions:**
- metric: per-cell comparison at matched false-positive rate
- tier: panel vs tool
- snapshot: arc-1 benchmark
- denominator: 9 cells (behaviour x gold)
- scope: arc-1
- supersession: n/a

### Q16

> Arc-2 repair loop (engaged precision, one behavior): 0.40 → 0.70 → 0.55 → 0.85 across four adjudicated attempts

**Values:** `{"engaged_precision_series": [0.4, 0.7, 0.55, 0.85], "attempt_count": 4}`

**Dimensions:**
- metric: engaged_precision
- tier: adjudicated (README: 'adjudicated attempts')
- snapshot: per-attempt, attempts 1-4, never pooled
- denominator: engaged set size per attempt (needed for each)
- scope: one behaviour (name needed)
- supersession: each attempt supersedes the previous as 'current'; the series itself is the claim

### Q17

> with the ledger's own honest headline being recall, not precision (23 of 40 declined passages were panel-relevant).

**Values:** `{"numerator": 23, "denominator": 40, "rate": 0.575}`

**Dimensions:**
- metric: declined-set panel-relevant fraction (a recall-side miss rate)
- tier: panel
- snapshot: the attempt/entry the ledger records it in (needed)
- denominator: 40 declined passages
- scope: same behaviour as Q16
- supersession: later declined-set measurements may exist; record

### Q18

> The separability census ("integration test passed") — withdrawn in `bf0d4978`

**Values:** `{"withdrawal_commit": "bf0d4978", "withdrawn_item": "separability census / integration test"}`

**Dimensions:**
- metric: commit existence and content
- tier: git
- snapshot: bf0d4978
- denominator: n/a
- scope: arc-2
- supersession: n/a

### Q19

> its pass condition was satisfiable by noise (random partition passed 299/300 trials)

**Values:** `{"numerator": 299, "denominator": 300}`

**Dimensions:**
- metric: random-partition null pass count
- tier: live_run or stated (re-derivation artifact needed)
- snapshot: the review or disposition that reports it
- denominator: 300 trials
- scope: integration census null
- supersession: n/a

### Q20

> relevance prediction over the representation ran at base rate.

**Values:** `{"prediction_accuracy": "equal to base rate (values needed)"}`

**Dimensions:**
- metric: relevance-prediction accuracy vs base rate
- tier: stated or live_run
- snapshot: the review/disposition reporting it
- denominator: prediction set size (needed)
- scope: 1-NN relevance prediction over the representation
- supersession: n/a

### Q21

> The L1/L2 licensing experiments — withdrawn in `365d68b3`: DOES-NOT-LICENSE

**Values:** `{"withdrawal_commit": "365d68b3", "verdict": "DOES-NOT-LICENSE"}`

**Dimensions:**
- metric: commit existence and content
- tier: git
- snapshot: 365d68b3
- denominator: n/a
- scope: L1/L2
- supersession: n/a

### Q22

> one bar was already met by numbers indistinguishable from noise, the other had no null.

**Values:** `{"L1_finding": "bar met by noise-level numbers", "L2_finding": "no null"}`

**Dimensions:**
- metric: review findings per experiment
- tier: stated (review record)
- snapshot: the L1/L2 review
- denominator: n/a
- scope: L1 and L2 respectively (which is which must be recovered)
- supersession: n/a

### Q23

> The query-class saturation claim — bounded in `1143a921` (erratum #20)

**Values:** `{"commit": "1143a921", "erratum_number": 20}`

**Dimensions:**
- metric: commit existence; erratum number and subject
- tier: git and ledger
- snapshot: 1143a921; ledger entry 0037
- denominator: n/a
- scope: query-class study
- supersession: n/a

### Q24

> # 2,270 passed, 1 skipped (4-10 min depending on machine; measured 2026-08-30)

**Values:** `{"passed": 2270, "skipped": 1, "measured_date": "2026-08-30"}`

**Dimensions:**
- metric: test_count by outcome
- tier: live_run (pytest in semi-formal-experiment/) and stated
- snapshot: pin (live) vs 2026-08-30 (stated)
- denominator: 2271 collected
- scope: arc-1 suite
- supersession: live run at the pin supersedes the stated date if they differ

### Q25

> the append-only ledger, entries 0000–0043

**Values:** `{"first_entry": "0000", "last_entry": "0043", "entry_count": 44}`

**Dimensions:**
- metric: entry_count
- tier: filesystem
- snapshot: ITERATION_NOTES.md at pin
- denominator: n/a
- scope: arc-2 ledger
- supersession: n/a

### Q26

> an ontology open-coded from 100 behavior definitions covered every sampled span

**Values:** `{"definition_count": 100}`

**Dimensions:**
- metric: count of behaviour definitions coded
- tier: filesystem or stated
- snapshot: the query-class study's input set
- denominator: n/a
- scope: query-class ontology study
- supersession: n/a

### Q27

> an ontology open-coded from 100 behavior definitions covered every sampled span

**Values:** `{"coverage": 1.0}`

**Dimensions:**
- metric: span coverage (covered / sampled)
- tier: adjudicated or stated
- snapshot: the coverage measurement the record reports
- denominator: sampled span count (needed)
- scope: query-class ontology
- supersession: bf0d4978's message reports '39/39 blind coverage'; record which measurement the README means

### Q28

> but failed every separability test once a matched random-partition null was run against it.

**Values:** `{"separability_tests_passed_against_null": 0}`

**Dimensions:**
- metric: per-test outcome against matched null
- tier: stated or live_run
- snapshot: the review/disposition
- denominator: number of separability tests run (needed)
- scope: query-class ontology
- supersession: n/a

### Q29

> it caught and withdrew three headline claims

**Values:** `{"withdrawn_headline_count": 3}`

**Dimensions:**
- metric: count of withdrawal events on headline claims
- tier: git and ledger
- snapshot: whole record
- denominator: n/a
- scope: whole repo
- supersession: n/a

*Note:* The README's own 'Withdrawn' list names two items as withdrawn and one as 'bounded'. Whether 'bounded' counts as a withdrawal is a query-time question, flagged here.

### Q30

> ⚠️ **Two different files are named `behaviours.json` and they are NOT interchangeable** — `data/behaviours.json` (the panel roster) and `engine/panel/behaviours.json` (the vendored harness's own copy); the experiment's query-side definitions are a differently named third file: `semi-formal-experiment/behaviours_query.json`.

**Values:** `{"paths": ["data/behaviours.json", "engine/panel/behaviours.json", "semi-formal-experiment/behaviours_query.json"], "distinct_contents": true}`

**Dimensions:**
- metric: file existence and content inequality
- tier: filesystem
- snapshot: pin
- denominator: n/a
- scope: repo root
- supersession: n/a

### Q31

> LEDGER.md          → the arc-2 append-only ledger (symlink)
> ARC2_HANDOFF.md    → the arc-2 handoff (symlink)

**Values:** `{"LEDGER.md": "symlink to walkthrough/.../behavior_pilot/ITERATION_NOTES.md", "ARC2_HANDOFF.md": "symlink to the arc-2 handoff file", "CLAUDE.md": "symlink to AGENTS.md (from 'For agents')"}`

**Dimensions:**
- metric: symlink existence and target
- tier: filesystem
- snapshot: pin
- denominator: n/a
- scope: repo root
- supersession: n/a

### Q32

> Large superseded run artifacts were pruned for publication with a signed manifest — see [`PRUNED.md`](walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/PRUNED.md) for what was removed and how to restore any of it from history.

**Values:** `{"manifest_path": "walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/PRUNED.md", "signed": true, "restorable_from_history": true}`

**Dimensions:**
- metric: file existence; presence of a signature; restore commits resolve in git
- tier: filesystem and git
- snapshot: pin
- denominator: n/a
- scope: graph_v2 runs
- supersession: n/a

### Q33

> | 1 (July–early Aug) | `semi-formal-experiment/` | ... | 2 (mid–late Aug) | `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/` |

**Values:** `{"arc1_window": "July to early August 2026", "arc2_window": "mid to late August 2026"}`

**Dimensions:**
- metric: first and last commit dates touching each directory
- tier: git
- snapshot: whole history to pin
- denominator: n/a
- scope: the two directories named
- supersession: n/a

### Q34

> CI runs both suites plus the citation and graph checks from the demo path on every push

**Values:** `{"workflow_steps": ["arc-1 pytest", "arc-2 pytest", "cite.py check", "graph_check.py"], "trigger": "push"}`

**Dimensions:**
- metric: workflow file content
- tier: filesystem
- snapshot: .github/workflows/ci.yml at pin
- denominator: n/a
- scope: CI
- supersession: n/a

### Q35

> `specs/openai-model-spec/` and `specs/claude-constitution/` are CC0 1.0 public-domain documents, redistributed with their upstream licence statements and README files intact ... `data/panel-v5/` redistributes data from ... (Andres Cotton), Apache-2.0 — see the LICENSE and NOTICE files in that directory. ... Everything else: MIT (see `LICENSE`).

**Values:** `{"specs_license": "CC0 1.0", "panel_v5_license": "Apache-2.0", "panel_v5_files": ["LICENSE", "NOTICE"], "root_license": "MIT"}`

**Dimensions:**
- metric: file existence and license identifier text
- tier: filesystem
- snapshot: pin
- denominator: n/a
- scope: specs/, data/panel-v5/, LICENSE
- supersession: n/a

### Q36

> # 1. every claim about a spec resolves to verbatim text
> python3 engine/spec-cite/cite.py outline model-spec
> python3 engine/spec-cite/cite.py resolve "model-spec@2025-12-18 > #avoid_sycophancy > ¶2 s1"

**Values:** `{"commands_exit_zero": true, "resolve_returns_verbatim_text": true}`

**Dimensions:**
- metric: exit status and output shape
- tier: live_run
- snapshot: pin
- denominator: n/a
- scope: engine/spec-cite
- supersession: n/a

### Q37

> # 5. the governance model as a queryable logic program (note the seat it reports as unvalidated)

**Values:** `{"unvalidated_seat_count": 1}`

**Dimensions:**
- metric: count of seats reported unvalidated
- tier: live_run (machine/query.py seats)
- snapshot: pin
- denominator: seats reported (needed)
- scope: semi-formal-experiment/machine
- supersession: n/a

### Q38

> operational details (usage plumbing, working notes) were redacted in the current files and remain in history by choice.

**Values:** `{"redaction_markers_present": true, "history_retains_content": true}`

**Dimensions:**
- metric: redaction markers in current files; earlier commit contains the redacted text
- tier: git and filesystem
- snapshot: pin vs pre-redaction commit
- denominator: n/a
- scope: ledger entries marked '[operational; redacted]' and any other redacted files
- supersession: n/a

### Q39

> The binding rule that came out of these: a separability claim is only as strong as its margin over a matched-granularity random-partition null, and a pass condition that cannot fail is void.

**Values:** `{"rule_recorded_as_binding": true}`

**Dimensions:**
- metric: presence of the rule text marked binding in the record
- tier: filesystem and git
- snapshot: bf0d4978 or the disposition document
- denominator: n/a
- scope: arc-2 rulings
- supersession: n/a

### Q40

> bash setup_env.sh --check    # verifies, ~3 s

**Values:** `{"wall_seconds_approx": 3}`

**Dimensions:**
- metric: wall clock
- tier: live_run
- snapshot: pin, this machine
- denominator: n/a
- scope: setup_env.sh --check
- supersession: n/a

*Note:* Soft claim (approximate). Verified as order-of-magnitude only.

### Q41

> Untuned behaviors never reliably reached that level.

**Values:** `{"threshold": 0.94, "any_untuned_reliably_at_or_above": false}`

**Dimensions:**
- metric: match_or_defensible_rate (or the closest measured rate) per untuned behaviour, with certification status
- tier: panel or adjudicated
- snapshot: every untuned-behaviour measurement in the record
- denominator: per-behaviour set size
- scope: behaviours with status(b)=untuned
- supersession: latest per behaviour

*Note:* Also stated as hypothesis H07 for the event-shaped part ('reliably').

### Q42

> [`ITERATION_NOTES.md`](walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/ITERATION_NOTES.md)

**Values:** `{"all_relative_links_resolve": true, "external_urls": "flagged, not checked (no network)"}`

**Dimensions:**
- metric: every relative markdown link target exists at the pin
- tier: filesystem
- snapshot: pin
- denominator: count of relative links in README (derived)
- scope: whole README
- supersession: n/a

*Note:* Representative sentence; the claim covers every relative link in the README.

### Q43

> Everything below is deterministic re-analysis of committed data: no API keys, no network, no model calls.

**Values:** `{"start_here_sequence_runs_as_written": true}`

**Dimensions:**
- metric: the five 'Start here' commands run in the order and working directories written, all exit 0
- tier: live_run
- snapshot: pin, this machine
- denominator: 5 commands
- scope: README 'Start here' block including the cd in step 3 carrying into steps 4 and 5
- supersession: n/a

*Note:* Q06/Q07/Q36/Q37 check outputs; this checks the sequence as a reader would type it. The 'no network' half of the sentence stays commitment C03.

## Prose-claim hypotheses (round-trip for owner confirmation)

Each hypothesis has: the README words; my English reading (in); the rule; the rule rendered back to English (out). Owner confirms in == out.

### H01

> adversarial review before every close

- **English (in):** Every time a cycle or iteration was closed, an adversarial review of that cycle had already been recorded before the close.
- **Rule:** `∀c. event(c, cycle_close ∨ iteration_close) → ∃r. event(r, adversarial_review) ∧ ts(r) ≤ ts(c) ∧ links(r, c)`
- **English (out):** For every recorded cycle or iteration close, there exists an adversarial review whose recorded time is no later than the close and whose text refers to that cycle or iteration.
- **Declared dimensions translators must carry:** event type (cycle_close, iteration_close, adversarial_review); timestamp; linkage: the cycle/iteration id or entry number the review names
- **Scope:** arc-1 cycles under semi-formal-experiment/cycles/ and arc-2 iteration/block closes in ITERATION_NOTES.md

### H02

> pre-registered predictions

- **English (in):** Every measurement in a cycle was preceded by a frozen prediction for that cycle.
- **Rule:** `∀m,c. event(m, measurement) ∧ links(m, c) → ∃p. event(p, prediction_freeze) ∧ ts(p) < ts(m) ∧ links(p, c)`
- **English (out):** For every recorded measurement that belongs to a cycle, there is a prediction-freeze event for the same cycle with an earlier timestamp.
- **Declared dimensions translators must carry:** event type (measurement, prediction_freeze); timestamp; linkage: cycle id
- **Scope:** cycles and iterations that record a measurement

### H03

> an append-only ledger with an erratum list

- **English (in):** The ledger was only ever added to (except explicitly marked redactions), and it keeps a numbered list of errata.
- **Rule:** `(∀k. event(k, commit) ∧ touches(k, ITERATION_NOTES.md) → deleted_lines_in_prior_entries(k) = 0 ∨ event(k, redaction)) ∧ ∃L. erratum_list(L) ∧ numbered(L)`
- **English (out):** Every commit that changed the ledger file either deleted no lines from previously written entries or is recorded as a redaction; and the ledger contains a numbered erratum list.
- **Declared dimensions translators must carry:** event type (commit, redaction, erratum); timestamp (commit date); linkage: commit hash to file; erratum number
- **Scope:** ITERATION_NOTES.md across its full git history

### H04

> blind adjudication seats

- **English (in):** No adjudication seat was given panel labels, the cycle's design document, or prior verdicts as input.
- **Rule:** `∀d. event(d, seat_dispatch) → inputs(d) ∩ {panel_labels, design_doc, prior_verdicts} = ∅`
- **English (out):** For every recorded seat dispatch, the recorded inputs contain none of: panel labels, the cycle's design document, prior verdicts.
- **Declared dimensions translators must carry:** event type (seat_dispatch); timestamp; linkage: the inputs list the record gives for the dispatch
- **Scope:** seat dispatches recorded in cycle records and the ledger

### H05

> every step, every erratum, every withdrawal, written at the time

- **English (in):** Each ledger entry's stated date matches the date of the commit that first introduced it.
- **Rule:** `∀e. event(e, ledger_entry) → |ts(e) − ts(first_commit(e))| ≤ 1 day`
- **English (out):** For every ledger entry, the date written in its heading is within one day of the date of the first commit containing that entry.
- **Declared dimensions translators must carry:** event type (ledger_entry, commit); timestamp (heading date; commit date); linkage: entry number to introducing commit
- **Scope:** entries 0000-0043

### H06

> the results that were withdrawn when adversarial review showed they were noise

- **English (in):** Every withdrawal was preceded by an adversarial review whose finding was that the result was noise or unsupported.
- **Rule:** `∀w. event(w, withdrawal) → ∃r. event(r, adversarial_review) ∧ ts(r) ≤ ts(w) ∧ links(w, r) ∧ finding(r) ∈ {noise, unsupported, does_not_license, null_dominated}`
- **English (out):** For every recorded withdrawal there is an adversarial review, no later than the withdrawal and named by it, whose recorded finding is noise, unsupported, does-not-license, or null-dominated.
- **Declared dimensions translators must carry:** event type (withdrawal, adversarial_review); timestamp; linkage: the review the withdrawal names; finding
- **Scope:** all withdrawals in the record

### H07

> Untuned behaviors never reliably reached that level.

- **English (in):** No behaviour that was not tuned in the arc-2 campaign has a certified match-or-defensible rate at or above 0.94.
- **Rule:** `∀b. status(b) = untuned → ¬∃m. event(m, measurement) ∧ links(m, b) ∧ metric(m) = match_or_defensible_rate ∧ value(m) ≥ 0.94 ∧ certified(m)`
- **English (out):** For every untuned behaviour, there is no certified match-or-defensible measurement of that behaviour with a value of 0.94 or more.
- **Declared dimensions translators must carry:** event type (measurement, certification_run); timestamp; linkage: behaviour name; tuned/untuned status; value, tier, certification status
- **Scope:** arc-2 behaviours

### H08

> the symbolic engine (ASP/clingo evaluation, conflict enumeration with witness scenarios, satisfiability checks) worked — its failures were refusals, not wrong answers.

- **English (in):** Every recorded failure of the symbolic engine was a refusal to answer, not an incorrect answer.
- **Rule:** `∀f. event(f, engine_failure) → kind(f) = refusal`
- **English (out):** For every recorded engine failure, its kind is refusal.
- **Declared dimensions translators must carry:** event type (engine_failure); timestamp; linkage: which engine component; kind (refusal or wrong_answer)
- **Scope:** ASP/clingo evaluation, conflict enumeration, satisfiability checks, arc 1

### H09

> Matching behaviors to passages did not beat a single frontier judge on the arc-1 benchmark

- **English (in):** The tool's MCC was below every individual judge's MCC on the arc-1 benchmark.
- **Rule:** `∀j. judge(j) → mcc(tool) < mcc(j)`
- **English (out):** For every judge on the panel, the tool's MCC is less than that judge's MCC.
- **Declared dimensions translators must carry:** per-judge MCC values; tool MCC (which tier: in-sample or label-free); linkage: benchmark run
- **Scope:** arc-1 benchmark; derived from Q12, Q13, Q14, Q15 plus per-judge values

### H10

> Large superseded run artifacts were pruned for publication with a signed manifest ... how to restore any of it from history.

- **English (in):** There is a prune event with a signed manifest, and every artifact it lists can be found in an earlier commit.
- **Rule:** `∃k. event(k, prune) ∧ manifest(k) ∧ signed(manifest(k)) ∧ ∀a ∈ listed(manifest(k)). ∃k'. ts(k') < ts(k) ∧ contains(k', a)`
- **English (out):** A prune commit exists whose manifest carries a signature, and each artifact the manifest lists exists in some commit earlier than the prune.
- **Declared dimensions translators must carry:** event type (prune, commit); timestamp; linkage: manifest paths to commit hashes
- **Scope:** PRUNED.md and git history

### H11

> operational details (usage plumbing, working notes) were redacted in the current files and remain in history by choice.

- **English (in):** Every section marked redacted in the current files had content in an earlier commit.
- **Rule:** `∀s. redaction_marker(s) → ∃k. event(k, commit) ∧ ts(k) < ts(pin) ∧ has_content(k, s)`
- **English (out):** For every redaction marker in the current files, some earlier commit contains non-empty content at that section.
- **Declared dimensions translators must carry:** event type (redaction, commit); timestamp; linkage: section/entry to commit
- **Scope:** all '[operational; redacted]' markers and any other redaction markers at the pin

## Verdict nodes (named needs and candidate providers)

A verdict verifies exactly when all its needs resolve to providers that verify. A need with no provider is loose language and is printed by name in results.

### V01

> It did not reach that bar on the axis that mattered — generalization.

- **Needs:** in-sample rate on tuned behaviours (the bar reached in-sample); rate on untuned behaviours (generalization)
- **Candidate providers:** Q01, Q41/H07

### V02

> the symbolic engine (ASP/clingo evaluation, conflict enumeration with witness scenarios, satisfiability checks) worked

- **Needs:** classification of every engine failure
- **Candidate providers:** H08

### V03

> Segmentation of both specs into typed clause inventories worked after repair.

- **Needs:** a segmentation failure event; a repair event linked to it; a post-repair measurement of segmentation quality
- **Candidate providers:** **none — dangling**
- *Note:* No adjacent README sentence provides any of the three needs; Q08/Q10 give inventory sizes only. Candidate dangling verdict.

### V04

> Matching behaviors to passages did not beat a single frontier judge on the arc-1 benchmark

- **Needs:** tool MCC; judge MCC (per judge or LOO); per-cell comparison
- **Candidate providers:** Q12, Q13, Q14, Q15, H09

### V05

> an ontology open-coded from 100 behavior definitions covered every sampled span but failed every separability test once a matched random-partition null was run against it.

- **Needs:** coverage measurement; per-test separability outcome against null
- **Candidate providers:** Q26, Q27, Q28, Q19, Q20

### V06

> The measurement discipline — pre-registered predictions, blind adjudication seats, adversarial review before every close, an append-only ledger with an erratum list — is the part that transferred

- **Needs:** each named discipline element instantiated in arc 2 (and in arc 1, for 'transferred')
- **Candidate providers:** H01, H02, H03, H04

### V07

> it caught and withdrew three headline claims

- **Needs:** three withdrawal events each linked to a review
- **Candidate providers:** Q29, Q18, Q21, Q23, H06
- *Note:* Q23 says 'bounded', not 'withdrawn'; provider set may resolve to two, not three.

### V08

> Withdrawn, by its own review process

- **Needs:** each withdrawal linked to a preceding review
- **Candidate providers:** H06

### V09

> with the ledger's own honest headline being recall, not precision

- **Needs:** a ledger entry stating recall as the headline; the recall-side number
- **Candidate providers:** Q17
- *Note:* 'honest' is residue (R11); the factual need is the ledger's stated headline.

### V10

> The binding rule that came out of these

- **Needs:** the rule recorded as binding, dated after the withdrawals
- **Candidate providers:** Q39

### V11

> It establishes that the specific demonstrations attempted here did not survive their own review process

- **Needs:** each demonstration linked to a failing review
- **Candidate providers:** H06, Q18, Q21

### V12

> the adversarial reviews that ended the headline claims

- **Needs:** review events linked to each ended claim
- **Candidate providers:** H06

## Author commitments (typed; declare no needs)

- **C01** — > This repo is the complete record of the attempt: the machinery, the measurements, and the discipline that kept the measurements honest
- **C02** — > The full commit history is published unrewritten so that every dated claim, pin, and withdrawal is externally checkable
- **C03** — > Everything below is deterministic re-analysis of committed data: no API keys, no network, no model calls.
- **C04** — > Claims are scoped throughout: every separability claim requires its null; every "unresolved conflict" is a claim about an encoding and a fragment, not about the document.
- **C05** — > `AGENTS.md` (symlinked as `CLAUDE.md`) is the canonical brief: read it before acting in this repo.
- **C06** — > `ARTIFACTS.md` at root is the full routing table.
- **C07** — > This is the primary artifact.

## Evaluative residue (out of scope, listed verbatim)

- **R01** — > it is the reason the numbers in this repo can be read at face value.
- **R02** — > the discipline that kept the measurements honest
- **R03** — > The two share a corpus and nothing else. Different representation, different failure modes, different evidence.
- **R04** — > an archive, not a read.
- **R05** — > The withdrawn results are defects in measurements, not proofs about the ontology.
- **R06** — > it documents that process well enough to be reused.
- **R07** — > the tool should match the panel, or give an answer a frontier model would accept as justifiable.
- **R08** — > on the axis that mattered
- **R09** — > Loading the wrong one produces a silently de-behaviourised score.  
  *Mechanistic and in principle runnable, but out of the inventory's scope: it asserts a counterfactual misuse, not a recorded measurement.*
- **R10** — > Frontier-model panels were the calibration instrument  
  *Descriptive framing; not a measurable claim.*
- **R11** — > the ledger's own honest headline
- **R12** — > ## What this repo does not establish ... That the approach is impossible.

## Forensic layer (pre-registered addendum; not README-derived)

Declared before freeze as a pre-registered addendum. NOT README-derived; not part of the registered expectations, which are scored over Q/H/V claims only. Forensic query outcomes are reported in a separate results table with their own unverifiable count.

**Why:** The record must support tracing what agent did what when the work went wrong, not only verifying the README. The ledger already carries this vocabulary natively (entry 0000 'SEED: tacit operational knowledge', erratum #16 'stale reset belief', erratum #21 'FOURTH recurrence', 'next agent must know' lines, errata series '4,4,4,2*,1'), so the dimensions are recoverable from spans without inference.

**Required on event spans:** actor; session; context_origin (unstated allowed); erratum number and class where the span records an erratum; recurrence link where the span says a defect recurred; caught_by where the span says who caught it; asserted_transfer where the span hands a fact forward

**Derived at query time, not translated:** fix_artifact(e): what an erratum produced; fired_after_fix(e): whether the class recurred after its fix; belief state of an agent at a time (only its proxy, asserted_transfer plus later contradiction, is translated)

**Defect classes:**
- `stale_belief` — acting on a remembered fact that had changed (erratum #16's class: 'dates not anchors')
- `scope_stretched_certificate` — using a validation certificate outside the brief it was earned on (erratum #14's class)
- `underspecified_vocabulary` — a coding or judgment vocabulary too loose to be applied consistently (erratum #19's class)
- `unfalsifiable_pass` — a pass condition satisfiable by noise or that cannot fail (the census withdrawal's class)
- `missing_null` — a claim with no null or baseline (L2's class)
- `wrong_artifact` — loading or citing the wrong file or tier (the behaviours.json trap; raw vs panel)
- `transcript_only_procedure` — a ruling or procedure that lived in a transcript instead of the repo
- `mixed_snapshots` — pooling or comparing values across attempts, tiers, or superseded entries
- `other` — record the span's own words for the class

**Glossary hazard:** 'reset' in the ledger means a provider usage-window reset, not a context reset. The glossary must define both and translators must not map one to the other.

**Pre-registered forensic queries:**
- **F01** — Does any defect class recur after a session boundary or seeding event more often than within a session?  
  needs: session, context_origin, erratum class, recurrence
- **F02** — Did the errata series converge by class, not just by count? List classes with a recurrence after their first fix.  
  needs: erratum number and class, recurrence, session
- **F03** — Which catch mechanism surfaced which defect class? Did self-catching ever surface a continuity (stale_belief) failure?  
  needs: caught_by, erratum class
- **F04** — For every asserted transfer, does a later span contradict or violate it, and by which actor?  
  needs: asserted_transfer, actor, session, linkage
- **F05** — Was any certificate or validated seat used outside the brief it was scoped to?  
  needs: actor, model_tier, linkage to brief/certificate, erratum class scope_stretched_certificate

## Coverage and additional query classes (second addendum)

**Span assignment:** Translation is EXHAUSTIVE over the primary sources named in the orchestration (arc-2 ledger entries 0000-0043, the round4_*_scored_raw.json and ITER*_SCORED.json files, semantic_audit.json / SEMANTIC_AUDIT.md, graph_check.py and benchmark.py outputs, the git log), not targeted at spans that look relevant to README claims. Reason: targeting would have to come from the orchestrator, who has seen the README, and it would make omission questions unanswerable.

**README provenance:** readme_blame.json records, for every README line at the pin, the commit, date, author and commit summary that introduced it. Produced by git blame; the pinned README is 193 lines, 165 of them from the 2026-08-31 publication-prep commit 6d01415b, with two correction commits on 2026-09-01 (6b9849f9 'scope the headline verdict', 3f87fd40 'certification claim corrected').

**Additional query classes:**
- **X01** — For each README metric, list every value of that metric in the record (all behaviours, attempts, tiers) and locate the README's pick among them: best, latest, representative, or unstated basis.  
  needs: exhaustive coverage, metric, scope, snapshot, tier
- **X02** — For each contradicted claim: was the README value ever true in the record (true-then-superseded) or never true? Uses the README line's blame date against the record's supersession dates.  
  needs: readme_blame.json, supersession, timestamp
- **X03** — For each withdrawn or bounded claim, was the README sentence about it written before or after the withdrawal commit, and by which actor?  
  needs: readme_blame.json, withdrawal events, actor
- **X04** — Direction of every discrepancy: README overstates or understates relative to the record.  
  needs: contradicted claims with both values
- **X05** — Evidence grade per verified claim: re-run, scored file, or stated-only. Fraction of dated claims reaching a definite state, reported against commitment C02.  
  needs: tier field on ledger claims
- **X06** — Internal consistency: README claims that constrain the same quantity (e.g. Q29 vs the withdrawn list; Q05 vs Q11) and whether they agree.  
  needs: inventory only

**Out of scope, noted:** Sibling documents (AGENTS.md, ARTIFACTS.md, handoffs, blog posts) make overlapping claims (e.g. AGENTS.md '~2,270 pass, ~8 min' vs README '2,270 passed, 1 skipped, 4-10 min'). Not inventoried; noted as a future target set.

## Verbatim check

All 85 quoted sentences are verbatim substrings of the pinned README.
