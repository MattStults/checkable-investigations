<!-- Clean-context adversarial review 2 of the revised claim inventory (commit e57edfd). Reviewer: general-purpose subagent, model opus, clean context, given the revised inventory, review_1.md, the pinned README and read access to the record. Committed untouched. -->

# Adversarial review 2 — revised claim inventory

Read: `inventory.json` (all sections), `inventory.md`, `README.md`, `render.py`, `review_1.md`, `readme_blame.json`; target repo at `48e66ce0` (read-only; `git log`/`show` and file reads only). I re-ran `render.py`'s verbatim check out-of-place: all 94 quoted sentences are verbatim substrings of the pinned README, including the new Q44–Q49.

---

## 1. Closure audit (A1–A19, B1–B20, C1–C12)

### A — README coverage

| # | Status | Closed by |
|---|---|---|
| A1 | **closed** | H12 (`∀h. hit(h) → span ∧ verbatim ∧ reason`), declared dimensions "span locator and whether it resolves"/"reason presence". See N11 for a residual scoping risk. |
| A2 | **closed** | H13 + `cove` in the tier vocabulary and in `caught_by`. Scope drift noted at N14. |
| A3 | **closed in form, defective in content** | Q44 added — but its declared values are wrong against the artifact (N1, blocking). |
| A4 | **closed** | C06 promoted to H15 (but H15 is undecidable as written — N3); Q46 added for the no-network half. |
| A5 | **closed** | Q47 (corpus identity) split out; R03 note retains "and nothing else". I confirmed the split is decidable: `graph_check.py:11` resolves `RAW = .../specs/openai-model-spec/model_spec.md`, so both arcs' corpus is the same file. |
| A6 | **partially closed** | H14 added, but it is circular against the record (N10). |
| A7 | **closed** | Q48 (starred blocks), Q49 (Layout paths), and `misses_printed_by_name: true` on Q06. |
| A8 | **closed** | Q29 scope now: "a withdrawal is 'headline' iff the withdrawn claim appeared in a handoff starred block or in the README"; arc-1 retractions routed to X01. Decidable — both handoffs carry ⭐-marked top blocks (`HANDOFF_CURRENT.md:1`, `semi-formal-experiment/HANDOFF.md:3`). |
| A9 | **partially closed** | `hypothesis_rules.non_vacuity` added and `min_witnesses` set on 12 of 15 hypotheses — H05, H09, H10 are ∀-shaped and carry no `min_witnesses`, and no default is stated (N5). |
| A10 | **partially closed** | `hypothesis_rules.order_relation` gives (date, entry ordinal) / (commit date, commit ordinal). Undefined for cross-source comparisons, which is what H01/H02/H06/H13 actually need (N6). |
| A11 | **closed** | H07 now operationalises "reliably" as certified-or-repeated; Q41's cross-reference is now accurate. Minor wording drift at N18. |
| A12 | **closed** | H06 scope: "arc-2 withdrawals (the sentence's referent). Arc-1 retractions are queried separately under X01 with self and cove as admissible catchers." |
| A13 | **closed** | H03's list conjunct replaced with `∃e. erratum(e,n,_) ∧ numbered(n)`; append-only conjunct is now per-hunk. Confirmed the record's shape: `ERRATUM #` runs #13–#21 only, and the class-vocabulary now carries `errata_facts` saying so. |
| A14 | **closed** | H11 second conjunct (unmarked in-place rewrites), `content class of removed text: operational or substantive (attribution, ruling text, findings)`, plus `hypothesis_rules.history_in_scope`. |
| A15 | **closed** (rule) / **new defect** (round-trip) | H09 gains the mean/best fallback comparanda and `≤`; but `english_in` still says "below" (N4). |
| A16 | **deliberately declined, with a reporting concession** | V03 keeps `providers: []`; the note adds a `record_only` results column. No `record_only` state enters the four-state outcome vocabulary, which is the frozen design's choice, stated as such. Acceptable. |
| A17 | **closed** | V02 need 2: "an enumeration of engine failures exists in the record (else H08 is vacuous and V02 is unverifiable)". |
| A18 | **closed** | V01 need 3 "the bar is defined (definitional provider)" + provider `R07 (definitional)`; R07 note reciprocates. |
| A19 | **closed** | V07 need: "three DISTINCT headline withdrawal events (claim appeared in a handoff starred block or the README)". |

