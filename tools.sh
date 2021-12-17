#!/bin/bash
#### SETUP ####################################################################
set -o errexit
set -o errtrace
set -o nounset

trap '_es=${?};
    printf "${0}: line ${LINENO}: \"${BASH_COMMAND}\"";
    printf " exited with a status of ${_es}\n";
    exit ${_es}' ERR

printf "\e[1m\e[7m %-80s\e[0m\n" 'isort'
pipenv run isort ${@:-.}
echo

printf "\e[1m\e[7m %-80s\e[0m\n" 'black'
pipenv run black ${@:-.}
echo

printf "\e[1m\e[7m %-80s\e[0m\n" 'flake8'
pipenv run flake8 ${@:-.}
echo
