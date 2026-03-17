# IEPA Intelligence Engine — In-Depth Overview

**Innovative EcoSystems Prosperity Algorithm (IEPA)**
Maintained by [Innovative EcoSystems](https://innovativeecosystems.com)
Registry v2.0.0 | Country Scores v2.1.0 | Last Updated: March 2026

---

## 1. What is IEPA?

The **Innovative EcoSystems Prosperity Algorithm (IEPA)** is a quantitative framework that models ecosystem prosperity as a **latent state variable** evolving annually across nations. It synthesizes **163 global indices** from authoritative international sources into a single composite prosperity signal, structured across three causal zones:

```
FOUNDATIONS  →  ENGINE  →  OUTCOMES
 (What a region builds)  (How prosperity is created)  (What success looks like)
```

The engine answers a core question: **"How well is a nation's ecosystem positioned to generate sustainable, innovation-driven prosperity?"**

---

## 2. Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    IE INDEX REGISTRY (GitHub)                     │
│                                                                   │
│  registry.json — 163 indices with weights, zones, factors, tiers │
│  country_scores.json — 2,728 data points across 13 markets       │
│  pipeline.py — automated PDF extraction + data merge              │
└──────────────┬────────────────────────────────────────────────────┘
               │ Defines WHAT gets measured and HOW it's weighted
               ▼
┌─────────────────────────────────────────────────────────────────┐
│                SUPABASE (raw_index_data table)                    │
│                                                                   │
│  Stores actual country scores by: index_id, country_iso3,        │
│  year, and value — linked to registry entries via index_id        │
└──────────────┬────────────────────────────────────────────────────┘
               │ Supplies scored data to the algorithm
               ▼
┌─────────────────────────────────────────────────────────────────┐
│                  IEPA ALGORITHM ENGINE                            │
│                                                                   │
│  Applies registry weights to compute composite prosperity        │
│  scores by factor, zone, and overall country ranking             │
└──────────────┬────────────────────────────────────────────────────┘
               │ Computed scores flow to the UI
               ▼
┌─────────────────────────────────────────────────────────────────┐
│             IE COMMUNITY PLATFORM (Lovable UI)                   │
│                                                                   │
│  Displays scores, country comparisons, factor breakdowns,        │
│  trend analysis, and scenario modeling                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. The IEPA Factor Model

IEPA organizes prosperity measurement into **3 zones** containing **6 factors** with a combined weight of **11.50**:

### 3.1 FOUNDATIONS Zone — "What a region builds"

These four factors represent the structural preconditions for prosperity.

#### Innovation Capacity (Weight: 1.97 | 30 indices)
Measures a nation's ability to produce and absorb innovation.

| Dimension | Examples |
|---|---|
| R&D Infrastructure | Global Innovation Index, Bloomberg Innovation Index |
| Digital Readiness | ICT Development Index, E-Government Index |
| IP Development | Patent applications, trademark filings |
| Technology Adoption | Tech readiness sub-indices, digital skills |

**Primary Indices:** GII (WIPO), Bloomberg Innovation Index, WIPO Patent Data, Nature Index, Networked Readiness Index, E-Government Development Index, ICT Development Index

#### Entrepreneurship Capacity (Weight: 1.77 | 23 indices)
Measures the ecosystem's ability to form, fund, and scale startups.

| Dimension | Examples |
|---|---|
| Startup Formation | Startup Genome GSER, new business density |
| Scale-up Pathways | Unicorn counts, venture capital flow |
| Access to Capital | VC investment data, PE penetration |
| Ease of Business | World Bank Business Ready, regulatory quality |

**Primary Indices:** Startup Genome GSER, World Bank Business Ready, OECD Entrepreneurship Indicators, VC Investment Data, Ease of Doing Business, Trade Logistics (LPI), SEZ Performance, Venture Capital, PE Penetration

#### Resilience (Weight: 1.93 | 32 indices)
Measures a society's capacity to absorb shocks and sustain progress.

| Dimension | Examples |
|---|---|
| Peace & Stability | Global Peace Index, Fragile States Index |
| Environment | Environmental Performance Index, Climate Risk |
| Social Cohesion | Freedom House, Gender Gap Index, HDI |
| Institutional Trust | Democracy Index, Press Freedom, CPI |

**Primary Indices:** GPI, Freedom House, SDG Index, EPI, Democracy Index, Press Freedom, AI Readiness, Fragile States Index, CPI, Gender Gap Index, Economic Freedom

#### Alignment (Weight: 2.00 | 27 indices)
Measures how well government, industry, and academia coordinate to create a unified innovation agenda.

| Dimension | Examples |
|---|---|
| Governance Quality | WGI, Regulatory Quality, Rule of Law |
| Government-Industry Links | PPP investment, industrial policy effectiveness |
| University-Industry Links | R&D spending by sector, tech transfer |
| Policy Coordination | Tax competitiveness, digital government |

**Primary Indices:** WGI Governance Effectiveness, WGI Regulatory Quality, WGI Control of Corruption, WGI Rule of Law, WGI Voice and Accountability, Tax Competitiveness Index, OECD Government at a Glance, E-Participation, Global Cybersecurity Index, OECD PMR

### 3.2 ENGINE Zone — "How prosperity is created"

#### FDI Accelerator (Weight: 2.34 | 32 indices)
The highest-weighted single factor. Measures how effectively a nation attracts and deploys foreign direct investment as a growth catalyst.

| Dimension | Examples |
|---|---|
| Capital Attraction | FDI inflows (% GDP), greenfield projects |
| Market Access | Trade openness, bilateral agreements |
| Investment Climate | Investment freedom, country risk ratings |
| Infrastructure | Port connectivity, air transport quality |

**Primary Indices:** FDI Inflows (% GDP), Greenfield FDI Projects, WTO Trade Openness, Investment Freedom, Global Competitiveness Index, OECD FDI Regulatory Restrictiveness, IMD World Competitiveness, Economic Complexity, Trade Facilitation, Foreign Market Size, Bilateral Investment Treaties, Logistics Performance

### 3.3 OUTCOMES Zone — "What success looks like"

#### Prosperity Outcomes (Weight: 1.49 | 19 indices)
Measures the tangible results of a well-functioning ecosystem.

| Dimension | Examples |
|---|---|
| Economic Growth | GDP growth, GDP per capita (PPP) |
| Job Creation | Employment rate, labor productivity |
| Company Creation | Unicorn count, high-growth firms |
| Wealth Distribution | GNI per capita, GINI coefficient |

**Primary Indices:** GDP Growth, GDP Per Capita (PPP), GNI Per Capita, Employment-to-Population Ratio, Labor Productivity, High-Growth Firm Rate, Unicorn Count, Foreign Value Added in Exports, Total Factor Productivity

---

## 4. Weighting & Tier System

### 4.1 Factor Weights

| Zone | Factor | Weight | % of Total | Index Count |
|---|---|---|---|---|
| Foundations | Innovation Capacity | 1.97 | 17.1% | 30 |
| Foundations | Entrepreneurship Capacity | 1.77 | 15.4% | 23 |
| Foundations | Resilience | 1.93 | 16.8% | 32 |
| Foundations | Alignment | 2.00 | 17.4% | 27 |
| Engine | FDI Accelerator | 2.34 | 20.3% | 32 |
| Outcomes | Prosperity Outcomes | 1.49 | 13.0% | 19 |
| **Total** | | **11.50** | **100%** | **163** |

**Key insight:** The FDI Accelerator carries the highest weight (20.3%), reflecting IEPA's thesis that foreign direct investment is the primary transmission mechanism from ecosystem foundations to prosperity outcomes.

### 4.2 Tier System

Each index is classified into one of three tiers:

| Tier | Count | Combined Weight | Role |
|---|---|---|---|
| **Primary** | 58 | 5.65 | Core algorithm inputs. Required for computation. |
| **Secondary** | 70 | 4.36 | Supplementary validation and enrichment signals. |
| **Tertiary** | 35 | 1.49 | Contextual UI enrichment and scenario analysis. |

Within each factor, individual index weights (`iepa_weight`) sum to 1.0.

---

## 5. Data Pipeline

### 5.1 Three-Stage Extraction Architecture

The `pipeline.py` module implements a production-grade data extraction system:

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  STAGE 1          │     │  STAGE 2          │     │  STAGE 3          │
│  PDF Extraction   │ ──▶ │  Curated Data     │ ──▶ │  Merge & Output   │
│                    │     │  Integration      │     │                    │
│  • GPI (IEP)      │     │  • GII (WIPO)     │     │  • Fetch existing  │
│  • GGI (WEF)      │     │  • CPI (TI)       │     │  • Non-destructive │
│  • SDG (SDSN)     │     │  • Freedom House   │     │    merge           │
│  • GCI (WEF)      │     │  • 10 more indices │     │  • GitHub push     │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

### 5.2 PDF Extraction Methods

| Method | Used For | Technique |
|---|---|---|
| `extract_gpi()` | Global Peace Index | `pdfplumber` table extraction with regex rank+score patterns |
| `extract_gender_gap()` | Gender Gap Index | `pdfplumber` table extraction, 0.xxx format, 0.50-0.92 validation |
| `extract_by_text_pattern()` | WEF GCR 2019 | `pdftotext -layout` with generic regex and range validation |
| Curated fallback | SDG Index (image-rendered PDFs) | Manually verified data from published reports |

### 5.3 Data Sources

**Live APIs (2 sources):**
- World Bank API — economic indicators, development data
- IMF World Economic Outlook API — GDP forecasts, macroeconomic projections

**PDF Extracted (4 reports):**
- Global Peace Index 2024 (Vision of Humanity / IEP)
- Global Gender Gap Report 2024 (WEF)
- Sustainable Development Report 2024 (SDSN)
- WEF Global Competitiveness Report 2019 (baseline)

**Curated Annual Reports (13 sources):**
- GII (WIPO) — 5-year history (2020-2024)
- CPI (Transparency International) — 5-year history
- Freedom in the World (Freedom House)
- Environmental Performance Index (Yale)
- Democracy Index (EIU) — 3-year history (2022-2024)
- Press Freedom Index (RSF)
- AI Readiness Index (Oxford Insights)
- Fragile States Index (Fund for Peace)
- IMD World Competitiveness Ranking
- Startup Genome GSER
- Economic Freedom Index (Heritage) — 5-year history
- WEF GCI 2019 (pre-pandemic baseline)
- SDG Index (SDSN)

### 5.4 Pipeline CLI

```bash
python3 pipeline.py                          # Extract only
python3 pipeline.py --push <GITHUB_TOKEN>    # Extract + push to GitHub
python3 pipeline.py --no-download            # Use cached PDFs
python3 pipeline.py --no-merge               # Don't merge with existing data
python3 pipeline.py --verbose                # Detailed logging
python3 pipeline.py --output custom.json     # Custom output file
```

---

## 6. Target Markets

IEPA focuses on **13 Tier 1 Emerging Markets** selected for their strategic importance to innovation-driven FDI:

| Country | ISO3 | Region |
|---|---|---|
| Vietnam | VNM | Southeast Asia |
| India | IND | South Asia |
| Egypt | EGY | North Africa / Middle East |
| Turkey | TUR | Europe / Middle East |
| Thailand | THA | Southeast Asia |
| South Korea | KOR | East Asia |
| Philippines | PHL | Southeast Asia |
| Saudi Arabia | SAU | Middle East |
| UAE | ARE | Middle East |
| Indonesia | IDN | Southeast Asia |
| Malaysia | MYS | Southeast Asia |
| Morocco | MAR | North Africa |
| Kenya | KEN | East Africa |

**Current Data Coverage:**
- 2,728 total data points across 59 populated indices
- Years covered: 2019-2024 (6 years)
- Average ~210 data points per country

---

## 7. Registry Schema

Every index in the registry follows a standardized schema:

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
  "notes": "7 pillars covering institutions, human capital, infrastructure...",
  "tags": ["innovation", "R&D", "IP", "infrastructure", "primary"],
  "data_years": [2020, 2021, 2022, 2023, 2024]
}
```

| Field | Purpose |
|---|---|
| `id` | Canonical key used across all IE systems and Supabase |
| `iepa_zone` | Maps to Foundations, Engine, or Outcomes |
| `iepa_factor` | Specific factor within the zone |
| `iepa_weight` | Relative weight within factor (factor weights sum to 1.0) |
| `tier` | Primary / Secondary / Tertiary importance classification |
| `data_years` | Available historical years for time-series loading |

---

## 8. Data Access & Licensing

| Access Type | Count | Percentage |
|---|---|---|
| Free | 139 | 85% |
| Paid | 9 | 5.5% |
| Free (summary) / Paid (full) | 6 | 3.7% |
| Other | 9 | 5.8% |

| License | Count | Percentage |
|---|---|---|
| Open | 139 | 85% |
| Restricted | 21 | 13% |
| Mixed | 3 | 2% |

**Paid Sources in Use:**
- IMD World Competitiveness (subscription)
- fDi Markets Greenfield Tracker (FT subscription)
- EIU Country Risk Service (subscription)
- MSCI ESG Scores (institutional license)
- Verisk Maplecroft Climate Vulnerability (subscription)

---

## 9. Integration Points

### 9.1 Claude (AI Partner)
The registry is loaded as project knowledge in Claude.ai for:
- Algorithm weight discussions and tuning
- Country coverage gap analysis
- Methodology documentation
- Index sourcing recommendations

### 9.2 Lovable (Community Platform UI)
```javascript
// Direct fetch from GitHub raw content
const REGISTRY_URL =
  "https://raw.githubusercontent.com/CommunityEngineApp/ie_index_registry/main/registry.json";

