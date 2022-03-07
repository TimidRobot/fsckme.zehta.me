#!/bin/bash
#
# https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity

set -o errtrace
set -o nounset

printf "\e[1m\e[7m %-80s\e[0m\n" 'Combining layout CSS'
pushd ./source/assets/static >/dev/null
{
    cat normalize.css
    cat skeleton.css
    cat pygments-monokai.css
} > layout.css
echo 'done.'
echo
echo
popd >/dev/null
