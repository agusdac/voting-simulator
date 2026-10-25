# JSON scenario

## Version

**v0.1.0** — unreleased; second input path beside N/M/seed.

## Plan

[JSON scenario map](../plans/json-scenario/map.md)

## Description

A JSON file of explicit `parties` and `voters` objects is another way to assemble a run. N and M are the list lengths. Extra keys on those objects are ignored until a later version declares them. `simulate(n_parties, n_voters, seed)` stays.

## Value

Scenarios can grow deterministic entity fields in the file without changing how a run is invoked.

## Primary User Stories

- As a model user, I load a JSON scenario and get the same kind of election result as `simulate`.
- As a model user, I put undeclared fields on parties or voters and the run still works; those fields are not on the entities yet.
- As a model user, I still call `simulate(n_parties, n_voters, seed)` without a file.

## Requirements

- JSON has optional `seed`, required `parties` and `voters` arrays of objects.
- N = len(parties), M = len(voters).
- v0.1 declared field on each object: `id`.
- Extra keys are ignored (not stored on `Voter` / `PoliticalParty`).
- Result shape is unchanged (raw votes, counts, winner or tied).
- Function/CLI N-M-seed path remains.

## Constraints

- Local file only. No remote load.
- No persistence, auth, or multi-tenant.
- Empty `parties` or `voters` does not simulate.

## Dependencies

[Minimal model](./minimal-model.md) — `simulate` and entities exist.
