import pytest

from entities import PoliticalParty, Voter
from simulate import simulate


def test_simulate_returns_one_vote_per_voter_for_an_existing_party():
    result = simulate(n_parties=3, n_voters=100, seed=1)

    assert len(result.raw_votes) == 100
    party_ids = {party.id for party in result.parties}
    assert party_ids == {1, 2, 3}
    for voter, party in result.raw_votes:
        assert isinstance(voter, Voter)
        assert isinstance(party, PoliticalParty)
        assert party.id in party_ids
        assert voter.vote == party


def test_simulate_returns_counts_that_sum_to_ballots_cast():
    result = simulate(n_parties=3, n_voters=100, seed=1)

    assert sum(result.counts.values()) == 100
    expected = {1: 0, 2: 0, 3: 0}
    for _, party in result.raw_votes:
        expected[party.id] += 1
    assert result.counts == expected


def test_simulate_names_a_unique_winner_when_one_party_has_the_max():
    result = simulate(n_parties=1, n_voters=10, seed=1)

    assert result.winner is not None
    assert result.winner.id == 1
    assert result.tied == ()


def test_simulate_lists_tied_parties_when_several_share_the_max():
    result = None
    for seed in range(10_000):
        candidate = simulate(n_parties=2, n_voters=2, seed=seed)
        if candidate.winner is None:
            result = candidate
            break
    assert result is not None
    assert {party.id for party in result.tied} == {1, 2}


def test_simulate_reproduces_votes_with_the_same_seed():
    a = simulate(n_parties=4, n_voters=100, seed=42)
    b = simulate(n_parties=4, n_voters=100, seed=42)

    assert [party.id for _, party in a.raw_votes] == [
        party.id for _, party in b.raw_votes
    ]


@pytest.mark.parametrize("n_parties,n_voters", [(0, 10), (3, 0), (-1, 5), (2, -1)])
def test_simulate_does_not_run_when_n_or_m_is_invalid(n_parties, n_voters):
    with pytest.raises(ValueError):
        simulate(n_parties=n_parties, n_voters=n_voters, seed=1)
