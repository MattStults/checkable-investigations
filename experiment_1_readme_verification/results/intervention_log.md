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

### D-07 — 2026-09-02 — engine_failure kind may be unstated

Caught by: checker rejecting 2 batch_023 claims whose event.kind was
"unstated". The frozen glossary's engine entry says to record kind as
refusal, wrong_answer, or unstated; the checker enum lacked unstated.
Artifact: check.py and SCHEMA.md accept unstated. Query-time consequence:
an engine_failure with kind unstated is a witness that is undecided, so
H08 counts it toward unverifiable, never toward vacuous verification.

### D-08 — 2026-09-02 — pre-redaction spans restricted to text that differs

Mechanical cut, not content targeting: a pre-redaction span whose
whitespace-normalised text equals some current-file span of the same path
adds no claim the current translation lacks (its claims would be
byte-identical with a different commit). Only spans whose text differs are
translated. 306 pre-redaction spans → 89 differing; 22 batches → 8.
Old batch files kept under ledger/batches/pre_d08/.

### D-09 — 2026-09-02 — seat inputs dropped between inventory and schema; scanned absence

Caught by: the owner's question about H04 and Q32 after the interim arm
comparison. (a) The inventory declares inputs(d) for seat dispatches; the
D-01 schema omitted the field and the brief never asked for it, so the 21
seat_dispatch events in the ledger carry none and H04 was unverifiable.
Artifact: event.inputs (required list on seat_dispatch, [] allowed),
checker rule, brief v0.7 rule 34; targeted retranslation of the current-
file spans carrying dispatch-input vocabulary (mechanical regex selection,
ledger/batches/_d09_pending.json), pre-redaction spans pick it up in their
normal batches. (b) The schema states absence only when a span states it;
absence over a whole artifact (Q32) is now a query-step claim with a
declared search that the checker re-derives (SCHEMA.md 'Absence by
search'); translators never produce it.

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
question was needed. batch_057 (Sonnet, git log) — 1 more hit ('my two
misreported numbers' → n=2), caught by the rule; retranslated. The class
(a nearby count read as an erratum number) recurs at low rate in both
tiers and is fully mechanically caught; no further amendment.

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

### I-05 — 2026-09-02 — 'coordinator' not in the actor vocabulary

Caught: translators of batch_023 and batch_031 both reported recording
actor unstated for rulings headed "(coordinator, 2026-08-04)" because the
word is not in the actor enum. Class: record vocabulary → enum mapping
missing (the arc-1 name for the driver role).

Operationalised: glossary amendment G-04 (actor word mapping), rendered.
Mechanical selection: accepted spans containing 'coordinator' or
'orchestration seat' with an event claim whose actor is unstated are
retranslated whole (ledger/batches/_g04_pending.json), folded into the
consolidated retry.

Recurrence: (tracked)

### I-06 — 2026-09-02 — brief rule 23 vs amendment G-04 on signed decisions

Caught: the batch_036 translator ("G-04 overrides the brief ... if the
coordinator intended rule 23 to win, these 5 claims need retiering").
Class: two machinery texts disagreeing; the translator chose one and
flagged it, which is the correct behaviour.

Operationalised: glossary amendment G-05 (precedence: a signature naming
the owner's authorization is human with both actors; coordinator-only is
driver/stated). Checker rule: a claim quoting `signed_by` whose quote
names Matt/owner must be tier human (I-06). Affected accepted claims
re-split and retranslated.

Recurrence: batch_039 (dispatched before G-05 was written) — 1 hit,
caught by the checker rule; retranslated. Not a post-fix recurrence: the
translator had not seen G-05. batch_043 (dispatched AFTER G-05) — a
genuine recurrence of the class: the COUNTERSIGNED marker fired for a
countersignature by a review seat. G-05 had fixed signed_by only.
Generalised as G-06 (every signature marker: the named signer decides).
Affected spans reselected mechanically (retry_G06). This is the first
defect class needing a second fix after its first fix was operationalised.

### I-07 — 2026-09-02 — commit sub-events without an ordinal

Caught: checker (122 of 205 claims in batch_059, Sonnet, rejected for a
missing ordinal). Class: brief rule 18 never said sub-events of a commit
inherit the commit's ordinal and date, while rule 15 says so for ledger
entries; Opus translators had assumed the parallel, Sonnet did not.

Operationalised: brief v0.6 rule 18 (inheritance sentence). The checker
rule already existed (D-02), so every instance was caught mechanically;
rejected claims retranslated with the same ids.

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


## Process events

- 2026-09-02 ~12:40 PT — session rate limit hit with 13 translators in
  flight (batches 052-063, batch_047 retry); all terminated by the API
  before writing output. No partial output reached ledger/out. Dispatch
  paused; owner asked for a slower pace. Remaining at pause: git-log
  batches 052-099 (48), pre-redaction batches 100-121 (22), retry_G06b
  (88 spans reselected under G-02/G-04/G-06, not yet split or dispatched),
  batch_047 single-claim retry.

## Compactions

(none recorded yet)

### Process event — 2026-09-02 — query-logic defects found by reading the arm comparison row by row

Not ledger edits; analysis code only. Q35 and H15 live-run checks had been
reported as fixed but the file was never changed (Q35 looked only for LICENSE
files; H15 treated `BP/` literally) — fixed now, both verify. H10 verified
on the mere mention of "sign" in PRUNED.md claims — now folds the Q32
absence-by-search, contradicted. Q27 accepted any coverage=1.0 without the
population the README binds it to — now requires it, contested (only the
39-node census reaches 1.0). Verdict nodes silently ignored providers no
query evaluates (residue items), so V01 read verified with need (b)
unaddressed — unevaluated providers now make the node contested. Live-run
conflict to adjudicate: `setup_env.sh --check` exits 0 here (Q40/Q43) where
the baseline reports exit 1 with two failing self-tests; pytest gives
2267 passed / 4 skipped here vs the baseline's 2,270 / 1 (Q24).

### Process event — 2026-09-02 evening — resumed dispatch; git-derived census for H03/H11; D-09 third batch

Dispatch resumed at two concurrent translators after the 18:10 reset.
Git-log batches 087-099 (Sonnet) all accepted; batch_090 returned 48
value claims tagged kind "event" with a null event object — the checker
rejected them and the same translator reclassified them (retry1, all
accepted). The git-log source class is complete. The append-only
conjunct of H03/H11 is decided by a git census (tier git, live run):
of 45 first-parent commits touching ITERATION_NOTES.md only 6d01415b
deletes lines (121 deleted, 89 added). H03 now verified; H05 verified
from commit linkage (31 entries, 0 date mismatches); H11 waits on the
pre-redaction batches. Merging under the D-09 checker rule exposed 21
pre-D-09 seat_dispatch events without inputs; 18 of their spans were
outside the vocabulary selection and are now a third retranslation
batch (retry_D09c) selected by claim predicate.

### Process event — 2026-09-02 ~20:15 — H04 decided from event.inputs; scope caveat for adjudication

After D-09a/c, 81 seat_dispatch events, 50 with recorded inputs; H04
reads verified (no input names panel labels, the design document, or
prior verdicts as received; mentions inside negations such as "never
shown seat verdicts" count as exclusions). Caveat for the packet: the
translators apply seat_dispatch to adversarial-review dispatches too,
and two such events (L1L2 review, current and pre-redaction) list truth
files among the reviewer's inputs. The inventory scopes H04 to
adjudication seats, so the query does not count those; the owner should
confirm the reviewer is not an adjudication seat. Spans without claims:
49, of which 31 are pre-redaction spans identical to current text
(D-08, untranslated by design) and 18 are batched spans that got no
claim (15 git-log spans of batch_073, 3 heading-only document spans),
now retry_leftover.

### Process event — 2026-09-02 21:05 — step 5 complete; final merge

All 107 index batches, three D-09 batches, six G-06 reselection batches
and the leftover batch are translated and checked: 14,721 claims, 0
checker failures, 4,080 superseded claims dropped, 29 spans without
claims (all D-08-excluded pre-redaction duplicates). Final scorecard,
ledger arm: Q 40 verified / 5 contradicted / 5 contested; H 10 / 3 / 2;
V 3 verified / 2 contradicted / 6 contested / 1 dangling. Agreement with
the baseline 60/77. Query-logic change at the end: an anti_rule counts as
a do-not-cite marking only when its text speaks of citing, quoting,
re-deriving, striking or staleness; a bare section flag ("UNREVIEWED")
is noted but does not contest a value (Q10 had flipped on such a flag
from a pre-redaction span). Cost and machine-checkability recorded in
results/COST.md and results/arm_comparison.json. Steps 8 and 9 not
started: waiting on the owner.
