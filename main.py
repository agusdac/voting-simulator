import argparse

from simulate import ElectionResult, simulate, simulate_from_scenario


def format_result(result: ElectionResult) -> str:
    lines = ["counts:"]
    for party_id, count in sorted(result.counts.items()):
        lines.append(f"  party {party_id}: {count}")
    if result.winner is not None:
        lines.append(f"winner: party {result.winner.id}")
    else:
        tied = ", ".join(f"party {party.id}" for party in result.tied)
        lines.append(f"tied: {tied}")
    lines.append("raw votes:")
    for voter, party in result.raw_votes:
        lines.append(f"  voter {voter.id} -> party {party.id}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a random-vote election simulation.")
    parser.add_argument("--scenario", help="Path to a JSON scenario file.")
    parser.add_argument("--parties", type=int)
    parser.add_argument("--voters", type=int, default=100)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    if args.scenario:
        result = simulate_from_scenario(args.scenario)
    elif args.parties is not None:
        result = simulate(n_parties=args.parties, n_voters=args.voters, seed=args.seed)
    else:
        parser.error("provide --scenario or --parties")
    print(format_result(result))


if __name__ == "__main__":
    main()
