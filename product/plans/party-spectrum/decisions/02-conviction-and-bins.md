# Conviction and bins

## Question

Given nearest-prototype L1, what does conviction percent measure, and what happens when two prototypes are equally close?

## Done means

Conviction is a defined 0–100 number from L1 distances, and an L1 tie has a locked rule.

## Type

grilling

## Status

closed

## Claimed by

user (chat)

## Blocked by

- [Scoring family](./01-scoring-family.md)

## Forge

- Gitea: TBD
- GitHub: TBD

## Answer

Conviction measures likeness to the winning prototype: `(1 − d1 / 2) × 100`, where `d1` is the L1 distance to that prototype and `2` is the L1 maximum between two share vectors in `[0, 1]` that sum to 1. Range is 0–100.

Label is still nearest L1. On a tie (two or more prototypes share `d1`), pick the **most central** on the order `far_left` — `left` — `center` — `right` — `far_right` (smallest distance to `center`). If centrality also ties (`left` vs `right`, or `far_left` vs `far_right`), pick the left-side label (lower index).
