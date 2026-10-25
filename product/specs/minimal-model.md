# Minimal model

## Version & scope

**v0.1.0.** A callable run: N parties, M voters, seed, uniform random vote. Out: demographics, districts, campaigns, UI, persistence, party names.

Spec defaults (fog left for the contract):

- Parties: integer id `1..N`.
- Seed: optional; if omitted, the run is not reproduced.
- Python identifiers: `Voter`, `PoliticalParty`, `simulate`.
- CLI: M defaults to 100.

## Decisions locked

- [v0.1 model inputs](../plans/minimal-model/decisions/01-model-inputs.md) — N parties, M voters (first runs M=100), random vote.
- [Domain entities](../plans/minimal-model/decisions/02-domain-entities.md) — `Voter` (extensible) and `PoliticalParty` in `entities/`.
- [Invocation surface](../plans/minimal-model/decisions/03-invocation-surface.md) — Python function + thin CLI.
- [Result shape](../plans/minimal-model/decisions/04-result-shape.md) — raw votes + counts + winner; tie → list of tied parties.
- [Reproducibility seed](../plans/minimal-model/decisions/05-seed.md) — same N, M, and seed → same raw votes.

## User stories & flows

1. Call `simulate(n_parties, n_voters, seed=None)` → result.
2. Repeat the same N, M, and seed → same raw votes.
3. Tie at the maximum → no unique winner, list of tied parties.
4. CLI: pass N (and optionally M and seed) → prints that function's result.

## Architecture touchpoints

- `entities/` — `Voter`, `PoliticalParty`.
- Function `simulate` — only place for electoral logic.
- CLI — parses args, calls `simulate`, shows the result. Does not count votes itself.

## Behaviors

- The user can call `simulate(n_parties, n_voters, seed=None)` when N≥1 and M≥1 / the system creates N parties (`1..N`) and M voters, each with a uniform vote among those parties.
- The user can reproduce a run when they pass the same N, M, and seed / the system returns the same raw votes.
- The user can read raw votes when a run finishes / the system returns M pairs (voter, party).
- The user can read counts when a run finishes / the system returns votes per party and the sum is M.
- The user can read a winner when one party has strictly more votes / the system sets winner to that party and tied empty.
- The user can read tied parties when two or more share the maximum / the system leaves winner empty and lists those parties.
- The user can reject an invalid run when N < 1 or M < 1 / the system does not simulate and signals the error.
- The user can fire a run from the CLI when they pass N / the system calls `simulate` and shows raw votes, counts, winner or tied. M default 100. Seed optional.

## Build tickets

### OR-1 — Callable simulation

- **Goal:** `simulate` + entities, full result.
- **Scope:** `entities/Voter`, `entities/PoliticalParty`, `simulate(n_parties, n_voters, seed=None)` with raw votes, counts, winner or tied, and seed reproducibility. No CLI.
- **Deps:** none
- **Done means:** `simulate(n_parties, n_voters, seed=None)` exists, uses those entities, returns raw votes, counts, and a winner or tied list, and reproduces votes when the seed repeats.
- **Checklist:**
  - [x] Entities in `entities/`
  - [x] `simulate` with N, M, and optional seed
  - [x] Uniform random vote
  - [x] Same N, M, and seed → same raw votes
  - [x] Raw + aggregate payload
  - [x] Tie → tied list, no unique winner
  - [x] N < 1 or M < 1 does not simulate

### OR-2 — Thin CLI

- **Goal:** Command that fires `simulate` and shows the result.
- **Scope:** CLI; M default 100; optional seed. No electoral logic of its own.
- **Deps:** OR-1
- **Done means:** A command accepts N (optional M default 100, optional seed), calls `simulate`, and prints raw votes, counts, and winner or tied.
- **Checklist:**
  - [ ] Args N, M (default 100), and optional seed
  - [ ] Delegates to `simulate`
  - [ ] Shows the payload
