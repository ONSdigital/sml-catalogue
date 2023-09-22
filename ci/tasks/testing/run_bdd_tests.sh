#!/bin/bash
set -euo

# Runs BDD testing on the deployed workspace

: ${URL}

pip install poetry
poetry install --sync
echo "Check if project toml file and poetry lock file are in sync"
poetry check
date=$(date '+%Y_%m_%d')
echo $date
mkdir -p ./features/test_reports/dev/$date
poetry run behave -D host=$URL --junit --junit-directory ./features/test_reports/dev/$date
cd ./features/test_reports/dev/$date
ls
cat TESTS-about.xml TESTS-accessibility.xml TESTS-cookies.xml TESTS-footer.xml TESTS-glossary.xml TESTS-header.xml TESTS-help_center.xml TESTS-method_summary.xml TESTS-methods.xml > test_report.xml
cat test_report.xml