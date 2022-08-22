#!/bin/bash

set -e

echo -n "Cleaning build directory..."
rm -rf build/*
echo "done"

echo -n "Freezing site to static files..."
pipenv run python freeze.py
echo "done"

echo -n "Uploading to S3 bucket..."
aws s3 sync build s3://sml-portal-`git branch --show-current` --delete --content-type "text/html"
echo "done"

echo -n "Invalidating CloudFront cache..."
pushd terraform
aws cloudfront create-invalidation --distribution-id `terraform output -raw cloudfront_id` --paths "/*" > /dev/null
popd
echo "done"
