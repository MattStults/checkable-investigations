# Step 2 — Glossary

Metric definitions, measurement tiers and modes, the authoritative-artifact
map, and the record's own conventions, each entry citing the record document
that defines it (`path:line` into the target repo at `48e66ce`). Written
before translation; the README under test was excluded from every source
pass so nothing here is derived from the claims being verified.

Files:

- `glossary.json` — source of truth. Sections: `tiers` (closed enum for the
  ledger's tier field), `entries` (34 terms), `authoritative_artifact_map`,
  `conventions` (ledger format, ordering, append-only history, redaction
  markers, prereg integrity, marking systems, git trailers, history rewrites,
  withdrawal commit conventions, overloaded words).
- `glossary.md` — rendered view.
- `render.py` — renders and fails if any cited `path:line` does not resolve
  in the target repo at the pin (line number within the file's length).
- `sources/` — the three extraction reports the entries cite, committed
  untouched: `arc2_extraction.md`, `arc1_extraction.md`,
  `hazards_extraction.md`. Extractors were Opus subagents with read-only
  access to the record, README.md excluded by instruction. The arc-1
  extraction also ran the deterministic scripts read-only and pasted output
  with wall clock.

What translators receive: `glossary.md` only (with the brief). They never
see `sources/`, the inventory, or the README.

Hazard classes the orchestration named, each confirmed against the record
and encoded in an entry or convention: raw vs panel tier (tiers; 'raw / panel
tier' entry); per-attempt series vs pooled snapshots ('attempt / ... /
pooled'); superseded ledger entries and self-marked stale sections
(`marking_systems`, `append_only`); opposing panel rulings on the same node
(its own entry); in-sample vs fresh-draw certification ('measurement modes',
'certification'); the three differently named behaviours files (its own
entry). Conflicts the record leaves standing are listed under each entry as
conflicts and are not resolved here.

Freeze: on owner sign-off. Later additions go through the brief amendment
history and the intervention log, each as a dated, numbered glossary
amendment appended to `glossary.json` under `amendments`, never by editing
an existing entry.

## Revision after clean-context review (2026-09-02)

`review_1.md` (committed untouched) found four blocking items and applied
here: two phrases that occur nowhere in the record except the README under
test ("the loop iterated against", "misses printed by name") removed and
replaced with the record's own words; the `raw` tier's two record senses
listed as a conflict with a field-name-keyed decision procedure for the whole
tier enum; Q04/Q32 operationalisations lifted from the inventory replaced by
record-anchored descriptions. Should-fix items applied: corrected citations
(check_model README line, measure_join lines, cycle count sources, attempt-2
decline line), citations added to every previously uncited conflict, the
human-panelist 71% recorded as a record conflict (not struck by the glossary),
node-count conflict added, decline-correctness vs decline-defensibility naming
recorded as unequated, new entries for separability/null, the symbolic
engine, relevance-query output, and CI, close-event headings listed, status
word carried verbatim, 'headline' and 'README' added to overloaded words,
human-tier markers extended to the post-redaction role language, cove and
attended rules made mechanical, sources/ pointers replaced by repo paths.

## Revision after closure review (2026-09-02)

`review_2.md` (committed untouched) found the tier decision procedure had
never rendered (it sat under a key the renderer skips), three more README-only
phrases that straddle README line breaks, and a rule ordering that mis-tiered
the handoff span. Applied: the procedure is now rendered, value-keyed rather
than span-keyed, with the prose/artifact gate first and arc-1 panel triggers;
the three phrases and the pre-answering sentences (seat names and counts, PASS
counts, span-quote counts, "at the pin" result glosses) are replaced by
attributive wording that names the record line or defers to a live run; the
two miscitations are fixed; the review pointer is gone from the rendered file.
`leakscan.py` now scans any translator-facing file for word n-grams shared
with the README that occur nowhere else in the record, tokenising across line
breaks; the glossary and brief pass with zero candidates, and a probe file
containing the three removed phrases fails.

## Revision after third closure pass (2026-09-02)

`review_3.md` (committed untouched): every review-2 blocker closed; the
procedure returned no wrong tier on seven spans but was not total. Applied:
claim-splitting moved to step 1; label attachment includes 'is' and the JSON
key walk; live-run/git/filesystem gate runs first; the prose gate covers any
record document; a terminal step tiers any unmatched value `stated`. Three
surviving pre-answers (14 unmatched, four PASS lines, wall 0.14 s) and the
quoted verdict string made attributive; the append-only convention no longer
pre-classifies what the redaction hunks removed; cites corrected
(machine/README.md:100 and :160-163, graph_check.py:39-140,
CALCULUS_RUNBOOK.md:128-129); a denominator route added for the criterion
standing entry. The PRUNED.md restore sentence is now quoted verbatim rather
than characterised.
