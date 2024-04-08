 
#  TODO: ensure the content models are the same in both environments
#  TODO: create a backup to allow rollbacks
#  TODO: add variables to migrate.sh to allow export to occur between both dev-preprod and preprod-prod

contentful space export --management-token $CLI_KEY --export-dir ./contentful-export --environment-id dev --content-file dev-export.json
contentful space import --management-token $CLI_KEY --environment-id preprod --content-file contentful-export/dev-export.json