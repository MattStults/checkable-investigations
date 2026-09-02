<!-- Source extraction for the glossary. Extractor: general-purpose subagent, model opus, read-only over the target record, README.md excluded by instruction; deterministic scripts run read-only with wall-clock noted. Committed untouched. -->

I have everything. Writing the report.

# arc-1 record: definitions, artifacts, denominators, variants

All paths relative to `~/Documents/ai_safety_projects/semi-formal-document-analysis/`. `SFE/` = `semi-formal-experiment/`. Every quote is verbatim.

---

## 0. Which HANDOFF block is current; what is self-marked stale

`SFE/HANDOFF.md` is 1,502 lines and organised as a stack of dated star-blocks, newest first.

**The starred current block** — `SFE/HANDOFF.md:3`:
> `## ⭐⭐⭐⭐ STATE AS OF 2026-08-06 — THE GOAL IS RESTATED. READ THIS BEFORE ANYTHING ELSE.`

It carries a **higher-starred nested banner** at `SFE/HANDOFF.md:5`, which is the only ⭐⭐⭐⭐⭐ marker in the file:
> `> **⭐⭐⭐⭐⭐ 2026-08-18 — SECOND-DOCUMENT GATE ARTIFACT.** Before translating / > ANY new document, read and implement / > \`walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/behavior_pilot/TRANSLATION_CONTRACT_V2.md\``

So the file contains **two competing "read this first" claims** and does not resolve which outranks the other; the ⭐⭐⭐⭐⭐ item is nested inside the ⭐⭐⭐⭐ block but is dated 12 days later.

Lower blocks, each also claiming primacy:
- `SFE/HANDOFF.md:99` — `## ⭐⭐⭐ STATE AS OF 2026-08-05 — S3b and S4 build-ready. READ THIS FIRST.`
- `SFE/HANDOFF.md:131` — `## ⭐⭐ STATE AS OF 2026-08-04 LATE — the fix ladder in execution. READ THIS FIRST.`
- `SFE/HANDOFF.md:955` — `## ⭐ THE CENTRAL QUESTION IS ANSWERED: the signal is a DOCUMENT property, not judge idiosyncrasy`
- `SFE/HANDOFF.md:1142` — `## ⭐ THE SCOPE DECISION — everything else in this file is input to it`

**Self-marked stale / superseded / retracted sections** (path:line):

| line | marker text |
|---|---|
| `SFE/HANDOFF.md:119` | `⚠️ **CORRECTED 2026-08-05.** This paragraph previously named \`backfill_author.md\` "for the attribution seat"… Both were wrong.` |
| `SFE/HANDOFF.md:224` | `⛔ \`SECTION_PRIOR_DESIGN.md\` §5 says "cycle-4 config if cycle 5 reverts"; that parenthetical is **STALE and wrong**` |
| `SFE/HANDOFF.md:290` | `## STATE AS OF 2026-08-04 (earlier) — the iteration-loop arc, when the portfolio was designs-only.` … `Everything below this section is history` |
| `SFE/HANDOFF.md:469` | `> ## ⛔ READ FIRST — EVERY PREVIOUSLY PUBLISHED NUMBER IN THIS FILE IS WRONG` |
| `SFE/HANDOFF.md:535` | `**⇒ ⛔ SUPERSEDED 2026-08-04: \`LADDER_PLAN.md\` is no longer the plan of record.**` |
| `SFE/HANDOFF.md:586` | `## The floors — see the banner; the table that was here is superseded` |
| `SFE/HANDOFF.md:621` | `## THE STRUCTURAL RESULT — the earlier NULL WAS WRONG. Retracted.` |
| `SFE/HANDOFF.md:705` | `## ⛔ THE DIAGNOSIS WAS WRONG. IT IS THE QUERY MECHANISM. DO NOT BUY ANNOTATION.` |
| `SFE/HANDOFF.md:1097` | `> **⛔⛔ THIS SECTION IS RETRACTED. Read the retraction 84 lines below` |
| `SFE/HANDOFF.md:1188` | `## ⛔⛔ RETRACTED: "THE COMPLIANT MODULE IS WORSE". It was an \`act_match\` artifact.` |
| `SFE/HANDOFF.md:1259` | `> **⚠️ FLAGGED UNRECONCILED (2026-08-04).**` |
| `SFE/HANDOFF.md:1280` | `> ⚠️ Count superseded 2026-08-04: the suite is now ~1,960 tests` |
| `SFE/HANDOFF.md:1352` | `## ~~THE RESULT (2026-08-01, first version)~~ — DELETED, IT WAS ALL BUG ARTIFACT` |
| `SFE/HANDOFF.md:1363` | `> ⚠️ SUPERSEDED AGAIN 2026-08-04: b8 superseded the originals; the ext_v1 line has now superseded b8.` |
| `SFE/HANDOFF.md:1374` | `### ⚠️ Every ablation number recorded before 2026-08-01 12:18 is void` |
| `SFE/HANDOFF.md:1380` | `### ~~Current headline~~ — DELETED (published universe, superseded)` |
| `SFE/HANDOFF.md:1388` | `### ⚠️ The \`section_path\` fix was a CALIBRATION fix, not a recovery` |
| `SFE/HANDOFF.md:1420` | `### (deleted) "the section signal is unexploited"` |
| `SFE/HANDOFF.md:1431` | `> ⚠️ STALE (2026-08-04): this section describes the 2026-08-02 state.` |

The file states its own deletion policy at `SFE/HANDOFF.md:1357`:
> `- **A superseded number left in a doc is an instruction, not a footnote.** Delete it.`

…which the file then does **not** follow in the ⛔⛔-retracted sections it explicitly keeps (`SFE/HANDOFF.md:1101`: `The section is kept because the measurement discipline in it is sound and worth reading`).

---

## 1. MCC

### Definition (verbatim, authoritative)

`SFE/benchmark.py:661-674`:
```
def mcc(predicted, gold, universe) -> float:
    """Matthews correlation coefficient — THE PRIMARY METRIC.

    F1 is unquotable on this task: it ignores true negatives, so at a 24-47%
    positive rate the degenerate all-relevant predictor scores 0.44-0.64 and on
    `avoiding-over-and-under-caution` a CONSTANT beats the best single judge.
    Every F1 therefore has to be read against a floor that moves per behaviour.

    MCC is 0 BY CONSTRUCTION for both degenerate predictors (all-positive gives
    tn = fn = 0; all-negative gives tp = fp = 0), so its floor is 0 everywhere
    and a number can be read directly. It is also sensitive to true negatives,
    which is deliberate: if the invisible-clause selection effect is ever fixed
    by adding real negatives back, MCC will refuse to keep looking good.
    """
```
Implementation `SFE/benchmark.py:675-684` — standard `(tp·tn − fp·fn)/√((tp+fp)(tp+fn)(tn+fp)(tn+fn))`, returning `0.0` when the denominator is `<= 0`.

The record **contradicts itself on whether MCC is the metric at all.** `SFE/HANDOFF.md:61` (current ⭐⭐⭐⭐ block):
> `2. **The metric is the accounted-for fraction, with (c) as the residual — NOT MCC.** It cannot be fitted: the only way to move it is a fact that survives replay.`

versus `SFE/HANDOFF.md:592`:
> `### Use MCC as the primary metric`

Both stand; the record does not reconcile them.

Also self-contradicting on MCC's robustness — `SFE/HANDOFF.md:488`:
> `> * **"MCC is robust to true negatives, so it is safe here."** False as applied — the true />   negatives had been deleted upstream.`

against `SFE/benchmark.py:671`: `It is also sensitive to true negatives, which is deliberate`.

### Authoritative artifact for the value
`SFE/benchmark.py` (report generator), reading `data/behaviours.json` via `SFE/benchmark.py:78` (`PANEL = os.path.join(HERE, "..", "data", "behaviours.json")`) and reconstructing the universe through `SFE/panel_universe.py`. Snapshot-era numbers come from `SFE/snapshots/*.json` via `SFE/snapshot.py`.

### Denominator / population
Passages, not clauses. TRUE universe = **589** model-spec passages / **374** constitution passages. Published universe = 377 / 333 / 153 (per behaviour, model spec). See §2.

Gold construction, `SFE/benchmark.py:524-526`:
```
#   * judge j predicts RELEVANT iff its label is `core` OR `related` (>= 1);
#     core-only does NOT reproduce the numbers;
#   * gold for j = BOTH other judges predict relevant (not "either");
```

### Every distinct tool MCC with its threshold rule

| value | rule / config | source |
|---|---|---|
| **+0.274** | tool @0.18 (in-sample), **published** universe, mean of 3 | `SFE/HANDOFF.md:480` |
| **+0.320** | tool @0.18 (in-sample), **TRUE 589** universe | `SFE/HANDOFF.md:480` |
| **+0.219** | tool, published universe, mean (re-run today, b8 config) | benchmark run, §11 |
| **+0.278** | tool, TRUE universe, mean (re-run today, b8 config) | benchmark run, §11 |
| **+0.206** | shipped tool, **held-out (LOBO) threshold** | `SFE/HANDOFF.md:754` |
| **+0.396** | shipped tool, **oracle threshold (generous)** | `SFE/HANDOFF.md:755` |
| **+0.278** | **label-free** tool | `SFE/HANDOFF.md:44`, `:777` |
| **+0.268 ± 0.007** | Otsu label-free, stable across all 5 atom draws | `SFE/HANDOFF.md:829` |
| **+0.293** | anchor = exact IDF (semantic-arm baseline) | `SFE/HANDOFF.md:792` |
| **+0.309** | **Dev MCC** (headline ext_v1 config, 3 DEV behaviours) | `SFE/HANDOFF.md:359` |
| **+0.310** | `structural.act_match`, **3 behaviours** (fitted) | `SFE/HANDOFF.md:1046` |
| **+0.246** | `structural.act_match`, **9 behaviours** | `SFE/HANDOFF.md:1046` |
| **+0.294 / +0.274** | `any_atom` no-choice baseline, 3 / 9 behaviours | `SFE/HANDOFF.md:1047` |
| **+0.277 / +0.284** | bag scorer (`relevance`, label-free), 3 / 9 behaviours | `SFE/HANDOFF.md:1048` |
| **+0.316** | **best COMPLIANT config** — `combined` V1@any | `SFE/HANDOFF.md:1066`, `:1150` |
| **+0.284** | **best VIOLATING config** — `relevance` bag | `SFE/HANDOFF.md:1151` |
| **+0.259** | combined PRE-REGISTERED PRIMARY (with rung gate) | `SFE/HANDOFF.md:1070` |
| **+0.198** | section alone (elect & distribute) | `SFE/HANDOFF.md:1072` |
| **+0.145** | intersection | `SFE/HANDOFF.md:1073` |
| **+0.185** | lexical control | `SFE/HANDOFF.md:1116`, `:1152` |
| **+0.243** | size-matched random subset control | `SFE/HANDOFF.md:1081` |
| **+0.2406** | random **whole sections**, size-matched | `SFE/HANDOFF.md:1233` |
| **+0.3085 / +0.3066** | `section@any_atom`, frontier-3 / held-out-6 | `SFE/HANDOFF.md:1257` |
| **+0.226 / +0.254** | semantic arm A (LSA) / arm B (embeddings) | `SFE/HANDOFF.md:796-797` |
| **+0.339 / +0.338 / +0.317 / +0.264 / +0.272** | ablation: full / −lex / −section / −atom / lex-only | `SFE/HANDOFF.md:1402-1406` |
| **+0.2637 → +0.2743** | best over sweep, pre- / post- `section_path` fix | `SFE/HANDOFF.md:1390` |
| **+0.1635 → +0.1867** | LOBO pre-fix / post-fix (published universe) | benchmark preamble item 6 |
| **+0.1526** | "the real pre-fix default" | benchmark preamble item 6 |
| **0.000 / −0.035 / −0.059** | FLOOR A (chance) / FLOOR B variants | `SFE/HANDOFF.md:588-590`, `:1117` |

**Supervised ceilings (not the tool):** text +0.398, atoms +0.435, section alone +0.536, atoms+section **+0.591**, text+atoms+section +0.606 (`SFE/HANDOFF.md:716-720`); in-cell +0.583, cross-judge **+0.404**, LOBO +0.241 (`SFE/HANDOFF.md:968-971`); 9-behaviour panel in-cell +0.644, cross-judge +0.437 (`SFE/HANDOFF.md:977`); memorisation control +0.511 (`SFE/HANDOFF.md:982`); atom-index injectivity bound **+0.972**, act-atoms +0.743, section +0.657 (`SFE/HANDOFF.md:735-736`).

**Oracle variants:** oracle section election then distribute **+0.641**; best label-free section ranking at an **oracle** cut +0.408 (`SFE/HANDOFF.md:843`, `:846`).

**Recorded conflict on `act_match`:** `SFE/HANDOFF.md:1046` gives `+0.310 → +0.246` under n=9, while `SFE/structural.py:323` still records the gate at `+0.340` and marks it `GATE SUSPENDED: +0.340 is DRAW0, the MAXIMUM of a 5-draw spread (mean +0.310 +/- 0.021)`. Both stand.

### Every judge MCC value

**Mean and best:**
- `SFE/HANDOFF.md:481` — `| judges (mean of 3) | +0.394 | **+0.555** |` (published | TRUE)
- `SFE/HANDOFF.md:722` — `| judges (best per behaviour) | +0.654 | — |`
- `SFE/HANDOFF.md:1149` — `| frontier-judge bar (**the stated goal**) | **+0.555 mean / +0.654 best-per-cell** |`
- `SFE/HANDOFF.md:772` — `Report **per-behaviour best judge, per cell** (0.706 / 0.705 / 0.552, mean +0.654).`
- `SFE/HANDOFF.md:1118` — `| small-model judges | +0.514 | (inflated ~+0.09) |`
- `SFE/HANDOFF.md:943` — small-model judges on the export's own citation list: **−0.221** mean vs **+0.525** on the true universe, "a delta of 0.746".

