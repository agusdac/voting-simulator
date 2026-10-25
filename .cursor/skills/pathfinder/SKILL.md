---
name: pathfinder
description: >-
  Find the way through foggy product work — chart a forge-backed decision map
  (grill, research, prototype, task), resolve tickets one at a time, then write
  slim release-ready brief + spec. Use when the user wants to plan a feature,
  pathfind, wayfind, chart a decision map, resolve planning tickets, write a
  feature brief or spec, pick a release version, update the product changelog,
  or any pre-implementation planning — even if they say wayfinder or feature-planner.
---

# Pathfinder

Senior Product Architect + navigator. Turn a loose idea into a **decision-complete route**, then into **slim `product/` docs** ready for [fire-in-the-hole](../fire-in-the-hole/SKILL.md).

```
idea → Phase A Pathfind (decisions) → Phase B Contract (brief + spec) → fire-in-the-hole
```

**Plan, don't do.** Destination is locked decisions + docs, not shipped code — unless Notes override. **Invoke, don't absorb:** [grill-me](../grill-me/SKILL.md), [research](../research/SKILL.md), [prepare-tea](../prepare-tea/SKILL.md).

Templates, versioning, and forge ops detail → [reference.md](reference.md).

## Mode

Pull from chat first. Ask only what's missing.

| Signal | Mode |
|--------|------|
| Loose idea / "plan this" / no map | **Chart** (start Phase A) |
| Map URL, issue #, or `product/plans/<slug>/` | **Work** (continue Phase A) |
| Map clear / "write the spec" / "consolidate" | **Consolidate** (Phase B) |
| Tiny change, way clear after a short grill | **Fast path** — skip map, Phase B only |

Never resolve more than **one** decision ticket per session (exception: fire all open `research` tickets in parallel when charting).

## Principles

- **Forge + local twin.** Canonical tickets live on the issue tracker; `product/plans/<slug>/` mirrors them. Neither drifts.
- **Map is an index.** Detail lives in the decision ticket once. Map / brief / spec only gist + link.
- **Fog of war.** Ticket only when the question is sharp. Dim in-scope questions stay in **Not yet specified** until they sharpen.
- **Done means.** Every ticket states, in one or two sentences, what is true when that ticket is finished. Close it only when that sentence holds.
- **Refer by name.** Human prose uses ticket titles (link wraps id/URL). Never a wall of bare `#42`.
- **One target version** per feature (`_changelog.json` + version folder + brief).
- **Workspace-scoped** data and auth are non-negotiable.

---

# Phase A — Pathfind

Tickets are **questions whose answer is a decision**, not build slices.

## Destination

Name it first (grill-me / domain modeling): what "done pathfinding" looks like — usually decision-complete brief + slim spec ready for fire-in-the-hole. Destination fixes scope.

## Layout (improved)

Keep decisions as **one file each forever**. Do **not** flatten into a single `decisions.md` after consolidate — the map's Decisions so far is the readable index; files hold the Answer.

```text
product/plans/<slug>/
  map.md                      # index (local twin of forge map issue)
  decisions/
    01-<title-slug>.md        # one decision ticket; keep after close
  assets/
    01-<title-slug>.md        # research / prototype; same NN as parent ticket when linked
product/issues/<n>.md         # forge mirrors (prepare-tea / gh)
product/features/<slug>.md    # Phase B brief
product/specs/<slug>.md       # Phase B slim spec
product/vX.Y.Z/               # release folder + _changelog.json entry
```

Legacy `.plan/<slug>/` remains valid; new work uses `product/plans/<slug>/`.

### Map body

Open tickets are **not** listed — query forge children / open files in `decisions/`. Frontier = open + unblocked + unclaimed.

```markdown
## Destination

<one or two lines — every session orients here>

## Notes

<domain; skills; forge URLs; version + slug; standing prefs; plan-don't-do unless overridden>

## Decisions so far

- [<closed title>](./decisions/01-....md) ([Gitea #N](url) · [GitHub #M](url)) — <one-line gist>

## Not yet specified

<!-- in-scope fog not sharp enough to ticket -->

## Out of scope

<!-- ruled out; never graduates; link closed mis-scoped tickets -->
```

### Decision ticket body

```markdown
## Question

<the decision or investigation>

## Done means

<one or two sentences: what is true when this ticket is finished>

## Type

grilling | research | prototype | task

## Status

open | closed

## Claimed by

<!-- assignee / none -->

## Blocked by

- <other ticket titles or none>

## Forge

- Gitea: <url or TBD>
- GitHub: <url or TBD>

## Answer

<!-- filled on resolution -->
```

Assets link from the ticket; never paste research into the map.

## Ticket types

