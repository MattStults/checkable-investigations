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
