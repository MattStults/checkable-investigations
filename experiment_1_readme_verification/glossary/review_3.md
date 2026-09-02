<!-- Third clean-context closure pass on the glossary at commit 60027e7. Reviewer: general-purpose subagent, model opus. Committed untouched. -->

I verified everything against the target repo at `48e66ce04a4d9f06771c42f89cb37b075583c5f6` (read-only; `git log`/`sed` only). Current glossary is the state at `60027e7`; the changed text is `git diff c17f96b..42b5db5 -- glossary/glossary.md`.

---

# 1. Closure of `review_2.md`

## A — items review_2 left partially closed / not closed

| review_2 item | Status | Closing text (verified) |
|---|---|---|
| **A §1.1** raw tier / dangling "rule 1" | **closed** | `glossary.md:9` now reads "**raw** — see procedure step 3; two record senses, both tier=raw, distinguished in venue", and step 3 exists at `:23` and names both senses with cites (`BP/ROUND4_DEV_TABLE.json:2` verified = "Raw = strict panel-majority truth"; `BP/ITERATION_NOTES.md:272` verified = "- FINAL NUMBERS (raw single-wave vs uniform panel tier):"). Pointer resolves. |
| **A §1.6** MCC half (wrong cite + unlocatable `+0.219`) | **closed** | `:211` now reads "SFE/benchmark.py:1698-1706 preamble text ('the in-sample mean MCC (+0.274 published / +0.320 true) is a CEILING') vs the universe-delta table the same script computes at run time (live_run; values recorded by the checker step, not stated here)"; `:218` adds the cite. Verified `benchmark.py:1698` = "5. **THE OPERATING POINT WAS FIT ON THIS PANEL.**", CEILING text at :1701-1702. `+0.219` is gone from the file. |
| **A §1.11** `374` miscited to `HANDOFF.md:469-486` | **closed** | `:177` now reads "374 constitution per SFE/HANDOFF.md:890"; verified `SFE/HANDOFF.md:890` = "(589 model-spec / 374 constitution universes via `panel_universe.spec_passages`)". Cite added at `:186`. |
| **A §3.4** Q32 three-part negation (PRUNED.md) | **not closed** | The PRUNED.md entry is byte-identical to the reviewed version (not in the diff). `:335` still reads "the restore instruction reads 'git checkout \<pre-prune-commit\> -- \<path\>' with **\<pre-prune-commit\> unfilled**". Strict test (wording must have changed) fails. |
| **A §4.1 / §4.2** procedure never rendered | **closed** | `:19-29` "### Tier decision procedure (apply per value, in order, stop at first match)" is in the rendered file. §4.1 (handoff disposition) is answered by step 2's gate; §4.2 (`adjudicated`) by step 5. |
| **A §4.9** unprefixed cite | **partially closed** | `:103` was fixed ("BP/HANDOFF_CURRENT.md:33-39") and `:111` now says "below the starred block of BP/HANDOFF_CURRENT.md" — but `:108` still reads "while **HANDOFF_CURRENT.md:33-39** uses it as the baseline", with no `BP/`. Sole remaining unprefixed non-root cite (a scan of the whole file returns only this one plus the correctly-unprefixed `ARTIFACTS.md`/`AGENTS.md`). **[nit]** |

## B — leakage / pre-answer findings

