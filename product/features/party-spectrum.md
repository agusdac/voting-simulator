# Party spectrum

## Version

**v0.3.0** — new capability: label parties from GDP share mix. Vote rule unchanged.

## Plan

[Party spectrum map](../plans/party-spectrum/map.md)

## Description

Each party’s nine GDP shares are compared with five locked prototype budgets. The label is the nearest prototype in L1 distance; conviction is how close that match is. Classification lives outside the election engine. A script prints labels for a scenario file.

## Value

The same budget numbers that drive affinity voting can be read as a left–right placement, without mixing that reading into ballots.

## Primary User Stories

- As a model user, I classify a party’s shares and get `spectrum` plus `conviction` on the party.
- As a model user, I run `classify.py --scenario` and see each party’s label without running an election.
- As a model user, I still run `simulate` / `--scenario` and get the same votes as v0.2; those paths do not classify.

## Requirements

- `PoliticalParty` carries optional `spectrum` and `conviction`.
- Five locked prototype share vectors; label = nearest L1; L1 ties pick the more central label (left-side on equal centrality).
- Conviction = `(1 − d1 / 2) × 100`.
- `spectrum.classify` (own module) sets the fields; not called from `simulate` or `simulate_from_scenario`.
- `uv run python classify.py --scenario <path>` prints `id`, `spectrum`, `conviction`.
- Invalid shares (missing, outside `[0, 1]`, or not summing to 1) do not classify.
- JSON does not take `spectrum` / `conviction` as input.

## Constraints

- Local JSON only. No auth, persistence, or multi-tenant.
- English identifiers: `far_left`, `left`, `center`, `right`, `far_right`.

## Dependencies

[Budget affinity](./budget-affinity.md) on v0.2.0 (nine shares).
