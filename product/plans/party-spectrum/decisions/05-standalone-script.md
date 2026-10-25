# Standalone script

## Question

Is the classify script a deliverable of this feature now (same version as the module), and what command runs it?

## Done means

The script is in this version’s build, not a later map, and callers know the command and what it prints.

## Type

grilling

## Status

closed

## Claimed by

user (chat)

## Blocked by

- [Label surface](./03-label-surface.md)

## Forge

- Gitea: TBD
- GitHub: TBD

## Answer

Yes — prepare it in this feature, not later. Command: `uv run python classify.py --scenario <path>`. It loads the JSON parties, runs the classify module (not `simulate`), and prints each party `id`, `spectrum`, and `conviction`. Same share constraints as the scenario path; invalid shares do not classify.
