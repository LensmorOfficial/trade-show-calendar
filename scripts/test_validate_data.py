import copy
import csv
from datetime import date
import json
from pathlib import Path
import runpy
import tempfile
import unittest

MODULE = runpy.run_path(str(Path(__file__).with_name("validate-data.py")))
validate = MODULE["validate"]
FIELDS = MODULE["FIELDS"]


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "data").mkdir()
        self.shows = [{
            "name": "Example Event", "website": "https://example.com/event",
            "city": "Example City", "country": "Example Country",
            "start_date": "2026-01-06", "end_date": "2026-01-09",
            "frequency": "Annual", "industry": "Technology", "region": "Europe",
            "notes": "Technology, music, and culture festival",
        }]
        self.verification = [{
            **{field: self.shows[0][field] for field in ("name", "start_date", "end_date", "city")},
            "source_url": "https://example.com/event", "verified_on": "2026-01-01",
        }]
        self.today = date(2026, 10, 7)

    def tearDown(self):
        self.temporary.cleanup()

    def write(self, csv_shows=None):
        (self.root / "data/trade_shows.json").write_text(json.dumps(self.shows))
        (self.root / "data/verification.json").write_text(json.dumps(self.verification))
        with (self.root / "data/trade_shows.csv").open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(self.shows if csv_shows is None else csv_shows)

    def test_quoted_notes_and_past_editions_are_preserved(self):
        self.write()
        result = validate(self.root, self.today)
        self.assertEqual(result["past_editions"], 1)
        self.assertEqual(result["verified_records"], 1)

    def test_csv_json_mismatch_is_rejected(self):
        csv_shows = copy.deepcopy(self.shows)
        csv_shows[0]["city"] = "Different City"
        self.write(csv_shows)
        with self.assertRaisesRegex(ValueError, "CSV and JSON records differ"):
            validate(self.root, self.today)

    def test_impossible_date_is_rejected(self):
        self.shows[0]["start_date"] = "2026-02-30"
        self.write()
        with self.assertRaisesRegex(ValueError, "invalid date"):
            validate(self.root, self.today)

    def test_inverted_date_range_is_rejected(self):
        self.shows[0]["end_date"] = "2026-01-05"
        self.write()
        with self.assertRaisesRegex(ValueError, "end date precedes"):
            validate(self.root, self.today)

    def test_duplicate_edition_is_rejected(self):
        self.shows.append(copy.deepcopy(self.shows[0]))
        self.write()
        with self.assertRaisesRegex(ValueError, "Duplicate event edition"):
            validate(self.root, self.today)

    def test_changed_edition_invalidates_old_verification(self):
        self.shows[0].update(start_date="2027-01-06", end_date="2027-01-09")
        self.write()
        with self.assertRaisesRegex(ValueError, "Verification does not match"):
            validate(self.root, self.today)

    def test_future_verification_is_rejected(self):
        self.verification[0]["verified_on"] = "2026-10-08"
        self.write()
        with self.assertRaisesRegex(ValueError, "verification date is in the future"):
            validate(self.root, self.today)


if __name__ == "__main__":
    unittest.main()
