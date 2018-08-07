#!/bin/bash

# code nay ho tro backup ca table trong mot db hoac backup 1 db
if [ $# -eq 0 ]; then
  echo "No params"
  exit -1
fi

dbname=${1}
username=${2:-root}
host=${3:-localhost}
is_replication=${4:-0}
params="--single-transaction --routines --triggers --events --add-drop-database --add-drop-table --extended-insert --quick"
[ ${is_replication} -eq 1 ] && params="${params} --master-data=2"
name=`echo $dbname | tr " " "_"` ### pass "dbname tblname" -> backup table in a db -> dbname_tblname.dump
echo "" > /tmp/${name}.dump.log
mysqldump -u ${username} -p -h ${host} ${params} ${dbname} --log-error=/tmp/${name}.dump.log > ${name}.dump
