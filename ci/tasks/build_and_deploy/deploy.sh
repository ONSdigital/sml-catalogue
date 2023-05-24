#!/bin/bash

# Deploys build code to the s3 bucket

set -euo pipefail

: ${TF_VAR_environment}
: ${AWS_SERVICE_ROLE}

workspace_name=`cat ./.git/resource/head_name| tr "[:upper:]" "[:lower:]"`
echo Workspace: ${workspace_name}
aws sts assume-role --output text \
  --role-arn "${AWS_SERVICE_ROLE}" \
  --role-session-name concourse-pipeline-run  \
  --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" \
  | awk -F '\t' '{print $1 > ("AccessKeyId")}{print $2 > ("SecretAccessKey")}{print $3 > ("SessionToken")}'
export AWS_ACCESS_KEY_ID="$(cat AccessKeyId)"
export AWS_SECRET_ACCESS_KEY="$(cat SecretAccessKey)"
export AWS_SESSION_TOKEN="$(cat SessionToken)"
aws s3 sync ./build s3://sml-portal-$TF_VAR_environment-$workspace_name --delete --content-type "text/html" --exclude "*.css" --exclude "*.js"
aws s3 sync ./build s3://sml-portal-$TF_VAR_environment-$workspace_name --delete --exclude "*" --include "*.css" --include "*.js"
