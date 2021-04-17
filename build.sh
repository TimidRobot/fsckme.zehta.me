#!/bin/bash
#### SETUP ####################################################################
set -o errexit
set -o errtrace
set -o nounset

trap '_es=${?};
    printf "${0}: line ${LINENO}: \"${BASH_COMMAND}\"";
    printf " exited with a status of ${_es}\n";
    exit ${_es}' ERR

printf "\e[1m\e[7m %-80s\e[0m\n" 'Removing contents of build dir (docs/)'
echo "$(rm -rfv docs/* | wc -l) files and directories removed"
if [[ "${1:-}" == '-p' ]]; then
    echo
    echo
    printf "\e[1m\e[7m %-80s\e[0m\n" 'Lektor: uninstalling all plugins'
    pipenv run lektor plugins flush-cache
    echo
    echo
    printf "\e[1m\e[7m %-80s\e[0m\n" 'Lektor: installing all plugins'
    pipenv run lektor plugins reinstall
fi
echo
echo
printf "\e[1m\e[7m %-80s\e[0m\n" 'Lektor: building site'
pipenv run lektor build --extra-flag minify --output-path ../docs
echo
echo
