"""Tool schemas, handlers, and registry for the observability MCP server."""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass

from mcp.types import Tool
from pydantic import BaseModel, Field

from mcp_obs.client import ObservabilityClient


class LogsSearchQuery(BaseModel):
    query: str = Field(
        description="LogsQL query string, e.g., '_time:1h service.name:\"Learning Management Service\" severity:ERROR'"
    )
    limit: int = Field(default=100, ge=1, le=1000, description="Max results to return")


class LogsErrorCountQuery(BaseModel):
    service: str = Field(
        default="Learning Management Service",
        description="Service name to count errors for"
    )
    time_range: str = Field(
        default="1h",
        description="Time range for the query (e.g., '10m', '1h', '24h')"
    )


class TracesListQuery(BaseModel):
    service: str = Field(
        default="Learning Management Service",
        description="Service name to list traces for"
    )
    limit: int = Field(default=10, ge=1, le=100, description="Max traces to return")


class TracesGetQuery(BaseModel):
    trace_id: str = Field(description="Trace ID to fetch")


ToolPayload = BaseModel | Sequence[BaseModel]
ToolHandler = Callable[[ObservabilityClient, BaseModel], Awaitable[ToolPayload]]


@dataclass(frozen=True, slots=True)
class ToolSpec:
    name: str
    description: str
    model: type[BaseModel]
    handler: ToolHandler

    def as_tool(self) -> Tool:
        schema = self.model.model_json_schema()
        schema.pop("$defs", None)
        schema.pop("title", None)
        return Tool(name=self.name, description=self.description, inputSchema=schema)


async def _logs_search(client: ObservabilityClient, args: BaseModel) -> ToolPayload:
    query = args  # type: ignore
    return await client.logs_search(query.query, query.limit)


async def _logs_error_count(client: ObservabilityClient, args: BaseModel) -> ToolPayload:
    query = args  # type: ignore
    return await client.logs_error_count(query.service, query.time_range)


async def _traces_list(client: ObservabilityClient, args: BaseModel) -> ToolPayload:
    query = args  # type: ignore
    return await client.traces_list(query.service, query.limit)


async def _traces_get(client: ObservabilityClient, args: BaseModel) -> ToolPayload:
    query = args  # type: ignore
    return await client.traces_get(query.trace_id)


TOOL_SPECS = (
    ToolSpec(
        "logs_search",
        "Search logs using LogsQL query. Returns matching log entries.",
        LogsSearchQuery,
        _logs_search,
    ),
    ToolSpec(
        "logs_error_count",
        "Count errors for a service over a time window.",
        LogsErrorCountQuery,
        _logs_error_count,
    ),
    ToolSpec(
        "traces_list",
        "List recent traces for a service.",
        TracesListQuery,
        _traces_list,
    ),
    ToolSpec(
        "traces_get",
        "Fetch a specific trace by ID.",
        TracesGetQuery,
        _traces_get,
    ),
)
TOOLS_BY_NAME = {spec.name: spec for spec in TOOL_SPECS}
