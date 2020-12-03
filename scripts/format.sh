#!/bin/bash

# Based on https://github.com/commitizen-tools/commitizen/blob/master/scripts/format

export PREFIX="poetry run python -m "
if [ -d 'venv' ] ; then
    export PREFIX="venv/bin/"
fi

set -x

${PREFIX}isort .
${PREFIX}black .
