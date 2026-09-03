# Counterfactual impact re-check — IMPACT.md

**Wall-clock start:** 2026-09-03 08:23:55 PDT (15:23:55 UTC) — first tool call of this run
**Wall-clock end:** 2026-09-03 08:28:20 PDT (15:28:20 UTC)
**Total time:** 4 min 25 s (08:23:55 → 08:28:20 PDT)

*Interruption note.* This run was interrupted three times by server-side overloads
(coordinator-confirmed, not caused by the work). No IMPACT.md content had been written
before the first interruption; the start time above is the earliest timestamp I recorded
myself, at my first tool call. The elapsed total therefore excludes idle time spent inside
the aborted attempts, which I have no recorded clock for.

Repository re-verified at the same pin `48e66ce04a4d9f06771c42f89cb37b075583c5f6`
(`README: publication links and CI badge filled`, 2026-09-01 17:44:18 -0700),
working tree clean.

**Environment change since REPORT.md.** The prior report noted that
`semi-formal-experiment/.venv` was a broken symlink farm pointing at an out-of-repo
Python that had moved to 3.12, so live runs had to be reconstructed. At this run the
venv has been rebuilt in place (`pyvenv.cfg: version = 3.12.14`, `.venv/bin/python -V`
→ Python 3.12.14, `clingo`/`pytest`/`pydantic` all import). `.venv*/` is `.gitignore`d,
so this is machine state, not a change in the record. Every live command below ran as
the README writes it, with `.venv/bin/python`.

---

## The counterfactual as stated, and what it can consistently mean

The assumption: the statements in `semi-formal-experiment/HANDOFF.md` that the arc-1
relevance tool reached **MCC +0.320 in-sample at the 0.18 threshold** and **+0.278
label-free** on the 589-passage Model Spec universe are FABRICATED — "assume those
numbers were never measured and the sentences carrying them are false."

Those sentences occur at `semi-formal-experiment/HANDOFF.md`:44
("label-free sits at +0.278, best compliant config +0.316, judge mean +0.555"),
:480 ("| tool @0.18 (in-sample) | +0.274 | **+0.320** |") and
:1386 ("On the true universe: tool @0.18 +0.320, judges +0.555").

**The strong reading is not satisfiable at this pin.** "Never measured" is refuted by
the record itself: a committed script regenerates both numbers from committed data,
read-only, with no network, in under five seconds (see **Re-derivation** below). The
measurement exists independently of the prose.

