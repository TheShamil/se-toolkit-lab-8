# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Command:** `uv run nanobot agent --session cli:report-1a-loop -c ./config.json -m "What is the agentic loop?"`

**Agent response:**
```
🐈 nanobot
The agentic loop is the fundamental cycle that an AI agent follows to accomplish tasks. It typically
consists of these core stages:

 1 Perceive — Gather information from the environment (user input, tool outputs, file contents, API
   responses, etc.)
 2 Reason — Process the information, plan next steps, and decide what action to take
 3 Act — Execute actions using available tools (read/write files, run commands, call APIs, send messages,
   etc.)
 4 Observe — Receive feedback from the action's result (success, error, output data)
 5 Repeat — Continue the loop until the task is complete or a stopping condition is met

 ┌─────────────┐
 │   Perceive  │
 └──────┬──────┘
        ↓
 ┌─────────────┐
 │   Reason    │
 └──────┬──────┘
        ↓
 ┌─────────────┐
 │    Act      │
 └──────┬──────┘
        ↓
 ┌─────────────┐
 │   Observe   │
 └──────┬──────┘
        ↓
    (repeat)

This loop enables agents to:

 • Handle multi-step tasks autonomously
 • Adapt based on feedback
 • Recover from errors
 • Break complex goals into manageable steps

In my case, each time you give me a request, I go through this loop: I read the context, decide which
tools to use, execute them, observe the results, and continue until I can provide you with a complete
answer.
```

---

**Command:** `uv run nanobot agent --session cli:report-1a-labs -c ./config.json -m "What labs are available in our LMS?"`

**Agent response:**
```
🐈 nanobot
Here are the available labs in the LMS:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 lab-08

Is there a specific lab you'd like to explore further? I can help you get pass rates, completion rates,
timelines, group performance, or top learners for any of these labs.
```

**Note:** This response came from the agent exploring local workspace files, not from live LMS backend data (MCP tools not yet configured).

## Task 1B — Agent with LMS tools

**Command:** `uv run nanobot agent --session cli:report-1b-labs -c ./config.json -m "What labs are available?"`

**Agent response:**
```
🐈 nanobot
Here are the available labs in the LMS:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 lab-08

Let me know if you'd like details about any specific lab (scores, pass rates, timeline, groups, top
learners, or completion rate)!
```

---

**Command:** `uv run nanobot agent --session cli:report-1b-health -c ./config.json -m "Is the LMS backend healthy?"`

**Agent response:**
```
🐈 nanobot
I'll check the LMS backend health for you.

🐈 nanobot
Yes, the LMS backend is healthy! It's currently tracking 56 items.
```

**MCP tools registered:**
- `mcp_lms_lms_health` — Check backend health and item count
- `mcp_lms_lms_labs` — List all available labs
- `mcp_lms_lms_learners` — List all learners
- `mcp_lms_lms_pass_rates` — Get pass rates for a lab
- `mcp_lms_lms_timeline` — Get submission timeline for a lab
- `mcp_lms_lms_groups` — Get group performance for a lab
- `mcp_lms_lms_top_learners` — Get top learners for a lab
- `mcp_lms_lms_completion_rate` — Get completion rate for a lab
- `mcp_lms_lms_sync_pipeline` — Trigger the sync pipeline

## Task 1C — Skill prompt

**Command:** `uv run nanobot agent --session cli:report-1c-scores -c ./config.json -m "Show me the scores"`

**Agent response:**
```
🐈 nanobot
I'll check what labs are available in the LMS so you can choose which one to see scores for.

🐈 nanobot
Here are the available labs:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 lab-08

Which lab would you like to see the scores for?
```

**Skill file:** `nanobot/workspace/skills/lms/SKILL.md`

The skill teaches the agent to:
- Call `lms_labs` first when a lab parameter is needed but not provided
- Ask the user to choose a lab before querying scores, pass rates, etc.
- Use each lab's title as the user-facing label
- Format numeric results nicely and keep responses concise

## Task 2A — Deployed agent

**Nanobot gateway startup logs:**

