#!/bin/bash
# Usage: ./contentful_migrate.sh -s <source_environment> -t <target_environment>
# -- Example: ./contentful_migrate.sh -s dev -t preprod
# Used to migrate content between environments in Contentful (not to be confused with Concourse).
# $MASTER_CDA_KEY, $SPACE_ID and $CLI_KEY must be set as environment variables.
# $MASTER_CDA_KEY is the (read-only) Content Delivery API key which can access all environments.
# $SPACE_ID is the Contentful space ID.
# $CLI_KEY is the Contentful management token (sometimes referred to as CMA key).


set -eo pipefail

GREEN="\033[32m"
RED="\033[31m"
NC="\033[0m"

while getopts s:t: opt; do
  case "${opt}" in
    s)
      source_environment=${OPTARG}
      ;;
    t)
      target_environment=${OPTARG}
      ;;
    ?)
      echo "Invalid option: -${OPTARG}."
      exit 1
      ;;
  esac
done

allowed_envs='^(dev|preprod|prod)$'

if  [ -z "$source_environment" ] || [ -z "$target_environment" ]; then
  echo "Usage: ./contentful_migrate.sh -s <source_environment> -t <target_environment>"
  echo " -- Example: ./contentful_migrate.sh -s dev -t preprod"
  exit 1
elif [ "$source_environment" == "$target_environment" ]; then
  echo "Usage: ./contentful_migrate.sh -s <source_environment> -t <target_environment>"
  echo " -- Source and target environments must be different"
  exit 1
elif [[ ! "$source_environment" =~ $allowed_envs ]] || [[ ! "$target_environment" =~ $allowed_envs ]]; then
  echo "Usage: ./contenful_migrate.sh -s <source_environment> -t <target_environment>"
  echo " -- Environment must be one of: dev, preprod, prod"
  exit 1
fi



err_handler() {
  # log the error
  timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
  migration_log="${timestamp}: Error raised while migrating content from $source_environment to $target_environment \n - Failing command: ${1} \n - Exit code: ${2}"
  echo -e $migration_log
  echo -e $migration_log >> ./contentful-data/migration-log.txt
  echo "Consider triggering a rollback with the contentful_rollback script:"
  echo "./contentful_rollback.sh -s $source_environment -t $target_environment"
  exit $2
}

trap 'err_handler "$BASH_COMMAND" "$?"' ERR

# Confirmation step
echo -e "You are about to migrate content from ${GREEN}$source_environment${NC} to ${GREEN}$target_environment${NC}."
read -p "Are you sure you want to proceed? (y/n): " confirm
if [[ $confirm != [yY] ]]; then
  echo -e "${RED}Migration cancelled.${NC}"
  exit 0
else
  echo -e "${GREEN}Proceeding with migration.${NC}"
fi
echo "Migrating content from $source_environment to $target_environment"
# create backup files
# store all the content entries and types in the target environment for rollback
contentful space export --management-token $CLI_KEY --export-dir ./contentful-data/rollbacks --environment-id $target_environment --content-file ${target_environment}-export.json
# store the migration that would be required to revert the target environment to its original state
contentful merge export --te $source_environment --se $target_environment --management-token $CLI_KEY --output-file ./contentful-data/rollbacks/${target_environment}-export.js

# migrate content types first
contentful merge export --te $target_environment --se $source_environment --management-token $CLI_KEY --output-file ./contentful-data/migrations/${source_environment}-export.js
contentful space migration --space-id $SPACE_ID --management-token $CLI_KEY --environment-id $target_environment ./contentful-data/migrations/${source_environment}-export.js

# then merge entries
contentful-merge create --space $SPACE_ID --source $source_environment --target $target_environment --cda-token $MASTER_CDA_KEY --output-file ./contentful-data/migrations/${source_environment}-${target_environment}-changeset.json
contentful-merge apply --space $SPACE_ID --environment $target_environment --cma-token $CLI_KEY --file ./contentful-data/migrations/${source_environment}-${target_environment}-changeset.json

# log the migration
timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
migration_log="${timestamp}: Migrated content from $source_environment to $target_environment"
echo $migration_log
echo $migration_log >> ./contentful-data/migration-log.txt
