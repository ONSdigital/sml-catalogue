#!/bin/bash

# grabs email of user that triggered contentful update for post steps

set -euo pipefail

: ${cms_email_list}

tag=$( tail -n 1 CONTENTFUL_CHANGELOG.md )
arr=($tag)
firstname=${arr[*]:0:1}
surname=${arr[*]:1:2}
grep "$firstname $surname" "$cms_email_list" | sed -n -e 's/^.*: //p' > email/email
echo "$firstname $surname made a change in contentful triggering the following build on Concourse SML: ${BUILD_ID}. Please contact the SML team if the pipeline has failed " > email/body
