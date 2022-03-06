#!/bin/bash
#
# https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity

set -o errtrace
set -o nounset

printf "\e[1m\e[7m %-80s\e[0m\n" 'Generating SRI hashes'
for _file in $(find docs -type f -iname '*.js')
do
    printf "%-40s %s\n" "${_file}"  "\"${_file#docs}\""
    sha384=$(cat "${_file}" | openssl dgst -sha384 -binary | openssl base64 -A)
    echo "sha384-${sha384}" | tee -a ${_file}.sha384
    echo
    echo
done
