 #!/bin/bash

# Runs static code testing and builds files

set -euo pipefail

apt-get -y update && apt-get install -y zip
pip install --upgrade pip
pip install pipenv
python3 -m venv venv
source venv/bin/activate
pipenv sync --dev
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
python freeze.py
zip -r build.zip build