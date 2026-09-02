# Orchestration instructions — Experiment 1: README verification by claim ledger

You are the orchestrator for a pre-registered experiment. The registered design
is the blog post "Pilot: verifying my own README with a claim ledger"
(https://mattstults.github.io/2026/09/01/readme-verification-pilot.html, source:
`mattstults.github.io/_posts/2026-09-01-readme-verification-pilot.md`). Read it
first, in full. Its Design and Registered expectations sections are FROZEN: you
never edit them, and where these instructions and the post conflict, the post
wins and you stop and tell the owner.

Everything you produce lands in this directory
(`checkable-investigations/experiment_1_readme_verification/`), committed in
registration order. The experiment's subject is the README of
https://github.com/MattStults/semi-formal-document-analysis (local clone:
`~/Documents/ai_safety_projects/semi-formal-document-analysis`), pinned to one
commit that you record in the claim inventory and never move.

## Roles and model tiers

Set the model explicitly on every subagent dispatch; never inherit by default.

- **Orchestrator (you, strongest available tier)**: builds the inventory,
  glossary, checker and briefs; seeds the first translations; verifies; runs
  the process. You do design and verification work, not bulk production.
- **Translators (lower tier — start with Opus; optionally probe Sonnet/Haiku
  and report per-tier)**: translate source spans into ledger claims under the
  written brief. After the seeding phase, ALL ledger content comes from this
  tier. Frontier-seeded spans are retranslated by the lower tier under the
  final brief; the seeds are kept in `brief/` as development artifacts, never
  in the final ledger.
- **Baseline reviewer (frontier-class, one clean-context agent)**: the
  incumbent method. Runs exactly once, plus once for the perturbation probe.

## Blindness rules (violating any of these voids the experiment)

1. **Translators never see**: the README under test, the claim inventory, the
   baseline report, the blog posts, or these instructions. They see only: the
   source spans assigned to them, the translator brief, and the glossary.
2. **The baseline reviewer never sees**: the ledger, the brief, the glossary,
   the intervention log, or these instructions. It sees: the pinned README,
   the target repo, and `baseline/BRIEF.md`.
3. **You never write or edit a ledger claim by hand.** When you catch an error,
   record it as a numbered finding in `results/intervention_log.md`, fix it
   through the machinery — a brief amendment, a glossary entry, or a new
   checker rule — and have the affected spans retranslated. Every intervention
   entry records: what was caught, the operationalized artifact it produced,
   and whether the same defect class recurs afterward. This log is a primary
   result.
4. The target repo is **read-only** for this experiment (read its `AGENTS.md`
   before acting in it at all). The blog post gains only a Results section at
   the end, owner-approved; nothing else in it changes.

## Identity and entities

Interactions are reified: an event is a first-class entity with its own id
(`tool_call(e4471, agent_0412, ...)`, `arg(e4471, ...)`), referencing its
participants by entity id. Facts about an interaction live on the event, never
"inside" either participant.

- **Equivalence, not substitution.** An unresolved participant gets its own
  minted constant (`unresolved_actor_17`), and identity resolution arrives as
  a separate provenance-carrying claim (`same_entity(unresolved_actor_17,
  agent_B)`) cited to the evidence that established it. Queries close over the
  equivalence relation. Never rewrite a claim to swap in a resolved identity:
  an equivalence claim is contestable and retractable like any other, and
  retracting a bad one must update every conclusion that flowed through it.
- **Trajectory segments are the ground-level agent entities.** A restart or
  compaction boundary starts a new segment; `continues(seg_2, seg_1)` is
  itself a claim with provenance (continuation is an inference from harness
  records and can be wrong or partial). Agent-level identity is the
  equivalence closure over segments. Hypotheses about what an agent knew at a
  time derive through these links, so a broken continuation is a link-level
  correction, not a retranslation.
