#!/bin/bash
username=$1
rolename=$2

if [ $# -eq 0 ]; then
  echo "No params"
  exit -1
fi

ansible-galaxy install ${username}.${rolename}
