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

## Submissions checklist

- [ ] Event is active and not discontinued
- [ ] Official website link is included
- [ ] Dates are verified from a primary source
- [ ] CSV and JSON entries match
