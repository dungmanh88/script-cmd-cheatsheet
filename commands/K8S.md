minikube get-k8s-versions
minikube start --kubernetes-version="v1.10.0"
minikube ssh
~/.minikube
minikube ip -> get ip of virtualbox vm running k8s
minikube dashboard

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
