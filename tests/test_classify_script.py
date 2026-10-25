import json
from pathlib import Path

import pytest

from classify import main
from test_budget_affinity import _shares

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "scenario.json"


def test_classify_script_prints_spectrum_for_the_example_scenario(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["classify.py", "--scenario", str(EXAMPLE)])

    main()

    out = capsys.readouterr().out
    assert "party 1: left 84.0" in out
    assert "party 2: right 88.0" in out
    assert "party 3: left 80.0" in out
    assert "counts:" not in out
    assert "raw votes:" not in out


def test_classify_script_ignores_undeclared_spectrum_input(tmp_path, capsys, monkeypatch):
    path = tmp_path / "scenario.json"
    path.write_text(
        json.dumps(
            {
                "parties": [
                    {
                        "id": 1,
                        "name": "X",
                        "spectrum": "right",
                        "conviction": 1,
                        **_shares(
                            health=0.18,
                            education=0.16,
                            infrastructure=0.08,
                            defense=0.02,
                            social_protection=0.22,
                            environment=0.12,
                            housing=0.14,
                            research=0.06,
                            public_order=0.02,
                        ),
                    }
                ]
            }
        )
    )
    monkeypatch.setattr("sys.argv", ["classify.py", "--scenario", str(path)])

    main()

    out = capsys.readouterr().out
    assert "party 1: far_left 100.0" in out


def test_classify_script_rejects_invalid_shares(tmp_path, monkeypatch):
    path = tmp_path / "scenario.json"
    path.write_text(json.dumps({"parties": [{"id": 1, **_shares(health=0.5)}]}))
    monkeypatch.setattr("sys.argv", ["classify.py", "--scenario", str(path)])

    with pytest.raises(ValueError, match="sum to 1"):
        main()


def test_classify_script_rejects_missing_share_fields(tmp_path, monkeypatch):
    path = tmp_path / "scenario.json"
    path.write_text(json.dumps({"parties": [{"id": 1, "health": 1.0}]}))
    monkeypatch.setattr("sys.argv", ["classify.py", "--scenario", str(path)])

    with pytest.raises(ValueError, match="GDP shares"):
        main()
