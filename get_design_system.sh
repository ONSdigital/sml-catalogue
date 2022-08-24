#!/bin/sh

set -e

TMPFILE=`mktemp ./templates.XXXXXXXXXX`

wget https://github.com/ONSdigital/design-system/releases/download/55.1.0/templates.zip -O $TMPFILE
rm -rf sml_builder/templates/components
rm -rf sml_builder/templates/layout

unzip -d ./sml_builder $TMPFILE
rm $TMPFILE
