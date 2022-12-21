#!/bin/sh

CMDS=("pylint sml_builder" "flake8 sml_builder" "bandit -r sml_builder")

for i in "${CMDS[@]}"
do 
    if $i
    then
        echo "$i command successfully executed"
    else
        echo "$i command failed to execute or have errors that needs to be corrected"
    fi
done