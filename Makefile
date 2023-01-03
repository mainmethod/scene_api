.SILENT:
.PHONY: run help

export FLASK_DEBUG := 1
export FLASK_APP := app

install: ## install dependencies with poetry
	@poetry install

run: ## run the api
	@poetry run flask run

init-db: ## initialize db
	@poetry run flask db init

make-migration: ## auto-generate migrations from schema changes
	@poetry run flask db migrate

migrate: ## run current migrations
	@poetry run flask db upgrade

migrate-down: ## migrate to previous version
	@poetry run flask db downgrade

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help