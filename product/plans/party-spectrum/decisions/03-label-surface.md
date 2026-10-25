# Label surface

## Question

Where does the spectrum label appear — on the party entity, in the election result payload, in CLI print, or all of those — and is it computed only on the JSON scenario path?

## Done means

Callers know which objects carry `spectrum` / `conviction` and which invocation paths compute them.

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

`PoliticalParty` carries optional `spectrum` and `conviction`. Classification is **not** inside `simulate` or `simulate_from_scenario`. A dedicated function (own module) maps nine shares → label + conviction and may set those fields on the party. A dedicated script is the invocation path: it reads a scenario JSON and prints each party id, `spectrum`, and `conviction` (English identifiers). The election CLI does not classify or print spectrum. The random `--parties` path does not classify. JSON does not accept spectrum as an input key (still ignored until some later version declares it).
