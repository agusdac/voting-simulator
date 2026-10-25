# Linear vote rule

## Question

How do party spend shares and voter traits produce a ballot (score, pick-max, noisy linear, leftover random)?

## Done means

The mapping from those fields to a single party choice is locked, including what seed still does.

## Type

grilling

## Status

closed

## Claimed by

user (chat)

## Blocked by

- [Party and voter fields](./01-party-and-voter-fields.md)

## Forge

- Gitea: TBD
- GitHub: TBD

## Answer

Traits map linearly to 9 budget weights; each party's score is the dot product with its GDP shares. The voter picks **argmax**. Seed does not affect the vote. Score ties use the existing tied list (no unique winner).
