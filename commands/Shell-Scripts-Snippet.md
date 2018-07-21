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

# Change shebang line
test.sh
```
#!/bin/bash
echo "hello"
```
chmod u+x test.sh && ./test.sh -> use program in shebang line to run the script

equivalent to bash test.sh
-> change shebang line
```
#!/usr/bin/rm
echo "hello"
```
run shell script -> remove shell script


# conditional
```
[ expression ]
equivalent to
test expression

[ ! expression ]
equivalent to
test ! expression

[ expression1 -o expression2 ]
equivalent to
test expression1 -o expression2

[ expression1 -a expression2 ]
equivalent to
test expression1 -a expression2
```

Test strings
```
[ $USER = "root" ]
[ ! $USER = "root" ]
```

Test empty
```
[ -z $SSH_TTY ] || echo "You are not in ssh session"
[ -n $SSH_TTY ] && echo "You are in ssh session"
```

Test integer
Check total param > 0
```
[ $# -gt 0 ] && echo "You entered param"
```

Test file type
```
[ -d $file ] && echo "This is a dir"
[ -h $file ] && echo "This is a soft link"
[ -e $file ] && echo "This file exists" # check exists, otherwise, check file type
[ -c $file ] && echo "This is a character device"
[ -b $file ] && echo "This is a block device"
[ -p $file ] && echo "This is a pipe"
[ -d $file ] && echo "This is a dir"
[ -f $file ] && echo "This is a file"
[ -r $file ] && echo "This is a readable file"
[ -x $file ] && echo "This is a executable file"
```

```
if [ expression ] ; then
  to do something
fi

if [ expression ] ; then
  to do something
elif [ expression ] ; then
  to do something
else
  to do something
fi
```

# test param empty
```
#!/bin/bash
echo "You are using shell $(basename $0)"
test -z $1 || echo "hello $1"
```
if $1 empty -> true -> not run command list echo
if $1 not empty -> false -> run command list echo

# backup2.sh
```
#!/bin/bash
read -p "Which level you want to compress (H, L, M) ? " level
read -p "Which folder you want to backup to ? " dir

if [ -z $level ] ; then
  echo "You must enter a level"
  exit 1
fi

if [ -z $dir ] ; then
  echo "You must enter a destination dir"
  exit 1
fi

[ -d $HOME/$dir ] || mkdir -m 700 $HOME/$dir
backup_dir=$HOME/$dir

if [ $level = "L" ] ; then
  tar_opt="-cvf $backup_dir/b.tar --exclude $backup_dir $HOME"
elif [ $level = "M" ] ; then
  tar_opt="-cvzf $backup_dir/b.tar.gz --exclude $backup_dir $HOME"
else
  tar_opt="-cvjf $backup_dir/b.tar.bz2 --exclude $backup_dir $HOME"
fi
tar $tar_opt
```
tar.bz2 > tar.gz
-> This script will backup and compress all file and dir in current dir to a backup dir in current dir exclude backup dir from backup progress.

# grade.sh
```
#!/bin/bash

if [ ! $# -eq 2 ] ; then
  echo "You must enter student_name and grade"
  exit 2
fi

case $2 in
  [A-C]|[a-c])
    echo "$1 is super star"
  ;;
  [dD])
    echo "$1 is good"
  ;;
  [E-F]|[e-f])
    echo "$1 is not better"
  ;;
  *)
    echo "Not enough to evaluate"
  ;;
esac
```
case in easc is good for evaluate a range of letter.
