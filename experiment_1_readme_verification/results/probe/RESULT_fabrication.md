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
removing a whole fact flips at most two items plus one verdict node. The
README's numbers are restated across sources (so single-entry fabrication
is absorbed) and the README's claims are mostly independent leaves (so
fabrication fan-out is tiny). The interesting structure in this record is
in events and their order (H01-H15), not in value dependencies; value
counterfactuals therefore have little to propagate through. A record with
derived quantities (rates computed from counts that the README also
states) would show chains; this one mostly does not.

## Baseline arm

(filled in when the counterfactual review returns; two attempts so far
ended in server-side 529 errors)
