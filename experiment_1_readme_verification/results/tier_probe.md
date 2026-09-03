# Tier probe and checker rejection rates by model

Source: results/translation_log.jsonl (every checker run of a translator output).

## Checker rejection rate by model (all runs, first submissions and retries)

| Model | Runs | Claims | Rejected | Rate |
|---|---|---|---|---|
| opus | 93 | 14,624 | 17 | 0.12% |
| sonnet | 58 | 6,092 | 202 | 3.32% |

## Tier probe (same batch, both models)

| Batch | Model | File | Claims | Accepted | Rejected | Fail reasons |
|---|---|---|---|---|---|---|
| batch_001 | sonnet | batch_001_sonnet | 232 | 221 | 11 | {'rate': 11} |
| batch_001 | sonnet | batch_001_sonnet_retry1 | 11 | 11 | 0 |  |
| batch_001 | opus | batch_001_opus | 260 | 260 | 0 |  |
| batch_001 | sonnet | batch_001_sonnet | 232 | 220 | 12 | {'erratum.n=2 does not appear as an erratum number in the quote (I-01)': 1, 'rate': 11} |
| batch_001 | sonnet | batch_001_sonnet_retry2 | 1 | 1 | 0 |  |
| batch_052 | opus | batch_052_opus | 155 | 154 | 1 | {'quote': 1} |
| batch_052 | sonnet | batch_052_sonnet | 150 | 149 | 1 | {'erratum.n=3 does not appear as an erratum number within the cited source lines (I-01)': 1} |

Probe outputs are excluded from the merged ledger (checker/merge.py PROBES).
The parity decision (Sonnet for git-log batches, Opus for documents, JSON and
cycle records) is recorded in results/intervention_log.md; this file is the
mechanical record only. Rejection rate measures checker-detectable defects
(quote, enum, shape, rate arithmetic), not semantic fidelity.
