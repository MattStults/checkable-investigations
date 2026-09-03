# Cost accounting — both arms

Source: task-notification usage blocks in the orchestrator transcript,
deduplicated (results/agent_usage.json). Subagent tokens are input+output as
the harness reports them. The orchestrator's own tokens (Fable, this
session) are NOT included for either arm; the orchestrator spent far more on
the ledger arm (machinery, checker, reselection, queries) than on the
baseline (one dispatch, one cost record).

| Arm | Agents | Subagent tokens | Tool calls | Agent-minutes |
|---|---|---|---|---|
| Baseline (one clean-context Opus review) | 1 | 320,488 | 89 | 27 |
| Ledger arm — translation (Opus docs/JSON/cycles, Sonnet git log, retries, D-09, G-06) | 140 | 15,406,453 | 1417 | 911 |
| Ledger arm — setup reviews and extraction (inventory/glossary clean reviews, round-trip check, glossary sources, leak checks) | 13 | 1,772,517 | 400 | 97 |

Ratio, translation alone vs baseline: 48x tokens, 34x agent-minutes.
Ratio, whole ledger arm (translation + setup) vs baseline: 54x tokens.

Wall clock: the baseline ran in 27 min. The ledger arm ran across two days
with a session rate-limit pause and an owner-directed throttle to two
concurrent translators; its wall clock is not a clean measure of the method.

Setup costs are one-off per record (the inventory and glossary are reusable
for the perturbation probe and any re-verification); translation cost is
per record and would recur only for spans whose text changes.

## Correction: tokens are not cost-equivalent

The table above sums harness "subagent_tokens" across models. Three things
make that a poor proxy for dollars:

1. **Model mix.** Translation split by model (results/agent_usage.json):

| Translators | Agents | Tokens | Agent-minutes |
|---|---|---|---|
| Opus (documents, JSON, cycle records, retries, D-09, G-06) | 83 | 9,102,393 | 584 |
| Sonnet (git log, leftovers) | 57 | 6,304,060 | 327 |

   At the usual list-price ratio of roughly 5:1 Opus:Sonnet, the Sonnet
   share weighs about 1.26M Opus-equivalent tokens, giving ~10.4M
   Opus-equivalent translation tokens, about **32x** the baseline rather
   than 48x. The exact ratio depends on current pricing; the 5:1 figure is
   an assumption, not a measurement.
2. **Cached prefix.** Every translator reads the same ~70 KB of brief,
   glossary and schema (about 20-30k tokens) before its batch. Across 140
   translator runs that is roughly 3-4M of the input tokens, and it is
   prompt-cache-eligible, so it is billed at a fraction of fresh input.
   The harness figure does not separate cached from uncached input.
3. **Input vs output.** The harness reports input+output combined. Output
   is the expensive side; the translators' output is the JSONL itself
   (14,721 surviving claims plus the 4,080 superseded ones, on the order
   of 2M tokens), while most of their reported tokens are re-read input.
   The baseline's 320k is likewise mostly input.

Net: the honest comparison is "tens of times the baseline in model
spend", not a precise multiple; 32x (price-weighted, cache ignored) is
an upper-bound-ish figure and the cache discount pushes it lower. What the
extra spend bought is the machine-checkable ledger, which the perturbation
probe (step 8) can re-check without re-translating.
