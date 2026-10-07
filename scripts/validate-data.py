#!/usr/bin/env python3
"""Validate local data consistency; organizer evidence is reviewed by humans."""

import argparse
import csv
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

FIELDS = ["name", "website", "city", "country", "start_date", "end_date",
          "frequency", "industry", "region", "notes"]


def iso_date(value, context):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"{context}: expected YYYY-MM-DD, got {value!r}")
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"{context}: invalid date {value!r}") from error


def validate(root, as_of):
    shows = json.loads((root / "data/trade_shows.json").read_text())
    if not isinstance(shows, list) or not shows:
        raise ValueError("JSON dataset must be a nonempty list")
    with (root / "data/trade_shows.csv").open(newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            raise ValueError("CSV header does not match the documented fields")
        csv_shows = list(reader)
    if csv_shows != shows:
        raise ValueError("CSV and JSON records differ; update both representations")

    editions = {}
    for index, show in enumerate(shows, 1):
        if set(show) != set(FIELDS):
            raise ValueError(f"Record {index}: unexpected or missing fields")
        for field in FIELDS:
            if not isinstance(show[field], str) or not show[field].strip():
                raise ValueError(f"Record {index}: {field} must be a nonempty string")
        start = iso_date(show["start_date"], show["name"])
        end = iso_date(show["end_date"], show["name"])
        if end < start:
            raise ValueError(f"{show['name']}: end date precedes start date")
        url = urlparse(show["website"])
        if url.scheme not in {"http", "https"} or not url.netloc:
            raise ValueError(f"{show['name']}: invalid website URL")
        key = (show["name"], show["start_date"])
        if key in editions:
            raise ValueError(f"Duplicate event edition: {key}")
        editions[key] = show

    verification = json.loads((root / "data/verification.json").read_text())
    if not isinstance(verification, list):
        raise ValueError("Verification log must be a list")
    verified = set()
    expected = {"name", "start_date", "end_date", "city", "source_url", "verified_on"}
    for item in verification:
        if not isinstance(item, dict) or set(item) != expected:
            raise ValueError("Verification record has unexpected or missing fields")
        key = (item["name"], item["start_date"])
        show = editions.get(key)
        if show is None or any(item[field] != show[field] for field in ("end_date", "city")):
            raise ValueError(f"Verification does not match the dataset edition: {key}")
        if key in verified:
            raise ValueError(f"Duplicate verification: {key}")
        url = urlparse(item["source_url"])
        if url.scheme != "https" or not url.netloc:
            raise ValueError(f"{item['name']}: verification needs an HTTPS source URL")
        checked = iso_date(item["verified_on"], item["name"])
        if checked > as_of:
            raise ValueError(f"{item['name']}: verification date is in the future")
        verified.add(key)

    return {
        "records": len(shows),
        "industries": len({show["industry"] for show in shows}),
        "regions": len({show["region"] for show in shows}),
        "country_labels": len({show["country"] for show in shows}),
        "verified_records": len(verified),
        "past_editions": sum(show["end_date"] < as_of.isoformat() for show in shows),
        "as_of": as_of.isoformat(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()
    try:
        result = validate(Path(__file__).resolve().parents[1], args.as_of)
    except (ValueError, OSError, TypeError, KeyError) as error:
        print(f"[FAIL] {error}", file=sys.stderr)
        sys.exit(1)
    print("[PASS] Data structure, CSV/JSON sync, and source log")
    print(json.dumps(result, indent=2))
