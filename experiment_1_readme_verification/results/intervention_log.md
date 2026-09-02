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

### D-05 — 2026-09-02 — JSON span cut by depth, not indentation

Caught by: pilot batches 005-008 (Opus): translators reported one-line
spans with no enclosing key and duplicated content; the old cutter took
any key at indent ≤2 as top-level, and the scored files use one-space
indents. Artifact: `brief/spans.py` cut_json finds depth-1 keys by brace
depth, carries windows of long values with a `context` field; spans
regenerated (1,686; ledger and doc spans unchanged, ids S00001-S00196
identical). Outputs translated under the old cut (batches 004-008, 216
claims, all checker-clean) moved to `ledger/out/pre_d05/` and excluded
from the final ledger; their batch files to `ledger/batches/pre_d05/`.
Brief v0.5 rules 31-33 (file name as outermost key; window context).

### D-06 — 2026-09-02 — batch header provenance

Caught by: the batch_005 translator ("brief file itself is v0.5, but I
followed the batch header"). batch.py parsed the brief version before the
v0.5 edit and computed the glossary hash from the wrong directory, so
batches 001-121 as first cut carried brief_version 0.4 and
glossary_version "frozen " (blank). Artifact: batch.py fixed; headers of
all not-yet-dispatched batches rewritten. Claims already produced under
the defective headers (batch_002, 003 dispatched under brief v0.4 text;
batch_004-009 dispatched under brief v0.5 text but header 0.4) keep
their translator block as written; the true brief in force at dispatch
is recorded here: batches 002-003 → v0.4; batches 004-009 → v0.5; every
batch → glossary frozen f169c02. Not a ledger edit.

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

Refinement (same day): the rule first required the number in the QUOTE;
an Opus claim from entry 0037 (heading 'ERRATUM #20') quoting a
sub-sentence without '#20' was rejected. Rule now requires the number as
'#n' / 'erratum n' within the claim's cited source lines. The Sonnet
count case (entry 0000, no '#2' anywhere in the entry) still fails.

Recurrence: batch_003 opus — 0 true recurrences (the one hit was the
over-narrow rule, not the defect class). batch_012 opus — 1 hit:
"errata addendum 5" translated as erratum.n = 5. Whether an "errata
addendum" numbered 5 is an erratum number is a reading the rule does not
admit; the claim is retranslated with n null and the span's words in
class. Counted as a recurrence of the class (a nearby number taken as n)
after the checker rule existed; the rule caught it, so no human
question was needed.

### I-02 — 2026-09-02 — wave verdict tiered panel by the key walk

Caught: the batch_010 translator flagged it ("`wave` inside the `panel`
array resolves to tier `panel`"); orchestrator confirmed 3 affected
accepted claims across batches 008, 009, 010 (one per panel-row span).
Class: the tier procedure's raw-label list lacked the bare word `wave`,
so the walk climbed to the enclosing `panel` key.

Operationalised: glossary amendment G-01 (step 5 gains `wave`), rendered
into glossary.md under Amendments; checker rule (a quote keyed "wave" with
tier ≠ raw is rejected, tagged I-02). The 3 claims are re-split as
rejected and retranslated.

Recurrence: (tracked as batches complete)

### I-03 — 2026-09-02 — human/cove tiers unreachable behind Gate B

Caught: the batch_014 translator ("Gate B fires and stops before the
human/cove steps — including the owner-ruling blocks ... and the CoVe
re-derivation numbers"). Orchestrator confirmed ledger batches 002/003 had
applied human/cove to the same kinds of span, so the procedure was being
read two ways. Class: procedure ordering.

Operationalised: glossary amendment G-02 (steps 8-9 before Gate B),
rendered. No mechanical checker rule is possible without content
judgment; instead a mechanical SELECTION: every accepted document-batch
span whose text contains a ruling/CoVe marker and whose claims are all
tier stated is retranslated whole under G-02, and its prior claims are
superseded (listed in the retry batch header). Applied to batches 014-016
now (retry_I03_a) and to 012-013, 017-021 when they land.

Recurrence: (tracked)

### I-04 — 2026-09-02 — owner name forms not in the human-tier marker set

Caught: the batch_021 translator ("'Matt's D1 amendment' carries no
step-8 marker, so it stayed stated"). The human markers listed only the
post-redaction role language and 'MATT RULING'; the record (especially
pre-redaction blobs and ledger prose) attributes rulings as 'Matt:',
'(Matt)', "Matt's ruling/correction". Class: marker set incomplete.

Operationalised: glossary amendment G-03 (marker forms added), rendered.
Mechanical selection: accepted spans matching the new forms with no
human-tier claim are retranslated whole (list in
ledger/batches/_g03_pending.json, folded into the next retry batch).

Recurrence: (tracked)

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
