#!/bin/bash

# Runs static code testing and builds files
: "${IS_MAIN}"

set -euo pipefail

pip install --upgrade pip
pip install poetry
python3 -m venv venv
source venv/bin/activate
poetry install
pip install wrapt
pip install dill
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
if [ "$IS_MAIN" -eq 0 ]; then
  python freeze.py
else
  semantic-release publish
fi
