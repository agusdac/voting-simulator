from pathlib import Path

from main import main
from simulate import simulate_from_scenario

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "scenario.json"


def test_example_scenario_runs_an_affinity_election():
    result = simulate_from_scenario(EXAMPLE)

    assert len(result.parties) == 3
    for party in result.parties:
        total = (
            party.health
            + party.education
            + party.infrastructure
            + party.defense
            + party.social_protection
            + party.environment
            + party.housing
            + party.research
            + party.public_order
        )
        assert abs(total - 1.0) < 1e-9
    assert result.raw_votes
    assert sum(result.counts.values()) == len(result.raw_votes)
    for voter, _ in result.raw_votes:
        assert voter.age or voter.age == 0
        assert hasattr(voter, "dependents")
        assert hasattr(voter, "gender")


def test_cli_prints_payload_for_the_example_scenario(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["main.py", "--scenario", str(EXAMPLE)])

    main()

    out = capsys.readouterr().out
    assert "counts:" in out
    assert "raw votes:" in out
    assert "party 1:" in out
