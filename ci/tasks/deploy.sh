#!/bin/bash

# Deploys build code to the s3 bucket

set -euo pipefail

: ${TF_VAR_environment}

workspace_name=`cat ./.git/resource/head_name| tr "[:upper:]" "[:lower:]"`
echo Workspace: ${workspace_name}

aws s3 sync build s3://sml-portal-$TF_VAR_environment-$workspace_name --delete --content-type "text/html" --exclude "*.css" --exclude "*.js"
aws s3 sync build s3://sml-portal-$TF_VAR_environment-$workspace_name --delete --exclude "*" --include "*.css" --include "*.js"