### B — contradiction and issue detection

| # | Status | Closed by |
|---|---|---|
| B1 | **closed** | Q16 `values.series` is now a list of `(attempt, value, tier)` with `tier: PER ELEMENT`; `not_to_be_confused_with: attempt-3 raw 0.40`. Verified against `ITERATION_NOTES.md` 0010 — see §2. |
| B2 | **closed** | Q16 attempt 4 carries `adjusted_value: 0.895`, `adjusted_basis: dispute-class quarantine, same entry`; supersession says the record renders it `0.85/0.895`. Matches 0014 verbatim. |
| B3 | **closed** | `universe` and `anti_rule` dimensions added; Q06 carries the MODULE_MAP §11 do-not-quote text and `universe: published`; `universe` set on Q10, Q12, Q13, Q14, Q15 as asked. |
| B4 | **closed in form, ambiguous in content** | Q04 gains `registration_artifact`; Q45 added. But the discriminator names two registrations that answer oppositely (N2, blocking). |
| B5 | **closed** | Q01/Q03 scope names the three dev behaviours explicitly; Q16 note names how-to-approach-tradeoffs as a repair-loop, not dev, behaviour; Q17 scope likewise. Confirmed by `CALCULUS_RUNBOOK.md:3` "three live iterations on how-to-approach-tradeoffs". |
| B6 | **closed** | Q01 `snapshot: the in-sample criterion standing ... before round-4 certification`, `supersession: the round-4 certification cells ... report both`. |
| B7 | **closed** | Q02 metric now names the task and lists exclusions. |
| B8 | **closed** | `supersession` vocabulary gains `struck`, with the 71% instance pre-declared; Q02 `not_to_be_confused_with` lists it. |
| B9 | **closed (globally), not per-claim** | `provenance_region` added with the global rule "never silently verified"; but only Q01 carries the field. Q02/Q14/Q15 — the other three the reviewer named — do not. Nit; the global rule does the work. |
| B10 | **closed** | `threshold_rule` is a first-class dimension, set on Q12 (`in_sample`), Q13 (`label_free`), Q41 (`record per measurement`), and in H07/H09's declared dimensions. |
| B11 | **closed** | Q14 denominator declares the 3-vs-5 ambiguity; note declares "leave-one-out" as the README's coinage and instructs matching on value + metric family. |
| B12 | **closed** | Q17 `snapshot: pooled over attempts 2 and 3 (both frozen draws)`, `not_to_be_confused_with: 23/38, 24/38`, and the node-vs-passage glossary term in `scope`. |
| B13 | **closed** | `cove` added to the tier vocabulary as "the highest evidence grade in this record"; Q19 tier is `cove ... or stated`. |
| B14 | **closed** | Q25 metric: "the set of entry numbers present equals {0000..0043} (gapless), not merely count = 44". |
| B15 | **closed** | Q27 denominator pre-declares both candidates and says the README binds coverage to the 100 definitions. |
| B16 | **closed** | Q37 metric counts only `*** NO VALIDATOR ***` and declares `(none recorded)` a distinct, separately reported state. |
| B17 | **closed** | Q34 `trigger: push (branches: main) + pull_request`; `workflow_steps: enumerate exactly from ci.yml; the demo path may run cite.py resolve only`. |
| B18 | **closed for Q32, dangling for H10** | Q32 defines "signed" (detached signature / signer-attested checksum / signer line; content-addressed ids do not qualify). H10 still uses the bare predicate with no cross-reference (N16, nit). |
| B19 | **closed** | Q03 gains `certification_outcome_each`, reported under X01. Confirmed the record backs the concern: `ROUND4_DEV_TABLE.json` `"raw_verdict": "F1 (prec below floor)"` (help), `"F1 by ONE node (27/40 vs floor 28)"` (caution). |
| B20 | **closed** | Q09 `supersession: the count was corrected from 15 to 16 by adversarial review 1; a '15-rule' may survive in older prose`. |

