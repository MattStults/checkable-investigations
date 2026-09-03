# Adjudicator brief — BLIND re-adjudication (D-12b)

You rule on items where the two verification arms of this experiment ended in
contradicted, contested, unverifiable or dangling. The frozen design assigned
this role to the project owner; the owner has delegated it to you and every
ruling will be labelled model-made. Rule as a careful, sceptical human would:
against the sources, not against either arm's argument.

## Your materials

- The packets in this directory's parent: `results/packets_blind/<id>.md` (one per
  item; each gives the README text, the inventory's values and dimensions,
  the ledger arm's derivation with the claims it rests on, and the baseline
  arm's state and reason) and `results/packets/INDEX.md` (live-run conflicts
  and scope caveats at the bottom).
- The repository under test at `~/Documents/ai_safety_projects/semi-formal-document-analysis`,
  READ-ONLY, checked out at the pinned commit. `git log/show/blame/diff` are
  fine; running committed scripts read-only is fine (use
  `semi-formal-experiment/.venv/bin/python` where the README does; no network).
  Never modify it. Do not read anything under its `.claude/`.
- The owner's recorded testimony: `results/owner_notes.md`. Treat it as a
  witness statement (tier human), not as a source in the record.
- The frozen inventory for dimensions: `claim_inventory/inventory.json`.

Do not read the ledger, the glossary, the brief, the intervention log, the
baseline report, or anything else under the experiment directory: the packets
carry what each arm concluded, and your job is to decide against the record.

## How to rule

For each item assigned to you:
1. Read the packet. Identify the exact question: which value, at which
   dimensions (metric, tier, snapshot, denominator, scope), or which rule.
2. Go to the record. Open the cited files at the cited lines; run the cited
   commands where the packet rests on a live run; check git where history is
   the question. Quote verbatim what decides it.
3. Rule one of: `verified`, `contradicted`, `contested`, `unverifiable`
   (for a verdict node with no provider: `dangling`). Definitions: verified —
   the record states the claimed value at the claimed dimensions;
   contradicted — the record states a different value or the event did not
   happen as claimed (give both values); contested — the record holds
   conflicting artifacts and neither is marked as superseding; unverifiable —
   no artifact in the record decides it.
4. Say which arm's reasoning was right, wrong, or right for the wrong reason,
   in one or two sentences, and whether the disagreement was substance or
   label (contested vs contradicted on the same facts).
5. If the ruling needs knowledge only the owner has (intent, what happened
   off the record), say so explicitly and rule provisionally.
6. For a README item, add a one-line disposition: grounded / tightened
   (give the tighter wording) / deleted / kept as an explicit commitment.

## Output

Write one file per item: `results/rulings_blind/<id>.md` with sections
`Ruling`, `Basis` (quotes with path:lines or command + output), `Arms`,
`Owner input needed` (yes/no and what), `README disposition`. Also append
one JSON line per item to `results/rulings_blind/rulings.jsonl`:
`{"id", "ruling", "substance_or_label", "arm_right": "ledger|baseline|both|neither", "owner_input_needed": bool, "disposition"}`.
For the live-run conflicts and scope caveats in INDEX.md write
`results/rulings/CONFLICTS_AND_CAVEATS.md` with the same structure.
Do not edit the packets. Reply with only the list of ids and rulings.

## Blind variant

The two arms appear as Arm A and Arm B, randomized per item, with their
reasoning removed. Rule on the record. In `Arms`, say which arm's EVIDENCE
decided the ruling (A, B, both, neither) and whether each arm's state was
right; do not guess which method produced which arm. Do not read
results/rulings/, results/packets/, or results/rulings_blind_mapping.SEALED.json.
In the JSON line use "arm_right": "A|B|both|neither".
