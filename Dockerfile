FROM python:3.14-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.10.0 /uv /uvx /bin/

WORKDIR /lab-api

RUN groupadd -g "10001" lab-api; \
    useradd -u "10001" -g "10001" -m -s /usr/sbin/nologin lab-api; \
    chown -R lab-api:lab-api /lab-api

USER lab-api

COPY --chown=lab-api:lab-api pyproject.toml uv.lock* .
RUN uv sync --frozen || uv sync

COPY --chown=lab-api:lab-api app ./app

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
