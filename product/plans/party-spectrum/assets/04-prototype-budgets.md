# Prototype budgets (locked)

Same constraints as `PoliticalParty`: each share in `[0, 1]`, nine shares sum to 1.

| share | far_left | left | center | right | far_right |
|---|---:|---:|---:|---:|---:|
| health | 0.18 | 0.16 | 0.12 | 0.10 | 0.08 |
| education | 0.16 | 0.15 | 0.12 | 0.10 | 0.07 |
| infrastructure | 0.08 | 0.10 | 0.14 | 0.14 | 0.12 |
| defense | 0.02 | 0.05 | 0.10 | 0.18 | 0.28 |
| social_protection | 0.22 | 0.18 | 0.12 | 0.08 | 0.04 |
| environment | 0.12 | 0.10 | 0.08 | 0.05 | 0.02 |
| housing | 0.14 | 0.12 | 0.10 | 0.08 | 0.05 |
| research | 0.06 | 0.08 | 0.10 | 0.08 | 0.06 |
| public_order | 0.02 | 0.06 | 0.12 | 0.19 | 0.28 |

Left of center leans `social_protection` / `health` / `housing` / `education` / `environment`. Right of center leans `defense` / `public_order`. `infrastructure` and `research` peak at center.

Adjacent L1 distances (spectrum is ordered; farther labels are farther):

| pair | L1 |
|---|---:|
| far_left ↔ left | 0.22 |
| left ↔ center | 0.34 |
| center ↔ right | 0.30 |
| right ↔ far_right | 0.38 |

Smoke on `examples/scenario.json` (illustration only; L1 ties unresolved):

| party | nearest | L1 to each (FL, L, C, R, FR) |
|---|---|---|
| 1 | **tie** far_left / left | 0.32, 0.32, 0.58, 0.80, 1.08 |
| 2 | right | 0.90, 0.72, 0.46, 0.24, 0.28 |
| 3 | left | 0.48, 0.40, 0.42, 0.60, 0.98 |