### C — forensics

| # | Status | Closed by |
|---|---|---|
| C1 | **closed** | Eight classes added (`skipped_verification`, `stale_registration`, `estimation_model_defect`, `sequencing_measure_after_spend`, `circular_construct`, `invalid_by_construction_registration`, `authority_overreach`, `undocumented_procedure`), and `other` now carries a canonicalisation rule with an intervention log. See §3 for the re-mapping (12/13 clean) and N17 for a blindness caveat on who canonicalises. |
| C2 | **closed** | F01 redefined onto the record's own BLOCK boundary; `context_origin` demoted to "expected: not recoverable; say so"; F01 carries a pre-registered expected shape. |
| C3 | **closed** | `caught_by` is a set; `a first-person confession with no named catcher is recorded caught_by=self with inferred=true`; F03 pre-declares that erratum #16 names no catcher. Precision issue at N12. |
| C4 | **closed** | `history_in_scope` + `forensic.history_note` + F06; forensic attributes translated from both the current file and the pre-redaction blob, labelled by commit. |
| C5 | **closed** | `errata_facts`: "n is optional; unnumbered errata carry n=null and the entry number", plus the #13–#21 scoping. |
| C6 | **closed** | `model_tier where the span states it; for the driver, from commit trailers (git), labelled as such`. Verified feasible: trailers across the full history are Fable 5 (460), Opus 5 1M (104), Opus 5 (14), Qwen (42). |
| C7 | **closed (no change needed)** | `asserted_transfer` retained as declared. |
| C8 | **closed** | `glossary_hazard` now covers `reset`, `block`, and the `seat` two-ontology collision. |
| C9 | **closed** | F07 (attended vs autonomous blocks). Small decidability gap at N13. |
| C10 | **closed** | F08 (registered stop/halt/revert consequences: executed / superseded / surfaced). |
| C11 | **closed** | F09 (defect class vs model tier). |
| C12 | **closed** | F01's question carries the pre-registered expected shape "erratum #21's four instances fall in one block on one date"; F02 scoped to #13–#21 plus the four unnumbered. |

**Score: 41 closed, 6 partially closed (A3, A6, A9, A10, B4, B18), 1 deliberately declined (A16), 3 closed-but-regressed (A15/N4, A4/N3, B4/N2).** No finding is simply ignored.

---

## 2. Regression check

**H03, H07, H09, H11 rewrites.** H03 in==out and decidable given `history_in_scope`; `operational_only(h)` is defined only in H11's declared dimensions, not H03's — cross-reference it. H07 in==out modulo one word: `english_in` says "two **independent** measurements", the rule says `m1≠m2` (distinct). Two rescorings of the same wave are distinct but not independent — say which you mean (**N18, nit**). H11 in==out and now bites on the real behaviour. **H09 fails the round-trip**: `english_in` "The tool's MCC was **below** every individual judge's MCC" (strict), rule and `english_out` "not greater" (`≤`). The rule is the right one ("did not beat" admits ties); the English-in is now the wrong half. **N4, should-fix**: change `english_in` to "was not above any individual judge's MCC (a tie does not beat)".

