from dataclasses import dataclass

from entities.political_party import PoliticalParty


@dataclass
class Voter:
    id: int
    vote: PoliticalParty | None = None
    age: float = 0.0
    dependents: float = 0.0
    urban: float = 0.0
    health_status: float = 0.0
    education_level: float = 0.0
    veteran: float = 0.0
    gender: float = 0.0
