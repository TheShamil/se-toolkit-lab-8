# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

### Question 1: "What is the agentic loop?"

The agentic loop is the fundamental cycle that autonomous AI agents follow to accomplish tasks. It's the
core reasoning and action pattern that enables agents to work independently toward goals.

The Basic Loop: Perceive → Reason → Act → Observe → (repeat)

1. **Perceive**: The agent gathers information about its environment (user input, tool outputs, file contents, API responses, system state)
2. **Reason**: The agent processes information and decides what to do (analyze current state, plan next steps, evaluate options, consider constraints)
3. **Act**: The agent executes actions (call tools, make API requests, send messages, modify state)
4. **Observe**: The agent observes the results of its actions (tool outputs, success/failure signals, new information, environment changes)

Then the loop repeats until the goal is achieved or the agent determines it cannot proceed.

This loop is what distinguishes agents from simple chatbots — agents can take actions, observe results, and iterate toward goals.

### Question 2: "What labs are available in our LMS?"

The agent explored the workspace using file system tools and found:

**Lab 8 — The Agent is the Interface**

This is the current lab focusing on building an AI agent (nanobot) as a natural-language interface to the LMS system.

**Required Tasks:**
1. Task 1: Set Up the Agent — install nanobot, configure Qwen API, add MCP tools, write skill prompt
2. Task 2: Deploy and Connect a Web Client — Dockerize nanobot, add WebSocket channel + Flutter chat UI
3. Task 3: Give the Agent New Eyes — explore observability data, write log/trace MCP tools
4. Task 4: Diagnose a Failure and Make the Agent Proactive — investigate a failure, schedule in-chat health checks, fix a planted bug

**Optional Tasks:**
1. Task 1: Add a Telegram Bot Client — same agent, different interface

**Note:** The agent inspected local repo files but could not query real LMS backend data yet (no MCP tools configured at this stage).

## Task 1B — Agent with LMS tools

### Question 1: "What labs are available?"

The agent successfully called the MCP tool `mcp_lms_lms_labs` and returned real lab data from the backend:

**Available labs:**
1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. lab-08

### Question 2: "Is the LMS backend healthy?"

The agent called the `mcp_lms_lms_health` tool and responded:

**Response:** "Yes, the LMS backend is healthy. It currently has 56 items in the system."

**MCP Tools Registered:**
- `mcp_lms_lms_health` - Check backend health
- `mcp_lms_lms_labs` - List available labs
- `mcp_lms_lms_learners` - Get learners data
- `mcp_lms_lms_pass_rates` - Get pass rates
- `mcp_lms_lms_timeline` - Get timeline data
- `mcp_lms_lms_groups` - Get groups data
- `mcp_lms_lms_top_learners` - Get top learners
- `mcp_lms_lms_completion_rate` - Get completion rate
- `mcp_lms_lms_sync_pipeline` - Trigger sync pipeline

## Task 1C — Skill prompt

### Question: "Show me the scores" (without specifying a lab)

The agent followed the LMS skill strategy:

1. Recognized that "scores" requires a lab parameter
2. Called `lms_labs` first to get available labs
3. Listed all 8 available labs and asked the user to choose one

**Response:**
```
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

**Skill file created:** `nanobot/workspace/skills/lms/SKILL.md`

The skill teaches the agent:
- Which `lms_*` tools are available and when to use each one
- When a lab parameter is needed but not provided, call `lms_labs` first and ask the user to choose
- Use each lab's title as the user-facing label
- Format numeric results nicely (percentages, counts)
- Keep responses concise
- When the user asks "what can you do?", explain its current tools and limits clearly

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
