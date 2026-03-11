#!/usr/bin/env python3
"""
IEPA Country Scores Pipeline
Maintained by Innovative EcoSystems
Fetches 2020-2024 data for 13 Tier 1 markets across IEPA-mapped indices.
Run: python3 pipeline.py
Output: country_scores.json
"""

import requests, json, time, base64, urllib.request

TIER1 = {
    "VNM": "Vietnam", "IND": "India", "EGY": "Egypt", "TUR": "Turkey",
    "THA": "Thailand", "KOR": "South Korea", "PHL": "Philippines",
    "SAU": "Saudi Arabia", "ARE": "UAE", "IDN": "Indonesia",
    "MYS": "Malaysia", "MAR": "Morocco", "KEN": "Kenya"
}
YEARS = [2020, 2021, 2022, 2023, 2024]
scores = {}

def store(index_id, iso, year, value):
    if index_id not in scores:
        scores[index_id] = {}
    if iso not in scores[index_id]:
        scores[index_id][iso] = {}
    if value is not None:
        try:
            scores[index_id][iso][str(year)] = round(float(value), 4)
        except: pass

def fetch_wb(indicator, index_id):
    iso_str = ";".join(TIER1.keys())
    url = f"https://api.worldbank.org/v2/country/{iso_str}/indicator/{indicator}"
    try:
        r = requests.get(url, params={"date": "2020:2024", "format": "json", "per_page": 1000}, timeout=20)
        if r.status_code == 200:
            data = r.json()
            if len(data) > 1 and data[1]:
                for entry in data[1]:
                    iso = entry.get("countryiso3code")
                    year = entry.get("date")
                    value = entry.get("value")
                    if iso in TIER1 and value is not None:
                        store(index_id, iso, int(year), value)
        time.sleep(0.4)
    except Exception as e:
        print(f"  WB {indicator}: {e}")

# World Bank indicators
wb_map = {
    "GE.EST": "WGI_GOV_EFF", "RQ.EST": "WGI_REG_QUALITY",
    "VA.EST": "WGI_VOICE_ACC", "PV.EST": "WGI_POLITICAL_STABILITY",
    "CC.EST": "WGI_CONTROL_CORRUPTION", "RL.EST": "RULE_OF_LAW",
    "HD.HCI.OVRL": "WB_HUMAN_CAPITAL", "NY.GDP.PCAP.KD": "IMF_GDP_GROWTH",
    "BX.KLT.DINV.CD.WD": "WB_FDI",
    "BX.KLT.DINV.WD.GD.ZS": "UNCTAD_FDI_INFLOWS",
    "LP.LPI.OVRL.XQ": "LPI", "SL.UEM.TOTL.ZS": "ILO_EMPLOYMENT",
    "SL.UEM.1524.ZS": "ILO_LABOUR_EXTENDED", "SH.DYN.MORT": "WHO_HEALTH",
    "SP.DYN.LE00.IN": "HDI", "SE.TER.ENRR": "OECD_EDUCATION",
    "SI.POV.GINI": "HOUSEHOLD_INCOME", "EG.ELC.ACCS.ZS": "ENERGY_TRANSITION",
    "IT.NET.USER.ZS": "ITU_DIGITAL_DEV", "IT.CEL.SETS.P2": "ITU_ICT",
    "GB.XPD.RSDV.GD.ZS": "OECD_MSTI", "IP.PAT.RESD": "WIPO_PATENTS",
    "TX.VAL.TECH.MF.ZS": "WEF_TECH_FRONTIER",
    "NY.GNP.PCAP.CD": "WB_NATIONAL_ACCOUNTS",
    "NY.GDP.MKTP.KD.ZG": "IMF_WEO_EXTENDED",
    "SG.GEN.PARL.ZS": "GLOBAL_GENDER_GAP",
    "SP.POP.TOTL": "GCI_MARKET_SIZE",
    "SH.XPD.CHEX.GD.ZS": "LANCET_BURDEN",
    "NE.EXP.GNFS.ZS": "KOF_GLOBALISATION",
}

print("Fetching World Bank data...")
for wb_code, idx_id in wb_map.items():
    fetch_wb(wb_code, idx_id)

# IMF WEO
print("Fetching IMF WEO data...")
imf_map = {"NGDP_RPCH": "IMF_WEO_EXTENDED", "NGDPD": "IMF_GDP_GROWTH", "LUR": "ILO_EMPLOYMENT", "BCA_NGDPD": "UNCTAD_WIR"}
for imf_code, idx_id in imf_map.items():
    try:
        r = requests.get(f"https://www.imf.org/external/datamapper/api/v1/{imf_code}", timeout=15)
        if r.status_code == 200:
            values = r.json().get("values", {}).get(imf_code, {})
            for iso in TIER1:
                for year in YEARS:
                    val = values.get(iso, {}).get(str(year))
                    if val: store(idx_id, iso, year, val)
        time.sleep(0.5)
    except: pass

print(f"Pipeline complete: {len(scores)} indices, {sum(len(y) for i in scores.values() for y in i.values())} data points")

# Build output
country_data = {iso: {"country": name, "iso3": iso, "scores": {}} for iso, name in TIER1.items()}
for idx_id, cdata in scores.items():
    for iso, ydata in cdata.items():
        if iso in country_data and ydata:
            country_data[iso]["scores"][idx_id] = ydata

output = {
    "meta": {
        "name": "IEPA Country Scores Dataset",
        "version": "1.0.0",
        "last_updated": "auto-generated",
        "description": "Run pipeline.py to refresh. See registry.json for index metadata."
    },
    "country_scores": country_data
}

with open("country_scores.json", "w") as f:
    json.dump(output, f, indent=2)
print("Saved country_scores.json")
