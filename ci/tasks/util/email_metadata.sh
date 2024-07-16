#!/bin/bash

# grabs email of user that triggered contentful update for post steps

set -euo pipefail

: ${cms_email_list}
: ${gov_notify_test}
: ${status}

tag=$( tail -n 1 CONTENTFUL_CHANGELOG.md )
arr=($tag)
export STATUS=$status
export FIRSTNAME=${arr[*]:0:1}
export SURNAME=${arr[*]:1:2}
export EMAIL=${grep "$firstname $surname" "$cms_email_list" | sed -n -e 's/^.*: //p'}
export GOVNOTIFYAPIKEY=$gov_notify_test
python ci/tasks/util/send_email.py