| # | Status | Evidence |
|---|---|---|
| **B-1** procedure not rendered *(blocking)* | **closed** | `:19-29` rendered; see above. |
| **B-2** "certification ran to completion" *(blocking)* | **closed** | `grep -cF "ran to completion" glossary.md` = **0**. Replaced at `:129` by "record the raw_verdict / headline_verdict string verbatim with every round-4 cell (e.g. BP/ROUND4_DEV_TABLE.json:17 'F1 (prec below floor); decl above band'); do not paraphrase a verdict string" — the exact wording review_2 prescribed. Cite verified: `ROUND4_DEV_TABLE.json:17` is that string. |
| **B-3** "History is published unrewritten" *(blocking)* | **closed** | `grep -c "unrewritten"` = **0**. `:448` now ends "…orphan 16bbbe59 survives). **Translate these as git-tier facts.**" The verdict clause is gone. |
| **B-4** "resolves to verbatim text" *(should-fix)* | **closed** | `grep -c "resolves to verbatim"` = **0**. `:414` now: "a span's quote is checkable only when the span carries one and that quote is a substring of the source document…". |
| **B-5** "symbolic engine / ASP/clingo" title *(should-fix)* | **closed** | `grep -c "symbolic engine"` = 0, `grep -c "ASP/clingo"` = 0. `:400` retitled exactly as prescribed: "conflict enumeration / witness scenario / coherence check / refusal (arc 1 engine)". `:405` reworded so neither kind reads as expected. |
| **B-6** "the vendored harness's" *(nit)* | **closed** | `grep -c "vendored harness"` = 0. `:325` = "the harness copy under engine/ (SFE/MODULE_MAP.md:22 calls engine/'s suites vendored)". Verified `MODULE_MAP.md:22` = "collect `engine/`'s vendored suites". |
| **B-7** seat names/count pre-answer *(should-fix)* | **closed** | `grep -c "12 seats"` = 0, `"attribution_author"` = 0. `:299` = "…SFE/machine/query.py:90-91 prints either '\*\*\* NO VALIDATOR \*\*\*' or '(none recorded)' for a seat with no validator fact; record the seat names and strings the run prints." Verified query.py:90-91. |
| **B-8** four PASS lines *(should-fix)* | **partially closed** | The Definition at `:305` was fixed ("the checker step records the run's PASS lines, contradiction count, and wall clock — the translator does not assert the count"), and the "60 contradictions" assertion is gone. **But the Conflicts bullet at `:308` still ends "…and the run prints four PASS lines"** — the run outcome is still asserted, and it is exactly Q07's `check_count: 4, all_pass: true`. |
| **B-9** graph_check numbers *(should-fix)* | **closed** (with a new cite defect, §3) | `:314` now lists the printed *fields* only; `:319` = "'bad spans' in ARTIFACTS.md:19 refers to the line-range field; the quote field is printed over the quoted subset only". `25`, `602`, `244`, `846`-as-result all gone from that entry. |
| **B-10** "at the pin" glosses *(should-fix)* | **closed** for 849/863 and 9/9 | `:249` = "SFE/MODULE_MAP.md:54 gives 849/863 and forbids quoting it ('Re-run it')…"; `:279` = "SFE/HANDOFF.md:497 states 'Judges beat the tool 9 of 9 cells'". Both source lines verified. (See §3 for the surviving complement.) |
| **B-11** four asserted negatives *(nit)* | **partially closed** | Only one of four went: "no file round4_help\*_scored_raw.json exists and the record does not say why" → `:127` "the helpfulness file names differ from the other two; copy file names exactly as they appear in git ls-tree". The other three survive verbatim: `:124` "Only the first is marked void in the record"; `:363` "no glossary in the record defines 'in-sample' or 'fresh draw'"; `:411` "the record holds no committed per-hit explanation artifact for arc 1". |
| **B-12** "see review_1.md" *(nit)* | **closed** | `:454` = "…support is not machine-verified.)". Only `review_1` hits left in the file are `SFE/adversarial_review_1.md:39`. |

---

# 2. Re-applying the rendered procedure, by hand, in order

Procedure as rendered at `glossary.md:19-29`. Applied per value.

**Span 1 — `BP/ITERATION_NOTES.md:272-275`** (verified text: "FINAL NUMBERS (raw single-wave vs uniform panel tier): attempt-1 transfer 0.40 (frozen) | attempt-2 0.75 raw / 0.70 panel | attempt-3 0.40 raw / 0.55 panel. Pooled panel-tier engaged precision over both frozen draws: 23/38 = 0.605.")

