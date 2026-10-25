# Party spectrum

## Version & scope

**v0.3.0.** Parties with nine GDP shares get a left–right label and conviction percent from five prototype budgets. Out: changing ballots, a second axis, labeling voters, classification inside `simulate`.

## Decisions locked

- [Scoring family](../plans/party-spectrum/decisions/01-scoring-family.md) — five prototypes; nearest L1.
- [Conviction and bins](../plans/party-spectrum/decisions/02-conviction-and-bins.md) — `(1 − d1/2)×100`; ties → more central, then left-side.
- [Label surface](../plans/party-spectrum/decisions/03-label-surface.md) — fields on the party; own module; not in `simulate`.
- [Prototype budgets](../plans/party-spectrum/decisions/04-prototype-budgets.md) — locked 9-share vectors.
- [Standalone script](../plans/party-spectrum/decisions/05-standalone-script.md) — `classify.py --scenario` in this version.

## User stories & flows

1. Call `classify(party)` → same party with `spectrum` and `conviction` set.
2. `uv run python classify.py --scenario path.json` → one line per party: id, label, conviction.
3. Election paths unchanged and unclassified.

## Architecture touchpoints

- `PoliticalParty` — optional `spectrum`, `conviction`.
- `spectrum` module — prototypes, L1, tie-break, conviction. Deep: callers pass a party, get a labeled party.
- `classify.py` — thin adapter: load `parties` from JSON, call `classify`, print. Does not import electoral tally.
- `simulate` / `simulate_from_scenario` / `main.py` — do not call `classify`.

## Prototypes

Share vectors: [Prototype budgets asset](../plans/party-spectrum/assets/04-prototype-budgets.md). Label order: `far_left`, `left`, `center`, `right`, `far_right`. Centrality is distance to `center` on that order.

## Behaviors

- The user can classify a party when its nine shares are in `[0, 1]` and sum to 1 / the system sets `spectrum` to the nearest L1 prototype and `conviction` to `(1 − d1 / 2) × 100`.
- The user can resolve an L1 tie when two or more prototypes share `d1` / the system picks the most central label, and the left-side label if centrality also ties.
- The user can reject invalid shares when a field is missing, a share is outside `[0, 1]`, or they do not sum to 1 / the system does not classify and signals the error.
- The user can run the script when a JSON file has `parties` / the system prints `party {id}: {spectrum} {conviction}` for each, without running an election.
- The user can ignore extra JSON keys when classifying / undeclared keys including `spectrum` are not read as input.
- The user can run an election after v0.3 / `simulate` and `simulate_from_scenario` still do not set `spectrum` or `conviction`.

## Build tickets

### OR-1 — Classify a party

- **Goal:** Module labels a `PoliticalParty` from its GDP shares.
- **Scope:** Entity fields; `spectrum.classify`; prototypes; L1; conviction; tie-break; share validation. No script. No `simulate` changes except that new entity defaults stay compatible.
- **Deps:** none
- **Done means:** `classify(party)` returns a party with `spectrum` and `conviction` per the locked rule; invalid shares error; election functions still do not classify.
- **Checklist:**
  - [x] Optional `spectrum` / `conviction` on `PoliticalParty`
  - [x] Nearest L1 vs locked prototypes
  - [x] Conviction `(1 − d1 / 2) × 100`
  - [x] L1 tie → more central, then left-side
  - [x] Invalid shares → error
  - [x] `simulate` / `simulate_from_scenario` leave fields unset

### OR-2 — Classify script

- **Goal:** `classify.py --scenario` prints labels for JSON parties.
- **Scope:** Thin script + JSON `parties` parse. No electoral logic.
- **Deps:** OR-1
- **Done means:** `uv run python classify.py --scenario examples/scenario.json` prints each party’s id, spectrum, and conviction; invalid shares error; `simulate` is not used.
- **Checklist:**
  - [x] `--scenario` path
  - [x] Prints `party {id}: {spectrum} {conviction}`
  - [x] Extra JSON keys ignored
  - [x] Does not call `simulate`
