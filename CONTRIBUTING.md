# Contributing to Trade Show Calendar

Thank you for contributing new trade show data.

## How to contribute

You can submit data in two ways:

- **Open an issue** using the data submission template
- **Open a pull request** with updates to the CSV/JSON files

## Data format requirements

All entries must include:

- `name`
- `website` (official site)
- `city`
- `country`
- `start_date` (YYYY-MM-DD)
- `end_date` (YYYY-MM-DD)
- `frequency`
- `industry`
- `region`
- `notes`

## Formatting rules

- One event per row in `data/trade_shows.csv`
- Keep fields aligned between CSV and JSON
- Use ISO dates (YYYY-MM-DD)
- Verify links are official and working
- Keep names consistent with official branding
- When verifying an edition, add its name, dates, city, official source URL, and check date to `data/verification.json`. Update or remove the old verification record if the edition changes.
- Never advance a date by assuming that an annual event repeats on the same day.

Run the validator before opening a pull request:

```bash
python3 scripts/validate-data.py
```

## Submissions checklist

- [ ] Event is active and not discontinued
- [ ] Official website link is included
- [ ] Dates are verified from a primary source
- [ ] CSV and JSON entries match
- [ ] Verification record matches the event edition and includes an official source
