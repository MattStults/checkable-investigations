# Live-run conflicts and scope caveats

Adjudication: model-made (delegated by owner).


## Live-run conflicts

Both commands were run read-only from the repository root (`~/Documents/ai_safety_projects/semi-formal-document-analysis`, pin `48e66ce0`, working tree clean apart from ignored files), on 2026-09-03, macOS (Darwin 25.5.0). System `python3` = /usr/bin/python3 (3.9.6, no numpy); venv `semi-formal-experiment/.venv/bin/python` = 3.12.14 with pytest 9.1.1, clingo 5.8.0, pydantic 2.13.4, xclingo 2.0b24, no numpy/scikit-learn.

### Q40/Q43 — `bash setup_env.sh --check` (ledger: exit 0, rerun 2026-09-02; baseline: exit 1, two self-tests failing)

**Ruling:** the environment now reproduces the ledger arm's observation: exit 0.

**Basis** — command `bash setup_env.sh --check` (README:43 and :131), 13:08:58 PDT, wall 2.18 s:
```
--- imports ---
  ok      pytest       9.1.1      the test suite
  ok      clingo       5.8.0      the solver; ...
  ok      pydantic     2.13.4     phase_1 schema and format forcing
--- self-tests that need no network and cost nothing ---
  ok      phase_1/translate.py — 52 passed, 0 failed
  ok      walkthrough/link.py — 21/21 self-test checks passed

environment OK.
EXIT=0
```
The script's only two self-tests are `translate.py --self-test` and `link.py --self-test` (`setup_env.sh:53-56`); those are the "two self-tests" the baseline saw fail, and both pass now. The script exits 1 iff an import is missing or a self-test fails (`setup_env.sh:63-66`).

**Why the arms could differ (inference from the record, not observed):** the check runs against whatever `semi-formal-experiment/.venv` holds at the moment. `requirements.txt` records that `xclingo` was "Discovered missing on the first fresh CI run (2026-08-31): the local venv had it, this file did not" and was added in `6d8e65a4` (2026-08-31 08:40, after the publication commit `6d01415b`); `translate.py --self-test` "fails at import without" pydantic (`requirements.txt`, pydantic entry). A venv created or last refreshed before those pins, or a partially installed one, fails both self-tests and exits 1; a `bash setup_env.sh` refresh (idempotent) repairs it, which is consistent with the ledger arm's exit 0 on its 2026-09-02 rerun. The baseline's exit 1 therefore reads as a venv-state artifact, not a property of the committed code at the pin. Owner input: none needed, unless the baseline arm's stderr is wanted to confirm which imports failed.

**Arms:** ledger right for the current environment; baseline's observation is not reproducible now. Disposition for README:42-43/:131 ("~3 s", "verifies"): grounded — 2.2 s, exit 0.

### Q24 — pytest (ledger: 2267 passed, 4 skipped; baseline: 2,270 passed, 1 skipped)

**Ruling:** the environment reproduces the ledger arm: `2267 passed, 4 skipped, 14 warnings in 322.19s (0:05:22)` (command exactly as README:133, `cd semi-formal-experiment && .venv/bin/python -m pytest -q`, 13:09 PDT; a second `-rs` run gave the same counts in 3 m 04 s).

