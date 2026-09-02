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

## Interventions

(none yet — translation has not begun)

## Compactions

(none recorded yet)
