# Trade Show Calendar

> Open dataset of global trade shows with dates, locations, and industry categories.

**Lensmor** helps B2B teams discover the right events, analyze exhibitors, and build qualified lead lists. Learn more at [lensmor.com](https://www.lensmor.com/).

## Dataset

This repository provides a starter calendar dataset in both CSV and JSON formats.

- `data/trade_shows.csv`
- `data/trade_shows.json`

### Data format

| Field | Description |
| --- | --- |
| name | Official event name |
| website | Official website |
| city | Host city |
| country | Host country |
| start_date | Start date (YYYY-MM-DD) |
| end_date | End date (YYYY-MM-DD) |
| frequency | Annual, biennial, etc. |
| industry | Primary industry category |
| region | Region grouping |
| notes | Additional context |

## Data Sources

All entries are compiled from publicly available and verified sources:

- **Official event websites** — Primary source for dates, locations, and descriptions
- **Exhibition industry associations** — [UFI](https://www.ufi.org/), [IAEE](https://www.iaee.com/), [SISO](https://www.siso.org/), [AUMA](https://www.auma.de/)
- **Event directories** — [10Times](https://10times.com/), [EventsEye](https://www.eventseye.com/), [m+a Expodatabase](https://www.expodatabase.com/)
- **Industry reports** — [CEIR Index](https://www.ceir.org/), [UFI Global Barometer](https://www.ufi.org/research/)

### Data quality

- Each entry is manually verified against the official event website
- Dates reflect the most recently confirmed schedule (some 2026 dates are tentative)
- Events marked as postponed or cancelled are noted in the `notes` field
- Discontinued events are removed during quarterly reviews

### Update frequency

- **Monthly** — New events and date corrections
- **Quarterly** — Full review of all entries for accuracy
- **Community** — Pull requests are reviewed and merged on a rolling basis

## Coverage

The dataset currently includes **76 trade shows** across:

- 9 industry categories (Technology, Food & Beverage, Healthcare, Manufacturing, Automotive, Fashion, Energy, Agriculture, Construction)
- 5 regions (Asia, Europe, North America, Middle East & Africa, Latin America)
- 25+ countries

We are actively expanding coverage. See [open issues](https://github.com/LensmorOfficial/trade-show-calendar/issues) for planned additions.

## Contributing

Contributions are welcome. Please open an issue or pull request with verified sources.

When adding new events, please include:
- A link to the official event website as the source
- Verified dates for the current or next edition
- The correct industry category and region

## License

MIT
