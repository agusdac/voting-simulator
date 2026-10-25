# JSON scenario

## Version & scope

**v0.1.0.** JSON is another way to assemble a run. Out: remote files, named extra fields on entities, changing the result shape.

## Decisions locked

- [JSON vs existing inputs](../plans/json-scenario/decisions/01-json-and-existing-inputs.md) — both paths; function/CLI stay.
- [Scenario document shape](../plans/json-scenario/decisions/02-scenario-document-shape.md) — `seed?`, `parties[]`, `voters[]`; N/M from lengths.
- [Extensible entity fields](../plans/json-scenario/decisions/03-extensible-entity-fields.md) — extra keys ignored until declared.

## User stories & flows

1. `simulate_from_scenario(path)` → `ElectionResult`.
2. Undeclared keys on party/voter objects do not appear on entities.
3. CLI `--scenario` later; this slice is the function.

## Architecture touchpoints

- `simulate` — electoral logic (vote, counts, winner/tie). JSON does not recount.
- `simulate_from_scenario` — reads local JSON, keeps `id`, drops extra keys, delegates the election.

## Behaviors

- The user can run a JSON scenario when the file has `parties` and `voters` with `id` / the system uses those ids, N and M from list lengths, optional `seed`, and returns raw votes, counts, winner or tied.
- The user can omit undeclared characteristics when they put extra keys on objects / the system ignores them; `Voter` and `PoliticalParty` only have declared fields (`id`, plus `vote` after the run).
- The user can still call `simulate(n_parties, n_voters, seed)` / that path is unchanged.
- The user can reject a scenario when `parties` or `voters` is missing or empty, or an object lacks `id` / the system does not simulate and signals the error.

## Build tickets

### OR-1 — Load JSON scenario

- **Goal:** `simulate_from_scenario(path)` from a local JSON file.
- **Scope:** Parse `seed?`, `parties[]`, `voters[]`; keep `id`; ignore extra keys; delegate election; no CLI.
- **Deps:** minimal-model OR-1 (`simulate`)
- **Done means:** A path to a valid scenario JSON yields an `ElectionResult`; extra keys are not on the entities; empty or id-less lists do not simulate.
- **Checklist:**
  - [x] `simulate_from_scenario(path)`
  - [x] N/M from list lengths, ids from the file
  - [x] Extra keys ignored
  - [x] Missing/empty/`id` missing → error
  - [x] `simulate(n, m, seed)` unchanged

### OR-2 — CLI `--scenario`

- **Goal:** CLI can take a scenario file and still take N/M/seed flags.
- **Scope:** Thin CLI only; delegates to `simulate` or `simulate_from_scenario`.
- **Deps:** OR-1
- **Done means:** `--scenario path` prints the same payload shape as the flags path.
- **Checklist:**
  - [x] `--scenario` path
  - [x] Existing `--parties` / `--voters` / `--seed` still work
  - [x] Prints result