| value | tier | judgment? |
|---|---|---|
| 0.40, 0.75, 0.70, 0.40, 0.55, 23/38=0.605 | **`stated`** (provenance_region = body) for all six | **No** — step 2 fires: ledger prose, span names no scored artifact. Stop. |

This is a clean, determinate answer and it fixes review_2's `raw`-for-everything failure. **But** step 9 — "A value with two labels on one line ('0.75 raw / 0.70 panel') is two claims, one per label" — uses *this span* as its worked example and is **unreachable for it**, because the procedure stops at step 2. A translator following the order emits one `stated` claim where the glossary's own hazard at `:47` demands two.

**Span 2 — `BP/HANDOFF_CURRENT.md:106-108`** (verified: "CRITERION STANDING (in-sample, all-truth): caution 0.941, harm 0.953, help 0.960 under match-or-adjudicated-defensible; raw match 0.81-0.85; the human-panelist baseline 71%.")

| value | tier | judgment? |
|---|---|---|
| 0.941, 0.953, 0.960, 0.81-0.85, 71% | **`stated`**, provenance_region = archive_block | **One**: locating the end of the starred block to choose `archive_block` vs `body`. The glossary supplies the answer at `:111`, so it is judgment the glossary pre-resolves. |

Determinate; no more `raw`. The residue is that step 5 would have given `adjudicated` off the label "under match-or-adjudicated-defensible" that the span *does* carry, and the gate discards it. Q01's declared tier is "panel or adjudicated"; the procedure now yields `stated`.

**Span 3 — `BP/ITER2_REMEASURE_SCORED.json`, `attempt2.panel_tier`** (`{"engaged_precision": 0.7, "decline_correctness": 0.5}`)

Tier: **`panel`** (step 2 does not fire — a scored JSON is none of handoff/ledger/review/disposition; step 4 matches `panel_tier`). **Judgment required at step 1:** "the nearest enclosing JSON field name" is ambiguous between the value's own key (`engaged_precision`, which matches no rule and falls to step 9 → `stated`) and the enclosing object key (`panel_tier` → `panel`). Read the first way, the answer is wrong.

**Span 4 — `BP/ROUND4_DEV_TABLE.json` harm `headline`** (verified `{"prec": 0.8824, "decl": 1.0}`)

Tier: **`adjudicated`** (step 5 on `headline`). Same step-1 key ambiguity (`prec`/`decl` match nothing; you must walk outward). Otherwise mechanical.

**Span 5 — `SFE/HANDOFF.md:480-481`** (verified: `| tool @0.18 (in-sample) | +0.274 | **+0.320** |` / `| judges (mean of 3) | +0.394 | **+0.555** |`)

Tier: **`stated`** for all four, **no judgment** — step 2 explicitly covers "prose **or a table**" in a handoff, which was review_2's open question, and neither line names the scored artifact (`panel_universe.py` appears at :484, outside the span). **Consequence:** the arc-1 triggers review_2 asked for in step 4 ("judges", "mean of 3", "per-judge", "leave-one-out") are **dead for this span** — the gate runs first. They are reachable only inside scored artifacts or live-run output.

**Span 6 — `BP/ITERATION_NOTES.md:556-559`** (verified: "…downgraded 36/77 Opus-relevants overall… THE NUMBER: visible engaged precision is EXACTLY / 32/122 = 0.262 (seal: 38 nodes untouched, single-use). The sample / series that pointed here: 0.60 (n=20 wave) -> 0.45 (corrected) ->")

| value | tier | judgment? |
|---|---|---|
| 36/77, 32/122, 0.262, 38, 0.60, 0.45 | **`stated`**, provenance_region = body | **No** for the tier. **Yes for step 1's label:** "visible engaged precision **is EXACTLY** 0.262" attaches by the word "is", which is not in step 1's closed list (`=`, `:`, `/`, parentheses, table row header). The translator must improvise a label. Similarly "0.60 (n=20 wave)" — the parenthetical gives "n=20 wave", which is *not* one of step 3's triggers (`single-wave`, `wave seat`). |

