#!/bin/bash

# shared runner

# https://xxx
GITLAB_URL=${1}
# https://xxx/admin/runners
REGISTRATION_TOKEN=$2
RUNNER_NAME=${3:-"my-runner"}
TAG_LIST=$4
# shell|docker
executor=${5:-shell}

if [ $# -eq 0 ]; then
  echo "No params"
  exit -1
fi

if [ $executor == "docker" ]; then
  gitlab-ci-multi-runner register -n \
    --url ${GITLAB_URL} \
    --registration-token ${REGISTRATION_TOKEN} \
    --executor docker \
    --description ${RUNNER_NAME} \
    --tag-list ${TAG_LIST} \
    --executor docker \
    --docker-image "docker:latest" \
    --docker-volumes /var/run/docker.sock:/var/run/docker.sock
fi

if [ $executor == "shell" ]; then
  gitlab-ci-multi-runner register -n \
    --url ${GITLAB_URL} \
    --registration-token ${REGISTRATION_TOKEN} \
    --executor docker \
    --description ${RUNNER_NAME} \
    --tag-list ${TAG_LIST} \
    --executor shell
fi
