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
