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
