# Budget affinity

## Version

**v0.2.0** — vote rule changes: ballots follow linear affinity to party GDP shares, not uniform random.

## Plan

[Budget affinity map](../plans/budget-affinity/map.md)

## Description

Each party declares nine GDP spend shares in `[0, 1]`. Each voter has seven raw intrinsic traits. Those traits map through a fixed +1/0/−1 matrix into nine weights; the voter’s score for a party is the dot product with that party’s shares; the ballot is argmax. Seed does not affect the vote. Score ties use the existing tied list.

## Value

The scenario JSON becomes the place where deterministic politics live: add fields on entities, get a different electorate, without changing how a run is invoked.

## Primary User Stories

- As a model user, I put GDP shares on parties and traits on voters in the JSON and get ballots from linear scores, not from uniform random.
- As a model user, I still call `simulate(n_parties, n_voters, seed)` and get the v0.1 random path.
- As a model user, two parties with the same top score for a voter contribute to a tied list at the aggregate if that is the national max.

## Requirements

- `PoliticalParty` declares: `health`, `education`, `infrastructure`, `defense`, `social_protection`, `environment`, `housing`, `research`, `public_order` in `[0, 1]`, and those nine values sum to 1.
- `Voter` declares: `age`, `dependents`, `urban`, `health_status`, `education_level`, `veteran`, `gender` (raw; `gender` 1 = woman).
- Score uses the locked coefficient matrix; vote is argmax; seed unused for ballots.
- JSON scenario requires those declared fields; other extra keys stay ignored.
- Result shape unchanged (raw votes, counts, winner or tied).
- `simulate(n_parties, n_voters, seed)` stays the uniform-random path.

## Constraints

- Local JSON only. No auth, persistence, or multi-tenant.
- Shares outside `[0, 1]`, or nine shares that do not sum to 1, do not simulate.
- Missing declared fields do not simulate.

## Dependencies

[JSON scenario](./json-scenario.md) and [minimal model](./minimal-model.md) on v0.1.0.
