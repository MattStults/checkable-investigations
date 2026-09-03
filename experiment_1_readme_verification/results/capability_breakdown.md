# Capability breakdown: what the data can and cannot say

Data available: (a) the tier probe — Sonnet and Opus translated the same two
batches (batch_001, prose ledger entries; batch_052, git-log commits),
outputs excluded from the merged ledger; (b) checker rejection rates by
model and source class over every run; (c) the intervention log (which
defects needed a human and which model produced them). No model smaller
than Sonnet and no Fable translator ran, so nothing below is evidence about
a 30B model or about Fable.

## Tier probe, same spans, both models

| batch | class | numeric (span,value) pairs shared / Opus / Sonnet | event (span,type) pairs shared / Opus / Sonnet | Opus-only event types | Sonnet claims vs Opus |
|---|---|---|---|---|---|
| batch_001 | prose ledger | 63 / 85 / 68 | 52 / 62 / 55 | annotation x5, measurement x2, ledger_entry x2, engine_failure x1 | 476 vs 260 (1.8x, finer splitting and duplicates; 23 rejected, 22 for rate formatting) |
| batch_052 | git log | 50 / 53 / 53 | 25 / 30 / 28 | adversarial_review x2, engine_failure, prediction_freeze, measurement | 299 vs 155 (1.9x) |

Reading: on git-log spans the two models recover the same numbers (50 of
53 shared) and nearly the same events; Sonnet's defects there were shape
(missing ordinal, kind tagged event without an event object) — exactly
what the checker catches. On prose ledger entries Sonnet recovered 74% of
Opus's numeric pairs and 84% of its event types, and the events it missed
are the semantically loaded ones (annotations, engine_failure, measurement
events), i.e. the claims the hypotheses run on.

## Checker rejections by model and class (all runs)

Opus: 0.0-0.6% in every class (17 rejections in 14,624 claims). Sonnet:
3.2% on git log (179, nearly all shape rules), 4.8% on prose ledger (23,
rate formatting). Shape defects are cheap because the checker catches them
and the translator fixes them on resend.

## What the interventions say about the top end

Of the defects that needed a human (I-01 to I-07, D-09 to D-11), none was a
frontier-model reading error that a stronger translator would have
avoided: I-01 (erratum numbers from counts) came from Sonnet; I-02 to I-06
were tier-procedure ambiguities that Opus resolved consistently but
differently from the glossary's intent, fixed by amendments; I-07 and
D-09 to D-11 were machinery gaps. The record holds no case where Opus
misread a span in a way the checker or a query surfaced. So the data
support pushing structured and semi-structured sources down to a cheaper
model behind the checker; they do not show that the prose lane was
capability-limited at Opus, and therefore give no evidence for or against
routing it to Fable.

## Lanes this suggests (untested)

1. Parser: JSON/YAML, git metadata, n/d rates, table cells, path
   existence (about a third of claims; 88% of rates).
2. Small model + checker: metric labelling of parser-found numbers, git-log
   subject sub-events, one-line spans (Sonnet at parity with Opus on git
   log in the probe; a 30B model is a plausible but untested candidate).
3. Frontier model: prose events with actors, findings, caught_by and
   refs, tier gating with markers, contested pairs (about 40% of claims;
   Sonnet's recall on prose event types was 84% of Opus's, with the misses
   concentrated in the types the hypotheses need).
