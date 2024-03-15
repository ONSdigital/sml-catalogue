#!/bin/bash

# Runs a `terraform apply` on ${TERRAFORM_SOURCE}

set -euo pipefail

: ${TERRAFORM_SOURCE}
: ${TF_VAR_environment}
: ${TF_VAR_slack_alert_token}
: ${TF_VAR_deployment_role}
: ${WORKSPACE_KEY_INFIX}
: ${AWS_DEFAULT_REGION}
: ${S3_NAME}
: ${S3_KEY}
: ${username}
: ${password}

echo "Setting netrc creds"
rm -f $HOME/.netrc
echo "default login $username password $password" >> "${HOME}/.netrc"
echo "starting terraform init"
cd ./terraform
terraform init \
    -upgrade \
    -backend-config "bucket=${S3_NAME}" \
    -backend-config "key=${S3_KEY}" \
    -backend-config "workspace_key_prefix=${WORKSPACE_KEY_INFIX}" \
    -backend-config "role_arn=${TF_VAR_deployment_role}"
echo "starting terraform plan"
if [ -z ${TF_WORKSPACE+x} ]; then export TF_WORKSPACE=`cat ../.workspace | tr "[:upper:]" "[:lower:]"`; else echo "Workspace already set"; fi
echo Workspace: ${TF_WORKSPACE}
terraform plan -out=plan.tfstate
echo "starting terraform apply"
terraform apply \
    -auto-approve \
    -var="environment=${TF_VAR_environment}" \
    -var="slack_alert_token=${TF_VAR_slack_alert_token}" \
    -var="deployment_role=${TF_VAR_deployment_role}" \
    -var="aws_account_id=${AWS_ACCOUNT_ID}"
rm plan.tfstate
echo "done"
echo "DEPLOY_URL=`terraform output -raw website_url`" > ../../GITHUB_OUTPUT/output.txt
echo "cloudfront_id=`terraform output -raw cloudfront_id`" >> ../../GITHUB_OUTPUT/output.txt