const response = await fetch(REGISTRY_URL);
const { indices } = await response.json();

// Filter by factor for UI dropdowns
const byFactor = indices.reduce((acc, idx) => {
  if (!acc[idx.iepa_factor]) acc[idx.iepa_factor] = [];
  acc[idx.iepa_factor].push(idx);
  return acc;
}, {});
```

### 9.3 Algorithm Engine
References `id` fields as canonical keys when pulling scored data from Supabase. Every country score stored in `raw_index_data` links back to an `index_id` that maps to a registry entry.

---

## 10. Versioning & Change Control

All changes are tracked via Git with conventional commit messages:

| Change Type | Commit Convention |
|---|---|
| New index added | `feat: add OECD PMR Index to Alignment factor` |
| Weight updated | `update: increase GII weight from 0.18 to 0.20` |
| New data year | `data: update latest_year to 2025 for 14 indices` |
| Index deprecated | `deprecate: remove Doing Business (replaced by Business Ready)` |
| Pipeline update | `feat: ie_pdf_pipeline.py v2 — 702-line production pipeline` |
| Score update | `feat: country_scores v2.1 — 2728 pts, 59 indices` |

**Version History:**
- **v1.0.0** — Initial release with 105 indices
- **v2.0.0** — Added 58 new indices, `data_years` field, enhanced schema (163 total)
- **v2.1.0** (Country Scores) — 2,728 data points, 59 indices, 13 countries, PDF pipeline

Weight changes require written justification in `metadata/weighting_rationale.md`.

---

## 11. Key Design Principles

1. **Single Source of Truth** — The registry is the canonical definition of what gets measured and how
2. **Non-Destructive Merging** — New data only fills gaps; existing values are never overwritten
3. **Multi-Source Validation** — PDF extraction is backstopped by curated data from published reports
4. **Transparency** — All metadata published under CC BY 4.0; full git audit trail
5. **Extensibility** — Standardized schema makes adding new indices straightforward
6. **Tier-Based Prioritization** — Clear separation between core algorithm inputs, validation signals, and contextual enrichment

---

*Built by Innovative EcoSystems — Designing the environments where innovation thrives.*
