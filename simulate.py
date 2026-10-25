import json
import math
from dataclasses import dataclass
from pathlib import Path
from random import Random

from affinity import SHARE_NAMES, TRAIT_NAMES, choose_party
from entities import PoliticalParty, Voter


@dataclass(frozen=True)
class ElectionResult:
    parties: tuple[PoliticalParty, ...]
    raw_votes: tuple[tuple[Voter, PoliticalParty], ...]
    counts: dict[int, int]
    winner: PoliticalParty | None
    tied: tuple[PoliticalParty, ...]


def _tally(
    parties: tuple[PoliticalParty, ...],
    raw_votes: list[tuple[Voter, PoliticalParty]],
) -> ElectionResult:
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
    return _tally(parties, raw_votes)


def simulate(
    n_parties: int,
    n_voters: int,
    seed: int | None = None,
) -> ElectionResult:
    if n_parties < 1 or n_voters < 1:
        raise ValueError("n_parties and n_voters must be >= 1")
    parties = tuple(PoliticalParty(id=i) for i in range(1, n_parties + 1))
    return _elect(parties, list(range(1, n_voters + 1)), seed)


def _parse_party(item: dict) -> PoliticalParty:
    try:
        shares = {name: item[name] for name in SHARE_NAMES}
        party_id = item["id"]
    except KeyError as exc:
        raise ValueError("party must include id and all GDP shares") from exc
    for value in shares.values():
        if not 0 <= value <= 1:
            raise ValueError("GDP shares must be in [0, 1]")
    if not math.isclose(sum(shares.values()), 1.0, abs_tol=1e-9):
        raise ValueError("a party's GDP shares must sum to 1")
    return PoliticalParty(id=party_id, **shares)


def _parse_voter(item: dict) -> Voter:
    try:
        traits = {name: item[name] for name in TRAIT_NAMES}
        voter_id = item["id"]
    except KeyError as exc:
        raise ValueError("voter must include id and all traits") from exc
    return Voter(id=voter_id, **traits)


def simulate_from_scenario(path: str | Path) -> ElectionResult:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    try:
        party_items = data["parties"]
        voter_items = data["voters"]
    except KeyError as exc:
        raise ValueError("scenario must include parties and voters") from exc
    parties = tuple(_parse_party(item) for item in party_items)
    voters = [_parse_voter(item) for item in voter_items]
    if not parties or not voters:
        raise ValueError("parties and voters must be non-empty")
    raw_votes = []
    for voter in voters:
        party = choose_party(voter, parties)
        if party is None:
            continue
        voter.vote = party
        raw_votes.append((voter, party))
    return _tally(parties, raw_votes)
