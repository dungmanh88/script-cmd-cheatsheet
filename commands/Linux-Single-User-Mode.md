# Go to single user mode
https://www.itzgeek.com/how-tos/linux/centos-how-tos/single-user-mode-in-centos-7-rhel-7.html
go to linux rescue -> e
choose the line has vmlinuz
ro -> rw init=/sysroot/bin/sh
ctrl + x
mount -n -o remount,rw /
visudo
