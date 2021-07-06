all: lint test

lint: ## Runs black and isort
	poetry run $(MAKE) lint-poetry

lint-poetry:
	python -m isort .
	python -m black .

test: pytest type-checking formatting dependencies  ## Runs all available tests (pytest, type checking, etc.)

# TODO: LOCATION = checkdigit/ tests/
pytest:  ## Runs pytest on docstrings and the tests folder and outputs coverage.xml
	poetry run python -m pytest --cov-report=xml:coverage.xml --cov=checkdigit --doctest-modules checkdigit/ tests/

type-checking:  ## Runs mypy --strict
	poetry run python -m mypy --strict .

dependencies:  ## Verifies pyproject.toml file integrity
	poetry check
	poetry run python -m pip check

formatting:  ## Tests whether formatting meets standards
	poetry run $(MAKE) formatting-poetry

formatting-poetry:
	python -m black --check .
	python -m isort --check-only .
	python -m pylint checkdigit
	python -m pydocstyle --convention=google
