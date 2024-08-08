#!/bin/bash

# grabs email of user that triggered contentful update for post steps

set -euo pipefail

: ${ENVIRONMENT}
: ${STATE}
: ${TOKEN}

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://github.com/ONSdigital/sml-catalogue/deployments/dev/statuses \
  -d "{'environment':'$ENVIRONMENT','state':'$STATE'}"