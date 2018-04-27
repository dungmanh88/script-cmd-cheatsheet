```
client ---- this-server:this-port --- middle-server ---> remote-server:remote-port
```
# ssh local port tunnel to remote server
```
ssh -L $host:$port:$remote_host:$remote_port $user@$remote_host

$host=127.0.0.1|0.0.0.0
```
# ssh local port tunnel to remote server without execute shell
```
ssh -L $host:$port:$remote_host:$remote_port $user@$remote_host -N
```
# ssh local port tunnel to middle server, from middle server tunnel to remote server without execute shell
```
ssh -L $host:$port:$remote_host:$remote_port $user@$middle_host -N
```
