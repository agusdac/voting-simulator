# Domain

- **Voter** — a member of the simulated electorate with raw traits (age, dependents, urban, health_status, education_level, veteran, gender).
- **Political party** — a ballot choice with id and nine GDP spend shares in `[0, 1]`.
- **Election result** — raw votes, per-party counts, and either a unique winner or a tie list.
- **simulate** — the callable model: N parties, M voters, optional seed.
- **JSON scenario** — a local file of `parties` and `voters` objects; another way to assemble a run. Extra keys are ignored until declared.
