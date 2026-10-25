from dataclasses import dataclass
from random import Random

from entities import PoliticalParty, Voter


@dataclass(frozen=True)
class ElectionResult:
    parties: tuple[PoliticalParty, ...]
    raw_votes: tuple[tuple[Voter, PoliticalParty], ...]
    counts: dict[int, int]
    winner: PoliticalParty | None
    tied: tuple[PoliticalParty, ...]


def simulate(
    n_parties: int,
    n_voters: int,
    seed: int | None = None,
) -> ElectionResult:
    if n_parties < 1 or n_voters < 1:
        raise ValueError("n_parties and n_voters must be >= 1")
    rng = Random(seed)
    parties = tuple(PoliticalParty(id=i) for i in range(1, n_parties + 1))
    raw_votes = []
    for i in range(1, n_voters + 1):
        party = rng.choice(parties)
        voter = Voter(id=i, vote=party)
        raw_votes.append((voter, party))
    counts = {party.id: 0 for party in parties}
    for _, party in raw_votes:
        counts[party.id] += 1
    top = max(counts.values())
    leaders = tuple(party for party in parties if counts[party.id] == top)
    winner = leaders[0] if len(leaders) == 1 else None
    tied = () if winner is not None else leaders
    return ElectionResult(
        parties=parties,
        raw_votes=tuple(raw_votes),
        counts=counts,
        winner=winner,
        tied=tied,
    )