**Span 7 — `BP/ROUND4_DEV_TABLE.json`, caution `raw`** (verified `{"prec": 0.675, "decl": 0.875}`)

Tier: **`raw`** (step 3 on the enclosing key `raw`), venue = round-4 sense "raw = strict panel-majority truth" (`:2`). **Judgment:** step-1 key ambiguity again, otherwise mechanical. The deliberate raw/panel-majority collision is documented and intended.

**Score: 4 of 7 fully mechanical (1, 2, 5, 6 — all via the step-2 gate); 3 of 7 (spans 3, 4, 7 — every scored-JSON case) need the same step-1 judgment call; 0 of 7 return a tier I consider wrong.** The gate fix works. The cost is that steps 3-5 and 9 are now unreachable for every handoff/ledger prose figure, which is where most of the record's headline numbers sit.

---

# 3. Fresh defects in text changed since review_2

**3.1 [blocking] The procedure has no terminal case for a labelled value that matches no keyword.**
Step 9's fallback is "A value with no label **at all** → `stated`". A labelled value outside the gate's document list that matches no rule 3-8 keyword falls off the end with no tier. Concrete instances: `ARTIFACTS.md:19` "773 nodes, zero bad spans of 846" — `ARTIFACTS.md` is the routing table, not a handoff/ledger/review/disposition, so step 2 does not fire; labels "nodes"/"spans" match nothing; the reader did not run a script, so step 8 misses. **Q05's `node_count: 773` has no tier.** Same for `BP/CALCULUS_RUNBOOK.md:129` "(0.846 self-agreement)" — label "self-agreement", no match, no terminal.
**Change:** rewrite step 9's second sentence as "Any value not matched by steps 2-8 → `stated`."

**3.2 [blocking] The step-2 gate enumerates document kinds instead of stating the test generally, so prereg/runbook/build-spec/routing prose escapes it and gets tiered by keyword alone.**
Gate list: "a handoff, ledger entry, review, or disposition". Not covered: `ROUND4_PREREG.md`, `PREREG_panel_equivalence.md`, `CALCULUS_RUNBOOK.md`, `GENERALIZATION_BUILD_SPEC.md`, `ARTIFACTS.md`, `PRUNED.md`, `SEMANTIC_AUDIT.md`. Worked instance: `BP/CALCULUS_RUNBOOK.md:128-129` "single-wave truth cannot be memoized (0.846 self-agreement)" — if a translator takes the sentence's "single-wave" as the governing label (which step 1 forbids but the wording invites), step 3 tiers a seat test-retest figure as `raw`, contradicting the glossary's own `:171` rule that self-agreement is its own metric.
**Change:** restate step 2 as "if the value sits in prose or a table in **any** record document and the span does not name the scored artifact the value came from…", and list handoff/ledger/review/disposition as examples.

**3.3 [should-fix] Step 8 (`live_run`) sits below steps 3-5, so script output gets tiered by its column heading instead of as a live run.**
A value you produce by running `benchmark.py` under the column "judges (mean of 3)" hits step 4 → `panel` before step 8 → `live_run`; a `measure_join.py` or `*_raw` field likewise hits step 3 → `raw`. Q06 and Q24 both declare `live_run`.
**Change:** move step 8's live_run/git/filesystem clause into the gate at step 2 as a second gate ("if you produced this value by running a script now → `live_run`; record command and wall clock; the label goes in venue"), or state that steps 3-5 set `venue`, not `tier`, for live-run values.

**3.4 [should-fix] Step 9's claim-splitting rule is unreachable for its own worked example.** See span 1 above. Claim splitting is not a tier rule and must not sit inside a stop-at-first-match ordering.
**Change:** promote it to step 1b, before the gate: "A line carrying two labels on one value pair ('0.75 raw / 0.70 panel') is two claims, one per label, whatever tier they end up with."

