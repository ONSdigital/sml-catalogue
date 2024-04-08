# Usage: ./migrate.sh
#  TODO: create a backup to allow rollbacks
#  TODO: add variables to migrate.sh to allow export to occur between both dev-preprod and preprod-prod

# merge content types first
contentful merge export --te preprod --se dev --management-token $CLI_KEY --output-file ./migrations/dev-export.js
contentful space migration --space-id $SPACE_ID --management-token $CLI_KEY --environment-id preprod ./migrations/dev-export.js

# then merge entries
contentful space export --management-token $CLI_KEY --export-dir ./contentful-export --environment-id dev --content-file dev-export.json
contentful space import --management-token $CLI_KEY --environment-id preprod --content-file contentful-export/dev-export.json