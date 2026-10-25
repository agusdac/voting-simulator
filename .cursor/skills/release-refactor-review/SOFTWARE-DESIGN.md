# A Functional Philosophy of Software Design

Use this reference during post-change refactors. It translates the core ideas of *A Philosophy of Software Design* into a functional-programming style: minimize complexity, make interfaces simple, hide decisions inside modules, and prefer explicit data flow over scattered mutable behavior.

The goal is not to make code look "functional" for style points. The goal is to reduce cognitive load, make changes local, and make the next refactor easier.

## 1. Design Means Managing Complexity

Good software design minimizes complexity.

Complexity appears when code is:

- hard to understand
- hard to modify
- dependent on too much context
- full of hidden assumptions
- spread across too many places for one small change

Watch for three signals:

- **Change amplification**: a small behavior change requires edits in many files.
- **Cognitive load**: the reader must simulate too many branches, flags, states, or side effects.
- **Unknowns**: the behavior depends on implicit ordering, hidden mutation, ambient state, or undocumented conventions.

Functional design helps because it favors explicit inputs, explicit outputs, small transformations, and narrow effect boundaries. When data flow is visible, fewer facts need to live in the reader's head.

## 2. Modules Are Design Decisions

A module should hide one important decision.

Good module boundaries answer questions like:

- How do we store or fetch this data?
- How do we normalize this payload?
- How do we call this external API?
- How do we map product intent into execution parameters?
- How do we recover from failures?

If that decision leaks, callers duplicate knowledge and future changes spread sideways.

Functional modules should expose behavior as stable functions over domain data. They should hide representation, orchestration details, retries, adapters, and validation rules unless those details are the actual public contract.

## 3. Prefer Deep Modules

A deep module has a small interface and a useful implementation.

Good:

```ts
const result = await processRequest(input)
```

The caller does not need to know how input is validated, how defaults are applied, how records are persisted, or how external service payloads are shaped.

Shallow:

```ts
const result = await processRequest(input, validator, storageClient, retryMode, notificationMode)
```

The caller is forced to understand implementation choices. That is leaked complexity.

During refactors, prefer fewer public functions with richer internal ownership over many tiny wrappers that only rename one line of work.

## 4. Interfaces Matter More Than Implementations

Spend design effort on interfaces first.

Implementation is private and can improve later. Interfaces become dependency points. A bad interface spreads complexity through every caller.

A good interface is:

- **Simple**: few concepts, few parameters, clear names.
- **Complete**: callers should not perform setup steps that the module itself can own.
- **Hard to misuse**: invalid states should be hard to represent.
- **Domain-shaped**: accepts and returns product concepts, not integration internals.
- **Effect-aware**: pure transformations and side effects are separated where practical.

Prefer:

```ts
evaluateAccess({ subject, policy })
```

Over:

```ts
checkAccess(subject, roleMap, featureFlags, regionRules, fallbackMode)
```

The first interface names the domain decision. The second exposes the mechanism.

## 5. Hide Information Aggressively

Information hiding is the foundation of deep modules.

Hide:

- storage details
- external service payload shapes
- cache strategy
- retry policy
- validation order
- derived field rules
- normalization quirks
- framework transport details

Expose:

- stable domain inputs
- stable domain outputs
- intentional errors
- small public capabilities

If multiple modules know the same detail, the detail is not hidden. Find the real owner and move the knowledge there.

## 6. Pull Complexity Downward

Top-level flows should read like product logic.

Bad top-level flow:

```ts
if (hasSpecialCase) {
  if (region === "x") {
    // apply regional rule
  }
  if (requiresManualReview) {
    // adjust status
  }
}
```

Better:

```ts
const decision = evaluateAccess({ subject, policy })
```

Lower-level modules can carry complexity when they hide it behind a stable interface. This keeps handlers, presentation code, and feature workflows obvious.

## 7. Functional Core, Imperative Shell

Use a functional core for decisions and an imperative shell for effects.

Functional core:

- parses
- normalizes
- validates
- maps
- derives
- compares
- selects
- formats

Imperative shell:

- reads request bodies
- calls databases
- calls external APIs
- logs
- writes files
- mutates stores
- performs navigation

This split makes behavior easier to test and refactor. Pure functions should receive all needed data as parameters and return new values instead of mutating inputs or reading ambient state.

During cleanup, look for logic hidden inside handlers, components, stores, controllers, jobs, or API clients that can become a pure domain function.

## 8. Model Data Flow Explicitly

Functional code is clear when data moves through named transformations.

Prefer pipelines where each step has one purpose:

```ts
const normalized = normalizeInput(input)
const decision = evaluateRules(normalized)
const payload = createIntegrationPayload({ normalized, decision })
```

Avoid pipelines that become anonymous cleverness:

```ts
const payload = pipe(input, a, b, c, d)
```

