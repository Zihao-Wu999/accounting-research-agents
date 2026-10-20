"""Download the EAA Accounting Research Calendar (calls for papers, conferences, workshops).

The calendar exposes a public WordPress JSON API, so no scraping is needed.
Output: agent_01_literature_review/outputs/conference_calendar/{calendar.json, calendar.csv}

Usage: .venv/bin/python agent_01_literature_review/tools/fetch_conference_calendar.py [--since 2025-01-01]
"""

import argparse
import csv
import html
import json
import re
from pathlib import Path

import httpx

API = "https://eaa-online.org/arc/wp-json/wp/v2"
OUT_DIR = Path(__file__).parents[1] / "outputs" / "conference_calendar"
HEADERS = {"User-Agent": "accounting-research-agent/0.1"}


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", text))).strip()


def _get_all(client: httpx.Client, path: str, params: dict) -> list[dict]:
    items, page = [], 1
    while True:
        resp = client.get(f"{API}/{path}", params={**params, "per_page": 100, "page": page})
        if resp.status_code == 400:  # past the last page
            break
        resp.raise_for_status()
        items += resp.json()
        if page >= int(resp.headers.get("X-WP-TotalPages", 1)):
            break
        page += 1
    return items


def fetch(since: str | None) -> list[dict]:
    with httpx.Client(headers=HEADERS, timeout=60) as client:
        terms = {}
        for taxonomy in ("event_category", "event_tag"):
            for t in _get_all(client, taxonomy, {"_fields": "id,name"}):
                terms[(taxonomy, t["id"])] = html.unescape(t["name"])

        params = {"_fields": "id,date,link,title,content,event_category,event_tag"}
        if since:
            params["after"] = f"{since}T00:00:00"
        events = _get_all(client, "event", params)

    return [
        {
            "posted": e["date"][:10],
            "title": _clean(e["title"]["rendered"]),
            "categories": "; ".join(terms.get(("event_category", i), str(i)) for i in e["event_category"]),
            "tags": "; ".join(terms.get(("event_tag", i), str(i)) for i in e["event_tag"]),
            "url": e["link"],
            "text": _clean(e["content"]["rendered"])[:3000],
        }
        for e in events
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", help="Only events posted on/after this date (YYYY-MM-DD)")
    args = parser.parse_args()

    rows = fetch(args.since)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "calendar.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False))
    with open(OUT_DIR / "calendar.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} events to {OUT_DIR}")


if __name__ == "__main__":
    main()
