#!/bin/bash

declare -A update_details

changelog_file="CONTENTFUL_CHANGELOG.md"

# Function to make an API call to the Content Management API and return the full name
get_user_full_name() {
    local space_id=$1
    local user_id=$2
    local cma_token=$3

    response=$(curl --silent --show-error --request GET "https://api.contentful.com/spaces/${space_id}/users/${user_id}" \
        -H "Authorization: Bearer ${cma_token}")

    first_name=$(echo "$response" | jq -r '.firstName')
    last_name=$(echo "$response" | jq -r '.lastName')

    update_details["full_name"]="${first_name} ${last_name}"
}

# Function to make an API call to the Content Management API and return the full name
get_entry_by_id() {
    local space_id=$1
    local env=$2
    local entity_id=$3
    local cda_token=$4

    response=$(curl --silent --show-error --request GET "https://cdn.contentful.com/spaces/${space_id}/environments/${env}/entries/${entity_id}" \
        -H "Authorization: Bearer ${cda_token}")

    #echo "Response: $response"

    # Clean the response
    # Use sed to escape control characters like newlines if needed
    cleaned_response=$(echo "$response" | tr '\n' ' ')

    update_details["environment"]=$(echo "$cleaned_response" | jq -r '.sys.environment.sys.id')
    update_details["content_type"]=$(echo "$cleaned_response" | jq -r '.sys.contentType.sys.id')
    update_details["revision"]=$(echo "$cleaned_response" | jq -r '.sys.revision')
    update_details["updated_at"]=$(echo "$cleaned_response" | jq -r '.sys.updatedAt')
    update_details["fields"]=$(echo "$cleaned_response" | jq -r '.fields')
}


# Replace these with actual space and user IDs as necessary
space_id="${GITHUB_EVENT_SPACE_ID}"
user_id="${GITHUB_EVENT_USER_ID}"
echo "Space ID: $space_id"
echo "User ID: $user_id"

# Get the full name
get_user_full_name "$space_id" "$user_id" "$CONTENTFUL_TOKEN"

# Get the entry by ID
entry_id="${GITHUB_EVENT_ENTITY_ID}"
get_entry_by_id "$space_id" "prod" "$entry_id" "$CONTENTFUL_CDA_TOKEN"

# Remove milliseconds and 'Z'
cleaned_timestamp=$(echo "${update_details["updated_at"]}" | sed -E 's/\.[0-9]{3}Z$//' | sed 's/T/ /')

# Detect if GNU date is available
if date --version &>/dev/null; then
  # GNU date (Linux)
  formatted_timestamp=$(date -d "$cleaned_timestamp" +"%d/%m/%Y at %I:%M:%S %p")
else
  # macOS date
  formatted_timestamp=$(date -j -f "%Y-%m-%d %H:%M:%S" "$cleaned_timestamp" +"%d/%m/%Y at %I:%M:%S %p")
fi

fields=$(echo "${update_details["fields"]}" | jq -r 'to_entries[] | "\(.key): \(.value)"')

{
  echo "# CMS Update: $formatted_timestamp"
  echo ""
  echo "Editor: ${update_details["full_name"]}"
  echo ""
  echo "Environment: ${update_details["environment"]}"
  echo ""
  echo "Content Type: ${update_details["content_type"]}"
  echo ""
  echo "Revision: ${update_details["revision"]}"
  echo ""
  echo "Updated At: ${update_details["updated_at"]}"
  echo ""
  echo "Content Updated:"
  echo ""
  echo '```txt'
  echo "$fields"
  echo '```'
  echo ""
  echo "— $formatted_timestamp —"
  echo ""

} >> "$changelog_file"