```
🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
✓ Channels enabled: webchat
✓ Heartbeat: every 1800s
2026-04-01 17:47:24.748 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_health' from server 'lms'
2026-04-01 17:47:24.749 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_labs' from server 'lms'
2026-04-01 17:47:24.750 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_learners' from server 'lms'
2026-04-01 17:47:24.750 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_pass_rates' from server 'lms'
2026-04-01 17:47:24.750 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_timeline' from server 'lms'
2026-04-01 17:47:24.750 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_groups' from server 'lms'
2026-04-01 17:47:24.750 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_top_learners' from server 'lms'
2026-04-01 17:47:24.750 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_completion_rate' from server 'lms'
2026-04-01 17:47:24.751 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_sync_pipeline' from server 'lms'
2026-04-01 17:47:24.751 | INFO  | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
2026-04-01 17:47:27.543 | DEBUG | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_webchat_ui_message' from server 'webchat'
2026-04-01 17:47:27.543 | INFO  | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'webchat': connected, 1 tools registered
2026-04-01 17:47:27.543 | INFO  | nanobot.agent.loop:run:280 - Agent loop started
```

**Files created/modified:**
- `nanobot/entrypoint.py` — resolves environment variables into config and launches nanobot gateway
- `nanobot/Dockerfile` — multi-stage build with uv for nanobot and MCP dependencies
- `docker-compose.yml` — nanobot service with correct volumes and environment variables
- `caddy/Caddyfile` — added `/ws/chat` route for WebSocket connections

## Task 2B — Web client

**Flutter web client accessible at:** `http://localhost:42002/flutter/`

**WebSocket endpoint test:**

```
Q1: What can you do?
I'm nanobot 🐈, your personal AI assistant. Here's what I can do in this system:

## Core Capabilities

**File & System Operations**
- Read, write, and edit files
- List directory contents
- Execute shell commands (with safety limits)
- Search the web and fetch web content

**LMS Integration**
- Query lab information, pass rates, and completion rates
- View submission timelines and group performance
- Get top learners and learner lists
- Check backend health and trigger sync pipelines

Q2: How is the backend doing?
The LMS backend is **healthy** ✅

- **Status**: Healthy
- **Item Count**: 56 items

Everything is running smoothly! Is there anything specific you'd like to check in the LMS?
```

**Files created/modified:**
- `nanobot-websocket-channel/` — Git submodule with WebSocket channel plugin and Flutter client
- `nanobot/config.json` — webchat channel enabled
- `nanobot/entrypoint.py` — webchat MCP server configuration
- `docker-compose.yml` — client-web-flutter service and caddy updates
- `caddy/Caddyfile` — `/flutter` route and `/ws/chat` WebSocket proxy

## Task 3A — Structured logging

**Happy-path log excerpt (request_started → request_completed with status 200):**

```
2026-04-01 18:02:00,559 INFO [lms_backend.main] [main.py:62] [trace_id=c5f348ea52230f344c4ac5a9637b7786 span_id=8db4bc8791aa089d resource.service.name=Learning Management Service trace_sampled=True] - request_started
2026-04-01 18:02:00,675 INFO [lms_backend.auth] [auth.py:30] [trace_id=c5f348ea52230f344c4ac5a9637b7786 span_id=8db4bc8791aa089d resource.service.name=Learning Management Service trace_sampled=True] - auth_success
2026-04-01 18:02:00,703 INFO [lms_backend.db.items] [items.py:16] [trace_id=c5f348ea52230f344c4ac5a9637b7786 span_id=8db4bc8791aa089d resource.service.name=Learning Management Service trace_sampled=True] - db_query
2026-04-01 18:02:01,034 INFO [lms_backend.main] [main.py:74] [trace_id=c5f348ea52230f344c4ac5a9637b7786 span_id=8db4bc8791aa089d resource.service.name=Learning Management Service trace_sampled=True] - request_completed
INFO:     172.18.0.10:53006 - "GET /items/ HTTP/1.1" 200 OK
```

**Error-path log excerpt (db_query with error):**

```
2026-04-01 18:24:38,760 INFO [lms_backend.db.items] [items.py:16] [trace_id=f91814ffc06110eec392a4219406f539 span_id=e668ec7eede2423c resource.service.name=Learning Management Service trace_sampled=True] - db_query
2026-04-01 18:24:38,871 ERROR [lms_backend.db.items] [items.py:23] [trace_id=f91814ffc06110eec392a4219406f539 span_id=e668ec7eede2423c resource.service.name=Learning Management Service trace_sampled=True] - db_query
2026-04-01 18:24:38,874 WARNING [lms_backend.routers.items] [items.py:23] [trace_id=f91814ffc06110eec392a4219406f539 span_id=e668ec7eede2423c resource.service.name=Learning Management Service trace_sampled=True] - items_list_failed_as_not_found
```

**VictoriaLogs query result:**

Query: `_time:1h service.name:"Learning Management Service" severity:ERROR`

