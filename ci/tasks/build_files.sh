 #!/bin/bash

# Runs static code testing and builds files

set -euo pipefail

pip install --upgrade pip
pip install pipenv
python3 -m venv venv
source venv/bin/activate
pipenv sync --dev
pip install wrapt
pip install dill
black --check --diff sml_builder
pylint sml_builder
flake8 sml_builder
bandit -r sml_builder
echo "Installing the ONS design system"
./get_design_system.sh
echo "Freezing flask"
python freeze.py
zip -r build.zip build