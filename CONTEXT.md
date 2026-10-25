# Domain

- **Voter** — a member of the simulated electorate. Built to grow beyond a ballot.
- **Political party** — a ballot choice, identified by integer id `1..N` in v0.1.
- **Election result** — raw votes, per-party counts, and either a unique winner or a tie list.
- **simulate** — the callable model: N parties, M voters, optional seed.
