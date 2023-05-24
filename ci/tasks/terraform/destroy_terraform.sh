#!/bin/sh

set -eu

export HOME=$(pwd)

echo "machine github.com login ${CONCOURSE_ACCESS_TOKEN} password x-oauth-basic" > ~/.netrc
chmod 600 ~/.netrc

cd repo

# --------------------------

export TF_VAR_head_sha=$(cat .git/resource/head_sha)
export TF_VAR_head_sha_short=$(cat .git/resource/head_sha_short)
#
#export TF_VAR_ses_cognito_email_arn="arn:aws:ses:eu-west-1:111111111111:identity/destroy@fake.ons.gov.uk"
#export TF_VAR_ses_cognito_email_address="destroy@fake.ons.gov.uk"

# --------------------------

cd terraform

terraform init \
-upgrade \
-backend-config "bucket=${S3_NAME}" \
-backend-config "key=${S3_KEY}" \
-backend-config "workspace_key_prefix=${WORKSPACE_KEY_INFIX}"

# --------------------------

export TF_WORKSPACE=$(cat ~/repo/.workspace)
echo "Workspace: ${TF_WORKSPACE}"

# --------------------------

terraform destroy -auto-approve

export TF_WORKSPACE=""
terraform workspace delete "$(cat ../../.workspace)" || ( echo "ERROR: Could not delete workspace!" && exit 1)