backend php.ini
```
max_execution_time = 300
```

backend www.conf
```
request_terminate_timeout = 300
```

backend nginx.conf
```
location ~ \.php$ {
  ...
  fastcgi_read_timeout 300;
  ...
}
```

proxy nginx.conf
```
location / {
    proxt_pass ...
    ...
    proxy_connect_timeout       300;
    proxy_send_timeout          300;
    proxy_read_timeout          300;
    send_timeout                300;
    ...
}
```

systemctl restart nginx
systemctl restart php-fpm
