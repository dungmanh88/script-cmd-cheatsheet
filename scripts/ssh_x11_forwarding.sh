#!/bin/bash

user=$1
remote_ssh_host=$2
remote_ssh_port=${3:-22}

if [ $# -eq 0 ]; then
  echo "No params"
  exit -1
fi

ssh -X $user@$remote_ssh_host -p $remote_ssh_port
### remote_ssh_host must install X11 server
