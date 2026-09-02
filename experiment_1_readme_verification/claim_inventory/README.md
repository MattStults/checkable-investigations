# Step 1 — Claim inventory

Extracted by the orchestrator from the README of
[semi-formal-document-analysis](https://github.com/MattStults/semi-formal-document-analysis)
at commit `48e66ce04a4d9f06771c42f89cb37b075583c5f6` (2026-09-01 17:44 -0700),
before any translation, glossary, or record reading beyond a directory listing
and the ledger's section headings (needed only to name the dimension vocabulary).

Files:

- `inventory.json` — source of truth. Sections: `pin`, `dimension_vocabulary`,
  `event_predicates`, `claims` (Q01–Q41), `hypotheses` (H01–H11),
  `verdict_nodes` (V01–V12), `commitments` (C01–C07), `residue` (R01–R12).
- `inventory.md` — rendered view, for review.
- `render.py` — renders the markdown and fails if any quoted sentence is not a
  verbatim (whitespace-normalised) substring of the pinned README.

Counts at freeze:

| Section | Count |
|---|---|
| Quantitative / checkable claims | 41 |
| Prose-claim hypotheses | 11 |
| Verdict nodes | 12 (1 with no candidate provider: V03) |
| Author commitments | 7 |
| Evaluative residue | 12 |

Conventions:

- A README sentence carrying several atomic values gets one claim id per value
  (e.g. Q08/Q09 from one parenthetical; Q05/Q11 are the same value in two
  sentences and are kept as two ids so each README occurrence terminates in a
  state).
- "Tier" names how a number was produced (raw / panel / adjudicated / human /
  live_run / git / filesystem / stated). Where the README does not say, the
  inventory lists the candidates and the ledger query must find the one the
  record actually holds. A value that matches at the wrong tier is a
  contradiction, not a verification.
- Every hypothesis names the event dimensions (type, timestamp, linkage)
  translators must carry for it to be decidable; the translator brief inherits
  that list without the hypothesis text.

Freeze: this directory is frozen on owner sign-off. Later steps may reference
claim ids but never edit this file set. If a defect is found in the inventory
after freeze it is logged in `results/intervention_log.md` and the claim is
marked, not silently fixed.

## Pre-registered addendum: forensic layer (added 2026-09-02, before freeze)

The README is not the only source of questions. If the agents in the record
lost their way, the ledger must let us trace what agent did what, with what
context, and whether the same mistake recurred after a handoff or compaction.
`inventory.json` therefore declares a `forensic` section: actor, session,
context-origin, erratum-class, recurrence, caught-by and asserted-transfer
predicates; a defect-class vocabulary drawn from the record's own errata; and
five pre-registered forensic queries F01–F05.

These are **not README-derived and not part of the registered expectations**
(which are scored over Q/H/V claims only). Their outcomes, including their own
unverifiable count, are reported in a separate results table. Translators
carry the forensic attributes on every event-shaped span; the blog post is
unchanged.

## Second addendum (2026-09-02, before freeze): coverage, provenance, sequence

- **Exhaustive translation.** Spans are assigned exhaustively over the named
  primary sources, never targeted at README-relevant spans, so omission and
  selection questions (X01) are answerable and no README knowledge leaks into
  span choice.
- **`readme_blame.json`** — per-line commit, date, author and summary for the
  pinned README, so each claim can be dated and attributed (X02, X03).
- **Q42, Q43** — relative links resolve; the "Start here" sequence runs as
  written.
- **Query classes X01–X06** — selection, true-then-superseded vs never-true,
  sentence-before-or-after-withdrawal, discrepancy direction, evidence grade
  against commitment C02, internal consistency. All derivable at query time
  given the above.

## Revision after clean-context review 1 (2026-09-02)

`review_1.md` is the reviewer's report, committed untouched (Opus, clean
context, given the inventory, the pinned README and read access to the record).
Its verdict was not-fit-to-freeze with six blocking findings. This revision
applies every blocking and should-fix item:

- Non-vacuity guard (`min_witnesses`) and a day-resolution order relation for
  all ∀-hypotheses; pre-redaction history declared an in-scope source.
- H03, H07, H09, H11 rewritten; H12–H15 added (span-and-reason per hit,
  re-derivation of decisive findings, every step has an entry, ARTIFACTS.md
  lists every star artifact — promoted from C06).
- New dimensions: `threshold_rule`, `universe`, `provenance_region`,
  `anti_rule`, `not_to_be_confused_with`; tier gains `cove`, supersession
  gains `struck`.
- Q16 now a per-element tiered series with the 0.895 adjusted value; Q01/Q02/
  Q03/Q04/Q06/Q17/Q29/Q32/Q34/Q37 sharpened; Q44–Q49 added; R03 split.
- Forensic layer: defect classes extended to cover all thirteen errata found;
  `caught_by` is a set with an inferred flag; block is the session unit; F01
  redefined; F06–F09 added.

Counts now: 49 claims, 15 hypotheses, 12 verdict nodes, 6 commitments, 12
residue, 9 forensic queries, 6 additional query classes.

## Revision after clean-context review 2 (2026-09-02)

`review_2.md` (committed untouched) audited closure of review 1: 41 closed, 6
partial, 1 declined, and found two blocking regressions (Q44 values, Q04
referent) plus should-fixes. All applied: Q44 values corrected; Q04 terminates
contested if the record holds more than one registration; `min_witnesses`
default and witness definition; cross-source order relation; H14 domain from
step-emitted artifacts; H15 inverted to the decidable direction (coverage half
→ R13); tier constrained to an enum with a separate `venue`; H09/H07/H13
round-trips corrected; Start-here count fixed (6 steps, 7 commands);
`caught_by` rule and historical-attribution precedence stated.

**Sealed annex.** Both reviews found the specific traps by probing the record
with the incumbent method (frontier adversarial review) armed with this
inventory. Pre-declaring those instances in the inventory would hand the
answers to both arms. So the inventory keeps only the general dimensions, and
the instances (26 ids) live in `sealed_instances.json`, which neither the
translators nor the baseline reviewer sees. At results time it is a scorecard:
per instance, which arm surfaced it unprompted. That the reviews found them
where five prior unstructured reviews did not is itself a reported result.