If the reader cannot tell what each step means from the names, the pipeline hides complexity instead of reducing it.

## 9. Separate Policy From Mechanism

Policy decides what should happen. Mechanism performs how it happens.

Examples:

- Policy: which rules apply to this request.
- Mechanism: how rules are evaluated.
- Policy: whether an account can access a capability.
- Mechanism: how account state is fetched from storage.
- Policy: which external service should handle a request.
- Mechanism: how the external service request is serialized.

Do not mix policy and mechanism unless the module is intentionally small and private. When policy leaks into mechanism, callers start reimplementing rules. When mechanism leaks into policy, product logic becomes brittle.

## 10. Make Invalid States Hard To Represent

Functional design favors data shapes that encode invariants.

Prefer discriminated unions, narrow types, and explicit result shapes over loose objects with optional fields that only some branches understand.

Good:

```ts
type AccessDecision =
  | { status: "allowed"; permissions: Permission[] }
  | { status: "denied"; reason: string }
```

Risky:

```ts
type AccessDecision = {
  permissions?: Permission[]
  error?: string
  denied?: boolean
}
```

The first shape forces callers to handle the actual states. The second allows contradictory data.

## 11. Prefer Composition Over Configuration Flags

Boolean flags often reveal a shallow interface.

Avoid:

```ts
createRequestPayload(input, true, false, true)
```

Prefer:

```ts
createDraftPayload(input)
createActivationPayload(input)
createCancellationPayload(input)
```

Or pass a named capability object when the variation is a real domain concept:

```ts
createRequestPayload({ input, capabilities })
```

Use composition when behaviors can be built from smaller transformations. Use separate functions when flags represent separate use cases.

## 12. Dependencies Are Design Pressure

Dependencies create coupling and change propagation.

Reduce dependency pressure by:

- depending on domain types instead of integration payloads
- keeping framework APIs at the shell
- moving shared rules into one owner
- avoiding imports from layers that should not know each other
- passing data explicitly instead of reading globals

For application code, this usually means:

- presentation code calls public application APIs, not persistence or transport internals
- request handlers delegate to services or use-case modules
- services own business rules and effect orchestration
- pure shared helpers live near the domain they serve, not in broad catch-all utility files
- integration-specific code stays behind adapter or gateway modules

## 13. Code Should Be Obvious, Not Clever

Readable functional code is explicit, boring, and named after domain behavior.

Avoid cleverness such as:

- dense point-free pipelines
- generic helpers that hide business meaning
- callback stacks where control flow is hard to see
- mutation disguised inside innocent function names
- abstractions that only save a few characters

Prefer names that explain product intent:

- `evaluateAccess`
- `normalizeInput`
- `createIntegrationPayload`
- `mapStateToPermissions`

If a function changes state, performs I/O, or throws, its name and layer should make that unsurprising.

## 14. Strategic Refactoring

Working code is not the same as good design.

Tactical programming optimizes for "make it pass now." Strategic programming pays down complexity while behavior is still fresh in the mind.

During a release refactor:

- preserve behavior unless the user explicitly allows fixes
- remove duplicated knowledge, not just duplicated lines
- simplify interfaces before polishing internals
- move decisions to their real owner
- make pure rules testable outside framework shells
- delete accidental abstractions when direct code is clearer

The best refactor often makes fewer concepts visible.

## 15. Practical Functional Heuristics

Use these checks while reviewing changed code:

- Can this branchy logic become a named pure function?
- Can this mutation become a returned value?
- Can this optional-field object become a discriminated union?
- Can integration details move behind a domain interface?
- Can a handler, component, or controller stop knowing a workflow step?
- Can repeated constants or field names move to the module that owns the concept?
- Can a boolean flag become a separate function or capability object?
- Can top-level orchestration read as a sequence of domain actions?
- Can this helper stay local because reuse is speculative?
- Can this shared helper be deleted because an existing owner already exists?

## 16. Anti-Patterns

Treat these as design smells:

- functions with many positional arguments
- boolean flags that change behavior significantly
- shared mutable objects passed through many functions
- modules that expose integration, storage, or framework internals
- components that know server-side business rules
- request handlers that contain domain workflows
- services that return transport-specific response shapes
- generic `utils` that mix unrelated decisions
- pure-looking functions that mutate input
- abstractions created before there are real call sites

## 17. Final Mental Model

Make interfaces simple. Push complexity into the module that owns the decision. Keep product rules as pure data transformations when possible. Keep effects at the edges.

For any product or platform:

- Complex workflows should be deep modules, not scattered conditional logic.
- External service complexity should be hidden behind domain functions.
- Parsing, validation, and mapping rules should be explicit transformations.
- Data access should be encapsulated behind clear ownership boundaries.
- Presentation code should express user flow, not integration or persistence mechanics.

If changing one feature requires understanding five unrelated services, complexity is leaking. The refactor target is not just less code; it is fewer visible decisions.