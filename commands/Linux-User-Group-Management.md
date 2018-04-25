# Get uid, gid and other group
```
id
uid=0(root) gid=0(root) groups=0(root)

id dungnm
uid=1002(dungnm) gid=1004(dungnm) groups=1004(dungnm),1000(dev)

dungnm has primary group is dungnm (1004)
and also belong to supplementary group dev (1000)
```

# Find all groups that a user belong to
```
groups dungnm
dungnm : dungnm dev
```

# Find all members in a group
```
cat /etc/group | grep dev
dev:x:1000:dungnm,test
```

# sudo usage
```
sudo -i similar sudo su -: Go to root with root shell and go to home of root
sudo -s: Go to root with invoking user's shell and go to home of invoking user
sudo -l: show privileges of current user
sudo su - dungnm: switch to dungnm and act if as dungnm has been logged in.
sudo -u: run commands as an other user
  sudo -u dungnm touch /tmp/1
  sudo su -s /bin/bash -c "touch /tmp/1" dungnm
```

# understanding /etc/passwd
```
dungnm:x:1002:1004::/home/dungnm:/bin/bash

dungnm is username
x is encrypted passwd in /etc/shadow
1002 is uid
1004 is gid of primary group (one account maybe belong many groups)
with normal account uid and gid >= 1000
with system account uid and gid < 1000
/home/dungnm is home folder
/bin/bash is shell
after gid is GECOS field. Now it is empty
```

# understanding /etc/shadow

## remove passwd
```
passwd -d dungnm

It makes /etc/shadow:
dungnm::17646:0:99999:7:::
```

## lock passwd
```
passwd -l dungnm

dungnm:!!:17646:0:99999:7:::  -> lock passwd after remove passwd
dungnm:!!$6$XvhGAeu2$cjD15YckRWi2NtvFRUrZ9Dods9eAhkCofn10SwON6DLwbvSStnygC4fu9hoF/N5SeTNUJwTEkXBIQNF8j6buF.:17646:0:99999:7:::  -> lock passwd

or
usermod -L dungnm
```

## unlock passwd
```
passwd -u dungnm

dungnm:$6$XvhGAeu2$cjD15YckRWi2NtvFRUrZ9Dods9eAhkCofn10SwON6DLwbvSStnygC4fu9hoF/N5SeTNUJwTEkXBIQNF8j6buF.:17646:0:99999:7:::  -> there is no !! in passwd field

or
usermod -U dungnm
```

(lock passwd is meaning the user is impossible to login using passwd but the user may log in by other means)

## disable passwd
```
change passwd field to * in /etc/shadow
dungnm:*:17646:0:99999:7:::
```

(disable account by changing passwd field is meaning the user is impossible to login using passwd but the user may log in by other means)

! or * is invalid character in passwd field in /etc/shadow. Using them is a nice way to lock|disable passwd

# The safest method to disable account completely
```
usermod -s /sbin/nologin dungnm
or
usermod -s /usr/bin/false dungnm

change passwd field to * in /etc/shadow
```
Read the way to disable system account of linux:
```
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
mail:*:17110:0:99999:7:::
```

# understanding /etc/group
```
dev:x:1000:dungnm,test
dev is group name
x is group passwd (never used)
1000 is gid
dungnm, test are two members in group dev
```

# add user
```
useradd test

passwd is locked by default
cat /etc/shadow | grep test
test:!!:17646:0:99999:7:::
```

useradd and adduser is the same in centos but there is a little difference in ubuntu

adduser is more friendly than useradd in ubuntu

# add group, add user to group, and remove user from group
```
groupadd finance
usermod -aG finance dungnm
```

Each user has a primary group.

The parameter -G will add a group as a supplementary group to the user but not replace primary group of the user.

```
gpasswd -d dungnm finance
Removing user dungnm from group finance
```

# remove group
```
groupdel finance

The association between group finanace and user dungnm will be lost

groups dungnm
dungnm : dungnm dev
```

# remove user
```
userdel -r test

The parameter -r will remove:

home folder (/home/test ) and spool mail (/var/spool/mail/test) of user test
```
