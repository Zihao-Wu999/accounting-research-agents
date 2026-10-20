"""Shared run storage for all agents.

If DATABASE_URL is set (Postgres, e.g. Neon via Vercel), runs, progress logs and results are
stored there so the web UI can read them. Otherwise results are read from local output folders.

Tables are created on first use.
"""

import json
import os
from contextlib import contextmanager
from pathlib import Path

SCHEMA = """
create table if not exists runs (
    id          bigserial primary key,
    agent       text not null,
    params      jsonb not null default '{}',
    status      text not null default 'queued',   -- queued | running | succeeded | failed
    error       text,
    result      jsonb,
    created_at  timestamptz not null default now(),
    started_at  timestamptz,
    finished_at timestamptz
);
create table if not exists run_logs (
    id         bigserial primary key,
    run_id     bigint not null references runs(id) on delete cascade,
    ts         timestamptz not null default now(),
    message    text not null
);
create index if not exists run_logs_run_id on run_logs(run_id, id);
"""


def db_enabled() -> bool:
    return bool(os.getenv("DATABASE_URL"))


@contextmanager
def connect():
    import psycopg  # imported lazily so local runs don't need it

    with psycopg.connect(os.environ["DATABASE_URL"], autocommit=True) as conn:
        conn.execute(SCHEMA)
        yield conn


def create_run(agent: str, params: dict) -> int:
    with connect() as conn:
        return conn.execute(
            "insert into runs (agent, params) values (%s, %s) returning id", (agent, json.dumps(params))
        ).fetchone()[0]


def mark_running(run_id: int) -> None:
    with connect() as conn:
        conn.execute("update runs set status='running', started_at=now() where id=%s", (run_id,))


def log(run_id: int | None, message: str) -> None:
    print(message, flush=True)
    if run_id is None or not db_enabled():
        return
    with connect() as conn:
        conn.execute("insert into run_logs (run_id, message) values (%s, %s)", (run_id, message))


def finish_run(run_id: int, result: dict | None = None, error: str | None = None) -> None:
    with connect() as conn:
        conn.execute(
            "update runs set status=%s, result=%s, error=%s, finished_at=now() where id=%s",
            ("failed" if error else "succeeded", json.dumps(result) if result else None, error, run_id),
        )


def previous_results(agent: str, local_dir: Path, limit: int = 10) -> list[dict]:
    """Most recent successful results of `agent` (newest first), from Postgres or local JSON files."""
    if db_enabled():
        with connect() as conn:
            rows = conn.execute(
                "select result from runs where agent=%s and status='succeeded' and result is not null "
                "order by finished_at desc limit %s",
                (agent, limit),
            ).fetchall()
        return [r[0] for r in rows]
    files = sorted(local_dir.glob("*/literature_review.json"), reverse=True)[:limit]
    return [json.loads(f.read_text()) for f in files]
