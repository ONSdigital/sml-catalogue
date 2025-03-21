#!/bin/bash
# Usage: ./contentful_rollback.sh -t <target_environment>
# -- Example: ./contentful_rollback.sh -t preprod
# Used to rollback content in an environment in Contentful (not to be confused with Concourse).
# Before a migration is completed, the migration script stores a snapshot of the target environment in the `contentful-data/rollbacks` directory.
# This script will import the snapshot and rollback the target environment to the state it was in before the migration.
# It is also expected that the files in the contentful-data directory are committed to git.
# $MASTER_CDA_KEY, $SPACE_ID and $CLI_KEY must be set as environment variables.
# $MASTER_CDA_KEY is the (read-only) Content Delivery API key which can access all environments.
# $SPACE_ID is the Contentful space ID.
# $CLI_KEY is the Contentful management token (sometimes referred to as CMA key).

# Note: this script requires your current working directory to be ./scripts.

set -eo pipefail

GREEN="\033[32m"
RED="\033[31m"
NC="\033[0m"

while getopts t: opt; do
  case "${opt}" in
    t)
      target_environment=${OPTARG}
      ;;
    ?)
      echo "Invalid option: -${OPTARG}."
      exit 1
      ;;
  esac
done

allowed_envs='^(preprod|prod)$'

if [ -z "$target_environment" ]; then
  echo "Usage: ./contentful_rollback.sh -t <target_environment>"
  echo " -- Example: ./contentful_rollback.sh -t preprod"
  exit 1
elif [[ ! "$target_environment" =~ $allowed_envs ]]; then
  echo "Usage: ./contentful_rollback.sh -t <target_environment>"
  echo " -- Environment must be one of: preprod, prod"
  exit 1
fi

err_handler() {
  # log the error
  timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
  migration_log="${timestamp}: Error raised while rolling back content in $target_environment \n - Failing command: ${1} \n - Exit code: ${2}"
  echo -e $migration_log
  echo -e $migration_log >> ../contentful-data/migration-log.txt
  exit $2
}

trap 'err_handler "$BASH_COMMAND" "$?"' ERR

# Confirmation step
read -p "Are you sure you want to rollback content in $target_environment? (y/n): " confirm
if [[ $confirm != [yY] ]]; then
  echo -e "${RED}Rollback cancelled.${NC}"
  exit 0
else
  echo -e "${GREEN}Proceeding with rollback.${NC}"
fi
echo "Rolling back content in $target_environment"
# export the current state of the environment for use in deletion_changeset.py
contentful space export --management-token $CLI_KEY --export-dir ../contentful-data/content-exports --environment-id $target_environment --content-file ${target_environment}-export.json
# delete all entries using deletion_changeset.py
python sub_scripts/deletion_changeset.py $target_environment ../contentful-data/content-exports/${target_environment}-export.json
contentful-merge apply --space $SPACE_ID --environment $target_environment --cma-token $CLI_KEY --file ../contentful-data/migrations/deletion-changeset.json
# perform any necessary content type changes
contentful space migration --space-id $SPACE_ID --management-token $CLI_KEY --environment-id $target_environment ../contentful-data/rollbacks/${target_environment}-export.js
# import the snapshot
contentful space import --management-token $CLI_KEY --environment-id $target_environment --content-file ../contentful-data/rollbacks/${target_environment}-export.json
# log the rollback
timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
migration_log="${timestamp}: Performed rollback on environment $target_environment"
echo $migration_log
echo $migration_log >> ../contentful-data/migration-log.txt
