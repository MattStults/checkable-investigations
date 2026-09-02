# Ledger claim schema

One claim per line in `ledger/claims.jsonl` (JSON object). Every field below
is required unless marked optional; a field the translator cannot fill from
the span's own words is set to the string `"unstated"`, never omitted and
never guessed.

```
id                 "L" + 5-8 digits, unique (batch N ≥ 9 uses N*10000+1 upward)
kind               "value" | "rate" | "event" | "existence"
source             {"path": repo-relative path, "commit": 40-hex or "pin",
                    "lines": "a-b" (1-based, inclusive)}
quote              verbatim substring of source at that commit, within lines a-b
                   (whitespace runs normalised to one space for comparison)
metric             glossary term (string) or "n/a" for pure events
value              number | string | null
numerator          integer | null      (required non-null when kind == "rate")
denominator        integer | null      (required non-null when kind == "rate")
tier               one of: raw panel adjudicated human live_run git filesystem stated cove
venue              free text or "unstated"
snapshot           free text: attempt index / entry number / file / commit / date;
                   "pooled:<set>" for pooled figures
population         what the denominator counts, or "n/a"
scope              behaviour / spec / universe / directory the value is about
threshold_rule     one of: in_sample label_free LOBO oracle training_folds n/a unstated
universe           one of: published true n/a unstated
provenance_region  one of: starred_block archive_block body n/a
anti_rule          text of any do-not-cite marking in the record for this value, or null
stance             the SPAN'S OWN stance toward the value, one of:
                   "current" | "superseded" | "struck" | "contested" | "unknown"
                   (never a judgment about other spans; see refs)
refs               list, possibly empty, of {"rel": one of
                     supersedes restates flags_unsourced strikes withdraws
                     contradicts re_derives amends quarantines forbids_citation,
                    "target_text": the words the span uses to name the thing
                     it refers to, copied verbatim,
                    "target_id": null (filled by checker/resolve_links.py, never
                     by the translator)}
event              null, or for kind == "event":
                   {"type": one of the event types below,
                    "ts": "YYYY-MM-DD" or "unstated",
                    "ordinal": integer entry number / commit ordinal or null,
                    "actor": list of {owner driver seat panel reviewer script unstated},
                    "model_tier": string or "unstated",
                    "session": block name and/or entry number, or "unstated",
                    "context_origin": one of fresh continued compacted seeded_by:<artifact> unstated,
                    "links": list of strings (entry numbers, hashes, file names, node ids the span names),
                    "finding": string or null,
                    "kind": "refusal"|"wrong_answer"|null   (engine_failure only),
                    "erratum": {"n": integer or null, "class": string} or null,
                    "recurrence_of": string or null,
                    "caught_by": {"set": list, "inferred": bool} or null,
                    "asserted_transfer": string or null}
translator         {"model": string, "brief_version": string, "glossary_version": string, "batch": string}
notes              free text (may be empty)
```

Event types: annotation (a span that speaks about another value's standing), trigger (a registered condition firing), cycle_close, iteration_close, adversarial_review, prediction_freeze,
measurement, ledger_entry, erratum, withdrawal, seat_dispatch, certification_run,
registration, commit, prune, redaction, engine_failure, cove, ruling, hunk.

Rules the checker enforces are listed in `README.md`. A claim that fails any
rule is rejected as a whole and returned for retranslation; the checker never
edits a claim.

## Value status is derived, not translated

A value's overall standing (asserted-current, flagged-unsourced, struck,
superseded, contested, restated) is computed at query time from the `refs`
edges pointing at it. Translators record only what their span says; the
graph carries the ambiguity. `checker/resolve_links.py` fills `target_id`
by matching `target_text` against claim quotes and values and logs every
match with its basis; the checker verifies that every non-null `target_id`
resolves and is not self.
