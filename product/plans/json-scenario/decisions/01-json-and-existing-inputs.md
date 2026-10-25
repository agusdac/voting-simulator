# JSON vs existing inputs

## Question

Is the JSON file the only way to start a v0.1 run, or does it sit beside `simulate(n_parties, n_voters, seed)` and the current CLI flags?

## Done means

It is decided whether N/M/seed flags remain, are replaced by a file path, or both work.

## Type

grilling

## Status

closed

## Claimed by

user (chat)

## Blocked by

- none

## Forge

- Gitea: TBD
- GitHub: TBD

## Answer

Both paths. `simulate(n_parties, n_voters, seed)` and the current CLI flags stay. JSON is another way to assemble that run.
