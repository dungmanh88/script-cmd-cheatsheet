put Dockerfile in an empty folder
docker build -t ruby-23-with-sonar-scanner .
docker build --no-cache=true -t ruby-23-with-sonar-scanner .

create docker hub account
naldocker/no-reply@nal.vn

docker login --username=naldocker
docker images
```
REPOSITORY                    TAG                 IMAGE ID            CREATED              SIZE
ruby-23-with-sonar-scanner    latest              c8dbb01d963c        About a minute ago   1.25GB
```
docker tag ruby-23-with-sonar-scanner naldocker/ruby-23-with-sonar-scanner
docker push naldocker/ruby-23-with-sonar-scanner

default latest
