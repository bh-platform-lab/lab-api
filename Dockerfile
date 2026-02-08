FROM python:3.14-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.10.0 /uv /uvx /bin/

COPY pyproject.toml uv.lock* /app/
RUN uv sync --frozen || uv sync

COPY app /app/app

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
