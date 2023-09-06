#!/bin/bash

# Runs static code testing and builds files
: "${BUILD_TYPE}"
: "${RELEASE_CANDIDATE}"

set -euo pipefail

pip install --upgrade pip
pip install poetry
python3 -m venv venv
source venv/bin/activate

run_linting(){
  poetry install --sync
  echo "Check if project toml file and poetry lock file are in sync"
  poetry check
  echo "Running Black"
  black --check --diff sml_builder
  echo "Running pylint"
  pylint sml_builder
  echo "Running flake8"
  flake8 sml_builder
  echo "Running bandit"
  bandit -r sml_builder
  echo "Installing the ONS design system"
  ./get_design_system.sh
  echo "Freezing flask"
}
git config --global user.email "spp-shared-services@example.com"
git config --global user.name "spp-shared-services"
if [ "$BUILD_TYPE" -eq 0 ]; then
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
