---
name: release-refactor-review
description: After implementing or editing code, run an ambitious behavior-preserving cleanup that maps a concrete changelog version in `product/` to the related changes, then searches repo-wide for reuse, simpler interfaces, stronger module boundaries, and code-judo opportunities that delete incidental complexity. Use for post-change refactors, horizontal DRY passes, strict maintainability/design cleanup, interface or module consolidation, architecture deepening, or alignment of "what just changed" with a planned release. When multiple deepening candidates exist, present them inline and ask which to pursue. If the refactor boundary, behavior freeze, or public contract is unclear, run a short clarification loop focused only on the missing decisions.
---

# Post-change reuse and design cleanup

You are doing a **horizontal** cleanup pass: changed code is the anchor, the **whole repo** is the search space for reuse, and the target changelog version in `product/` is the product-intent guardrail. Prefer deleting, merging, or rewiring to existing building blocks over adding new parallel implementations.

This skill is not only about removing duplicate code. It is also about **deepening opportunities** — refactors that turn shallow modules into deep ones — for testability, clearer ownership, and easier navigation.

Read `SOFTWARE-DESIGN.md` for the functional philosophy (deep modules, information hiding, functional core). Use the vocabulary below in every suggestion — do not drift into generic "component," "service," "API," or "boundary" when a precise term applies.

Assume the implementation is wrong and sub-optimal. Be ambitious when a clear restructuring can delete concepts, branches, flags, wrappers, or layers rather than merely rearrange them. Call this a **code-judo move**: using the existing architecture more effectively so the simpler implementation feels inevitable in hindsight.

## Architecture vocabulary

Use these terms exactly:

| Term | Meaning |
|------|---------|
| **module** | A unit that hides one important decision behind a public surface |
| **interface** | The public contract callers depend on — the test surface |
| **depth** | How much useful work a module hides behind a simple interface |
| **seam** | A boundary where one module ends and another begins; where tests can plug in |
| **adapter** | Code that translates between a module's interface and an external system |
| **leverage** | How much future change one refactor unlocks relative to its cost |
| **locality** | Whether related logic lives together so a change stays in one place |

Principles:

- **Deletion test**: Would deleting this module concentrate complexity into a clearer owner, or just move it? "Concentrates" signals a real deepening opportunity.
- **Concept-count test**: Did the refactor reduce the concepts a reader must hold, or only move them?
- **The interface is the test surface**: If you cannot test behavior through the public interface, the seam is wrong or the module is too shallow.
- **One adapter = hypothetical seam; two adapters = real seam**: Do not extract adapter layers for a single integration; wait until a second caller or integration proves the boundary.

Domain language in `CONTEXT.md` names good seams. ADRs in `docs/adr/` record decisions this skill must not re-litigate without cause.

## When to use this skill

- Right after a feature slice, before merge, or when the user points at "what I just changed."
- When new code **reimplements** something that already exists: helpers, composables, validators, service calls, endpoint orchestration, DTOs, shared types, wrappers, or tiny modules.
- When the user wants **fewer lines** without changing product behavior.
- When the user wants a cleanup focused on **design**, **interfaces**, **modules**, **ownership**, **depth**, or **architecture**, not just DRY.
- When the user wants the cleanup tied to a specific release or feature already tracked in `product/`.
- When friction in the change set suggests **shallow modules**, **leaky seams**, or **missing locality**.

## When not to use

- Greenfield code with no clear duplication, no concrete change set, and no stable extraction target.
- Behavioral bugs or missing tests that must be solved first; this skill assumes behavior is correct or explicitly frozen.
- Broad speculative rewrites detached from a real diff, feature, or version anchor.

## Workflow

### 1. Lock the refactor anchor

Establish two anchors before editing:

1. The **change set**.
2. The **target product version** in `product/`.

Default precedence:

- Explicit file list, commit range, feature slug, or version from the user.
- `git diff` against the merge base or the **last 1–3 commits** if the user said "what I just changed."
- A concrete feature slug or touched files under `product/specs/` or `product/features/`.
- The newest `unreleased` or `frozen` version in `product/features/_changelog.json` only if the cleanup is clearly about current shipping work.

Always read `product/features/_changelog.json` and map the cleanup to a specific version. Record:

- target version
- feature slug(s), if known
- in-scope file list
- behavior freeze: strict freeze, cleanup-only, or small safe interface changes allowed

If you cannot confidently map the cleanup to a version, ask before editing.

### 2. Read domain context and product intent

Before exploring code, read:

- `CONTEXT.md` — domain glossary and good seam names (create lazily if missing)
- `docs/adr/` — ADRs for the area you are touching
- `product/features/_changelog.json`
- `product/<version>/overview.md` and `product/<version>/changelog.md`
- relevant `product/features/<slug>.md`, and `product/specs/<slug>.md` or `product/specs/<slug>/spec.md`, when the feature slug is known

