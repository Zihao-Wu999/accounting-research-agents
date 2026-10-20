"""Check which target journals are retrievable through OpenAlex, and how complete the records are.

Usage: .venv/bin/python agent_01_literature_review/tools/check_journal_coverage.py
"""

import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent))
from scholarly_search import JOURNALS, openalex_get  # noqa: E402

load_dotenv(Path(__file__).parents[2] / ".env")

YEARS = "2020-2026"


def main() -> None:
    print(f"{'Journal':<6} {'Indexed':<8} {'Works ' + YEARS:>16} {'With abstract':>14} {'Latest pub date':>16}")
    for short, (name, issn) in JOURNALS.items():
        try:
            base = f"primary_location.source.issn:{issn},publication_year:{YEARS},type:article|preprint"
            total = openalex_get("/works", {"filter": base, "per-page": 1})["meta"]["count"]
            with_abs = openalex_get("/works", {"filter": base + ",has_abstract:true", "per-page": 1})["meta"]["count"]
            latest = openalex_get("/works", {"filter": base, "sort": "publication_date:desc", "per-page": 1})["results"]
            latest_date = latest[0]["publication_date"] if latest else "-"
            pct = f"{with_abs / total:.0%}" if total else "-"
            print(f"{short:<6} {'yes' if total else 'NO':<8} {total:>16,} {pct:>14} {latest_date:>16}")
        except Exception as e:  # noqa: BLE001
            print(f"{short:<6} ERROR {e}")


if __name__ == "__main__":
    main()
