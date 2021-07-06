.PHONY: docs  # The docs directory already exists
all: format test

CMD:=poetry run python -m

format: ## Runs black and isort
	$(CMD) isort .
	$(CMD) black .

test: pytest type-checking lint dependencies  ## Runs all available tests (pytest, type checking, etc.)

# TODO: LOCATION = checkdigit/ tests/
pytest:  ## Runs pytest on docstrings and the tests folder and outputs coverage.xml
	$(CMD) pytest --cov-report=xml:coverage.xml --cov=checkdigit --doctest-modules checkdigit/ tests/

type-checking:  ## Runs mypy --strict
	$(CMD) mypy --strict .

dependencies:  ## Verifies pyproject.toml file integrity
	poetry check
	$(CMD) pip check

lint:  ## Tests whether formatting meets standards
	$(CMD) black --check .
	$(CMD) isort --check-only .
	$(CMD) pylint checkdigit
	$(CMD) pydocstyle --convention=google

docs:  ## Continuously build the documentation using sphinx-autobuild
	poetry run sphinx-autobuild docs/source docs/_build/html
