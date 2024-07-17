#!/bin/bash

# grabs email of user that triggered contentful update for post steps

set -euo pipefail

: ${CMS_EMAIL_LIST}
: ${GOV_NOTIFY}
: ${status}

pip install notifications-python-client

tag=$( tail -n 1 CONTENTFUL_CHANGELOG.md )
export STATUS=$status
export FIRSTNAME=$(echo "${tag//\"}" | awk '{print $1;}')
echo "$FIRSTNAME"
export SURNAME=$(echo "${tag//\"}" | awk '{print $2;}')
echo "$SURNAME"
export EMAIL=$(echo "$CMS_EMAIL_LIST" | grep "$FIRSTNAME $SURNAME" | sed 's/.*://')
export GOVNOTIFYAPIKEY=$GOV_NOTIFY
python ci/tasks/util/send_email.py