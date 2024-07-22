#!/bin/bash

# grabs email of user that triggered contentful update for post steps

set -euo pipefail

: ${CMS_EMAIL_LIST}
: ${GOV_NOTIFY}
: ${status}

pip install notifications-python-client

# Extract the last entry, RS is the record separator and ORS is the output record separator
# which preserves the separator in the output.
last_entry=$(awk 'BEGIN {RS="\n# CMS Update:"; ORS="# CMS Update:"} {entry=$0} END {print entry}' CONTENTFUL_CHANGELOG.md)

# Use grep to find the line containing "Editor:" and cut to extract the editor's name
editor_name=$(echo "$last_entry" | grep '^Editor:' | sed 's/^Editor: //')

# Use grep to find the line containing "Revison:" and cut to extract the value
revision=$(echo "$last_entry" | grep '^Revision:' | sed 's/^Revision: //')

# Use grep to find the line containing "Content Type:" and cut to extract the value
content_type=$(echo "$last_entry" | grep '^Content Type:' | sed 's/^Content Type: //')

# Use sed to extract the content between the lines containing "```txt and ```" 
content_changed=$(echo "$last_entry" | sed -n '/```txt/,/```/p' | sed '1d;$d')

# Split editor name into first and last name
first_name=$(echo "$editor_name" | cut -d ' ' -f 1)
surname=$(echo "$editor_name" | cut -d ' ' -f 2)

export STATUS=$status
export FIRSTNAME=$first_name
export SURNAME=$surname
export EMAIL=$(echo "$CMS_EMAIL_LIST" | grep "$FIRSTNAME $SURNAME" | sed 's/.*://')
export GOVNOTIFYAPIKEY=$GOV_NOTIFY

# Set additional environment variables that may prove useful
# for the email template
export REVISION=$revision
export CONTENTTYPE=$content_type
export CONTENTCHANGED=$content_changed
python ci/tasks/util/send_email.py