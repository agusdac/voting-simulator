import json

import pytest

from entities import PoliticalParty
from simulate import simulate, simulate_from_scenario
from spectrum import classify
from test_budget_affinity import _shares, _traits


def test_classify_matches_an_exact_far_left_prototype():
    party = PoliticalParty(
        id=1,
        health=0.18,
        education=0.16,
        infrastructure=0.08,
        defense=0.02,
        social_protection=0.22,
        environment=0.12,
        housing=0.14,
        research=0.06,
        public_order=0.02,
    )

    labeled = classify(party)

    assert labeled.spectrum == "far_left"
    assert labeled.conviction == 100.0


def test_classify_picks_the_more_central_label_on_an_l1_tie():
    party = PoliticalParty(
        id=1,
        health=0.25,
        education=0.2,
        infrastructure=0.1,
        defense=0.05,
        social_protection=0.2,
        environment=0.08,
        housing=0.07,
        research=0.03,
        public_order=0.02,
    )

    labeled = classify(party)

    assert labeled.spectrum == "left"
    assert labeled.conviction == 84.0


def test_classify_rejects_shares_that_do_not_sum_to_one():
    party = PoliticalParty(id=1, health=0.5)

    with pytest.raises(ValueError, match="sum to 1"):
        classify(party)


def test_classify_rejects_shares_outside_unit_interval():
    party = PoliticalParty(id=1, health=1.5, education=-0.5)

    with pytest.raises(ValueError, match=r"\[0, 1\]"):
        classify(party)


def test_simulate_from_scenario_does_not_classify_parties(tmp_path):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "parties": [{"id": 1, **_shares(health=1.0)}],
                "voters": [{"id": 1, **_traits()}],
            }
        )
    )

    result = simulate_from_scenario(path)

    assert result.parties[0].spectrum is None
    assert result.parties[0].conviction is None


def test_random_simulate_does_not_classify_parties():
    result = simulate(n_parties=2, n_voters=3, seed=1)

    assert all(party.spectrum is None and party.conviction is None for party in result.parties)
