# Party spectrum

## Destination

Brief + spec ready for fire-in-the-hole: each party with nine GDP spend shares is labeled `far_left` / `left` / `center` / `right` / `far_right` plus a conviction percent derived from those shares. A standalone `classify.py` script is a deliverable of this version. The affinity vote rule does not change.

## Notes

- Domain: democratic election simulation, simple to complex.
- Slug: `party-spectrum`. Version: **v0.3.0**.
- Phase B done: [brief](../../features/party-spectrum.md) · [spec](../../specs/party-spectrum.md).
- Sibling: [budget-affinity](../budget-affinity/map.md) — nine shares already locked; this map only *reads* them.
- Plan, don't do.
- Project language: English identifiers (`far_left`, `left`, `center`, `right`, `far_right`, `conviction`).
- Forge: not requested (ask once).

## Decisions so far

- [Scoring family](./decisions/01-scoring-family.md) — five prototype budgets; label = nearest L1.
- [Conviction and bins](./decisions/02-conviction-and-bins.md) — conviction `(1 − d1/2)×100`; L1 ties pick the more central label.
- [Prototype budgets](./decisions/04-prototype-budgets.md) — locked 9-share vectors per label (asset table).
- [Label surface](./decisions/03-label-surface.md) — fields on the party; own module + script; not inside `simulate`.
- [Standalone script](./decisions/05-standalone-script.md) — `classify.py --scenario` is in this version’s build, not later.

## Not yet specified

<!-- empty. Destination met once brief + spec exist. -->

## Out of scope

- Changing ballots or the affinity matrix because of the label.
- Computing spectrum inside `simulate` / `simulate_from_scenario`.
- A second political axis (authoritarian–libertarian, GAL–TAN).
- NLP of party names or manifesto text.
- Labeling voters.
