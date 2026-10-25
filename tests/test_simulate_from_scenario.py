import json

import pytest

from simulate import simulate_from_scenario


def test_simulate_from_scenario_uses_parties_and_voters_from_the_file(tmp_path):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "seed": 1,
                "parties": [{"id": 10}, {"id": 20}],
                "voters": [{"id": 1}, {"id": 2}, {"id": 3}],
            }
        )
    )

    result = simulate_from_scenario(path)

    assert {party.id for party in result.parties} == {10, 20}
    assert len(result.raw_votes) == 3
    assert {voter.id for voter, _ in result.raw_votes} == {1, 2, 3}
    for _, party in result.raw_votes:
        assert party.id in {10, 20}


def test_simulate_from_scenario_ignores_undeclared_entity_keys(tmp_path):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "seed": 1,
                "parties": [{"id": 1, "name": "Left"}],
                "voters": [{"id": 1, "age": 40}],
            }
        )
    )

    result = simulate_from_scenario(path)

    party = result.parties[0]
    voter, _ = result.raw_votes[0]
    assert party.id == 1
    assert not hasattr(party, "name")
    assert voter.id == 1
    assert not hasattr(voter, "age")


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
