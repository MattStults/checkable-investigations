# Adjudication packets (step 9)

One file per item whose ledger state is contradicted, contested, unverifiable or dangling. Each packet gives the README text, the inventory's values and dimensions, the ledger arm's derivation with the claims it rests on (verbatim quotes and sources), the baseline arm's state and reason, and any live-run evidence. No recommendation is made; the owner rules, and rulings are committed alongside.

| item | ledger | baseline | packet |
|---|---|---|---|
| Q02 | contradicted | contradicted | [Q02.md](Q02.md) |
| Q06 | contested | contested | [Q06.md](Q06.md) |
| Q24 | contradicted | verified | [Q24.md](Q24.md) |
| Q27 | contested | contested | [Q27.md](Q27.md) |
| Q28 | contested | contradicted | [Q28.md](Q28.md) |
| Q29 | contested | contradicted | [Q29.md](Q29.md) |
| Q32 | contradicted | contradicted | [Q32.md](Q32.md) |
| Q33 | contradicted | contradicted | [Q33.md](Q33.md) |
| Q34 | contradicted | contradicted | [Q34.md](Q34.md) |
| Q48 | contested | contradicted | [Q48.md](Q48.md) |
| H01 | contradicted | contradicted | [H01.md](H01.md) |
| H02 | contested | verified | [H02.md](H02.md) |
| H06 | contested | verified | [H06.md](H06.md) |
| H08 | contradicted | unverifiable | [H08.md](H08.md) |
| H10 | contradicted | contradicted | [H10.md](H10.md) |
| V01 | contested | contested | [V01.md](V01.md) |
| V02 | contradicted | unverifiable | [V02.md](V02.md) |
| V03 | dangling | unverifiable | [V03.md](V03.md) |
| V05 | contested | contested | [V05.md](V05.md) |
| V06 | contradicted | contested | [V06.md](V06.md) |
| V07 | contested | contradicted | [V07.md](V07.md) |
| V08 | contested | verified | [V08.md](V08.md) |
| V11 | contested | verified | [V11.md](V11.md) |
| V12 | contested | contested | [V12.md](V12.md) |

## Live-run conflicts (both arms ran code; results differ)

| item | ledger arm | baseline |
|---|---|---|
| Q40/Q43 setup_env.sh --check | exit 0 (rerun 2026-09-02) | exit 1, two self-tests failing |
| Q24 pytest | 2267 passed, 4 skipped | 2,270 passed, 1 skipped |

## Scope caveats surfaced during the run

- H04: translators tag adversarial-review dispatches as seat_dispatch; two such events list truth files among the reviewer's inputs. The inventory scopes H04 to adjudication seats. Owner to confirm the reviewer is not an adjudication seat.
- H08: translators label scoring-code bugs as engine_failure alongside symbolic-engine wrong derivations. Owner to define the engine-failure scope; the 9 wrong_answer events are listed in the H08 packet.
