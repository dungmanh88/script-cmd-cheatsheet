https://github.com/etcd-io/etcd/releases
https://coreos.com/etcd/docs/latest/dev-guide/interacting_v3.html
https://www.digitalocean.com/community/tutorials/how-to-use-etcdctl-and-etcd-coreos-s-distributed-key-value-store

curl -L https://github.com/etcd-io/etcd/releases/download/v3.1.11/etcd-v3.1.11-linux-amd64.tar.gz -o /tmp/etcd.tar.gz


./etcdctl ls / --recursive
./etcdctl --endpoints http://127.0.0.1:2379 ls /

**Use proper version of etcdctl match with etcd**

https://stackoverflow.com/questions/48076272/etcdctl-cant-see-the-key-put-by-go-client
version V3 khong co ls  nua
export ETCDCTL_API=3
./etcdctl get / --prefix --keys-only

./etcdctl put foo bar
./etcdctl get foo
./etcdctl  member list
