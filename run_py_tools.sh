#!/bin/sh

CMDS=("black --check --diff freeze.py sml_builder features" "pylint freeze.py sml_builder features" "flake8 ." "isort --check-only ." "bandit -r freeze.py sml_builder features")

for i in "${CMDS[@]}"
do 
    if $i
    then
        echo "$i command successfully executed"
    else
        echo "$i command failed to execute or display errors that needs to be corrected"
    fi
done