# Scenario document shape

## Question

What must a v0.1 JSON scenario contain (parties, voters, seed, and how they are listed)?

## Done means

The required keys and how N and M are derived from the file are locked.

## Type

grilling

## Status

closed

## Claimed by

user (chat)

## Blocked by

- [JSON vs existing inputs](./01-json-and-existing-inputs.md)

## Forge

- Gitea: TBD
- GitHub: TBD

## Answer

Explicit lists. The file has optional `seed`, `parties` (array of objects), and `voters` (array of objects). N = length of `parties`, M = length of `voters`. Objects are the extension point because later complexity is deterministic characteristics on those entities.
