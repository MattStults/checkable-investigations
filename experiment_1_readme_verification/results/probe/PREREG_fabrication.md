# Perturbation probe (reframed) — pre-registration

Written and committed BEFORE either arm runs. Owner's framing (2026-09-02):
choose a record fact that might have been fabricated, chosen because its
truth changes README answers, and use both approaches to state the impact
if it is fabricated vs not. Owner's remark on seeing the impact ranking:
"this means the symbolic model is very flat" — recorded as a finding (see
RESULT_fabrication.md).

## The fact

The arc-1 relevance benchmark's tool result: MCC +0.320 in-sample at the
0.18 threshold and +0.278 label-free, on the 589-passage Model Spec
universe. In the named sources this is carried only by prose in
semi-formal-experiment/HANDOFF.md at tier `stated` (results/probe/
fabrication_carriers.json lists the carrier claim ids). Counterfactual:
these numbers were never measured — the sentences are fabricated.

## Ledger arm — registered prediction

Removing every carrier claim and re-running the queries flips exactly:
Q12 verified -> unverifiable or contradicted (no claim carries +0.32),
Q13 verified -> unverifiable or contradicted (+0.278), V04 verified ->
non-verified (aggregator). Every other item unchanged (74 of 77). Cost: 0
model tokens, seconds of wall clock. The ledger cannot say whether the
numbers are re-derivable from committed scripts: it holds no live-run
claim for them (the benchmark output is not a named source).

## Baseline arm — protocol and registered expectation

One clean-context Opus reviewer receives: the pinned README, the repo
(read-only), baseline/probe2/BRIEF.md, baseline/CLAIMS.md (the original
claim list), and its own prior report baseline/REPORT.md (the incumbent
workflow: an analyst re-checking their own report under a counterfactual;
the ledger, glossary, brief, intervention log and everything else under
the experiment stay hidden). Question: assume the fact above is
fabricated; for every claim id, does its state change, to what, and why;
and can the numbers be independently re-derived from committed artifacts
or scripts (read-only, no network)? Expectation: cost well below a fresh
pass (it has its prior report); correctness open. If the reviewer flips
items outside {Q12, Q13, V04}, each such item is an adjudication question:
either the ledger's dependency structure is missing an edge (a real gap in
the symbolic model) or the reviewer over-propagated.

## What this probe can and cannot show

Necessary, not sufficient (owner). A pass shows the ledger's impact
statement is mechanical and exact for the edges it has; the flatness
finding already shows it has few edges.
