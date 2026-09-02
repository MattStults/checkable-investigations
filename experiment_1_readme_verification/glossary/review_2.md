<!-- Clean-context closure and leakage check of the revised glossary at commit c17f96b. Reviewer: general-purpose subagent, model opus. Committed untouched. -->

I verified everything against the target repo at `48e66ce0` (656 commits, clean checkout, HEAD subject "README: publication links and CI badge filled").

---

# A. Closure of `review_1.md` findings

## §1 Fidelity

| # | Status | Closing text / gap |
|---|---|---|
| 1.1 raw tier merges two senses | **partially closed** | `glossary.md:9` now reads "CONFLICT in the record, resolved only by field name (rule 1)" and names both senses with cites. The *conflict* is closed. But **"rule 1" is a dangling pointer**: the decision procedure it names is not in `glossary.md` (see A-§4.1/4.2 and finding B-1 below). |
| 1.2 criterion standing pre-strikes 71% | **closed** | `:100` now records both record positions verbatim and directs `supersession.status=contested`. I confirmed `BP/GENERALIZATION_PREREG_DRAFT.md:81-84` reads "is STRUCK 2026-08-21" and `BP/HANDOFF_CURRENT.md:210-211` reads "must be sourced or struck". |
| 1.3 check_model cite | **closed** | `:296-298` cite `:98` ("## The validator: three independent checks") and `:16` ("the validator: 4 checks"). Both verified. |
| 1.4 join-rate miscite | **closed** | `:246` cites `SFE/measure_join.py:85-87`; verified those are the `unmatched[:10]` / `[:100]` lines. |
| 1.5 cycle hazard | **closed** | `:278` now splits the two cites and quotes "drafts, pre-OPEN, not live work", giving three states. |
| 1.6 uncited conflicts | **partially closed** | Helpfulness half: closed — `:112` now carries all four file cites and `BP/ROUND4_PREREG.md:150-161` (verified: line 150 = "E1 — CANARY ATTEMPT 1 VOIDED"). MCC half: **not closed**. `:199` quotes benchmark.py "item 5 … is a CEILING" but the entry's cite list gives `SFE/benchmark.py:661-684` — that is the `mcc()` docstring. The quoted preamble is at **`benchmark.py:1698-1706`**. Worse, the other side of the conflict, `+0.219`, occurs **nowhere on disk** (`grep -rF "+0.219"` = 0 hits outside README, which also lacks it); it is a live-run output with no locator and no wall clock. |
| 1.7 node-count conflict | **closed** | `:168` gives 773 / 593 root-unwind / 183 translated with both cites. |
| 1.8 asserted metric identities | **closed** | `:23` and `:42` now say "the record does not state these are one metric — carry the field name from the file". |
| 1.9 off-by-one | **closed** | `:51` cites `:153`; verified ("P4 FAILED (decline_correctness 0.60 …)"). |
| 1.10 panel-v5 scope | **closed** | `:143` "9 behaviours × both specs …, 589 Model Spec passages in the review's cut". |
| 1.11 uncited 374 / 1,336 | **partially closed** | 1,336: closed (`:313` cites `SFE/HANDOFF.md:618`, verified "4008 verdict lines, 1336 passages"). **374: a wrong cite was added.** `:165` says "374 constitution per SFE/HANDOFF.md:469-486"; `374` does not occur anywhere in lines 469-486. Its only occurrence in that file is **`SFE/HANDOFF.md:890`**. |
| 1.12 render.py footer overclaim | **closed** | `:442` reworded to "line-bound check only; support is not machine-verified". |

## §2 Sufficiency

