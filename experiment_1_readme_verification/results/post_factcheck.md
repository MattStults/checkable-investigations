# Fact-check of the blog post's "Post-experiment summary" and "Results" sections

Post: `mattstults.github.io/_posts/2026-09-01-readme-verification-pilot.md`
Checked by a clean-context fact-checker against the committed artifacts under
`experiment_1_readme_verification/` (and, for target-repo figures, read-only
git in `semi-formal-document-analysis`). Numbers only; framing and opinion
are out of scope.

## A. Every quantitative claim

| # | claim as written | artifact / command | derived | verdict |
|---|---|---|---|---|
| 1 | 50 quantitative claims, 15 hypotheses, 12 verdict nodes | `claim_inventory/inventory.json` lengths | 50 / 15 / 12 (also 6 commitments, 13 residue) | PASS |
| 2 | inventory and glossary "tagged in the repo" | `git tag` | `exp1-inventory-frozen`, `exp1-glossary-frozen` | PASS |
| 3 | 1,686 spans cut mechanically | `wc -l ledger/spans/spans.jsonl` | 1686 | PASS |
| 4 | Sonnet at parity on git log, 50 of 53 numbers | `results/capability_breakdown.md` batch_052 row `50 / 53 / 53` | 50 of 53 | PASS |
| 5 | Sonnet 74% numeric / 84% event-type recall on prose | `results/capability_probe.md` ("prose numbers 74%, prose event types 84%") | same | PASS |
| 6 | Twelve numbered design changes D-01..D-12 | `results/intervention_log.md` headings | D-01..D-12 (+D-12b) | PASS |
| 7 | Seven translator interventions I-01..I-07 | same | I-01..I-07 | PASS |
| 8 | one class recurred after its fix (I-06 then G-06) | intervention_log lines 219-237 | I-06 → G-05 → recurrence → G-06 | PASS |
| 9 | three late deviations D-09, D-10, D-11 share one cause | intervention_log D-09/D-10/D-11 entries | same | PASS |
| 10 | claims in the final ledger: 14,721 | `wc -l ledger/claims.jsonl` | 14721 | PASS |
| 11 | checker pass on final re-check: 14,721 of 14,721 | `ledger/check_result.json` summary | total 14721, passed 14721, failed 0 | PASS |
| 12 | 0 checker failures | same (`failed: 0`, `fail_reasons: {}`) | 0 | PASS |
| 13 | 219 claims rejected by the checker across the run | sum of `rejected` over `results/translation_log.jsonl` (151 runs) | 17 opus + 202 sonnet = 219 | PASS (note: de-duplicating to the last check per file, as `failure_modes.py` does, gives 205; "across the run" = every check run) |
| 14 | 29 spans without a claim | `ledger/spans_without_claims.json` | 29 ids | PASS |
| 15 | "all pre-redaction spans identical to current text" | span classes for those 29 in `ledger/spans/spans.jsonl`; whitespace-normalised text compared with current-file spans of the same path | 29/29 are `*_preredaction`; 29/29 text-identical to a current span | PASS |
| 16 | 100 claims reported contested | `ledger/claims.jsonl`, `stance == "contested"` | 100 | PASS |
| 17 | numeric literals carried 97% (4,368 of 4,501) | `results/completeness_audit.md` "all" row | 4368/4501 = 97.0% | PASS |
| 18 | event markers carried 95% | same (216/228) | 94.7% | PASS |
| 19 | backticked paths 71% | same (522/739) | 70.6% | PASS |
| 20 | Opus checker rejection rate 0.12% | translation_log: 17/14,624; `results/tier_probe.md` | 0.116% → 0.12% | PASS |
| 21 | Sonnet rejection rate 3.32% | translation_log: 202/6,092 | 3.316% → 3.32% | PASS |
| 22 | baseline: 27 minutes | `baseline/COST.md`, `baseline/REPORT.md` header | 27 min 09 s | PASS |
| 23 | baseline: 89 tool calls | `baseline/COST.md` | 89 | PASS |
| 24 | baseline: 320k tokens | `baseline/COST.md` | 320,488 | PASS |
| 25 | baseline: 77 items | `baseline/citations_check.json` summary `items` | 77 (= 50 Q + 15 H + 12 V) | PASS |
| 26 | ledger arm, quantitative (50): 40/5/5/0 | `results/arm_comparison.json` group Q; re-derived from `results/query_results.json` | 40 verified, 5 contradicted, 5 contested, 0 other | PASS |
| 27 | ledger arm, hypotheses (15): 10/3/2/0 | same, group H | 10/3/2/0 | PASS |
| 28 | ledger arm, verdict nodes (12): 3/2/6/1 dangling | same, group V | 3/2/6/1 | PASS |
| 29 | baseline, all 77: 54/12/6/5 | arm_comparison baseline sub-counts summed (38+11+5; 9+2+1; 2+0+4; 1+2+2) | 54/12/6/5 | PASS |
| 30 | Agreement: 60 of 77 | `arm_comparison.json` `agreement_total` (43+11+6) | 60/77 | PASS |
| 31 | 24 items ended non-verified in the ledger | query_results: 77 − 53 verified | 24 | PASS |
| 32 | 11 label only / 13 substance | `results/rulings/rulings_summary.json` counter | label 11, substance 13 | numbers PASS, **denominator MISMATCH** — the 11/13 split is over all 24 non-verified items, not over "arm disagreements": only 13 of the 24 are items where the arms differ, and 3 of the 11 label items (Q06, V05, V12) are items where both arms agreed |
| 33 | 27 of the baseline's 77 items rest on live runs | `baseline/citations_check.json` `live_run_items` | 27 | PASS |
| 34 | 109 quoted segments | same, `quote_segments` | 109 | PASS |
| 35 | 83 verify verbatim at the pin | same, `verbatim_or_abridged_verbatim` | 83 (23 of them abridged with an ellipsis and verified piecewise) | PASS (wording note: "verbatim" includes abridged-verbatim) |
| 36 | 5 exist only in pre-redaction history | same, `pre_redaction_hits` | 5 | PASS |
| 37 | non-blind: both 8, baseline 10, ledger 2, neither 4 | `rulings/rulings_summary.json` `arm_right` | 8/10/2/4 | PASS |
| 38 | non-blind: ledger state equals ruling 9, baseline 16 | same `state_equals_ruling` | 9 / 16 | PASS |
| 39 | blind agrees with non-blind on 22 of 24 | `rulings_blind/summary.json` `agree_rulings` | 22 | PASS |
| 40 | Q28 contradicted→verified; H06 verified→contradicted | `rulings_blind/summary.json` rows | exactly those two | PASS |
| 41 | blind table, all 24: both 5, baseline 9, ledger 3, neither 7 | `rulings_blind/summary.json` `tally_all` | 5/9/3/7 | PASS |
| 42 | blind table, 13 substance: both 5, baseline 4, ledger 2, neither 2 | `tally_substance` | 5/4/2/2 | PASS |
| 43 | blind: state equals ruling, ledger/baseline 9/14 (all), 8/9 (substance) | `match_all`, `match_substance` | 9/14 and 8/9 | PASS |
| 44 | owner ruled on seven flagged questions | `rulings_summary.json` `owner_input_needed` = H06, H08, Q02, Q27, Q29, Q33, V02; `results/DECISIONS.md` D1–D7 | 7 items / 7 decisions (an 8th ruling, V07, follows D2 mechanically) | PASS |
| 45 | overrode the model ruling on two | `rulings/owner_rulings.jsonl`, `FINAL_STATES.md` | H08, V02 (unverifiable → contradicted) | PASS |
| 46 | Q-22 fixed 2026-08-09 | owner_rulings.jsonl / DECISIONS.md D1 (commit 818045f4) | 2026-08-09 | PASS |
| 47 | owner-final: ledger 11 / baseline 14 (all 24) | `rulings/FINAL_STATES.md` | 11 / 14 | PASS |
| 48 | owner-final: ledger 10 / baseline 7 (13 substance) | same | 10 / 7 | PASS |
| 49 | "its 28 engine-failure events" | `ledger/claims.jsonl` `event.type == engine_failure`; `results/packets/H08.md` derivation | **27** events (12 refusal, 11 unstated, 4 wrong_answer) | **MISMATCH** |
| 50 | 28 engine-failure events, 9 of them wrong-answer | same | 27 events, **4** wrong_answer (44 pre-merge with duplicates; no denominator yields 28/9) | **MISMATCH** |
| 51 | pytest 2,267 passed and 4 skipped | `results/live_runs.json` Q24 output | "2267 passed, 4 skipped ... in 163.30s" | PASS |
| 52 | 2,270 and 1 with two optional packages | `rulings/rulings_summary.json` Q24 disposition (numpy, scikit-learn) | as stated | PASS |
| 53 | setup check exits 0 | `live_runs.json` Q40/Q43 ("environment OK", exit 0) | exit 0 | PASS |
| 54 | applied to the target repo in `eb5253be` | `git log` in semi-formal-document-analysis | commit eb5253be474c6672d5f3d589d5264cbe3322b4a4 exists, README.md only (+49/−30) | PASS |
| 55 | 13 claim sites changed | commit subject + intervention_log close-out entry | "13 claim sites changed" | PASS |
| 56 | 13 of 15 hypotheses ended definite (threshold 2) | `results/query_results.json` H items | 10 verified + 3 contradicted = 13 definite, 2 contested | PASS |
| 57 | number probe Q26, 100 → 94 | `results/probe/PREREG.md`, `RESULT_ledger.md` | 100 → 94 | PASS |
| 58 | run 1 changed nothing; run 2 flipped exactly Q26 and V05 | `RESULT_ledger.md`, `probe/query_results_mutated*.json` | run 1: 0 of 77; run 2: Q26 verified→contradicted, V05 contested→contradicted, other 75 unchanged | PASS |
| 59 | fabrication probe: MCC +0.320 / +0.278; ledger predicted Q12, Q13, V04 fall | `probe/PREREG_fabrication.md`, `RESULT_fabrication.md`, `impact_ranking.json` | exactly those three | PASS |
| 60 | numbers re-derive from the committed scorer in 12 seconds | `RESULT_fabrication.md` baseline table | 12 s | PASS |
| 61 | reviewer's re-check 120k tokens | same | 120,272 | PASS |
| 62 | 4.5 minutes | same | 4 min 25 s | PASS |
| 63 | about 38% of its first pass | 120,272 / 320,488 | 37.5% | PASS |
| 64 | inventory-to-machinery seam leaked three times | intervention_log D-09, D-10, D-11 | 3 | PASS |
| 65 | 41 of 65 inventory items feed no verdict node | `probe/RESULT_fabrication.md` flatness table (24 of 65 feed a V node, 41 leaves) | 41 as recorded; re-deriving from `inventory.json` providers gives 40 leaves if the single provider string "Q41/H07" is counted as two items | PASS against the artifact (fragile: the count depends on how "Q41/H07" is parsed; no derivation script is committed) |
| 66 | no node depends on another | inventory verdict_nodes providers | no V id appears as a provider | PASS |
| 67 | fan-in is at most five | providers per node | max 5 (V04, V05, V07); median 3 | PASS |
| 68 | 4 of 206 cited spans flip anything; at most one item each | `probe/impact_ranking_spans.json` | 206 entries, 202 with 0 flips, 4 with exactly 1 | PASS |
| 69 | "removing a whole fact flips at most two plus a verdict" | `probe/impact_ranking.json` | max flips per fact = 2 total, and each is one README item + one verdict node (Q13+V04, Q12+V04, Q17+V09) | **MISMATCH** — reads as three (two items plus a verdict); the maximum is one item plus one verdict. Same wording appears in `RESULT_fabrication.md` |
| 70 | Translation used 140 agents | `results/COST.md` | 140 | PASS |
| 71 | 15.4M harness tokens | same | 15,406,453 | PASS |
| 72 | 9.1M Opus | same | 9,102,393 | PASS |
| 73 | 6.3M Sonnet | same | 6,304,060 | PASS |
| 74 | 911 agent-minutes | same | 911 | PASS |
| 75 | about 32x the baseline, price-weighted, before cache discounts | `results/COST.md` "Correction" section (5:1 Opus:Sonnet assumption → ~10.4M Opus-equivalent vs 320k) | ~32x, explicitly an assumption not a measurement | PASS |
| 76 | setup reviews added 1.8M | `results/COST.md` | 1,772,517 | PASS |
| 77 | about a third of claims mechanical | `results/mechanical_fraction.md` | 32% | PASS |
| 78 | about half with a labelling step | same | 49% | PASS |
| 79 | events are 39% of claims | same ("Events are 39% of the ledger") | 39% | PASS |
| 80 | events are the inputs to every hypothesis | same ("carry every hypothesis (H01-H15)") | as stated | PASS |
| 81 | events 18% mechanical | same ("events 18%") | 18% | PASS |
| 82 | Haiku 0 to 48% recall | `results/capability_probe.md` / `capability_probe_score.json` (B 0/20, C 10/25, D 12/30, E 10/21) | 0% – 48% | PASS |
| 83 | Haiku 80 to 100% precision | same score file: numbers precision B 0/4 = 0%, C 83%, D 80%, E 91%; event-type precision B 70%, D 100%, E 80% | full range is 0% – 100% | **MISMATCH** — the stated range excludes lane B's 0% numeric and 70% event-type precision (note: `capability_probe.md`'s own "Reading" section makes the same 80-100% claim) |
| 84 | query layer "patched seven times during the run" | `results/intervention_log.md` (names three post-baseline tunings: Q27, V01, H10); `git log -- results/queries.py` = 14 commits | no artifact yields 7 | **MISMATCH / not established** |
| 85 | three queries tuned after reading the baseline (Q27, V01, H10) | intervention_log line 406 | Q27, V01, H10 | PASS |
| 86 | Q26 and V05 as registered; "the number probe was chosen to favor it" | `probe/PREREG.md` (favorable-case selection disclosed) | as stated | PASS |
| 87 | summary: 97% of numeric literals carried | completeness_audit.md | 4368/4501 | PASS |
| 88 | summary: "roughly 32x the baseline review" | COST.md | consistent with Results | PASS |
| 89 | run dates 2026-09-02 to 03 | translation_log `checked_at` (2026-09-02/03), intervention_log entries | translation and queries 09-02/03; adjudication D-12/D-12b 09-03; owner rulings 09-04; close-out 09-09 | PASS for the translation/verification run; the status line's window does not cover the owner rulings (09-04) or the target-repo commit (09-09), both reported in the same Results section |

