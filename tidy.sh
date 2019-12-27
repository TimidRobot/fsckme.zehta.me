#!/bin/bash
#### SETUP ####################################################################
set -o errexit
set -o errtrace
set -o nounset

trap '_es=${?};
    printf "${0}: line ${LINENO}: \"${BASH_COMMAND}\"";
    printf " exited with a status of ${_es}\n";
    exit ${_es}' ERR

for _file in $(find docs -type f -name '*.html')
do
    printf "\e[1m\e[7m %-80s\e[0m\n" "${_file}"
    tidy -modify -indent -wrap 80 -quiet -utf8 \
        --drop-empty-elements no \
        --drop-empty-paras no \
        --quote-ampersand no \
        --quote-nbsp no \
        "${_file}" || true
    echo
done
