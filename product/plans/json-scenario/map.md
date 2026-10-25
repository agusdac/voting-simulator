# JSON scenario

## Destination

Brief + spec ready for fire-in-the-hole on **v0.1.0**: a JSON file of explicit `parties` and `voters` objects (fields grow with deterministic characteristics) is another way to assemble a run; `simulate(n_parties, n_voters, seed)` stays; the result shape does not change.

## Notes

- Domain: democratic election simulation, simple to complex.
- Slug: `json-scenario`. Version: **v0.1.0** (unreleased; folded in by request, not a v0.2 bump).
- Sibling: [minimal-model](../minimal-model/map.md) — `simulate(n_parties, n_voters, seed)` remains a valid path.
- Plan, don't do.
- Project language: English.
- Forge: not requested.
- Phase B done: [brief](../../features/json-scenario.md) · [spec](../../specs/json-scenario.md).
- Spec defaults from minimal-model until this map overrides them: party ids `1..N`, optional seed, `Voter` / `PoliticalParty` / `simulate`.
- Evolution: add deterministic characteristics on party and voter entities, not generated populations.

## Decisions so far

- [JSON vs existing inputs](./decisions/01-json-and-existing-inputs.md) — both paths: function/CLI stay; JSON is another way to assemble the run.
- [Scenario document shape](./decisions/02-scenario-document-shape.md) — `seed?`, `parties[]`, `voters[]`; N/M from list lengths.
- [Extensible entity fields](./decisions/03-extensible-entity-fields.md) — extra keys ignored until a version declares them.

## Not yet specified

<!-- v0.1: empty. Declared entity field is `id`; named extras are later versions. -->

## Out of scope

- Demographics, districts, campaigns, UI, persistence as product features — unless a later ticket pulls a field into the JSON.
- Remote/network loading of the file.