Figures checked: 89. MISMATCH: 6 (rows 32, 49, 50, 69, 83, 84).

## B. Internal consistency

1. **Engine-failure counts contradict the experiment's own H08 evidence.** The
   Results section says "its 28 engine-failure events" (Adjudication) and "28
   translator-labelled engine-failure events, 9 of them wrong-answer"
   (Findings). The ledger the same section relies on holds 27 `engine_failure`
   events, of which 4 are typed `wrong_answer` (11 `unstated`, 12 `refusal`) —
   the exact list is printed in `results/packets/H08.md` and in the H08 row of
   `results/arm_comparison.json`. Both post figures are wrong, and the
   "9 of them wrong-answer" figure is not reachable from any variant
   (all pre-merge accepted outputs, duplicates included, give 44 events / 24
   wrong_answer).
2. **Denominator slip on the label/substance split.** "Of the 24 items that
   ended non-verified in the ledger, the adjudicators classified 11 of the arm
   disagreements as label only ... and 13 as substance" attributes the split to
   disagreements. The committed classification (`rulings_summary.json`) is over
   all 24 items; only 13 of them are arm disagreements, and 3 of the 11 label
   items (Q06, V05, V12) are items where the two arms recorded the same state.
3. No contradiction was found between the "Post-experiment summary" and the
   "Results" section: the summary's 97%-anchor claim, its 32x cost claim, its
   "translation mistyped most of it" statement about the engine-failure
   enumeration, and its tier claims all match the Results text and the
   artifacts (subject to finding 1, which affects both sections' shared
   underlying figure only in Results).

Findings: 2 substantive (plus one "none found" note).
