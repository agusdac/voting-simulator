---
name: fire-in-the-hole
description: Kick off implementation after pathfinder has produced product docs. Use when the user says start development, kick off implementation, build the next ticket, implement this planned feature, ship the next slice, fire in the hole, or work from product/features and product/specs. Also use right after feature planning is done, when a slim spec exists and the user wants code. One build ticket at a time.
---

# Fire in the hole

Senior Implementation Lead. Turn pathfinder docs into code **one build ticket at a time**. Open in-scope decisions go back to pathfinder. This skill does not re-plan the feature.

## When

Use when a brief and a spec exist and the user wants the next slice built.

Do not use for planning (**pathfinder**), idea stress-tests (**grill-me**), or a cleanup-only pass (**release-refactor-review**).

## Before code

Pull from chat: feature slug, target version, named ticket, and whether forge, branch, or commit is allowed. If several features match, ask.

Read, in order. Docs win over chat memory.

1. `product/features/_changelog.json` — the version lists the slug.
2. `product/features/<slug>.md` — value, requirements, constraints, dependencies.
3. `product/plans/<slug>/map.md` or `.plan/<slug>/map.md` — if in-scope decision tickets are still open, stop.
4. Spec: `product/specs/<slug>.md`. Legacy folder: `product/specs/<slug>/` (`spec.md`, `api.md`, `schema.md`, `tests.md`, `tickets.md`). Read API and Schema only when this slice touches HTTP or persistence.

If the user contradicts the spec, confirm a doc update or an explicit override before editing.

Report: version, slug, ticket, and the behaviors it unlocks.

## One slice

From **Build tickets** (legacy: `tickets.md`): the first ticket whose **Done means** is not yet true, unless the user named one. Ask before reordering.

**Done means** is one or two sentences of what is true when that ticket is finished. State goal, scope, dependencies, and Done means. Confirm the boundary before editing unless they already named the ticket and said to proceed.

Stay inside that ticket. No later tickets, drive-by refactors, or decision-map tickets.

## Preflight

Flag blockers before the first edit. If tenant scope, auth, or schema ownership is unclear, run a short **grill-me** (3–6 questions). Do not guess.

| Area | Check |
|------|--------|
| Multi-tenant | Every read and write scoped by `workspaceId`. No cross-tenant data. |
| Auth | Endpoints and jobs reject missing or invalid auth. |
| Audit / logs | Trace state changes by ID. No raw PII, document body, embeddings, tokens, or secrets. |
| Retention | Deletes match the spec. |
| Injection / paths | Parameterized queries. Validated input at the edge. Allowlisted URLs. Sanitized object keys and file paths. |

Follow the repo: versioned `/api/v{n}` thin handlers, domain logic in packages, schemas in `packages/db`, Docker-first tests, `bun` / `bunx`.

## Forge

Create issues, branches, commits, or pushes only with explicit approval for that action.

An approved issue for this slice carries goal, scope, **Done means**, a link to the spec, and **Working branch**. Label `enhancement` unless it is a bug. No secrets or PII. If they decline issues, implement anyway.

## Build

Invoke **[tdd](../tdd/SKILL.md)** for the mapped behaviors: one observable test, the minimum code that passes it, repeat. No speculative APIs. If the spec and the code disagree, surface the gap before widening scope.

## Close

1. Lint and test the touched packages. Prefer the Compose commands CI uses.
2. Invoke **[release-refactor-review](../release-refactor-review/SKILL.md)** on the slice diff. Behavior stays the same.
3. Close only when **Done means** is true. Otherwise stop and propose a split or a pathfinder doc update.
4. Write **What landed** so a reader can see what the software now contains without opening the diff. For each file created or edited, one intuitive sentence: what that file adds or now holds, and the guard it enforces — e.g. "a function that receives a documentId and returns all its evidence for the workspace; checks the document exists before running". Name the responsibility, not the line count.
5. **Do not commit or push when a slice ends.** Every push spends PR CI quota; the user commits. Leave the work in the working tree and end the report with a **Proposed commit**: a subject line plus one or two body lines, ready to paste, without any AI attribution.
6. Forge follow-up waits for the user's commit: keep the slice issue open and the PR checklist unticked until the user says it is pushed, then close the issue with the real commit hash and **What landed** in the resolution comment.

Put **What landed** in the slice report and, once committed, in the resolution comment that closes the issue.

```markdown
## Slice complete

- **Version:** vX.Y.Z
- **Feature:** <slug>
- **Ticket:** <n> — <title>
- **Done means:** <the sentence, and that it now holds>
- **Behaviors covered:** <from Behaviors / tests.md>
- **Tests run:** <commands and result>
- **Forge:** issue stays open until the user commits
- **What landed:**
  - `path/to/file` — <what this file adds, in plain language, and what it checks>
- **Gaps:** <checklist still open, or none>
- **Next slice:** <next ticket, or feature complete>
- **Proposed commit:**

  ```
  <type>(<slug>): <ticket> — <subject>

  <one or two lines of body>
  ```
```

## Guardrails

- A spec for the slug exists: implement from it.
- Stay inside the selected ticket.
- No issues, branches, commits, or pushes without explicit approval — and never an automatic commit at the end of a slice (it spends PR CI quota); propose the commit instead.
- No skip of the preflight on persistence, auth, or tenant paths.
- Do not rewrite the spec mid-slice. Flag drift.
- Do not start a build ticket while in-scope decision tickets are still open.

## Handoffs

| Need | Skill |
|------|--------|
| Specs or open decisions | pathfinder |
| Red-green-refactor | tdd |
| Issues or releases | prepare-tea |
| Ambiguous design or security | grill-me |
| Reuse and module boundaries after the slice | release-refactor-review |
