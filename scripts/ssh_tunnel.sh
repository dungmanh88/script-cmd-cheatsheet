#!/bin/bash

local_host=${1:-"127.0.0.1"}
local_port=$2  ### local_port must be greater than 1023
### because 0-1023 is privileged ports
user=$3
remote_host=$4
remote_port=$5
execute_shell=${6:-0}

if [ $# -eq 0 ]; then
  echo "No params"
  exit -1
fi

if [ $execute_shell -eq 0 ]; then
  ssh -L $local_host:$local_port:$remote_host:$remote_port $user@$remote_host -N
else
  ssh -L $local_host:$local_port:$remote_host:$remote_port $user@$remote_host
fi
