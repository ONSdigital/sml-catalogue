#!/bin/sh

if [ "$1" == "" ]; then
  echo "Usage: terraform.sh apply|destroy"
  exit 1
fi

cd terraform
terraform init
export TF_WORKSPACE=`git branch --show-current`
if [ "$1" == "destroy" ]; then
  terraform destroy
else
  terraform apply
fi