#!/bin/sh

set -eu


if [ -f .git/resource/metadata.json ]; then

  #
  # This is triggered if the metadata is being generated from a PR (type: pull-request)
  #

  cd .git/resource/

  cut -c1-7 < head_sha > head_sha_short

  PR="$(cat pr)"
  HEAD_NAME="$(cat head_name)"


  cd ../..
  printf "%s\n" "Deriving workspace name from PR name"
  printf "%s" "${PR}-${HEAD_NAME}" | sed 's/[^a-zA-Z0-9]/-/g' | tr '[:upper:]' '[:lower:]' | sed 's/cognito/cogneeto/g'| cut -c1-13 | sed 's/-$//' > .workspace

else

  #
  # This is triggered if the metadata is being generated without a PR (type: git)
  #

  apk add --no-progress git

  mkdir -p .git/resource/

  git rev-parse HEAD > .git/resource/head_sha
  cut -c1-7 < .git/resource/head_sha > .git/resource/head_sha_short

  printf "%s\n" "Setting workspace name to 'main'"
  printf "%s" "main" >.workspace

fi

printf "\nContents of head_sha :  %s\n\n " "$(cat .git/resource/head_sha)"
printf "\nContents of head_sha_short :  %s\n\n " "$(cat .git/resource/head_sha_short)"
printf "\nContents of .workspace:  %s\n\n " "$(cat .workspace)"
