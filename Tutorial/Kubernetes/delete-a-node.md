# Delete a Node

## Environment

Ubuntu 20.04.5 LTS

Kubernetes 1.26.1

## Date

2023-02-02-Thursday.

## Delete a Node

### 1. Drain a node

```Bash
kubectl drain {node_name} # --ignore-daemonsets --delete-local-data
```

### Finally, Delete the Node

```Bash
kubectl delete node {node_name}
```

---

### Reference
- How to gracefully remove a node from Kubernetes?, https://stackoverflow.com/questions/35757620/how-to-gracefully-remove-a-node-from-kubernetes, 2023-02-02-Thu.
