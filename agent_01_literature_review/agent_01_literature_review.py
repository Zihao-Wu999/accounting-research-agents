"""Agent 01 — Literature Review & Idea Generation.

Usage:
    .venv/bin/python agent_01_literature_review/agent_01_literature_review.py "CEO overconfidence and audit fees"
    .venv/bin/python agent_01_literature_review/agent_01_literature_review.py --run-id 12   # params from DB (web UI)
"""

import argparse
import asyncio
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from agents import Agent, RunHooks, Runner, WebSearchTool, function_tool
from dotenv import load_dotenv

AGENT_NAME = "agent_01_literature_review"
AGENT_DIR = Path(__file__).parent
sys.path.insert(0, str(AGENT_DIR))
sys.path.insert(0, str(AGENT_DIR.parent))
load_dotenv(AGENT_DIR.parent / ".env")

from schemas import LiteratureReviewInput, LiteratureReviewOutput  # noqa: E402
import idea_bank  # noqa: E402
from common import storage  # noqa: E402
from tools import scholarly_search as ss  # noqa: E402


def _safe(fn, **kwargs) -> str:
    try:
        return json.dumps(fn(**kwargs), ensure_ascii=False)
    except Exception as e:  # noqa: BLE001 - report errors back to the model instead of crashing
        return json.dumps({"error": str(e)})


@function_tool
def search_journals(query: str, journals: list[str], year_from: int, year_to: int, limit: int = 15) -> str:
    """Search published papers in specific journals via OpenAlex.

    Args:
        query: Keywords, e.g. "CEO overconfidence audit fees".
        journals: Journal short names from: TAR, JAR, JAE, CAR, RAST, AOS, AJPT, MS, JF, JFE, RFS.
            Pass an empty list to search all journals indexed by OpenAlex.
        year_from: First publication year.
        year_to: Last publication year.
        limit: Max results (<= 50).
    """
    return _safe(ss.search_openalex, query=query, year_from=year_from, year_to=year_to,
                 journals=journals or None, limit=limit)


@function_tool
def search_ssrn(query: str, year_from: int, year_to: int, limit: int = 15) -> str:
    """Search SSRN working papers (indexed via OpenAlex). Abstracts are usually missing.

    Args:
        query: Keywords.
        year_from: First year.
        year_to: Last year.
        limit: Max results (<= 50).
    """
    return _safe(ss.search_ssrn, query=query, year_from=year_from, year_to=year_to, limit=limit)


@function_tool
def search_semantic_scholar(query: str, year_from: int, year_to: int, limit: int = 15) -> str:
    """Search Semantic Scholar (cross-check index; may be rate-limited).

    Args:
        query: Keywords.
        year_from: First year.
        year_to: Last year.
        limit: Max results (<= 100).
    """
    return _safe(ss.search_semantic_scholar, query=query, year_from=year_from, year_to=year_to, limit=limit)


@function_tool
def search_edgar_fulltext(query: str, forms: str, start_date: str, end_date: str) -> str:
    """Count SEC EDGAR filings whose text contains a phrase, to check text-data availability.

    Args:
        query: Search phrase; wrap exact phrases in double quotes, e.g. "\"tariff\"".
        forms: Comma-separated form types, e.g. "10-K" or "10-K,10-Q,8-K".
        start_date: YYYY-MM-DD (full-text search covers 2001 onward).
        end_date: YYYY-MM-DD.
    """
    return _safe(ss.search_edgar_fulltext, query=query, forms=forms, start_date=start_date, end_date=end_date)


@function_tool
def get_wrds_catalog() -> str:
    """Return the catalog of WRDS datasets and free text sources available to this project."""
    return (AGENT_DIR / "tools" / "wrds_catalog.yaml").read_text()


class ProgressLogger(RunHooks):
    """Print one line per model call / tool call so long runs are observable."""

    def __init__(self, run_id: int | None = None) -> None:
        self.run_id = run_id
        self.start = datetime.now()
        self.turn = 0

    def _log(self, msg: str) -> None:
        storage.log(self.run_id, f"[{(datetime.now() - self.start).seconds:>4}s] {msg}")

    async def on_llm_start(self, context, agent, system_prompt, input_items) -> None:
        self.turn += 1
        self._log(f"model call #{self.turn} started")

    async def on_llm_end(self, context, agent, response) -> None:
        for item in response.output:
            if item.type == "web_search_call":
                action = getattr(item, "action", None)
                self._log(f"  web_search: {getattr(action, 'query', None) or getattr(action, 'type', '')}")
        u = response.usage
        self._log(f"model call #{self.turn} done (input {u.input_tokens:,} / output {u.output_tokens:,} tokens)")

    async def on_tool_start(self, context, agent, tool) -> None:
        args = getattr(context, "tool_arguments", "") or ""
        self._log(f"  tool {tool.name} {args[:150]}")


