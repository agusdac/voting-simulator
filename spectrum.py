import math
from dataclasses import replace

from entities import PoliticalParty

LABELS = ("far_left", "left", "center", "right", "far_right")

PROTOTYPES: dict[str, dict[str, float]] = {
    "far_left": {
        "health": 0.18,
        "education": 0.16,
        "infrastructure": 0.08,
        "defense": 0.02,
        "social_protection": 0.22,
        "environment": 0.12,
        "housing": 0.14,
        "research": 0.06,
        "public_order": 0.02,
    },
    "left": {
        "health": 0.16,
        "education": 0.15,
        "infrastructure": 0.10,
        "defense": 0.05,
        "social_protection": 0.18,
        "environment": 0.10,
        "housing": 0.12,
        "research": 0.08,
        "public_order": 0.06,
    },
    "center": {
        "health": 0.12,
        "education": 0.12,
        "infrastructure": 0.14,
        "defense": 0.10,
        "social_protection": 0.12,
        "environment": 0.08,
        "housing": 0.10,
        "research": 0.10,
        "public_order": 0.12,
    },
    "right": {
        "health": 0.10,
        "education": 0.10,
        "infrastructure": 0.14,
        "defense": 0.18,
        "social_protection": 0.08,
        "environment": 0.05,
        "housing": 0.08,
        "research": 0.08,
        "public_order": 0.19,
    },
    "far_right": {
        "health": 0.08,
        "education": 0.07,
        "infrastructure": 0.12,
        "defense": 0.28,
        "social_protection": 0.04,
        "environment": 0.02,
        "housing": 0.05,
        "research": 0.06,
        "public_order": 0.28,
    },
}


def _l1(a: dict[str, float], b: dict[str, float]) -> float:
    return sum(abs(a[name] - b[name]) for name in a)


def classify(party: PoliticalParty) -> PoliticalParty:
    party.require_valid_shares()
    shares = party.shares()
    distances = {label: _l1(shares, PROTOTYPES[label]) for label in LABELS}
    d1 = min(distances.values())
    tied = [
        label
        for label in LABELS
        if math.isclose(distances[label], d1, abs_tol=1e-9)
    ]
    center = LABELS.index("center")
    label = min(
        tied,
        key=lambda item: (abs(LABELS.index(item) - center), LABELS.index(item)),
    )
    conviction = (1 - d1 / 2) * 100
    return replace(party, spectrum=label, conviction=conviction)
