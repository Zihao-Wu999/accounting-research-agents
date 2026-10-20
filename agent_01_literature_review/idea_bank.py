"""Cumulative idea and paper bank for Agent 01.

Ideas and papers persist across runs in idea_bank/ (committed to the repo by GitHub Actions):
- ideas.json: every idea ever proposed, with a stable id (I-001, ...), status, and version history.
- papers.json: every paper reviewed, keyed by paper_id.

Each run either adds new ideas or updates an earlier idea (when the model sets previous_idea_id).
"""

import json
from datetime import datetime
from pathlib import Path

BANK_DIR = Path(__file__).parent / "idea_bank"
IDEAS_FILE = BANK_DIR / "ideas.json"
PAPERS_FILE = BANK_DIR / "papers.json"


def _load(path: Path, default):
    return json.loads(path.read_text()) if path.exists() else default


def load_ideas() -> list[dict]:
    return _load(IDEAS_FILE, [])


def load_papers() -> dict[str, dict]:
    return _load(PAPERS_FILE, {})


def merge_run(result: dict, run_label: str) -> list[dict]:
    """Merge one run's output into the bank. Returns the full idea list with this run's changes flagged."""
    ideas = load_ideas()
    by_id = {i["id"]: i for i in ideas}
    next_num = max((int(i["id"].split("-")[1]) for i in ideas), default=0) + 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    for i in ideas:
        i["change_this_run"] = None
    for new in result.get("research_ideas", []):
        prev_id = new.get("previous_idea_id")
        if prev_id in by_id:
            entry = by_id[prev_id]
            entry["history"].append({"run": run_label, "at": now, "title": entry["idea"]["title"]})
            entry.update(idea=new, last_updated=now, change_this_run="updated")
        else:
            entry = {"id": f"I-{next_num:03d}", "first_seen": now, "last_updated": now, "status": "active",
                     "history": [{"run": run_label, "at": now, "title": new["title"]}],
                     "idea": new, "change_this_run": "new"}
            next_num += 1
            ideas.append(entry)
            by_id[entry["id"]] = entry

    papers = load_papers()
    for p in result.get("papers", []):
        papers[p["paper_id"]] = {**papers.get(p["paper_id"], {}), **p, "last_seen": now}

    BANK_DIR.mkdir(exist_ok=True)
    IDEAS_FILE.write_text(json.dumps(ideas, indent=2, ensure_ascii=False))
    PAPERS_FILE.write_text(json.dumps(papers, indent=2, ensure_ascii=False))
    return ideas


def summary_for_model() -> dict:
    """Compact view of the bank given to the model at the start of a run."""
    ideas = load_ideas()
    papers = load_papers()
    return {
        "n_ideas_in_bank": len(ideas),
        "previous_ideas": [
            {"id": i["id"], "status": i["status"], "last_updated": i["last_updated"],
             "title": i["idea"]["title"], "research_question": i["idea"]["research_question"],
             "novelty_angle": i["idea"]["novelty_angle"],
             "news_used": [n["url"] for n in i["idea"].get("news_triggers", [])]}
            for i in ideas
        ],
        "reviewed_papers": [
            {k: p.get(k) for k in ("paper_id", "title", "year", "venue", "main_findings")}
            for p in papers.values()
        ],
    }
