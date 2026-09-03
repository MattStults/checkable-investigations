# Claims to verify

README of https://github.com/MattStults/semi-formal-document-analysis at commit `48e66ce04a4d9f06771c42f89cb37b075583c5f6`, file `README.md`. Each item below quotes the README verbatim and names the value(s) asserted and the dimensions a verification must pin down.

## Quantitative / checkable claims

### Q01
> On the behaviors tuned during the arc-2 campaign, in-sample match-or-defensible rates against the panel reached 0.94–0.96, comparable to the panel's own internal agreement (measured on truth the loop iterated against; raw-match certification ran to completion on the three tuned behaviors, and the registered match-or-defensible pass never ran).

Values: `{"match_or_defensible_rate_range": [0.94, 0.96]}`  
Dimensions: metric: match_or_defensible_rate; tier: panel or adjudicated (in-sample: measured on truth the loop iterated against); snapshot: the measurement the record holds these values under (which document, which stage relative to certification) — to be recovered, not assumed final; denominator: per-behaviour engaged set size (needed); scope: the three dev behaviours: helpfulness, harm-avoidance-to-third-parties, avoiding-over-and-under-caution ('tuned' in the README; 'dev behaviours' in the record); supersession: the round-4 certification cells for the same behaviours (raw and headline columns) — report both; provenance_region: report

### Q02
> On the behaviors tuned during the arc-2 campaign, in-sample match-or-defensible rates against the panel reached 0.94–0.96, comparable to the panel's own internal agreement

Values: `{"panel_internal_agreement": "unstated; must be comparable to 0.94-0.96"}`  
Dimensions: metric: inter-judge agreement on relevance verdicts over the same node/passage set. Excludes seat self-agreement / test-retest, mint stability, split rates, and any struck value.; tier: panel; snapshot: whichever the record cites as the panel's agreement figure; denominator: pairs or nodes compared (needed); scope: the panel used for arc-2 truth; supersession: latest; 'struck' values reported as struck

### Q03
> raw-match certification ran to completion on the three tuned behaviors

Values: `{"tuned_behaviour_count": 3, "certification_completed_each": true, "certification_outcome_each": "record-supplied, README-silent: the raw verdict per behaviour (in band / falsifier fired), reported under X01"}`  
Dimensions: metric: count of tuned behaviours; per-behaviour certification_run status; tier: raw; snapshot: the certification run per behaviour; denominator: n/a; scope: the three dev behaviours (helpfulness, harm-avoidance-to-third-parties, avoiding-over-and-under-caution); supersession: n/a

### Q04
> the registered match-or-defensible pass never ran

Values: `{"registration_exists": true, "run_exists": false}`  
Dimensions: metric: event presence/absence; tier: git; snapshot: whole record through the pin; denominator: n/a; scope: the registered match-or-defensible certification pass; companion Q45 covers the round-4 headline column; supersession: n/a; registration_artifact: the pass 'ran' iff a run cites a registration of a match-or-defensible pass by filename, band, or amendment id. If the record holds MORE THAN ONE such registration and they answer oppositely, the claim terminates CONTESTED with both registrations named; the inventory does not pick the referent.; venue: commit history and ledger

### Q05
> # 2. the 773-node document graph, every span checked against the source

Values: `{"node_count": 773}`  
Dimensions: metric: node_count; tier: live_run (graph_check.py on runs/ds7/root_graph.production.json) and filesystem; snapshot: runs/ds7/root_graph.production.json at the pin; denominator: n/a; scope: graph_v2 production root graph; supersession: n/a

### Q06
> # 3. the measurement instrument, and its recall ceiling (98.4% join, misses printed by name)

Values: `{"join_rate": 0.984, "misses_printed_by_name": true}`  
Dimensions: metric: join_rate; tier: live_run (measure_join.py); snapshot: committed inputs at the pin; denominator: joined / total (both counts needed); scope: semi-formal-experiment measurement instrument; supersession: a re-run on the other universe if one exists; universe: published or true — record which; anti_rule: report if the record marks this figure do-not-cite

### Q07
> (`machine/check_model.py`, the companion source-check for step 5, also runs clean — all four checks pass.)

