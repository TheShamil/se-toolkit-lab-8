"""Settings for the observability MCP server."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ObservabilitySettings:
    """Configuration for VictoriaLogs and VictoriaTraces endpoints."""

    victorialogs_url: str
    victoriatraces_url: str


def resolve_settings() -> ObservabilitySettings:
    """Resolve settings from environment variables."""
    return ObservabilitySettings(
        victorialogs_url=os.environ.get(
            "NANOBOT_VICTORIALOGS_URL", "http://localhost:42010"
        ),
        victoriatraces_url=os.environ.get(
            "NANOBOT_VICTORIATRACES_URL", "http://localhost:42011"
        ),
    )
