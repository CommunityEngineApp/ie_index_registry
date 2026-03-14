# IE Index Registry

**Maintained by [Innovative EcoSystems](https://innovativeecosystems.com)**  
**Version:** 1.0.0 | **Last Updated:** March 2026  
**Total Indices:** 100

---

## What Is This?

This repository is the canonical master registry of every global index used to power the **IEPA — Innovative EcoSystems Prosperity Algorithm**.

It is the single source of truth for:
- Which indices feed each IEPA Foundation Factor
- How each index is weighted in the algorithm
- Where to download raw data for each index
- Data access type, license, coverage, and freshness

Both the IEPA algorithm engine and the IE Community Platform UI read directly from this registry.

---

## How IEPA Uses These Indices

IEPA models ecosystem prosperity as a latent state variable that evolves annually, structured across three zones:

```
FOUNDATIONS  →  ENGINE  →  OUTCOMES
```

### Foundation Factors (What a region builds)
| Factor | Description |
|---|---|
| **Innovation Capacity** | R&D, infrastructure, digital readiness, IP, tech adoption |
| **Entrepreneurship Capacity** | Startup formation, scale-up pathways, access to capital |
| **Resilience** | Peace, stability, environment, social cohesion, institutional trust |
| **Alignment** | Government-industry-university coordination and governance quality |

### Engine (How prosperity is created)
| Factor | Description |
|---|---|
| **FDI Accelerator** | Capital attraction, market access, investment climate |

### Outcomes (What success looks like)
| Factor | Description |
|---|---|
| **Prosperity Outcomes** | GDP growth, job creation, scalable company creation |

---

## Registry Schema

Each index entry follows this structure:

```json
{
  "id": "GII",
  "name": "Global Innovation Index",
  "publisher": "WIPO",
  "url": "https://www.wipo.int/gii",
  "frequency": "Annual",
  "latest_year": 2024,
  "country_coverage": 133,
  "iepa_zone": "Foundations",
  "iepa_factor": "Innovation Capacity",
  "iepa_weight": 0.20,
  "tier": "Primary",
  "data_access": "Free",
  "license": "Open",
  "format": "Excel, PDF",
  "notes": "...",
  "tags": ["innovation", "R&D", "IP", "infrastructure"]
}
```

### Field Definitions

| Field | Description |
|---|---|
| `id` | Unique identifier used across all IE systems |
| `name` | Full official index name |
| `publisher` | Organization that produces the index |
| `url` | Official source URL for data download |
| `frequency` | How often the index is updated |
| `latest_year` | Most recent year data is available |
| `country_coverage` | Number of countries covered |
| `iepa_zone` | Which IEPA zone this feeds: `Foundations`, `Engine`, or `Outcomes` |
| `iepa_factor` | Specific factor within the zone |
| `iepa_weight` | Relative weight within that factor (0–1, factor weights sum to 1.0) |
| `tier` | `Primary` / `Secondary` / `Tertiary` — importance to algorithm |
| `data_access` | `Free`, `Paid`, or `Free (summary) / Paid (full)` |
| `license` | `Open` or `Restricted` |
| `format` | Available file formats |
| `notes` | Methodology notes and IEPA usage rationale |
| `tags` | Searchable topic tags |

---

## Tier Definitions

| Tier | Meaning |
|---|---|
| **Primary** | Core IEPA inputs. Required for algorithm computation. High weight. |
| **Secondary** | Important supplementary inputs. Used for validation and enrichment. |
| **Tertiary** | Contextual signals. Used for UI enrichment and scenario analysis. |

---

## Index Summary by Factor

| IEPA Factor | Primary | Secondary | Tertiary | Total |
|---|---|---|---|---|
| Innovation Capacity | 4 | 9 | 7 | 20 |
| Entrepreneurship Capacity | 4 | 8 | 4 | 16 |
| Resilience | 5 | 9 | 7 | 21 |
| Alignment | 4 | 9 | 3 | 16 |
| FDI Accelerator | 4 | 9 | 4 | 17 |
| Prosperity Outcomes | 3 | 4 | 3 | 10 |
| **Total** | **24** | **48** | **28** | **100** |

---

## Target Markets

The registry is optimized for coverage of IE's 13 **Tier 1 Emerging Markets**:

Vietnam · India · Egypt · Turkey · Thailand · South Korea · Philippines · Saudi Arabia · UAE · Indonesia · Malaysia · Morocco · Kenya

When selecting indices, priority is given to sources with strong coverage across these markets.

---

## Data Access Guide

### Free & Open (Download Directly)
Most Primary and Secondary indices are freely available. Download instructions:
1. Visit the `url` field for each index
2. Navigate to the data download section
3. Download as Excel or CSV
4. Store raw files in your Supabase `raw_index_data` table with `index_id`, `country_iso3`, `year`, and `value` fields

### Paid / Restricted
Indices marked `Restricted` require licensing agreements. Current paid sources in use:
- IMD World Competitiveness (subscription)
- fDi Markets Greenfield Tracker (FT subscription)
- EIU Country Risk Service (subscription)
- MSCI ESG Scores (institutional license)
- Verisk Maplecroft Climate Vulnerability (subscription)

### Partially Free
Some indices offer summary data free and full data behind a paywall. Use summary data for UI display, full data for algorithm computation where licensed.

---

## How to Consume This Registry

### Claude (AI Partner)
This file is loaded as project knowledge in Claude.ai. Claude references it for:
- Algorithm weight discussions
- Country coverage gap analysis
- Methodology documentation
- Index sourcing recommendations

### Lovable (Community Platform UI)
Fetch the raw JSON directly:
```javascript
const REGISTRY_URL = 
  "https://raw.githubusercontent.com/CommunityEngineApp/ie_index_registry/main/registry.json";

const response = await fetch(REGISTRY_URL);
const { indices } = await response.json();
```

Filter by factor:
```javascript
const innovationIndices = indices.filter(
  i => i.iepa_factor === "Innovation Capacity"
);
```

Filter by tier:
```javascript
const primaryIndices = indices.filter(i => i.tier === "Primary");
```

### IEPA Algorithm Engine
The algorithm references `id` fields as canonical keys when pulling scored data from Supabase. Every country score stored in the database links back to an `index_id` that maps to an entry here.

---

## Architecture Overview

```
ie_index_registry (this repo — GitHub)
        │
        ├── Defines WHAT indices exist and HOW they're weighted
        │
        ▼
Supabase (raw_index_data table)
        │
        ├── Stores ACTUAL country scores by index_id + country + year
        │
        ▼
IEPA Algorithm Engine
        │
        ├── Computes prosperity scores using registry weights
        │
        ▼
IE Community Platform (Lovable)
        │
        └── Displays scores, comparisons, and factor breakdowns
```

---

## Iconography

The file `iconography.json` defines the canonical icon mapping for the IE Community Platform UI. All icon names reference the **Lucide** icon library (`lucide-react`), which ships with shadcn/ui and Lovable.

### What It Covers

| Section | Purpose |
|---|---|
| `brand` | Logo and IEPA badge icons with brand colors |
| `zones` | Icons for Foundations, Engine, and Outcomes |
| `factors` | Icons for each of the 6 IEPA factors |
| `tiers` | Visual indicators for Primary / Secondary / Tertiary |
| `data_access` | Lock/unlock icons for free vs. paid data |
| `navigation` | Sidebar and nav menu icons |
| `actions` | Common UI actions (download, filter, search, sort) |
| `status` | Data freshness indicators |
| `tag_categories` | Icon groupings for the tag cloud |
| `score_display` | Score level indicators and trend arrows |
| `countries` | Country flag emoji for Tier 1 markets |

### Usage in Lovable

```javascript
import { Lightbulb, Rocket, ShieldCheck } from "lucide-react";

const ICON_URL =
  "https://raw.githubusercontent.com/CommunityEngineApp/ie_index_registry/main/iconography.json";

const response = await fetch(ICON_URL);
const iconography = await response.json();

// Get factor icon name
const innovationIcon = iconography.factors["Innovation Capacity"].icon;
// => "lightbulb"
```

---

## Versioning & Updates

All changes to this registry are tracked via Git commits. Follow this convention:

| Change Type | Example Commit Message |
|---|---|
| Add new index | `feat: add OECD PMR Index to Alignment factor` |
| Update weight | `update: increase GII weight from 0.18 to 0.20` |
| New data year | `data: update latest_year to 2025 for 14 indices` |
| Deprecate index | `deprecate: remove Doing Business (replaced by Business Ready)` |

See `metadata/changelog.md` for full version history.

---

## Contributing

This registry is maintained by the Innovative EcoSystems core team. To propose changes:
1. Open an Issue with the label `index-proposal` or `weight-change`
2. Include methodology rationale
3. Tag `@john` for review

All weight changes require written justification in `metadata/weighting_rationale.md`.

---

## License

Registry metadata (this file and `registry.json`) is published under **CC BY 4.0**.  
Individual index data remains subject to the licensing terms of each publisher.  
See `metadata/data_sources.md` for licensing details per index.

---

*Built by Innovative EcoSystems — Designing the environments where innovation thrives.*
