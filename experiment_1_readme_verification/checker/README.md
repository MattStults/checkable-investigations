# Step 3 — Checker

`check.py` is the mechanical re-check every ledger claim must pass. It is
deterministic, reads the target repo at the pin through `git show`, and never
edits a claim. Output is a PASS/FAIL line per claim id plus a JSON summary;
exit status 1 if any claim fails.

Rules (ledger mode):

1. **Verbatim quote.** `quote` is a whitespace-normalised substring of the
   cited file at the cited commit AND lies within the cited line range. A quote
   found in the file but outside the cited lines fails with its own reason.
2. **Rate re-derivation.** `kind == "rate"` claims carry integer numerator and
   denominator; `value` must equal numerator/denominator rounded to the
   value's own stated precision.
3. **Closed vocabularies.** `tier`, `threshold_rule`, `universe`,
   `provenance_region`, `supersession.status`, `event.type`, `event.actor`,
   `event.context_origin` must be in their enums (see `SCHEMA.md`). Free text
   in an enum field fails.
4. **Declared dimensions present.** Every schema field present; `snapshot`,
   `scope`, `metric`, `venue`, `population` non-empty (`unstated`/`n/a`
   allowed). Event claims carry every event attribute the inventory declared
   (type, timestamp, ordinal for ledger/commit-shaped events, actor set,
   model tier, session, context origin, links, finding, erratum, recurrence,
   caught_by, asserted_transfer).
5. **Stance and refs.** `stance` is in its enum; every ref has a relation
   from the closed set and a non-empty verbatim `target_text`; a non-null
   `target_id` names an existing claim, never self. `resolve_links.py` fills
   `target_id` by logged text matching; translators never do.
6. **Provenance.** Every claim names the translator model, brief version,
   glossary version, and batch.
7. Duplicate ids fail; duplicate content (same source, quote, metric, value)
   is noted, not failed.

Citations mode (`--citations file.jsonl`, entries `{id, path, quote[,
commit][, lines]}`) applies rule 1 only. It is used in step 7 to re-verify
the baseline arm's citations with the same machinery, so both arms report a
machine-checkable fraction from one checker.

`selftest/resolve_log.jsonl` shows the resolver's basis for its one fixture
ref. `selftest/claims.jsonl` holds 8 fixture claims (2 valid, 6 each violating one
rule); `selftest/citations.jsonl` holds one good and one bad citation.
Expected: 2 pass / 6 fail and 1 pass / 1 fail. `selftest/expected_output.json`
is the checker's JSON for the fixture at commit time.

```
python3 check.py selftest/claims.jsonl
python3 check.py --citations selftest/citations.jsonl
```

The checker fires before the ledger exists: the registered expectation that
"the mechanical checker rejects at least one translated claim" is counted only
over real translator output, never over these fixtures.
