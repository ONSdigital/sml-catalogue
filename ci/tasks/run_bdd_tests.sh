#!/bin/bash

# Runs BDD testing on the deployed workspace

: ${GITHUB_OUTPUT}


cat GITHUB_OUTPUT
cd repo
pip install pipenv
pipenv install --dev
date=$(date '+%Y_%m_%d')
echo $date
mkdir -p ./features/test_reports/dev/$date
pipenv run behave -D host=$ENDPOINT --junit --junit-directory ./features/test_reports/dev/$date
cd ./features/test_reports/dev/$date
ls
cat TESTS-about.xml TESTS-accessibility.xml TESTS-cookies.xml TESTS-footer.xml TESTS-glossary.xml TESTS-header.xml TESTS-help_center.xml TESTS-method_summary.xml TESTS-methods.xml > test_report.xml
cat test_report.xml