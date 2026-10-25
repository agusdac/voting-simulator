# Prototype budgets

## Question

What nine GDP shares (each in `[0, 1]`, summing to 1) define the `far_left`, `left`, `center`, `right`, and `far_right` prototypes?

## Done means

Five locked share vectors, same fields and constraints as `PoliticalParty`, one per spectrum label.

## Type

prototype

## Status

closed

## Claimed by

user (chat)

## Asset

[Draft five vectors](../assets/04-prototype-budgets.md)

## Blocked by

- [Scoring family](./01-scoring-family.md)

## Forge

- Gitea: TBD
- GitHub: TBD

## Answer

The five prototype share vectors are locked as in [the asset](../assets/04-prototype-budgets.md). Each sums to 1; fields match `PoliticalParty`.

| share | far_left | left | center | right | far_right |
|---|---:|---:|---:|---:|---:|
| health | 0.18 | 0.16 | 0.12 | 0.10 | 0.08 |
| education | 0.16 | 0.15 | 0.12 | 0.10 | 0.07 |
| infrastructure | 0.08 | 0.10 | 0.14 | 0.14 | 0.12 |
| defense | 0.02 | 0.05 | 0.10 | 0.18 | 0.28 |
| social_protection | 0.22 | 0.18 | 0.12 | 0.08 | 0.04 |
| environment | 0.12 | 0.10 | 0.08 | 0.05 | 0.02 |
| housing | 0.14 | 0.12 | 0.10 | 0.08 | 0.05 |
| research | 0.06 | 0.08 | 0.10 | 0.08 | 0.06 |
| public_order | 0.02 | 0.06 | 0.12 | 0.19 | 0.28 |