2.1 separability/null — **closed** (new entry `:374-386`, with the BINDING METHOD RULE quoted; I confirmed the rule text at `BP/RETRANS_REVIEW_DISPOSITION.md:66` and `BP/L1L2_ADVERSARIAL_REVIEW.md:121,151`).
2.2 engine failure — **closed** (new entry `:388-395`, with `refusal | wrong_answer | unstated`).
2.3 `finding(r)` — **closed** (`:178` lists UNSUPPORTED / DOES-NOT-LICENSE / "satisfiable by noise" / "at base rate" / "null-free" / "no null" / BLOCKING / upheld as verbatim-carried words). Note: no mapping to the inventory's `null_dominated`; the glossary correctly leaves that to query time.
2.4 decisive finding — **closed** (`:178`, with the `ITERATION_NOTES.md:836-838` and entry-0043 quotes).
2.5 close events — **closed** (`:128` enumerates 0005/0010/0014/0023/0024/0034/0038 and the `ITERATION n, STEP k` form with its 0001-0014 domain).
2.6 `status(b)` — **closed** (`:137` "record the span's own class word verbatim in a status field").
2.7 headline overloaded — **closed** (`:438`, three senses).
2.8 hit/reason — **closed** (new entry `:397-404`).
2.9 `CLAUDE.md → AGENTS.md` — **closed** (`:424`).
2.10 CI entry — **closed** (new entry `:406-410`).

## §3 Leakage

3.1 "the loop iterated against" — **closed**; phrase gone, `:91` uses the record's "CRITERION STANDING (in-sample, all-truth)" and `satisfiability_census.truth_all()`.
3.2 "misses printed by name" — **closed**; `:246` states the record behaviour only.
3.3 Q04 operationalisation — **closed**; `:85` now ends "copy the name the span uses verbatim".
3.4 Q32 three-part negation — **partially closed**; `:323` describes positive shape and adds "do not summarise what it lacks", but still asserts one lack ("`<pre-prune-commit>` unfilled") — that is the record's literal text, so it is defensible, but see B-9.
3.5 tier-enum provenance — **closed**; `:3` final sentence added.
3.6 "28 terms" — **closed**; `glossary/README.md:12` says 34, and `glossary.json` holds exactly 34 entries.

## §4 Translator usability

**4.1 arc-2 handoff disposition rule — NOT CLOSED. 4.2 `adjudicated` decision procedure — NOT CLOSED.** Both were written, but into `glossary.json`'s `tiers._note`, and `render.py:52` skips any key starting with `_`:

```python
for k, v in d["tiers"].items():
    if not k.startswith("_"):
```

The rendered `glossary.md` — the **only** file translators receive — contains no decision procedure at all. See B-1/C.

4.3 human markers — **closed** (`:12`, full marker set incl. post-redaction role language).
4.4 cove mechanical — **closed** (`:17`).
4.5 attended-by-convention — **closed** (`:123`, "BY EXPERIMENT CONVENTION with inferred=true").
4.6 `sources/§N` authority pointers — **closed**; no entry cites `sources/` any more (only the provenance sentence at `:3` mentions the directory).
4.7 engaged-precision denominator — **closed** (`:27`, "copy the `n_engaged`/`n_not_engaged` field … verbatim").
4.8 ambiguous "README" — **closed** (`:252` qualified, plus an `overloaded_words` clause at `:438`).
4.9 unprefixed cites — **partially closed**; `:96` still reads `HANDOFF_CURRENT.md:33-39` with no `BP/` prefix. (`ARTIFACTS.md`, `AGENTS.md` at `:174/:302/:309/:433` are repo-root files and correctly unprefixed.)

---

# B. Leakage, exhaustive

Method: tokenised `glossary.md` and `README.md`, built every 4–8-gram of README **across line breaks** (a per-line scan misses two of the hits below), intersected, then grepped the repo with `--exclude=README.md --exclude-dir=.git --exclude-dir=.claude`. Separately intersected every numeric token. Eleven maximal shared n-grams and 37 shared numeric tokens resulted.

