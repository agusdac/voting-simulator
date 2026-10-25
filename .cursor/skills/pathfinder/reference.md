# Pathfinder reference

Read from [SKILL.md](SKILL.md) only when you need templates or forge/version detail.

---

## Versioning

Before release-facing docs:

1. Read `product/features/_changelog.json` (create if missing, newest-first shape below).
2. Propose target: latest `unreleased`, next planned, or new bump (patch / fix / minor / breaking). Confirm with user.
3. Append slug to that version's `features` array after confirmation.

```json
{
  "v0.3.0": {
    "status": "unreleased",
    "date": null,
    "theme": "Short phrase",
    "features": ["new-feature-slug"]
  }
}
```

`status`: `unreleased` | `released` | `frozen`. Never add features to `released`.

### Version folders

Ensure `product/<version>/` with:

- `changelog.md` — Keep-a-Changelog; one user-facing line linking `../features/<slug>.md`
- `overview.md` — theme, scope boundaries, index of feature slugs

---

## Forge conventions

Ask once per effort if forge sync is wanted (standing preference in map Notes wins).

### Labels

| Thing | Labels |
|-------|--------|
| Map issue | default (`enhancement` or `question`) + `pathfinder:map` |
| Decision child | default + `pathfinder:grilling` \| `research` \| `prototype` \| `task` |

Legacy `wayfinder:map` / `wayfinder:<type>` on existing issues remain valid — treat as aliases; don't relabel unless asked.

### Bodies

- Map title = feature destination name.
- Child title = decision question name (human-readable).
- Body includes: Question, **Done means** (one or two sentences of what finished looks like for that ticket), link to local `product/plans/<slug>/...`, **Working branch** line per prepare-tea.
- Blocking: use forge native dependency when available; else **Blocked by** in local ticket + forge body.
- Claim: assign on forge before work. Unassigned open = unclaimed.
- Resolve: resolution comment = Answer; close issue; refresh `product/issues/<n>.md`; append Decisions so far on map.

### Dual forge

This repo: Gitea via prepare-tea (`minerva`) + GitHub via `gh` when `origin` is GitHub. Put both URLs in map Notes and each ticket's Forge section.

### Research branches

Research subagents may capture findings on a throwaway `research/<name>` branch; the durable artifact is `product/plans/<slug>/assets/NN-<title-slug>.md` linked from the ticket.

---

## Decision file naming

- Zero-pad: `01-`, `02-`, …
- Slug from the ticket title (kebab-case).
- Matching research/prototype asset reuses the same `NN-` prefix when it belongs to that ticket.
- Never renumber closed tickets; new tickets take the next free NN.

---

## Spec split (rare)

Default: one file `product/specs/<slug>.md`.

Split into `product/specs/<slug>/{spec,api,schema,tests,tickets}.md` only if the single file would exceed ~400 lines or the API surface is large. Legacy multi-file specs stay valid — do not mandatorily migrate.

---

## Build ticket shape (OR-*)

```markdown
### OR-1 — <title>

- **Goal:** …
- **Scope:** …
- **Deps:** none | OR-N
- **Done means:** <one or two sentences: what is true when this ticket is finished>
- **Checklist:**
  - [ ] …
```

Prefer vertical slices. Foundation tickets only when later OR-* cannot proceed without them.

---

## Out-of-scope handling

When a ticket sits past the destination:

1. Close it (forge + local Status).
2. One line under map **Out of scope**: gist + why + link.
3. Do **not** put it in Decisions so far.

---

## Migration notes

| Old | New |
|-----|-----|
| `/wayfinder`, `/feature-planner` | `/pathfinder` |
| `wayfinder:*` labels | `pathfinder:*` (legacy accepted) |
| Flattened `decisions.md` after Phase B | Keep `decisions/NN-*.md`; map indexes |
| `.plan/<slug>/` | Prefer `product/plans/<slug>/` for new work |
