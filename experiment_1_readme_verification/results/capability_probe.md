# Capability probe: Haiku on the same spans, by routing lane

Sample: 5 spans per lane (B git log, C number labelling, D marker-triggered
prose events, E free-prose events), all already translated by Opus (docs)
or Sonnet (git log) and accepted by the checker; retranslated by Haiku 4.5
under the same brief, glossary and schema. Scored against the accepted
translation (results/capability_probe_score.py). One span per probe batch
was declined by Haiku as having nothing to translate (a LICENSE span; an
AGENTS.md reading-instructions span) — the accepted translations hold
claims for both. Excluded from the merged ledger. Cost: 148k Haiku tokens.

| lane | Haiku claims vs accepted | numbers recall / precision | event types recall / precision | checker |
|---|---|---|---|---|
| B git log (Sonnet reference) | 16 vs 58 | 0% / 0% (0 of 20) | 70% / 70% | |
| C number labelling | 15 vs 59 | 40% / 83% | n/a | 28/31 pass (3 quote) |
| D marker-triggered events | 26 vs 122 | 40% / 80% | 35% / 100% | |
| E free-prose events | 18 vs 65 | 48% / 91% | 44% / 80% | 37/44 pass (6 quote, 1 shape) |

Context, Sonnet vs Opus on the same-span tier probe: prose numbers 74%,
prose event types 84%; git-log numbers 94%, events 83%.

## Reading

- Haiku under-extracts on every lane: it writes a quarter to a third of the
  accepted claim count, and its number recall is 0-48%. What it does write
  is mostly right where it writes anything (numeric precision 83-91% on the
  three lanes where it produced numbers, and 0% on lane B where it produced none), and it passes the checker at
  85-90%. So a small model alone is a recall problem, not a precision
  problem — the failure mode is silence, which no checker catches.
- That is the case for the harness the owner sketched: let the
  deterministic pass do the FINDING (numbers, fractions, markers, git
  metadata), and use the small model only to LABEL what was found. Haiku's
  precision on the numbers it did label suggests labelling is within reach;
  its recall says do not let it decide what exists.
- Sonnet is a different tier: 74-94% recall against Opus with shape errors
  the checker catches. For lanes B and C it is at parity with Opus on
  content; for prose events it misses ~16% of event types, concentrated in
  annotations and engine failures.
- Lanes D and E (prose events) at Haiku lose more than half the event
  types, including seat dispatches, withdrawals, rulings and adversarial
  reviews — the hypotheses' inputs. Nothing in this run says whether Opus
  itself is the ceiling there (no independent reference above it).

## Untested

A 30B open model (Haiku is the proxy), a Fable translator on lane E, and
the deterministic-find + small-model-label pipeline itself, which was not
built. The numbers above are 5 spans per lane; they bound the shape of the
curve, not its values.
