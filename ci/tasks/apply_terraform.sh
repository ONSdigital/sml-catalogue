#!/bin/bash

# Runs a `terraform apply` on ${TERRAFORM_SOURCE}

set -euo pipefail
=
: ${TERRAFORM_SOURCE}
: ${TF_VAR_environment}
: ${AWS_DEFAULT_REGION}
: ${S3_NAME}
: ${S3_KEY}
: ${username}
: ${password}

echo "Setting netrc creds"
rm -f $HOME/.netrc
echo "default login $username password $password" >> "${HOME}/.netrc"

cd ./terraform
terraform init \
    -upgrade \
    -backend-config "bucket=${S3_NAME}" \
    -backend-config "key=${S3_KEY}" \
    -backend-config "workspace_key_prefix=workspace"

terraform plan -out=plan.tfstate
terraform apply \
    -auto-approve \
    -var="environment=${TF_VAR_environment}"
    plan.tfstate
rm plan.tfstate
echo "done"
echo "DEPLOY_URL=`terraform output -raw website_url`" >> $GITHUB_ENV
echo "cloudfront_id=`terraform output -raw cloudfront_id`" >> $GITHUB_OUTPUT
id=`terraform output -raw cloudfront_id`" >> $GITHUB_OUTPUT