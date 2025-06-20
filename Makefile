# Makefile for python-flask-server

.PHONY: help run test docker-build docker-run docker-clean

help:
	@echo "Available targets:"
	@echo "  run           Run the Flask server using Poetry"
	@echo "  test          Run tests with pytest using Poetry"
	@echo "  docker-build  Build the Docker image"
	@echo "  docker-run    Run the Docker container"
	@echo "  docker-clean  Stop and remove Docker container and image"

run:
	poetry run python -m server

test:
	poetry run pytest

docker-build:
	docker build -t flask-svr .

docker-run:
	docker run -d -p 3000:3000 --restart always --name flask-server flask-svr

docker-clean:
	docker stop flask-server && docker rm flask-server && docker rmi flask-svr