I therefore evaluate the only consistent reading: **HANDOFF.md's three sentences are
struck as evidence** — they may not be cited, and any claim whose decisive support was
one of them loses that support. This is also the reading the original brief's own
evidence hierarchy demands ("Prefer the committed scored artifact over prose that
restates it"): the HANDOFF sentences were never the authoritative source for these
numbers, only a restatement of them.

**Consequence: no claim changes state.** Exactly one entry in REPORT.md cited a
fabricated sentence at all — Q13, and only as a secondary corroborator alongside the
live `benchmark.py` run that is its primary evidence. Q13's state survives on the
primary evidence plus two further HANDOFF-independent artifacts identified in this run
(`semi-formal-experiment/test_quality_floor.py`:64-74 and my own live re-derivation).

Where the fabrication *does* bite is on the author commitments, which carry no state:
it would put a false quantitative sentence in a starred handoff, which C01 and C02
speak to. Reported under C01/C02 below.

---

## Per-claim impact

### Quantitative / checkable claims

| id | impact |
|---|---|
| **Q01** | unchanged (verified) |
| **Q02** | unchanged (contradicted) |
| **Q03** | unchanged (verified) |
| **Q04** | unchanged (contradicted) |
| **Q05** | unchanged (verified) |
| **Q06** | unchanged (contested) |
| **Q07** | unchanged (verified) |
| **Q08** | unchanged (verified) |
| **Q09** | unchanged (verified) |
| **Q10** | unchanged (verified) |
| **Q11** | unchanged (verified) |
| **Q12** | unchanged (verified) |
| **Q13** | unchanged (verified) |
| **Q14** | unchanged (verified) |
| **Q15** | unchanged (verified) |
| **Q16** | unchanged (verified) |
| **Q17** | unchanged (verified) |
| **Q18** | unchanged (verified) |
| **Q19** | unchanged (verified) |
| **Q20** | unchanged (verified) |
| **Q21** | unchanged (verified) |
| **Q22** | unchanged (verified) |
| **Q23** | unchanged (verified) |
| **Q24** | unchanged (verified) |
| **Q25** | unchanged (verified) |
| **Q26** | unchanged (verified) |
| **Q27** | unchanged (contested) |
| **Q28** | unchanged (contradicted) |
| **Q29** | unchanged (contradicted) |
| **Q30** | unchanged (verified) |
| **Q31** | unchanged (verified) |
| **Q32** | unchanged (contradicted) |
| **Q33** | unchanged (contradicted) |
| **Q34** | unchanged (contradicted) |
| **Q35** | unchanged (verified) |
| **Q36** | unchanged (verified) |
| **Q37** | unchanged (verified) |
| **Q38** | unchanged (verified) |
| **Q39** | unchanged (verified) |
| **Q40** | unchanged (unverifiable) |
| **Q41** | unchanged (verified) |
| **Q42** | unchanged (verified) |
| **Q43** | unchanged (contradicted) |
| **Q44** | unchanged (verified) |
| **Q45** | unchanged (verified) |
| **Q46** | unchanged (verified) |
| **Q47** | unchanged (verified) |
| **Q48** | unchanged (contradicted) |
| **Q49** | unchanged (verified) |
| **Q50** | unchanged (verified) |

Notes on the four entries the assumption could plausibly have touched:

- **Q12** (`mcc_tool_in_sample = 0.32`) — **unchanged: verified.** Its evidence in
  REPORT.md was never HANDOFF.md: it was the live `benchmark.py --tool` run,
  disclosure note 5, "the in-sample mean MCC (+0.274 published / **+0.320** true) is a
  CEILING, not a result", corroborated at `semi-formal-experiment/benchmark.py`:1701.
  Re-run at this pin (exit 0, 11.98 s) and re-derived independently at +0.3197 (§Re-derivation).
  Dependency relied on: `semi-formal-experiment/benchmark.py` + `annotations_b8.json` +
  `behavior_atoms_b8.json` + `data/behaviours.json` (via `load_true_panel`).
- **Q13** (`mcc_tool_label_free = 0.278`) — **unchanged: verified.** This is the one
  entry that cited a fabricated sentence (`semi-formal-experiment/HANDOFF.md`:43-44),
  and only as a corroborator. Strike it and the primary evidence stands: the live
  benchmark's "Universe delta" mean row `| **mean** | | **+0.278** | +0.219 | …`, plus
  two HANDOFF-independent supports found in this run —
  `semi-formal-experiment/test_quality_floor.py`:69-70 ("Measured label-free:
  helpfulness +0.2007, harm-avoidance +0.3502, over/under +0.2826", mean +0.2778) and
  my live re-derivation. The "label-free" characterisation, which is the part the
  HANDOFF sentence supplied in REPORT.md, is independently established by
  `test_quality_floor.py`:114-117 ("`idx.predict(b)` is the SHIPPED label-free path")
  and `benchmark.py`:1026 `label_free_cuts` / `thresholds_frozen.json`
  ("Derived label-free: these are the Otsu cuts this exact configuration computes").
- **Q14** (`mcc_judges_loo_mean = 0.555`) — **unchanged: verified.** The +0.555 figure
  appears in the same HANDOFF sentences, but the assumption is scoped to the *tool's*
  two numbers, and Q14's evidence was the live benchmark run in any case
  (`| **mean** | … | **+0.555** | +0.394 | …`).
- **Q48** (handoff starred blocks) — **unchanged: contradicted.** It cites
  `semi-formal-experiment/HANDOFF.md` for heading *structure* (four star-marked blocks
  at :3/:99/:131 and undated sections at :504-:609), not for any MCC value. A fabricated
  quantitative sentence inside the file does not move the structural finding; if
  anything it strengthens the adversarial reading of the file.

Also unaffected though it quotes the same file: **Q02** cites
`semi-formal-experiment/HANDOFF.md`:865 ("Inter-judge Jaccard is 0.16–0.62 and gold is
the intersection of two judges"), a different sentence about the panel, not about the
tool's MCC; its decisive support is `semi-formal-experiment/REPO_TRAPS.md`:74-76 in any
case.

### Universally quantified prose claims (hypotheses)

| id | impact |
|---|---|
| **H01** | unchanged (contradicted) |
| **H02** | unchanged (verified) |
| **H03** | unchanged (verified) |
| **H04** | unchanged (verified) |
| **H05** | unchanged (verified) |
| **H06** | unchanged (verified) |
| **H07** | unchanged (verified) |
| **H08** | unchanged (unverifiable) |
| **H09** | unchanged (verified) |
| **H10** | unchanged (contradicted) |
| **H11** | unchanged (verified) |
| **H12** | unchanged (verified) |
| **H13** | unchanged (verified) |
| **H14** | unchanged (unverifiable) |
| **H15** | unchanged (verified) |

- **H09** (`∀j. mcc(tool) ≤ mcc(j)`) — **unchanged: verified**, and the only hypothesis
  with a live dependency on the tool's MCC. Its evidence is the benchmark's nine-row
  head-to-head table and the threshold-free table, both regenerated at this pin
  (`**judge wins 9 / 9 cells at its own operating point.**`, re-run line 163 of the
  output). Note the direction: striking the tool's headline numbers cannot *help* the
  tool, so the hypothesis is if anything more secure under the assumption. Dependency:
  live `benchmark.py --tool` §"Head-to-head" and §"Threshold-free".

### Verdict statements

| id | impact |
|---|---|
| **V01** | unchanged (contested) |
| **V02** | unchanged (unverifiable) |
| **V03** | unchanged (unverifiable) |
| **V04** | unchanged (verified) |
| **V05** | unchanged (contested) |
| **V06** | unchanged (contested) |
| **V07** | unchanged (contradicted) |
| **V08** | unchanged (verified) |
| **V09** | unchanged (verified) |
| **V10** | unchanged (verified) |
| **V11** | unchanged (verified) |
| **V12** | unchanged (contested) |

- **V04** ("did not beat a single frontier judge") — **unchanged: verified.** Its needs
  are Q12, Q14, Q15 and the per-judge values, all of which resolve to the live
  `benchmark.py` run, not to HANDOFF.md. No need becomes dangling. Under the strict
  reading in which the tool's MCC is unmeasured, need 1 (tool MCC) would dangle and V04
  would drop to *unverifiable* — but that reading is refuted by the re-derivation, so
  V04 stays verified. Dependency: live `benchmark.py --tool`, §"Head-to-head" (9 rows).
- **V11** ("did not survive their own review process") — **unchanged: verified.** One
  of its four legs is the arc-1 relevance benchmark's own verdict column ("below bar"
  on the true universe), which is the scorer's output, not HANDOFF prose.

### Author commitments (no state assigned)

| id | impact |
|---|---|
| **C01** | unchanged in substance; one new named hole (below) |
| **C02** | unchanged in substance; one new named hole (below) |
| **C03** | unchanged |
| **C04** | unchanged |
| **C05** | unchanged |
| **C07** | unchanged |

- **C01** ("the complete record … the discipline that kept the measurements honest") —
  the substance is unchanged, but the assumption adds a third hole to the two REPORT.md
  named (Q01 denominators, Q02 panel agreement): a fabricated quantitative sentence
  inside a starred handoff block would be exactly the failure of measurement discipline
  the commitment claims against. Mitigating, and worth stating plainly: the record's
  own structure catches it. `HANDOFF.md`:500 carries a do-not-quote list, `benchmark.py`
  regenerates the figures from committed data, and `test_quality_floor.py` pins them as
  test floors — so the prose is checkable against the artifact rather than load-bearing.
  Evidence path for the dependency: `semi-formal-experiment/benchmark.py`,
  `semi-formal-experiment/test_quality_floor.py`:64-79.
- **C02** ("full commit history published unrewritten so that every dated claim, pin,
  and withdrawal is externally checkable") — unchanged, and this is the commitment the
  counterfactual most directly tests. It is borne out in the relevant sense: the
  fabrication would be *externally checkable* from the published record alone, because
  the numbers re-derive in ~5 s from committed inputs. Evidence path:
  `git log` at the pin plus the re-derivation command below.

**Changed claim ids: none.** Old and new states are identical for all 77 stated claims
(Q01–Q50, H01–H15, V01–V12); the six commitments carry no state and are unchanged in
substance, with the C01/C02 annotations above.

---

## Re-derivation

**Question:** can +0.320 (in-sample @ 0.18) and +0.278 (label-free) be independently
re-derived from committed artifacts or scripts at the pin, read-only, no network?

**Answer: yes, twice over — once by the README's own command, once by a direct
recomputation through the committed modules. Neither path reads `HANDOFF.md`.**

### (a) The README's own command reprints both numbers

```
$ cd semi-formal-experiment
$ .venv/bin/python benchmark.py --tool --annotations annotations_b8.json \
      --behaviour-atoms behavior_atoms_b8.json
exit 0    real 11.98 s   user 11.85 s   sys 0.06 s
```

Both figures appear in the output, on the true 589-passage universe:

- **+0.320** — disclosure note 5: *"every thresholded number here is a
  HINDSIGHT-THRESHOLD number and the in-sample mean MCC (+0.274 published / **+0.320
  true**) is a CEILING, not a result."* The full threshold curve prints the components
  at threshold 0.18: helpfulness **+0.262**, harm-avoidance **+0.444**,
  avoiding-over-and-under-caution **+0.253** → mean **+0.3197 ≈ +0.320**.
- **+0.278** — §"Universe delta", mean row:
  `| **mean** | | **+0.278** | +0.219 | +0.059 | **+0.555** | +0.394 | … |`
  with components **+0.201 / +0.350 / +0.283**, each on `589` passages
  (`| helpfulness | 589 / 377 | **+0.201** | …`).

### (b) Direct recomputation through the committed modules

Read-only script (in scratchpad, nothing written into the repo), importing the pinned
`benchmark.py` and `relevance.py` and reproducing exactly the two code paths those
modules ship:

```python
import benchmark as B, relevance
rows, _ = B.load_clauses()
idx   = relevance.RelevanceIndex(rows, relevance.load_annotations("annotations_b8.json"))
panel = B.load_true_panel(spec_keys=("openai",))        # THE TRUE UNIVERSE (589)
behs  = relevance.behaviours_from_panel(panel, "behavior_atoms_b8.json")
label_free = B.evaluate(panel[slug], idx.predict(b), rows)["tool_mcc_mean_full"]
fitted     = B.evaluate(panel[slug], idx.predict(b, relevance.DEFAULT_THRESHOLD),
                        rows)["tool_mcc_mean_full"]
```

```
$ cd semi-formal-experiment
$ .venv/bin/python <scratchpad>/baseline_probe2_rederive.py
DEFAULT_THRESHOLD = 0.18
  label-free  avoiding-over-and-under-caution          +0.2826
  label-free  harm-avoidance-to-third-parties          +0.3502
  label-free  helpfulness                              +0.2007
  label-free MEAN     +0.2778
  @0.18       avoiding-over-and-under-caution          +0.2533
  @0.18       harm-avoidance-to-third-parties          +0.4439
  @0.18       helpfulness                              +0.2618
  @0.18 in-sample MEAN +0.3197
real 4.64 s   user 4.59 s   sys 0.02 s
```

**Result: +0.2778 → +0.278 label-free, and +0.3197 → +0.320 in-sample at
`relevance.DEFAULT_THRESHOLD = 0.18`.** Both match the assumed-fabricated numbers to
the precision the README and HANDOFF state them at. Total re-derivation wall clock:
**16.6 s** across both paths.

### Third, independent corroborator (no run required)

`semi-formal-experiment/test_quality_floor.py`:69-71 records the same two triples as
committed source comments, one for each path:

> "Measured label-free: helpfulness +0.2007, harm-avoidance +0.3502, over/under
> +0.2826. Old numbers, fitted path: over/under +0.2533, harm-avoidance +0.4439,
> helpfulness +0.2618."

Means: +0.2778 and +0.3197. These are in a *test* file whose floors are asserted
against `_measure_bag`/`_panel` (`load_true_panel`), so they are guarded by the
committed suite, not merely written down. This artifact alone, without any run, would
carry Q12 and Q13.

### No network, read-only, provenance of the universe

Both runs are on the demo path REPORT.md audited under `sys.addaudithook` (Q46: zero
socket/urllib events). Nothing in the repository was modified; the only writes were to
the scratchpad. The 589 denominator is the benchmark's own reconstruction, printed as
*"The panel graded EVERY passage of the spec in one prompt: 589 for the model spec"*
and confirmed per behaviour in the Universe-delta table (`589 / 377`, `589 / 333`,
`589 / 153`).

### Nothing is missing

There is no gap to report: inputs (`annotations_b8.json`, `behavior_atoms_b8.json`,
`data/behaviours.json`, the clause inventory), the scorer (`benchmark.py`), the
predictor (`relevance.py`, `DEFAULT_THRESHOLD = 0.18`, `thresholds_frozen.json` for
the label-free Otsu cuts) and a committed regression guard
(`test_quality_floor.py`) are all present at the pin. The one environmental
dependency — a working Python for `.venv` — is machine state, and at this run it works
as written.

**Bottom line.** The assumption "those numbers were never measured" cannot be sustained
against the record: the record measures them, reproducibly, in seconds, from committed
data. The fabrication can only be located in the *prose*, and the prose was never the
authoritative source. Zero claims change state.
