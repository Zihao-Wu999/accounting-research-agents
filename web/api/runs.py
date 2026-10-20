"""GET /api/runs        -> recent runs
POST /api/runs       -> create a run and trigger the GitHub Actions workflow that executes the agent
"""

import json
import os
import sys
from http.server import BaseHTTPRequestHandler
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).parents[2]))  # repo root, for common/
from common import storage  # noqa: E402

AGENTS = {"agent_01_literature_review": "agent_01_literature_review.yml"}


def _authorized(handler: BaseHTTPRequestHandler) -> bool:
    expected = os.getenv("APP_PASSWORD")
    return bool(expected) and handler.headers.get("X-App-Password") == expected


def _send(handler: BaseHTTPRequestHandler, status: int, body: dict | list) -> None:
    data = json.dumps(body, default=str).encode()
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.end_headers()
    handler.wfile.write(data)


def dispatch_workflow(workflow: str, run_id: int) -> None:
    resp = httpx.post(
        f"https://api.github.com/repos/{os.environ['GH_REPO']}/actions/workflows/{workflow}/dispatches",
        headers={"Authorization": f"Bearer {os.environ['GH_DISPATCH_TOKEN']}",
                 "Accept": "application/vnd.github+json"},
        json={"ref": os.getenv("GH_REF", "main"), "inputs": {"run_id": str(run_id)}},
        timeout=30,
    )
    resp.raise_for_status()


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if not _authorized(self):
            return _send(self, 401, {"error": "unauthorized"})
        with storage.connect() as conn:
            rows = conn.execute(
                "select id, agent, params, status, created_at, finished_at from runs order by id desc limit 30"
            ).fetchall()
        _send(self, 200, [dict(zip(("id", "agent", "params", "status", "created_at", "finished_at"), r))
                          for r in rows])

    def do_POST(self):
        if not _authorized(self):
            return _send(self, 401, {"error": "unauthorized"})
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        agent = body.get("agent", "agent_01_literature_review")
        if agent not in AGENTS:
            return _send(self, 400, {"error": f"unknown agent {agent}"})
        topic = (body.get("topic") or "").strip()
        if not topic:
            return _send(self, 400, {"error": "topic is required"})
        params = {
            "topic": topic,
            "n_ideas": int(body.get("n_ideas", 5)),
            "news_window_months": int(body.get("news_window_months", 6)),
            "max_papers": int(body.get("max_papers", 30)),
        }
        run_id = storage.create_run(agent, params)
        try:
            dispatch_workflow(AGENTS[agent], run_id)
        except Exception as e:  # noqa: BLE001
            storage.finish_run(run_id, error=f"Could not start GitHub Actions: {e}")
            return _send(self, 502, {"id": run_id, "error": str(e)})
        storage.log(run_id, "Queued: waiting for GitHub Actions runner (usually ~30s)")
        _send(self, 201, {"id": run_id})
