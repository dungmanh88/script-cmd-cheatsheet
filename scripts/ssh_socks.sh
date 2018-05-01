#!/bin/bash

local_host=${1:-"127.0.0.1"}
local_port=$2  ### local_port must be greater than 1023
### because 0-1023 is privileged ports
user=$3
remote_ssh_host=$4
remote_ssh_port=${5:-22}
execute_shell=${6:-0}

if [ $# -eq 0 ]; then
  echo "No params"
  exit -1
fi

if [ $execute_shell -eq 0 ]; then
  ssh -D $local_host:$local_port $user@$remote_ssh_host -p $remote_ssh_port -Nq
else
  ssh -D $local_host:$local_port $user@$remote_ssh_host -p $remote_ssh_port
fi

### Socks proxy does not help you
# clear cookie, cache on your browser
# avoid tracking information
### Socks proxy makes your connection slow down because of extra hop and busy proxy server
