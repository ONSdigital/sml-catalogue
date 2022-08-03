#!/bin/sh

set -e

TMPFILE=`mktemp ./templates.XXXXXXXXXX`
wget https://github.com/ONSdigital/design-system/releases/download/53.1.1/templates.zip -O $TMPFILE
unzip -d ./ $TMPFILE
rm $TMPFILE