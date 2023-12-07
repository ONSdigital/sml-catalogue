#!/bin/sh

set -e

TMPFILE=`mktemp ./templates.XXXXXXXXXX`

wget https://github.com/ONSdigital/design-system/releases/download/67.0.1/templates.zip -O $TMPFILE
rm -rf sml_builder/templates/components
rm -rf sml_builder/templates/layout

unzip -d ./sml_builder $TMPFILE
rm $TMPFILE
