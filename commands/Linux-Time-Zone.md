# Centos 6
```
cp /etc/localtime /root/old.timezone
rm -rf /etc/localtime
ln -s /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime
```
/etc/sysconfig/clock
```
ZONE="Asia/Ho_Chi_Minh"
```
systemctl restart ntpd
