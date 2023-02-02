# Delete a Node on Kubernetes

## Environment

Ubuntu 20.04.5 LTS

Kubernetes 1.26.1

## Date

2023-02-02-Thursday.

## Contents

### 1. Check nodes' name

```Bash
kubectl get nodes
```

### 2. Drain the node

```Bash
kubectl drain {node_name}
```

[Or](https://github.com/inyong37/Vision/blob/master/Troubleshooting/Kubernetes-node-drain.md):

```Bash
kubectl drain {node_name} --ignore-daemonsets --delete-local-data
```

### 3. Delete the node

```Bash
kubectl delete node {node_name}
```

### Finally, reset the cluster's state

```Bash
kubectl reset
```

---

### Reference
- How to gracefully remove a node from Kubernetes?, https://stackoverflow.com/questions/35757620/how-to-gracefully-remove-a-node-from-kubernetes, 2023-02-02-Thu.
