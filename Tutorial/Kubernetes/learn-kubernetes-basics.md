# _[Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)_ | [Blog (KR)](https://hyeo-noo.tistory.com/m/362)

## 1. _[Create a Kubernetes cluster](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/)_

```Bash
# Step 1: Cluster up and running
minikube version
minikube start
# Step 2: Cluster version
kubectl version
# Step 3: Cluster details
kubectl cluster-info
kubectl get nodes
```

## 2. _[Deploy an app](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)_

```Bash
# Step 1: kubectl basics
kubectl version
kubectl get nodes
# Step 2: Deploy our app
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
kubectl get deployments
# Step 3: View our app
echo -e "\n\n\n\e[92mStarting Proxy. After starting it will not output a response. Please click the first Terminal Tab\n";
kubectl proxy
curl http://localhost:8001/version
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/ 
```

## 3. _[Explore your app](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/)_

```Bash
# Step 1: Check application configuration
kubectl get pods
kubectl describe pods
# Step 2: Show the app in the terminal
echo -e "\n\n\n\e[92mStarting Proxy. After starting it will not output a response. Please click the first Terminal Tab\n"; kubectl proxy
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/
# Step 3: View the container logs
kubectl logs $POD_NAME
# Step 4: Executing command on the container
kubectl exec $POD_NAME -- env
kubectl exec -ti $POD_NAME -- bash
cat server.js
curl localhost:8080
exit
```
      
## 4. _[Expose your app publicly](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/)_

```Bash
# Step 1: Create a new service
kubectl get pods
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
kubectl get services
kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
curl $(minikube ip):$NODE_PORT
# Step 2: Using labels
kubectl describe deployment
kubectl get pods -l app=kubernetes-bootcamp
kubectl get services -l app=kubernetes-bootcamp
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
kubectl label pods $POD_NAME version=v1
# Step 3 Deleting a service
kubectl delete service -l app=kubernetes-bootcamp
kubectl get services
curl $(minikube ip):$NODE_PORT
kubectl exec -ti $POD_NAME -- curl localhost:8080
```
      
## 5. _[Scale up your app](https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/)_

```bash
# Step 1: Scaling a deployment
kubectl get deployments
kubectl get rs
kubectl scale deployments/kubernetes-bootcamp --replicas=4
kubectl get deployments
kubectl get pods -o wide
kubectl describe deployments/kubernetes-bootcamp
# Step 2: Load Balancing
kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
curl $(minikube ip):$NODE_PORT
# Step 3: Scale Down
kubectl scale deployments/kubernetes-bootcamp --replicas=2
kubectl get deployments
kubectl get pods -o wide
```
      
## 6. _[Update your app](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)_

```bash
# Step 1: Update the version of the app
kubectl get deployments
kubectl get pods
kubectl describe pods
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
kubectl get pods
# Step 2: Verify an update
kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
curl $(minikube ip):$NODE_PORT
kubectl rollout status deployments/kubernetes-bootcamp
kubectl describe pods
# Step 3: Rollback an update
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10
kubectl get deployments
kubectl get pods
kubectl describe pods
kubectl rollout undo deployments/kubernetes-bootcamp
kubectl get pods
kubectl describe pods
```
      
---

### Reference
- Learn Kubernetes Basics, https://kubernetes.io/docs/tutorials/kubernetes-basics/, 2022-11-22-Tue.
