#!/bin/bash

# grabs email of user that triggered contentful update for post steps

set -euo pipefail

: ${ENVIRONMENT}
: ${STATE}
: ${TOKEN}

id=$(curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/ONSdigital/sml-catalogue/deployments \
  -d "{'ref':'spp11763','environment':'$ENVIRONMENT'}" | jq -r '.id')

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/ONSdigital/sml-catalogue/deployments/"$id"/statuses \
  -d "{'environment':'$ENVIRONMENT','state':'$STATE'}"