**Per-judge (published universe), `SFE/HANDOFF.md:594-595`:**
> `judge ranking is unchanged under it (helpfulness: kimi 0.659, fable 0.648, **sol −0.027** = chance, which F1's 0.240 precision hides).`

**Per-judge corrections on the true universe:**
- `SFE/HANDOFF.md:491` — `helpfulness MCC **−0.027 → +0.308**` (sol)
- `SFE/HANDOFF.md:493` — `\`kimi-k2\` MCC is **+0.552**`
- `SFE/benchmark.py:731` — `cell: on the true universe kimi-k2's MCC is +0.552.`

**Per-judge, all 9 cells, TRUE universe (today's re-run, b8 config)** — head-to-head table:

| behaviour | gold = | vs judge | tool MCC | judge MCC |
|---|---|---|---:|---:|
| helpfulness | kimi+sol | fable | +0.172 | **+0.697** |
| helpfulness | fable+sol | kimi | +0.223 | **+0.706** |
| helpfulness | fable+kimi | sol | +0.207 | **+0.308** |
| harm-avoidance | opus+sol | kimi | +0.359 | **+0.705** |
| harm-avoidance | kimi+sol | opus | +0.316 | **+0.677** |
| harm-avoidance | kimi+opus | sol | +0.375 | **+0.464** |
| over/under-caution | kimi-k2+sol | fable | +0.276 | **+0.535** |
| over/under-caution | fable+sol | kimi-k2 | +0.296 | **+0.552** |
| over/under-caution | fable+kimi-k2 | sol | +0.276 | **+0.354** |

Per-behaviour judge means, TRUE / published: helpfulness +0.571 / +0.426; harm-avoidance +0.615 / +0.434; over/under +0.481 / +0.321; **mean +0.555 / +0.394** (benchmark universe-delta table, §11).

### "leave-one-out" — the phrase, wherever it exists

The exact hyphenated string **does not appear in HANDOFF.md**; it appears in `SFE/benchmark.py:25`:
> `2. The bar is the PANEL'S OWN AGREEMENT, and specifically its leave-one-out`
> `   number — one judge predicting the other two's consensus. That is what`
> `   "just ask a frontier model" actually buys you. The 3-judge consensus is a`
> `   committee and is not the thing we are competing with.`

Machine form at `SFE/benchmark.py:258-260`:
> `` `leave_one_out[t][j]` judge j scored against the CONSENSUS of the other``
> `                        two (both of them at threshold t). This is the real`
> `                        bar: it is what one frontier model gets you.`

Abbreviated **LOO** values:
- `SFE/HANDOFF.md:603` — `compare to judges' **mean LOO** (0.636/0.697/0.419)` — these are **F1**, not MCC.
- `SFE/HANDOFF.md:930` — `Applying the export's \`score >= 2\` rule to the frontier panel moves judge LOO **+0.631 -> +0.720**` — MCC.
- `SFE/benchmark.py:528` — `#   * bar = max over j, "mean LOO" = mean over j.`

**LOBO** (leave-one-*behaviour*-out) is a distinct thing: tool +0.206 (`SFE/HANDOFF.md:754`), supervised +0.241 (`:971`), and refused as a point estimate — `SFE/HANDOFF.md:602`/benchmark preamble item 5: *"The leave-one-behaviour-out POINT ESTIMATE is not reportable: at n=3 its 95% CI is [-0.055, +0.466] and contains zero"*.

---

## 2. Universe — published vs true

### Definition (verbatim)

`SFE/HANDOFF.md:469-486`:
> `> ## ⛔ READ FIRST — EVERY PREVIOUSLY PUBLISHED NUMBER IN THIS FILE IS WRONG`
> `>`
> `> The panel did **not** score a candidate list. \`engine/panel/whole_doc.py\` put the`
> `> **entire spec in one prompt as 589 numbered passages** and required a verdict for every`
> `> one. \`build_site_data.py:40 keeps_citation()\` then **dropped every passage scoring 0** —`
> `> **212 / 256 / 436** per behaviour (36% / 43% / 74%). Those passages are gold-negative`
> `> **and correctly predicted negative by every judge**, so deleting them stripped`
> `> true-negative credit the judges had earned.`
> …
> `> **The gap was understated by ~2×.** Reconstructed by \`panel_universe.py\`, join rate`
> `> **1.000** on all six (behaviour × spec) cells.`

Authoritative artifact: **`SFE/panel_universe.py`** (`SFE/MODULE_MAP.md:61` — `the TRUE 589-passage evaluation universe. Join rate 1.000 on all six cells. **Every pre-existing number was computed on a truncated universe and is wrong in the tool's favour.**`). It rebuilds from `harness.passages(spec)` — `SFE/panel_universe.py:45-47`: *"The passage list comes from the same function the panel used — `harness.passages(spec)`, imported by path exactly as `whole_doc.py` imports it — so the reconstruction cannot drift from what was prompted."*

### Passage counts

| | model-spec (openai) | constitution (anthropic) |
|---|---:|---:|
| TRUE universe | **589** | **374** |
| published, helpfulness | 377 | 197 |
| published, harm-avoidance-to-third-parties | 333 | 199 |
| published, avoiding-over-and-under-caution | 153 | 77 |
| recovered as 0, helpfulness | 212 (36%) | 177 (47%) |
| recovered as 0, harm-avoidance | 256 (43%) | 175 (47%) |
| recovered as 0, over/under | 436 (74%) | 297 (79%) |
| join rate | 1.000 on all six cells | 1.000 |

(Reproduced live today — benchmark "Judged universe — reconstruction provenance" table, §11. `unjoined published passages: **0**`.) Published total across the three model-spec behaviours = **863**, which is `measure_join.py`'s denominator (§3).

### What was deleted and why

`build_site_data.keeps_citation()` dropped every passage whose **summed** score was 0. Deletion consequences, verbatim `SFE/HANDOFF.md:487-501`:
> `> Four claims repeated throughout this project are ARTIFACTS of that deletion:`
> `> * **"MCC is robust to true negatives, so it is safe here."** False as applied…`
> `> * **"\`sol\` is degenerate / near chance."** It is a *low-threshold* judge: helpfulness MCC **−0.027 → +0.308**.`
> `> * **"over/under-caution is UNUSABLE for a headline."** On the true universe it is the **strongest** behaviour by AUC (0.90). \`kimi-k2\` MCC is **+0.552**.`
> `> * **The selection-effect caveat** (\`unliftable_frac\` 22% / 14% / 56%) described the broken universe; on the true one it is **2% / 1% / 2%**.`
> …
> `> Anything below quoting 377/333/153, 863 passages, 0.764/0.780/0.500, +0.274, +0.187, or`
> `> the over/under refusal is a published-universe number and must be re-derived.`

Restoration is worth `+0.046 mean MCC to the tool and **+0.161 to the judges**, widening the gap 0.120 -> 0.235` (benchmark preamble item 1) — note this conflicts with `SFE/HANDOFF.md:482`'s `| **tool → judge gap** | 0.119 | **0.236** |` at the third decimal; both stand.

### The *second*, worse truncation (panel v2 / 9-behaviour)

`SFE/HANDOFF.md:908-912`:
> `2. **THE UNIVERSE IS TRUNCATED, WORSE THAN BEFORE.** Score distribution is`
> `   \`{2:1309, 3:1145, 4:741, 5:583, 6:536}\` — **no 0 AND no 1**, where \`behaviours.json\` at`
> `   least kept score 1. Reconstruct via \`panel_universe\` and restore absent passages as`
> `   all-zero. **Score-1 passages are IRRECOVERABLE** — real "tangentially related" judgements`
> `   now indistinguishable from "not related". State that limitation with any number.`

Effect, `SFE/HANDOFF.md:927`: `**⚠️ THE SCORE-1 TRUNCATION INFLATES THE JUDGES BY ~+0.089 MCC.**` — `6,867 recovered rows` restored (`SFE/HANDOFF.md:923`).

---

## 3. Join rate / recall ceiling (`measure_join.py`)

### Definition (verbatim)

`SFE/measure_join.py:1-9`:
```
"""How many panel passages join to a clause? The ceiling on every benchmark number.

A passage that matches no clause is neither a hit nor a miss — it is invisible
to the tool, so it caps recall regardless of how good the tool gets. This
reports that ceiling directly, overall and on the high-consensus subset that
the headline F1 is computed over.

    python3 measure_join.py
"""
```

### Numerator / denominator

- **Numerator** = passages for which `bool(inventory.match_passage(p["quote"], rows))` is true (`SFE/measure_join.py:74`).
- **Denominator** = `panel_passages()` — every `(behaviour, passage)` triple from `data/behaviours.json`'s `coverage["openai"]["passages"]` (`SFE/measure_join.py:33-47`), i.e. **863**, the *published* universe. `clause_rows()` supplies 593 clauses from `modelspec_clauses.json` with `marked_span=None` (`SFE/measure_join.py:22-28`).
- Strata: `all`, per-behaviour, `score >= 5`, `score == 6`, `example blocks` (`SFE/measure_join.py:63-77`).

The denominator is therefore **the broken one**: `measure_join.py` never uses `panel_universe.py`. This is the source of the anti-quote rule below.

### "Misses printed by name"

`SFE/measure_join.py:81-84`:
```
    print(f"\nunmatched ({len(unmatched)}):")
    for p in unmatched[:10]:
        print(f"  [{p['behaviour']} s={p['score']}] {p['quote'][:100]!r}")
```
The count is honest (`unmatched (14)`) but **only the first 10 are printed, each truncated to 100 characters** — so "printed by name" means *quote-prefix*, not id or locator, and 4 of 14 are never shown. The record does not disclose this truncation anywhere I found.

### The anti-rule text

The record's own warning about the join figure is **in §1, not §11** — `SFE/MODULE_MAP.md:54`:
> `| \`measure_join.py\` | 93 | ⚠️ the recall ceiling. **Do not quote 849/863** — that is the published-universe figure, and the published universe deleted every passage the panel scored 0. Re-run it; never cite the number from this table. |`

**§11 contains no anti-rule about the join *rate*.** The nearest §11 entry concerns join *identity*, `SFE/MODULE_MAP.md:316`:
> `| \`--mixed-variants\` under \`--join-version 1\` raises instead of being ignored, and the census header records \`mixed_variants\` as an explicit \`null\`/bool rather than omitting it | The census RECORDS the join it ran; a silently-ignored flag would make that record false. … | "Accepting the flag anywhere" ships a census whose header names a variant set it never used — the same class of defect as the 2026-08-03 plain-index rebuild of an overlay config |`

**The record then violates its own rule twice, in the same file:** `SFE/HANDOFF.md:529` (`the panel join now reaches **849/863 (98.4%)**`) and `SFE/HANDOFF.md:1287` (`the recall ceiling: 849/863 overall, 110/112 at score ≥5, 313/313 example blocks. **Gates every benchmark number**`), plus the table at `SFE/HANDOFF.md:1326-1331`.

### The 14 misses, characterised

`SFE/HANDOFF.md:1333-1337`:
> `The 14 remaining misses are **not paraphrase and not version skew** — our spec copy is`
> `byte-identical to \`../specs/openai-model-spec/model_spec.md\` (sha256 \`8c95f020…\`). The`
> `panel's own renderer rewrote \`[text](url)\` inconsistently, sometimes *within a single*`
> `*passage*, so no one normalization variant matches. A real but small ~1.6% reference-side`
> `ceiling.`

### Run output

**Command** (from `SFE/`): `.venv/bin/python measure_join.py` — **wall clock 9.62 s real / 9.50 user / 0.05 sys**

```
clauses: 593   panel passages: 863

stratum                              matched   total     pct
all                                      849     863   98.4%
  helpfulness                            372     377   98.7%
score >= 5                               110     112   98.2%
score == 6                                58      60   96.7%
example blocks                           313     313  100.0%
  harm-avoidance-to-third-parties        326     333   97.9%
  avoiding-over-and-under-caution        151     153   98.7%

unmatched (14):
  [helpfulness s=6] 'The assistant may sometimes encounter instructions that are ambiguous, inconsistent, or difficult to'
  [helpfulness s=4] 'While the assistant should display big-picture thinking on how to help the user accomplish their lon'
  [helpfulness s=3] 'Inapplicable instructions should typically be ignored. The only other reason an instruction should b'
  [helpfulness s=2] 'If the assistant lacks sufficient confidence in its response, it should use a tool to gather more in'
  [helpfulness s=1] 'As mentioned in #letter_and_spirit, users or developers may sometimes include untrusted text content'
  [harm-avoidance-to-third-parties s=6] 'The assistant must not generate *restricted content* (such as information hazards and sensitive pers'
  [harm-avoidance-to-third-parties s=4] 'If the assistant lacks sufficient confidence in its response, it should use a tool to gather more in'
  [harm-avoidance-to-third-parties s=4] '#prohibited_content: only applies to sexual content involving minors, and transformations of user-pr'
  [harm-avoidance-to-third-parties s=4] 'As mentioned in #letter_and_spirit, users or developers may sometimes include untrusted text content'
  [harm-avoidance-to-third-parties s=3] 'While the assistant should display big-picture thinking on how to help the user accomplish their lon'
```

The re-run **reproduces 849/863 exactly** — i.e. the number MODULE_MAP forbids quoting is the number the tool still emits, unchanged, with no universe warning in its own output.

### Related join facts on the record
- `SFE/HANDOFF.md:1481-1485` — `**The join normalizer needs all four transforms**: whitespace runs, \`[^xxxx]\` footnote markers (25 mid-sentence), markdown emphasis, and *both* renderings of a markdown link. Emphasis stripping alone is worth 313 passages … Dropping any one transform silently lowers every downstream metric.`
- `SFE/HANDOFF.md:615-616` — clauses-per-passage `{0:14, 1:847, 2:2}`, mean 1.002, max 2.
- `SFE/HANDOFF.md:617` — `only 9 of 851 joins rest on a quote under 40 chars.`
- TRUE-universe join residue (benchmark, today): `passages judged 589 | joinable 582 | unjoinable 7`.

---

## 4. Clause inventories, ASP rule counts, recorded corrections

### Clause inventories (measured today)

| artifact | count | schema keys |
|---|---:|---|
| `SFE/modelspec_clauses.json` | **593** clauses | `id, locator, section_path, section_id, quote, kind, in_example_block, focus_ids, line` (+ top-level `spec`, `source_sha256`) |
| `SFE/constitution_clauses.json` | **616** clauses | `id, locator, section_path, quote, kind, modality_hint` (+ `spec`) |
| `SFE/modelspec_focus_areas.json` | **259** focus areas (bare list) | — |

Record's own statements: `SFE/MODULE_MAP.md:218` — `| \`modelspec_clauses.json\` | 496 KB | **live** — 593 clauses, the analysis unit |`; `:227` — `| \`constitution_clauses.json\` | 311 KB | **live for swappability** — 616 clauses, same schema, loads today |`; `SFE/HANDOFF.md:1286` — `**593 clauses**, 97.35% char coverage, 100% verbatim, 0 duplicate locators, 259/259 focus markers preserved as a privileged subset`.

**Recorded internal conflicts on these counts:**
- `SFE/HANDOFF.md:527` says `593 clauses at 97.35% character coverage`, but `SFE/HANDOFF.md:554` says `relevance annotates all 593 clauses` while `SFE/HANDOFF.md:1350` says `annotations over all 593 including examples` — consistent. However `SFE/HANDOFF.md:353` describes the *preferred* annotation as `1,442 atoms over 589 clauses`, and `SFE/annotations_b8.json` covers **587** clauses (`by_clause` n=587). Benchmark reports `clauses visible to the panel: 586`. So four clause counts circulate — 593 (segmentation), 589 (ext_v1 annotation), 587 (b8 annotation), 586 (panel-visible) — and the record never states the relation.
- `SFE/HANDOFF.md:949-950` — `**Constitution clause annotations do not exist** — \`annotations_b8.json\` is 587 clauses, all \`m*\`, zero \`c*\`.` **Confirmed today**: `clause id prefixes: Counter({'m': 587})`.

### ASP fragment — rule counts (measured today)

| file | lines | statements ending `.` | `source(...)` atoms | rules with `:-` |
|---|---:|---:|---:|---:|
| `SFE/machine/facts.lp` | 720 | 585 | **282** | 0 |
| `SFE/machine/rules.lp` | 106 | 53 | — | **27** |
| `SFE/machine/scanned.lp` | 1,939 | 1,929 | **964** | 0 |
| `SFE/machine/semantics.lp` | 81 | 40 | — | **18** |

The record's own count, `SFE/machine/README.md:47`:
> `| \`facts.lp\` | THE MODEL, hand-transcribed. 281 facts, each with a \`source/3\` + \`needle/2\` companion (955 more come from \`scanned.lp\`). |`

**This is a recorded count that is now off by one and by nine respectively**: 282 sourced facts in `facts.lp`, 964 in `scanned.lp`. `check_model.py` reports **282 comparisons** for its differential check, matching the fact count.

Model coverage counts, `SFE/machine/README.md:63-75`: `**Gates** — 20 gates`, `**Seats** — 12 seats (every file in \`briefs/\`)`, `**Constants** — 10`. **All three verified today**: `query.py gates` returns 20; `query.py seats` returns 12; `query.py constants` returns 10.

### Recorded corrections of counts (each explicit)

| what was corrected | correction text | path:line |
|---|---|---|
| test count | `**Test count** "1113 tests (2026-08-02)" → ~1,960 now (README; 1,919 collect under a bare interpreter without the venv).` | `SFE/HANDOFF.md:455` |
| test count again | `The suite is now **2,156 passed / 3 skipped (measured 2026-08-04)**.` | `SFE/MODULE_MAP.md:237` |
| test count policy | `⚠️ **Test counts drift, and every count written into a doc goes stale within days** — this one has already been wrong twice (a "808 passing" line frozen at 2026-08-01 and a "~1,960" line frozen at 2026-08-02 both survived into 2026-08-04). **The command is the source of truth, not any number in this file.**` | `SFE/MODULE_MAP.md:246-250` |
| expert anchors | `**4 core-passage anchors — THREE anthropic-side … plus ONE openai-side**. "Two anchors" was a miscount (PORTFOLIO_REVIEW addendum ruling 1); corrected here 2026-08-04` | `SFE/MODULE_MAP.md:133` — but `SFE/HANDOFF.md:426` still says `Two expert core-passage anchors are reserved` (unfixed conflict) |
| pricing ladder | `**The pricing ladder, corrected 2026-08-04** (an earlier revision of this file stopped at "1.1, the shippable config after cycles 1–3" — that has been false since S1 shipped)` | `SFE/MODULE_MAP.md:97-98` |
| snapshot enumeration | `**Enumerate with \`ls snapshots/\`** — the previous hand-list here undercounted (11 files on disk at 2026-08-04).` | `SFE/MODULE_MAP.md:120` |
| brief count | `d(brief_count,"briefs/README.md says the directory holds 11 briefs as of 2026-08-05","ls briefs/*.md returns 12 — density_editor.md is in the directory and absent from the list")` | `query.py disagreements` |
| accuracy pass | `**Accuracy pass 2026-08-04**: stale counts, the containment pricing ladder, the anchor count and the snapshot/cycle enumerations corrected; §0 added.` | `SFE/MODULE_MAP.md:10-11` |
| chain-audit tally | `**97 correct, 11 agent_missing, 1 unlicensed**` (`SFE/HANDOFF.md:403`) vs `109/109 chain-audit` and `97 correct / 12 repaired` (`cycles/decoration-blind-join-2026-08-04/assignments/review.md:10`) — 11 vs 12 unreconciled |
| suite count post-cycle | `2128 passed / 3 skipped` (review) then `2129 passed, 3 skipped` (justification) in the same `decision.json` | `SFE/cycles/patient-pricing-2026-08-04/decision.json:74`, `:86` |
| cycle dir count | `At 2026-08-04: 7 cycle dirs, 5 of them closed … 2 open (join-integrity-v2, segmentation-variants)` | `SFE/MODULE_MAP.md:121` — **now stale**: `CYCLE_LOG.jsonl` has **6** lines (join-integrity-v2 closed KEEP), so 7 dirs / 6 closed / 1 draft |

---

## 5. Behaviour-gold cells

### What a cell is

Two distinct senses, both in the record and **not distinguished by name**:

**(a) Gold cell = (behaviour × held-out judge).** `SFE/benchmark.py:825-830`:
```
    """`{held-out judge: roc cell}` — the threshold-free head-to-head.

    Each cell carries the tool's AUC over the whole universe, the judge's own
    (FPR, TPR), and the tool's TPR at that FPR. `judge_wins` is the comparison
    that matters and is precomputed so no reader has to eyeball two columns.
    """
```
Count: 3 behaviours × 3 pair-golds = **9 cells** (`SFE/benchmark.py:722` — `On the true 589-passage universe the judge wins 9/9 cells.`). Scaled up: the 9-behaviour panel gives **27 cells** (`SFE/HANDOFF.md:977`).

**(b) Scoring cell = (behaviour × spec).** `SFE/benchmark.py:2390` — `# ------------------------------------------------------ the 18-cell scoring`; `SFE/benchmark.py:2409` — `"""\`evaluate\` for one (behaviour, spec) cell, with the floors it needs.`. Count: **18** (`SFE/HANDOFF.md:888` — `**9 behaviours x 2 specs = 18 cells**`). The 3-behaviour panel gives **6** such cells (`SFE/HANDOFF.md:485` — `join rate **1.000** on all six (behaviour × spec) cells`).

Gold construction (verbatim), `SFE/HANDOFF.md:574-575`:
> `- **Gold for judge *j* = both other judges relevant.** Not "either" — that variant gives`
> `  0.544/0.689/0.640 and matches nothing.`

And the refusal at `SFE/HANDOFF.md:582-584`:
> `Do **not** use consensus \`score ≥5\` as gold: it implies every judge rated ≥1, so gold is a`
> `subset of every judge's positive set and **every judge scores recall 1.0 by construction** —`
> `there is no bar at all on that basis.`

### The "judge's own false-positive rate" comparison

Definition, `SFE/benchmark.py:715-721`:
```
# The threshold-free statement is: a judge is a SINGLE (FPR, TPR) point; the
# tool is a CURVE. Comparing them at the judge's own FPR asks the only fair
# question — "held to the same false-positive rate the judge chose, does the
# tool recall as much?" — and no threshold choice can flatter either side.
# AUC summarises the whole curve alongside it.
```
Headline, `SFE/HANDOFF.md:497-498`:
> `> **Judges beat the tool 9 of 9 cells** at the judge's own false-positive rate. On`
> `> helpfulness the judge gets TPR 0.76–0.79 at FPR ≈0.06 where the tool gets **0.13**.`

Reproduced today (benchmark, b8 config, TRUE universe):

| behaviour | vs judge | tool AUC | judge FPR | judge TPR | tool TPR @ judge FPR | winner |
|---|---|---:|---:|---:|---:|---|
| helpfulness | fable | 0.642 | 0.061 | 0.761 | 0.128 | **judge** |
| helpfulness | kimi | 0.669 | 0.065 | 0.788 | 0.124 | **judge** |
| helpfulness | sol | 0.660 | 0.566 | 0.978 | 0.813 | **judge** |
| harm-avoidance | kimi | 0.779 | 0.065 | 0.753 | 0.304 | **judge** |
| harm-avoidance | opus | 0.762 | 0.135 | 0.875 | 0.522 | **judge** |
| harm-avoidance | sol | 0.795 | 0.397 | 0.967 | 0.805 | **judge** |
| over/under-caution | fable | 0.900 | 0.092 | 1.000 | 0.708 | **judge** |
| over/under-caution | kimi-k2 | 0.764 | 0.000 | 0.333 | 0.000 | **judge** |
| over/under-caution | sol | 0.900 | 0.221 | 1.000 | 0.875 | **judge** |

`**judge wins 9 / 9 cells at its own operating point.**`

Floors attached to every cell — `SFE/benchmark.py:2394-2400`:
```
    """FLOOR B — the degenerate predictor that fires on every JOINABLE passage.

    Floor A is MCC's definitional zero (predict the literal universe: 0.000,
    chance). Floor B is that same do-nothing predictor once the coverage gap is
    imposed on it: it cannot reach a passage no clause joins to. The two are
    different numbers and conflating them is how a coverage cost gets absorbed
    into a headline, so both are printed on every row.
    """
```

---

## 6. Judges — names, count, panel version

Authoritative artifact: **`data/behaviours.json`**, `provenance` block (read today):

```json
"method": "llm-panel whole-document judging",
"rubric": "v3w",
"panel_config": "frontier",
"panel": ["sol (gpt-5.6-sol)", "fable (claude-fable-5)", "kimi (moonshotai/Kimi-K3)"],
"substitution": "opus (claude-opus-4-8) replaces fable on harm-to-third-parties x model-spec (fable output content-filtered, 3 attempts); kimi-k2 (Kimi-K2.6) replaces kimi on over-under-caution x model-spec (K3 exhausted a 65k output budget on reasoning without emitting verdicts, finish_reason length)",
"judges_seen_in_data": ["fable", "kimi", "kimi-k2", "opus", "sol"],
"runDate": "2026-07-30",
"scoring": "per passage: sum over judges of core=2/related=1/neither=0; display thresholds are client-side URL params"
```
`"generatedFrom": ["engine/panel/build_site_data.py (v3w)"]`.

**Count: 3 judges per behaviour, 5 distinct judges across the panel.** Per-behaviour rosters, `SFE/HANDOFF.md:576-578`:
> `- **The judge panels differ per behaviour**: helpfulness = Sol/Kimi-K3/Fable 5;`
> `  harm-avoidance = Sol/Kimi-K3/**Opus 4.8**; over/under-caution = Sol/Fable 5/**Kimi-K2.6**.`
> `  Hardcoding one panel yields 0.000 for the other two and looks like a modelling failure.`

Reinforced in code, `SFE/benchmark.py:38-40`:
> `Judge names are read from the data, never hardcoded: the panel does not use`
> `the same three judges for every behaviour (helpfulness has fable/kimi/sol,`
> `harm-avoidance has kimi/opus/sol, over-under-caution has fable/kimi-k2/sol).`

Scale definition (bar pinning), `SFE/HANDOFF.md:570-573`:
> `- \`role\` free text gives three levels per judge: **core=2, related=1, not relevant=0**;`
> `  the published \`score\` is their sum. Verified 377/377, 333/333, 153/153. A parser that`
> `  doesn't reproduce \`score\` exactly is wrong.`
> `- A judge predicts relevant at **core OR related (≥1)**, not core-only.`

**The second (v2 / small-model) panel is explicitly NOT the bar** — `SFE/HANDOFF.md:903-906`:
> `1. **IT IS A WEAKER PANEL. NEVER QUOTE ITS AGREEMENT AS "THE BAR."** Judges are`
> `   **gpt-mini, haiku, qwen-small** — small models. The goal is "quality equal to or better than`
> `   asking the FRONTIER models", so \`behaviours.json\` (sol/kimi/fable/opus/kimi-k2) remains THE`
> `   BAR. Use this panel for **generalisation and power**, and label it by its roster wherever it`
> `   appears.`

Enforcement: `SFE/HANDOFF.md:945-946` — `\`check_bar_provenance\` is now a standing guard: any document quoting a bar off these behaviours must name the roster and say "small-model panel", or it raises.`

Verdict scale for v2, `SFE/HANDOFF.md:918-920`: `Verdict scale is **2 = relevant, 1 = tangentially related, 0 = not related** (confirmed by the project owner)`. Same line records a retracted claim: `An earlier note here said \`verdicts\` was a string repr — that was wrong, an artifact of a pretty-printer calling \`str()\` on it.`

A third judge tier exists: `data/panel-v5/` — `| Panel v5 | 9 behaviors × 589 passages, externally authored (Apache-2.0) | \`data/panel-v5/runlog-v5.jsonl\` | the untouched replication tier |` (`ARTIFACTS.md:30`).

---

## 7. Cycles

### Definitions (verbatim)

**A cycle** — `SFE/CYCLE_DESIGN.md:3-6`:
> `One fix cycle as a state machine over typed artifacts. The driver runs`
> `mechanical phases itself and halts with a named, templated blank wherever`
> `judgment is required. The operator (LLM or human) is only ever filling typed`
> `blanks — the seats' dossier-in/verdict-out contract lifted to workflow level.`

**Phases**, `SFE/CYCLE_DESIGN.md:24-39`: OPEN → PREDICT → IMPLEMENT GATE → MEASURE → ADJUDICATE → CENSUS → DECIDE → CLOSE.

**A cycle close** — `SFE/CYCLE_DESIGN.md:39`:
> `8. CLOSE — one line appended to \`cycles/CYCLE_LOG.jsonl\`.`

and `SFE/CYCLE_DESIGN.md:255-256`:
> `The driver NEVER runs git. CLOSE drafts \`commit_message.txt\` and \`staging_list.txt\``
> `(= \`files_to_change\` ∪ the cycle dir); the coordinator stages, verifies, and commits.`

`SFE/MODULE_MAP.md:121` — `plus \`CYCLE_LOG.jsonl\`, **one line per CLOSED cycle**. \`ls cycles/\` and \`cycles/CYCLE_LOG.jsonl\` are the source of truth; do not maintain a list here.`

**What records a prediction freeze** — `SFE/CYCLE_DESIGN.md:26-27`:
> `2. PREDICT — \`prediction.json\`: expected_shrink / must_not_grow over the`
> `   closed cause taxonomy; sha-FROZEN on validation, tamper = hard error.`

The sha itself is recorded in `state.json` as `frozen_prediction_sha` (and `frozen_manifest_sha`) — e.g. `SFE/cycles/versioned-cut-2026-08-04/state.json:28-29`:
```
 "frozen_manifest_sha": "fa3e4b250d4dc9d77fd24a94434f620324c6f5e63441216c27e20f1c38811f61",
 "frozen_prediction_sha": "181e7bc7b6dec758c85c0ac5f301b39eb5c17dff74b18b35c2662c459e19f2d9",
```
Gate name in the ASP model: `gate_blocks(g_predict_freeze,predict)` — non-overridable per `SFE/machine/README.md:118` (`PREDICT-freeze, ADJUDICATE-validation and the DECIDE signature are non-overridable (overriding PREDICT *demotes* rather than waives)`).

A `prediction.json` in full (`SFE/cycles/versioned-cut-2026-08-04/prediction.json:1-7`) — note the first-customer defect it records against itself:
```json
{
 "expected_flip_count": {"min": 0, "max": 0},
 "expected_directions": ["newly_predicted", "no_longer_predicted"],
 "expected_clauses": [],
 "max_regressions": 0,
 "notes": "DELIBERATE NO-OP NOW: ... FIELD NOTE / FIRST-CUSTOMER FINDING: expected_directions is intended as NONE — zero flips means no direction can occur — but the driver refuses an empty list ('expected_directions must be a non-empty list'), so a zero-flip prediction cannot express its true direction target. ..."
}
```

**What records an adversarial review** — `review_verdict.json`, schema stated in the driver-written assignment, `SFE/cycles/decoration-blind-join-2026-08-04/assignments/review.md:14-25`:
> `Required output: review_verdict.json in this cycle's directory:`
>
> `    {"verdict": "proceed" | "blocked",`
> `      "by": "<who reviewed — never the implementer>",`
> `      "notes": "<what was verified, or why blocked>"}`
>
> `All three keys are REQUIRED; verdict is a CLOSED set. The driver re-checks`
> `the frozen manifest/prediction shas, the two-sided one-variable check and`
> `the gate tests mechanically; your seat verifies what the machine cannot`
> `(see the brief: freeze shas, declared-diff-only, tests bind — at least one`
> `mutant — and the fence scan). A "blocked" verdict halts the cycle until`
> `resolved and re-reviewed.`

Policy, `SFE/HANDOFF.md:284-286`:
> `Every cycle gets a clean-context adversarial review before its close; **a positive review**`
> `**stops everything until fixed** (this has fired twice: the A2 dossier-license block, and`
> `S1's own disclosed restart).`

The verdict is also copied verbatim into `state.json` under `gate.review` and into `decision.json` under `gate.review` — so it is stored three times.

**What a `decision.json` contains** — closed vocabulary + computed fields. From `SFE/cycles/patient-pricing-2026-08-04/decision.json` (read in full), the top-level keys are:

`adjudication` (with `agreement_on_contested`, `confirmed_regressions`, `contested`, `dossier_set_sha`, `leg_1_official`, `leg_2_verification`, `resolved_not_regression`, `record`), `census`, `census_delta`, `cycle`, `date`, `decision`, `exploratory`, `fix_description`, `flip_tallies`, `flip_verdicts_reused_from`, `gate` (`closure_checked`, `files_changed`, `review`, `tests_passed`), `justification`, `noop`, `overrides`, `prediction_check` (`checks[]` + `pass_rate`), `shape`, `signed_by`.

Its DECIDE gate: `SFE/CYCLE_DESIGN.md:37-38` — `7. DECIDE — drafts \`decision.draft.json\` with every computed field filled and \`decision\`/\`signed_by\` blank; halts for a signed \`decision.json\`.` Signature at `:210`: `"signed_by": "session coordinator (Claude), on Matt's standing authorization for the reviewed portfolio order"`.

Decision rule, `SFE/CYCLE_DESIGN.md:43-48`:
> `Keep/revert is grounded in the DOCUMENT-SIDE evidence: the flip`
> `adjudications (phase 5). The census deltas and prediction check (phase 6) are`
> `MEASUREMENT, reported in the draft so the decision is informed, and gating`
> `only in the refusal direction: a FAILED prediction or an override obliges a`
> `written justification; it never auto-decides. Nothing in the driver keeps a`
> `change because a panel-derived count moved the right way.`

Its own self-flagged tension, `SFE/CYCLE_DESIGN.md:52-60`:
> `The prediction artifact quantifies targets over CENSUS CAUSE CLASSES, which`
> `are panel-derived … Whether that line is drawn correctly — or whether`
> `per-cycle prediction-checking on panel-derived counts is de-facto fitting`
> `with extra steps — is exactly what an adversarial review should attack.`

### Every cycle directory

`SFE/cycles/` — 7 directories + `CYCLE_LOG.jsonl` (6 lines).

| directory | date | `decision.json` | `review_verdict.json` | in CYCLE_LOG | decision | predictions |
|---|---|---|---|---|---|---|
| `versioned-cut-2026-08-04` | 2026-08-04 | ✅ | ✅ | ✅ line 1 | keep | 2/2 |
| `chain-repair-2026-08-04` | 2026-08-04 | ✅ | ✅ | ✅ line 2 | keep | 3/3 |
| `decoration-blind-join-2026-08-04` | 2026-08-04 | ✅ | ✅ | ✅ line 3 | keep | 4/4 |
| `patient-backfill-2026-08-04` | 2026-08-04 | ✅ | ✅ | ✅ line 4 | keep | 3/3 |
| `patient-pricing-2026-08-04` | 2026-08-04 | ✅ | ✅ | ✅ line 5 | **revert** | 19/20 |
| `join-integrity-v2-2026-08-04` | 2026-08-04 | ✅ | ✅ | ✅ line 6 | keep | 3/3 |
| `segmentation-variants-2026-08-04` | 2026-08-04 | ❌ (drafts only: `manifest.draft.json`, `prediction.draft.json`) | ❌ | ❌ | — | — |

`CYCLE_LOG.jsonl` verbatim (6 lines, one per closed cycle) — line 5:
```json
{"census_consulted": false, "census_deltas": null, "cycle": "patient-pricing-2026-08-04", "date": "2026-08-04", "decision": "revert", "exploratory": false, "noop": false, "overrides": [], "prediction_pass_rate": [19, 20], "shape": "code"}
```
Every line records `"census_consulted": false` and `"census_deltas": null`.

**Files each directory contains** (union across cycles): `manifest.json` (+ `.template`/`.draft` variants), `prediction.json` (+ `.template`/`.draft`), `prediction_check.json`, `state.json`, `diff.json`, `review_verdict.json`, `decision.json` (+ `.draft`/`.proposed`), `flip_dossiers/` with `index.jsonl`, `flip_verdicts.json`, `assignments/` (`flips.md`, `review.md`, sometimes `backfill.md`), `snapshot_build/<cycle>.json`, `commit_message.txt`, `staging_list.txt`. Per-cycle extras: `join-integrity-v2` has `measure/` (10 files incl. `superseded_floor25/`); `patient-backfill` has `backfill/` (10 files incl. `APPLY_HALT.md`, `RULINGS.md`, `REVIEW_HARDENING_NOTES.md`); `patient-pricing` has `ADJUDICATION_LEGS.md`, `AMENDED_RECOMPUTATION.md`, `DISCOUNT_DERIVATION.md`, `MECHANISM_AMENDMENT.md`, `M0108_SEAT_DEFECT_REVIEW.md`, `OPEN_RECOMPUTATION.md`, `manifest_amendments.json`, `pre_change/behaviours_query.json`, `flip_verdicts_verification_leg.json`, and 18 named flip dossiers.

**Recorded conflict:** `SFE/MODULE_MAP.md:121` says `At 2026-08-04: 7 cycle dirs, 5 of them closed …, 2 open (join-integrity-v2, segmentation-variants)`. On disk today join-integrity-v2 is **closed** (log line 6), so the count is 6 closed / 1 draft. `SFE/HANDOFF.md:249-250` says the same thing (`Two do right now (join-integrity-v2, segmentation-variants — both P1/P2 drafts, pre-OPEN, not live work)`) and is equally stale.

### One `decision.json` in full

Read in full: `SFE/cycles/patient-pricing-2026-08-04/decision.json` (211 lines). Its load-bearing parts:

- `"decision": "revert"` (`:41`) — the program's only revert.
- `"flip_tallies": {"correct": 12, "regression": 5, "unclear": 1}` (`:44-48`).
- Two adjudication legs (`:14-31`): leg 1 official (all 18 flips, 12/5/1); leg 2 verification (`"seat": "frontier, split-blind to leg 1's verdicts"`, 6 contested flips, 2 correct / 4 regression).
- `"contested": {"m0108": "leg 1 regression / leg 2 correct — final verdict \`unclear\` per the divergence rule; both document reasons preserved verbatim in ADJUDICATION_LEGS.md; flagged for seat-defect review, never silently resolved"}` (`:11`).
- `prediction_check` (`:89-207`): 19 PASS + one FAIL — `{"expected": 0, "kind": "max_regressions", "observed": 5, "result": "FAIL"}` (`:197-202`).
- `justification` (`:86`, ~4,500 words) opening: `"REVERT. THE BOUND IS BREACHED: the frozen prediction (prediction.json sha c99260f0…) pre-registered max_regressions = 0 as this cycle's falsifiable bound."` and closing proof: `"rebuilding the S2 baseline snapshot from the reverted tree yields sha256 8159ba49… — BIT-IDENTICAL to the frozen snapshots/patient-backfill-2026-08-04.json"`.
- The justification also carries the standing prohibition: `"The measure snapshot snapshots/patient-pricing-2026-08-04.json is retained as the immutable record of what was measured (amendment F3); it is a reverted configuration and must never be used as a baseline."`
- `"census": "deferred_to_checkpoint"`, `"census_delta": null` (`:37-38`) — the census never ran.

### One review file in full

`SFE/cycles/versioned-cut-2026-08-04/review_verdict.json` (5 lines, read in full):
```json
{
 "verdict": "proceed",
 "by": "adversarial review seat (agent)",
 "notes": "Verified: (1) frozen manifest/prediction shas match state.json; only snapshot.py, test_snapshot.py, thresholds_frozen.json changed — threshold.py, test_no_reference_leak.py, cycle.py, test_cycle.py byte-untouched per git. (2) thresholds_frozen.json's three cuts EQUAL the baseline snapshot's recorded thresholds exactly (all behaviours covered — full freeze, not partial); its derived_from_snapshot sha256 matches snapshots/baseline-2026-08-04-auditv1.json, rule 'otsu' == threshold.PREFERRED, config matches the baseline's recorded inputs, and the cited escalation (dossiers/baseline-2026-08-03__containment-v1.1-kindinherit/decision.json, m0422) and cut_stability_results.json exist — provenance is label-free (values are the rule's own output; no panel value in the chain). (3) Deliberate no-op reproduced mechanically in an isolated scratch copy: frozen-flag snapshot vs baseline = 0 flips, identical cuts/predicted sets, diff names only 'thresholds' as the changed input. (4) F9 dispatch: no flag -> rule-derived cuts, config inputs.thresholds explicit null, no threshold_source key (old shape); flag -> artifact sha in config identity; no wall-clock, determinism test present and green. (5) Fallback for behaviours absent from the artifact is recorded per behaviour as threshold_source: 'rule_fallback', so a partial freeze is visible in the snapshot itself. (6) Tests bind — mutant checks run by this seat in a scratch copy: mutant A (artifact cut ignored) killed by test_frozen_threshold_artifact_honored + test_cli_thresholds_flag (the honored test also asserts artifact value != rule value, so it cannot green with the flag ignored); mutant B (frozen artifact silently made default) killed by test_old_behavior_reachable_without_thresholds_flag + test_thresholds_sha_recorded_and_null_when_absent. (7) Fence: FORBIDDEN scan of snapshot.py and thresholds_frozen.json, raw and comment/docstring-stripped — zero hits; nothing reads a panel file. All three gate test files pass (103 passed). No files modified by this review other than this verdict."
}
```

Note the mutant discipline here predates the record's own warning at `SFE/HANDOFF.md:504-520` (`## ⚠️ MUTATION TESTING IN THIS REPO CAN LIE TO YOU — clear the bytecode cache` … `Every "# MUTATION-VERIFIED" marker in this repo predates this discovery.`). This review says "in a scratch copy" but does not say the cache was cleared; the later patient-pricing review does (`pycache cleared, mutant presence grep-asserted each time`, `decision.json:74`).

---

## 8. Seats, validators, "NO VALIDATOR" vs "(none recorded)"

### Definition

`SFE/REPRODUCIBILITY.md:38-41` (the sandwich rule):
> `The LLM is always sandwiched: deterministic producer → LLM under written`
> `instructions → deterministic validator. A step where the model's output flows`
> `onward unvalidated, or whose instructions exist only in a session log, is a`
> `reproducibility bug even if it worked once.`

`SFE/MODULE_MAP.md:270-273`:
> `REPRODUCIBILITY.md's sandwich rule: every LLM/human judgment seat runs under a`
> `versioned brief in the repo, between a deterministic producer and a mechanical`
> `validator. Seats are Haiku-operable by default (a small/frontier divergence is`
> `diagnosed as a seat defect first); three ⚠️ seats are explicitly frontier/human.`

`SFE/machine/README.md:66-70`:
> `* **Seats** — 12 seats (every file in \`briefs/\`): brief path, model tier`
> `  (haiku / frontier / human — a seat may carry two when the repo says`
> `  "a human, or a frontier model"), producer, validator, the phase it is used`
> `  at, and its **scaling unit**: \`per_flip\`, \`per_cycle\`, \`per_document\`,`
> `  \`per_dossier\`, \`per_worksheet_row\`, \`per_behaviour\`, \`per_corpus\`.`

### The two absence markers — they are semantically different

`SFE/machine/query.py:90-91`:
```python
        v = ", ".join(V.get(seat, [])) or (
            "*** NO VALIDATOR ***" if seat in missing else "(none recorded)")
```
- **`*** NO VALIDATOR ***`** — the model carries a positive fact `seat_validator_missing/1`: the repo *states* the seat has no validator. It is an asserted gap, i.e. a sandwich-rule violation on the record.
- **`(none recorded)`** — no `seat_validator/2` fact and no `seat_validator_missing/1` fact: the repo says nothing either way. An unknown, not a violation.

Today exactly one seat is in each state: `attribution_author` → `*** NO VALIDATOR ***`; `golden_review` → `(none recorded)`.

### Run output

**Command** (from `SFE/`): `.venv/bin/python machine/query.py seats` — **wall clock 0.29 s real / 0.20 user / 0.02 sys**

```
seat | tier(s) | scaling unit | producer -> validator

  attribution_author     haiku            per_worksheet_row  -                                    -> *** NO VALIDATOR ***
  backfill_author        frontier         per_worksheet_row  backfill_worksheet.py build --dir    -> backfill_worksheet.py validate --dir <dir>
  blind_coder            haiku            per_corpus         prep_hole_corpus.py                  -> check_taxonomy.py / taxonomy_agreement.py
  change_reviewer        frontier/human   per_cycle          cycle.py writes assignments/review   -> cycle.py _implement: verdict in {proceed,blocked} and non-empty 'by'
  decision_signer        frontier/human   per_cycle          cycle.py drafts decision.draft.jso   -> cycle.py _decide: closed decision vocabulary, non-empty signed_by, forced justification
  density_editor         haiku            per_document       -                                    -> check_rewrite.py <before> <after>
  disagreement_autopsy   haiku            per_dossier        audit_disagreements.py dossiers      -> audit_disagreements.py validate --verdicts <file> --dossier-dir <dir>
  drift_standing         haiku            per_dossier        drift_dossiers.py dossiers           -> drift_dossiers.py validate --verdicts <file> --dossier-dir <dir>
  flip_adjudicator       haiku            per_flip           dossier.py dossiers                  -> dossier.py validate --dir <dir> --verdict-file <file>
  golden_author          haiku            per_document       -                                    -> golden.load sha-freeze + test_golden.py
  golden_review          frontier/human   per_document       the golden_author seat's golden_tr   -> (none recorded)
  select_audit           haiku            per_behaviour      select_audit.py                      -> select_audit.py validate
```

12 seats — matches `SFE/machine/README.md:66`. Three carry `frontier/human` — matches `SFE/MODULE_MAP.md:273` (`three ⚠️ seats are explicitly frontier/human`). Four seats show `-` as producer (`attribution_author`, `density_editor`, `golden_author`, `golden_review`).

**Deliberate divergence in validator flag spellings** — `SFE/MODULE_MAP.md:300-301`:
> `The panel-blind flip seat is singular (\`--verdict-file\`) because the plural \`--verdicts\` is`
> `a FORBIDDEN token — it names per-judge panel labels. Do not "harmonize" them.`

Pinned as a §11 anti-rule, `SFE/MODULE_MAP.md:314`:
> `| \`dossier.py --verdict-file\` vs \`audit_disagreements.py --verdicts\` | Must stay divergent | \`test_dossier.py:583-598\`, \`CYCLE_DESIGN\` F9 | Plural \`--verdicts\` is a FORBIDDEN token (it names per-judge panel labels) |`

**Recorded conflict on seat count:** the machine records `d(brief_count,"briefs/README.md says the directory holds 11 briefs as of 2026-08-05","ls briefs/*.md returns 12 — density_editor.md is in the directory and absent from the list")`. The query output above shows `density_editor` present, so the *model* has 12 and the *README* has 11.

---

## 9. `check_model.py`

### Definition

`SFE/machine/README.md:104-105`: `## The validator: three independent checks` — followed by `**(a) SOURCE CHECK.**`, `**(b) DIFFERENTIAL CHECK against \`cycle.py\` — 282 comparisons.**`, `**(c) KNOWN-ANSWER SET.**`, plus the separate `ACCEPTANCE TEST`.

**The heading says three; the output prints four.** `SFE/machine/README.md:16` — `.venv/bin/python machine/check_model.py              # the validator: 4 checks`. Both statements are in the same file, 88 lines apart, unreconciled. **Count of checks: 4** — (a), (b), (c), and (\*) the acceptance test, which the README describes under its own heading (`## The acceptance test: both known contradictions surfaced`, `:190`).

### Run output

**Command** (from `SFE/`): `.venv/bin/python machine/check_model.py` — **wall clock 2.41 s real / 2.09 user / 0.25 sys**

```
PASS (a) SOURCE CHECK
PASS (b) DIFFERENTIAL CHECK vs cycle.py (282 comparisons)
PASS (c) KNOWN-ANSWER SET
PASS (*) ACCEPTANCE TEST

60 contradiction(s) reported by rules.lp (run `python3 machine/query.py contradictions`)
```

Four PASS lines; **60 contradictions reported and not treated as a failure**. The two acceptance-test contradictions are documented at `SFE/machine/README.md:194-213`: the `section.py` `-0.143` retraction still live at `:82` and `:326`, and `exactly **27** hits` of `both_defensible` verdicts (`14 fp_threshold_drift, 13 fp_promiscuous_atom`), with the finding that `**The two \`either\`-kind boundary_dispute causes are used ZERO times in the whole 294-case census**`.

**Discrepancy found in the model's own documentation.** `SFE/machine/README.md:86-90` states:
> `* **\`HARNESS_REDESIGN.md\` is excluded entirely** from the scan`
> `  (\`scan_excluded/2\` records why): other agents are editing it, so any line`
> `  citation into it would be stale before it was read. Its content is therefore`
> `  invisible to the model — including anything it says about \`FLIP_BUDGET\`.`

But `SFE/machine/scan.py:41` reads `EXCLUDED = {}  # HARNESS_REDESIGN.md un-excluded 2026-08-06: editing finished`, `machine/scanned.lp` contains **zero** `scan_excluded` facts, and **20** lines of `machine/scanned.lp` cite `HARNESS_REDESIGN.md` (its first three facts are `claim_retracted("-0.0479",...)`, `claim_retracted("-0.143",...)`, `claim_retracted("0.0021",...)` from that file). The README is stale; the code records the correction.

Constants the model carries (`query.py constants`, 10, provenance-tagged):
```
  c(closure_defaults,"modelspec_clauses.json, constitution_clauses.json, behaviours_query.json",chosen)
  c(containment_pricing_version,"1.2",chosen)
  c(decision_values,"keep, revert",chosen)
  c(dev_census_cells,"avoiding-over-and-under-caution, harm-avoidance-to-third-parties, helpfulness",chosen)
  c(directions,"newly_predicted, no_longer_predicted",chosen)
  c(fanout_degenerate,"5",chosen)
  c(flip_budget,"30",chosen)
  c(noise_floor,"(0.0316, 0.037)",derived)
  c(overridable_phases,"PREDICT, IMPLEMENT, CENSUS",chosen)
  c(patient_mismatch_discount,"0.10",derived)
```
`SFE/machine/README.md:74` — `\`FLIP_BUDGET = 30\` is \`chosen\`; \`NOISE_FLOOR = (0.0316, 0.037)\` is \`derived\`.` The gap is stated at `:213+`: `**\`FLIP_BUDGET = 30\` has no derivation.**`

---

## 10. `graph_check.py` on `runs/ds7/root_graph.production.json`

**Command** (from `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/`):
`~/…/semi-formal-experiment/.venv/bin/python graph_check.py runs/ds7/root_graph.production.json` — **wall clock 0.14 s real / 0.11 user / 0.01 sys**

This is the exact demo-path command in CI — `.github/workflows/ci.yml:35`:
```
          python3 walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/graph_check.py walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/runs/ds7/root_graph.production.json
```

```
nodes: 773   uncovered entries: 733
bad line ranges: 0 / 846 spans  []
bad quotes: 0 / 602  []
span sizes (lines covered): min 1  median 1  max 44
  nodes covering 0 lines: 0;  >100 lines: 0 of 773
overlapping node pairs: 266 (of 298378); nested pairs: 266
provided names: 115 (6 provided by >1 node)
needs: 1085; dangling (no provider): 25
   dangling: L699-796_n021 needs ask_clarifying_questions_section
   dangling: L797-830_n014 needs sexual_content_involving_minors_section
   dangling: L831-1000_n003 needs authority_level_ordering
   dangling: L831-1000_n004 needs authority_level_ordering
   dangling: L831-1000_n010 needs authority_level_ordering
   dangling: L831-1000_n011 needs authority_level_ordering
   dangling: L831-1000_n014 needs authority_level_ordering
   dangling: L1108-1367_n004 needs objective_point_of_view
   dangling: L1108-1367_n007 needs objective_point_of_view
   dangling: L1368-1541_n005 needs avoid_info_hazards
   dangling: L1542-1706_n002 needs avoid_info_hazards
   dangling: L1542-1706_n007 needs assume_best_intentions
   dangling: L1542-1706_n014 needs support_mental_health
   dangling: L2405-2473_n011 needs assume_objective_pov
   dangling: L3041-3146_n002 needs letter_and_spirit_principle
   dangling: L3041-3146_n002 needs assume_best_intentions_principle
   dangling: L3596-3876_n032 needs avoid_errors_rule
   dangling: L3954-4251_n006 needs be_warm_rule
   dangling: L3954-4251_n007 needs be_warm_rule
   dangling: L3954-4251_n042 needs be_thorough_but_efficient_rule
   dangling: L4572-4692_n002 needs do_not_encourage_self_harm
   dangling: L4572-4692_n011 needs do_not_encourage_self_harm
   dangling: L4572-4692_n012 needs respect_real_world_ties
   dangling: L4572-4692_n015 needs avoid_info_hazards
   dangling: L4572-4692_n016 needs do_not_encourage_self_harm
   multi-provided: {'root_authority': ['L1-170_n043', 'L171-426_n004', 'L171-426_n007', 'L609-698_n001', 'L699-796_n001', 'L1001-1107_n001', 'L1001-1107_n005', 'L1108-1367_n011', 'L1108-1367_n012', 'L1542-1706_n001', 'L1707-1973_n015'], 'system_authority': ['L1-170_n049', 'L171-426_n008', 'L1108-1367_n010', 'L1974-2125_n001'], 'developer_authority': ['L1-170_n051', 'L171-426_n009', 'L1707-1973_n001'], 'user_authority': ['L1-170_n055', 'L171-426_n010', 'L1108-1367_n013', 'L1707-1973_n007', 'L2126-2404_n024', 'L2126-2404_n025', 'L2555-2652_n007', 'L3239-3382_n001', 'L3877-3953_n014', 'L3505-3953_n001', 'L4252-4482_n004'], 'guideline_authority': ['L1-170_n058', 'L171-426_n011', 'L2126-2404_n026', 'L2821-3040_n001', 'L3239-3382_n009', 'L3954-4251_n005', 'L3954-4251_n009', 'L3954-4251_n016', 'L3954-4251_n022', 'L3954-4251_n032', 'L3954-4251_n041', 'L4252-4482_n012', 'L4252-4482_n018'], 'conversational_language_examples': ['L2821-3040_n019', 'L2821-3040_n020', 'L2821-3040_n021']}
K1 nodes grounded on the L183-191 list: [('L1-170_n042', (183, 183)), ('L171-426_n007', (186, 186)), ('L171-426_n008', (187, 187)), ('L171-426_n009', (188, 188)), ('L171-426_n010', (189, 189)), ('L171-426_n011', (190, 190))]; with ordering in provides: [('L1-170_n042', (183, 183), 'PARTIAL list coverage'), ('L171-426_n007', (186, 186), 'PARTIAL list coverage')]
nodes with zero needs: 94 / 773
spans with quotes: 602 / 846
authority-tagged headings captured in some node: 50 / 59
lines covered by nodes: 3638 / 3722 non-blank; declared uncovered: 92; unaccounted: 0
```

The record's own summary, `ARTIFACTS.md:19`:
> `| The certified graph | 773 nodes, zero bad spans of 846 | \`walkthrough/…/runs/ds7/root_graph.production.json\` | the arc-2 substrate |`

**Reproduced exactly** (773 nodes, `bad line ranges: 0 / 846`). But the record's one-liner omits: 733 uncovered entries, **25 dangling needs** with no provider, `spans with quotes: 602 / 846` (244 spans carry no quote), and `authority-tagged headings captured in some node: 50 / 59` (9 missing). "Zero bad spans" is a true but narrow claim about line-range validity only. This is arc-2, not arc-1 — included because it is the CI demo path.

---

## 11. `benchmark.py --tool` on the b8 config

**Command** (from `SFE/`):
`.venv/bin/python benchmark.py --tool --annotations annotations_b8.json --behaviour-atoms behavior_atoms_b8.json` — **wall clock 16.60 s real / 16.32 user / 0.08 sys**. Output is 354 lines; the key blocks verbatim.

`MODULE_MAP.md:257-259` names this exact command as "the headline table", while `:234-236` warns: `⚠️ 2026-08-04: the commands below still run but quote the b8 config; the preferred config is \`annotations_ext_v1_merged.json\` + \`behavior_atoms_audit_v1.json\``.

```
# Behavioural-relevance benchmark

clause set: `modelspec_clauses.json @ threshold None (tool)` (593 clauses)

Headline universe: **TRUE universe (every passage the judges graded)**. Every number is printed beside its **published universe (score-0 passages deleted)** counterpart and the delta.

## Judged universe — reconstruction provenance

The panel graded EVERY passage of the spec in one prompt; `build_site_data.keeps_citation` then dropped every passage whose summed score was 0 before publishing. Those rows are gold-negative AND unanimously predicted negative, so restoring them restores true-negative credit rather than inventing any. Recovered rows carry verdict 0 from every judge.

| behaviour | spec | universe | published | recovered as 0 | join rate |
| --- | --- | ---: | ---: | ---: | ---: |
| avoiding-over-and-under-caution | constitution (anthropic) | 374 | 77 | 297 (79%) | 1.000 |
| avoiding-over-and-under-caution | model-spec (openai) | 589 | 153 | 436 (74%) | 1.000 |
| harm-avoidance-to-third-parties | constitution (anthropic) | 374 | 199 | 175 (47%) | 1.000 |
| harm-avoidance-to-third-parties | model-spec (openai) | 589 | 333 | 256 (43%) | 1.000 |
| helpfulness | constitution (anthropic) | 374 | 197 | 177 (47%) | 1.000 |
| helpfulness | model-spec (openai) | 589 | 377 | 212 (36%) | 1.000 |

unjoined published passages: **0** (every published passage joins)
```

```
## Universe delta — TRUE universe vs published universe

| behaviour | n passages (true / published) | tool MCC true | tool MCC published | tool delta | judge MCC true | judge MCC published | judge delta | gap true | gap published |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| helpfulness | 589 / 377 | **+0.201** | +0.142 | +0.058 | **+0.571** | +0.426 | +0.144 | +0.370 | +0.284 |
| harm-avoidance-to-third-parties | 589 / 333 | **+0.350** | +0.250 | +0.100 | **+0.615** | +0.434 | +0.181 | +0.265 | +0.184 |
| avoiding-over-and-under-caution | 589 / 153 | **+0.283** | +0.264 | +0.018 | **+0.481** | +0.321 | +0.160 | +0.198 | +0.056 |
| **mean** | | **+0.278** | +0.219 | +0.059 | **+0.555** | +0.394 | +0.162 | +0.278 | +0.175 |
```

```
### TRUE universe — the headline
## Headline — tool vs the panel, on the panel's own passage denominator

| behaviour | scope | **tool MCC** | judge MCC (mean) | tool F1 | F1 FLOOR | tool lift | judge F1 (mean LOO) | judge lift | verdict |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| helpfulness | matched | **+0.207** | +0.570 | 0.379 | 0.304 | +0.074 | 0.634 | +0.329 | below bar |
| helpfulness | full | **+0.201** | +0.571 | 0.376 | 0.307 | +0.069 | 0.636 | +0.329 | below bar |
| harm-avoidance-to-third-parties | matched | **+0.366** | +0.607 | 0.494 | 0.371 | +0.122 | 0.687 | +0.316 | below bar |
| harm-avoidance-to-third-parties | full | **+0.350** | +0.615 | 0.482 | 0.381 | +0.101 | 0.697 | +0.316 | below bar |
| avoiding-over-and-under-caution | matched | **+0.281** | +0.481 | 0.273 | 0.126 | +0.147 | 0.420 | +0.294 | below bar |
| avoiding-over-and-under-caution | full | **+0.283** | +0.481 | 0.273 | 0.125 | +0.148 | 0.419 | +0.294 | below bar |

| behaviour | predicted clauses | of which unscored | clauses visible to the panel | passages predicted | passages judged | joinable | unjoinable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| helpfulness | 199 | 3 (2%) | 586 | 196 | 589 | 582 | 7 |
| harm-avoidance-to-third-parties | 111 | 2 (2%) | 586 | 110 | 589 | 582 | 7 |
| avoiding-over-and-under-caution | 181 | 4 (2%) | 586 | 178 | 589 | 582 | 7 |
```

The **published-universe** counterpart tables, printed for comparison only, still fire the historical refusals:
```
| helpfulness | matched | **+0.149** | +0.426 | 0.432 | 0.438 | -0.006 | 0.634 | +0.194 | BELOW FLOOR |
| helpfulness | full | **+0.142** | +0.426 | 0.428 | 0.441 | -0.013 | 0.636 | +0.194 | BELOW FLOOR |
| harm-avoidance-to-third-parties | matched | **+0.268** | +0.426 | 0.517 | 0.578 | -0.061 | 0.687 | +0.109 | BELOW FLOOR |
| harm-avoidance-to-third-parties | full | **+0.250** | +0.434 | 0.504 | 0.588 | -0.083 | 0.697 | +0.109 | BELOW FLOOR |
| avoiding-over-and-under-caution | matched | **+0.258** | +0.320 | 0.466 | 0.398 | +0.067 | 0.420 | +0.025 | **UNUSABLE FOR HEADLINE** |
| avoiding-over-and-under-caution | full | **+0.264** | +0.321 | 0.466 | 0.394 | +0.071 | 0.419 | +0.025 | **UNUSABLE FOR HEADLINE** |

> **REFUSED — these behaviours must not carry a headline number.** On the targets listed the F1 floor exceeds the judge bar, so a constant predictor outscores the judge the tool is being compared to.
>
> - `avoiding-over-and-under-caution`: gold(s) held out from kimi-k2, on a universe of 153 passages. Contributing: kimi-k2 never emits `related`, so it ran a BINARY scale while the others ran a three-point one and `>=1 = relevant` is not the same decision rule for it. That is a scale caveat, not by itself a reason to refuse — the refusal here is the floor-over-bar check above.
```

Head-to-head, ROC and band tables are quoted in §1 and §5. Bands:
```
| behaviour | band min | band median | band max | n thresholds |
| helpfulness | +0.080 | +0.165 | +0.262 | 16 |
| harm-avoidance-to-third-parties | +0.320 | +0.381 | +0.444 | 16 |
| avoiding-over-and-under-caution | +0.147 | +0.282 | +0.379 | 16 |
```

Tail:
```
**Atom vocabulary — top 15 by clause count.** An atom on a large fraction of clauses is a stopword; those above the cutoff are floored to zero weight.

| atom | n_clauses | share | stopworded |
| `safe_completion` | 43 | 7.3% |  |
| `express_uncertainty` | 36 | 6.1% |  |
| `nonjudgmental_assistance` | 27 | 4.6% |  |
| `follow_chain_of_command` | 24 | 4.0% |  |
| `user_request` | 24 | 4.0% |  |
| `clarify_user_intent` | 22 | 3.7% |  |
| `comply_user_request` | 21 | 3.5% |  |
| `informational_guidance` | 20 | 3.4% |  |
| `redirect_user_request` | 20 | 3.4% |  |
| `human_autonomy` | 18 | 3.0% |  |
| `content_transformation` | 17 | 2.9% |  |
| `instruction_authority_levels` | 17 | 2.9% |  |
| `maintain_factual_tone` | 17 | 2.9% |  |
| `acknowledge_user_feelings` | 16 | 2.7% |  |
| `behavior_customization` | 16 | 2.7% |  |

distinct atoms: 361; stopworded: 0
```

**Self-referential caveats the report prints about its own headline** (preamble items 5 and 6):
> `5. **THE OPERATING POINT WAS FIT ON THIS PANEL.** \`relevance.DEFAULT_THRESHOLD\` is the argmax of a 51-point grid selected on the same three behaviours scored below, so every thresholded number here is a HINDSIGHT-THRESHOLD number and the in-sample mean MCC (+0.274 published / +0.320 true) is a CEILING, not a result.`

Note the report's item 5 quotes **+0.274 / +0.320** as "the in-sample mean MCC" while its own universe-delta table (same run) prints **+0.219 / +0.278**. This is a live self-conflict inside one generated document: the hardcoded prose and the computed table disagree. Also, `relevance.DEFAULT_THRESHOLD` is described as live in item 5, while `SFE/HANDOFF.md:835-837` records it as retired:
> `*(\`relevance.predict\` now derives its cut label-free by default, retiring \`DEFAULT_THRESHOLD = 0.18\` — an in-sample argmax on the scoring panel, i.e. a live invariant-9 violation that shipped for most of this session.)*`

---

## 12. `cite.py`

### Definition

`engine/spec-cite/cite.py:2-20`:
```
"""spec-cite: resolve and verify precise citations into the mirrored specs.

Locator grammar (canonical form, see specs/CITATION.md):

    <spec>@<version> > <section-ref> > ¶<n>[ s<a>[-<b>]]
    <spec>@<version> > <section-ref> > ¶<n> s<a> - ¶<m> s<b>

  spec         constitution | model-spec
  section-ref  #anchor (model-spec) or heading path "Chapter > Section" (constitution)
  ¶<n>         block number within the section's direct span ("p<n>" also accepted)
  s<a>[-<b>]   sentence (range) within the block; omit for the whole block

  ">" and "›" are interchangeable path separators.

Commands:
    cite.py outline <spec>[@<version>]
    cite.py show    "<spec>[@<version>] > <section-ref>"
    cite.py resolve "<locator>"
    cite.py find    <spec>[@<version>] "<text>"
"""
```
Pinned specs, `engine/spec-cite/cite.py:29-33`:
```python
SPECS = {
    ("constitution", "2026-01-20"): "specs/claude-constitution/20260120-constitution.md",
    ("model-spec", "2025-12-18"): "specs/openai-model-spec/model_spec.md",
}
DEFAULT_VERSION = {"constitution": "2026-01-20", "model-spec": "2025-12-18"}
```

`ARTIFACTS.md:27` — `| Spec citation engine | Locator → verbatim text for both specs | \`engine/spec-cite/cite.py\` | the citation discipline |`.

### Run 1 — outline

**Command** (from repo root): `.venv_clingo/bin/python engine/spec-cite/cite.py outline model-spec` — **wall clock 0.05 s real / 0.03 user / 0.01 sys**. 81 lines:

```
model-spec@2025-12-18
Overview  {#overview}
  Structure of the document  {#structure}
  Red-line principles  {#red_line_principles}
  General principles  {#general_principles}
  Specific risks  {#risk_taxonomy}
  Instructions and levels of authority  {#levels_of_authority}
Definitions  {#definitions}
The chain of command  {#chain_of_command}
  Follow all applicable instructions  {#follow_all_applicable_instructions}
  Respect the letter and spirit of instructions  {#letter_and_spirit}
  No other objectives  {#no_other_objectives}
  Act within an agreed-upon scope of autonomy  {#scope_of_autonomy}
  Control and communicate side effects  {#control_side_effects}
  Assume best intentions  {#assume_best_intentions}
  Ignore untrusted data by default  {#ignore_untrusted_data}
Stay in bounds  {#stay_in_bounds}
  Comply with applicable laws  {#comply_with_laws}
  Do not generate disallowed content  {#disallowed_content}
    Prohibited content  {#prohibited_content}
      Never generate sexual content involving minors  {#sexual_content_involving_minors}
    Restricted content  {#restricted_content}
      Don't provide information hazards  {#avoid_info_hazards}
      Don’t facilitate the targeted manipulation of political views  {#avoid_targeted_political_manipulation}
      Respect creators and their rights  {#respect_creators}
      Protect people's privacy  {#protect_privacy}
    Sensitive content in appropriate contexts  {#sensitive_content}
      Don't respond with erotica or gore  {#no_erotica_or_gore}
      Do not contribute to extremist agendas that promote violence  {#avoid_extremist_content}
      Avoid hateful content directed at protected groups  {#avoid_hateful_content}
      Don't engage in abuse  {#avoid_abuse}
    Comply with requests to transform restricted or sensitive content  {#transformation_exception}
  Take extra care in risky situations  {#risky_situations}
    Try to prevent imminent real-world harm  {#prevent_imminent_harm}
    Do not facilitate or encourage illicit behavior  {#do_not_facilitate_illicit_behavior}
    Do not encourage self-harm, delusions, or mania  {#do_not_encourage_self_harm}
    Provide information without giving regulated advice  {#avoid_regulated_advice}
    Support users in mental health discussions  {#support_mental_health}
  Do not reveal privileged information  {#protect_privileged_information}
  Always use the preset voice  {#use_preset_voice_in_voice_mode}
  Uphold fairness  {#uphold_fairness}
  Respect real-world ties  {#respect_real_world_ties}
Seek the truth together  {#seek_truth}
  Don't have an agenda  {#no_agenda}
    Assume an objective point of view  {#assume_objective_pov}
    Present perspectives from any point of an opinion spectrum  {#present_perspectives}
    No topic is off limits  {#no_topic_off_limits}
  Be honest and transparent  {#be_honest_and_transparent}
    Do not lie  {#do_not_lie}
    Don't be sycophantic  {#avoid_sycophancy}
    Consider uncertainty, state assumptions, and ask clarifying questions when appropriate  {#ask_clarifying_questions}
    Express uncertainty  {#express_uncertainty}
    Highlight possible misalignments  {#highlight_misalignments}
Do the best work  {#best_work}
  Avoid factual, reasoning, and formatting errors  {#avoid_errors}
  Avoid overstepping  {#avoid_overstepping}
  Be creative  {#be_creative}
  Support the different needs of interactive chat and programmatic use  {#support_programmatic_use}
Use appropriate style  {#style}
  Love humanity  {#love_humanity}
  Be rationally optimistic  {#be_rationally_optimistic}
  Be responsible  {#be_responsible}
  Be interesting and interested  {#be_interesting_and_interested}
  Be curious  {#be_curious}
  Be clear and direct  {#be_clear}
  Be suitably professional  {#be_professional}
  Have conversational sense  {#have_conversational_sense}
  Be warm  {#be_warm}
  Don't make unprompted personal comments  {#do_not_make_unprompted_personal_comments}
  Avoid being condescending or patronizing  {#avoid_being_condescending}
  When appropriate, be helpful when refusing  {#refusal_style}
  Use Markdown with LaTeX extensions  {#formatting}
  Be thorough but efficient, while respecting length limits  {#be_thorough_but_efficient}
  Adapt to the user's modality  {#voice_style}
    Use accents respectfully  {#imitate_accents_in_voice_mode}
    Be concise and conversational  {#be_concise_and_conversational_in_voice_mode}
    Adapt length and structure to user objectives  {#adapt_length_in_voice_mode}
    Handle interruptions gracefully  {#handle_interruptions_in_voice_mode}
    Respond appropriately to audio testing  {#respond_to_audio_testing_in_voice_mode}
Under-18 Principles  {#chatgpt_u18}
  Prioritize safety for teens {#prioritize_teen_safety authority=root tags=under_18}
```
80 sections, only 1 (`prioritize_teen_safety`) carrying `authority=` in its heading — cf. graph_check's `authority-tagged headings captured in some node: 50 / 59`, which counts a different corpus/version.

### Run 2 — resolve

**Command** (from repo root): `.venv_clingo/bin/python engine/spec-cite/cite.py resolve "model-spec@2025-12-18 > #avoid_sycophancy > ¶2 s1"` — **wall clock 0.05 s real / 0.03 user / 0.01 sys**

```
For objective questions, the factual aspects of the assistant’s response should not differ based on how the user’s question is phrased.
```

This is the same command CI runs (`.github/workflows/ci.yml:33`) as the demo path.

Settled finding tying `cite.py` to the join, `SFE/HANDOFF.md:611-614`:
> `- **Judges saw full example blocks, not captions.** \`cite.py:147-148\` attaches the fenced dialogue to its \`**Example**:\` caption *before* judging; \`build_site_data.py:50-57\` stores only the caption as \`quote\` because fenced content "renders as code the matcher cannot see". The caption is a display anchor. Label unit and prediction unit agree.`

Verified in source — `engine/spec-cite/cite.py:147-149`:
```python
            if blocks and re.match(r"^\*\*Example\*\*", blocks[-1]):
                blocks[-1] = blocks[-1] + "\n\n" + fenced
            else:
```

---

## 13. Withdrawn / retracted / suspended arc-1 results

Repo-wide, 278 lines carry a retraction word. The **distinct results** withdrawn, retracted or suspended in arc-1:

| # | result | disposition | path:line |
|---|---|---|---|
| 1 | `"typing contributes nothing measurable on this data"` | **retracted** — three independent errors | `SFE/HANDOFF.md:621`, `:623-625`; `SFE/structural.py:115`, `:118` |
| 2 | `"a coarse topic filter, not concept-level ontological work"` | **retracted** | `SFE/HANDOFF.md:624`, `:687`; `SFE/structural.py:119` |
| 3 | the noise floor `NOISE = 0.06` | **expired constant** — `an interim guardrail explicitly conditional on n=1` | `SFE/HANDOFF.md:627-631` |
| 4 | `The ontology-pass gate at +0.310 ± 0.021` | **suspended** — `it was defending a null that does not exist` | `SFE/HANDOFF.md:700` |
| 5 | `structural.py`'s `+0.340` gate | **GATE SUSPENDED** — `+0.340 is DRAW0, the MAXIMUM of a 5-draw spread` | `SFE/structural.py:323` |
| 6 | `"USE THIS MODULE…"` recommendation in `structural.predict` | **retracted** | `SFE/structural.py:308` |
| 7 | `structural.PRIMARY_OPERATOR = "act_match"` at `+0.310` | **retracted / must not be carried forward** — `Anything quoted from \`structural.py\` at +0.310 is a 3-behaviour figure` | `SFE/HANDOFF.md:1038`, `:1057-1058`, `SFE/structural.py:353` |
| 8 | the supervised ceiling `+0.258` | **retracted** — `Three compounding faults, all mine` | `SFE/HANDOFF.md:726-731` |
| 9 | `"the ceiling is representation capacity"` diagnosis | **⛔ THE DIAGNOSIS WAS WRONG** — `Refuted, twice, from data already on disk.` | `SFE/HANDOFF.md:705-709` |
| 10 | the `rho`-against-learned-coefficients lead | **WITHDRAWN, it was a fitting vector** | `SFE/HANDOFF.md:1007`, `:824` |
| 11 | `"a genuine result being left on the table"` | **retracted** — `an instruction to go fit it` | `SFE/HANDOFF.md:1015`, `:1423-1426` |
| 12 | `## ⛔ THE CONTRACT-COMPLIANT MODULE IS WORSE THAN THE ONE IT REPLACES` | **RETRACTED in full** (section kept deliberately) | `SFE/HANDOFF.md:1095`, `:1097-1104`, `:1188` |
| 13 | `section.py`'s `"⚠️ THIS LOSES. Measured −0.143 MCC"` | **RETRACTED**, but the machine finds `-0.143` still asserted live at `section.py:82` and `:326` | `SFE/section.py:480`; `SFE/machine/README.md:194-200` |
| 14 | `"the gain is the partition, not the extra prediction mass"` | **RETRACTED** — `The partition is INERT.` | `SFE/HANDOFF.md:1229-1235` |
| 15 | `benchmark.noise_floor` | **MIS-SPECIFIED — delete it** | `SFE/HANDOFF.md:1209-1214` |
| 16 | `"sign consistent in 5/5 draws"` as evidence | **`worthless evidence`** | `SFE/HANDOFF.md:1220` |
| 17 | noise floor `0.0295` | superseded — `The noise floor is 0.035–0.037, not 0.0295` and `0.0316–0.037, NOT 0.0295` | `SFE/HANDOFF.md:1090`, `:1138` |
| 18 | noise floor `0.045` | `refused *by name* in code and test` | `SFE/HANDOFF.md:925`, `SFE/benchmark.py:2803` |
| 19 | `relevance.DEFAULT_THRESHOLD = 0.18` | **retired** — `a live invariant-9 violation that shipped for most of this session` | `SFE/HANDOFF.md:835-837` |
| 20 | `"Reframe the tool as a high-precision lead generator reporting P@k"` | **Deleted from this list, deliberately — do not reinstate** | `SFE/HANDOFF.md:1461-1468` |
| 21 | `## ~~THE RESULT (2026-08-01, first version)~~` (F1 table, "MCC near chance", channel ablation) | **DELETED, IT WAS ALL BUG ARTIFACT** | `SFE/HANDOFF.md:1352-1354` |
| 22 | `~~Current headline~~` block headed `"QUOTE THIS +0.187"` | **DELETED (published universe, superseded)** | `SFE/HANDOFF.md:1380-1386` |
| 23 | `"the section signal is unexploited"` (AUC 0.795 vs 0.522) | **(deleted)** | `SFE/HANDOFF.md:1420-1426` |
| 24 | `"the section prior is harmful"` / `"dropping it costs 0.022 MCC"` | **Both overstate** — `we cannot yet tell` | `SFE/HANDOFF.md:1413-1418` |
| 25 | every ablation number before 2026-08-01 12:18 | **void** — `section_path` dropped by `benchmark._clause_rows` | `SFE/HANDOFF.md:1374-1378` |
| 26 | shipped section AUCs `0.522/0.633/0.623` | **do not reproduce** — corrected to `0.561/0.695/0.840` | `SFE/HANDOFF.md:879-881` |
| 27 | `"MCC is robust to true negatives, so it is safe here"` | **False as applied** | `SFE/HANDOFF.md:488-490` |
| 28 | `"sol is degenerate / near chance"` | artifact of deletion — `−0.027 → +0.308` | `SFE/HANDOFF.md:490-491` |
| 29 | `"over/under-caution is UNUSABLE for a headline"` | artifact — `the **strongest** behaviour by AUC (0.90)` | `SFE/HANDOFF.md:492-493` |
| 30 | the selection-effect caveat `unliftable_frac 22%/14%/56%` | `on the true one it is **2% / 1% / 2%**` | `SFE/HANDOFF.md:494-495` |
| 31 | the published bar `0.764/0.780/0.500` | `superseded and must not be quoted` | `SFE/HANDOFF.md:1275-1276` |
| 32 | `849/863` | `**Do not quote 849/863**` (still quoted 4× in HANDOFF — §3) | `SFE/MODULE_MAP.md:54` |
| 33 | `verdicts` is a string repr | `that was wrong, an artifact of a pretty-printer calling \`str()\` on it` | `SFE/HANDOFF.md:915-918` |
| 34 | the S3 patient-pricing mechanism (`pricing_version 2.0`) | **BUILT AND REVERTED** — `The bound fired; the module stays in the tree, out of the shipped path` | `SFE/MODULE_MAP.md:106`; `SFE/cycles/patient-pricing-2026-08-04/decision.json:41`, `:86` |
| 35 | the census `side` field | `was assigned by judgment, was block-segregated by run (129/0/0, 58/0/27, 39/41/0), and was demonstrably wrong on H006` | `SFE/HANDOFF.md:63-66` |
| 36 | `combined.MEASURED` / `section.MEASURED` | `⚠️ … ARE HAND-TRANSCRIBED CONSTANTS` — `A green suite is not evidence that any of them is what the pipeline computes.` | `SFE/HANDOFF.md:1241-1247` |
| 37 | the "unmined document meaning" / semantic arm (Lead 3) | **UNREVIEWED** — `do not cite as settled, and do not iterate it` | `SFE/HANDOFF.md:93-96`, `:781`, `:809` |
| 38 | every `# MUTATION-VERIFIED` marker | `Every "# MUTATION-VERIFIED" marker in this repo predates this discovery.` — `A mutation test that cannot prove it ran the mutant proves nothing.` | `SFE/HANDOFF.md:515`, `:520` |
| 39 | the old goal (`"Quality equivalent to or higher than just asking the frontier models"`) | **retired** — `is **not the target any more**` | `SFE/HANDOFF.md:41-45` |
| 40 | `HARNESS_REDESIGN.md` claims `-0.0479`, `-0.143`, `0.0021` | scanned as `claim_retracted` | `SFE/machine/scanned.lp:7-12` |
| 41 | the 294-case census's own config identity | never backfilled — `Backfilling one fabricates the identity of a run nobody observed.` | `SFE/MODULE_MAP.md:317` |

**Unresolved by design:** `SFE/HANDOFF.md:1259-1264` — `> **⚠️ FLAGGED UNRECONCILED (2026-08-04).** The iteration loop as built does NOT run this recommendation … No recorded decision reverses this paragraph; the two simply have not been reconciled.` The record explicitly does *not* choose between `Ship \`section@any_atom\`, not \`combined\`` (`:1256`) and the fact that `snapshot.py` scores through `relevance.RelevanceIndex`.

---

## 14. The three `behaviours.json` files

### Schema and counts (measured today)

**(a) `data/behaviours.json`** — 1,082,124 bytes. The panel roster / answer key.

Top-level: `{generatedFrom: [1], provenance: {8 keys}, behaviours: [3]}`. Each behaviour: `id, slug, name, definition, category, coverage`. Each `coverage[spec]`: `{verdict, depth, note, verifiedDate, passages}`. Each passage: `id, locator, quote, exampleBlock, role, adjacent, verdicts, score`.

Entry counts: **3 behaviours × 2 specs = 6 coverage cells**; passages 377 + 333 + 153 (openai) and 197 + 199 + 77 (anthropic) = **1,336 passages** total, **863** on the model-spec side. `SFE/HANDOFF.md:618`: `**\`role\` ↔ \`verdicts\` agree exactly**: 4008 verdict lines, 1336 passages, zero mismatches.`

**(b) `engine/panel/behaviours.json`** — 10,303 bytes. The vendored harness's behaviour *definitions*, no labels.

A flat dict keyed by slug: **11 entries** — `no-sycophancy, undermine-oversight, helpfulness, harmlessness-to-user, third-party-harm, proportionate-risk, tradeoffs, over-under-caution, objectivity, user-autonomy, general-welfare`. Per-entry keys: `label, title, source, query, boundary` (4–7 keys; `general-welfare` also carries `query_v2` and `note_v2`; `helpfulness` lacks `title`).

Note the slugs **do not match** `data/behaviours.json`'s (`third-party-harm` vs `harm-avoidance-to-third-parties`; `over-under-caution` vs `avoiding-over-and-under-caution`), and 11 ≠ 3 ≠ 9.

**(c) `SFE/behaviours_query.json`** — 1,367 bytes. The query-side split.

`{_comment, _source, behaviours: [3]}`; each behaviour `{slug, name, definition, category}`. **3 entries**, definitions only, **no coverage, no verdicts, no scores**.

### How they differ

| | `data/behaviours.json` | `engine/panel/behaviours.json` | `SFE/behaviours_query.json` |
|---|---|---|---|
| purpose | the answer key (per-judge verdicts + scores) | the harness's behaviour catalogue (prompt text) | the tool's legitimate query input |
| entries | 3 behaviours, 6 cells, 1,336 passages | 11 behaviours | 3 behaviours |
| labels? | **yes** — `verdicts`, `score`, `role` | no | **no** |
| fence status | `FORBIDDEN` token | not fenced | readable by query modules |
| slug scheme | full (`harm-avoidance-to-third-parties`) | short (`third-party-harm`) | full, matches (a) |

### The record's own warning text

`SFE/behaviours_query.json:2` — the split's rationale, verbatim:
> `"_comment": "QUERY-SIDE ONLY. Behaviour name and definition are legitimate tool inputs. The panel labels are the answer key and must never be reachable from the query path. They lived in one file, which put a leak one line away and made it invisible to every test. Split so the leak is structurally impossible, not merely forbidden. See test_no_reference_leak.py."`

`SFE/behaviours_query.json:3` — `"_source": "derived from the panel file; definitions only"`

`SFE/test_no_reference_leak.py:16-17` (why the substring guard was insufficient):
> `\`import benchmark\`, \`load_panel\`, \`pair_targets\`, \`reference(\`, \`judge_set\`,`
> `or simply opening \`behaviours.json\`. Nothing about reading the answer key`
> `requires a network call.`

`SFE/test_no_reference_leak.py:92-93`, and the laundering-path warning at `:102-108`:
```python
FORBIDDEN = (
    "behaviours.json",      # the panel file itself
    ...
    # LAUNDERING PATHS. panel_universe legitimately reads behaviours.json to
    # rebuild the evaluation universe, so a query module importing it reaches
    # the answer key WITHOUT naming any token above. A reviewer did exactly
    # that in ~15 lines and moved the structural headline +0.340 -> +0.611,
    # past the judge bar, with all 808 tests passing.
    "panel_universe",
```

`SFE/panel_v2.py:11-15` — which file is the bar:
> `It is **NOT a new bar.** Its judges are \`gpt-mini\`, \`haiku\`, \`qwen-small\` —`
> `small models. The question the project is actually asking is "is this tool as`
> `good as just asking a FRONTIER model", and the frontier panel`
> `(\`behaviours.json\`: sol / kimi / fable / opus / kimi-k2) remains the only thing`
> `that answers it.`

`SFE/CYCLE5_REVIEW.md:30` records a live violation:
> `   validate_behaviours.py opens data/behaviours.json (FORBIDDEN). House the`

**Confirmed today**: `SFE/validate_behaviours.py:19` still reads `PANEL = os.path.join(..., "..", "data", "behaviours.json")`. `SFE/MODULE_MAP.md:212` files it under §7 *Superseded* (`| \`validate_behaviours.py\` | \`conflict_output.validate\` | |`) but it is still on disk and still opens the answer key.

The repo README (`README.md:145-146`) also carries a warning that the two files are not interchangeable; per instruction I did not read it.

---

## 15. `PRUNED.md`

Path: `walkthrough/paper_pipeline/phase_1/resolve_runs/graph_v2/PRUNED.md`, 135 lines. This is arc-2 infrastructure, cited from `ARTIFACTS.md:20` — `| Prune manifest | What was removed at publication, pinned by git object id | … | what was removed and how to restore it |`.

### What it lists (verbatim, `PRUNED.md:1-9`)

```
# PRUNED.md — evidence-prune manifest (2026-08-30)

Everything below was removed from the working tree at publication prep to keep
the repo reviewable. NOTHING IS LOST: full git history is retained, and each
entry pins the exact content by git object id (tree/blob sha at the pre-prune
commit). To restore any entry: `git checkout <pre-prune-commit> -- <path>`.
Reason per entry: superseded iteration runs, repair-stage intermediates, or
regenerable caches; the certified artifacts (ds7_production, the cited
translation runs, all behavior_pilot evidence) are retained in full.
```

### How entries are identified

Four-column table, header at `PRUNED.md:11-12`: `| path | git object id | files | bytes |`. **87 entries** plus a `**TOTAL**` row (`PRUNED.md:100`) — `**9801**` files, `**173,154,896**` bytes — and a `**Net after the post-prune restore (below)**` row (`:101`) — `**~7,778**` files, bytes `—`.

Each entry is a repo-relative path plus a 40-hex git tree/blob sha. **Two entries have no sha**, carrying the literal string `untracked-or-file` with `0` files and `0` bytes:
- `PRUNED.md:73` — `| walkthrough/.../runs/ds7/inflight | untracked-or-file | 0 | 0 |`
- `PRUNED.md:99` — `| semi-formal-experiment/HARNESS_REDESIGN.md.presplice | untracked-or-file | 0 | 0 |`

For these two, the manifest's own restore recipe (`git checkout <pre-prune-commit> -- <path>`) cannot work — the content is genuinely gone. The manifest's opening claim `NOTHING IS LOST` is therefore not true of all 87 entries; it holds for the 85 with object ids.

### Signature / checksum / signer

**No signature, checksum, or signer line exists in `PRUNED.md`.** I searched the full 135 lines. Specifically absent:
- no `signed_by` / `signer` / `by:` field;
- no sha256 or checksum over the manifest itself;
- no pre-prune commit id is named anywhere — the restore instruction says `git checkout <pre-prune-commit> -- <path>` (`PRUNED.md:6`) with `<pre-prune-commit>` left as an **unfilled placeholder**, so the manifest does not identify the commit its own object ids are relative to;
- no date beyond the title `(2026-08-30)`;
- the only integrity mechanism is the per-entry git object id.

This contrasts with the cycle artifacts, which do carry signature lines — e.g. `SFE/cycles/patient-pricing-2026-08-04/decision.json:210`: `"signed_by": "session coordinator (Claude), on Matt's standing authorization for the reviewed portfolio order"`, and `SFE/cycles/versioned-cut-2026-08-04/review_verdict.json:3`: `"by": "adversarial review seat (agent)"`. `SFE/HANDOFF.md:266-267` names the gap as known debt in arc-1 too: `R1–R3: conftest registration outside any manifest; **sign-offs as attestation-in-text rather than signed artifacts**; scope check should harden to \`live == frozen − licensed\`.`

### The self-correction it carries

`PRUNED.md:110-114`:
> `**Restored post-prune (load-bearing for tests), 2026-08-30.** The first pass`
> `over-pruned: the entries below are read at test time, so removing them turned`
> `the walkthrough suite red. Each was restored from the pre-prune commit at the`
> `exact path and content the loader reads — no test was weakened, and the run`
> `directories they live in remain pruned except for these files.`

Restored: 1,973 `l*.{json,lp,version.json}` node modules + 34 `run.json`/`concepts.json` (5.5 MB + 3.1 MB), and 16 files of four named `repair_graveyard` arity-defect instances. `PRUNED.md:120-121` records the blast radius: `Pre-prune \`gather()\` selected 762 nodes; post-prune it selected 66.` — a 91% silent data loss caught only by a red suite.

Retention list at `PRUNED.md:103-108`; the population-floor guard at `:133-135` (`\`scanned > 100\` population floor (71 stored modules post-prune, ~800 with the corpus back)`).

---

## 16. Summary of self-conflicts found (unresolved, as instructed)

1. **Which HANDOFF block is current** — ⭐⭐⭐⭐ (2026-08-06) vs the nested ⭐⭐⭐⭐⭐ (2026-08-18). `SFE/HANDOFF.md:3` vs `:5`.
2. **Is MCC the metric** — `NOT MCC` (`:61`) vs `Use MCC as the primary metric` (`:592`).
3. **Is MCC robust to true negatives** — `False as applied` (`:488`) vs `It is also sensitive to true negatives, which is deliberate` (`benchmark.py:671`).
4. **849/863** — `**Do not quote 849/863**` (`MODULE_MAP.md:54`) vs four live quotations in `HANDOFF.md` (`:529`, `:1287`, `:1328`) and the tool still printing it unchanged.
5. **Tool in-sample MCC** — benchmark's own preamble says `+0.274 published / +0.320 true`; its own computed table in the same run says `+0.219 / +0.278`.
6. **Tool→judge gap** — `0.119 → 0.236` (`HANDOFF.md:482`) vs `0.120 -> 0.235` (benchmark preamble).
7. **`DEFAULT_THRESHOLD`** — described as live in benchmark preamble item 5 vs `retiring \`DEFAULT_THRESHOLD = 0.18\`` (`HANDOFF.md:836`).
8. **`check_model.py` check count** — `three independent checks` (`machine/README.md:104`) vs `the validator: 4 checks` (`:16`) vs 4 PASS lines in the output.
9. **`facts.lp` fact count** — `281 facts … 955 more` (`machine/README.md:47`) vs 282 / 964 measured.
10. **`HARNESS_REDESIGN.md` scan status** — `excluded entirely` (`machine/README.md:86`) vs `EXCLUDED = {}` (`machine/scan.py:41`) and 20 scanned facts from it.
11. **Brief/seat count** — 11 (`briefs/README.md`) vs 12 (`ls`, `query.py seats`) — recorded as `d(brief_count,…)`.
12. **Cycle count** — `7 cycle dirs, 5 of them closed … 2 open` (`MODULE_MAP.md:121`, `HANDOFF.md:249`) vs 7 dirs / 6 closed / 1 draft on disk.
13. **Expert anchors** — `Two expert core-passage anchors` (`HANDOFF.md:426`) vs `**4 core-passage anchors** … "Two anchors" was a miscount` (`MODULE_MAP.md:133`).
14. **Chain-audit tally** — `97 correct, 11 agent_missing, 1 unlicensed` (`HANDOFF.md:403`) vs `97 correct / 12 repaired` (`cycles/decoration-blind-join-2026-08-04/assignments/review.md:10`).
15. **Suite count within one decision** — 2128 (`decision.json:74`) vs 2129 (`:86`).
16. **Clause count** — 593 / 589 / 587 / 586 all in play, relation never stated.
17. **`validate_behaviours.py`** — filed as superseded (`MODULE_MAP.md:212`) and flagged FORBIDDEN-violating (`CYCLE5_REVIEW.md:30`), yet still on disk still opening `data/behaviours.json`.
18. **`section.py` `-0.143`** — retracted at `:480`, still asserted at `:82` and `:326`; the ASP model detects this as `contradiction(retracted_claim_still_asserted_in_same_file,"-0.143","section.py")`.
19. **Ship `section@any_atom` vs what the loop runs** — `**⚠️ FLAGGED UNRECONCILED**` (`HANDOFF.md:1259`), explicitly left open.
20. **`PRUNED.md` `NOTHING IS LOST`** vs two `untracked-or-file` entries and an unfilled `<pre-prune-commit>` placeholder.
21. **`measure_join.py`'s misses "by name"** — prints only `unmatched[:10]` of 14, quote-prefix only, undisclosed.
22. **`CYCLE_DESIGN.md` phase list** — recorded as `d(census_in_default_phases,…)`: CENSUS is phase 6 in prose, checkpoint-shape-only in `PHASES_BY_SHAPE`.
23. **`d(predict_targets,…)`, `d(f5_stale_rationale,…)`, `d(side_cause_independence,…)`** — three further prose-vs-code disagreements the machine records itself.