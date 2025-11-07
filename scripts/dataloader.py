import argparse
import json
from datasets import load_dataset

def save_humanevalpack_test(output_path: str, pretty: bool = True) -> None:
    ds = load_dataset("bigcode/humanevalpack", "python")["test"]
    # Convert to plain Python list of dicts
    records = list(ds)
    with open(output_path, "w", encoding="utf-8") as f:
        if pretty:
            json.dump(records, f, ensure_ascii=False, indent=2)
        else:
            json.dump(records, f, ensure_ascii=False, separators=(",", ":"))


def parse_args():
    p = argparse.ArgumentParser(description="Save humanevalpack test split to JSON")
    p.add_argument(
        "--output",
        "-o",
        default="data/humanevalpack_test.json",
        help="Output JSON file path (default: data/humanevalpack_test.json)",
    )
    p.add_argument(
        "--compact",
        action="store_true",
        help="Write compact JSON (no pretty indentation)",
    )
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()
    save_humanevalpack_test(args.output, pretty=not args.compact)