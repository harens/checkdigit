#!/bin/bash

# Based on https://github.com/commitizen-tools/commitizen/blob/master/scripts/test

export PREFIX="poetry run python -m "
if [ -d 'venv' ] ; then
    export PREFIX="venv/bin/"
fi

${PREFIX}pytest --cov-report=xml:coverage.xml --cov=checkdigit --doctest-modules checkdigit/ tests/
