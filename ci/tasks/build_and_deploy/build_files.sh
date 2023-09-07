#!/bin/bash

# Runs static code testing and builds files
: "${BUILD_TYPE}"
: "${RELEASE_CANDIDATE}"
: "${SIGNING_KEY}"

set -euo pipefail

pip install --upgrade pip
pip install poetry
python3 -m venv venv
source venv/bin/activate

run_linting(){
  poetry install
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
echo "${SIGNING_KEY}" > signingkey.key
gpg --import signingkey.key
git config --global user.email "spp@ons.gov.uk"
git config --global user.name "SPP Machine User"
git config --global user.signingkey "79DDAC12EE2E036D"
git config --global commit.gpgsign true
if [ "$BUILD_TYPE" -eq 0 ]; then
  run_linting
  python freeze.py
  echo "test" > test.txt
  git add test.txt
  git commit -m "Test"
  git push origin fix-semantic-release-issues
elif [ "$BUILD_TYPE" -eq 1 ]; then
  git fetch
  run_linting
  semantic-release publish --prerelease
else
  git fetch
  run_linting
  semantic-release publish
fi
