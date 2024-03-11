#!/bin/bash

# Runs static code testing and builds files
: "${BUILD_TYPE}"
: "${RELEASE_CANDIDATE}"
: "${SIGNING_KEY}"
: "${ROLLBACK_TAG}"




set -eo pipefail

pip install --upgrade pip
pip install poetry
python3 -m venv venv
source venv/bin/activate

cd lambda_functions/healthcheck
mkdir package
pip install --target ./package requests
pip install --target ./package boto3
cd package
zip -r ../healthcheck.zip .
cd ..
zip healthcheck.zip healthcheck.py
cd ../alerter
mkdir package
pip install --target ./package requests
pip install --target ./package boto3
cd package
zip -r ../alerter.zip .
cd ..
zip alerter.zip alerter.py
cd ../..

run_linting(){
  poetry install --sync
  echo "Check if project toml file and poetry lock file are in sync"
  poetry check
  black --check --diff freeze.py sml_builder features
  echo "Running pylint"
  pylint freeze.py sml_builder features
  echo "Running flake8"
  flake8 freeze.py sml_builder features
  echo "Running bandit"
  bandit -c pyproject.toml -r .
  echo "Running isort"
  isort --check-only .
  echo "Installing the ONS design system"
  ./get_design_system.sh
  echo "Freezing flask"
}
echo "${SIGNING_KEY}" > signingkey.key
gpg --import signingkey.key
git config user.email "spp@ons.gov.uk"
git config user.name "SPP Machine User"
git config user.signingkey 79DDAC12EE2E036D
git config commit.gpgsign true
if [ ! -z "$ROLLBACK_TAG" ]; then
  git fetch
  run_linting
  python freeze.py
elif [ "$BUILD_TYPE" -eq 0 ]; then
  run_linting
  python freeze.py
elif [ "$BUILD_TYPE" -eq 1 ]; then
  git fetch
  run_linting
  semantic-release publish --prerelease
else
  git fetch
  run_linting
  semantic-release publish
fi
