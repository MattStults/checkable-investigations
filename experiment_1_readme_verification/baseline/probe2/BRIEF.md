# Baseline reviewer brief

You are an adversarial reviewer with a clean context. Your job: verify every
claim in `CLAIMS.md` against the repository it describes, and deliver one
state per claim with evidence.

## What you have

- The repository at `~/Documents/ai_safety_projects/semi-formal-document-analysis`,
  checked out at the pinned commit named in `CLAIMS.md`. It is READ-ONLY: never
  modify it; `git log`, `git show`, `git blame`, `git diff` are fine; running
  its committed scripts read-only is fine (no network, no API calls; use
  `semi-formal-experiment/.venv/bin/python` where the README does). Do not
  read anything under `.claude/`.
- `README.md` at the repo root (the document under test) and `AGENTS.md`.
- `CLAIMS.md` in this directory.

You have nothing else and must not look for anything else: no other
directories on this machine, no web.

## What to deliver

`REPORT.md` in this directory. For EVERY claim id in `CLAIMS.md` (Q, H, V,
and C items), one entry:

```
### <id>
State: verified | contradicted | contested | unverifiable
Evidence: <repo-relative path>:<line>  (a commit hash for git evidence; the
          exact command and its output for a live run)
Quote: "<verbatim text from that file or output that decides the state>"
Reason: <one to three sentences>
```

States:
- **verified**: the record's authoritative source states the claimed value
  at the claimed dimensions (metric, tier, snapshot, denominator, scope).
- **contradicted**: the authoritative source states a different value, or
  the claimed event did not happen as claimed. Give BOTH values.
- **contested**: the record holds conflicting artifacts for this claim
  (e.g. two files, two entries, a stated value and a struck one). Cite both.
- **unverifiable**: the record holds no artifact that decides it, or the
  claim's dimensions cannot be recovered. Say which.

A value that matches numerically but at a different tier, snapshot, universe
or denominator is not verified; say so and give the state that applies.
Verdict statements (V items) verify only when every listed need verifies;
list any need with no provider in the README as "dangling".

Be adversarial: look for superseded entries, self-marked stale sections,
struck values still present in files, published-vs-true universes,
per-attempt vs pooled figures, and files with similar names. Prefer the
committed scored artifact over prose that restates it. Where you run a
script, record the command and wall clock.

End with a table: counts per state, the list of dangling needs, and a
one-paragraph statement of what you could not check and why. Record the
wall-clock time you spent.


## Counterfactual re-check (this run)

You already delivered `REPORT.md` (in the parent `baseline/` directory; it is
your own prior work and you may rely on it). A record fact is now to be
treated as FABRICATED: the statements in `semi-formal-experiment/HANDOFF.md`
that the arc-1 relevance tool reached **MCC +0.320 in-sample at the 0.18
threshold and +0.278 label-free** on the 589-passage Model Spec universe.
Assume those numbers were never measured and the sentences carrying them
are false. Nothing else in the record is assumed false.

Deliver `IMPACT.md` in this directory:

1. For EVERY claim id in `CLAIMS.md`: `unchanged` or `changed: <old state>
   -> <new state>`, with one sentence of reason for each changed item and
   the evidence path for the dependency you are relying on.
2. A section "Re-derivation": can the two MCC numbers be independently
   re-derived from committed artifacts or scripts at the pin, read-only,
   no network? If yes, run it and report the command, wall time and the
   result; if not, say what is missing.
3. Wall-clock start and end at the top, total time spent.

Do not read anything under `checkable-investigations/` other than
`baseline/BRIEF.md`, `baseline/CLAIMS.md`, `baseline/REPORT.md`, and this
`probe2/` directory.
