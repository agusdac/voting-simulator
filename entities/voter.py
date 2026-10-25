from dataclasses import dataclass

from entities.political_party import PoliticalParty


@dataclass
class Voter:
    id: int
    vote: PoliticalParty
