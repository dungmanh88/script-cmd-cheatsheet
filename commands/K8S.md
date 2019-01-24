# Minikube
minikube get-k8s-versions // remove from 0.29.0
minikube start --kubernetes-version="v1.10.0"
minikube ssh
~/.minikube
minikube ip -> get ip of virtualbox vm running k8s
minikube dashboard
minikube delete

# Get nodes
kubectl get nodes
kubectl get nodes -o wide
kubectl get nodes -o json
kubectl get nodes -o yaml
kubectl describe nodes
kubectl get no -o json|wide|yaml

# Get overall of cluster
kubectl cluster-info

# Get pods
kubectl get pods -n default (= kubectl get pods)
kubectl get pods -o yaml|wide|json
kubectl get po -n kube-system

kubectl get po -n kube-system --sort-by spec.nodeName -o custom-columns=POD:metadata.name,NODE:spec.nodeName

kubectl get po -n kube-system --sort-by metadata.name -o custom-columns=POD:metadata.name,NODE:spec.nodeName
POD

kubectl delete pod busybox -n kube-system
kubectl edit pod pod-name --namespace kube-system

# Manage service
kubectl get services
kubectl get service echo -o jsonpath='{.spec.ports[0].nodePort}'
kubectl get service echo -o json
kubectl describe service --namespace=kube-system
kubectl get services --namespace kube-system
kubectl get services -o yaml -n kube-system
kubectl delete service my-cip-service

# Get namespace
kubectl get namespaces

# I dont know
kubectl run echo --image=gcr.io/google_containers/echoserver:1.4 --port=8080
kubectl expose deployment echo --type=NodePort

# Debug pods
kubectl describe pod pod-name -n kube-system
kubectl logs <pod-name> -n kube-system
same as
/var/log/pods -> view log in it
or
kubectl logs <pod-name> -n kube-system --previous

# Debug container in a pod
https://stackoverflow.com/questions/45486828/kube-dns-kubedns-dnsmasq-sidecar-fails-to-start
kubectl logs kube-dns-pod-name -n kube-system -c sidecar
kubectl logs kube-dns-pod-name -n kube-system -c kubedns
kubectl logs kube-dns-pod-name -n kube-system -c dnsmasq

# Debug service without exposion
Forward port of a pod
```
kubectl port-forward pod-name host-port:container-port &

curl localhost:host-port
```

# Almanac (like a manual)
kubectl explain pods
kubectl explain pod.spec

# use current context in kubectl, current context declared in kubeconfig ~/.kube/config
kubectl config use-context
kubectl config view - view kubeconfig of kubectl
kubectl config current-context
export KUBECONFIG=$KUBECONFIG:$HOME/.kube/config

##if you want to use another kube config:
kubectl config --kubeconfig=/path/to/config view --flatten|--minify

# Check daemonset
kubectl get ds

check rolling update feature of ds
kubectl get ds/kube-proxy -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}' -n kube-system

# check health of scheduler, controller manager, etcd-xxx
kubectl get cs -n kube-system

# etcdctl
etcdctl cluster-health
etcdctl member list
etcdctl set test
etcdctl get test

# Exec a pod
kubectl exec busybox --namespace=kube-system cat /etc/resolv.conf
kubectl exec busybox --namespace=kube-system -- nslookup kubernetes-dashboard.kube-system.svc.cluster.local

kubectl exec -n kube-system -it ubuntu -- /bin/bash
kubectl exec -n kube-system -it <pod-name> -- sh

# Exec a container in a pod
Mot pod co nhieu container -> exec vao container trong pod nhu the nay nhe
kubectl exec pod-name -c container-name ls /etc/nginx/conf.d

# Start kubectl proxy
```
kubectl proxy --address=0.0.0.0 --port=8001 --accept-hosts='^*$'
```

# Deployments
kubectl get deployments  --namespace kube-system

# Podspec and apply pod spec
```
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: kube-system
spec:
  containers:
  - name: busybox
    image: busybox:1.28
    command:
      - sleep
      - "3600"
    imagePullPolicy: IfNotPresent
  restartPolicy: Always
```
kubectl create/apply/delete -f busybox.yaml


# Cluster role
kubectl get clusterrole
kubectl edit clusterrole <clusterrole>

# Secret
kubectl get secrets --all-namespaces
kubectl delete secret --namespace=kube-system default-xxx

# Link
https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/

show all container in pods
kubectl describe pod/xxx -n default
