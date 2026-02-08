.PHONY: lint format test check
lint:
	uv run ruff check .
format:
	uv run ruff format .
test:
	uv run pytest
check: lint test