#!/bin/sh

set -e

TMPFILE=`mktemp ./templates.XXXXXXXXXX`
wget https://github.com/ONSdigital/design-system/releases/download/54.0.1/templates.zip -O $TMPFILE
unzip -d ./sml_builder $TMPFILE
rm $TMPFILE