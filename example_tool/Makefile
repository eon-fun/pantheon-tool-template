.PHONY: help install test lint format check clean

export PYTHONPATH := $(shell pwd)/src
export ENV_FILE := .env

# Default target - show help
help:
	@echo "Pantheon Agent Template - Available commands:"
	@echo "  make install    - Install dependencies and setup development environment"
	@echo "  make test       - Run tests (if any exist)"
	@echo "  make lint       - Run all linters and type checkers"
	@echo "  make format     - Format code automatically"
	@echo "  make check      - Run all checks (lint + format + test)"
	@echo "  make clean      - Clean up temporary files"
	@echo "  make precommit  - Run pre-commit on all files"

# Install dependencies and setup development environment
install:
	@echo "✅ Installing dependencies..."
	poetry install --with dev --no-root


# Run tests
test:
	@if [ -d ./tests ] && ls ./tests/test*.py 1>/dev/null 2>&1; then \
		echo "✅ Running tests..."; \
		ENVIRONMENT=test pytest -v; \
	else \
		echo "⚠️  No tests to run."; \
	fi

# Run linters
lint:
	@echo "✅ Running linters..."
	poetry run ruff check .
	poetry run mypy .

# Format code
format:
	@echo "✅ Formatting code..."
	poetry run ruff format .

# Run all checks (lint + format + test)
check: lint format test

# Clean up temporary files
clean:
	@echo "✅ Cleaning up..."
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type f -name '.DS_Store' -delete

# Run pre-commit on all files
precommit:
	@echo "✅ Running pre-commit on all files..."
	poetry run pre-commit run --all-files