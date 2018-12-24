openssl rand -base64 20
openssl x509 -in ca.crt -text -noout
openssl rsa  -in ca.key -check
openssl rsa -modulus -noout -in myserver.key | openssl md5
openssl x509 -modulus -noout -in myserver.crt | openssl md5
