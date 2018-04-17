#!/bin/bash

# code nay ho tro backup ca table trong mot db hoac backup 1 db
if [ $# -eq 0 ]; then
  echo "No params"
  exit -1
fi

dbname=${1}
host=${2:-localhost}
is_replication=${3:-0}
params="--single-transaction --routines --triggers --events --add-drop-database --add-drop-table --extended-insert --quick"
[ ${is_replication} -eq 1 ] && params="${params} --master-data=2"
name=`echo $dbname | tr " " "_"`
echo "" > /tmp/${name}.dump.log
mysqldump -u root -p -h ${host} ${params} ${dbname} --log-error=/tmp/${name}.dump.log > ${name}.dump
