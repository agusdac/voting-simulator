# Budget affinity

## Version & scope

**v0.2.0.** Scenario JSON parties and voters carry declared GDP shares and traits; scenario ballots are linear argmax. Out: remote files, changing the result payload, leftover uniform random on the scenario path.

`simulate(n_parties, n_voters, seed)` stays v0.1 uniform random.

## Decisions locked

- [Party and voter fields](../plans/budget-affinity/decisions/01-party-and-voter-fields.md) — 9 GDP shares; voter traits including `dependents` (people supported, including children).
- [Linear vote rule](../plans/budget-affinity/decisions/02-linear-vote-rule.md) — matrix → dot product → argmax; seed unused; aggregate ties → tied list.
- [Trait-to-budget weights](../plans/budget-affinity/decisions/03-trait-to-budget-weights.md) — +1/0/−1; `gender` 1 = woman.
- [Share and trait scale](../plans/budget-affinity/decisions/04-share-and-trait-scale.md) — shares in `[0, 1]` and sum to 1 per party; traits raw.

## User stories & flows

1. `--scenario` / `simulate_from_scenario` with full declared fields → affinity ballots → same payload as v0.1 (raw votes, counts, winner or tied).
2. `--parties N` still uniform random.
3. Missing declared field, share outside `[0, 1]`, or shares that do not sum to 1 → no simulation.

## Architecture touchpoints

- `PoliticalParty` / `Voter` — declared fields live on the entities.
- Scoring module behind `simulate_from_scenario` — owns the matrix and argmax. CLI still does not count.
- Unknown JSON keys other than declared fields stay ignored.

## Score

Budget weight for share *s* = Σ (trait × coefficient). Party score = Σ (weight_s × share_s). Coefficients: see [Trait-to-budget weights](../plans/budget-affinity/decisions/03-trait-to-budget-weights.md).

Each voter votes for the party with the **strictly** highest score. A per-voter score tie casts no ballot. Seed is unused. National winner / tied list still comes from vote **counts**, same as v0.1.

## Behaviors

- The user can run a scenario when every party has the 9 shares in `[0, 1]` summing to 1 and every voter has the 7 traits / the system scores parties with the locked matrix and each voter with a unique max score votes for that party.
- The user can read the same result shape when the run finishes / raw votes, counts, winner or tied list from counts.
- The user can reject a scenario when a declared field is missing, a share is outside `[0, 1]`, or a party’s shares do not sum to 1 / the system does not simulate and signals the error.
- The user can still run `--parties` / `simulate(n, m, seed)` / uniform random, no shares or traits required.

## Build tickets

### OR-1 — Affinity scenario run

- **Goal:** Scenario path uses declared fields and argmax, not uniform random.
- **Scope:** Entity fields; JSON reads declared keys (others still ignored); matrix + argmax; shares in `[0, 1]`; flags/`simulate(n,m,seed)` untouched.
- **Deps:** json-scenario OR-1
- **Done means:** `simulate_from_scenario` on a valid v0.2 JSON casts affinity ballots from the locked score; missing fields or shares outside `[0, 1]` error; `simulate(n, m, seed)` still uniform random.
- **Checklist:**
  - [x] 9 shares on `PoliticalParty`, 7 traits on `Voter`
  - [x] JSON requires those fields; unknown extra keys ignored
  - [x] Linear score + unique argmax ballot
  - [x] Per-voter score tie → no ballot
  - [x] Share outside `[0, 1]`, shares that do not sum to 1, or missing field → error
  - [x] `simulate(n, m, seed)` unchanged

### OR-2 — Example scenario

- **Goal:** `examples/scenario.json` is a valid v0.2 file; CLI `--scenario` still prints the payload.
- **Scope:** Example JSON only + existing CLI. No new electoral rules.
- **Deps:** OR-1
- **Done means:** `uv run python main.py --scenario examples/scenario.json` runs an affinity election and prints counts, winner or tied, and raw votes.
- **Checklist:**
  - [x] Example parties have 9 shares in `[0, 1]`
  - [x] Example voters have 7 traits
  - [x] CLI still delegates and prints