### B-1 [blocking] The translator-facing file has no tier decision procedure at all
Not leakage, but it is the finding that dominates the freeze decision, so it leads. `glossary.json`'s `tiers._note` holds a seven-rule DECISION PROCEDURE; `render.py:52` drops it; `glossary.md:7-17` is a bare enum. `glossary.md:9` then cites "rule 1" — a rule the reader cannot see. Everything in Task C follows from this.
**Change:** render `_note` (or move it to a `_procedure` key rendered as a numbered list under `## Tiers`), and re-run `render.py`.

### B-2 [blocking] "certification ran to completion" — README-only phrase, and it names the distinction the question turns on
- `glossary.md:116`: `'certification ran to completion' and 'certification passed' are different facts`
- README lines 12-13: `raw-match certification ran / to completion on the three tuned behaviors`
- `grep -rF "ran to completion" --exclude=README.md` → **0 hits** in 656 commits' worth of working tree.

Doubly bad: the phrase is the README's, *and* the hazard tells the translator that the completion/passing distinction is the live issue — which is exactly the Q01 sub-claim.
**Change:** replace with record-anchored wording only: "record the `raw_verdict` / `headline_verdict` string verbatim with every round-4 cell (e.g. `BP/ROUND4_DEV_TABLE.json:17` `\"F1 (prec below floor); decl above band\"`)"; delete the completion-vs-passed sentence.

### B-3 [blocking] "History is published unrewritten" — README-only, quoted as record text, and carrying a verdict
- `glossary.md:436` (`history_rewrites` convention): `Consistent with 'History is published unrewritten' except for that message-only amend.`
- README:17: `The full commit history is published unrewritten`
- `grep -rniI "unrewritten" --exclude=README.md` → **one hit, unrelated**: `semi-formal-experiment/test_dechain.py:98` ("unparseable names pass through unrewritten").

The quotation marks present a README sentence as record vocabulary, and "Consistent with … except for" is the *verdict* on the claim under test.
**Change:** keep only the mechanical facts already there — "reflog complete (661 entries); no rebase, filter-branch or force-push recorded; six no-op resets; exactly one amend (HEAD@{416}, message-only, empty diff, orphan 16bbbe59 survives)" — and delete the final clause entirely.

### B-4 [should-fix] "resolves to verbatim text" — README-only phrase, quoted as a term of art
- `glossary.md:402`: `a hit's span 'resolves to verbatim text' only if the node's span carries a quote that is a substring of the spec`
- README:45: `# 1. every claim about a spec resolves to verbatim text`
- `grep -rF "resolves to verbatim"` / `"resolve to verbatim"` `--exclude=README.md` → **0 hits**. The record has only `ARTIFACTS.md:27` "Locator → **verbatim text**" (which supports `glossary.md:329`, not `:402`).
**Change:** drop the quotes and the phrase: "a span's quote is checkable only when the span carries one and that quote is a substring of the source document."

