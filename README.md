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
Browse and filter 133 trade shows by industry, region, and month.

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

The dataset currently includes **133 trade shows** across:

- 19 industry categories (Technology, Food & Beverage, Healthcare, Manufacturing, Automotive, Fashion, Energy, Agriculture, Construction, Consumer Goods, Real Estate, Digital Marketing, Pharmaceutical, Beauty & Personal Care, Education, Retail, Finance & Fintech, Defense, Logistics & Supply Chain)
- 5 regions (Asia, Europe, North America, Middle East & Africa, Latin America)
- 35+ countries

We are actively expanding coverage. See [open issues](https://github.com/LensmorOfficial/trade-show-calendar/issues) for planned additions.

## Contributing

Contributions are welcome. Please open an issue or pull request with verified sources.

When adding new events, please include:
- A link to the official event website as the source
- Verified dates for the current or next edition
- The correct industry category and region

## About Lensmor

[Lensmor](https://www.lensmor.com/?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar) is an AI-native event intelligence platform that helps B2B teams discover trade shows, analyze exhibitors (uncovering [hidden competitors](https://www.lensmor.com/blog/hidden-competitors-trade-shows?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar)), and generate [qualified leads](https://www.lensmor.com/blog/trade-show-lead-capture?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar) before the event starts.

**[Try Lensmor Free →](https://www.lensmor.com/?utm_source=github&utm_medium=readme&utm_campaign=trade-show-calendar)**

## More Open Source from Lensmor

- [awesome-trade-shows](https://github.com/LensmorOfficial/awesome-trade-shows) — Curated list of 130+ trade shows across 16 industries
- [exhibitor-intelligence-playbook](https://github.com/LensmorOfficial/exhibitor-intelligence-playbook) — Complete B2B trade show ROI playbook
- [trade-show-skills](https://github.com/LensmorOfficial/trade-show-skills) — AI-powered Claude Code skills for trade show automation
- [event-tech-landscape](https://github.com/LensmorOfficial/event-tech-landscape) — Map of 80+ tools powering the event industry
- [trade-show-email-templates](https://github.com/LensmorOfficial/trade-show-email-templates) — Ready-to-use email templates for trade show outreach

## License

MIT
