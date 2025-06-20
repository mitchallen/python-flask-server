# Makefile for python-flask-server

.PHONY: help run test install docker-build docker-run docker-clean in-devcontainer

help:
	@echo "Available targets:"
	@echo "  run           Run the Flask server using Poetry"
	@echo "  test          Run tests with pytest using Poetry"
	@echo "  install        Install Python dependencies with Poetry"
	@echo "  docker-build  Build the Docker image"
	@echo "  docker-run    Run the Docker container"
	@echo "  docker-clean  Stop and remove Docker container and image"
	@echo "  in-devcontainer Check if running inside a Microsoft dev container"

run:
	poetry run python -m server

test:
	poetry run pytest

install:
	poetry install

docker-build:
	@if [ -d "/.devcontainer" ] || [ -n "$$DEVCONTAINER" ] || [ -n "$$CODESPACES" ] || [ "$$REMOTE_CONTAINERS" = "true" ] || grep -q 'devcontainer' /proc/1/cgroup 2>/dev/null; then \
		echo "docker-build must be run outside a dev container."; \
		exit 1; \
	else \
		docker build -t flask-svr .; \
	fi

docker-run:
	@if [ -d "/.devcontainer" ] || [ -n "$$DEVCONTAINER" ] || [ -n "$$CODESPACES" ] || [ "$$REMOTE_CONTAINERS" = "true" ] || grep -q 'devcontainer' /proc/1/cgroup 2>/dev/null; then \
		echo "docker-run must be run outside a dev container."; \
		exit 1; \
	else \
		docker run -d -p 3000:3000 --restart always --name flask-server flask-svr; \
	fi

docker-clean:
	@if [ -d "/.devcontainer" ] || [ -n "$$DEVCONTAINER" ] || [ -n "$$CODESPACES" ] || [ "$$REMOTE_CONTAINERS" = "true" ] || grep -q 'devcontainer' /proc/1/cgroup 2>/dev/null; then \
		echo "docker-clean must be run outside a dev container."; \
		exit 1; \
	else \
		docker stop flask-server && docker rm flask-server && docker rmi flask-svr; \
	fi

in-devcontainer:
	@if [ -d "/.devcontainer" ] || [ -n "$$DEVCONTAINER" ] || [ -n "$$CODESPACES" ] || [ "$$REMOTE_CONTAINERS" = "true" ] || grep -q 'devcontainer' /proc/1/cgroup 2>/dev/null; then \
		echo "Running inside a Microsoft dev container."; \
	else \
		echo "Not running inside a Microsoft dev container."; \
	fi