Result:
```json
{
  "_msg": "db_query",
  "error": "(sqlalchemy.dialects.postgresql.asyncpg.InterfaceError) <class 'asyncpg.exceptions._base.InterfaceError'>: connection is closed",
  "event": "db_query",
  "severity": "ERROR",
  "service.name": "Learning Management Service",
  "trace_id": "f91814ffc06110eec392a4219406f539"
}
```

## Task 3B — Traces

**Healthy trace example (trace_id: `03dc4ef55039e3883a5a1990e0cb8f26`):**

Span hierarchy showing successful request flow:

| Span ID | Operation | Duration | Status |
|---------|-----------|----------|--------|
| `9475c0748f35a765` | GET /items/ | ~100ms | 200 OK |
| `d4eefbb7b987891a` | SELECT db-lab-8 | 36.6ms | Success |
| `12e4208e88846c72` | GET /items/ http send | 58μs | 200 |

**Span details (database query span):**
```json
{
  "spanID": "d4eefbb7b987891a",
  "operationName": "SELECT db-lab-8",
  "duration": 36631,
  "tags": {
    "db.system": "postgresql",
    "db.name": "db-lab-8",
    "db.statement": "SELECT item.id, item.type, item.parent_id, item.title, item.description, item.attributes, item.created_at FROM item",
    "db.user": "postgres",
    "net.peer.name": "postgres",
    "net.peer.port": "5432",
    "span.kind": "client"
  }
}
```

**Error trace example (trace_id: `f91814ffc06110eec392a4219406f539`):**

When PostgreSQL was stopped, the trace shows:

| Span ID | Operation | Duration | Status |
|---------|-----------|----------|--------|
| `e668ec7eede2423c` | SELECT db-lab-8 | Failed | Error |
| `...` | GET /items/ http send | - | 404 |

**Error span details:**
```json
{
  "spanID": "e668ec7eede2423c",
  "operationName": "SELECT db-lab-8",
  "tags": {
    "db.system": "postgresql",
    "error": true,
    "exception.message": "asyncpg.exceptions._base.InterfaceError: connection is closed"
  }
}
```

**Key differences between healthy and error traces:**
1. **Healthy trace**: Database span completes in ~37ms, HTTP response returns 200
2. **Error trace**: Database span fails with "connection is closed" error, HTTP response returns 404
3. **Span hierarchy**: Both show the same structure (request → db_query → response), but error trace has exception tags

**VictoriaTraces UI:** Accessible at `http://localhost:42002/utils/victoriatraces`
- Query by service name: "Learning Management Service"
- Filter by trace ID to inspect specific requests
- Timeline view shows span duration and parent-child relationships

## Task 3C — Observability MCP tools

**Files created:**
- `mcp/mcp-obs/src/mcp_obs/` — MCP server with observability tools
- `mcp/mcp-obs/src/mcp_obs/client.py` — HTTP client for VictoriaLogs and VictoriaTraces
- `mcp/mcp-obs/src/mcp_obs/tools.py` — Tool definitions (logs_search, logs_error_count, traces_list, traces_get)
- `mcp/mcp-obs/src/mcp_obs/server.py` — MCP server implementation
- `nanobot/workspace/skills/observability/SKILL.md` — Observability skill prompt

**MCP tools registered:**
- `mcp_obs_logs_search` — Search logs using LogsQL
- `mcp_obs_logs_error_count` — Count errors per service
- `mcp_obs_traces_list` — List recent traces
- `mcp_obs_traces_get` — Fetch specific trace by ID

---

**Agent response under normal conditions:**

**Q:** "Any LMS backend errors in the last 10 minutes?"

**A:** "No errors found in the Learning Management Service over the last 10 minutes. The backend appears to be running smoothly."

---

**Agent response under failure conditions (PostgreSQL stopped):**

**Q:** "Any LMS backend errors in the last 10 minutes?"

**A:** 
```
## Backend Status: ⚠️ Unhealthy

**Root Cause:** Database connection issue

The LMS backend is experiencing a **PostgreSQL connection failure**. The error shows:
- `asyncpg.exceptions._base.InterfaceError: connection is closed`
- The database connection to `db-lab-8` on `postgres:5432` was closed during a query
- This caused the health check endpoint to return **HTTP 404**

**Timeline:**
- Error occurred at **18:24:38 UTC** (about 15 minutes ago)
- 1 error recorded in the last hour

**Impact:**
- The backend cannot query the database
- Health checks are failing
- API requests to `/items/` are returning 404 errors

The database connection pool may need to be restarted or the PostgreSQL service should be checked.
```

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
