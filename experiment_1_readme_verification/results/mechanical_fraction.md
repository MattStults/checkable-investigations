# How much of the translation could have been purely mechanical?

Method: classify every claim in the final ledger (14,721) by whether a
parser or regex could have produced its core (kind, value, verbatim quote,
source) from the span without a model. Classes, applied in order:
structured file (JSON/YAML key-value parse); git commit metadata; a rate
written as n/d; a path existence; a markdown table cell; "label: number";
a short span (<= 60 chars) containing the literal (value recoverable, but
the metric label still needs assignment). Everything else: model needed.
Owner's question; computed 2026-09-03.

| class | claims | share |
|---|---|---|
| model needed | 7,546 | 51.3% |
| structured file (JSON/YAML) | 2,746 | 18.7% |
| short span containing the literal (metric labelling still needed) | 2,457 | 16.7% |
| git commit metadata | 647 | 4.4% |
| rate written as n/d | 605 | 4.1% |
| markdown table cell | 405 | 2.8% |
| label: number | 251 | 1.7% |
| path existence | 64 | 0.4% |

Strictly mechanical (everything but the two "needs labelling"/"model"
rows): 32%. Mechanical core with a labelling step: 49%.

By kind: rates 88% mechanical, values 68%, existence 43%, events 18%
(essentially only the git commit events). Events are 39% of the ledger
and carry every hypothesis (H01-H15); of the 3,345 document-sourced event
claims, 20% open with a heading or all-caps marker (ERRATUM, RULING,
SIGNED, WITHDRAWN...) that a regex can detect as a trigger, but actor,
finding, caught_by and links need reading.

Of the 465 claims the query decisions actually relied on, 35% are in a
mechanical class. The other 65% are prose values needing a metric label,
or events.

Caveat on "most logs": this record is a prose ledger (markdown entries,
handoffs, prereg documents, review dispositions). Its structured parts
(JSON score files, cycle records, git metadata) were the mechanical share.
A record that is mostly structured logs would sit far above 32%; the
translation cost here was paid almost entirely for the prose.
