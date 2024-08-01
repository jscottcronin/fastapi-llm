# Variables
DOCKER_COMPOSE=docker-compose
POETRY=poetry

# Targets
.PHONY: all run-local run-docker build up down prune logs shell setup sync update lint mypy clean help

all: setup prune build up

run-local: ## Run the application locally
	$(POETRY) run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

run-docker: ## Run the application locally
	make prune
	make build
	make up

# Docker Compose commands
build: ## Build the Docker containers
	$(DOCKER_COMPOSE) build

up: ## Start the Docker containers in detached mode
	$(DOCKER_COMPOSE) up

down: ## Stop and remove the Docker containers
	$(DOCKER_COMPOSE) down

prune: ## Prune unused Docker containers, networks, images, and optionally volumes
	docker container prune -f
	docker image prune -f

logs: ## Follow the logs of the Docker containers
	$(DOCKER_COMPOSE) logs -f

shell: ## Open a shell in the specified Docker service container
	$(DOCKER_COMPOSE) exec <service_name> /bin/sh

# Python environment setup with Poetry
setup: ## Install dependencies using Poetry
	poetry config virtualenvs.in-project true
	$(POETRY) install

# Sync python environment with Poetry
sync: ## Sync dependencies between lock file and pyproject.toml using Poetry
	$(POETRY) lock --no-update
	$(POETRY) install

# Update python libraries to latest versions
update: ## Update dependencies using Poetry
	$(POETRY) update

# Linting and type-checking
lint: ## Run flake8 for linting
	$(POETRY) run ruff check --no-fix
	$(POETRY) run mypy .

test: ## Run tests
	$(POETRY) run pytest

# Clean up
clean: ## Clean up Docker containers, volumes, images, and caches
	$(DOCKER_COMPOSE) down -v --rmi all --remove-orphans
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf **/__pycache__
	rm -rf .tox
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

help: ## Display this help message
	@echo "Usage: make [target]"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"; printf "\033[1m%-15s\033[0m %s\n", "Target", " Description"} /^[a-zA-Z_-]+:.*##/ { printf "\033[1m%-15s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