**Why the two differ (observed):** the `-rs` run names the four skips — `test_latent_fix_tripwires.py:151` (S3b artifact not built; skips in every environment) and three in `test_weight_diag.py:352/:366/:377` with reason "numpy/sklearn are system-python only". `requirements.txt` lists numpy and scikit-learn as commented-out OPTIONAL entries, so the README's `setup_env.sh` venv lacks them and those three tests skip; a venv that has them runs them and reports 2,270/1. Both totals are 2,271 collected with zero failures. The baseline arm's 2,270/1 (and the author's 2026-08-30 figure, `git show 6d01415b`) came from venvs carrying the optional packages; the README's prescribed setup yields 2,267/4. See `Q24.md` for the ruling (contradicted at the pin; tightened wording proposed).

**Arms:** both observations are genuine; the ledger arm's is the one the README's own setup path reproduces. Disagreement is substance with an identified environmental cause, not a code change between runs (`git log -1 -- semi-formal-experiment/test_weight_diag.py requirements.txt` → `6d8e65a4`, 2026-08-31, before both arms ran).

## Scope caveats

_Model-made rulings (adjudicator: Claude, delegated by the owner per ADJUDICATOR_BRIEF.md). Ruled from the record's own definitions: AGENTS.md, CYCLE_DESIGN.md, briefs/README.md, the arc-2 handoff and ledger._

### H04 — do adversarial-review dispatches count as adjudication seats?

**Ruling: no.** The record separates the two roles consistently, and the inventory's `seat_dispatch` domain should be read as the blind verdict-producing seats only. The two review dispatches that list truth files among their inputs are therefore outside H04's antecedent and are not counterexamples. Substance, decided by the record; owner confirmation is welcome but not required.

**Basis**
- `AGENTS.md` "Working rules": "Strongest available model for orchestration, design, and adversarial review; a mid tier for executing a written and reviewed plan; a small model for validated judgment seats — the adjudication seat is proven at small-model/frontier parity". Three roles, named separately; "adjudication seat" is the small-model judgment seat.
- `AGENTS.md` "Things that will silently corrupt a result": "A cycle's own design document is never seat material. Design docs pre-register expected outcomes; handing one to an adjudication seat destroys the judgment." — the blindness rule is stated for adjudication seats.
- `semi-formal-experiment/CYCLE_DESIGN.md:222-223` "A re-closure made without prior designer sign-off must be FLAGGED FOR THE REVIEW SEAT to countersign or block." and `:227-231` "Every judgment seat gets a written `briefs/` file, a closed output schema, and a mechanical validator. The brief states what the seat may never see. A cycle's own design document is never seat material". The review seat is a distinct role; blindness is the judgment seats' property.
- `semi-formal-experiment/briefs/README.md` lists `change_reviewer.md` as "⚠️ Frontier/careful seat ... it exists to catch the implementer's mistakes, so the small-model standard does not apply", and `briefs/change_reviewer.md:19-22` gives its **input** as "the frozen `manifest.json` and `prediction.json`, `state.json`'s recorded `open_shas` / `closure_shas`, and the repo's working tree" — i.e. the reviewer is handed the pre-registered prediction by design. A role whose brief requires the frozen prediction cannot be the role whose brief forbids design documents.
- Arc 2 uses the same split: `HANDOFF_CURRENT.md:56-57` "Seat must be BLIND (packet = claims+span only; never truth or this file)" for escalation seats, while the clean-context adversarial reviewers are dispatched to inspect the record including truth (`L1L2_ADVERSARIAL_REVIEW.md:51-58` lists `ua_truth_visible.json`, `ua_truth_sealed.json`, `ITER1_TRADEOFFS_REPAIR_TRUTH.json`, `GEN_BLOCK1_SCORED.json`, `panel_run1/` among "Repo artifacts inspected").
- The record's own words for the reviewer are "review seat", "change-review seat", "clean-context adversarial review", "reviewer"; "adjudication seat" / "judgment seat" / "ruling seat" / "wave seat" / "panel seat" are reserved for verdict producers.

**Consequence for the ledger.** Events typed `seat_dispatch` whose actor is a reviewer should be retyped `adversarial_review`; H04's witness set is the blind seats (flip adjudicator, ruling/wave/panel seats, blind coders, annotation seats). Side note for the owner, outside H04: the L1/L2 reviewer read `ua_truth_sealed.json`, a file the record marks single-use and sealed; the disposition itself notes "the UA seal needed a guard" (ITERATION_NOTES.md:890). That is a process observation, not a blindness violation of an adjudication seat.

**Owner input needed:** no (confirmation only). **README disposition:** "blind adjudication seats" stands as worded.

### H08 — what counts as a symbolic-engine failure versus a scoring-code bug?

**Ruling: the record's own boundary is the clingo-evaluated artifacts and the code that emits, checks and solves them; instrument and tooling defects fall outside it. One item sits on the boundary and only the owner can place it.**

**Basis for the boundary**
- The README names the engine by its functions: "the symbolic engine (ASP/clingo evaluation, conflict enumeration with witness scenarios, satisfiability checks)" (README.md:23-24). In arc 1 those are `semi-formal-experiment/emit_asp.py`, `checker.py` (satisfiability of definitions and rule triggers: `checker.py:118` "definition is unsatisfiable under the axioms (vacuous)", `:148` "trigger unsatisfiable under axioms (dead rule)"), `run_conflicts.py` (`:37-38` "One witness scenario for a given conflict"). In arc 2 the same functions live in `behavior_pilot/satisfiability_census.py`, `calculus.lp`, and the walkthrough link stage's clingo checks (`link._check_clingo`).
- The record itself distinguishes engine from instrument: `PROJECT_ASSESSMENT.md:104` "the biggest single improvement in the whole record came from fixing a *measuring instrument*, not the engine"; `semi-formal-experiment/HANDOFF.md:1352-1355` "DELETED, IT WAS ALL BUG ARTIFACT ... Every number in it came from the broken loader" (`benchmark._clause_rows` dropping `section_path`); `HANDOFF.md:1478-1480` "`jaccard({},{}) == 1.0` meant all-empty runs reported *perfect* self-agreement" — a metric bug.
- Therefore **not** engine failures: scorer/loader bugs, `route.py`/`atom_provenance.py` KeyErrors (path plumbing), heredoc patch no-ops, `ModuleNotFoundError: clingo` (environment; AGENTS.md calls it "a known environment gap, not a failure"), LLM-seat document-completion, and the blind-rater "global question" failure (a human/LLM instrument experiment). The ledger's `engine_failure` events of these kinds should be retyped.
- **Engine refusals** (kind = refusal) on the record: the two `checker.py` error classes; `ITERATION_NOTES.md:117-121` "SC.census REFUSES contracts declaring governs_conditional ... The engine itself consumes it fine."
- **Boundary case — wrong-answer-shaped:** `walkthrough/OPEN_QUESTIONS.md:373` "Q-22 ⛔ DEFECT — an UNSATISFIED `requires` is silently false, not an error" ... `:389-391` "silently false in every enumerated situation" ... "An unsatisfiable promise is currently indistinguishable from a kept one." Fixed in 818045f4 (2026-08-09) "Q-22 FIX: an unsatisfied `requires` now reaches the situation signature". This is the ASP situation-enumeration stage of arc 2's walkthrough returning answers it should have refused: a silent wrong answer by the README's own "refusals, not wrong answers" test, if the walkthrough link stage is part of "the symbolic engine". The inventory scoped H08 to arc 1, which excludes it; the README sentence carries no arc restriction.
- **Encoding-level findings are not engine failures:** `adversarial_review_1.md` findings 7, 8, 9 (fragment selection, an unlicensed `incompat` axiom, a vacuous planted check) are defects in what was fed to the solver; the same review's finding 1 says "Core solver numbers reproduce exactly". The README already scopes these ("every 'unresolved conflict' is a claim about an encoding and a fragment, not about the document", README.md:191-193).

**What only the owner can settle:** whether "the symbolic engine" in the README includes the walkthrough link/clingo stage (then Q-22 is a recorded wrong answer and H08/V02 are contradicted) or means the arc-1 engine only (then no wrong answer is on record, no failure census exists, and H08/V02 stay unverifiable). The nine `wrong_answer`-typed ledger events referred to in INDEX.md are not reproduced in the H08 packet and could not be checked; only four ids are listed there.

**Owner input needed:** yes. **README disposition:** tightened per H08.md, or kept as an explicit commitment to publish the engine-failure census the sentence presupposes.
