<p align="center">
  <a href="https://www.lensmor.com/?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar">
    <img src="https://raw.githubusercontent.com/LensmorOfficial/.github/main/profile/assets/banner.png" alt="Lensmor" width="600">
  </a>
</p>

# Trade Show Calendar

[![Stars](https://img.shields.io/github/stars/LensmorOfficial/trade-show-calendar?style=flat)](https://github.com/LensmorOfficial/trade-show-calendar/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/LensmorOfficial/trade-show-calendar?style=flat)](https://github.com/LensmorOfficial/trade-show-calendar/commits/main)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**If you find this dataset useful, please star this repo — it helps others discover it.**

> Open dataset of global trade shows with dates, locations, and industry categories.

**[View Interactive Calendar →](https://lensmorofficial.github.io/trade-show-calendar/)**
Browse 133 event records by industry, region, and year/month; show upcoming/current editions or the full dataset.

Built by [Lensmor](https://www.lensmor.com/?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar) — AI-powered trade show intelligence for B2B teams. Learn how to turn trade shows into [lead capture machines](https://www.lensmor.com/blog/trade-show-lead-capture?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar).

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

Official organizer and venue websites are the primary sources for event dates and locations. Community corrections should link the exact page supporting the change.

### Verification status — October 7, 2026

This is a community-maintained starter dataset. A repository update does not mean every event has been reverified. Older editions remain in the dataset until a sourced replacement is available.

Six priority records have been checked against official sources in this maintenance pass:

| Event | Confirmed dates | Official source |
| --- | --- | --- |
| FABTECH, Las Vegas | October 21–23, 2026 | [Organizer](https://cdn.fabtechexpo.com/attend) |
| MEDICA, Düsseldorf | November 16–19, 2026 | [Organizer](https://www.medica-tradefair.com/en/Visit/What_to_expect/Reasons_to_attend_1) |
| GITEX Global, Dubai | December 7–11, 2026 | [Organizer](https://www.gitex.com/) — summit December 7; expo December 8–11 |
| CES, Las Vegas | January 6–9, 2027 | [Organizer](https://www.ces.tech/about-ces/about-ces/) |
| MWC Barcelona | March 1–4, 2027 | [Organizer](https://www.mwcbarcelona.com/) |
| Hannover Messe | April 5–8, 2027 | [Organizer](https://www.hannovermesse.de/de/fuer-besucher/oeffnungszeiten/) |

The matching records, source URLs, and check dates are stored in [data/verification.json](data/verification.json). The other **127 records have not been reverified in this pass**. Always confirm the edition, dates, location, and access requirements with the organizer before making plans.

The interactive calendar groups events by year and month and lets you switch between upcoming/current and all listed editions.

### Data validation

```bash
python3 scripts/validate-data.py
```

This checks ISO dates, date order, required fields, duplicate editions, CSV/JSON consistency, and verification records. It reports past editions for maintenance planning; it does not verify organizer websites or silently advance event dates.

Validation runs on pull requests and changes to `main`.

## Coverage

The dataset includes **133 event records**, **24 industry categories**, **5 regions**, and **26 country/territory labels**. These counts describe the records in this repository, including past editions; they do not represent complete global coverage.

## Contributing

Contributions are welcome. Please open an issue or pull request with verified sources.

When adding new events, please include:
- A link to the official event website as the source
- Verified dates for the current or next edition
- The correct industry category and region

## About Lensmor

[Lensmor](https://www.lensmor.com/?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar) is an AI-native event intelligence platform that helps B2B teams discover trade shows, analyze exhibitors, and generate [qualified leads](https://www.lensmor.com/blog/trade-show-lead-capture?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar) before the event starts.

**[Try Lensmor Free →](https://www.lensmor.com/?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar)**

## More Open Source from Lensmor

- [awesome-trade-shows](https://github.com/LensmorOfficial/awesome-trade-shows) — Curated list of 130+ trade shows across 16 industries
- [trade-show-world-map](https://github.com/LensmorOfficial/trade-show-world-map?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar) — Interactive world map of global trade shows by region and industry
- [exhibitor-intelligence-playbook](https://github.com/LensmorOfficial/exhibitor-intelligence-playbook) — Complete B2B trade show ROI playbook
- [trade-show-skills](https://github.com/LensmorOfficial/trade-show-skills) — Reusable OpenClaw skills for trade show planning and outreach
- [event-tech-landscape](https://github.com/LensmorOfficial/event-tech-landscape) — Map of 80+ tools powering the event industry
- [trade-show-email-templates](https://github.com/LensmorOfficial/trade-show-email-templates) — Ready-to-use email templates for trade show outreach

## License

MIT
