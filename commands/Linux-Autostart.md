# Ubuntu
```
sudo update-rc.d sonar defaults
```
# Centos 6x
```
sudo chkconfig sonar on
chkconfig --list | grep sonar
```
# Centos 7x
```
sudo systemctl enable sonar
systemctl list-unit-files | grep sonar
```
