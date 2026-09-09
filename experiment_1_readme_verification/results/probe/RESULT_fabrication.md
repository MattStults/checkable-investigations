# Perturbation probe (reframed) — result

Pre-registration: PREREG_fabrication.md (committed before either arm ran).
Fact treated as fabricated: arc-1 tool MCC +0.320 in-sample / +0.278
label-free (HANDOFF.md prose, tier `stated`, four carrier claims).

## Ledger arm

Command: remove the four carrier claims, re-run the queries in memory
(results/probe/impact.py machinery; result in fabrication_ledger_result.json).

| item | before | after |
|---|---|---|
| Q12 | verified | contradicted (no claim carries +0.32; record holds +0.358, 0.3088, +0.274, +0.206, +0.396 under other scopes) |
| Q13 | verified | contradicted (no claim carries +0.278; record holds +0.277, +0.284, +0.20 ... under other scopes) |
| V04 | verified | contradicted (aggregator) |
| other 74 | unchanged | unchanged |

Registered prediction met exactly. Cost: 0 model tokens, 2 s wall clock.
The ledger cannot answer the re-derivation question (whether the numbers
can be recomputed from committed scripts): the benchmark output is not a
named source, so it holds no live-run claim for them.

## Finding: the symbolic model is flat (owner's observation, confirmed)

Dependency structure of the frozen inventory as the queries use it:

| measure | value |
|---|---|
| Q items | 50 |
| H items | 15 |
| V nodes | 12 |
| Q/H items that feed any V node | 24 of 65 |
| Q/H items that feed nothing (leaves) | 41 |
| V nodes with V providers (depth > 2) | none |
| providers per V node | 0 to 5 (median 3) |

Consequences seen in the impact analysis: removing any single record span
flips at most one README item (4 of 206 cited spans flip anything);
removing a whole fact flips at most two items in total (one README claim plus one verdict node). The
README's numbers are restated across sources (so single-entry fabrication
is absorbed) and the README's claims are mostly independent leaves (so
fabrication fan-out is tiny). The interesting structure in this record is
in events and their order (H01-H15), not in value dependencies; value
counterfactuals therefore have little to propagate through. A record with
derived quantities (rates computed from counts that the README also
states) would show chains; this one mostly does not.

## Baseline arm

One clean-context Opus reviewer with its prior report, the claim list, the
README and the read-only repo; asked to assume the fact fabricated. Four
attempts: three ended in server-side 529 overloads before writing anything;
the fourth completed. Report: baseline/probe2/IMPACT.md.

| measure | value |
|---|---|
| changed claim ids | none (all 77 unchanged) |
| re-derivation | yes: the README's own `benchmark.py --tool` reprints +0.320 (true-universe in-sample) and +0.278 (universe-delta mean) in 12 s; a direct recomputation through the committed modules gives +0.3197 / +0.2778; `test_quality_floor.py` guards the same values |
| wall clock | 4 min 25 s (excluding idle time in the aborted attempts) |
| subagent tokens | 120,272 (about 38% of the first pass) |
| tool calls | 25 |

The reviewer's argument: the prose in HANDOFF.md was never the authoritative
source for these numbers; the committed scorer is, and it reproduces them.
So "the prose was fabricated" changes no README claim.

## Comparison and interpretation

The two arms gave opposite impact statements, and the baseline's is the
correct one about the world. The ledger's statement was exact for the edges
it had and wrong because of source coverage: its named sources hold the MCC
numbers only as prose, so it treated the prose as the sole support and
flipped Q12, Q13 and V04. The inventory had declared Q12/Q13 at tier
"live_run (benchmark.py --tool) or stated", and the live run was never
added to results/live_runs.py — an omission of the same class as D-09 and
D-10 (a declared dimension or source not carried into the machinery). The
pre-registration itself noted that the ledger could not answer the
re-derivation question; the probe shows that limitation is not cosmetic:
without the live-run witness, the ledger's fabrication-impact answer is
wrong for exactly the fact the probe chose.

Post-probe (D-11, labelled as such, not part of the registered run): the
declared live run was added. Q12/Q13 now verify from the benchmark output
(0.32, 0.278; 11 s), and the counterfactual removal of the prose carriers
flips nothing, matching the baseline. The frozen scorecard is unchanged
(40/5/5, 10/3/2, 3/2/6/1).

What the probe shows, taken together with the flatness finding:

1. Mechanical re-check is cheap and exact for the dependency edges the
   ledger has (0 tokens, 2 s, prediction met on run 2 of the number
   probe and run 1 of the fabrication probe).
2. The ledger's answers are only as good as its source coverage; two of
   the three probe runs exposed machinery that had dropped something the
   inventory declared (D-10 literal values, D-11 missing live run). The
   inventory-to-machinery step is where this method leaks.
3. The record's value structure is flat, so value counterfactuals have
   little to propagate; the cost advantage of a standing artifact is real
   but buys little when almost nothing depends on anything else.
4. The frontier reviewer, given its prior report, re-checked the
   counterfactual correctly at about 38% of its first-pass cost and, unlike
   the ledger, reached for the committed scorer unprompted.
