from dataclasses import dataclass


@dataclass(frozen=True)
class PoliticalParty:
    id: int
    health: float = 0.0
    education: float = 0.0
    infrastructure: float = 0.0
    defense: float = 0.0
    social_protection: float = 0.0
    environment: float = 0.0
    housing: float = 0.0
    research: float = 0.0
    public_order: float = 0.0
