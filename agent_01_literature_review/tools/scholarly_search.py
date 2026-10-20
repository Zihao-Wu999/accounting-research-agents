"""Plain-Python scholarly search helpers used as tools by Agent 01.

Sources:
- OpenAlex: journals + SSRN (SSRN papers carry DOIs 10.2139/ssrn.*, indexed as
  "SSRN Electronic Journal", ISSN 1556-5068). Free; an API key raises the daily budget.
- Semantic Scholar: optional second index; heavily rate-limited without a key.
"""

import os
import time

import httpx

OPENALEX_URL = "https://api.openalex.org"
S2_URL = "https://api.semanticscholar.org/graph/v1"

# Journal short name -> (full name, print ISSN)
JOURNALS = {
    "TAR": ("The Accounting Review", "0001-4826"),
    "JAR": ("Journal of Accounting Research", "0021-8456"),
    "JAE": ("Journal of Accounting and Economics", "0165-4101"),
    "CAR": ("Contemporary Accounting Research", "0823-9150"),
    "RAST": ("Review of Accounting Studies", "1380-6653"),
    "AOS": ("Accounting, Organizations and Society", "0361-3682"),
    "AJPT": ("Auditing: A Journal of Practice & Theory", "0278-0380"),
    "MS": ("Management Science", "0025-1909"),
    "JF": ("Journal of Finance", "0022-1082"),
    "JFE": ("Journal of Financial Economics", "0304-405X"),
    "RFS": ("Review of Financial Studies", "0893-9454"),
    "SSRN": ("SSRN Electronic Journal", "1556-5068"),
}


def _openalex_params(params: dict) -> dict:
    if key := os.getenv("OPENALEX_API_KEY"):
        params["api_key"] = key
    if email := os.getenv("OPENALEX_EMAIL"):
        params["mailto"] = email
    return params


def openalex_get(path: str, params: dict | None = None) -> dict:
    resp = httpx.get(f"{OPENALEX_URL}{path}", params=_openalex_params(params or {}), timeout=30)
    resp.raise_for_status()
    return resp.json()


def _abstract(inverted_index: dict | None) -> str | None:
    if not inverted_index:
        return None
    positions = [(i, word) for word, idxs in inverted_index.items() for i in idxs]
    return " ".join(word for _, word in sorted(positions))


def _format_openalex_work(w: dict) -> dict:
    source = (w.get("primary_location") or {}).get("source") or {}
    return {
        "id": w.get("doi") or w.get("id"),
        "title": w.get("title"),
        "authors": [a["author"]["display_name"] for a in w.get("authorships", [])][:8],
        "year": w.get("publication_year"),
        "venue": source.get("display_name"),
        "cited_by": w.get("cited_by_count"),
        "abstract": (_abstract(w.get("abstract_inverted_index")) or "")[:1500] or None,
    }


def search_openalex(
    query: str,
    year_from: int = 2000,
    year_to: int = 2026,
    journals: list[str] | None = None,
    limit: int = 15,
) -> list[dict]:
    """Search OpenAlex. `journals` is a list of short names from JOURNALS (e.g. ["TAR", "SSRN"])."""
    filters = [f"publication_year:{year_from}-{year_to}"]
    if journals:
        issns = [JOURNALS[j][1] for j in journals if j in JOURNALS]
        if issns:
            filters.append("primary_location.source.issn:" + "|".join(issns))
    data = openalex_get(
        "/works",
        {"search": query, "filter": ",".join(filters), "per-page": min(limit, 50), "sort": "relevance_score:desc"},
    )
    return [_format_openalex_work(w) for w in data.get("results", [])]


def search_ssrn(query: str, year_from: int = 2015, year_to: int = 2026, limit: int = 15) -> list[dict]:
    """Search SSRN working papers (via OpenAlex's SSRN index)."""
    return search_openalex(query, year_from, year_to, journals=["SSRN"], limit=limit)


def search_semantic_scholar(query: str, year_from: int = 2000, year_to: int = 2026, limit: int = 15) -> list[dict]:
    headers = {"x-api-key": key} if (key := os.getenv("SEMANTIC_SCHOLAR_API_KEY")) else {}
    params = {
        "query": query,
        "year": f"{year_from}-{year_to}",
        "limit": min(limit, 100),
        "fields": "title,authors,year,venue,externalIds,citationCount,abstract",
    }
    for attempt in range(3):
        resp = httpx.get(f"{S2_URL}/paper/search", params=params, headers=headers, timeout=30)
        if resp.status_code != 429:
            break
        time.sleep(2 ** attempt * 3)
    resp.raise_for_status()
    return [
        {
            "id": (p.get("externalIds") or {}).get("DOI") or p.get("paperId"),
            "title": p.get("title"),
            "authors": [a["name"] for a in p.get("authors", [])][:8],
            "year": p.get("year"),
            "venue": p.get("venue"),
            "cited_by": p.get("citationCount"),
            "abstract": (p.get("abstract") or "")[:1500] or None,
        }
        for p in resp.json().get("data", [])
    ]


# ---------- SEC EDGAR full-text search (10-K text availability) ----------

EDGAR_FTS_URL = "https://efts.sec.gov/LATEST/search-index"


def search_edgar_fulltext(
    query: str, forms: str = "10-K", start_date: str = "2020-01-01", end_date: str | None = None, limit: int = 10
) -> dict:
    """Count EDGAR filings containing `query` (use quotes for phrases) and return sample filings.

    SEC requires a descriptive User-Agent with contact info (SEC_USER_AGENT in .env).
    """
    params = {"q": query, "forms": forms, "dateRange": "custom", "startdt": start_date}
    if end_date:
        params["enddt"] = end_date
    headers = {"User-Agent": os.getenv("SEC_USER_AGENT") or "AccountingResearchAgent admin@example.org"}
    resp = httpx.get(EDGAR_FTS_URL, params=params, headers=headers, timeout=30)
    resp.raise_for_status()
    hits = resp.json()["hits"]
    return {
        "total_hits": hits["total"]["value"],
        "total_is_lower_bound": hits["total"].get("relation") == "gte",
        "unique_filings_in_sample": len({h["_source"]["adsh"] for h in hits["hits"]}),
        "samples": [
            {
                "company": h["_source"]["display_names"][0],
                "form": h["_source"]["form"],
                "file_date": h["_source"]["file_date"],
                "document": h["_source"].get("file_type"),
                "sic": (h["_source"].get("sics") or [None])[0],
            }
            for h in hits["hits"][:limit]
        ],
    }
