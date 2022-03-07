#!/bin/bash
#
# https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity

set -o errtrace
set -o nounset

printf "\e[1m\e[7m %-80s\e[0m\n" 'Generating SRI hashes'
for _file in $(find docs -type f \( -iname '*.js' -o -iname '*.css' \))
do
    printf "%-40s %s\n" "${_file}"  "\"${_file#docs}\""
    sha512=$(cat "${_file}" | openssl dgst -sha512 -binary | openssl base64 -A)
    echo "sha512-${sha512}" | tee -a ${_file}.sha512
    echo
    echo
done
