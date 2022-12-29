#!/bin/sh

CMDS=("pylint sml_builder" "flake8 sml_builder" "black --check --diff sml_builder" "bandit -r sml_builder")

for i in "${CMDS[@]}"
do 
    if $i
    then
        echo "$i command successfully executed"
    else
        echo "$i command failed to execute or display errors that needs to be corrected"
    fi
done