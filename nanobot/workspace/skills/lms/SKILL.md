---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

Use LMS MCP tools to answer questions about the Learning Management System.

## Available Tools

- `lms_health` — Check if the LMS backend is healthy and report the item count. No arguments.
- `lms_labs` — List all labs available in the LMS. No arguments.
- `lms_learners` — List all learners registered in the LMS. No arguments.
- `lms_pass_rates` — Get pass rates (avg score and attempt count per task) for a lab. Requires `lab` parameter.
- `lms_timeline` — Get submission timeline (date + submission count) for a lab. Requires `lab` parameter.
- `lms_groups` — Get group performance (avg score + student count per group) for a lab. Requires `lab` parameter.
- `lms_top_learners` — Get top learners by average score for a lab. Requires `lab` and optional `limit` (default 5).
- `lms_completion_rate` — Get completion rate (passed / total) for a lab. Requires `lab` parameter.
- `lms_sync_pipeline` — Trigger the LMS sync pipeline. May take a moment. No arguments.

## Strategy

### When the user asks about scores, pass rates, completion, groups, timeline, or top learners without naming a lab:

1. Call `lms_labs` first to get the list of available labs.
2. If multiple labs are available, use the `mcp_webchat_ui_message` tool with `type: "choice"` to let the user pick a lab.
3. Use each lab's `title` field as the user-facing label and the `lab` field as the value to pass back.
4. Once the user selects a lab, call the appropriate tool with the selected lab identifier.

### When the user asks "what can you do?":

Explain your current tools and limits clearly:
- You can query the LMS backend for lab information, learner data, pass rates, timelines, group performance, and completion rates.
- You need a lab identifier for most detailed queries (scores, timeline, groups, top learners, completion rate).
- You can check backend health and trigger the sync pipeline.
- You cannot modify data — only read and report.

### Formatting responses:

- Format percentages with a `%` symbol (e.g., "85%").
- Format counts as plain numbers.
- Keep responses concise — lead with the answer, then offer additional details if relevant.
- When presenting lab lists, use the lab title as the primary identifier.

### Lab choice handling:

- If the user's request is ambiguous about which lab, always ask for clarification before proceeding.
- Use the shared `structured-ui` skill to present lab choices interactively on supported channels.
- For plain text channels, list available labs with their identifiers and ask the user to specify.

## Examples

**User:** "Show me the scores"
**You:** Call `lms_labs`, then present a choice of labs for the user to select.

**User:** "Which lab has the lowest pass rate?"
**You:** Call `lms_labs`, then call `lms_pass_rates` for each lab, compare results, and report the answer.

**User:** "Is the backend working?"
**You:** Call `lms_health` and report the status and item count.
