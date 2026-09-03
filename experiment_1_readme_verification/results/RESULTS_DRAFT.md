# Proposed blog updates (draft for owner approval; the post is untouched)

Two edits proposed: (A) replace the pilot post's "Results" placeholder and its
"Current status" line; (B) a short addendum to the proposal post. Facts and
tables only; numbers trace to files under `experiment_1_readme_verification/`.
Items marked [BLIND] are filled from the blind re-adjudication when it lands.

---

## (A) Pilot post — replace "Current status" line

> **Current status**: run complete (2026-09-02 to 03). Results below; design and expectations sections are as registered. Artifacts: [checkable-investigations/experiment_1_readme_verification](https://github.com/MattStults/checkable-investigations/tree/main/experiment_1_readme_verification).

## (A) Pilot post — Results section

### What ran, and where it deviated from the design

The inventory (50 quantitative claims, 15 hypotheses, 12 verdict nodes, commitments and residue) and the glossary were frozen before translation and reviewed by clean-context agents; both are tagged in the repo. 1,686 spans were cut mechanically from the named sources (the ledger, handoffs, preregs, review dispositions, scored JSON, cycle records, the first-parent git log, and pre-redaction blobs of every redacted file) and translated blind under a written brief and glossary, with a mechanical checker gating every batch.

Deviations from the registered design, all logged in `results/intervention_log.md`:

- **Translation tier.** The design said the finished ledger would be entirely lower-tier translated after a frontier-seeded brief. In the run, documents, JSON and cycle records were translated by Opus and only the git log by Sonnet, after a same-batch probe showed Sonnet at content parity on git log (50 of 53 numbers) but at 74% numeric and 84% event-type recall on prose. The ledger is therefore mostly frontier-translated, and the claim "the context works for the models the proposal needs" was not tested at the scale planned.
- **Adjudication.** The design made adjudication human. Rulings were made by a Fable adjudicator (D-12), then repeated blind with the arms anonymized and reasons removed (D-12b). Seven rulings are provisional on owner knowledge.
- **Design changes during the run.** Twelve numbered (D-01 to D-12): schema and cutter fixes early; three late ones (D-09 seat inputs, D-10 literal values in query specs, D-11 a declared live run never implemented) share one cause, an inventory declaration that did not make it into the machinery. Seven translator-facing interventions (I-01 to I-07) each produced a brief or glossary amendment or a checker rule; one class recurred once after its fix (signature markers, I-06 then G-06).

### The artifact

| measure | value |
|---|---|
| claims in the final ledger | 14,721 |
| checker pass on final re-check | 14,721 of 14,721 |
| claims rejected by the checker across the run (and retranslated) | 219 |
| spans without a claim | 29, all pre-redaction spans identical to current text (excluded by design) |
| claims reported contested rather than resolved | 100 |
| numeric literals in spans carried by some claim | 97% (4,368 of 4,501) |
| event markers carried | 95%; backticked paths 71% |

Checker rejection rate by translator model: Opus 0.12%, Sonnet 3.32% (shape errors the checker catches).

### The two arms

Baseline: one clean-context Opus agent with the README, the repo and a brief; 27 minutes, 89 tool calls, 320k tokens, 77 items.

| | verified | contradicted | contested | unverifiable / dangling |
|---|---|---|---|---|
| ledger arm, quantitative (50) | 40 | 5 | 5 | 0 |
| ledger arm, hypotheses (15) | 10 | 3 | 2 | 0 |
| ledger arm, verdict nodes (12) | 3 | 2 | 6 | 1 dangling |
| baseline, all 77 | 54 | 12 | 6 | 5 |

Agreement: 60 of 77. Of the 17 disagreements, 13 are label only (the ledger says contested wherever the record holds unweighed conflict; the baseline weighs), 4 are substance.

Machine-checkable fraction: every ledger claim re-verifies. Of the baseline's 77 items, 27 rest on live runs with no file quote; of its 109 quoted segments, 83 verify verbatim at the pin, 5 exist only in pre-redaction history, and the rest are command output or the reviewer's summaries.

### Adjudication

Non-blind model rulings (D-12) on the 24 items ending non-verified in the ledger: arm judged right, both 8, baseline 10, ledger 2, neither 4; ledger state equals ruling on 9, baseline on 16. Restricted to the 11 substance disagreements: both 7, baseline 3, ledger 2, neither 1.

Blind re-adjudication (D-12b, arms anonymized, reasons removed): [BLIND: rulings agree with non-blind on N of 24; evidence decided by ledger X / baseline Y / both Z / neither W; substance-only ...].

Live-run conflicts settled by re-running: the setup check exits 0; pytest gives 2,267 passed and 4 skipped in the README's own venv (2,270 and 1 only with two optional packages installed). Both reproduce the ledger arm's observation.

README dispositions proposed per item (nearly all "tightened", with wording) are in `results/rulings/SUMMARY.md`; the disposition commit to the target repo waits on the seven provisional rulings.

### Registered expectation 1: met

No untracked edits; the ledger passes its own re-check end to end; the checker rejected 219 claims; 100 contested pairs held open; 13 of 15 hypotheses ended definite (threshold 2).

### Registered expectation 2: not met as stated

Re-check cost was as predicted: zero model tokens, seconds. "Correctly" was not:

- Number-mutation probe (Q26, 100 to 94, pre-registered): run 1 changed nothing, because the query table held literal copies of the README values (D-10); run 2, after binding values to the inventory, flipped exactly Q26 and V05 as registered. The baseline half could not be run fairly: the reviewer has the repo and detected the mutation by diff against the original README.
- Fabrication probe (owner's reframing; arc-1 MCC +0.320 / +0.278 treated as fabricated, pre-registered): the ledger predicted Q12, Q13 and V04 fall; a reviewer given its own prior report found nothing changes, because the numbers re-derive from the committed scorer in 12 seconds. The reviewer was right. The ledger held those numbers only as prose because a live run the inventory had declared was never implemented (D-11). Cost of the reviewer's re-check: 120k tokens, 4.5 minutes, about 38% of its first pass, not "roughly full price".

The residue list is non-empty and its boundary was stated in advance.

### The "update against" clause

Interventions did not approach the claim count and no state was dominated by unverifiable. One defect class did recur after being operationalized: the inventory-to-machinery seam leaked three times. That is an update against the method as built, and the fix is a conformance check at that seam, which the design did not have.

### Findings beyond the registered ones

- **The dependency graph is flat.** 41 of 65 inventory items feed no verdict node; no node depends on another; fan-in is at most five. Removing any single record span flips at most one README item (4 of 206 cited spans flip anything); removing a whole fact flips at most two plus a verdict. There is little for a standing artifact to propagate.
- **Cost.** Translation used 140 agents, 15.4M harness tokens (9.1M Opus, 6.3M Sonnet), 911 agent-minutes; about 32x the baseline price-weighted, before prompt-cache discounts. Setup reviews added 1.8M. `results/COST.md`.
- **Mechanical extractability.** About a third of claims had a core a parser could have produced; about half with a labelling step; events, 39% of claims and the inputs to every hypothesis, were 18% mechanical.
- **Capability probe.** Haiku on the same spans: 80 to 100% precision, 0 to 48% recall. A small model fails by silence, which the checker cannot see; the completeness audit against regex denominators can.
- **One finding the review did not surface:** 28 translator-labelled engine-failure events, 9 wrong-answer, bearing on the README's "every failure was a refusal"; on inspection most are scoring-code bugs and two or three are the engine deriving wrongly. Ruled unverifiable pending the owner's definition of the engine boundary.

### Fairness of the comparison

Not clean, in both directions. Against the ledger: its query layer was hand-written and patched seven times during the run; declared live runs and named sources were incomplete; it was scored against a label convention. For the ledger: I tuned three queries after reading the baseline's reasons (Q27, V01, H10); it had tens of times the compute and iterations; the number probe was chosen to favor it. The blind re-adjudication corrects the judging; it does not correct the query-tuning leak. Conclusions that do not depend on the comparison: the cost ratio, the flatness, the machinery leaks, the probe outcomes, the completeness and capability numbers.

### What I take from it

The advertised advantage, cheap correct re-verification through a standing artifact, did not materialize on this record: the record is flat, and the ledger's answers were bounded by source coverage that leaked where the inventory became machinery. What did hold: the discipline hypotheses (review before close, freeze before measure, append-only, dated, blind seats) were mechanically decidable wherever the project had imposed conventions on itself, and every failure of the method is a numbered entry with a cause. That reads as a tool for guarding a project's own record against drift, checked at write time, more than as a tool for investigating a record after the fact.

---

## (B) Proposal post (2026-08-30) — proposed addendum

> **Update 2026-09-03.** The pilot ran ([results](link to pilot post)). Registered expectation 1 (the artifact has the claimed properties) held; expectation 2 (cheap *correct* re-verification) did not as stated: the re-check was free but wrong until two machinery gaps were fixed, and a frontier reviewer re-checking its own report was both correct and only ~38% of a first pass. Two things I now believe that I did not when I wrote this: (1) the structured lane's value depends on the record having dependency structure, and a README-plus-ledger record is nearly flat; (2) filtering bias is checkable only against a denominator the model did not write, which argues for a harness-emitted event spine in the project's own record rather than post-hoc translation. Both push the design toward guarding a project against its own agents' drift, and away from after-the-fact investigation of arbitrary records.
