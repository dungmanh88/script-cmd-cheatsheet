# How to find out the diff
```
diff -x <exclude-file-1> -x <exclude-file-2> -x <exclude-folder-1> -x <exclude-folder-2> -r <src> <dest>
```

# Set hostname
```
hostnamectl set-hostname web-performance
```

# Send message between accounts in linux
```
write vagrant < message.txt
```
or
```
cat message.txt | write vagrant
```
or
```
echo "test" | write vagrant
```
or
```
write vagrant << EOM
content
EOM
```

# Print multiple lines to file
```
cat << EOF > testfile
content
EOF
```

# Read multiple lines to variables
```
read -r -d '' VAR << EOM
 this is line 1
 this is line 2
 this is line 3
EOM
echo $VAR
this is line 1 this is line 2 this is line 3
```