Values: `{"check_count": 4, "all_pass": true}`  
Dimensions: metric: check count and pass status; tier: live_run; snapshot: pin; denominator: 4; scope: semi-formal-experiment/machine/check_model.py; supersession: n/a

### Q08
> Constitution pilot (616 clauses, 16-rule ASP fragment, conflict enumeration, expressibility triage)

Values: `{"clause_count": 616}`  
Dimensions: metric: clause_count; tier: filesystem or live_run; snapshot: the clause inventory artifact the record names as the pilot's; denominator: n/a; scope: claude-constitution clause inventory, arc 1; supersession: later inventories may differ; record which is the pilot's

### Q09
> Constitution pilot (616 clauses, 16-rule ASP fragment, conflict enumeration, expressibility triage)

Values: `{"rule_count": 16}`  
Dimensions: metric: rule_count; tier: filesystem; snapshot: the ASP fragment artifact; denominator: n/a; scope: arc-1 constitution ASP fragment; supersession: report any correction of this count in the record

### Q10
> the Model Spec relevance benchmark against a frontier-judge panel on the full 589-passage universe

Values: `{"passage_count": 589}`  
Dimensions: metric: passage_count; tier: filesystem or live_run (benchmark.py); snapshot: the universe file benchmark.py reads at the pin; denominator: n/a; scope: Model Spec passage universe, arc 1; supersession: n/a; universe: published or true — must be recorded; README's own remark 'true vs published universe'

### Q11
> Document-graph translation (773 nodes), panel-adjudicated repair iterations, minted-dimension experiments, the query-class ontology study, and the adversarial reviews that ended the headline claims.

Values: `{"node_count": 773}`  
Dimensions: metric: node_count; tier: same as Q05; snapshot: same as Q05; denominator: n/a; scope: same as Q05; supersession: n/a

### Q12
> Arc-1 benchmark (Model Spec, 589-passage universe, MCC): the tool reached +0.32 in-sample (+0.278 label-free)

Values: `{"mcc_tool_in_sample": 0.32}`  
Dimensions: metric: mcc; tier: live_run (benchmark.py --tool) or stated; snapshot: the published arc-1 benchmark run; denominator: confusion counts over 589 passages x behaviours; scope: tool, in-sample (tuned threshold), Model Spec; supersession: the README's own 'true vs published universe' remark: record which universe; universe: published or true — must be recorded; README's own remark 'true vs published universe'; threshold_rule: in_sample

### Q13
> the tool reached +0.32 in-sample (+0.278 label-free)

Values: `{"mcc_tool_label_free": 0.278}`  
Dimensions: metric: mcc; tier: live_run or stated; snapshot: the label-free variant of the arc-1 benchmark; denominator: as Q12; scope: tool, label-free threshold; supersession: as Q12; universe: published or true — must be recorded; README's own remark 'true vs published universe'; threshold_rule: label_free

### Q14
> the frontier judges' leave-one-out mean was +0.555

Values: `{"mcc_judges_loo_mean": 0.555}`  
Dimensions: metric: mcc, leave-one-out mean over judges; tier: panel; snapshot: arc-1 benchmark; denominator: number of judges averaged, and the roster it is over; scope: frontier judge panel, Model Spec universe; supersession: n/a; universe: published or true — must be recorded; README's own remark 'true vs published universe'

### Q15
> the judges beat the tool in all nine behavior-gold cells at the judge's own false-positive rate

Values: `{"cell_count": 9, "judge_wins": 9}`  
Dimensions: metric: per-cell comparison at matched false-positive rate; tier: panel (judges) vs live_run/stated (tool); snapshot: arc-1 benchmark; denominator: 9 cells (behaviour x gold); scope: arc-1; supersession: n/a; universe: published or true — must be recorded; README's own remark 'true vs published universe'

### Q16
> Arc-2 repair loop (engaged precision, one behavior): 0.40 → 0.70 → 0.55 → 0.85 across four adjudicated attempts

