"""HTTP client for VictoriaLogs and VictoriaTraces APIs."""

from __future__ import annotations

import httpx

from mcp_obs.settings import ObservabilitySettings


class ObservabilityClient:
    """Client for querying VictoriaLogs and VictoriaTraces."""

    def __init__(self, settings: ObservabilitySettings) -> None:
        self.victorialogs_url = settings.victorialogs_url.rstrip("/")
        self.victoriatraces_url = settings.victoriatraces_url.rstrip("/")
        self._http_client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> ObservabilityClient:
        self._http_client = httpx.AsyncClient(timeout=30.0)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._http_client:
            await self._http_client.aclose()

    async def logs_search(
        self, query: str, limit: int = 100
    ) -> list[dict]:
        """Search logs using VictoriaLogs LogsQL query."""
        if not self._http_client:
            raise RuntimeError("Client not initialized")
        
        url = f"{self.victorialogs_url}/select/logsql/query"
        params = {"query": query, "limit": limit}
        response = await self._http_client.get(url, params=params)
        response.raise_for_status()
        # VictoriaLogs returns newline-delimited JSON
        lines = response.text.strip().split("\n")
        results = []
        for line in lines:
            if line.strip():
                import json
                try:
                    results.append(json.loads(line))
                except json.JSONDecodeError:
                    results.append({"_msg": line})
        return results

    async def logs_error_count(
        self, service: str = "Learning Management Service", time_range: str = "1h"
    ) -> dict:
        """Count errors per service over a time window."""
        if not self._http_client:
            raise RuntimeError("Client not initialized")
        
        query = f'_time:{time_range} service.name:"{service}" severity:ERROR'
        url = f"{self.victorialogs_url}/select/logsql/query"
        params = {"query": query, "limit": 1000}
        response = await self._http_client.get(url, params=params)
        response.raise_for_status()
        lines = response.text.strip().split("\n")
        count = len([l for l in lines if l.strip()])
        return {"service": service, "time_range": time_range, "error_count": count}

    async def traces_list(
        self, service: str = "Learning Management Service", limit: int = 10
    ) -> list[dict]:
        """List recent traces for a service."""
        if not self._http_client:
            raise RuntimeError("Client not initialized")
        
        url = f"{self.victoriatraces_url}/select/jaeger/api/traces"
        params = {"service": service, "limit": limit}
        response = await self._http_client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])

    async def traces_get(self, trace_id: str) -> dict:
        """Fetch a specific trace by ID."""
        if not self._http_client:
            raise RuntimeError("Client not initialized")
        
        url = f"{self.victoriatraces_url}/select/jaeger/api/traces/{trace_id}"
        response = await self._http_client.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