**3.5 [should-fix] Step 1's attachment list is under-specified in two ways.** (a) It does not cover copular attachment ("visible engaged precision **is** EXACTLY 32/122"), which is how the ledger writes its headline numbers. (b) "the nearest enclosing JSON field name" does not say whether that is the value's own key or the enclosing object key — the difference between `panel` and `stated` on span 3.
**Change:** "…attached by '=', ':', 'is', '/', parentheses, or a table row header"; and "in JSON, take the value's own key, then each enclosing object key outward, and use the first that matches a rule below."

**3.6 [should-fix] New miscitation: `SFE/machine/README.md:190` does not mention an ACCEPTANCE TEST.**
`:305` reads "…and an ACCEPTANCE TEST (:190)". Line 190 is `boundary_dispute_panel_defensible` in the cause-taxonomy section. "acceptance" occurs at `:41`, `:100` ("`check_model.py` (plus the acceptance test):"), `:155`, `:163` ("PASS (\*) ACCEPTANCE TEST"), `:166`. The named checks (a)/(b)/(c) are at `:102`, `:109`, `:125`, and the four PASS lines at `:160-163`. This cite replaced the old `check_model.py:1-40` in the B-8 fix, so it is new. `render.py` passed it because it only checks the line is in range.
**Change:** cite `SFE/machine/README.md:100` and `:160-163`.

**3.7 [should-fix] New miscitation: `G2/graph_check.py:55-75` does not print the fields the entry lists.**
`:314` claims that range prints nodes, uncovered entries, provided names, dangling, nodes with zero needs, spans with quotes, authority-tagged headings, lines covered. Lines 55-75 hold only the bad-line-range / bad-quote / span-size prints (`:63`, `:64`, `:69`, `:70`). The full field set spans **`:39-140`** (`:39` nodes+uncovered, `:82` overlapping, `:98` provided names, `:99` dangling, `:125` zero needs, `:126` spans with quotes, `:131` authority headings, `:140` lines covered). The field list itself is accurate to the file; only the range is wrong. It also omits `:44` duplicate ids and `:121` K1 grounding.
**Change:** cite `G2/graph_check.py:39-140`, and either add the two omitted prints or say "among them".

**3.8 [should-fix] The B-10 fix is undone inside the same entry: `:258` still asserts "14 are unmatched at the pin".**
`:249` was correctly made attributive about 849/863, and `:257` carries the anti_rule. But `:258` states the complement as a present-tense live result — 863 − 849 = 14 — re-supplying the forbidden figure by arithmetic and pre-answering Q06's `join_rate` and its "misses printed by name" half.
**Change:** "…prints 'unmatched (N):' followed by the first 10 unmatched passages with the quote truncated to 100 characters; obtain N from the live run."

**3.9 [should-fix] `:308` still asserts the run outcome the B-8 fix removed from `:305`** — "the run prints four PASS lines". See B-8 above; it is Q07's answer.
**Change:** "SFE/machine/README.md:160-163 shows a sample run with four PASS lines; the checker step records what the run at the pin prints."

**3.10 [nit] `:316` still carries an asserted live-run measurement in the reworded graph_check entry**: "**Authoritative artifact.** live run (wall 0.14 s)". The Definition was made deferential; this line was not.
**Change:** "live run recorded by the checker step (record command and wall clock); CI runs the same command (.github/workflows/ci.yml:35)."

**3.11 [nit] The new `:129` example quotes helpfulness's `raw_verdict` verbatim** — "F1 (prec below floor); decl above band". Correctly cited and record-anchored, but it hands the translator one of the three per-behaviour certification outcomes Q03 asks the query to recover.
**Change:** cite `BP/ROUND4_DEV_TABLE.json:17` as the location of a verdict string without quoting its content.

**Out-of-scope but material (pre-existing, found while applying the procedure):** `:87` and `:173` both cite `BP/CALCULUS_RUNBOOK.md:130-132` for "single-wave self-agreement is 0.846"; `0.846` occurs **only at `:129`** in that file (grepped), and 130-132 is the engaged-set-first acquisition text. **[should-fix]** Change both cites to `:128-129`.

