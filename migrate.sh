
#!/bin/bash
source_environment=$1
target_environment=$2
if  [ -z "$source_environment" ] || [ -z "$target_environment" ]; then
  echo "Usage: ./migrate.sh <source_environment> <target_environment>"
  echo " -- Example: ./migrate.sh dev preprod"
  echo " -- Environment must be one of: dev, preprod, prod"
  exit 1
fi


# migrate content types first
contentful merge export --te $target_environment --se $source_environment --management-token $CLI_KEY --output-file ./contentful-data/migrations/${source_environment}-export.js
contentful space migration --space-id $SPACE_ID --management-token $CLI_KEY --environment-id $target_environment ./contentful-data/migrations/${source_environment}-export.js

# then merge entries
contentful space export --management-token $CLI_KEY --export-dir ./contentful-data/content-exports --environment-id $source_environment --content-file ${source_environment}-export.json
contentful space import --management-token $CLI_KEY --environment-id $target_environment --content-file ./contentful-data/content-exports/${source_environment}-export.json

# log the migration
echo "Migrated content from $source_environment to $target_environment"

timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
echo "${timestamp}: Migrated content from $source_environment to $target_environment" > ./contentful-data/migration-log.txt
#  TODO: create a backup to allow rollbacks
#  TODO: restructure to account for content deletion
#  TODO: add a log to track migrations
#  TODO: check that the input env is one of dev, preprod, prod
