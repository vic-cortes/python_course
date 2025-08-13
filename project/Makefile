.PHONY: run_api db_up test_db_connection db-create-migrations ruff_check message migrate

run_api:
	@echo "Starting FastAPI server..."
	uv run uvicorn src.api.server:app --reload

db_up:
	@echo "Starting database with Docker Compose..."
	docker compose -f docker-compose.yml up -d scraper-db

test_db_connection:
	@echo "Testing database connection..."
	uv run src/db/test_connection.py

ruff_check:
	@echo "Running ruff check..."
	ruff check src --fix .

db-create-migrations: message
ifndef message
	@echo "Please provide a message for the migration using 'make db-create-migrations message='<your message here>'"
else
	@echo "Creating migrations for Api"
	uv run alembic revision --autogenerate -m "${message}"
endif

migrate:
	@echo "Applying migrations to the database"
	uv run alembic upgrade head
