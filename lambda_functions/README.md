# Healthcheck Lambdas

The lambdas for the SML Portal healthcheck can be changed to do this you will need to follow some steps after making your code changes.

## Updating healthcheck.zip

Run the following commands to update the healthcheck.zip (starting in the lambda_functions/healthcheck directory)

```
    mkdir packages
    pip install --target ./packages requests
    pip install --target ./packages boto3
    pip install --target ./packages <any packages you need>
    zip -r ../healthcheck.zip .
    cd ..
    zip healthcheck.zip healthcheck.py
```

This will allow your lambda to use package dependencies.

## Updating alerter.zip

Run the following commands to update the alerter.zip (starting in the lambda_functions/alerter directory)

```
    mkdir packages
    pip install --target ./packages requests
    pip install --target ./packages <any packages you need>
    zip -r ../alerter.zip .
    cd ..
    zip alerter.zip alerter.py
```

This will allow your lambda to use package dependencies.

## Uploading your lambdas

When you deploy your stack the terraform will take the zip file and upload it to lambda.

In the event of any issues you can manually upload it via the lambda function's AWS console input.

