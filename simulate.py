import json
from dataclasses import dataclass
from pathlib import Path
from random import Random

from entities import PoliticalParty, Voter


@dataclass(frozen=True)
class ElectionResult:
    parties: tuple[PoliticalParty, ...]
    raw_votes: tuple[tuple[Voter, PoliticalParty], ...]
    counts: dict[int, int]
    winner: PoliticalParty | None
    tied: tuple[PoliticalParty, ...]


def _elect(
    parties: tuple[PoliticalParty, ...],
    voter_ids: list[int],
    seed: int | None,
) -> ElectionResult:
    rng = Random(seed)
    raw_votes = []
    for voter_id in voter_ids:
        party = rng.choice(parties)
        voter = Voter(id=voter_id, vote=party)
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


def simulate(
    n_parties: int,
    n_voters: int,
    seed: int | None = None,
) -> ElectionResult:
    if n_parties < 1 or n_voters < 1:
        raise ValueError("n_parties and n_voters must be >= 1")
    parties = tuple(PoliticalParty(id=i) for i in range(1, n_parties + 1))
    return _elect(parties, list(range(1, n_voters + 1)), seed)


def simulate_from_scenario(path: str | Path) -> ElectionResult:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    try:
        party_items = data["parties"]
        voter_items = data["voters"]
        parties = tuple(PoliticalParty(id=item["id"]) for item in party_items)
        voter_ids = [item["id"] for item in voter_items]
    except KeyError as exc:
        raise ValueError("scenario must include parties and voters with id") from exc
    if not parties or not voter_ids:
        raise ValueError("parties and voters must be non-empty")
    return _elect(parties, voter_ids, data.get("seed"))
