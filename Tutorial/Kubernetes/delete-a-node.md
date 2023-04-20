# Delete a Node

## Environment

- Ubuntu 20.04.5 LTS
  - Kubernetes 1.26.1

- Ubuntu 22.04.2 LTS
  - Kubernetes 1.24.10
  - CRIO 1.24.4

## Date

2023-02-02-Thursday.

2023-04-20-Thursday.

## Delete a Node

### :bulb: TLDR

```Bash
kubectl cordon {node_name}
kubectl drain {node_name} --ignore-daemonsets --delete-local-data
kubectl delete node {node_name}
```

### 1. Mark a Node as Unschedulable 

```Bash
kubectl cordon {node_name}
```

### 2. Drain a Node in Preparation for Maintenance

```Bash
kubectl drain {node_name} --ignore-daemonsets --delete-local-data
```

### 3. Delete the Node

```Bash
kubectl delete node {node_name}
```

---

### Reference
- How to gracefully remove a node from Kubernetes?, https://stackoverflow.com/questions/35757620/how-to-gracefully-remove-a-node-from-kubernetes, 2023-02-02-Thu.
