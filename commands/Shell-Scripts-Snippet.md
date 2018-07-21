```
test -d $HOME/bin || mkdir $HOME/bin
```

Run command 2 only if command 1 failed
```
command 1 || command 2
```

Run command 2 only if command 1 successful
```
command 1 && command 2
```

Set exit status
```
exit 0
```

Get exit status
```
echo $?
```

Append path to $PATH
```
export PATH=$PATH:<new-path>
```

Get all script name in $PATH
For your information, you also have duplicated script name in many different path in $PATH.
You can check:
```
[root@vagrant-box tmp]# type -a zeno.sh
zeno.sh is /usr/local/bin/zeno.sh  -> this is first match in searching $PATH
zeno.sh is ./zeno.sh
```

# Using param in shell script
Source code:
```
cat zeno.sh
#!/bin/bash
echo "Hello $1"
echo "\n"
echo "Hello $0"
echo "\n"
echo "Hello $(basename $0)"
echo "\n"
echo "$*"
echo "\n"
echo "count = $#"
echo "\n"
echo "${10}"
```
Output:
```
bash zeno.sh fred tom peter lena legolas galdaf angel toma linus elon molly
Hello fred
\n
Hello /tmp/zeno.sh
\n
Hello zeno.sh
\n
fred tom peter lena legolas galdaf angel toma linus elon molly
\n
count = 11
\n
elon
```

$1 is first param

${10} is tenth param, use when two or more digits are needed to represent position.

$* all params

$# total of params

$0 is full file name

$(basename $0) is file name


# Using double quote vs single quote:
```
#!/bin/bash
echo "Hello \$1"
echo "\n"
echo 'Hello $1'
echo "\n"
echo "Hello $1"
echo "\n"
```
Output
```
/tmp/zeno.sh fred tom peter lena legolas galdaf angel toma linus elon molly
Hello $1
\n
Hello $1
\n
Hello fred
\n
```

# Debug
bash -x or bash -v

# New line
```
echo -n "Do not print trailing newline"
echo -e "Allow escape sequence to add to string\n"
```
By default, echo always has a built-in trailing newline
-> you can take the built-in feature to add new line
just use `echo`

# Read user data
```
#!/bin/bash
read -p "May I ask your name: " name
echo "Hello $name"
exit 0
```
read -p will prompt a message, like "May I ask your name: "

# Read and wait
```
#!/bin/bash
read -p "May I ask your name: " name
echo "Hello $name"
read -n1 -p "Please enter a key to exit"
echo
exit 0
```
echo is just a new line near the bottom of code.

read -n1 will require user to press **one** key stroke.

# Read passwd
```
#!/bin/bash
read -p "May I ask your name: " name
echo "Hello $name"
read -s -p "Your credit accout :)) " account_num
echo
echo "$name has entered account number $account_num"
read -sn1 -p "Please enter a key to exit"
echo
exit 0
```

read -s will hide input.

# Ping count
```
#!/bin/bash
read -p "Enter server you want to watch: " server_name
read -p "How many count you want to watch: " count
ping -c $count $server_name 2>&1 > /dev/null || echo "Server Dead"
```
`2>&1 > /dev/null` is a technique that you want to hide output as well as error of ping command.
The drawback of shell script above: ping return successfully if one of ping is successful. Ping return failed if all ping are failed.


# SSH
```
#!/bin/bash
read -p "Enter your username: " username
read -p "Enter your server name: " server_name
ssh ${username}@$server_name
```
${username} for separating @ char from username

# Mysql
```
#!/bin/bash
read -p "Enter your username: " username
read -sp "Enter your passwd: " passwd
echo
read -p "Enter your db: " db
read -p "Enter your command: " cmd

mysql -u$username -p$passwd $db -e "$cmd"
```