### B-5 [should-fix] "the symbolic engine (ASP/clingo evaluation, conflict enumeration …, satisfiability checks)" — an entry title copied from the README sentence under test
- `glossary.md:388` title: `symbolic engine: ASP/clingo evaluation, conflict enumeration, witness scenario, satisfiability (coherence) check, refusal` — same five items in the same order as README:23-25.
- `grep -rF "symbolic engine"` → **0 hits** outside README. `grep -rF "ASP/clingo"` → **0 hits** outside README. The *components* are record-derived (`run_conflicts.py:2,38`; `checker.py:7-9`; `MODULE_MAP.md:318`) — only the grouping and the two cover terms are the README's.
- Aggravating: the entry's `refusal` vs `wrong_answer` dichotomy at `:393` restates README:25 ("its failures were refusals, not wrong answers"), which is precisely the claim H08 tests.
**Change:** retitle to record vocabulary — "conflict enumeration / witness scenario / coherence check / refusal (arc 1)" — and drop "symbolic engine" and "ASP/clingo". Keep the `refusal | wrong_answer | unstated` kinds (they are the inventory's enum, unavoidable), but delete any framing implying one is the expected answer.

### B-6 [nit] "the vendored harness's" — README wording, thinly supported
- `glossary.md:313`: `engine/panel/behaviours.json = the vendored harness's 11-behaviour catalogue`; README:146 `the vendored harness's own copy`.
- `grep -rniI "vendored harness"` → **0 hits** outside README. `"vendored"` alone appears at `SFE/MODULE_MAP.md:22` ("`engine/`'s vendored suites") and `:265` ("vendored third-party repos"), so the adjective is record-attested for `engine/`, but not the noun phrase.
**Change:** "`engine/panel/behaviours.json` = the harness copy under `engine/` (`SFE/MODULE_MAP.md:22` calls `engine/`'s suites vendored) — 11 behaviours, definitions only, short slugs."

### Cleared on grep (record-supported, no action)
`claim is only as strong as its margin over` + `matched-granularity random-partition null` → `RETRANS_REVIEW_DISPOSITION.md:66`, `L1L2_ADVERSARIAL_REVIEW.md:121,151`, `HANDOFF_CURRENT.md:15`. `at the judge's own false-positive` → `SFE/HANDOFF.md:497`, `benchmark.py:717,806,857`. `the ledger's own` → `G2/EXPERIMENTS.md:4479`, `spend.py:224`. Every shared numeric token is record-attested: `+0.555`/`+0.654` (`structural.py:78`, `section.py:78`), `+0.394` (`HANDOFF.md:481`, `panel_universe.py:32`), `+0.278` (`benchmark.py:3795`), `849/863`/`98.4%` (`MODULE_MAP.md:54`), `299/300` (`RETRANS_REVIEW_DISPOSITION.md`, `ITERATION_NOTES.md:836-838`), `773` + "zero bad spans of 846" (`ARTIFACTS.md:19`), `616` (`MODULE_MAP.md:227`), `1336` (`HANDOFF.md:618`), `16` (`adversarial_review_1.md:39`), `589`, `9/9` (`HANDOFF.md:497`). The single unsupported number is `+0.219` (A-§1.6) — not a README leak, but an unlocatable assertion.

### Sentences that pre-answer a README claim (record-derived words, wrong function)

7. **[should-fix] `glossary.md:287`** — "live run of `SFE/machine/query.py` seats (**12 seats; attribution_author NO VALIDATOR; golden_review none recorded**)". README:59: "note **the seat** it reports as unvalidated" (singular). The glossary hands the translator the run result *and* the fact that there are two differently-marked seats, one of which decides whether the README's singular is right. **Change:** name the two output strings from `machine/query.py:91` (`*** NO VALIDATOR ***`, `(none recorded)`) and say "record the seat names the run prints"; do not name them or state the count.
8. **[should-fix] `glossary.md:293`** — "the validator prints **four PASS lines**" and "it also reports 60 contradictions from `rules.lp` without failing". README:64: "all four checks pass". The conflict framing (README-heading 3 vs README-body 4 vs the run's 4) is legitimate and record-derived; asserting the run outcome is not. **Change:** keep the `:16`/`:98` conflict; replace "the run prints four PASS lines" with "the checker step records the run's PASS lines and wall clock; the translator does not assert the count".
9. **[should-fix] `glossary.md:302`, `:307`, `:402`** — "dangling (no provider) **25**", "quote verification covers only the **602** quoted spans", "**244 of 846** spans carry no quote". README:49 claims "every span checked against the source" and README:45 "every claim … resolves to verbatim text". Stating that 244 spans have no quote *is* the disconfirming answer, supplied before the translator reads anything. **Change:** state what `graph_check.py:55-75` prints as fields ("nodes, bad line ranges / total spans, bad quotes / quoted spans, spans with quotes, dangling, authority-tagged headings") and require a live run for the values; keep `ARTIFACTS.md:19` as the record's own summary but drop the interpretive hazard at `:307`.
10. **[should-fix] `glossary.md:237`, `:267`** — "prints **849/863 = 98.4%** at the pin, wall 9.6 s"; "judge wins **9/9** at the pin". README:53 asserts 98.4%, README:104 asserts nine of nine. Both are record-attested (`MODULE_MAP.md:54`, `HANDOFF.md:497`) so this is not contamination, but the "at the pin" gloss converts a record statement into a confirmed present-tense result. **Change:** attribute rather than assert — "`SFE/MODULE_MAP.md:54` gives 849/863 and forbids quoting it; re-run to obtain the value" and "`SFE/HANDOFF.md:497` states 'Judges beat the tool 9 of 9 cells'".
11. **[nit] `glossary.md:112,115,351,399`** — four "the record does not say / no such file exists / no glossary defines" negatives. Each is checkable and each is also a finished answer. Lowest-risk of the set because none maps to a single README sentence, but `:115` ("no file `round4_help*_scored_raw.json` exists") is one keystroke from a filesystem claim the inventory will want to derive independently.
12. **[nit] `glossary.md:442`** — "see review_1.md". Translators do not receive `review_1.md`, and that file contains README phrases and inventory question ids. Same defect class as review_1 §4.6. **Change:** delete the pointer; the sentence stands alone.

---

# C. Mechanical applicability of the decision procedure

The procedure is not in `glossary.md`. I applied the version in `glossary.json` `tiers._note`, verbatim, in order.

**Span 1 — `BP/ITERATION_NOTES.md:272-275`**
```
- FINAL NUMBERS (raw single-wave vs uniform panel tier):
  attempt-1 transfer 0.40 (frozen) | attempt-2 0.75 raw / 0.70 panel |
  attempt-3 0.40 raw / 0.55 panel. Pooled panel-tier engaged precision
  over both frozen draws: 23/38 = 0.605.
```
**Tier obtained: `raw`, for the whole span.** Rule 1 ("a span saying 'raw' / 'single-wave'") fires on the heading and stops. The 0.70, 0.55 and 0.605 panel-tier figures are thereby mis-tiered. **Judgment required at step 1** — the procedure is keyed to the *span*, but this span carries two tiers on one line, which is the hazard the glossary itself flags at `:35` ("carry attempt AND tier on every value"). There is also a silent rule-1/rule-6 collision: these are ledger-prose figures with no scored artifact named, so rule 6 would say `stated`, but rule 1 pre-empts it. Three defensible answers; the procedure cannot pick.

**Span 2 — `BP/HANDOFF_CURRENT.md:106-108`**
```
- CRITERION STANDING (in-sample, all-truth): caution 0.941, harm 0.953, help
  0.960 under match-or-adjudicated-defensible; raw match 0.81-0.85; the
  human-panelist baseline 71%.
```
**Tier obtained: `raw`.** Rule 1 fires on "raw match 0.81-0.85" and stops, before rule 3 can see "match-or-adjudicated-defensible". This is **Q01's span**, and Q01 expects `panel or adjudicated`. Rule 6 (no scored artifact named in the span) would give `stated`. So the revision has replaced review_1's failure mode (`stated`) with a different wrong answer (`raw`), and review_1 §4.1 is **not closed** — it is now closed-in-JSON and broken-in-order. **Judgment required at step 1.**

**Span 3 — `BP/ITER2_REMEASURE_SCORED.json`, `attempt2.panel_tier`** (`{"engaged_precision": 0.7, "decline_correctness": 0.5}`)
**Tier obtained: `panel`. No judgment required.** Rule 1 does not fire (the object's own name is `panel_tier`; its sibling `raw_wave` is a different object), rule 2 matches `panel_tier*` exactly. This is the case the procedure was written for and it works cleanly.

**Span 4 — `BP/ROUND4_DEV_TABLE.json`, `table["harm-avoidance-to-third-parties"].headline`** (`{"prec": 0.8824, "decl": 1.0}`)
**Tier obtained: `adjudicated`. No judgment required.** Rules 1-2 miss; rule 3 matches the field name `headline`. Correct, and consistent with the file's own header at `:2`. (Note the deliberate consequence: the sibling `raw` object → `raw` by rule 1 even though `:2` defines it as *panel-majority* truth. That is the conflict `glossary.md:9` documents, so it is intended, not a defect.)

**Span 5 — `SFE/HANDOFF.md:480-481`**
```
> | tool @0.18 (in-sample) | +0.274 | **+0.320** |
> | judges (mean of 3) | +0.394 | **+0.555** |
```
**Tier obtained: `stated` — with two judgment calls.** Rules 1-5 all miss: rule 2's triggers are arc-2-only ("3-instance panel", "panel majority", "uniform panel tier"), so an *arc-1 frontier-judge* figure never reaches `panel`, contradicting the `panel` tier's own definition at `glossary.md:10` ("arc 1 = the 3-judge frontier panel per behaviour"). Rule 6 then applies, but only if a **markdown table inside a quoted block counts as "PROSE"** — the procedure says prose, and this is a table. A translator must also decide whether "Reconstructed by `panel_universe.py`" four lines below counts as "the span names the scored artifact"; inside 480-481 it does not.

**Score: 2 of 5 mechanical (spans 3 and 4, both JSON field lookups); 3 of 5 require judgment, and 2 of those 3 return a wrong tier** — including the span the inventory's headline claim depends on.

**Concrete change:** (a) render the procedure into `glossary.md`; (b) make it **value-keyed, not span-keyed** — "assign a tier to each numeric value, from the nearest enclosing JSON field name, or from the label immediately governing that value in prose; never from any other word in the span"; (c) reorder so the prose/artifact test (current rule 6) runs *first* as a gate — if the span is prose and names no scored artifact, tier is `stated` with `provenance_region`, full stop; rules 1-5 apply only inside scored artifacts or where the prose span names one; (d) add an arc-1 trigger to rule 2 ("judges", "mean of 3", "leave-one-out", "per-judge cell") so `panel` is reachable in arc 1; (e) add an explicit tie-break for a span carrying two tier words: emit one claim per value, never one claim per span.

---

# Verdict

**Not fit to freeze.** The revision genuinely closed the two contamination blockers from `review_1` — "the loop iterated against" and "misses printed by name" are gone, the inventory-lifted Q04/Q32 operationalisations are replaced by record-anchored text, and eighteen of the twenty-two should-fix and nit items are properly closed with citations I verified line-by-line against the pin. But it did not close the two structural blockers, and it introduced a third. The tier decision procedure that answers `review_1` §4.1 and §4.2 exists only in `glossary.json`'s `tiers._note`, which `render.py:52` drops from the one file translators actually receive — so `glossary.md:9`'s "resolved only by field name (rule 1)" points at nothing, and a translator holding the frozen artifact has strictly less guidance on tiering than the reviewer assumed. Applied by hand, that procedure is mechanical on only two of five real spans, and on `BP/HANDOFF_CURRENT.md:106-108` — the span Q01 lives on — its rule ordering makes rule 1 fire on the words "raw match" and returns `raw` for figures the record labels match-or-adjudicated-defensible, trading `review_1`'s wrong answer for a different wrong answer. Meanwhile three fresh README-only phrases survived the de-leaking pass: "certification ran to completion" (`glossary.md:116`, zero record hits, and it names the exact distinction Q01 turns on), "History is published unrewritten" (`:436`, quoted as record text and followed by a verdict on the claim), and "resolves to verbatim text" (`:402`) — the first two escaped the earlier review because they straddle a README line break and a per-line n-gram scan misses them. Add the two miscitations that the fix pass created or left (`374` cited to `HANDOFF.md:469-486` when it lives at `:890`; the benchmark "CEILING" preamble cited to `:661-684` when it is at `:1698-1706`, with `+0.219` unlocatable anywhere on disk) and the position is: render the procedure and make it value-keyed, strike the three phrases, fix the two cites, and re-run the cross-line leakage scan — after which I would expect this to freeze cleanly, since nothing remaining is structural.