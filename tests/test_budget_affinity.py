import json

import pytest

from simulate import simulate, simulate_from_scenario

SHARES = (
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
TRAITS = (
    "age",
    "dependents",
    "urban",
    "health_status",
    "education_level",
    "veteran",
    "gender",
)


def _shares(**overrides):
    data = {name: 0.0 for name in SHARES}
    data.update(overrides)
    return data


def _traits(**overrides):
    data = {name: 0.0 for name in TRAITS}
    data.update(overrides)
    return data


def test_scenario_voter_with_health_need_votes_for_the_health_party(tmp_path):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "parties": [
                    {"id": 1, **_shares(health=1.0)},
                    {"id": 2, **_shares(defense=1.0)},
                ],
                "voters": [{"id": i, **_traits(health_status=1)} for i in range(1, 21)],
            }
        )
    )

    result = simulate_from_scenario(path)

    assert len(result.raw_votes) == 20
    assert {party.id for _, party in result.raw_votes} == {1}
    assert result.counts[1] == 20
    assert result.winner is not None
    assert result.winner.id == 1


def test_scenario_casts_no_ballot_when_a_voters_top_score_is_tied(tmp_path):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "parties": [
                    {"id": 1, **_shares(health=1.0)},
                    {"id": 2, **_shares(health=1.0)},
                ],
                "voters": [{"id": 1, **_traits(health_status=1)}],
            }
        )
    )

    result = simulate_from_scenario(path)

    assert result.raw_votes == ()
    assert result.counts == {1: 0, 2: 0}
    assert result.winner is None
    assert {party.id for party in result.tied} == {1, 2}


@pytest.mark.parametrize("bad_share", [-0.1, 1.1])
def test_scenario_rejects_shares_outside_unit_interval(tmp_path, bad_share):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "parties": [{"id": 1, **_shares(health=bad_share)}],
                "voters": [{"id": 1, **_traits()}],
            }
        )
    )

    with pytest.raises(ValueError):
        simulate_from_scenario(path)


def test_scenario_rejects_party_shares_that_do_not_sum_to_one(tmp_path):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "parties": [{"id": 1, **_shares(health=0.5)}],
                "voters": [{"id": 1, **_traits()}],
            }
        )
    )

    with pytest.raises(ValueError):
        simulate_from_scenario(path)


def test_simulate_flags_path_is_still_uniform_random():
    a = simulate(n_parties=3, n_voters=40, seed=1)
    b = simulate(n_parties=3, n_voters=40, seed=1)
    c = simulate(n_parties=3, n_voters=40, seed=2)

    assert [party.id for _, party in a.raw_votes] == [
        party.id for _, party in b.raw_votes
    ]
    assert [party.id for _, party in a.raw_votes] != [
        party.id for _, party in c.raw_votes
    ]
