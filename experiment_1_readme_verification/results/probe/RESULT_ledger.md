# Perturbation probe — ledger arm result

Mutation per PREREG.md: Q26 definition_count 100 -> 94 (README line 28).
Ledger unchanged (ledger/claims.jsonl, 14,721 claims). Live runs unchanged.

## Run 1 — FAILED (recorded as run, not discarded)

Command: checker over the ledger (12 s, 14,721/14,721 pass) then
`queries.py --inventory results/probe/inventory_mutated.json`.
Result: 0 of 77 items changed state. Q26 stayed verified.
Cause, found on inspection: the query table in results/queries.py carried
its own literal copy of each README value (and, for Q26, the number inside
a quote regex) instead of reading it from the inventory, so the mutated
inventory never reached the comparison. The re-check was therefore not a
re-check of the mutated README at all. Registered prediction (Q26 ->
contradicted) not met on this run.

## D-10 — value binding

Fix (query code only; no ledger, inventory, brief or glossary change):
each spec's target value is bound at load time to the frozen inventory
key holding the same literal, and the inventory passed on the command line
supplies the value used (a literal inside a quote regex is re-templated).
Binding is automatic and logged; the frozen-inventory run is bit-identical
before and after the change (40/5/5, 10/3/2, 3/2/6/1).

## Run 2 — after D-10

`queries.py --inventory results/probe/inventory_mutated.json` (1 s).
Binding changed: Q26 definition_count 100 -> 94.
Items changed: Q26 verified -> contradicted; V05 contested -> contradicted.
All other 75 items unchanged. Q26 derivation: "no claim carries the claimed
value; the record holds ... L1010221 = 100 (stated) ..." — the record's
100 is reported as the other value; the record's separability 94 (a
different metric) did NOT match, which was the point of choosing 94.

Both registered ledger-arm predictions met on run 2; not met on run 1.

## Cost (ledger arm)

Model tokens: 0. Wall clock: 12 s (checker) + 1 s (queries) per run;
orchestrator time to diagnose and fix D-10 about 10 minutes. Build cost for
comparison: 15.4M subagent tokens, 911 agent-minutes (results/COST.md).
Re-check is far under 10% of build cost by every measure, but the honest
statement is: under 10% only after a query-engine defect that the probe
itself exposed was fixed.
