 #!/bin/bash

# Runs static code testing and builds files

set -euo pipefail


pip install pipenv
python3 -m venv venv
source venv/bin/activate
pipenv sync --dev
pipenv run black --check --diff sml_builder
pipenv run pylint sml_builder
pipenv run flake8 sml_builder
pipenv run bandit -r sml_builder
echo "Installing the ONS design system"
./get_design_system.sh
echo "Freezing flask"
python freeze.py
zip -r build.zip build