# Decisions needed from the owner

Seven questions. Only **D1 changes an outcome**; D2–D7 change wording only.
Answer inline (write your answer after `ANSWER:`) or just say "defaults" to
take every recommended option. Full reasoning per item is in
`results/rulings/<id>.md`; nothing here needs you to read those.

---

## D1. Is the walkthrough's ASP link stage part of "the symbolic engine"? (H08, V02)

**README sentence:** "every failure was a refusal, not a wrong answer."

**Why it's asked:** arc 1's engine (checker, conflict enumerator, clingo) has no
recorded wrong answer — its failures are unsatisfiable-definition and dead-rule
*refusals*. But the arc-2 walkthrough's ASP link stage had one: Q-22, where an
unsatisfied `requires` was "silently false in every enumerated situation"
(fixed 2026-08-09, commit 818045f4). Silently false = a wrong answer, not a refusal.
The inventory scoped H08 to arc 1; the README sentence does not say arc 1.

| option | consequence |
|---|---|
| **(a) arc-1 engine only** *(recommended)* | H08 stays **unverifiable**, V02 unverifiable. README needs a scope word: "every failure of the arc-1 engine…". Note the sentence still presupposes a failure census that does not exist. |
| (b) include the walkthrough ASP stage | H08 becomes **contradicted**, V02 contradicted. README sentence is wrong as written and must be tightened or deleted. |

ANSWER: Link stage is part of the symbolic engine.

---

## D2. Does "bounded" count as "withdrawn"? (H06, Q29, V07)

**README sentence:** "it caught and withdrew three headline claims."

**Why it's asked:** two of the three were withdrawn after adversarial review
(the separability census, `bf0d4978`; L1/L2, `365d68b3`). The third — the
query-class saturation claim — was *bounded* by erratum #20, not withdrawn, and
was never in a starred block. The README itself calls it "bounded" in the same
list it introduces as "withdrawn".

| option | consequence |
|---|---|
| **(a) bounded ≠ withdrawn** *(recommended)* | Ruling stands: two withdrawn, one bounded. README tightened to "withdrew two headline claims and bounded a third". |
| (b) bounded counts | Count is still not three-withdrawn (the third was never a headline). Same tightening, plus H06 gains one counterexample. |

ANSWER: Agree.

---

## D3. Was the "no new places" claim ever a headline anywhere? (Q29)

**Why it's asked:** to see if the third item was ever public. `PRUNED.md` lists
4 pruned `blog_drafts` files, restorable from history — the adjudicator could
not check those without knowing if you'd count them.

| option | consequence |
|---|---|
| **(a) no / don't know** *(recommended)* | No change; ruling stands as D2(a). |
| (b) yes, it was a headline | Count becomes 3 headline items (2 withdrawn, 1 bounded). Still not "withdrew three". Wording shifts slightly. |

ANSWER: Agree.

---

## D4. Does "every sampled span" mean the 39 census nodes or the 100 definitions? (Q27)

**README sentence:** "an ontology open-coded from 100 behavior definitions
covered every sampled span."

**Why it's asked:** the record states coverage 39/39 over spans (nodes), in four
places, by two blind seats with zero new coinages. There is **no** coverage
figure over the 100 definitions — the only 100-denominator number is
*separability* 94/100, a different metric. The record uses "spans" for nodes.

| option | consequence |
|---|---|
| **(a) the 39 sampled spans** *(recommended)* | Q27 **verified**. README tightened to name the 39. |
| (b) the 100 definitions | Q27 becomes **unverifiable** — no such measurement exists. README claim would need deleting or re-measuring. |

ANSWER: Agree

---

## D5. What was the 71% "human-panelist baseline"? (Q02)

**README sentence:** rates "0.94–0.96, comparable to the panel's own internal agreement."

**Why it's asked:** the record has **no** measured internal-agreement figure for
the arc-2 panel ("currently unmeasured"), and the 71% comparator was **struck on
2026-08-21** as sourceless. Your testimony (recorded 2026-09-02) is that it was
"a set of cases that I blindly scored" — no artifact of that scoring is in the
repo. The only measured panel agreement is arc-1's, at 0.16–0.62 Jaccard /
0.39–0.50 kappa.

| option | consequence |
|---|---|
| **(a) confirm: blind scoring, no artifact** *(recommended)* | Q02 **contradicted** stands. README comparison clause tightened or deleted. |
| (b) you meant a different figure | Name it and the ruling is redone against it. |

ANSWER: agree

---

## D6. When did arc-1 work actually begin? (Q33)

**README sentence:** arc table row "1 (July–early Aug)".

**Why it's asked:** this repo's first commit is 2026-08-02 (arc 1 arrived as an
import); zero commits before August. Internal dating points at the boundary: a
contract draft dated 2026-07-31, handoff "spec ontology spike (2026-08-01)".
Arc-1 edits also continue to Aug 31, past "early Aug".

| option | consequence |
|---|---|
| **(a) late July, outside this repo** *(recommended)* | Ruling stands (contradicted at the git metric). README tightened to "late July–early Aug; imported into this repo 2026-08-02, edited through Aug 31". |
| (b) give a different start date | Same ruling, your date in the wording. |

ANSWER: agree.

---

## D7. Approve the two blog edits

**Files:** `results/RESULTS_DRAFT.md` holds the proposed text.
Section (A) → `_posts/2026-09-01-readme-verification-pilot.md` (replaces the
"Current status" line and the empty Results section; the design and expectations
sections stay untouched as registered).
Section (B) → `_posts/2026-08-30-checkable-investigations.md` (adds a dated addendum).

**What it says, in one line:** expectation 1 met, expectation 2 not met as
stated, the ledger's re-check was free but wrong until two machinery gaps were
fixed, a frontier reviewer re-checking its own report was correct at ~38% of a
first pass, the record's dependency graph is flat, and the method reads as a
drift guard for a project's own record rather than an investigator's tool.

| option | consequence |
|---|---|
| approve | I apply both edits; D1–D6 answers are folded in first. |
| approve with changes | Tell me what to change. |
| hold | Nothing is published; artifacts stay in the repo. |

ANSWER: agree

---

## After D1–D7

The README disposition commit to the target repo (`semi-formal-document-analysis`)
is a separate approval — proposed per-item wording is in
`results/rulings/SUMMARY.md`. That repo has been read-only for this whole
experiment and stays that way until you say otherwise.
