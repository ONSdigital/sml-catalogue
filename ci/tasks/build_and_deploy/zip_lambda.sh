# This file is to take the lambda function and make it available to be deployed into AWS via terraform and concourse.
# To to this we have to add dependencies and zip the lambda using the following commands.
pip install --upgrade pip
pip install poetry
python3 -m venv tempenv
source tempenv/bin/activate

poetry install --sync
echo "Zip Lambdas"
cd lambda_functions/healthcheck
mkdir package
pip install --target ./package requests
pip install --target ./package boto3
cd package
zip -r ../healthcheck.zip .
cd ..
zip healthcheck.zip healthcheck.py
rm -rf package
cd ../alerter
mkdir package
pip install --target ./package requests
pip install --target ./package boto3
cd package
zip -r ../alerter.zip .
cd ..
zip alerter.zip alerter.py
rm -rf package
cd ../..
rm -rf tempenv
