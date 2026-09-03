# Perturbation probe — pre-registration

Written and committed BEFORE either arm's re-check runs. Time: 2026-09-02T21:29-07:00.

## Mutation

One README number. README.md at the pin, line 28:

    before: ontology open-coded from 100
    after:  ontology open-coded from 94

Q26 ("an ontology open-coded from 100 behavior definitions covered every
sampled span"): definition_count 100 -> 94.

## Why this number (favorable-case selection, disclosed)

Chosen by ranking the ledger (results/probe_candidates.json): both arms
verified Q26 from documents; ten ledger claims from five sources carry the
value; Q26 feeds verdict node V05; and 94 is a REAL number elsewhere in the
record (the separability count, 94 of 100 definitions), so a re-check that
matches on the bare number, or a reader who finds "94" next to
"definitions", can be fooled. This is the most favorable case for the
ledger arm's representation, not a random draw. The owner's framing: the
probe is necessary, not sufficient — if it fails, the approach is almost
certainly not useful; if it passes, nothing more than that is shown.

## Predictions (ledger arm)

- Q26: verified -> contradicted (the ledger holds 100 as the definition
  count; the mutated inventory asks for 94; the 94 in the record is a
  separability count under a different metric and must NOT match).
- V05: contested -> contradicted (aggregator: any contradicted provider).
- Every other item (75 of 77): unchanged state.
- Cost: no model tokens; wall clock under two minutes; under 10% of build
  cost by any measure.

## Predictions (baseline arm)

A fresh clean-context Opus review of the mutated README with the same brief.
Expected cost roughly that of the first pass (about 320k tokens, ~27 min).
Correctness is the open question: it should mark Q26 contradicted with the
record's 100 as the other value. No prediction is registered on the other
76 items beyond "the same states as the first review, modulo reviewer
variance", and that variance is itself a result to report.

## Mechanics

- Frozen inventory untouched; the probe uses results/probe/inventory_mutated.json.
- Ledger arm: results/queries.py --inventory results/probe/inventory_mutated.json
  over the unchanged ledger/claims.jsonl and live_runs.json; diff against
  results/query_results.json.
- Baseline arm: baseline/probe/BRIEF.md, baseline/probe/CLAIMS.md (rendered
  from the mutated inventory by the frozen renderer), baseline/probe/README.md
  (mutated copy); the agent reads only those, AGENTS.md, and the read-only
  repo; it never sees baseline/REPORT.md, the ledger, or anything else under
  the experiment.

## Addendum (before running): consistency of the mutated inventory

The inventory quotes the mutated README sentence in more than one place
(Q26, Q27, and the hypothesis/verdict text that quotes it) and Q27's
dimension note names the README's number. All of those are mutated to 94 in
the probe copy so the baseline reviewer sees one consistent README; record-
derived mentions of 100 definitions (the separability 94/100) are untouched.
The ledger arm's Q27 query requires the population "100 or definition"; with
the mutated note it still matches "definition", so the Q27 prediction is
unchanged (contested).
