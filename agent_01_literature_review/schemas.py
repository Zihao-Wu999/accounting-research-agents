"""Input / output contracts for Agent 01 (Literature Review).

The output model is meant to be passed as `output_type` to an OpenAI Agents SDK
`Agent`, so downstream agents receive structured data instead of free text.
"""

from typing import Literal

from pydantic import BaseModel, Field


# ---------- Input ----------

class LiteratureReviewInput(BaseModel):
    topic: str = Field(description="Research area or preliminary question; broad areas allowed, e.g. 'auditing'")
    keywords: list[str] = Field(default_factory=list)
    year_start: int = 2000
    year_end: int = 2026
    max_papers: int = 30
    n_ideas: int = 5
    news_window_months: int = 6


# ---------- Output building blocks ----------

class Paper(BaseModel):
    paper_id: str = Field(description="DOI, SSRN id, or OpenAlex id")
    title: str
    authors: list[str]
    year: int
    venue: str = Field(description="Journal, working paper series, or conference name")
    status: Literal["published", "working_paper", "conference"]
    source: str = Field(description="Where it was found, e.g. OpenAlex, SSRN, AAA 2026 agenda")
    url: str | None = None
    research_question: str
    sample: str = Field(description="Setting, period, and sample size")
    datasets: list[str] = Field(description="e.g. Compustat, CRSP, Audit Analytics")
    identification: str = Field(description="Empirical design, e.g. DiD around SOX 404")
    main_findings: str
    theories: list[str]
    relevance_score: int = Field(ge=1, le=5, description="Relevance to the input topic")


class LiteratureStream(BaseModel):
    name: str
    summary: str
    key_paper_ids: list[str]


class ResearchGap(BaseModel):
    description: str
    rationale: str
    supporting_paper_ids: list[str]


class FrontierPaper(BaseModel):
    """Recent working / conference papers that may overlap with our idea."""
    paper_id: str
    title: str
    venue: str
    overlap_risk: Literal["low", "medium", "high"]
    note: str


class Measure(BaseModel):
    concept: str = Field(description="Construct being measured, e.g. earnings management")
    measure: str = Field(description="e.g. modified Jones discretionary accruals")
    source_paper_ids: list[str]


class Theory(BaseModel):
    name: str = Field(description="e.g. agency theory, signaling theory")
    how_used: str
    source_paper_ids: list[str]


class DatasetUsage(BaseModel):
    name: str = Field(description="e.g. Compustat, CRSP, Audit Analytics")
    n_papers: int


class NewsItem(BaseModel):
    headline: str
    source: str = Field(description="Outlet, e.g. Reuters, WSJ, SEC press release")
    date: str = Field(description="Publication date, YYYY-MM-DD")
    url: str


class DataPlan(BaseModel):
    wrds_datasets: list[str] = Field(description="Datasets from the WRDS catalog, e.g. Compustat, Audit Analytics")
    text_data: list[str] = Field(description="Disclosure text used, e.g. 10-K Item 1A risk factors, 8-K Item 4.02")
    key_variables: list[str] = Field(description="Dependent, treatment, and control variables with how they are built")
    sample: str = Field(description="Sample firms and period")
    edgar_evidence: str = Field(description="EDGAR full-text search queries run and hit counts, or 'not checked'")
    feasibility: Literal["high", "medium", "low"]
    feasibility_notes: str = Field(description="Main data risks, e.g. small treated sample, hand collection needed")


class ResearchIdea(BaseModel):
    previous_idea_id: str | None = Field(
        description="ID of an idea from the idea bank (e.g. I-003) that this idea updates; null if brand new")
    title: str
    news_triggers: list[NewsItem] = Field(description="Recent news that motivates the idea")
    idea: str = Field(description="What the idea is, in 2-4 sentences")
    research_question: str
    accounting_angle: str = Field(description="Why this is an accounting question (reporting, disclosure, audit, tax, governance)")
    gap: str = Field(description="What the existing literature has not answered, citing paper_ids")
    novelty_angle: str = Field(description="What is new: setting, shock, data, mechanism, or measure")
    hypotheses: list[str]
    identification: str = Field(description="Empirical design and source of variation")
    data: DataPlan
    related_paper_ids: list[str]
    novelty_score: int = Field(ge=1, le=5, description="5 = no close paper found, including SSRN/conferences")
    risks: str = Field(description="Biggest threats: scoop risk, identification, data")


class SearchLogEntry(BaseModel):
    source: str
    query: str
    n_results: int
    retrieved_at: str


# ---------- Output ----------

class LiteratureReviewOutput(BaseModel):
    topic: str
    research_ideas: list[ResearchIdea]
    papers: list[Paper]
    streams: list[LiteratureStream]
    research_gaps: list[ResearchGap]
    frontier: list[FrontierPaper]
    measures: list[Measure]            # -> data cleaning agent
    datasets: list[DatasetUsage]       # -> data cleaning agent
    theories: list[Theory]             # -> theory matching agent
    bibtex: str
    narrative: str = Field(description="Draft related-literature section")
    search_log: list[SearchLogEntry]
