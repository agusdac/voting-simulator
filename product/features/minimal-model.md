# Minimal model

## Version

**v0.1.0** — first delivery: a callable model, simple to complex.

## Plan

[Minimal model map](../plans/minimal-model/map.md)

## Description

Simulates an election: takes N parties, M voters, and a seed; each voter votes at random; returns raw votes plus the aggregate (counts, winner or tied parties). The same seed reproduces the run. Invoked as a Python function; a thin CLI fires it. Entities live in `entities/`; `Voter` is built to grow.

## Value

Run a synthetic election from code or a terminal, with a domain core that can get richer without rewriting the run contract.

## Primary User Stories

- As a model user, I call a function with N, M, and a seed and get an election result.
- As a model user, I repeat the same N, M, and seed and get the same votes.
- As a terminal user, I fire that run with a command (M=100 by default).
- As a developer, I extend `Voter` without moving it out of `entities/`.

## Requirements

- The model is a function that takes N parties, M voters, and a seed.
- There are exactly M votes; each is random among the N parties.
- The same N, M, and seed produce the same raw votes.
- The result includes raw votes, counts per party, and a winner or a list of tied parties if they share the maximum.
- `Voter` and `PoliticalParty` live in `entities/`.
- A thin CLI invokes the function; it does not contain electoral logic.

## Constraints

- No persistence, auth, or multi-tenant: local process.
- Seed is optional: if omitted, the run is not guaranteed reproducible.
- Parties identified by integer id `1..N`; no names.

## Dependencies

None. Python ≥3.12 project.
