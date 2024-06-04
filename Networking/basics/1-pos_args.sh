#!/usr/bin/env bash
# Pings to the argument passed to the script
# address=$1
# ping -c 5 $address


if [ $# -lt 1 ]; then
  echo "We don't deal with no arguments"
else
  echo "Args Found: $*"
fi