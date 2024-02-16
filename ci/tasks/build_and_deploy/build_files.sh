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

# Read and parse the feature.json file
FEATURES = $(cat config/feature.json | jq -r 'features[] | "\(.name)=\(.enabled)"')
for feature in $FEATURES; do
  echo "Feature sml_builder found"
done


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
