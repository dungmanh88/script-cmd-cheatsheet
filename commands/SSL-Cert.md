# Check expire certbot
```
openssl x509 -dates -noout < /etc/letsencrypt/live/<domain-name>/fullchain.pem
or
openssl x509 -dates -noout < /etc/letsencrypt/live/<domain-name>/cert.pem
```

# Where certbot store cert and privkey
```
cert
/etc/letsencrypt/live/<domain-name>/fullchain.pem

privkey
/etc/letsencrypt/live/<domain-name>/privkey.pem
```
