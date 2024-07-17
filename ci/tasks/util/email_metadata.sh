#!/bin/bash

# grabs email of user that triggered contentful update for post steps

set -euo pipefail

: ${CMS_EMAIL_LIST}
: ${GOV_NOTIFY}
: ${status}

pip install notifications-python-client

tag=$( tail -n 1 CONTENTFUL_CHANGELOG.md )
arr=($tag)
export STATUS=$status
export FIRSTNAME=${arr[*]:0:1}
export SURNAME=${arr[*]:1:2}
export EMAIL=${echo "$CMS_EMAIL_LIST" | grep "$firstname $surname"| sed 's/.*://'}
export GOVNOTIFYAPIKEY=$GOV_NOTIFY
python ci/tasks/util/send_email.py