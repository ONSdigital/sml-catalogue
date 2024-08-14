#!/bin/bash

# Runs static code testing and builds files
: "${BUILD_TYPE}"
: "${RELEASE_CANDIDATE}"
: "${SIGNING_KEY}"
: "${ROLLBACK_TAG}"
: "${SPACE_ID}"
: "${CDA_KEY}"


set -eo pipefail

pip install --upgrade pip
pip install poetry
python3 -m venv venv
source venv/bin/activate

run_linting(){
  poetry install --sync
  echo "Check if project toml file and poetry lock file are in sync"
  poetry check
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
