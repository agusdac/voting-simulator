# Invocation surface

## Question

How is the simulator invoked in v0.1?

## Done means

v0.1 is locked as a Python function, a CLI, or both, and the input signature is known (N parties, later also M).

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

v0.1 is a **Python function + thin CLI**. The model is the function (inputs: N parties, M voters, optional seed). The terminal command only fires it.
