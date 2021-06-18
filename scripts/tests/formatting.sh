#!/bin/bash

# Based on https://github.com/commitizen-tools/commitizen/blob/master/scripts/test

export PREFIX="poetry run python -m "
if [ -d 'venv' ] ; then
    export PREFIX="venv/bin/"
fi

${PREFIX}black --diff --check .
${PREFIX}isort --check-only .

${PREFIX}pydocstyle --convention=google
${PREFIX}pylint checkdigit