---

# 4. Sufficiency spot-check

A translator holding only `glossary.md` can carry the declared fields for 12 of the 14, with one gap and one systematic tier mismatch.

| item | verdict | entry that carries it |
|---|---|---|
| **Q01** | **gap** | "criterion standing (in-sample, all-truth)" `:101-114` carries metric, scope (via "dev behaviours vs repair-loop behaviours" `:144`), supersession (round-4 cells named as the out-of-sample counterpart), provenance_region (`:111`), and the 71% contest rule. **It has no Denominator / population section**, and the span carries no n — the inventory declares "per-behaviour engaged set size (needed)". Nothing in the glossary routes the translator from `truth_all()` to a per-behaviour count. **Also:** the procedure yields tier `stated` where the inventory declares "panel or adjudicated". |
| **Q04** | ok | "match-or-defensible / match-or-adjudicated-defensible / headline" `:97` names *both* registrations (`ROUND4_PREREG.md:106-113` amendment 1; `PREREG_panel_equivalence.md`) and says "copy the name the span uses verbatim" — exactly what the inventory's CONTESTED clause needs, without picking. |
| **Q06** | ok | "join rate / recall ceiling" `:245-260`: denominator 863 = published universe, anti_rule verbatim, live-run route, and the `unmatched (N):` / first-10 / 100-char print behaviour. Defect 3.8 applies. |
| **Q16** | ok | "engaged precision" `:33-50` (per-venue artifact, copy `n_engaged` verbatim) + "attempt / iteration / block / draw…" `:135` (iter n → attempt n+1) + "raw / panel tier" `:80` + `:146` for the behaviour name (how-to-approach-tradeoffs, attempts 1-4). Attempt-4's quarantine-adjusted companion is flagged at `:48`. |
| **Q17** | ok | "recall against truth / declined nodes panel-relevant" `:67-78`: `panel_tier_misses.not_engaged_FN`, pooled snapshot + attempt set, and the numerator-collision hazard that separates 23/40 from 23/38. Tier via the procedure is `stated`, not the declared `panel`. |
| **Q19** | ok | "separability / matched-granularity random-partition null / base rate" `:386-398`: 300 seeded trials, and `:396` gives the exact stated-vs-cove split the inventory's tier field asks for. |
| **Q24** | ok | "test suite counts" `:345-351`: "The command is the source of truth, not any number in this file", live pytest as the authoritative artifact, `MODULE_MAP.md:237/:246-250` and `HANDOFF.md:455` for the stated side. |
| **Q29** | ok | `overloaded_words` `:450` sense (c) "a 'headline claim' in a handoff starred block or writeup" + `arc2_current_state` `:427` (which block is starred) + `withdrawal_commit_conventions` `:449` ("record which filter produced a list") + `withdrawals_arc2` `:431`. |
| **Q32** | ok | "PRUNED.md" `:333-337`: four-column shape, 87 entries, git object ids, the two `untracked-or-file` rows, the restore instruction, the Restored-post-prune section — all verified against the file (87 data rows at :13-99; `untracked-or-file` at :73 and :99; restore text at :6; restored section at :110). Enough to answer "signed" negatively at query time without the glossary saying so. Carries the A-§3.4 pre-answer. *(Minor: the table has two summary rows — TOTAL at :100 and "Net after the post-prune restore" at :101 — the entry names only TOTAL.)* |
| **Q37** | ok | "seat / validator (machine/query.py)" `:295-301`: both output strings distinguished by meaning, "record the seat names and strings the run prints", no count. Exactly the shape Q37's "distinct, separately reported state" needs. |
| **H06** | ok | `:190` carries the verbatim finding vocabulary (UNSUPPORTED, DOES-NOT-LICENSE, 'satisfiable by noise', 'at base rate', 'null-free', 'no null', BLOCKING, upheld) with no mapping to `null_dominated` — correctly left to query time; `withdrawals_arc2` and `withdrawal_commit_conventions` supply the event enumeration and linkage. |
| **H08** | ok | "conflict enumeration / witness scenario / coherence check / refusal (arc 1 engine)" `:400-407`: `:405` defines the engine-failure event and requires kind from the span's own words as refusal / wrong_answer / unstated, with neither framed as expected. |
| **H11** | ok | `append_only` `:442` and `redaction_marker` `:443`: the single deleting commit `6d01415b`, the three stubs, the marker's only form, the unmarked-edit examples, and `git show 6d01415b^:<path>` for pre-redaction content. *(Note: `:442` already classifies what was removed — "named owner attributions and verbatim quoted speech" — which is H11's second-conjunct answer supplied in advance. Same class as B-11; pre-existing text, so out of §3's scope.)* |
| **H13** | ok | `:190` "decisive finding = a review finding the disposition marks as decisive and re-derives", with both record counts quoted ("the three decisive findings were RE-DERIVED by the driver", `ITERATION_NOTES.md:836-838`; "The four decisive defects", entry 0043) — the inventory itself expects a count per review — plus the `cove` tier at `:17` requiring the actor verbatim and leaving independence to query time, which is H13's `actor(d) ≠ actor(r)` test. |