Use **CONTEXT.md vocabulary** for domain concepts and the architecture vocabulary above for structure. If `CONTEXT.md` defines "Order," talk about "the Order intake module" — not internal handler names.

Open the **entire** touched files, not only the diff hunk. These docs are guardrails: the cleanup should make the implementation **clearer and easier to ship**, not silently drift from planned behavior.

### 3. Explore for friction and deepening opportunities

Walk the change set and its neighbors organically. Note where you experience friction:

- Understanding one concept requires bouncing between many small modules
- Modules are **shallow** — interface nearly as complex as the implementation
- Pure functions were extracted for testability, but real bugs hide in how they are wired (**locality** failure)
- Tightly-coupled modules leak across their **seams**
- Parts are untested or hard to test through the current **interface**
- A single **adapter** was extracted prematurely (hypothetical seam)
- Ad-hoc conditionals, nullable modes, booleans, casts, or fallbacks obscure an invariant
- A changed file crosses 1,000 lines, unless cohesion gives a compelling reason
- Independent effects are serialized, or related writes can leave partially applied state

Apply the **deletion test** to anything suspicious. Apply the horizontal discovery table below for every meaningful chunk.

| Signal in the change | Search strategy |
|----------------------|-----------------|
| HTTP / `$fetch` / `useFetch` | Same path, method, payload, or response shape; existing composables, services, or stores |
| Validation / normalization | Same field names, errors, parsing, or `createError` patterns; `server/utils`, `shared/`, neighboring services |
| DB access in endpoints | `server/services/*.service.ts` or existing query helpers; endpoint stays thin |
| Interface / type duplication | Repeated DTOs, payload types, response shapes, domain vocabulary; find the real owner |
| Module boundary leaks | UI importing server-ish concepts, endpoints doing orchestration, services carrying transport details |
| Vue duplication | Existing base components, composables, or repeated template patterns |
| Pinia actions / orchestration | Repeated fetch-flow-state sequences before adding another store-local workflow |
| Tiny wrappers / micro-modules | Nearby modules with nearly identical responsibilities; merge when the split is artificial |
| Shallow modules | Interface with many parameters, flags, or setup steps the module should own internally |
| Branch / type growth | Repeated conditions, optional fields, casts, `any`, or `unknown`; seek an explicit invariant, typed model, or simpler default flow |
| Async writes / orchestration | Independent operations serialized unnecessarily; related updates lacking an atomic owner |

Use **semantic search** for behavioral, architectural, or ownership-based duplication. Use **grep** for exact strings, routes, types, and error messages.

### 4. Present candidates inline (when more than one deepening path exists)

When exploration surfaces **multiple** non-trivial deepening opportunities, summarize them in chat before implementing. Skip when there is one obvious cleanup or the user already picked a direction.

For each candidate, give a short block:

- **Name** — domain term from `CONTEXT.md`, not internal handler names
- **Strength** — `Strong`, `Worth exploring`, or `Speculative`
- **Files** — modules involved
- **Problem** — friction in vocabulary terms (shallow, leaky seam, missing locality)
- **Solution** — plain English of what would change
- **Benefits** — **locality**, **leverage**, and how tests improve through the **interface**
- **ADR note** (optional) — only when a candidate contradicts an ADR and friction is real enough to reopen (e.g. _"contradicts ADR-0007 — worth reopening because…"_)

End with your **top recommendation** — which candidate to tackle first and why — then ask: **"Which of these would you like to explore?"**

Do **not** propose final interfaces yet.

### 5. Clarification loop (when boundaries are unclear)

If the user has not picked a candidate, or repo exploration does not answer important constraints, run a short clarification loop before refactoring. Keep it sharp: **3–6 high-leverage questions max**.

Good triggers:

- Behavior freeze is unclear
- Public **interfaces** that must stay stable are unclear
- Smallest diff vs stronger structural cleanup is unclear
- Multiple modules look like valid owners for the same behavior
- Version/feature mapping is ambiguous
- User picked a candidate but the deepened module shape is still open

Good question themes:

- Which version or feature should this cleanup stay inside?
- Are interface simplifications allowed if behavior stays the same?
- Which APIs, composables, or service functions are stable contracts?
- Optimize for fewer modules, stronger seams, or minimal risk?
- Is cross-feature extraction allowed, or stay inside one release slice?
- What sits behind the seam, and what tests should survive?

If the repo answers the question, do not ask it.

Side effects as decisions crystallize:

- **Naming a deepened module after a concept not in `CONTEXT.md`?** Add the term to `CONTEXT.md`.
- **Sharpening a fuzzy term during conversation?** Update `CONTEXT.md` inline.
- **User rejects a candidate with a load-bearing reason?** Offer to record an ADR: _"Want me to record this as an ADR so future reviews don't re-suggest it?"_ Only when the reason would help a future explorer — skip ephemeral ("not now") or self-evident rejections.

### 6. Run the design-focused cleanup review

For every meaningful chunk of changed logic, ask:

