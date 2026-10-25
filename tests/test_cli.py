import json

from main import main
from test_budget_affinity import _shares, _traits


def test_cli_scenario_prints_the_same_payload_shape(tmp_path, capsys, monkeypatch):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "seed": 1,
                "parties": [
                    {"id": 1, **_shares(health=1.0)},
                    {"id": 2, **_shares(defense=1.0)},
                ],
                "voters": [
                    {"id": 1, **_traits(health_status=1)},
                    {"id": 2, **_traits(health_status=1)},
                ],
            }
        )
    )
    monkeypatch.setattr("sys.argv", ["main.py", "--scenario", str(path)])

    main()

    out = capsys.readouterr().out
    assert "counts:" in out
    assert "raw votes:" in out
    assert "party 1:" in out
    assert "voter 1 -> party" in out


def test_cli_flags_path_still_prints_the_payload(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--parties", "2", "--voters", "4", "--seed", "1"],
    )

    main()

    out = capsys.readouterr().out
    assert "counts:" in out
    assert "raw votes:" in out
    assert "voter 1 -> party" in out
    assert "voter 4 -> party" in out