**Still cannot carry: Q01's denominator.** Everything else is carryable from `glossary.md` alone.

---

# Verdict

**Not fit to freeze — but the remaining work is small and none of it is a re-design.** The revision closed every blocking item from `review_2`: the tier decision procedure is rendered at `:19-29`, `:9`'s pointer now resolves, all three README-only phrases are gone (zero grep hits for "ran to completion", "unrewritten", "resolves to verbatim"), the seat/PASS/span-count pre-answers were made attributive, and both miscitations were fixed to lines I verified (`HANDOFF.md:890`, `benchmark.py:1698-1706`, with `+0.219` removed rather than relocated). Re-applied by hand, the value-keyed procedure with the gate first is a real improvement: four of my seven spans are fully mechanical and none returns a tier I consider wrong, where review_2 got two wrong answers out of five — in particular `BP/HANDOFF_CURRENT.md:106-108` now yields `stated` with a provenance_region instead of `raw`. What blocks the freeze is that the procedure is not total: step 9's fallback only catches values with *no* label, so `ARTIFACTS.md:19`'s 773 nodes (Q05) and `CALCULUS_RUNBOOK.md:129`'s 0.846 fall off the end untiered (3.1), and the step-2 gate enumerates four document kinds rather than stating the test generally, so every prereg, runbook, build-spec and routing-table figure escapes it and is tiered by keyword alone (3.2). Both are one-sentence edits. Below that: step 8 should run before steps 3-5 or live-run values get tiered by their column heading (3.3); step 9's claim-splitting rule must move above the gate or it is unreachable for the very span it quotes (3.4); step 1 needs "is" in its attachment list and needs to say which JSON key it means (3.5). Two new citations that `render.py`'s line-bound check cannot catch are wrong — `machine/README.md:190` has no acceptance test (it is at `:100`/`:160-163`) and `graph_check.py:55-75` prints four of the twelve fields the entry lists (the range is `:39-140`) — plus the pre-existing `CALCULUS_RUNBOOK.md:130-132` for a value that lives at `:129`. Three pre-answers survived their own fixes inside the fixed entries: "14 are unmatched at the pin" (`:258`, which reconstitutes 849/863 by subtraction), "the run prints four PASS lines" (`:308`), and "wall 0.14 s" (`:316`). And one sufficiency gap remains: the criterion-standing entry has no denominator route, so Q01's per-behaviour engaged set size cannot be carried. Fix those, re-run `render.py` and `leakscan.py`, add a support check (not just a line-bound check) for any citation touched, and I would expect a clean freeze; the PRUNED.md `<pre-prune-commit>` sentence (A-§3.4, unchanged) is the only item I would leave to the owner's judgment, since it is the record's literal text.