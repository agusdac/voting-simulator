# Scoring family

## Question

How do the nine GDP spend shares become a left–right placement — a signed index, five prototype budgets, or polar-mass (left shares vs right shares, neutrals ignored)?

## Done means

The family of scoring is locked (not yet the exact polarities, bins, or conviction formula).

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

Five prototype budgets, one share vector per label (`far_left`, `left`, `center`, `right`, `far_right`). A party’s placement is the prototype with the smallest L1 distance: Σ |party_share − prototype_share| over the nine GDP categories. No signed index and no polar-mass ratio. The five vectors themselves, L1 ties, and conviction are later tickets.
