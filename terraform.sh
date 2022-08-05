#!/bin/sh

cd terraform
terraform init
export TF_WORKSPACE=`git branch --show-current`
terraform apply