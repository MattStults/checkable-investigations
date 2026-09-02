# Translator brief — v0.7

You translate spans of a project record into atomic claims. You are one of
several translators; you see only this brief, the glossary, and the spans
assigned to you. You do not know what the claims will be used for, and you
must not guess. Copy what the span says; never infer, summarise, or resolve.

## Your inputs

1. This brief.
2. `glossary.md` — definitions of the record's own terms, a closed tier
   enum with a decision procedure, and the record's conventions. Where the
   glossary lists a conflict, the record itself disagrees; you translate each
   side as its own claim and never pick.
3. A batch file of spans. Each span is: a repo-relative path, a commit
   (40-hex or `pin`), a 1-based inclusive line range, and the verbatim text
   of those lines. The text is the only content you may quote from.

## Your output

One JSON object per claim, one per line, in the schema below (identical to
`checker/SCHEMA.md`). A mechanical checker rejects any claim whose quote is
not a verbatim substring of the span within its line range, whose rate does
not re-derive from its numerator and denominator, whose enum fields are
outside the enum, whose event object lacks any attribute, or whose refs
carry a relation outside the enum. Rejected claims come back to you with
the reason; you fix and resubmit.

## What is a claim

One atomic thing the span asserts:

- **value**: a named quantity with one value (a score, a count, a date, a
  hash, a threshold).
- **rate**: a value stated as or derivable from a fraction. Carry numerator
  and denominator as integers from the span; if the span gives only a
  decimal, kind is `value`, not `rate`.
- **event**: something that happened, was ruled, was registered, was
  withdrawn, was reviewed, was re-derived, was redacted. Every event carries
  the full event object.
- **existence**: a file, symlink, field, or marker exists (or the span says
  it does not).

A span with three numbers yields at least three claims. A span with a
number given at two tiers ("0.75 raw / 0.70 panel") yields two claims, one
per tier, each with its own quote. A span that restates a number from an
earlier entry yields a claim whose `stance` comes from the span's own words
and whose `refs` carry a `restates` ref with the entry or value named as the
span names it.

## Rules

1. **Quote verbatim.** `quote` is copied from the span text, whitespace
   aside. Do not paraphrase, do not join fragments from different lines
   unless they are adjacent, do not add ellipses.
2. **Never fill a field you cannot read off the span.** Write `unstated`.
   `unstated` is a correct answer; a plausible guess is a rejected claim.
3. **Tier by the decision procedure**, not by sense. Apply the glossary's
   numbered steps in order and stop at the first that matches. Put the
   instrument's name in `venue`.
4. **Snapshot is the record's own index**: entry number, attempt index,
   file name, commit, or date, copied from the span. For a pooled value
   write `pooled:` followed by the set the span pools.
5. **Population is the span's own count**: copy `n_engaged`, `20+20`,
   `32/122`, `all 80 nodes`, exactly as written.
6. **Scope is the behaviour, spec, universe, or directory the span names.**
   If the span names a class word (tuned, dev, never-consulted), copy it
   into `notes` as `status: <word>` as well.
7. **Stance from the span's words only.** `stance` is what THIS span says
   about the value: `superseded` if the span says a later value replaces it;
   `struck` if the span says struck; `contested` if the span records two
   rulings on one thing; `current` if the span presents it as standing;
   `unknown` otherwise. You never know what other spans say, and you must
   not try to.
7a. **Refs for anything the span says about another value or event.** When
   the span refers to something outside itself ("the 71% anchor is STRUCK",
   "supersedes the 12% registration", "0041 WITHDRAWN", "re-derived by the
   driver"), add a ref with the relation word and `target_text` = the words
   the span uses for the target, verbatim. Leave `target_id` null. One ref
   per reference; a span may carry several.
8. **Anti-rule**: if the span or the glossary marks this value do-not-cite,
   copy the marking text into `anti_rule`.
9. **Events**: `actor` is the set of parties the span names by role (owner,
   driver, seat, panel, reviewer, script). A first-person confession that
   names no other party is `["driver"]` with `caught_by.set=["self"]` and
   `caught_by.inferred=true`. `links` are the entry numbers, commit hashes,
   file names, node ids, and finding ids the span mentions, verbatim.
   `erratum.class` is the span's own words for what went wrong (the
   coordinator canonicalises later); `erratum.n` is the number if the span
   gives one, else null. `asserted_transfer` is any "next agent must know"
   style sentence, copied.
10. **Never merge**: two values with the same number at different attempts,
    tiers, or universes are two claims.
11. **Never resolve**: if a span records two rulings on one thing, translate
    both as separate claims, each with stance `contested` and a ref
    `contradicts` naming the other in the span's own words.

## Granularity and shape (learned from seed batch 1)

12. **One claim per assertion, not per span.** A ledger entry yields one
    `ledger_entry` event for its heading plus one claim per bullet-level
    assertion: each number, each rule, each thing that happened. A bullet
    with a count and two node ids yields three claims.