Values: `{"series": [{"attempt": 1, "value": 0.4, "tier": "per element, to be recovered"}, {"attempt": 2, "value": 0.7, "tier": "per element, to be recovered"}, {"attempt": 3, "value": 0.55, "tier": "per element, to be recovered"}, {"attempt": 4, "value": 0.85, "tier": "per element, to be recovered"}], "attempt_count": 4}`  
Dimensions: metric: engaged_precision; tier: PER ELEMENT: each attempt's value carries its own tier (enum) and venue (free text); the series may be tier-mixed; snapshot: per-attempt, attempts 1-4, never pooled; denominator: engaged set size per attempt (needed for each); scope: one behaviour (name needed); supersession: per element: any adjusted or re-measured value for the same attempt in the same or a later entry

### Q17
> with the ledger's own honest headline being recall, not precision (23 of 40 declined passages were panel-relevant).

Values: `{"numerator": 23, "denominator": 40, "rate": 0.575}`  
Dimensions: metric: declined-set panel-relevant fraction (a recall-side miss rate); tier: panel; snapshot: the entry/attempt set the value is over; if pooled, snapshot=pooled plus the set; denominator: 40 declined passages; scope: the same behaviour as Q16; the README's 'passages' may be the record's 'nodes' (glossary term); supersession: later declined-set measurements may exist; record

### Q18
> The separability census ("integration test passed") — withdrawn in `bf0d4978`

Values: `{"withdrawal_commit": "bf0d4978", "withdrawn_item": "separability census / integration test"}`  
Dimensions: metric: commit existence and content; tier: git; snapshot: bf0d4978; denominator: n/a; scope: arc-2; supersession: n/a

### Q19
> its pass condition was satisfiable by noise (random partition passed 299/300 trials)

Values: `{"numerator": 299, "denominator": 300}`  
Dimensions: metric: random-partition null pass count; tier: stated, live_run, or cove — record which; snapshot: the review or disposition that reports it; denominator: 300 trials; scope: integration census null; supersession: n/a

### Q20
> relevance prediction over the representation ran at base rate.

Values: `{"prediction_accuracy": "equal to base rate (values needed)"}`  
Dimensions: metric: relevance-prediction accuracy vs base rate; tier: stated or live_run; snapshot: the review/disposition reporting it; denominator: prediction set size (needed); scope: 1-NN relevance prediction over the representation; supersession: n/a

### Q21
> The L1/L2 licensing experiments — withdrawn in `365d68b3`: DOES-NOT-LICENSE

Values: `{"withdrawal_commit": "365d68b3", "verdict": "DOES-NOT-LICENSE"}`  
Dimensions: metric: commit existence and content; tier: git; snapshot: 365d68b3; denominator: n/a; scope: L1/L2; supersession: n/a

### Q22
> one bar was already met by numbers indistinguishable from noise, the other had no null.

Values: `{"L1_finding": "bar met by noise-level numbers", "L2_finding": "no null"}`  
Dimensions: metric: review findings per experiment; tier: stated (review record); snapshot: the L1/L2 review; denominator: n/a; scope: L1 and L2 respectively (which is which must be recovered); supersession: n/a

