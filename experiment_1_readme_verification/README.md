# Experiment 1: README verification by claim ledger

The registered design, expectations included, is the blog post:
[Pilot: verifying my own README with a claim
ledger](https://mattstults.github.io/2026/09/01/readme-verification-pilot.html).
The design and expectations sections there are frozen; results will be added to
the post and the artifacts committed here.

Target: the README of
[semi-formal-document-analysis](https://github.com/MattStults/semi-formal-document-analysis),
pinned to the commit recorded in `claim_inventory` when it lands.

Artifacts land here in registration order:

1. `claim_inventory/` — the README's checkable claims + hypothesis rules, frozen before translation
2. `glossary/` — metric definitions and authoritative-artifact map, frozen before translation
3. `brief/` — the translator brief, with its amendment history
4. `ledger/` — the translated claims (final ledger is entirely lower-tier translated)
5. `checker/` — the mechanical checks
6. `baseline/` — the adversarial-review arm's report and brief
7. `results/` — query outcomes, perturbation probe, rulings, intervention log
