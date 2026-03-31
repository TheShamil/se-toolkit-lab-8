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
