#!/bin/bash

# This script is used to update the CONTENTFUL_CHANGELOG.md file with the details of the latest Contentful update.
# Concourse pipeline detects changes to the changelog file to trigger a preprod build for CMS content review.
# Uage:
# ./update_changelog.sh <environment - preprod|prod|dev>
#
# The CONTENTFUL_CDA_TOKEN envvironment variable must be set to the
# API Token matching the passed environment parameter. 

# Stop on first error
set -e

declare -A update_details

changelog_file="CONTENTFUL_CHANGELOG.md"

# Parse error response
parse_error_response() {
    local response=$1
    local http_status=$2

    case "$http_status" in
        400)
            echo "Error: Bad request (HTTP 400)"
            ;;
        401)
            echo "Error: Unauthorized (HTTP 401)"
            ;;
        403)
            echo "Error: Forbidden (HTTP 403)"
            ;;
        404)
            echo "Error: Not found (HTTP 404)"
            ;;
        500)
            echo "Error: Internal server error (HTTP 500)"
            ;;
        *)
            echo "Error: Unexpected HTTP status $http_status"
            ;;
    esac

    echo "Error Response: $response"
}

# Function to make an API call to the Content Management API and return the full name
get_user_full_name() {
    local space_id=$1
    local user_id=$2
    local cma_token=$3

    response=$(curl --silent --show-error --write-out "HTTPSTATUS:%{http_code}" --request GET "https://api.contentful.com/spaces/${space_id}/users/${user_id}" \
        -H "Authorization: Bearer ${cma_token}")

    # Extract the body and the status code and remove the status code from the response
    http_body=$(echo "$response" | sed -e 's/HTTPSTATUS\:.*//g')
    http_status=$(echo "$response" | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')

    echo "User Full Name HTTP Status: $http_status"

    if [ "$http_status" -eq 200 ]; then
        first_name=$(echo "$http_body" | jq -r '.firstName')
        last_name=$(echo "$http_body" | jq -r '.lastName')

        if [ -n "$first_name" ] && [ -n "$last_name" ]; then
            update_details["full_name"]="${first_name} ${last_name}"
        else
            echo "Error: Failed to parse the user's full name from the API response."
            return 1
        fi
    else
        parse_error_response "$http_body" "$http_status"
        return 1
    fi
}

# Function to make an API call to the Content Management API and return the full name
get_entry_by_id() {
    local space_id=$1
    local env=$2
    local entity_id=$3
    local cda_token=$4

    response=$(curl --silent --show-error --write-out "HTTPSTATUS:%{http_code}" --request GET "https://cdn.contentful.com/spaces/${space_id}/environments/${env}/entries/${entity_id}" \
        -H "Authorization: Bearer ${cda_token}")

    # Extract the body and the status code and remove the status code from the response
    http_body=$(echo "$response" | sed -e 's/HTTPSTATUS\:.*//g')
    http_status=$(echo "$response" | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')

    echo "Entry by ID HTTP Status: $http_status"

    if [ "$http_status" -eq 200 ]; then
        # Clean the response
        # Use sed to escape control characters like newlines if needed
        cleaned_response=$(echo "$http_body" | tr '\n' ' ')

        update_details["environment"]=$(echo "$cleaned_response" | jq -r '.sys.environment.sys.id')
        update_details["content_type"]=$(echo "$cleaned_response" | jq -r '.sys.contentType.sys.id')
        update_details["revision"]=$(echo "$cleaned_response" | jq -r '.sys.revision')
        update_details["updated_at"]=$(echo "$cleaned_response" | jq -r '.sys.updatedAt')
        update_details["fields"]=$(echo "$cleaned_response" | jq -r '.fields')
    else
        parse_error_response "$http_body" "$http_status"
        return 1
    fi
}


# Check if the environment parameter is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <environment>"
    exit 1
fi

# Assign the first parameter to a variable
environment="$1"

# Replace these with actual space and user IDs as necessary
space_id="${GITHUB_EVENT_SPACE_ID}"
user_id="${GITHUB_EVENT_USER_ID}"
echo "Space ID: $space_id"
echo "User ID: $user_id"

# Get the full name
get_user_full_name "$space_id" "$user_id" "$CONTENTFUL_TOKEN"

# Check the return from the function
if [ $? -eq 0 ]; then
    echo "User full name: ${update_details["full_name"]}"

    # Get the entry by ID
    entry_id="${GITHUB_EVENT_ENTITY_ID}"
    get_entry_by_id "$space_id" "$environment" "$entry_id" "$CONTENTFUL_CDA_TOKEN"

    # Check the return from the function
    if [ $? -eq 0 ]; then
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

    else
        echo "Failed to retrieve entry details."
        #exit 1
    fi

else
    echo "Failed to retrieve user full name."
    #exit 1
fi

