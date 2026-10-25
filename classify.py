import argparse
import json
from pathlib import Path

from entities import PoliticalParty
from spectrum import classify


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify parties on a left-right spectrum.")
    parser.add_argument("--scenario", required=True, help="Path to a JSON scenario file.")
    args = parser.parse_args()
    data = json.loads(Path(args.scenario).read_text(encoding="utf-8"))
    try:
        party_items = data["parties"]
    except KeyError as exc:
        raise ValueError("scenario must include parties") from exc
    for item in party_items:
        labeled = classify(PoliticalParty.from_mapping(item))
        print(f"party {labeled.id}: {labeled.spectrum} {labeled.conviction}")


if __name__ == "__main__":
    main()