| Type | Mode | What |
|------|------|------|
| **grilling** | HITL | Default. One question at a time via grill-me. Agent never answers for the human. |
| **research** | AFK | Primary-source facts via research skill → `assets/` + pointer on ticket. |
| **prototype** | HITL | Cheap concrete artifact under `assets/` to react to. Not product implementation. |
| **task** | HITL/AFK | Manual work that unblocks a *decision* (signup, access, sample data). Not an OR-* build ticket. |

**Fog vs ticket vs out of scope**

- **Ticket** — question already sharp (even if blocked).
- **Not yet specified** — can't phrase it sharply yet; don't pre-slice fog into fake tickets.
- **Out of scope** — beyond destination; close mis-scoped tickets; one map line with why; not in Decisions so far.

## Chart (new effort)

1. **Grill → destination**; propose `slug` + target **version** (see [reference.md](reference.md#versioning)). Confirm version before forge noise.
2. Breadth-first grill: open decisions + first takeable steps. **No fog** and journey fits one session → Fast path. Ask how to proceed.
3. Create `product/plans/<slug>/map.md`.
4. Create sharp tickets under `decisions/`; each includes **Done means** (one or two sentences). Wire **Blocked by** in a second pass.
5. **Forge** (ask once if not standing pref): map + children via prepare-tea (Gitea `minerva`) and `gh` when `origin` is GitHub. Mirror `product/issues/`. Labels: `pathfinder:map` / `pathfinder:<type>` (+ a default label). Accept legacy `wayfinder:*` on existing issues.
6. Fire **research** subagents in parallel for each research ticket (throwaway `research/<name>` branch OK; findings in `assets/`).
7. Stop — charting does not hand-resolve grilling / prototype / task.

## Work (continue)

1. Load **map.md** only. Zoom related closed tickets on demand.
2. Pick ticket: user-named, else first frontier item. **Claim** first (forge assignee = claim; note Claimed by locally).
3. Resolve by type. Consult Notes skills. If in doubt → grill-me.
4. Write **Answer** only when **Done means** is true. Status closed, forge resolution comment + close, refresh `product/issues/<n>.md`, append Decisions so far gist.
5. Graduate fog → new tickets (create-then-wire); rule out-of-scope discoveries; fix invalidated tickets.
6. Stop after one ticket (research exception).

When no open in-scope tickets remain and Not yet specified is empty (or only Phase B detail) → **destination met** → offer Consolidate.

---

# Phase B — Contract

Write the contract from Decisions so far — gist + link, never rewrite the debate.

1. Confirm version wiring ([reference.md](reference.md#versioning)).
2. Write slim **brief** `product/features/<slug>.md`.
3. Write slim **spec** `product/specs/<slug>.md` (split only if >~400 lines or huge API).
4. Wire `_changelog.json` + `product/<version>/changelog.md` + `overview.md`.
5. Hand off: do **not** auto-start TDD. User invokes fire-in-the-hole. Name the first OR-* ticket and behaviors it unlocks.

### Brief (keep short)

| Section | Content |
|---------|---------|
| **Version** | Target + one-line placement rationale |
| **Plan** | Link map + forge map URLs |
| **Description** | 2–3 sentences |
| **Value** | Why it matters |
| **Primary User Stories** | 2–5 outcomes |
| **Requirements** | Concrete, testable |
| **Constraints** | Tenant, audit, security |
| **Dependencies** | What must land first |

### Spec skeleton

```markdown
# <Feature title>

## Version & scope
## Decisions locked
<!-- gist + link per closed decision — no restated debate -->
## User stories & flows
## Architecture touchpoints
## API          <!-- only if Decisions so far locked it; else omit -->
## Schema       <!-- ditto -->
## Behaviors    <!-- user can… when… / system… given…; risk order -->
## Build tickets
<!-- OR-1… vertical slices — not decision tickets -->
```

Each OR ticket: title, goal, scope, deps, **Done means** (one or two sentences of what finished looks like), checklist. Foundation → delivery.

### Done checks

- Every brief requirement maps to ≥1 Behavior
- Build tickets executable without re-opening product questions
- Open product questions stay on the map, never hidden in the spec
- Decision files under `decisions/` remain; map indexes them

### Fast path

Small effort, no fog: skip `product/plans/`. Brief + slim spec + version wiring. Major choices as inline bullets under **Decisions locked**.

---

# Handoffs

| Need | Skill |
|------|--------|
| Stress-test a decision | grill-me |
| Primary-source facts | research |
| Create/close/mirror forge issues | prepare-tea (+ `gh`) |
| Implement OR-* slices | fire-in-the-hole |
| Red-green-refactor during build | tdd |

Aliases: `/wayfinder` and `/feature-planner` route here.
