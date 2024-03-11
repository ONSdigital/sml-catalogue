pip install --upgrade pip
pip install poetry
python3 -m venv venv
source venv/bin/activate

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
rm -f package
cd ../alerter
mkdir package
pip install --target ./package requests
pip install --target ./package boto3
cd package
zip -r ../alerter.zip .
cd ..
zip alerter.zip alerter.py
rm -f package
cd ../..
