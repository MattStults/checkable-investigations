# Step 2 — Glossary

Metric definitions, measurement tiers and modes, the authoritative-artifact
map, and the record's own conventions, each entry citing the record document
that defines it (`path:line` into the target repo at `48e66ce`). Written
before translation; the README under test was excluded from every source
pass so nothing here is derived from the claims being verified.

Files:

- `glossary.json` — source of truth. Sections: `tiers` (closed enum for the
  ledger's tier field), `entries` (28 terms), `authoritative_artifact_map`,
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
