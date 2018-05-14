# Create app-user and www-data user
```
useradd app-user
useradd www-data
usermod -s /sbin/nologin www-data
passwd -l app-user
```

# Assign permission for webapp
```
find /path/to/vhost/document/root -type f -exec chmod 664 {} \;
find /path/to/vhost/document/root -type d -exec chmod 775 {} \;

/path/to/vhost/document/root = /var/www/app-user  
```

# Assign owner for webapp
```
chown -R app-user:www-data /path/to/vhost/document/root

/path/to/vhost/document/root = /var/www/app-user
```

# Add user into group
```
usermod -aG www-data nginx
usermod -aG www-data apache
```
