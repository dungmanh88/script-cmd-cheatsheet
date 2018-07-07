# Create app-user and www-data user
```
useradd app-user
usermod -s /sbin/nologin app-user
passwd -l app-user
```

# Assign permission for webapp
```
find /path/to/vhost/document/root -type f -exec chmod 664 {} \;
find /path/to/vhost/document/root -type d -exec chmod 775 {} \;

/path/to/vhost/document/root = /var/www/webapp
```

# Assign owner for webapp
```
chown -R app-user:app-user /path/to/vhost/document/root

/path/to/vhost/document/root = /var/www/webapp
```

# Add user into group
```
usermod -aG app-user nginx
usermod -aG app-user apache
```

You should use app-user for all webapp because it is better if you run as app-user. Every file you create will have owner: app-user:app-user
