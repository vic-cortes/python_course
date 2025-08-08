.PHONY: run_api db_up

run_api:
	@echo "Starting FastAPI server..."
	uv run uvicorn src.api.server:app --reload

db_up:
	@echo "Starting database with Docker Compose..."
	docker compose -f docker-compose.yml up -d scraper-db

test_db_connection:
	@echo "Testing database connection..."
	uv run src/db/test_connection.py
