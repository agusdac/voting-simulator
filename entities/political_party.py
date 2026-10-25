import math
from dataclasses import dataclass

SHARE_NAMES = (
    "health",
    "education",
    "infrastructure",
    "defense",
    "social_protection",
    "environment",
    "housing",
    "research",
    "public_order",
)


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
    spectrum: str | None = None
    conviction: float | None = None

    def shares(self) -> dict[str, float]:
        return {name: getattr(self, name) for name in SHARE_NAMES}

    def require_valid_shares(self) -> None:
        values = self.shares()
        for value in values.values():
            if not 0 <= value <= 1:
                raise ValueError("GDP shares must be in [0, 1]")
        if not math.isclose(sum(values.values()), 1.0, abs_tol=1e-9):
            raise ValueError("a party's GDP shares must sum to 1")

    @classmethod
    def from_mapping(cls, item: dict) -> "PoliticalParty":
        try:
            party = cls(
                id=item["id"],
                **{name: item[name] for name in SHARE_NAMES},
            )
        except KeyError as exc:
            raise ValueError("party must include id and all GDP shares") from exc
        party.require_valid_shares()
        return party