@function_tool
def get_previous_results() -> str:
    """Return the cumulative idea bank (ids, titles, questions) and papers reviewed in earlier runs.

    Call this first. Do not re-propose existing ideas; set previous_idea_id when updating one.
    """
    return json.dumps(idea_bank.summary_for_model(), ensure_ascii=False)


def build_agent() -> Agent:
    return Agent(
        name="Agent 01 - Literature Review",
        instructions=(AGENT_DIR / "prompts" / "system_prompt.md").read_text(),
        tools=[get_previous_results, search_journals, search_ssrn, search_semantic_scholar, search_edgar_fulltext,
               get_wrds_catalog, WebSearchTool()],
        output_type=LiteratureReviewOutput,
        model=os.getenv("OPENAI_MODEL") or None,
    )


def save_outputs(result: LiteratureReviewOutput) -> Path:
    slug = re.sub(r"[^a-z0-9]+", "_", result.topic.lower()).strip("_")[:50]
    out_dir = AGENT_DIR / "outputs" / f"{datetime.now():%Y%m%d_%H%M%S}_{slug}"
    out_dir.mkdir(parents=True)
    (out_dir / "literature_review.json").write_text(result.model_dump_json(indent=2))
    (out_dir / "references.bib").write_text(result.bibtex)
    (out_dir / "related_literature.md").write_text(f"# Related Literature: {result.topic}\n\n{result.narrative}\n")
    bank = idea_bank.merge_run(result.model_dump(), run_label=out_dir.name)
    report = render_ideas(result, bank)
    (out_dir / "research_ideas.md").write_text(report)
    (idea_bank.BANK_DIR / "idea_bank.md").write_text(report)
    return out_dir


def _cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def _idea_details(entry: dict, papers: dict[str, dict]) -> list[str]:
    idea, d = entry["idea"], entry["idea"]["data"]
    stars = "★" * idea["novelty_score"] + "☆" * (5 - idea["novelty_score"])
    return [
        f"**Novelty** {stars} · **Data feasibility** `{d['feasibility']}` · "
        f"first seen {entry['first_seen']} · last updated {entry['last_updated']}\n",
        f"> **Research question.** {idea['research_question']}\n",
        "| | |", "|---|---|",
        f"| **What it is** | {_cell(idea['idea'])} |",
        f"| **Gap** | {_cell(idea['gap'])} |",
        f"| **Novel angle** | {_cell(idea['novelty_angle'])} |",
        f"| **Accounting angle** | {_cell(idea['accounting_angle'])} |",
        f"| **Identification** | {_cell(idea['identification'])} |",
        f"| **Risks** | {_cell(idea['risks'])} |",
        "", "**Hypotheses**", *[f"- {h}" for h in idea["hypotheses"]], "",
        "<details><summary><b>Data plan</b></summary>\n",
        f"- **WRDS:** {', '.join(d['wrds_datasets'])}",
        f"- **Disclosure text:** {', '.join(d['text_data'])}",
        f"- **Sample:** {d['sample']}",
        "- **Key variables:**", *[f"  - {v}" for v in d["key_variables"]],
        f"- **EDGAR check:** {d['edgar_evidence']}",
        f"- **Feasibility notes:** {d['feasibility_notes']}",
        "\n</details>\n",
        "<details><summary><b>News triggers</b></summary>\n",
        *[f"- [{n['headline']}]({n['url']}) — {n['source']}, {n['date']}" for n in idea["news_triggers"]],
        "\n</details>\n",
        "<details><summary><b>Related papers</b></summary>\n",
        *[f"- {p['title']} ({', '.join(p['authors'][:3])}, {p['year']}, {p['venue']})"
          for pid in idea["related_paper_ids"] if (p := papers.get(pid))],
        "\n</details>",
        "<details><summary><b>Version history</b></summary>\n",
        *[f"- {h['at']} — {h['run']}" for h in entry["history"]],
        "\n</details>",
    ]


