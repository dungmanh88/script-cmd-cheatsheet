minikube get-k8s-versions // remove from 0.29.0
minikube start --kubernetes-version="v1.10.0"
minikube ssh
~/.minikube
minikube ip -> get ip of virtualbox vm running k8s
minikube dashboard
minikube delete

kubectl get nodes
kubectl cluster-info
kubectl describe nodes
kubectl run echo --image=gcr.io/google_containers/echoserver:1.4 --port=8080
kubectl get pods
kubectl expose deployment echo --type=NodePort
kubectl get services
kubectl get service echo -o jsonpath='{.spec.ports[0].nodePort}'
kubectl get service echo -o json
kubectl describe service --namespace=kube-system


etcdctl cluster-health
etcdctl member list
etcdctl set test
etcdctl get test

kubectl get namespaces
kubectl get services --namespace kube-system
kubectl get deployments  --namespace kube-system

https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/

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
kubectl create -f busybox.yaml

kubectl exec busybox --namespace=kube-system cat /etc/resolv.conf
kubectl exec busybox --namespace=kube-system -- nslookup kubernetes-dashboard.kube-system.svc.cluster.local

kubectl delete pod busybox -n kube-system
kubectl delete service my-cip-service
kubectl exec -n kube-system -it ubuntu -- /bin/bash

kubectl edit pod pod-name --namespace kube-system
