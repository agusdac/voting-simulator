# Extensible entity fields

## Question

How does the JSON carry extra party and voter characteristics so we can add fields later without changing the call shape?

## Done means

It is locked that party and voter objects in the file are the extension point, and how unused fields behave until a later version uses them.

## Type

grilling

## Status

closed

## Claimed by

user (chat)

## Blocked by

- [Scenario document shape](./02-scenario-document-shape.md)

## Forge

- Gitea: TBD
- GitHub: TBD

## Answer

Ignore extra keys. Party and voter objects are the extension point; undeclared fields are read and discarded. They do not live on `Voter` / `PoliticalParty` until a later version declares them. v0.1 voting still does not use them.
