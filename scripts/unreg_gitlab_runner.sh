#!/bin/bash

RUNNER_NAME=${1:-"my-runner"}

if [ $# -eq 0 ]; then
  echo "No params"
  exit -1
fi

gitlab-ci-multi-runner unregister -n ${RUNNER_NAME}
