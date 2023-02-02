# Drain a Node on Kubernetes

## Environment

Ubuntu 20.04.5 LTS

Kubernetes 1.26.1

## Date

2023-02-02-Thursday.

## Problem

I was trying to delete worker node due to downgrade Kubernetes 1.26.1 to 1.24.0. However, `kubectl drain` get an error as below:

> <img width="1514" alt="Screenshot 2023-02-02 at 2 14 49 PM" src="https://user-images.githubusercontent.com/20737479/216237639-f840ff19-cb70-4e77-86af-5d0484676751.png">

## [Solution](https://stackoverflow.com/questions/35757620/how-to-gracefully-remove-a-node-from-kubernetes)

Add options as below:

```Bash
kubectl drain kubenode01 --ignore-daemonsets
```

> <img width="755" alt="Screenshot 2023-02-02 at 2 15 59 PM" src="https://user-images.githubusercontent.com/20737479/216237794-976aca80-2fdd-4e2b-b697-aee2b0b54d9f.png">

---

### Reference
- How to gracefully remove a node from Kubernetes?, https://stackoverflow.com/questions/35757620/how-to-gracefully-remove-a-node-from-kubernetes, 2023-02-02-Thu.
