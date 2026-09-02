# Translator brief — v0.2 (draft, pre-seed)

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

## Provenance

Every claim carries `translator: {model, brief_version, glossary_version,
batch}` exactly as given in your batch header.

## Amendment history

- v0.1 (2026-09-02): skeleton written before seeding; not yet used by any
  translator.
- v0.2 (2026-09-02): stance + refs replace the single supersession link
  (design change D-01, see results/intervention_log.md).
