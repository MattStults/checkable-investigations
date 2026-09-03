# Completeness audit: model output against deterministic denominators

Owner's point (2026-09-03): the goal is to fight LLM filtering bias, which
needs an artifact whose completeness can be checked mechanically. Such a
check needs a denominator the model did not choose. Three are enumerable
from the spans by regex, and the current ledger (Opus documents, Sonnet git
log; blind, exhaustive, checker-accepted) can be scored against them.

| source class | numeric literals carried by a claim | event markers carried | backticked paths carried |
|---|---|---|---|
| ledger (ITERATION_NOTES) | 491/491 (100%) | 61/61 (100%) | n/a |
| arc2_json | 104/104 (100%) | 2/2 | n/a |
| arc2_docs | 722/740 (98%) | 86/86 (100%) | 48/154 (31%) |
| arc1_docs | 985/991 (99%) | 19/20 (95%) | 440/527 (83%) |
| arc1_cycles | 369/390 (95%) | 10/17 (59%) | n/a |
| git_log (Sonnet) | 1697/1785 (95%) | 38/42 (90%) | 34/58 (59%) |
| all | 4368/4501 (97%) | 216/228 (95%) | 522/739 (71%) |

Denominators: numeric literals excluding dates and single digits; markers =
ERRATUM, RULING, SIGNED, COUNTERSIGNED, WITHDRAWN, STRUCK, VOID, SUPERSEDED,
REGISTERED, BINDING, ADDENDUM, DISPATCH, CoVe, re-derived; paths = backticked
file names. "Carried" = the token appears as a claim's value/numerator/
denominator or inside a claim's quote from that span. Misses inspected
include entry cross-references ("notes 0031"), version strings ("1.2 join"),
table headers ("95% CI") and a genuine omission ("264 of the 692 chain-free
candidates"). Paths are under-carried because the brief (rule 20) says a
file name in prose is not by itself an existence claim.

Same denominators applied to the Haiku capability probe give 0-48% numeric
coverage: the check separates the tiers immediately, and it would have
flagged Haiku's silence, which the verbatim checker cannot see.

## What this does and does not buy

- It makes omission of a NUMBER, MARKER or PATH detectable per span, with
  the residue forced into an explicit "declined, reason class" list that
  can be sampled. That is a real, mechanical completeness check, and it
  is cheap (regex over spans).
- It does not detect omission of an assertion that has no such anchor
  (a prose sentence with no number, marker or path), nor mislabelling of
  what an anchored number means. Those remain a model-judgement layer;
  their bias can be bounded only by redundancy (two translators, disagreement
  sampling) or by owner adjudication samples.
- Applied to a question-directed reviewer it turns "the reviewer cited
  what it chose" into "the reviewer accounted for every anchor in every
  span it touched", and every anchor it did not touch is visible as
  uncovered. Coverage becomes a number, not a claim.
