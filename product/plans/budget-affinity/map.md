# Budget affinity

## Destination

Brief + spec ready for fire-in-the-hole: parties declare GDP spend shares; voters have intrinsic traits linearly related to those shares; the ballot is no longer uniform-random among ids. JSON extra keys that this version declares become real entity fields.

## Notes

- Domain: democratic election simulation, simple to complex.
- Slug: `budget-affinity`. Version: **v0.2.0**.
- Phase B done: [brief](../../features/budget-affinity.md) · [spec](../../specs/budget-affinity.md).
- Sibling: [json-scenario](../json-scenario/map.md) — undeclared keys stay ignored; this map declares the new ones.
- Plan, don't do.
- Project language: English identifiers for spend shares and voter traits.
- Forge: not requested.

## Decisions so far

- [Party and voter fields](./decisions/01-party-and-voter-fields.md) — 9 party GDP shares; voter: age, dependents, urban, health_status, education_level, veteran, gender.
- [Linear vote rule](./decisions/02-linear-vote-rule.md) — linear weights → dot product → argmax; seed unused; score ties → tied list.
- [Trait-to-budget weights](./decisions/03-trait-to-budget-weights.md) — +1/0/−1 matrix; gender 1 = woman.
- [Share and trait scale](./decisions/04-share-and-trait-scale.md) — GDP shares in [0, 1] and sum to 1 per party; traits raw.

## Not yet specified

<!-- empty. Destination met once brief + spec exist. -->

## Out of scope

- Campaigns, districts, UI, persistence, remote JSON.
- Tax/ideology axes that are not GDP spend or linear voter traits (until ticketed).
