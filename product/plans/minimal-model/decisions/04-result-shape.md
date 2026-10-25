# Result shape

## Question

What does the election result of a v0.1 run contain?

## Done means

The minimum payload a simulation returns is locked (counts, winner, tie, or raw votes only).

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

A run returns **raw votes** (each voter and who they voted for) and the aggregate: **counts per party + winner**. If there is a tie at the maximum, there is no unique winner: the result lists the **tied** parties.
