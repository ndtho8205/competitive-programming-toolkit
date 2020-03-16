#!/usr/bin/env bash

export SCRIPT_PATH="$(cd "$(dirname "$0")"; pwd -P)"

set -e
echo ''

if test -t 1
then
  ncolors=$(command -v tput > /dev/null && tput colors)
  if test -n "$ncolors" && test "$ncolors" -ge 8
  then
    normal="$(tput sgr0)"
    green="$(tput setaf 2)"
  fi
fi

success () {
  printf "\r\033[2K  [ ${green}OK${normal} ] %s\n" "$1"
}

install () {
  src="$SCRIPT_PATH/app.py"
  dst="$HOME/.local/bin/cptool"

  ln -s "$src" "$dst"
  success "linked $src to $dst"
}

install

echo 'All installed!'
