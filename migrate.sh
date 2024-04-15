#!/bin/bash
# Usage: ./migrate.sh -s <source_environment> -t <target_environment> [-r]
set -eo pipefail

while getopts s:t:r opt; do
  case "${opt}" in
    s)
      source_environment=${OPTARG}
      ;;
    t)
      target_environment=${OPTARG}
      ;;
    r)
      rollback_requested=true
      echo "Performing rollback..."
      ;;
    ?)
      echo "Invalid option: -${OPTARG}."
      exit 1
      ;;
  esac
done

allowed_envs='^(dev|preprod|prod)$'

if  [ -z "$source_environment" ] || [ -z "$target_environment" ]; then
  echo "Usage: ./migrate.sh -s <source_environment> -t <target_environment> [-r]"
  echo " -- Use the flag -r to initiate a rollback"
  echo " -- Example: ./migrate.sh -s dev -t preprod"
  exit 1
elif [ "$source_environment" == "$target_environment" ]; then
  echo "Usage: ./migrate.sh -s <source_environment> -t <target_environment> [-r]"
  echo " -- Use the flag -r to initiate a rollback"
  echo " -- Source and target environments must be different"
  exit 1
elif [[ ! "$source_environment" =~ $allowed_envs ]] || [[ ! "$target_environment" =~ $allowed_envs ]]; then
  echo "Usage: ./migrate.sh -s <source_environment> -t <target_environment> [-r]"
  echo " -- Use the flag -r to initiate a rollback"
  echo " -- Environment must be one of: dev, preprod, prod"
  exit 1
fi

err_handler() {
  # log the error
  timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
  migration_log="${timestamp}: Error raised while migrating content from $source_environment to $target_environment \n - Failing command: ${1} \n - Exit code: ${2}"
  echo -e $migration_log
  echo -e $migration_log >> ./contentful-data/migration-log.txt
  echo "Consider triggering a rollback with the -r flag:"
  echo "./migrate.sh -s $source_environment -t $target_environment -r"
  exit $2
}

trap 'err_handler "$BASH_COMMAND" "$?"' ERR

if [ -z "$rollback_requested" ]; then
  echo "Migrating content from $source_environment to $target_environment"
  # create backup files
  # store all the content entries and types in the target environment
  contentful space export --management-token $CLI_KEY --export-dir ./contentful-data/rollbacks --environment-id $target_environment --content-file ${target_environment}-export.json
  # store the migration that would be required to revert the target environment to its original state
  contentful merge export --te $source_environment --se $target_environment --management-token $CLI_KEY --output-file ./contentful-data/rollbacks/${target_environment}-export.js

  # migrate content types first
  contentful merge export --te $target_environment --se $source_environment --management-token $CLI_KEY --output-file ./contentful-data/migrations/${source_environment}-export.js
  contentful space migration --space-id $SPACE_ID --management-token $CLI_KEY --environment-id $target_environment ./contentful-data/migrations/${source_environment}-export.js

  # then merge entries
  contentful space export --management-token $CLI_KEY --export-dir ./contentful-data/content-exports --environment-id $source_environment --content-file ${source_environment}-export.json
  contentful space import --management-token $CLI_KEY --environment-id $target_environment --content-file ./contentful-data/content-exports/${source_environment}-export.json
  
  # log the migration
  timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
  migration_log="${timestamp}: Migrated content from $source_environment to $target_environment"
  echo $migration_log
  echo $migration_log >> ./contentful-data/migration-log.txt

else
  echo "Rolling back content in $target_environment"
  contentful space import --management-token $CLI_KEY --environment-id $target_environment --content-file ./contentful-data/rollbacks/${target_environment}-export.json
  contentful space migration --space-id $SPACE_ID --management-token $CLI_KEY --environment-id $target_environment ./contentful-data/rollbacks/${target_environment}-export.js
  # log the rollback
  timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
  migration_log="${timestamp}: Performed rollback on environment $target_environment"
  echo $migration_log
  echo $migration_log >> ./contentful-data/migration-log.txt
fi