### Q23
> The query-class saturation claim — bounded in `1143a921` (erratum #20)

Values: `{"commit": "1143a921", "erratum_number": 20}`  
Dimensions: metric: commit existence; erratum number and subject; tier: git and ledger; snapshot: 1143a921; ledger entry 0037; denominator: n/a; scope: query-class study; supersession: n/a

### Q24
> # 2,270 passed, 1 skipped (4-10 min depending on machine; measured 2026-08-30)

Values: `{"passed": 2270, "skipped": 1, "measured_date": "2026-08-30"}`  
Dimensions: metric: test_count by outcome; tier: live_run (pytest in semi-formal-experiment/) and stated; snapshot: pin (live) vs 2026-08-30 (stated); denominator: 2271 collected; scope: arc-1 suite; supersession: live run at the pin supersedes the stated date if they differ

### Q25
> the append-only ledger, entries 0000–0043

Values: `{"first_entry": "0000", "last_entry": "0043", "entry_count": 44}`  
Dimensions: metric: the set of entry numbers present equals {0000..0043} (gapless), not merely count = 44; tier: filesystem; snapshot: ITERATION_NOTES.md at pin; denominator: n/a; scope: arc-2 ledger; supersession: n/a

### Q26
> an ontology open-coded from 94 behavior definitions covered every sampled span

Values: `{"definition_count": 94}`  
Dimensions: metric: count of behaviour definitions coded; tier: filesystem or stated; snapshot: the query-class study's input set; denominator: n/a; scope: query-class ontology study; supersession: n/a

### Q27
> an ontology open-coded from 94 behavior definitions covered every sampled span

Values: `{"coverage": 1.0}`  
Dimensions: metric: span coverage (covered / sampled); tier: adjudicated or stated; snapshot: the coverage measurement the record reports; denominator: sampled span count and what a span is (node or definition) — the README binds coverage to the 94 definitions; report every coverage figure found; scope: query-class ontology; supersession: bf0d4978's message reports '39/39 blind coverage'; record which measurement the README means

### Q28
> but failed every separability test once a matched random-partition null was run against it.

Values: `{"separability_tests_passed_against_null": 0}`  
Dimensions: metric: per-test outcome against matched null; tier: stated or live_run; snapshot: the review/disposition; denominator: number of separability tests run (needed); scope: query-class ontology; supersession: n/a

### Q29
> it caught and withdrew three headline claims

Values: `{"withdrawn_headline_count": 3}`  
Dimensions: metric: count of distinct headline withdrawal events; tier: git and ledger; snapshot: whole record; denominator: n/a; scope: headline withdrawals: a withdrawal is 'headline' iff the withdrawn claim appeared in a handoff starred block or in the README. Arc-1 retractions exist and are reported under X01.; supersession: n/a

### Q30
> ⚠️ **Two different files are named `behaviours.json` and they are NOT interchangeable** — `data/behaviours.json` (the panel roster) and `engine/panel/behaviours.json` (the vendored harness's own copy); the experiment's query-side definitions are a differently named third file: `semi-formal-experiment/behaviours_query.json`.

Values: `{"paths": ["data/behaviours.json", "engine/panel/behaviours.json", "semi-formal-experiment/behaviours_query.json"], "distinct_contents": true}`  
Dimensions: metric: file existence and content inequality; tier: filesystem; snapshot: pin; denominator: n/a; scope: repo root; supersession: n/a

### Q31
> LEDGER.md          → the arc-2 append-only ledger (symlink)
> ARC2_HANDOFF.md    → the arc-2 handoff (symlink)

Values: `{"LEDGER.md": "symlink to walkthrough/.../behavior_pilot/ITERATION_NOTES.md", "ARC2_HANDOFF.md": "symlink to the arc-2 handoff file", "CLAUDE.md": "symlink to AGENTS.md (from 'For agents')"}`  
Dimensions: metric: symlink existence and target; tier: filesystem; snapshot: pin; denominator: n/a; scope: repo root; supersession: n/a

### Q32
> Large superseded run artifacts were pruned for publication with a signed manifest — see [`PRUNED.md`](walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/PRUNED.md) for what was removed and how to restore any of it from history.

Values: `{"manifest_path": "walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/PRUNED.md", "signed": "defined: a detached signature, a signer-attested checksum of the manifest itself, or an explicit signer line. Content-addressed (git object id) entries alone do NOT satisfy 'signed'.", "restorable_from_history": true}`  
Dimensions: metric: file existence; presence of a signature; restore commits resolve in git; tier: filesystem and git; snapshot: pin; denominator: n/a; scope: graph_v2 runs; supersession: n/a

### Q33
> | 1 (July–early Aug) | `semi-formal-experiment/` | ... | 2 (mid–late Aug) | `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/` |

Values: `{"arc1_window": "July to early August 2026", "arc2_window": "mid to late August 2026"}`  
Dimensions: metric: first and last commit dates touching each directory; tier: git; snapshot: whole history to pin; denominator: n/a; scope: the two directories named; supersession: n/a

### Q34
> CI runs both suites plus the citation and graph checks from the demo path on every push

Values: `{"workflow_steps": "enumerate exactly from ci.yml", "trigger": "as ci.yml states; README says 'every push'"}`  
Dimensions: metric: workflow file content; tier: filesystem; snapshot: .github/workflows/ci.yml at pin; denominator: n/a; scope: CI; supersession: n/a

### Q35
> `specs/openai-model-spec/` and `specs/claude-constitution/` are CC0 1.0 public-domain documents, redistributed with their upstream licence statements and README files intact ... `data/panel-v5/` redistributes data from ... (Andres Cotton), Apache-2.0 — see the LICENSE and NOTICE files in that directory. ... Everything else: MIT (see `LICENSE`).

Values: `{"specs_license": "CC0 1.0", "panel_v5_license": "Apache-2.0", "panel_v5_files": ["LICENSE", "NOTICE"], "root_license": "MIT"}`  
Dimensions: metric: file existence and license identifier text; tier: filesystem; snapshot: pin; denominator: n/a; scope: specs/, data/panel-v5/, LICENSE; supersession: n/a

### Q36
> # 1. every claim about a spec resolves to verbatim text
> python3 engine/spec-cite/cite.py outline model-spec
> python3 engine/spec-cite/cite.py resolve "model-spec@2025-12-18 > #avoid_sycophancy > ¶2 s1"

Values: `{"commands_exit_zero": true, "resolve_returns_verbatim_text": true}`  
Dimensions: metric: exit status and output shape; tier: live_run; snapshot: pin; denominator: n/a; scope: engine/spec-cite; supersession: n/a

### Q37
> # 5. the governance model as a queryable logic program (note the seat it reports as unvalidated)

Values: `{"unvalidated_seat_count": 1}`  
Dimensions: metric: count of seats the tool prints as '*** NO VALIDATOR ***'; seats printing '(none recorded)' are a distinct, separately reported state; tier: live_run (machine/query.py seats); snapshot: pin; denominator: seats reported (needed); scope: semi-formal-experiment/machine; supersession: n/a

### Q38
> operational details (usage plumbing, working notes) were redacted in the current files and remain in history by choice.

Values: `{"redaction_markers_present": true, "history_retains_content": true}`  
Dimensions: metric: redaction markers in current files; earlier commit contains the redacted text; tier: git and filesystem; snapshot: pin vs pre-redaction commit; denominator: n/a; scope: ledger entries marked '[operational; redacted]' and any other redacted files; supersession: n/a

### Q39
> The binding rule that came out of these: a separability claim is only as strong as its margin over a matched-granularity random-partition null, and a pass condition that cannot fail is void.

Values: `{"rule_recorded_as_binding": true}`  
Dimensions: metric: presence of the rule text marked binding in the record; tier: filesystem and git; snapshot: bf0d4978 or the disposition document; denominator: n/a; scope: arc-2 rulings; supersession: n/a

### Q40
> bash setup_env.sh --check    # verifies, ~3 s

Values: `{"wall_seconds_approx": 3}`  
Dimensions: metric: wall clock; tier: live_run; snapshot: pin, this machine; denominator: n/a; scope: setup_env.sh --check; supersession: n/a

### Q41
> Untuned behaviors never reliably reached that level.

Values: `{"threshold": 0.94, "any_untuned_reliably_at_or_above": false}`  
Dimensions: metric: match_or_defensible_rate (or the closest measured rate) per untuned behaviour, with certification status; tier: panel or adjudicated; snapshot: every untuned-behaviour measurement in the record; denominator: per-behaviour set size; scope: behaviours with status(b)=untuned; supersession: latest per behaviour; threshold_rule: record per measurement

### Q42
> [`ITERATION_NOTES.md`](walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/ITERATION_NOTES.md)

Values: `{"all_relative_links_resolve": true, "external_urls": "flagged, not checked (no network)"}`  
Dimensions: metric: every relative markdown link target exists at the pin; tier: filesystem; snapshot: pin; denominator: count of relative links in README (derived); scope: whole README; supersession: n/a

### Q43
> Everything below is deterministic re-analysis of committed data: no API keys, no network, no model calls.

Values: `{"start_here_sequence_runs_as_written": true}`  
Dimensions: metric: the five 'Start here' commands run in the order and working directories written, all exit 0; tier: live_run; snapshot: pin, this machine; denominator: 6 numbered steps (0-5), 7 command lines (step 1 has two); step 3's cd carries into 4 and 5; scope: README 'Start here' block including the cd in step 3 carrying into steps 4 and 5; supersession: n/a

### Q44
> # 2. the 773-node document graph, every span checked against the source

Values: `{"bad_line_ranges": 0, "bad_quotes": 0, "spans_total": "record-supplied", "spans_with_quotes": "record-supplied (may be fewer than spans_total)"}`  
Dimensions: metric: graph_check.py spans checked and failures; tier: live_run; snapshot: pin; denominator: spans_total for line ranges; spans_with_quotes for quote checks — 'every span checked' is evaluated against each; scope: runs/ds7/root_graph.production.json; supersession: n/a

### Q45
> the registered match-or-defensible pass never ran

Values: `{"round4_headline_column_exists": "record-supplied"}`  
Dimensions: metric: presence and values of a match-or-adjudicated-defensible ('headline') column in the round-4 scored files, and whether it cites the registration; tier: adjudicated; snapshot: round-4 scored files; denominator: per behaviour; scope: three dev behaviours; supersession: n/a; venue: round-4 scored files

### Q46
> Everything below is deterministic re-analysis of committed data: no API keys, no network, no model calls.

Values: `{"network_calls_on_demo_path": 0}`  
Dimensions: metric: static check: no urllib/requests/httpx/socket use reachable from the seven Start-here commands; tier: live_run (static analysis); snapshot: pin; denominator: 6 numbered steps (0-5), 7 command lines (step 1 has two); step 3's cd carries into 4 and 5; scope: demo path; supersession: n/a

### Q47
> The two share a corpus and nothing else.

Values: `{"both_arcs_primary_corpus": "the Model Spec under specs/openai-model-spec/"}`  
Dimensions: metric: corpus identity per arc; tier: filesystem; snapshot: pin; denominator: n/a; scope: both arcs; supersession: n/a

### Q48
> **Read only the top starred block of each handoff**: everything below is stacked historical state, self-marked and partly superseded

Values: `{"each_handoff_has_starred_top_block": true, "lower_sections_self_marked": "every section below the top starred block carries a date or an explicit superseded/archive marker"}`  
Dimensions: metric: the 'top starred block' is the first heading block marked with star glyphs; where a file has two star-marked blocks at the top, both are reported; tier: filesystem; snapshot: pin; denominator: 2 handoffs; scope: ARC2_HANDOFF.md target and semi-formal-experiment/HANDOFF.md; supersession: n/a

### Q49
> engine/            spec-cite (locator → verbatim text) and the vendored panel harness

Values: `{"layout_paths_exist": ["engine/", "specs/", "data/", "semi-formal-experiment/", "walkthrough/", "ARTIFACTS.md", "LEDGER.md", "ARC2_HANDOFF.md"]}`  
Dimensions: metric: path existence; tier: filesystem; snapshot: pin; denominator: 8 paths; scope: README Layout block; supersession: n/a

### Q50
> then answer deterministically, with a citable span and a stated reason for every hit.

Values: `{"identical_output_on_rerun": true}`  
Dimensions: metric: byte-identical output of the demo-path queries on two consecutive runs; tier: live_run; snapshot: pin, this machine; denominator: the Start-here commands that produce query output; scope: engine/spec-cite and semi-formal-experiment demo path; supersession: n/a

## Universally quantified prose claims (hypotheses)

### H01
> adversarial review before every close

Reading: Every time a cycle or iteration was closed, an adversarial review of that cycle or iteration had been recorded no later than the close.  
Rule: `∀c. event(c, cycle_close ∨ iteration_close) → ∃r. event(r, adversarial_review) ∧ ts(r) ≤ ts(c) ∧ links(r, c)`  
Scope: arc-1 cycles under semi-formal-experiment/cycles/ and arc-2 iteration/block closes in ITERATION_NOTES.md

### H02
> pre-registered predictions

Reading: Every measurement in a cycle was preceded by a frozen prediction for that cycle.  
Rule: `∀m,c. event(m, measurement) ∧ links(m, c) → ∃p. event(p, prediction_freeze) ∧ ts(p) < ts(m) ∧ links(p, c)`  
Scope: cycles and iterations that record a measurement

### H03
> an append-only ledger with an erratum list

Reading: The ledger was only ever added to, hunk by hunk, except hunks that are marked redactions or remove only operational content; and it records numbered errata.  
Rule: `(∀k,h. hunk(h, k, ITERATION_NOTES.md) ∧ deletes_prior_entry_text(h) → marked_redaction(h) ∨ operational_only(h)) ∧ ∃e. erratum(e, n, _) ∧ numbered(n)`  
Scope: ITERATION_NOTES.md across its full git history, per hunk not per commit

### H04
> blind adjudication seats

Reading: No adjudication seat was given panel labels, the cycle's design document, or prior verdicts as input.  
Rule: `∀d. event(d, seat_dispatch) → inputs(d) ∩ {panel_labels, design_doc, prior_verdicts} = ∅`  
Scope: seat dispatches recorded in cycle records and the ledger

### H05
> every step, every erratum, every withdrawal, written at the time

Reading: Each ledger entry's stated date is within one day of the date of the commit that first introduced it.  
Rule: `∀e. event(e, ledger_entry) → |ts(e) − ts(first_commit(e))| ≤ 1 day`  
Scope: entries 0000-0043

### H06
> the results that were withdrawn when adversarial review showed they were noise

Reading: Every arc-2 withdrawal was preceded by an adversarial review whose finding was noise, unsupported, does-not-license, or null-dominated.  
Rule: `∀w. event(w, withdrawal) → ∃r. event(r, adversarial_review) ∧ ts(r) ≤ ts(w) ∧ links(w, r) ∧ finding(r) ∈ {noise, unsupported, does_not_license, null_dominated}`  
Scope: arc-2 withdrawals (the sentence's referent). Arc-1 retractions are queried separately under X01 with self and cove as admissible catchers.

### H07
> Untuned behaviors never reliably reached that level.

Reading: No untuned behaviour has a certified match-or-defensible rate at or above 0.94, and none has two measurements from different attempts or draws both at or above 0.94.  
Rule: `∀b. status(b)=untuned → (¬∃m. certified(m) ∧ links(m,b) ∧ value(m) ≥ 0.94) ∧ (¬∃m1,m2. different_draw(m1,m2) ∧ links(m1,b) ∧ links(m2,b) ∧ value(m1) ≥ 0.94 ∧ value(m2) ≥ 0.94)`  
Scope: arc-2 behaviours

### H08
> the symbolic engine (ASP/clingo evaluation, conflict enumeration with witness scenarios, satisfiability checks) worked — its failures were refusals, not wrong answers.

Reading: Every recorded failure of the symbolic engine was a refusal to answer, not an incorrect answer.  
Rule: `∀f. event(f, engine_failure) → kind(f) = refusal`  
Scope: ASP/clingo evaluation, conflict enumeration, satisfiability checks, arc 1

### H09
> Matching behaviors to passages did not beat a single frontier judge on the arc-1 benchmark

Reading: The tool's MCC did not exceed the best individual judge's MCC on the arc-1 benchmark; a tie does not beat.  
Rule: `∀j. judge(j) → mcc(tool) ≤ mcc(j)`  
Scope: arc-1 benchmark; derived from Q12, Q13, Q14, Q15 plus per-judge values

### H10
> Large superseded run artifacts were pruned for publication with a signed manifest ... how to restore any of it from history.

Reading: There is a prune event with a signed manifest that states how to restore its artifacts, and every artifact it lists exists in an earlier commit.  
Rule: `∃k. event(k, prune) ∧ signed(manifest(k)) ∧ restore_instructions(manifest(k)) ∧ ∀a. listed(manifest(k), a) → ∃k'. ts(k') < ts(k) ∧ contains(k', a)`  
Scope: PRUNED.md and git history

### H11
> operational details (usage plumbing, working notes) were redacted in the current files and remain in history by choice.

Reading: Every section marked redacted had content in an earlier commit; and every hunk that deletes or replaces text of a previously written ledger entry is a marked redaction or removes only operational content.  
Rule: `(∀s. redaction_marker(s) → ∃k. ts(k) < ts(pin) ∧ has_content(k,s)) ∧ (∀h,k. hunk(h,k,ITERATION_NOTES.md) ∧ deletes_prior_entry_text(h) → marked_redaction(h) ∨ operational_only(h))`  
Scope: all '[operational; redacted]' markers and any other redaction markers at the pin

### H12
> then answer deterministically, with a citable span and a stated reason for every hit.

Reading: Every hit carries a span locator that resolves to verbatim text, and a reason.  
Rule: `∀h. hit(h) → ∃s. span(h,s) ∧ verbatim(s) ∧ ∃r. reason(h,r)`  
Scope: relevance-query outputs committed in the record (arc 2), and for arc 1 the live_run output of the committed explain path on the demo inputs (admitted as a witness source)

### H13
> the review, the independent re-derivation of each decisive finding, the corrected verdicts.

Reading: Every decisive finding of the withdrawal reviews (the census review and the L1/L2 review) was independently re-derived before the verdicts were corrected.  
Rule: `∀f,r. decisive_finding(f, r) → ∃d. event(d, cove) ∧ links(d,f) ∧ actor(d) ≠ actor(r) ∧ ts(d) ≤ ts(corrected_verdicts(r))`  
Scope: L1L2_ADVERSARIAL_REVIEW.md and its disposition; ledger entries 0042-0043

### H14
> every step, every erratum, every withdrawal, written at the time.

Reading: Every step that the runbook says emits a committed artifact, and whose artifact exists in the record for iterations 1–3, has a ledger entry naming that step.  
Rule: `∀i∈{1,2,3},s. step_artifact_exists(i,s) → ∃e. event(e, ledger_entry) ∧ links(e,(i,s))`  
Scope: iterations 1–3 (the entries with ITERATION n, STEP k headings); later entries have no step structure

### H15
> ARTIFACTS.md       routing table for every star artifact

Reading: Every path ARTIFACTS.md routes to exists at the pin.  
Rule: `∀a. listed(ARTIFACTS.md, a) → exists(a, pin)`  
Scope: ARTIFACTS.md at pin. The converse (every star artifact is listed) is OUT OF SCOPE: no star marking exists outside ARTIFACTS.md; filed as residue R13.

## Verdict statements (verify via their needs)

### V01
> It did not reach that bar on the axis that mattered — generalization.

Needs: in-sample rate on tuned behaviours (the bar reached in-sample); rate on untuned behaviours (generalization); the bar is defined (definitional provider)

### V02
> the symbolic engine (ASP/clingo evaluation, conflict enumeration with witness scenarios, satisfiability checks) worked

Needs: classification of every engine failure; an enumeration of engine failures exists in the record (else H08 is vacuous and V02 is unverifiable)

### V03
> Segmentation of both specs into typed clause inventories worked after repair.

Needs: a segmentation failure event; a repair event linked to it; a post-repair measurement of segmentation quality

### V04
> Matching behaviors to passages did not beat a single frontier judge on the arc-1 benchmark

Needs: tool MCC; judge MCC (per judge or LOO); per-cell comparison

### V05
> an ontology open-coded from 94 behavior definitions covered every sampled span but failed every separability test once a matched random-partition null was run against it.

Needs: coverage measurement; per-test separability outcome against null

### V06
> The measurement discipline — pre-registered predictions, blind adjudication seats, adversarial review before every close, an append-only ledger with an erratum list — is the part that transferred

Needs: each named discipline element instantiated in arc 2 (and in arc 1, for 'transferred')

### V07
> it caught and withdrew three headline claims

Needs: three DISTINCT headline withdrawal events (claim appeared in a handoff starred block or the README), each linked to a review

### V08
> Withdrawn, by its own review process

Needs: each withdrawal linked to a preceding review

### V09
> with the ledger's own honest headline being recall, not precision

Needs: a ledger entry stating recall as the headline; the recall-side number

### V10
> The binding rule that came out of these

Needs: the rule recorded as binding, dated after the withdrawals

### V11
> It establishes that the specific demonstrations attempted here did not survive their own review process

Needs: each demonstration linked to a failing review

### V12
> the adversarial reviews that ended the headline claims

Needs: review events linked to each ended claim

## Author commitments (report whether the record bears them out; no state required)

- **C01** > This repo is the complete record of the attempt: the machinery, the measurements, and the discipline that kept the measurements honest
- **C02** > The full commit history is published unrewritten so that every dated claim, pin, and withdrawal is externally checkable
- **C03** > Everything below is deterministic re-analysis of committed data: no API keys, no network, no model calls.
- **C04** > Claims are scoped throughout: every separability claim requires its null; every "unresolved conflict" is a claim about an encoding and a fragment, not about the document.
- **C05** > `AGENTS.md` (symlinked as `CLAUDE.md`) is the canonical brief: read it before acting in this repo.
- **C07** > This is the primary artifact.
