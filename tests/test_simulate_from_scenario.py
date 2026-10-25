import json

import pytest

from simulate import simulate_from_scenario
from test_budget_affinity import _shares, _traits


def test_simulate_from_scenario_uses_parties_and_voters_from_the_file(tmp_path):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "seed": 1,
                "parties": [
                    {"id": 10, **_shares(health=1.0)},
                    {"id": 20, **_shares(defense=1.0)},
                ],
                "voters": [
                    {"id": 1, **_traits(health_status=1)},
                    {"id": 2, **_traits(health_status=1)},
                    {"id": 3, **_traits(health_status=1)},
                ],
            }
        )
    )

    result = simulate_from_scenario(path)

    assert {party.id for party in result.parties} == {10, 20}
    assert len(result.raw_votes) == 3
    assert {voter.id for voter, _ in result.raw_votes} == {1, 2, 3}
    assert {party.id for _, party in result.raw_votes} == {10}


def test_simulate_from_scenario_ignores_undeclared_entity_keys(tmp_path):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "seed": 1,
                "parties": [{"id": 1, "name": "Left", **_shares(health=1.0)}],
                "voters": [{"id": 1, "nickname": "Ada", **_traits(health_status=1)}],
            }
        )
    )

    result = simulate_from_scenario(path)

    party = result.parties[0]
    voter, _ = result.raw_votes[0]
    assert party.id == 1
    assert not hasattr(party, "name")
    assert voter.id == 1
    assert voter.health_status == 1
    assert not hasattr(voter, "nickname")


@pytest.mark.parametrize(
    "payload",
    [
        {"parties": [], "voters": [{"id": 1}]},
        {"parties": [{"id": 1}], "voters": []},
        {"voters": [{"id": 1}]},
        {"parties": [{"id": 1}]},
        {"parties": [{}], "voters": [{"id": 1}]},
        {"parties": [{"id": 1}], "voters": [{}]},
    ],
)
def test_simulate_from_scenario_does_not_run_when_the_file_is_invalid(tmp_path, payload):
    path = tmp_path / "scenario.json"
    path.write_text(json.dumps(payload))

    with pytest.raises(ValueError):
        simulate_from_scenario(path)
