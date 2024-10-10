#!/bin/bash

# $MASTER_CDA_KEY, $SPACE_ID and $CLI_KEY must be set as environment variables.
# $MASTER_CDA_KEY is the (read-only) Content Delivery API key which can access all environments.
# $SPACE_ID is the Contentful space ID.
# $CLI_KEY is the Contentful management token (sometimes referred to as CMA key).

GREEN="\033[32m"
RED="\033[31m"
NC="\033[0m"

while getopts b:c: opt; do
  case "${opt}" in
    b)
      base_environment=${OPTARG}
      ;;
    c)
      compare_environment=${OPTARG}
      ;;
    ?)
      echo "Invalid option: -${OPTARG}."
      exit 1
      ;;
  esac
done

allowed_envs='^(dev|preprod|prod)$'


if  [ -z "$base_environment" ] || [ -z "$compare_environment" ]; then
  echo "Usage: ./contentful_audit.sh -b <base_environment> -c <compare_environment>"
  echo " -- Example: ./contentful_migrate.sh -s dev -t preprod"
  exit 1
elif [ "$base_environment" == "$compare_environment" ]; then
  echo "Usage: ./contentful_audit.sh -b <base_environment> -c <compare_environment>"
  echo " -- Source and target environments must be different"
  exit 1
elif [[ ! "$base_environment" =~ $allowed_envs ]] || [[ ! "$compare_environment" =~ $allowed_envs ]]; then
  echo "Usage: ./contentful_audit.sh -b <base_environment> -c <compare_environment>"
  echo " -- Environment must be one of: dev, preprod, prod"
  exit 1
fi



err_handler() {
  # log the error
  timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
  migration_log="${timestamp}: Error raised while auditing content from $base_environment to $compare_environment \n - Failing command: ${1} \n - Exit code: ${2}"
  echo -e $migration_log
  echo -e $migration_log >> ./contentful-data/migration-log.txt
  exit $2
}

trap 'err_handler "$BASH_COMMAND" "$?"' ERR

export ACTIVE_VALUE=False
python contentful_webhook.py
echo " -- Webhook Disabled"
contentful merge show --te "$compare_environment" --se "$base_environment" --management-token $CLI_KEY
contentful merge export --te $compare_environment --se "$base_environment" --management-token $CLI_KEY --output-file ./contentful-data/audits/${compare_environment}-export.js
contentful-merge create --space $SPACE_ID --source $base_environment --target $compare_environment --cda-token $MASTER_CDA_KEY --output-file ./contentful-data/audits/${base_environment}-${compare_environment}-changeset.json
export ACTIVE_VALUE=True
python contentful_webhook.py
echo " -- Webhook Enabled"

timestamp=$(date "+%Y.%m.%d-%H.%M.%S")
migration_log="${timestamp}: Audited content between $base_environment and $compare_environment"
echo $migration_log
echo $migration_log >> ./contentful-data/migration-log.txt