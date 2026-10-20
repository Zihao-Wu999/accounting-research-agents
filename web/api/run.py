"""GET /api/run?id=12&after=0 -> run status, result, and log lines with id > after."""

import json
import os
import sys
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).parents[2]))  # repo root, for common/
from common import storage  # noqa: E402


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        expected = os.getenv("APP_PASSWORD")
        if not expected or self.headers.get("X-App-Password") != expected:
            return self._send(401, {"error": "unauthorized"})
        qs = parse_qs(urlparse(self.path).query)
        run_id = int(qs["id"][0])
        after = int(qs.get("after", ["0"])[0])
        with storage.connect() as conn:
            row = conn.execute(
                "select id, agent, params, status, error, result, created_at, started_at, finished_at "
                "from runs where id=%s", (run_id,)
            ).fetchone()
            if not row:
                return self._send(404, {"error": "not found"})
            logs = conn.execute(
                "select id, ts, message from run_logs where run_id=%s and id>%s order by id", (run_id, after)
            ).fetchall()
        keys = ("id", "agent", "params", "status", "error", "result", "created_at", "started_at", "finished_at")
        run = dict(zip(keys, row))
        run["logs"] = [{"id": i, "ts": ts, "message": m} for i, ts, m in logs]
        self._send(200, run)

    def _send(self, status, body):
        data = json.dumps(body, default=str).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)