**H12 — decidable?** Yes for arc 2: `panel_run1/relevance_by_act.json` is committed and each hit is `node_id → [act:polarity reasons]`, e.g. `"l4251_4571_n029": ["respond_with->respond:prefer", ...]` — a reason per hit, and the node id resolves to graph spans. Whether the span is *verbatim* is exactly the interesting question, since only 602 of 846 spans in `root_graph.production.json` carry a quote at all. Arc 1 has `Scorer.explain()` (`semi-formal-experiment/relevance.py:719`, returning `matched_atoms` "with the spans licensing them"), but I found no committed per-hit explanation artifact. H12's scope says "relevance-query outputs **committed** in the record (arc 1)" — as scoped, the arc-1 witness set may be empty and H12 lands `unverifiable (vacuous)` on a scoping technicality while the capability is live-runnable on the demo path (**N11, should-fix**: admit `live_run` output of `explain()` as a witness source).

**H14 — decidable?** Only partly, and it is circular. `CALCULUS_RUNBOOK.md` does define step numbering (`STEP 1 — TRIAGE`, `STEP 2 — MOVES`, `STEP 3 — VALIDATE`, `STEP 4 — REALIZE`, `STEP 5 — RECORD`, `STEP 5b — NOTES`), and entries 0001–0014 carry `ITERATION n, STEP k` headings. But (a) the runbook records no set of steps "having been run", so `english_out`'s quantifier domain does not exist; (b) the only evidence a step ran is a ledger entry, so a step with no entry is invisible and H14 cannot fail — the A9 defect re-instantiated at the level of the witness domain, and `min_witnesses: 1` does not catch it; (c) step labelling stops at 0015; entries 0016–0043 have no step structure, and there is no `ITERATION 4` heading even though the Q16 series has four attempts. **N10, should-fix**: define the step domain from an artifact the ledger does not author — the runbook says each step emits committed artifacts ("Emit the routed queue as a committed artifact before any move executes"; STEP 5 traces are `trace_check.py`-certifiable) — and scope H14 to iterations 1–3.

