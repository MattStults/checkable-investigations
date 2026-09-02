# Intervention log

Primary result of the experiment. Two sections:

- **Design changes (D-nn)**: changes to machinery made BEFORE any translator
  output existed. Not counted as interventions; listed so the machinery's
  history is visible.
- **Interventions (I-nn)**: every time the orchestrator catches an error in
  translator output after translation begins. Each records what was caught,
  the operationalised artifact it produced (brief amendment / glossary
  amendment / checker rule), and whether the same defect class recurs
  afterward. The orchestrator never edits a ledger claim by hand.

Compaction notes (C-nn) record orchestrator context compactions with the
brief and glossary versions in force, so incomplete continuity is visible.

## Design changes

### D-01 — 2026-09-02 — value standing is derived, not translated

Caught by: owner question ("do we actually support that kind of ambiguity in
the representation?") about the struck-but-still-present human-panelist 71%
figure, which three record spans treat differently (asserted current;
flagged unsourced; struck).

Defect: the schema carried one supersession link per claim and asked the
translator to set a status that depends on spans it cannot see.

Artifact: `checker/SCHEMA.md` and `checker/check.py` replace
`supersession{status,by}` with `stance` (the span's own words only) plus a
`refs` list of typed edges (supersedes, restates, flags_unsourced, strikes,
withdraws, contradicts, re_derives, amends, quarantines) with verbatim
`target_text` and a `target_id` filled only by `checker/resolve_links.py`,
which logs every match and its basis. Event type `annotation` added. Brief
v0.2 rules 7, 7a, 11. Value standing (asserted-current, flagged-unsourced,
struck, superseded, contested, restated) is computed at query time from
incoming refs.

Inventory impact: none. The inventory declares the dimensions (supersession,
linkage); the schema is their storage. Recorded here rather than as an
inventory amendment for that reason.

### D-02 — 2026-09-02 — checker: generated sources and ordinals

Caught by: seed batch 1 (5 git-log claims failed 'source not found'; a
handoff-sourced withdrawal failed 'requires an ordinal').
Artifact: `check.py` resolves `GENERATED:` paths under `ledger/spans/`;
ordinal required only for ledger-entry and git-log sourced events (the
ledger file header excepted). Brief v0.3 rules 12-21.

### D-03 — 2026-09-02 — span assignment: JSON cut carries nested values

Caught by: seed batch 2 selection (a span read `"attempt2": {` and nothing
else). Artifact: `brief/spans.py` cut_json tracks brace depth; spans
regenerated (2,538).

### D-04 — 2026-09-02 — schema: forbids_citation, trigger; brief v0.4

Caught by: seed batch 2 translation (no relation for a do-not-cite marking;
no event type for a stop condition firing; cycle-artifact keys had no tier
mapping; arrows/multipliers/unnamed triples had no rule). Artifact: rel
`forbids_citation`, event type `trigger`; brief rules 22-30.

## Interventions

### I-01 — 2026-09-02 — erratum number taken from a count

Caught: orchestrator inspection of batch_001 (Sonnet probe) after the
checker passed it. Span: entry 0000, "two commits today shipped with a
red/unverified state"; the claim carried erratum.n = 2. The Opus
translation of the same span carried n = null. Class: a count in the span
read as an erratum number.

Operationalised: checker rule — erratum.n, when non-null, must appear in
the quote as "#n" or "erratum n" (check.py, tagged I-01). No brief change
(rule 9 already says n is the number the span gives).

Recurrence: (tracked below as batches complete)

### Observations not (yet) interventions

- Both tiers type most standing statements in entry 0000 as `registration`
  (Opus 43 of 123 events, Sonnet 79 of 129). Not mechanisable without a
  content rule; watched.
- Actor `unstated` dominates in both tiers on entry-0000 bullets that carry
  no first-person marker. Consistent with brief rule 2; the orchestrator's
  own seed had inferred `driver`, which was the over-reading.

## Tier probe (registered: start with Opus, optionally probe others)

| batch | model | claims | checker-rejected | after retry |
|---|---|---|---|---|
| batch_001 (ledger, 15 entries) | opus | 260 | 0 | — |
| batch_001 (ledger, 15 entries) | sonnet | 232 | 11 (rate value as string) | 0 |
| batch_004 (scored JSON, 15 objects) | opus | 74 | 0 | — |


## Compactions

(none recorded yet)
