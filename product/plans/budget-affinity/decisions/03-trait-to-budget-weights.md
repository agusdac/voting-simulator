# Trait-to-budget weights

## Question

What linear coefficients map voter traits (`age`, `dependents`, `urban`, `health_status`, `education_level`, `veteran`, `gender`) onto the 9 party GDP categories?

## Done means

The weight each trait adds to each spend share is locked enough to implement the argmax score.

## Type

grilling

## Status

closed

## Claimed by

user (chat)

## Blocked by

- [Linear vote rule](./02-linear-vote-rule.md)

## Forge

- Gitea: TBD
- GitHub: TBD

## Answer

Coefficients are `+1` / `0` / `−1`. `urban` and `veteran` are 0/1. `gender` is 1 = woman, 0 = otherwise.

| trait | health | education | infrastructure | defense | social_protection | environment | housing | research | public_order |
|---|---|---|---|---|---|---|---|---|---|
| age | +1 | −1 | 0 | +1 | +1 | 0 | 0 | 0 | 0 |
| dependents | +1 | +1 | 0 | 0 | +1 | 0 | +1 | 0 | 0 |
| urban | 0 | 0 | 0 | 0 | 0 | +1 | +1 | 0 | +1 |
| health_status | +1 | 0 | 0 | 0 | +1 | 0 | 0 | 0 | 0 |
| education_level | 0 | +1 | 0 | 0 | 0 | +1 | 0 | +1 | 0 |
| veteran | +1 | 0 | 0 | +1 | 0 | 0 | 0 | 0 | +1 |
| gender | +1 | +1 | 0 | −1 | +1 | 0 | 0 | 0 | 0 |

Budget weight for a share = Σ (trait × cell). Party score = Σ (budget weight × party GDP share).
