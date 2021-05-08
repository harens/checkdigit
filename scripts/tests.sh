#!/bin/bash

# Based on https://github.com/commitizen-tools/commitizen/blob/master/scripts/test

export PREFIX="poetry run python -m "
if [ -d 'venv' ] ; then
    export PREFIX="venv/bin/"
fi

${PREFIX}coverage run tests.py
poetry check
${PREFIX}black --check .
${PREFIX}isort --check-only .
${PREFIX}mypy --strict .
${PREFIX}pylint checkdigit
${PREFIX}pydocstyle --convention=google