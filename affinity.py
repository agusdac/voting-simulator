from entities import PoliticalParty, Voter

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
TRAIT_NAMES = (
    "age",
    "dependents",
    "urban",
    "health_status",
    "education_level",
    "veteran",
    "gender",
)

_COEFFICIENTS: dict[str, dict[str, int]] = {
    "age": {"health": 1, "education": -1, "defense": 1, "social_protection": 1},
    "dependents": {
        "health": 1,
        "education": 1,
        "social_protection": 1,
        "housing": 1,
    },
    "urban": {"environment": 1, "housing": 1, "public_order": 1},
    "health_status": {"health": 1, "social_protection": 1},
    "education_level": {"education": 1, "environment": 1, "research": 1},
    "veteran": {"health": 1, "defense": 1, "public_order": 1},
    "gender": {"health": 1, "education": 1, "defense": -1, "social_protection": 1},
}


def _coefficient(trait: str, share: str) -> int:
    return _COEFFICIENTS.get(trait, {}).get(share, 0)


def budget_weights(voter: Voter) -> dict[str, float]:
    weights = {share: 0.0 for share in SHARE_NAMES}
    for trait in TRAIT_NAMES:
        value = getattr(voter, trait)
        for share in SHARE_NAMES:
            weights[share] += value * _coefficient(trait, share)
    return weights


def party_score(voter: Voter, party: PoliticalParty) -> float:
    weights = budget_weights(voter)
    return sum(weights[share] * getattr(party, share) for share in SHARE_NAMES)


def choose_party(
    voter: Voter, parties: tuple[PoliticalParty, ...]
) -> PoliticalParty | None:
    scored = [(party_score(voter, party), party) for party in parties]
    top = max(score for score, _ in scored)
    leaders = tuple(party for score, party in scored if score == top)
    if len(leaders) != 1:
        return None
    return leaders[0]
