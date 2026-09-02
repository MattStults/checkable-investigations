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