**H15 — decidable?** No. Repo-wide, the phrase "star artifact" occurs exactly twice: `ARTIFACTS.md:3` "Every star artifact, one line each" and `README.md:159`. The `⭐` glyph is used as prose emphasis throughout (`walkthrough/DEFERRED.md`, `WALKTHROUGH_REPORT.md`, a test docstring) and as a handoff-block marker (`⭐⭐`, `⭐⭐⭐⭐`), never as an artifact designation. So `star_artifact(a)` has no extension outside `ARTIFACTS.md` itself: the hypothesis is either trivially true (star = listed) or unverifiable, and its declared dimension "star marking (where the record marks it)" points at nothing. **N3, should-fix**: either define the star set extensionally at inventory time (e.g. the union of AGENTS.md's reading list, the README Layout block, and the handoff starred blocks) and check ARTIFACTS.md covers it, or replace H15 with the decidable converse — every path in ARTIFACTS.md exists at the pin — and file the coverage half as residue.

**Q44–Q49.** Verbatim: all six pass. Checkability:

- **Q44 is wrong (N1, blocking).** It declares `spans_checked_equals_node_count: true`. The artifact has 773 nodes and **846 spans**, of which **602 carry a quote**; `graph_check.py:63-64` prints `bad line ranges: X / <spans>` and `bad quotes: X / <quotes_total>`, and `ARTIFACTS.md:19` itself says "773 nodes, zero bad spans of 846". A translator carrying Q44 as declared reports a contradiction on the inventory's own arithmetic error and never surfaces the real finding, which is that only 71% of spans have text compared to source. Change values to `spans_total: 846`, `spans_with_quotes: 602`, `bad_line_ranges: 0`, `bad_quotes: 0`, and note that "every span checked" holds for line ranges but for quote-verification only on the quoted subset.
- **Q45** is checkable: `ROUND4_DEV_TABLE.json` has a populated `headline` column for all three behaviours.
- **Q46** is checkable and will verify: no `requests`/`httpx`/`urllib`/`socket` import in `cite.py`, `graph_check.py`, `measure_join.py`, `benchmark.py`, `machine/query.py`, `machine/check_model.py`, `setup_env.sh`.
- **Q47** is checkable and will verify (`graph_check.py:11`).
- **Q48**: half checkable. Both handoffs have ⭐ top blocks. `lower_sections_self_marked: true` is not operationalised — "file structure" is not a criterion (**N15, nit**: define as "every section below the top starred block carries a date or an explicit superseded/archive marker"). Also note arc-1's `HANDOFF.md` has a `⭐⭐⭐⭐` block at :3 and a deeper `⭐⭐⭐⭐⭐` at :5 — say which is "the top starred block".
- **Q49** verifies; all eight paths exist. Unlike Q42 it carries no "representative sentence" note although the quoted sentence covers only one of the eight paths (nit).
- **Q43/Q46 denominator is wrong (N7, should-fix).** Both declare `denominator: 5 commands` / "the five 'Start here' commands". The block has **six numbered steps (0–5) and seven command lines** (step 1 issues two `cite.py` invocations). Also step 3's `cd semi-formal-experiment` must carry into steps 4 and 5, which Q43's scope already notes — so the count matters.

**Q16 against 0010 and 0014.** Attempts 2–4 check out exactly: 0010 reads `attempt-2 0.75 raw / 0.70 panel | attempt-3 0.40 raw / 0.55 panel`, and 0014 reads `ENGAGED PRECISION 0.85 … the quarantine RAISED the adjusted precision to 0.895` and `Attempt series: 0.40 transfer -> 0.70 -> 0.55 -> 0.85/0.895`. **Attempt 1 is over-declared (N8, should-fix)**: the record says only `attempt-1 transfer 0.40 (frozen)` under a header naming two columns (`FINAL NUMBERS (raw single-wave vs uniform panel tier)`), and gives attempt-1 one value, not two. The inventory's `tier: "frozen transfer (raw, single wave)"` is an inference; declare it as "tier unstated in the record; single value under a two-column header" so a wrong-tier match is reportable rather than pre-decided.

**A separate Q16 problem (N9, should-fix):** the per-element tiers — `"frozen transfer (raw, single wave)"`, `"certified-Opus venue"` — are not values of the declared `tier` enum ("One of: raw / panel / adjudicated / human / live_run / git / filesystem / stated" + `cove`). Same for `Q04 tier: "git and ledger"` ("ledger" is not a tier), `Q15 "panel vs tool"`, `Q45 "raw/adjudicated"`. A checker comparing declared tier to record tier cannot do string equality on these. Either extend the enum (add `certified_venue`, `ledger`) or map each free-text tier to an enum value plus a `venue` note.

**Non-vacuity rule — implementable?** Nearly. Two gaps: (a) three ∀-hypotheses (H05, H09, H10) carry no `min_witnesses` and the rule states no default, so a checker has no branch for them — H09 is the one that matters, since its note anticipates an empty witness set but nothing enforces `unverifiable` (**N5, should-fix**: set `min_witnesses` on all three and add "absent ⇒ 1"); (b) "witness set" is undefined — antecedent-satisfying `x`, or `(x, y)` pairs where the consequent was found? The natural reading (antecedent-satisfying events) is the right one and should be written down, because for H03/H10/H11 the ∀ is over hunks/manifest entries, not events.

**Order relation — implementable?** For same-source comparisons, yes: (date, entry ordinal) for ledger, (commit date, commit ordinal in first-parent order) for commits, and an explicit `unverifiable` fallback. But **every rule that needs it compares across sources** (**N6, should-fix**): H01 compares a review (often a standalone `.md`) to a close (a ledger entry); H06 a review document to a withdrawal commit; H13 a `cove` event in ledger 0042/0043 to `corrected_verdicts` in `L1L2_REVIEW_DISPOSITION.md`, which is date-only with no ordinal of any kind. As written those land `unverifiable` by construction. Concrete fix: "an event whose source is a document maps to the ordinal of the commit that introduced its span (`git log -S` / blame), and cross-source order is compared on (commit date, commit ordinal)."

---

## 3. Forensic layer

**Re-mapping the thirteen errata to the extended classes:**

| erratum | entry | class now available | fit |
|---|---|---|---|
| #13 verify contract predictions before freezing | 0017 | `skipped_verification` | ✓ |
| #14 parity certificates are brief-local | 0018 | `scope_stretched_certificate` | ✓ |
| #15 fresh-rulings-per-attempt by inertia | 0019 | `stale_registration` | ✓ |
| #16 stale reset belief | 0025 | `stale_belief` | ✓ |
| #17 cost model missing node-count term | 0026 | `estimation_model_defect` | ✓ |
| #18 measure shelf sources before the spend | 0027 | `sequencing_measure_after_spend` | ✓ |
| #19 coding vocabulary under-specified | 0034 | `underspecified_vocabulary` | ✓ |
| #20 closed-vocabulary circularity | 0037 | `circular_construct` | ✓ (was marginal, now exact) |
| #21 pass condition that cannot fail | 0042/0043 | `unfalsifiable_pass` | ✓ |
| RUNBOOK ERRATUM (first command, first failure) | 0001 | `skipped_verification` (per its own gloss) | **marginal** — the span is `route.py <slug> <node>` KeyErroring because "SC.truth_all's fmap only knows the three round-4 behaviours": a procedure whose coverage assumption was never tested, closer to `scope_stretched_certificate` or `undocumented_procedure`. Assigning it in the gloss pre-decides a coding judgment; drop it from the gloss and let the translator classify. |
| RUNBOOK ERRATUM (STEP 4) | 0004 | `undocumented_procedure` | ✓ |
| MY REGISTRATION ERROR (V5 with zero move coverage) | 0009 | `invalid_by_construction_registration` | ✓ |
| DRIVER ERRATUM (options not mine to offer) | 0013 | `authority_overreach` | ✓ |

**12 of 13 fit cleanly; one (0001) is force-fit by the gloss.** `missing_null`, `wrong_artifact` and `mixed_snapshots` still have no erratum instance, which is fine — they are classes for the non-erratum defects (L2, the behaviours.json trap, tier pooling) and no longer damage F02, since F02 is now scoped to "#13–#21 plus the four unnumbered errata" and `other` has a canonicalisation rule.

**Are F06–F09 answerable from the record's own words?**

- **F06 — yes.** `git show 6d01415b^:…/ITERATION_NOTES.md` versus the pin gives exactly the attribute-loss diff, and `history_in_scope` puts both versions in the span set. The pre/post pair for 0013 (`Matt: "Let's ignore my 'final run' message for now"` → `RULING:`) is a real, findable witness.
- **F07 — yes, with one convention missing.** The record positively marks the autonomous side (`## 0032 — CONSTRAINED-AUTONOMY BLOCK`, `## 0033 — UA ARC (autonomous block)`, `## 0034 — AUTONOMOUS BLOCK CLOSE`) but never marks a block "attended". **N13, nit**: state "a block with no autonomy marker is attended" or F07's independent variable is undefined for two-thirds of the record.
- **F08 — yes.** 0009 supplies the worked example in its own words: `registered consequence = REVERT the batch move. NOT EXECUTED: halt-and-surface`. The redacted budget entries (0002, 0008) are recoverable via `history_in_scope`.
- **F09 — yes, with limited power.** Driver tier is not in any span but is in commit trailers, and those do vary across the history (Fable 5 ×460, Opus 5 1M ×104, Opus 5 ×14, Qwen ×42). Worth pre-declaring the expected shape as F01 does: arc-2, where nearly all errata live, is largely single-tier, so most tier variance sits on the *seat* axis (`Sonnet 0.13, Haiku 0.00 at v1`) rather than the driver axis.

**Is `caught_by`'s inference rule mechanically applicable?** Mostly, but it has a known false positive the revision itself created the conditions to detect. The rule is one clause: "a first-person confession with no named catcher is recorded `caught_by=self` with `inferred=true`". It works on erratum #16 (0025: "The reset I had been scheduling against had already passed; I carried the stale anchor forward"). It fails on 0013, whose current text reads first-person and names no catcher (`two of the three "options" I offered were not mine to offer`) while the pre-redaction blob shows the owner's message triggered the ruling — so a translator reading the published file records `self`, and one reading the blob records `owner`. **N12, should-fix**: (a) define "first-person confession" operationally (the span attributes the defect to its own writer — "mine", "my error", "I carried" — and names no other party); (b) add a precedence rule: where the pre-redaction blob names a catcher or actor the current file does not, the historical attribution wins, both are recorded with their commit labels, and the span is flagged for F06.

---

## 4. New findings

| id | severity | evidence | change |
|---|---|---|---|
| **N1** | **blocking** | `root_graph.production.json`: 773 nodes, 846 spans, 602 with quotes; `ARTIFACTS.md:19` "zero bad spans of 846". Q44 declares `spans_checked_equals_node_count: true`. | Replace Q44's values with `spans_total: 846`, `spans_with_quotes: 602`, `bad_line_ranges: 0`, `bad_quotes: 0`; note that quote-verification covers only the quoted subset. |
| **N2** | **blocking** | `ROUND4_PREREG.md:106` "**DEFENSIBILITY PASS** (project owner's decision, 2026-08-24): round-4 misses receive a pre-declared ONE-PASS blind Fable defensibility adjudication … match-or-adjudicated-defensible"; `ROUND4_DEV_TABLE.json:_` "one-pass defensibility per amendment 1 … headline = match-or-adjudicated-defensible. Both publish." Q04's discriminator says the pass ran "iff a run cites the registration by name (the round-4 prereg / panel-equivalence prereg)". | The disjunction is the whole question: under the round-4 prereg the pass **was** registered and **did** run (contradicted); under `PREREG_panel_equivalence.md` it did not (verified). Name one registration as the referent of "the registered match-or-defensible pass", and declare that "cites the registration" includes citing a registered band or amendment id (`E4`, `amendment 1`), not only a filename. |
| **N3** | should-fix | "star artifact" occurs only at `ARTIFACTS.md:3` and `README.md:159`; `⭐` is prose emphasis elsewhere. | See §2 — define the star set extensionally, or invert H15 to "every ARTIFACTS.md path exists". |
| **N4** | should-fix | H09 `english_in` "was **below** every individual judge's MCC" vs rule `mcc(tool) ≤ mcc(j)`. | Rewrite `english_in` to "not above any individual judge's MCC; a tie does not beat". |
| **N5** | should-fix | H05, H09, H10 carry no `min_witnesses` though all are ∀-shaped; `hypothesis_rules.non_vacuity` says "Every universally quantified hypothesis declares min_witnesses". | Add the field to all three; add "absent ⇒ 1"; define "witness" as an antecedent-satisfying element (event, hunk, or manifest entry). |
| **N6** | should-fix | `order_relation` defines ledger and commit ordinals only; H13 compares ledger 0042/0043 to `L1L2_REVIEW_DISPOSITION.md`, which is date-only. | Add: a document-sourced event takes the ordinal of the commit that introduced its span; cross-source order compares (commit date, commit ordinal). |
| **N7** | should-fix | README "Start here" has steps 0–5 and seven command lines; Q43 and Q46 declare `denominator: 5 commands`. | Correct to six steps / seven commands and enumerate them. |
| **N8** | should-fix | 0010: `FINAL NUMBERS (raw single-wave vs uniform panel tier): attempt-1 transfer 0.40 (frozen)` — one value, two-column header. Q16 declares attempt 1 `tier: "frozen transfer (raw, single wave)"`. | Declare attempt-1's tier as unstated-in-record with the two candidates, so a wrong-tier match reports rather than passing. |
| **N9** | should-fix | Q16 (`certified-Opus venue`), Q04 (`git and ledger`), Q15 (`panel vs tool`), Q45 (`raw/adjudicated`) use tier strings outside the declared enum. | Constrain `tier` to the enum plus an optional free-text `venue`; extend the enum if `certified_venue` / `ledger` are wanted. |
| **N10** | should-fix | H14's quantifier domain ("pairs the runbook defines as having been run") does not exist; the ledger is the only step enumerator; step labels stop at 0015. | Derive the step domain from step-emitted committed artifacts (routed-queue artifact, `trace_check.py`-certifiable traces); scope H14 to iterations 1–3. |
| **N11** | should-fix | H12 scope says "relevance-query outputs **committed** in the record (arc 1)"; arc-1's reasons come from `relevance.py:719 explain()`, with no committed per-hit artifact found. | Admit `live_run` `explain()` output as an H12 witness source. |
| **N12** | should-fix | 0013 current text is first-person with no named catcher; the pre-redaction blob names the owner. | Add the precedence and definition rules in §3. |
| **N13** | nit | Autonomy is marked only positively (0032/0033/0034). | State "unmarked block = attended" in F07. |
| **N14** | nit | H13 `english_in` says "the L1/L2 review"; `scope` adds "ledger entries 0042-0043", and 0042 is the *census* review. 0042 says "the three decisive findings"; 0043 says "The four decisive defects". | Either restrict scope to L1/L2 (0043 + disposition) or widen `english_in`; pre-declare the 3-vs-4 enumeration difference. |
| **N15** | nit | Q48 `lower_sections_self_marked: true`, metric "file structure". | Operationalise: every section below the top starred block carries a date or an explicit superseded/archive marker. Say which block is "top" in `semi-formal-experiment/HANDOFF.md` (⭐⭐⭐⭐ at :3 vs ⭐⭐⭐⭐⭐ at :5). |
| **N16** | nit | H10 uses `signed(manifest(k))`; the definition lives only in Q32's values. | Cross-reference Q32 from H10's note. |
| **N17** | nit | `defect_classes.other`: "the orchestrator canonicalises 'other' entries into a named class at batch review". The orchestrator has read the README; translators have not. | Fine for the forensic layer (not scored against README expectations), but say so explicitly, and log each canonicalisation with the span's original words so the leak is auditable. |
| **N18** | nit | H07 `english_in` "two **independent** measurements" vs rule `m1≠m2`. | Define distinctness as different attempts/draws, or drop "independent". |

---

## Verdict

**Not yet fit to freeze — but the gap is one editing pass, not another round.** The revision genuinely applies review 1: 41 of 51 findings are closed with dimension or rule changes that actually change what a translator carries or what a query decides (the `universe`/`anti_rule`/`threshold_rule`/`provenance_region`/`struck`/`cove` additions, per-element Q16 tiers with 0.895, the Q17 confusion set, the per-hunk H03/H11 rewrite with pre-redaction history in scope, the extended defect vocabulary that now fits 12 of 13 errata, and F06–F09) — and I verified the sharpest of those against the record rather than taking the notes at face value. What blocks a freeze is small and concrete: Q44's declared values are arithmetically wrong against the artifact it checks (846 spans, 602 quoted, 773 nodes), and Q04's discriminator names two registrations that answer the README's most recently added sentence in opposite directions, so the query cannot terminate. Behind those, four should-fixes are cheap and would otherwise burn translation budget on predictable non-answers: `min_witnesses` missing on the three ∀-hypotheses the new rule claims to cover universally, the order relation undefined exactly where the hypotheses cross source types, H15's `star_artifact` having no extension in the repo, and H14 quantifying over a domain only the ledger can enumerate. Fix those six, plus the Start-here command count and the out-of-enum tier strings, and the inventory is defensible to freeze; nothing found here requires re-deriving the inventory's structure.