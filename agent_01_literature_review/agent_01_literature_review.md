# Agent 01 — Literature Review

## Role
Given a research topic, systematically search the accounting literature (plus related finance and
economics work) and produce a structured literature database, literature streams, research gaps,
and hand-off information for downstream agents.

## Run
```bash
.venv/bin/python agent_01_literature_review/agent_01_literature_review.py "CEO overconfidence and audit fees"
```
API keys are read from the project-level `.env` (see `.env.example`).

## Input (`LiteratureReviewInput`)
| Field | Description | Example |
|---|---|---|
| `topic` | Research topic / preliminary question | "CEO overconfidence and audit fees" |
| `keywords` | Optional extra keywords | ["managerial overconfidence", "audit pricing"] |
| `year_start`, `year_end` | Publication year range | 2000–2026 |
| `max_papers` | Max number of papers | 25 |

## Tools
| Tool | Backend | Covers |
|---|---|---|
| `search_journals` | OpenAlex API | TAR, JAR, JAE, CAR, RAST, AOS, AJPT, MS, JF, JFE, RFS |
| `search_ssrn` | OpenAlex (SSRN DOIs 10.2139/ssrn.*) | SSRN working papers |
| `search_semantic_scholar` | Semantic Scholar API | Cross-check index |
| `web_search` | OpenAI hosted web search | Conference programs, SSRN abstract pages, missing abstracts |

SSRN has no official API; it is reached through OpenAlex's SSRN index and through web search.

### Coverage check (OpenAlex, 2020–2026, run 2026-10-20)
Run `tools/check_journal_coverage.py` to refresh.

| Journal | Indexed | Articles | With abstract | Latest |
|---|---|---|---|---|
| TAR | yes | 697 | 95% | 2026-10 |
| JAR | yes | 301 | 92% | 2026-10 |
| JAE | yes | 338 | **21%** | 2026-10 |
| CAR | yes | 539 | 95% | 2026-10 |
| RAST | yes | 423 | **47%** | 2026-10 |
| AOS | yes | 221 | **34%** | 2026-10 |
| AJPT | yes | 253 | 90% | 2026-10 |
| MS | yes | 2,842 | 94% | 2026-10 |
| JF | yes | 624 | 79% | 2026-10 |
| JFE | yes | 873 | **27%** | 2026-10 |
| RFS | yes | 710 | 95% | 2026-10 |
| SSRN | yes | 838,465 | **2%** | 2026-09 |

All journals are retrievable (titles, authors, year, citations). Abstracts are largely missing for
Elsevier journals (JAE, JFE, AOS) and SSRN, so the agent falls back to web search for those.

## Output (`LiteratureReviewOutput`, see `schemas.py`)
1. `papers` — structured paper cards (question, sample, datasets, identification, findings, theories, relevance)
2. `streams` — literature streams and how they developed
3. `research_gaps` — candidate gaps grounded in specific papers
4. `frontier` — recent working/conference papers with overlap risk
5. `measures` — construct → measure → source papers (→ data cleaning agent)
6. `datasets` — databases used and how often (→ data cleaning agent)
7. `theories` — theories and how they are used (→ theory matching agent)
8. `bibtex` — references for LaTeX
9. `narrative` — draft related-literature section
10. `search_log` — every query run, for reproducibility

Saved to `outputs/<timestamp>_<topic>/`: `literature_review.json`, `references.bib`, `related_literature.md`.

## Files
Everything for this agent lives in this folder. The only file outside it is the GitHub Actions
workflow `.github/workflows/agent_01_literature_review.yml` (GitHub requires that location).
```
agent_01_literature_review/
├── agent_01_literature_review.md   # this spec
├── agent_01_literature_review.py   # the agent (OpenAI Agents SDK)
├── schemas.py                      # input/output data contracts
├── idea_bank.py                    # cumulative idea + paper bank across runs
├── requirements.txt                # Python dependencies for this agent
├── prompts/system_prompt.md        # agent instructions
├── tools/                          # search tools, conference list, WRDS catalog
├── idea_bank/                      # ideas.json, papers.json, idea_bank.md (persisted)
└── outputs/                        # per-run result files
```

## Conference sources
- `tools/conferences.yaml` — curated list: 19 general conferences + 15 AAA meetings (with verified
  paper-level program pages, e.g. `https://aaahq.org/Meetings/{year}/{slug}/Program`) and access level
  (`public_papers`, `public_sessions`, `members_only`, `cfp_only`, `unverified`).
- `tools/fetch_conference_calendar.py` — downloads the EAA Accounting Research Calendar
  (public JSON API, 1,205 events since 2017) to `outputs/conference_calendar/`.
- SSRN's ARN conference pages are stale (archive ends 2019, announcements end 2018) and block
  scripted access, so they are not used.