def render_ideas(result: LiteratureReviewOutput, bank: list[dict]) -> str:
    """Markdown report of the whole idea bank (new/updated ideas first); also the GitHub job summary."""
    papers = idea_bank.load_papers()
    changed = [e for e in bank if e["change_this_run"]]
    history = sorted((e for e in bank if not e["change_this_run"]), key=lambda e: e["last_updated"], reverse=True)
    badge = {"new": "🆕 new", "updated": "🔄 updated", None: "—"}
    lines = [
        "# Research Idea Bank",
        f"_Run {datetime.now():%Y-%m-%d %H:%M} · topic: {result.topic}_\n",
        f"**{sum(e['change_this_run'] == 'new' for e in bank)} new · "
        f"{sum(e['change_this_run'] == 'updated' for e in bank)} updated · {len(bank)} ideas in bank · "
        f"{len(papers)} papers reviewed in total**\n",
        "## Overview\n",
        "| ID | This run | Idea | Novelty | Data | Last updated |",
        "|---|---|---|---|---|---|",
    ]
    for e in changed + history:
        i = e["idea"]
        lines.append(f"| {e['id']} | {badge[e['change_this_run']]} | [{_cell(i['title'])}](#{e['id'].lower()}) | "
                     f"{i['novelty_score']}/5 | {i['data']['feasibility']} | {e['last_updated']} |")
    lines += ["", "## New and updated ideas this run"]
    for e in changed:
        lines += ["", "---", "", f'<a id="{e["id"].lower()}"></a>',
                  f"### {e['id']} · {e['idea']['title']} ({badge[e['change_this_run']]})", *_idea_details(e, papers)]
    if history:
        lines += ["", "## Earlier ideas"]
        for e in history:
            lines += ["", f'<a id="{e["id"].lower()}"></a>',
                      f"<details><summary><b>{e['id']} · {e['idea']['title']}</b></summary>\n",
                      *_idea_details(e, papers), "\n</details>"]
    return "\n".join(lines) + "\n"


async def run(inp: LiteratureReviewInput, run_id: int | None = None) -> LiteratureReviewOutput:
    message = (
        f"Today's date: {datetime.now():%Y-%m-%d}\n"
        f"Research area/topic: {inp.topic}\n"
        f"Number of research ideas: {inp.n_ideas}\n"
        f"News window: last {inp.news_window_months} months\n"
        f"Extra keywords: {', '.join(inp.keywords) or 'none'}\n"
        f"Year range: {inp.year_start}-{inp.year_end}\n"
        f"Target number of papers: up to {inp.max_papers}"
    )
    result = await Runner.run(build_agent(), message, max_turns=80, hooks=ProgressLogger(run_id))
    return result.final_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", nargs="?")
    parser.add_argument("--run-id", type=int, help="Run created by the web UI; params are read from the database")
    parser.add_argument("--keywords", nargs="*", default=[])
    parser.add_argument("--year-start", type=int, default=2000)
    parser.add_argument("--year-end", type=int, default=2026)
    parser.add_argument("--max-papers", type=int, default=30)
    parser.add_argument("--ideas", type=int, default=5)
    parser.add_argument("--news-months", type=int, default=6)
    args = parser.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY is empty. Fill it in the project's .env file.")

    if args.run_id:
        with storage.connect() as conn:
            params = conn.execute("select params from runs where id=%s", (args.run_id,)).fetchone()[0]
        inp = LiteratureReviewInput(**params)
        storage.mark_running(args.run_id)
    elif args.topic:
        inp = LiteratureReviewInput(topic=args.topic, keywords=args.keywords, year_start=args.year_start,
                                    year_end=args.year_end, max_papers=args.max_papers,
                                    n_ideas=args.ideas, news_window_months=args.news_months)
    else:
        sys.exit("Provide a topic or --run-id.")

    try:
        output = asyncio.run(run(inp, args.run_id))
    except Exception as e:
        if args.run_id:
            storage.finish_run(args.run_id, error=f"{type(e).__name__}: {e}")
        raise
    out_dir = save_outputs(output)
    if args.run_id:
        storage.finish_run(args.run_id, result=output.model_dump())
    storage.log(args.run_id, f"Done: {len(output.research_ideas)} ideas, {len(output.papers)} papers. Saved to {out_dir}")


if __name__ == "__main__":
    main()
