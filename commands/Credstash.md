# a tool to manage dynamodb and KMS
https://github.com/fugue/credstash

credstash list

credstash -r region -t table-name get key-name
credstash -r region -t table-name get key-name key=value

credstash -r region -t table-name put myapp.db.prod @secret.txt
credstash -r region -t table-name put myapp.db.prod @secret.txt key=value

key=value is encryption context

tr -dc '[:alnum:]' < /dev/urandom | fold -w 32 | head -n 1 | credstash put myapp.db.prod -

credstash  -r region -t table-name put myapp.db.prod value # table-name is on dynamodb
credstash  -r region -t table-name put myapp.db.prod value -v 2 # automatically convert to 0000000000000000002
credstash  -r region -t table-name put -a myapp.db.prod # automatically version increment

credstash  -r region -t table-name get myapp.db.prod # get the latest version
credstash  -r region -t table-name put myapp.db.prod -v 0000000000000000001 # get a specific version, 0000000000000000001 not 1

credstash  -r region -t table-name delete myapp.db.prod # delete all versions of this credential
