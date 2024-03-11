# Healthcheck Lambdas

The lambdas for the SML Portal healthcheck require manual zipping.

This is due to their runtime version and their need for dependencies like request.

You can complete the upload using the below guide.

## Updating healthcheck.zip

Run the following commands to update the healthcheck.zip (starting in the lambda_functions/healthcheck directory)

```
    mkdir package
    pip install --target ./package requests
    pip install --target ./package boto3
    cd package
    zip -r ../healthcheck.zip .
    cd ..
    zip healthcheck.zip healthcheck.py
```

This will allow your lambda to use package dependencies.

## Updating alerter.zip

Run the following commands to update the alerter.zip (starting in the lambda_functions/alerter directory)

```
    mkdir package
    pip install --target ./package requests
    cd package
    zip -r ../alerter.zip .
    cd ..
    zip alerter.zip alerter.py
```

This will allow your lambda to use package dependencies.

## Updating your lambdas

When you deploy your stack the terraform will take the zip file and upload it to lambda.

However, if the code and zip file is updated the terraform is unable to detect the change and therefore will not deploy.

The reason we have zip files is due to the need for the dependencies like requests and boto3 combined with our older runtime version.

Otherwise we would not have a zip file but instead we would have lambda functions files which are updated via the pipeline.

The dependencies combined with the lambda runtime causes the need for zip files.

Hence you will need to upload the new zip file via the AWS Lambda console.

