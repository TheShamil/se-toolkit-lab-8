# Adapted from backend/Dockerfile and qwen-code-api/Dockerfile
# Also see https://docs.astral.sh/uv/guides/integration/docker/

# ---
# Stage 1: build the application in the `/app` directory.
# ---

ARG REGISTRY_PREFIX_DOCKER_HUB
ARG APP_UID=1000
ARG APP_GID=1000

FROM ${REGISTRY_PREFIX_DOCKER_HUB}astral/uv:python3.14-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Omit development dependencies
ENV UV_NO_DEV=1

# Disable Python downloads - use the system interpreter across both images.
ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app

# Copy nanobot project first (from build context)
COPY . /app/nanobot

# Copy mcp and nanobot-websocket-channel projects from workspace using additional_contexts
COPY --from=workspace mcp/mcp-lms /app/mcp/mcp-lms
COPY --from=workspace nanobot-websocket-channel/nanobot-webchat /app/nanobot-websocket-channel/nanobot-webchat
COPY --from=workspace nanobot-websocket-channel/mcp-webchat /app/nanobot-websocket-channel/mcp-webchat
COPY --from=workspace nanobot-websocket-channel/nanobot-channel-protocol /app/nanobot-websocket-channel/nanobot-channel-protocol

# Fix workspace references in all pyproject.toml files
# mcp-webchat
RUN sed -i 's/nanobot-channel-protocol = { workspace = true }/nanobot-channel-protocol = { path = "..\/nanobot-channel-protocol" }/g' /app/nanobot-websocket-channel/mcp-webchat/pyproject.toml

# nanobot-webchat
RUN sed -i 's/nanobot-channel-protocol = { workspace = true }/nanobot-channel-protocol = { path = "..\/nanobot-channel-protocol" }/g' /app/nanobot-websocket-channel/nanobot-webchat/pyproject.toml

# nanobot
RUN sed -i 's/mcp-lms = { workspace = true, editable = true }/mcp-lms = { path = "..\/mcp\/mcp-lms", editable = true }/g' /app/nanobot/pyproject.toml
RUN sed -i 's/nanobot-webchat = { workspace = true, editable = true }/nanobot-webchat = { path = "..\/nanobot-websocket-channel\/nanobot-webchat", editable = true }/g' /app/nanobot/pyproject.toml
RUN sed -i 's/mcp-webchat = { workspace = true, editable = true }/mcp-webchat = { path = "..\/nanobot-websocket-channel\/mcp-webchat", editable = true }/g' /app/nanobot/pyproject.toml

# Sync the nanobot project
RUN --mount=type=cache,target=/root/.cache/uv \
    cd /app/nanobot && uv sync --no-dev

# ---
# Stage 2: use a final image without uv
# ---

ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}python:3.14.2-slim-bookworm

# Set environment variables for Python and application
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Make sure we use UTF-8 encoding
ENV LANG=C.UTF-8

# Re-declare ARGs with defaults for this stage
ARG APP_UID=1000
ARG APP_GID=1000

RUN apt-get update && apt-get install -y --no-install-recommends gosu && rm -rf /var/lib/apt/lists/*

# Setup a non-root user with configurable UID/GID
RUN groupadd --system --gid "${APP_GID}" appgroup && \
    useradd --system --gid "${APP_GID}" --uid "${APP_UID}" --create-home appuser

# Copy the application from the builder with correct ownership
COPY --from=builder --chown=appuser:appgroup /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Switch to non-root user
USER appuser

# Run the entrypoint script which resolves config and launches nanobot gateway
CMD ["python", "/app/nanobot/entrypoint.py"]