- Who should own this behavior?
- Is there one obvious public **interface**?
- Is the module **deep** enough, or is complexity leaking to callers?
- Are we duplicating contracts or naming the same concept differently across layers?
- Does the **seam** match the domain, or is it accidental?
- Is transport leaking into business logic, or persistence leaking into UI-facing code?
- Can two shallow modules become one clearer owner?
- Can a broad public surface become narrower without changing behavior?
- Does this refactor improve **locality** and **leverage** for the version we are shipping?
- Is there a **code-judo move** that deletes whole branches, modes, helpers, or layers?
- Did the change add special cases to a shared flow instead of extending its canonical owner?
- Can invalid states be removed with a narrower type instead of casts, optionality, or silent fallbacks?
- Is orchestration direct, parallel where work is independent, and atomic where state must change together?
- Did the diff push a file past 1,000 lines without a strong cohesion argument?

Prefer removing accidental complexity over extracting more helpers. Working code is not enough when a clear behavior-preserving structure is materially simpler.

### 7. Refactor decisions

- **Replace** a local copy with an existing function, composable, service, schema, or type when the contract already fits or fits with one thin **adapter**.
- **Merge** tiny modules when the split creates indirection without a meaningful **seam**.
- **Extract** a new shared helper or contract only if there are **at least two real call sites** now, or a clearly stable boundary the version needs.
- **Move** interfaces, types, and helpers to the layer that owns the concept.
- **Narrow** exports and public entry points when wide module surfaces create confusion.
- **Deepen** shallow modules by pulling setup, validation, and orchestration behind a simpler **interface**.
- **Reframe** the state or ownership model when doing so removes branches or concepts instead of centralizing the same spaghetti.
- **Type** real states explicitly when optional fields, casts, or loose objects hide invariants.
- **Parallelize** independent work and make related updates atomic when that also simplifies the orchestration.
- **Leave** code local when extraction would create speculative APIs, version-crossing coupling, or a fake abstraction.

Respect the user's rules: **no drive-by refactors** outside the change set unless the duplication or seam problem is directly coupled to the changed code.

### 8. Keep the version mapping explicit

When you report the cleanup, always state:

- target version
- feature slug(s), if any
- files treated as in scope
- what was deduplicated
- what **interface**, ownership, **seam**, or **depth** improved
- whether the cleanup stayed behavior-preserving

If the cleanup reveals a mismatch between code and mapped `product/` docs, flag it clearly. Update product docs only if the user asked for docs to stay in sync.

### 9. Verify

- Run relevant **lint** and **tests** for the touched area.
- Do not change public API or UX unless the user asked for it.
- Re-check that the cleanup still fits the mapped `product/` version and feature intent.

## Principles

- **Same behavior**: refactors are behavior-preserving unless the user explicitly allows fixes.
- **Version-aware**: anchor cleanup to one concrete version in `product/`, not vague "recent work."
- **Shorter, clearer, deeper, better owned**: fewer lines, simpler **interfaces**, stronger **seams**, one obvious path.
- **Design over churn**: prefer better module **depth** and **locality** over cosmetic edits.
- **Project shape**: follow existing Nuxt and server layout, shared services, and neighboring naming patterns.
- **Explain briefly**: say what now owns the logic and why the structure is better. No essay.

## Anti-patterns

- Renaming unrelated symbols or reformatting whole files "while you're here."
- Copy-pasting a giant helper into `utils` without checking for an existing owner.
- Extracting abstractions with only hypothetical reuse or a single **adapter** (hypothetical seam).
- Moving complexity without reducing concept count.
- Adding special-case branches, nullable modes, cast-heavy contracts, or silent fallbacks to shared flows.
- Letting a changed file cross 1,000 lines without testing whether decomposition improves cohesion.
- Keeping duplicate DTOs, validators, or wrappers just because they live in different folders.
- Refactoring across versions or features without checking the `product/` mapping first.
- Skipping clarification when public contracts or refactor boundaries are ambiguous.
- Re-litigating ADR decisions without concrete friction.
- Presenting handler or class names instead of domain terms from `CONTEXT.md`.

## Quick checklist before you finish

- [ ] Cleanup anchored to a concrete version from `product/features/_changelog.json`.
- [ ] In-scope changes and version mapping are explicit.
- [ ] `CONTEXT.md` and relevant ADRs were read; domain vocabulary used in suggestions.
- [ ] Every new API-ish or interface-ish block in the diff was searched for an existing owner or twin.
- [ ] Deletion test applied to shallow or suspicious modules.
- [ ] Code-judo and concept-count tests applied before settling for local cleanup.
- [ ] No unjustified 1,000-line crossing, ad-hoc branch growth, loose type boundary, sequential independent work, or partial-update flow.
- [ ] No new duplicate validation, transport contracts, or leaky seams introduced.
- [ ] Cleanup improved **depth**, **locality**, ownership, or **interfaces** — not just line count.
- [ ] Tests and lint still pass for touched packages.