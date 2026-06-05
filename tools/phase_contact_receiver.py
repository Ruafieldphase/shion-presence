#!/usr/bin/env python3
"""Serve shion-presence locally and record coarse phase-contact events.

The receiver records boundary deltas, not visitor identity. It intentionally
does not store IP addresses, raw user-agent strings, cookies, or query strings.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


AI_CRAWLER_RE = re.compile(
    r"(bot|crawler|spider|gptbot|chatgpt|claude|perplexity|google-extended|ccbot|oai-search|bingpreview)",
    re.IGNORECASE,
)
TEXT_PATH_RE = re.compile(r"^/(AI_READ_FIRST\.md|llms\.txt|PROMPT_FOR_USER_AI\.md|README\.md)$")


@dataclass
class ReceiverEvent:
    timestamp: str
    schema: str
    event_kind: str
    contact_source: str
    contact_class: str
    path: str
    referrer_class: str
    viewport_class: str
    boundary_pressure: float
    phase_effect: str
    field_delta: dict[str, Any]
    privacy_contract: dict[str, bool]
    note: str


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def classify_user_agent(value: str) -> str:
    if not value:
        return "unknown_contact"
    return "ai_crawler_candidate" if AI_CRAWLER_RE.search(value) else "browser_contact_candidate"


def classify_referrer(value: str) -> str:
    if not value:
        return "none"
    parsed = urlparse(value)
    if parsed.hostname in {"127.0.0.1", "localhost"}:
        return "local"
    if parsed.hostname:
        return "external"
    return "unknown"


def sanitize_path(raw_path: str) -> str:
    parsed = urlparse(raw_path or "/")
    path = parsed.path or "/"
    if path == "":
        return "/"
    return path[:160]


def should_record_get(path: str) -> bool:
    if path in {"/", "/index.html", "/robots.txt", "/sitemap.xml"}:
        return True
    if TEXT_PATH_RE.match(path):
        return True
    if path.startswith("/public/") and path.endswith(".json"):
        return True
    if path.startswith("/docs/") and path.endswith(".md"):
        return True
    return False


def pressure_for(contact_class: str, referrer_class: str, source: str) -> float:
    pressure = 0.18
    if contact_class == "ai_crawler_candidate":
        pressure += 0.12
    if referrer_class == "external":
        pressure += 0.10
    if source == "client_beacon":
        pressure += 0.06
    return round(clamp01(pressure), 4)


def phase_effect_for(boundary_pressure: float, event_kind: str) -> str:
    if event_kind == "music_phase_input":
        return "music_wave_delta"
    if boundary_pressure >= 0.34:
        return "reinforcement_pressure"
    if boundary_pressure <= 0.20:
        return "soft_contact"
    return "boundary_damping"


def privacy_contract() -> dict[str, bool]:
    return {
        "identity_not_collected": True,
        "ip_not_stored": True,
        "raw_user_agent_not_stored": True,
        "full_referrer_not_stored": True,
        "cookies_not_set": True,
        "persistent_identifier_not_created": True,
    }


def coerce_payload(raw: bytes) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return {"parse_error": "invalid_json"}
    return data if isinstance(data, dict) else {"parse_error": "non_object_payload"}


class PhaseContactStore:
    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = self.output_dir / "contact_phase_receiver_events.jsonl"
        self.latest_path = self.output_dir / "contact_phase_receiver_latest.json"

    def append(self, event: ReceiverEvent) -> None:
        payload = asdict(event)
        with self.log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        self.latest_path.write_text(
            json.dumps(self.summary(latest=payload), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def read_recent(self, limit: int = 40) -> list[dict[str, Any]]:
        if not self.log_path.exists():
            return []
        lines = self.log_path.read_text(encoding="utf-8").splitlines()[-limit:]
        events = []
        for line in lines:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return events

    def summary(self, latest: dict[str, Any] | None = None) -> dict[str, Any]:
        events = self.read_recent()
        if latest and (not events or events[-1].get("timestamp") != latest.get("timestamp")):
            events.append(latest)
        by_kind = Counter(str(event.get("event_kind", "unknown")) for event in events)
        by_contact = Counter(str(event.get("contact_class", "unknown")) for event in events)
        return {
            "schema": "shion_presence_contact_phase_receiver_latest_v1",
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "event_count_recent_window": len(events),
            "counts": {
                "by_event_kind": dict(sorted(by_kind.items())),
                "by_contact_class": dict(sorted(by_contact.items())),
            },
            "latest_event": latest or (events[-1] if events else None),
            "recent_events": events[-8:],
            "readback": "coarse boundary deltas only; identity remains outside the field",
        }


def build_event(
    *,
    headers: Any,
    raw_path: str,
    payload: dict[str, Any] | None = None,
    event_kind: str = "http_request_contact",
    contact_source: str = "server_request",
) -> ReceiverEvent:
    payload = payload or {}
    path = sanitize_path(str(payload.get("path") or raw_path))
    contact_class = str(payload.get("contact_class") or classify_user_agent(headers.get("User-Agent", "")))
    referrer_class = str(payload.get("referrer_class") or classify_referrer(headers.get("Referer", "")))
    viewport_class = str(payload.get("viewport_class") or "unknown")
    boundary_pressure = payload.get("boundary_pressure")
    if not isinstance(boundary_pressure, (int, float)):
        boundary_pressure = pressure_for(contact_class, referrer_class, contact_source)
    boundary_pressure = round(clamp01(float(boundary_pressure)), 4)
    raw_phase_effect = payload.get("phase_effect")
    phase_effect = raw_phase_effect if isinstance(raw_phase_effect, str) else phase_effect_for(boundary_pressure, event_kind)

    field_delta = {
        "path": path,
        "boundary_pressure": boundary_pressure,
        "phase_effect": phase_effect,
        "phase_effect_detail": raw_phase_effect if isinstance(raw_phase_effect, dict) else {},
        "music_phase_seed": payload.get("music_phase_seed", ""),
        "event_family": payload.get("event_family", ""),
        "delta_hint": payload.get("delta_hint", ""),
    }
    return ReceiverEvent(
        timestamp=datetime.now(timezone.utc).isoformat(),
        schema="shion_presence_contact_phase_event_v1",
        event_kind=event_kind,
        contact_source=contact_source,
        contact_class=contact_class,
        path=path,
        referrer_class=referrer_class,
        viewport_class=viewport_class,
        boundary_pressure=boundary_pressure,
        phase_effect=phase_effect,
        field_delta=field_delta,
        privacy_contract=privacy_contract(),
        note=str(payload.get("note") or ""),
    )


def make_handler(root: Path, store: PhaseContactStore):
    class Handler(SimpleHTTPRequestHandler):
        server_version = "ShionPhaseContactReceiver/1.0"

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, directory=str(root), **kwargs)

        def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
            return

        def end_headers(self) -> None:
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            super().end_headers()

        def do_OPTIONS(self) -> None:  # noqa: N802
            self.send_response(HTTPStatus.NO_CONTENT)
            self.end_headers()

        def do_GET(self) -> None:  # noqa: N802
            path = sanitize_path(self.path)
            if path == "/phase-contact/latest":
                self.respond_json(store.summary())
                return
            if should_record_get(path):
                event = build_event(headers=self.headers, raw_path=self.path)
                store.append(event)
            super().do_GET()

        def do_POST(self) -> None:  # noqa: N802
            path = sanitize_path(self.path)
            length = int(self.headers.get("Content-Length", "0") or 0)
            payload = coerce_payload(self.rfile.read(min(length, 16384)))
            if path in {"/phase-contact", "/phase-event", "/phase-music"}:
                if path == "/phase-music":
                    event_kind = "music_phase_input"
                else:
                    event_kind = str(payload.get("event_kind") or "browser_boundary_contact")
                event = build_event(
                    headers=self.headers,
                    raw_path=self.path,
                    payload=payload,
                    event_kind=event_kind,
                    contact_source="client_beacon",
                )
                store.append(event)
                self.respond_json({"ok": True, "event": asdict(event)})
                return
            self.send_error(HTTPStatus.NOT_FOUND, "unknown receiver endpoint")

        def respond_json(self, data: dict[str, Any]) -> None:
            body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    return Handler


def default_output_dir(root: Path) -> Path:
    agi_sena = root.parent / "agi" / "outputs" / "sena"
    if agi_sena.exists():
        return agi_sena
    return root / "outputs"


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Serve shion-presence and record coarse contact phase events.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=58231)
    parser.add_argument("--root", default=str(root))
    parser.add_argument("--output-dir", default="", help="Defaults to ../agi/outputs/sena when available.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    output_dir = Path(args.output_dir).resolve() if args.output_dir else default_output_dir(root)
    store = PhaseContactStore(output_dir)
    server = ThreadingHTTPServer((args.host, args.port), make_handler(root, store))
    print(f"serving={root}")
    print(f"receiver=http://{args.host}:{args.port}/phase-contact")
    print(f"latest=http://{args.host}:{args.port}/phase-contact/latest")
    print(f"output={output_dir}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
