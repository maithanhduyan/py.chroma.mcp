# Stage 1: Base with minimal dependencies
FROM python:3.12-slim AS base

# Install only essential system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Stage 2: Builder with build dependencies
FROM base AS builder

# Install build dependencies in builder stage only
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv (faster than pip)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Create virtual environment
RUN uv venv /opt/venv --python 3.12
ENV PATH="/opt/venv/bin:$PATH"

# Copy only dependency files first (better caching)
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN uv pip install -e . --no-cache-dir

# Stage 3: Development (for devcontainer)
FROM base AS development

# Create non-root user
RUN useradd -ms /bin/bash vscode

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Switch to non-root user
USER vscode
WORKDIR /workspace

# Git configuration
RUN git config --global user.name "Mai Thành Duy An" && \
    git config --global user.email "tiachop0102@gmail.com"

# Expose port
EXPOSE 3000

# Development command
CMD ["bash"]

# Stage 4: Production (minimal size)
FROM base AS production

# Create non-root user
RUN useradd -ms /bin/bash appuser

# Copy only the virtual environment (no build tools)
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy source code
COPY --chown=appuser:appuser src/ /app/src/
COPY --chown=appuser:appuser pyproject.toml /app/

# Switch to non-root user and working directory
USER appuser
WORKDIR /app

# Set environment variables
ENV PYTHONPATH="/app"
ENV ENVIRONMENT="production"
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Production command
CMD ["python", "-m", "src.server"]
