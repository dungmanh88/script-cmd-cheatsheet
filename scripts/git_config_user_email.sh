#!/bin/bash

if [ $# -eq 0 ]; then
  echo "No params"
  exit -1
fi

name=$1
email=$2

git config user.name "${name}" && \
git config user.email "${email}"
