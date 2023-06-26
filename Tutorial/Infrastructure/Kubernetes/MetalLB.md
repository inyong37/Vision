# MetalLB

MetalLB hooks into your Kubernetes cluster, and provides a network load-balancer implementation. In short, it allows you to create Kubernetes services of type LoadBalancer in clusters that don’t run on a cloud provider, and thus cannot simply hook into paid products to provide load balancers.

It has two features that work together to provide this service: address allocation, and external announcement.

## Date

2023-06-26-Monday.

## Environment

* Ubuntu 22.04.2 LTS
  * Kubernetes 1.24.10 

## Installation

### 1. Configure `kube-proxy`

```Bash
kubectl edit configmap -n kube-system kube-proxy
```

Change:

```Bash
...
ipvs:
  strictARP: true
...
```

### 2. Install

```Bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.10/config/manifests/metallb-native.yaml
```

### Reference
- MetalLB Installation, https://metallb.universe.tf/installation/, 2023-06-26-Mon.
