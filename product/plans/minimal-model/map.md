# Minimal model

## Destination

Brief + spec ready for fire-in-the-hole of **v0.1.0**: a callable model that takes N parties, M voters, and a seed, simulates a reproducible random vote, and exposes `Voter` (extensible) and `PoliticalParty` in `entities/`. First runs with M=100.

## Notes

- Domain: democratic election simulation, simple to complex.
- Slug: `minimal-model`. Version: `v0.1.0` (first, explicit request).
- Plan, don't do: pathfinder locks decisions and docs; it does not implement.
- Skills: grill-me (HITL), fire-in-the-hole + tdd when building.
- Stack: Python ≥3.12, `voting-simulator`.
- Project language: English (code, product docs, identifiers).
- Forge: GitHub origin `agusdac/voting-simulator`. Gitea/`gh` sync not requested yet.
- Phase B done: [brief](../../features/minimal-model.md) · [spec](../../specs/minimal-model.md).
- Spec defaults: party ids `1..N` with no names; optional seed (if missing, the run is not reproduced); identifiers `Voter` / `PoliticalParty` / `simulate`; CLI M=100 by default.

## Decisions so far

- [v0.1 model inputs](./decisions/01-model-inputs.md) — N parties, M voters (first runs M=100), random vote.
- [Domain entities](./decisions/02-domain-entities.md) — `Voter` (extensible) and `PoliticalParty` in `entities/`.
- [Invocation surface](./decisions/03-invocation-surface.md) — Python function + thin CLI; the model is the function.
- [Result shape](./decisions/04-result-shape.md) — raw votes + counts + winner; tie → list of tied parties.
- [Reproducibility seed](./decisions/05-seed.md) — same N, M, and seed → same raw votes.

## Not yet specified

<!-- v0.1: empty. Spec defaults in Notes. -->

## Out of scope

- Demographics, districts, campaigns, UI, persistence — later versions.
- Party names — not in v0.1 (id `1..N`).
