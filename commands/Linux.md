# Get pid
```
Root pid = 0
id
uid=0(root) gid=0(root) groups=0(root)
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
