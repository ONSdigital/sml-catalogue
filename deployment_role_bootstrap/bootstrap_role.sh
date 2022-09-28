#!/bin/sh

if [ "$1" == "" ]; then
  echo "Usage: bootstrap_role.sh apply|destroy prod|preprod|dev"
  exit 1
fi

if [ "$2" == "prod" ]; then
  bucket="statistical-methods-library-tf-state-prod"
elif [ "$2" == "preprod" ]; then
  bucket="statistical-methods-library-tf-state-preprod"
elif [ "$2" == "dev" ]; then
  bucket="statistical-methods-library-tf-state"
else
  echo "Usage: bootstrap_role.sh apply|destroy prod|preprod|dev"
  exit 1
fi

terraform init \
  -reconfigure \
  -upgrade \
  -backend-config "bucket=$bucket" \
  -backend-config "key=sml-portal.tfstate" \
  -backend-config "workspace_key_prefix=account"

export TF_WORKSPACE="account"
if [ "$1" == "destroy" ]; then
  terraform destroy
else
  terraform apply \
    -auto-approve \
    -var="environment=$2"
fi