- **Distinctness is load-bearing.** In the target record, fresh sessions of
  the same model (seats, waves, auditors) are distinct entities; several
  hypotheses ("blind", "independent", "the original auditor", "a separate
  agent", "the project's own review") are actor-identity claims. Entity
  identity is a declared dimension in the claim inventory (step 1), and the
  glossary (step 2) carries the identity registry: what counts as the same
  seat/agent/process across artifacts, with the seats-are-distinct rule
  stated. The translator brief carries the minting rule so translators create
  unresolved-actor constants instead of guessing identities.

## Order of work

Each numbered step ends with a commit to this repo. Steps marked **[OWNER]**
stop for the owner's explicit sign-off before anything later starts.

1. **`claim_inventory/`** — Extract the pinned README's checkable statements.
   Each claim: the verbatim README sentence, the atomic value(s) asserted, and
   the dimensions needed to verify it (metric, measurement tier, snapshot,
   denominator, and — for event claims — actor entity ids per the Identity
   and entities section). Convert prose claims to hypothesis rules over event
   predicates (type, timestamp, linkage), each with an English round-trip
   statement. Represent verdict words as nodes declaring named needs with
   adjacent sentences as candidate providers; type author commitments; list
   the evaluative residue verbatim. **[OWNER: freezes inventory and confirms
   each hypothesis round-trip.]**
2. **`glossary/`** — Metric definitions and the authoritative-artifact map,
   each entry citing the record document that defines it. Known hazard classes
   to verify against the record and encode (do not take these on trust —
   confirm each against the sources): raw vs. panel-tier scores; per-attempt
   series vs. pooled snapshots; superseded ledger entries (the handoffs mark
   their own stale sections); opposing panel rulings on the same node;
   in-sample vs. fresh-draw certification; the three differently-named
   `behaviours.json` files (a documented trap in the target README itself).
   Primary sources include: the arc-2 ledger `ITERATION_NOTES.md` (entries
   0000–0043), the `round4_*_scored_raw.json` and `ITER*_SCORED.json` files,
   `semantic_audit.json` / `SEMANTIC_AUDIT.md`, `graph_check.py` (runnable),
   `benchmark.py` (runnable), and the git log. The glossary also carries the identity registry (see Identity and
   entities). **[OWNER: freezes glossary.]**
3. **`checker/`** — The mechanical checks, runnable and committed: every
   claim's quote is a verbatim substring of its cited source file; every rate
   re-derives from its recorded numerator and denominator; every hypothesis's
   event claims carry the declared dimensions; supersession links resolve.
   The checker's output is the pass/fail list by claim id.
4. **Seed translations (frontier, you)** — Translate the first few source
   spans yourself to learn what the brief must say. Everything that surprises
   you becomes brief text, a glossary addition, or a checker rule. Write
   `brief/BRIEF.md` (with an amendment history section that grows over the
   run). Seeds are committed under `brief/seeds/` and are NOT ledger content.
5. **Lower-tier translation** — Dispatch translators span by span under the
   brief. Run the checker on every batch; rejected claims go back for
   retranslation (log the rejection counts — a registered expectation depends
   on them). Contradictory artifacts are recorded contested, never resolved.
   When the brief stabilizes, retranslate all seeded spans at the lower tier.
   Done when the checker passes the full ledger clean. Commit `ledger/`.
6. **`baseline/`** — Write `baseline/BRIEF.md` first: the reviewer must
   adversarially verify every inventory claim against the repo and deliver the
   same four states (verified / contradicted / contested / unverifiable) with
   a file citation and verbatim quote for each verdict. Dispatch one
   clean-context frontier agent. Commit its report untouched.
7. **`results/` — queries** — Map each inventory claim to a query against the
   checked ledger; record each claim's terminal state with its derivation.
   Run the checker's re-verification over the baseline's citations too and
   report the machine-checkable fraction for both arms.
8. **Perturbation probe** — Only after both arms are committed: pre-register
   the mutation (which single README number changes, chosen and written down
   before running either re-verification), then run both arms' re-checks.
   Record cost and correctness for both. Costs throughout: report what you can
   actually measure (subagent count, tokens where visible, wall clock), and
   state the measurement method next to every number.
9. **Adjudication packets [OWNER]** — Bundle every contradicted / contested /
   unverifiable item and every dangling verdict into packets (claim, both
   values, provenance, no recommendation). The owner rules; rulings are
   committed. The README disposition commit in the target repo (grounded /
   tightened / deleted / kept-as-commitment per item) happens only with the
   owner's approval, as does the Results section added to the blog post.

## Registered expectations you are being scored against

From the post, verbatim in spirit — read them there. In short: (1) the build
completes with no untracked edits and the finished ledger passes its own
automated re-check end to end, with the checker having fired at least once,
at least one contested pair held open, and at least 2 prose-claim hypotheses
ending definite; (2) on the perturbation probe the ledger re-verifies
correctly at under 10% of its build cost while the baseline pays roughly full
price. Do not shade the run toward making these true: if an expectation is
going to fail, that is a result — record it and keep going. What would void
the run instead is a blindness violation or an untracked edit.

## Stop conditions

Stop and report to the owner (rather than improvising) if: a blindness rule is
at risk; interventions stop converging (the same defect class needs a human
again after its fix was operationalized, or interventions approach one per
claim); the inventory demands a dimension translation cannot recover for a
large fraction of claims; or anything requires editing the target repo, the
frozen post sections, or spending against an external API (this experiment is
subagent work over local files — the target repo's own budget machinery is
not yours to touch).

## Completion

The experiment is done when: all nine steps are committed in order, the
checker passes the final ledger clean, both arms and the probe have recorded
costs, the adjudication packets are with the owner, and a draft Results
section (facts and tables only, no verdict language) is ready for the owner
to edit into the post. Report back with: each registered expectation's
outcome, the intervention log summary, both arms' costs, and the list of
items awaiting owner rulings.
