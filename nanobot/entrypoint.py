#!/usr/bin/env python3
"""Resolve environment variables into nanobot config and launch the gateway."""

import json
import os
import sys
import tempfile
from pathlib import Path


def main():
    # Paths
    base_dir = Path(__file__).parent
    config_path = base_dir / "config.json"
    # Write resolved config to temp directory to avoid permission issues
    resolved_path = Path(tempfile.gettempdir()) / "nanobot.config.resolved.json"
    workspace_dir = base_dir / "workspace"

    # Read base config
    with open(config_path) as f:
        config = json.load(f)

    # Override agent defaults from env vars
    if os.environ.get("LLM_API_MODEL"):
        config["agents"]["defaults"]["model"] = os.environ["LLM_API_MODEL"]

    # Override provider config from env vars
    if os.environ.get("LLM_API_KEY"):
        config["providers"]["custom"]["apiKey"] = os.environ["LLM_API_KEY"]
    if os.environ.get("LLM_API_BASE_URL"):
        config["providers"]["custom"]["apiBase"] = os.environ["LLM_API_BASE_URL"]

    # Override gateway config from env vars
    if os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS"):
        config["gateway"]["host"] = os.environ["NANOBOT_GATEWAY_CONTAINER_ADDRESS"]
    if os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT"):
        config["gateway"]["port"] = int(os.environ["NANOBOT_GATEWAY_CONTAINER_PORT"])

    # Configure webchat channel from env vars
    if os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS"):
        if "webchat" not in config["channels"]:
            config["channels"]["webchat"] = {}
        config["channels"]["webchat"]["enabled"] = True
        config["channels"]["webchat"]["host"] = os.environ["NANOBOT_WEBCHAT_CONTAINER_ADDRESS"]
    if os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT"):
        if "webchat" not in config["channels"]:
            config["channels"]["webchat"] = {}
        config["channels"]["webchat"]["enabled"] = True
        config["channels"]["webchat"]["port"] = int(os.environ["NANOBOT_WEBCHAT_CONTAINER_PORT"])

    # Configure MCP servers from env vars
    if "mcpServers" not in config["tools"]:
        config["tools"]["mcpServers"] = {}

    # Use the venv python for MCP servers
    venv_python = "/app/nanobot/.venv/bin/python"

    # LMS MCP server
    if os.environ.get("NANOBOT_LMS_BACKEND_URL") or os.environ.get("NANOBOT_LMS_API_KEY"):
        if "lms" not in config["tools"]["mcpServers"]:
            config["tools"]["mcpServers"]["lms"] = {
                "command": venv_python,
                "args": ["-m", "mcp_lms"],
                "env": {}
            }
        else:
            # Update command to use venv python
            config["tools"]["mcpServers"]["lms"]["command"] = venv_python
        if "env" not in config["tools"]["mcpServers"]["lms"]:
            config["tools"]["mcpServers"]["lms"]["env"] = {}
        if os.environ.get("NANOBOT_LMS_BACKEND_URL"):
            config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_BACKEND_URL"] = os.environ["NANOBOT_LMS_BACKEND_URL"]
        if os.environ.get("NANOBOT_LMS_API_KEY"):
            config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_API_KEY"] = os.environ["NANOBOT_LMS_API_KEY"]

    # Webchat MCP server
    if os.environ.get("NANOBOT_VICTORIALOGS_URL") or os.environ.get("NANOBOT_VICTORIATRACES_URL"):
        if "webchat" not in config["tools"]["mcpServers"]:
            config["tools"]["mcpServers"]["webchat"] = {
                "command": venv_python,
                "args": ["-m", "mcp_webchat"],
                "env": {}
            }
        else:
            # Update command to use venv python
            config["tools"]["mcpServers"]["webchat"]["command"] = venv_python
        if "env" not in config["tools"]["mcpServers"]["webchat"]:
            config["tools"]["mcpServers"]["webchat"]["env"] = {}
        if os.environ.get("NANOBOT_VICTORIALOGS_URL"):
            config["tools"]["mcpServers"]["webchat"]["env"]["NANOBOT_VICTORIALOGS_URL"] = os.environ["NANOBOT_VICTORIALOGS_URL"]
        if os.environ.get("NANOBOT_VICTORIATRACES_URL"):
            config["tools"]["mcpServers"]["webchat"]["env"]["NANOBOT_VICTORIATRACES_URL"] = os.environ["NANOBOT_VICTORIATRACES_URL"]

    # Write resolved config
    with open(resolved_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"Using config: {resolved_path}", file=sys.stderr)

    # Launch nanobot gateway using the full path from venv
    nanobot_path = "/app/nanobot/.venv/bin/nanobot"
    os.execvp(nanobot_path, [nanobot_path, "gateway", "--config", str(resolved_path), "--workspace", str(workspace_dir)])


if __name__ == "__main__":
    main()
