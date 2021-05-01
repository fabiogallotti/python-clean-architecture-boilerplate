.DEFAULT_GOAL := help
SHELL = bash


.PHONY: help
help: ## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: ## install dependencies
	poetry install --extras local
	poetry run pre-commit install

.PHONY: lint
lint: ## lint code
	poetry run isort src tests
	poetry run black src tests
	poetry run flake8 src tests

.PHONY: test-unit
test-unit: ## run unit tests
	poetry run pytest tests --rununit

.PHONY: test
test: ## run all tests
	poetry run pytest tests -vv -s -cov-report term-missing --cov=src
