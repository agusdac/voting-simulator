# Domain

- **Voter** — a member of the simulated electorate with raw traits (age, dependents, urban, health_status, education_level, veteran, gender).
- **Political party** — a ballot choice with id and nine GDP spend shares in `[0, 1]` that sum to 1. Optional `spectrum` and `conviction` after classification.
- **Spectrum** — left–right label (`far_left`, `left`, `center`, `right`, `far_right`) from nearest prototype budget in L1 distance.
- **Conviction** — 0–100 likeness to that prototype: `(1 − d1 / 2) × 100`.
- **classify** — maps a party’s shares to spectrum and conviction; not part of the election engine.
- **Election result** — raw votes, per-party counts, and either a unique winner or a tie list.
- **simulate** — the callable model: N parties, M voters, optional seed.
- **JSON scenario** — a local file of `parties` and `voters` objects; another way to assemble a run. Extra keys are ignored until declared.