13. **Standing rules and conventions** ("EVERY step ... appends a dated
    entry", "NEW BINDING RULE: ...", "highest-precedence truth") are events of
    type `registration`, actor `unstated` unless the span names who ruled.
14. **Voided** dispatches, seats, measurements → event type `withdrawal`
    with `finding` beginning "voided:".
15. **Ledger entries**: `ts` = the heading date; `ordinal` = the entry
    number; `session` = "entry NNNN". Sub-events inside an entry inherit the
    entry's ts and ordinal unless the span gives another date.
16. **Handoff starred block**: values in the first star-marked heading block carry
    `provenance_region` = `starred_block`; below it, `archive_block`;
    everything else `body`. Document-sourced events carry `ordinal` null.
17. **JSON header strings** (the `"_"` field of a scored file) are prose whose
    named scored artifact is the file itself: proceed past Gate B with the
    label the header attaches to the value.
18. **Git log spans**: `event.type` `commit`, `ordinal` = the `ordinal` line,
    `ts` = the date line, `session` = "commit <8 hex>". `actor`: the
    `author` line is `owner`; a `Co-Authored-By` model trailer adds `driver`
    with `model_tier` = the trailer's model name verbatim. Events named in
    the subject or body (a cycle close, a review verdict, a prediction
    score) are separate claims linking the full hash, and they INHERIT the
    commit's `ordinal` and `ts` (as sub-events of a ledger entry inherit the
    entry's, rule 15) unless the body gives another date.
19. **Rates**: `value` = numerator/denominator rounded to at most 4
    decimals; write the fraction the span writes in `population` or
    `notes` if it is not already the numerator/denominator.
20. **Files named in a span** ("GEN_BLOCK1_SCORED.json") are not existence
    claims by themselves; put them in `event.links` or `snapshot`. Make an
    `existence` claim only when the span asserts a file, field, or marker
    exists or does not.
21. **Node ids with votes** ("l3954_4251_n038 2-1") are `value` claims,
    metric "panel vote", tier `panel`; a 2-1 vote carries stance
    `contested`.

## Shapes learned from seed batch 2

22. **Scored JSON objects**: each numeric leaf is one claim; `venue` names
    the enclosing object path (e.g. `raw_wave (attempt2)`); a list of node
    ids is one claim whose metric is the key and whose value is the count,
    with the ids in the quote. Tier by the key walk (rule 2 of the
    procedure): `engaged_precision` → `raw_wave` → raw.
23. **Cycle artifacts** (`decision.json`, `state.json`, `prediction.json`,
    `review_verdict.json`): keys `flip_tallies`, `adjudication`,
    `flip_verdicts*` → tier `adjudicated`; `prediction_check`,
    `prediction.json` → `stated` with snapshot the cycle name;
    `gate.review` / `review_verdict.json` → event `adversarial_review`,
    actor `reviewer`, finding = the verdict string; `decision` /
    `signed_by` → event `ruling`, tier `human` per the signer text.
24. **Do-not-cite markings** ("Do not quote 849/863", "must be re-derived")
    are `annotation` events with a ref `forbids_citation` naming the values
    verbatim; the value itself, when the span states it, is its own claim
    carrying the marking text in `anti_rule`.
25. **A registered condition firing** ("STOP CONDITION fired") is event type
    `trigger`, linking the registration it fired under.
26. **Owner-supplied measurements** ("Matt pasted /usage = 23%") are tier
    `human`: the procedure's step 8 covers values inside ruling blocks and
    values the span says the owner supplied.
27. **Arrows and multipliers** ("−0.027 → +0.308", "2.8x its declared
    bound"): keep the record's rendering as the value string; do not split
    into two claims unless each side carries its own label.
28. **Per-behaviour triples without names** ("212 / 256 / 436 per
    behaviour"): scope is "per behaviour, order unstated" unless the span
    names the order; never take the order from another span or table.
29. **Pre-redaction spans** carry the blob commit in `source.commit` and the
    words "(pre-redaction blob)" in `snapshot`; translate them exactly like
    current spans.
30. **Text in a quoted `>` block** in a handoff is still prose: Gate B.

## Learned from the pilot batches

31. **The source file name is the outermost key.** For the tier walk
    (glossary procedure step 2), after the value's own key and every
    enclosing object key, the file name in `source.path` is the last key
    tried: `round4_caution_scored_raw.json` → `_raw` → raw. Put the file
    name in `venue` when it decided the tier.
32. **Span `context`.** A span whose `context` field says it is a window
    inside a top-level key carries that key as an enclosing key for the walk
    and in `venue`.
33. **One-line spans** that are a single JSON leaf are still one claim;
    `scope` is the node id or key; do not invent a behaviour name.

## Seat inputs (D-09)

34. **Every `seat_dispatch` event carries `event.inputs`**: the list of
    materials the span says the seat received or was denied, copied verbatim
    ("only the packet prompt string plus the recorded content-free tool
    fence", "never shown seat verdicts, panel citations, or queue
    membership", "given ONLY the behavior definition and each node's
    ESTABLISHES + SOURCE TEXT"). Write `[]` when the span names none. Never
    infer what a seat saw from what it produced.

## Provenance

Every claim carries `translator: {model, brief_version, glossary_version,
batch}` exactly as given in your batch header.

## Amendment history

- v0.1 (2026-09-02): skeleton written before seeding; not yet used by any
  translator.
- v0.2 (2026-09-02): stance + refs replace the single supersession link
  (design change D-01, see results/intervention_log.md).
- v0.3 (2026-09-02): rules 12-21 from seed batch 1 (granularity, standing
  rules, voids, ledger/handoff/JSON-header/git-log shapes, rates, files,
  votes). Checker: generated sources resolve under ledger/spans/; ordinal
  required only for ledger- and git-sourced events (D-02).
- v0.4 (2026-09-02): rules 22-30 from seed batch 2; schema gains rel
  `forbids_citation` and event type `trigger` (D-04).
- v0.6 (2026-09-02): rule 18 — sub-events of a commit inherit its ordinal
  and ts (I-07).
- v0.7 (2026-09-02): rule 34 — seat_dispatch events carry inputs (D-09; the
  inventory declared inputs(d) for H04 and the schema had dropped it).
- v0.5 (2026-09-02): rules 31-33 after the pilot; JSON spans re-cut by
  brace depth with window context (D-05).
